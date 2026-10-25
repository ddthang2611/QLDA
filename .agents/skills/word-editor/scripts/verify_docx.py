import sys
import io
import argparse
from collections import Counter
import docx
from docx.shared import Pt, RGBColor
import docx.oxml.simpletypes as st
from docx.oxml.ns import qn
from docx.enum.section import WD_ORIENT

# Bảo đảm xuất UTF-8 trên mọi môi trường Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Hỗ trợ đọc các giá trị font size số thực trong XML
orig_st_hps = st.ST_HpsMeasure.convert_from_xml
def safe_hps_convert(cls, xml_value):
    try:
        return orig_st_hps(xml_value)
    except ValueError:
        return Pt(float(xml_value) / 2.0)
st.ST_HpsMeasure.convert_from_xml = classmethod(safe_hps_convert)

def get_doc_defaults(doc):
    """Trích xuất font mặc định và cỡ chữ mặc định từ docDefaults của styles.xml."""
    default_font = None
    default_size = Pt(12) # Chuẩn mặc định Word là 24 half-points = 12pt
    try:
        styles_elm = doc.styles.element
        doc_defaults = styles_elm.find(qn('w:docDefaults'))
        if doc_defaults is not None:
            rpr = doc_defaults.find('.//' + qn('w:rPr'))
            if rpr is not None:
                rfonts = rpr.find(qn('w:rFonts'))
                if rfonts is not None:
                    for attr in ['ascii', 'hAnsi', 'cs']:
                        val = rfonts.get(qn(f'w:{attr}'))
                        if val:
                            default_font = val
                            break
                sz = rpr.find(qn('w:sz'))
                if sz is not None:
                    val = sz.get(qn('w:val'))
                    if val and val.isdigit():
                        default_size = Pt(float(val) / 2.0)
    except Exception:
        pass
    return default_font, default_size

def get_effective_font_name(run, paragraph, default_font=None):
    """Xác định font name hiệu lực của run."""
    if run and run.font.name:
        return run.font.name
    if run and run._r.rPr is not None:
        elem = run._r.rPr.find(qn('w:rFonts'))
        if elem is not None:
            for attr in ['ascii', 'cs', 'hAnsi']:
                val = elem.get(qn(f'w:{attr}'))
                if val:
                    return val
    if paragraph and paragraph.style and paragraph.style.font and paragraph.style.font.name:
        return paragraph.style.font.name
    return default_font

def get_effective_font_size(run, paragraph, default_size=Pt(12)):
    """Xác định cỡ chữ (Pt) hiệu lực của run."""
    if run and run.font.size is not None:
        return run.font.size.pt
    if run and run._r.rPr is not None:
        sz = run._r.rPr.find(qn('w:sz'))
        if sz is not None:
            val = sz.get(qn('w:val'))
            if val and val.isdigit():
                return float(val) / 2.0
    if paragraph and paragraph.style and paragraph.style.font and paragraph.style.font.size is not None:
        return paragraph.style.font.size.pt
    return default_size.pt if hasattr(default_size, 'pt') else default_size

def get_effective_bold(run, paragraph):
    """Xác định thuộc tính in đậm hiệu lực của run."""
    if run and run.bold is not None:
        return run.bold
    if run and run._r.rPr is not None:
        b = run._r.rPr.find(qn('w:b'))
        if b is not None:
            val = b.get(qn('w:val'))
            return val is None or val not in ['0', 'false', 'off']
    if paragraph and paragraph.style and paragraph.style.font and paragraph.style.font.bold is not None:
        return paragraph.style.font.bold
    return False

def get_effective_color(run, paragraph):
    """Xác định mã màu HEX hiệu lực của run."""
    if run and run.font.color and run.font.color.rgb:
        return str(run.font.color.rgb).upper()
    if run and run._r.rPr is not None:
        color_elem = run._r.rPr.find(qn('w:color'))
        if color_elem is not None:
            val = color_elem.get(qn('w:val'))
            if val:
                return val.upper()
    if paragraph and paragraph.style and paragraph.style.font and paragraph.style.font.color and paragraph.style.font.color.rgb:
        return str(paragraph.style.font.color.rgb).upper()
    return "000000"

def inspect_sections_and_tables(doc):
    """Kiểm tra hướng trang và vị trí của các bảng trong tài liệu."""
    section_info = []
    for s_idx, s in enumerate(doc.sections):
        is_landscape = (s.orientation == WD_ORIENT.LANDSCAPE or s.page_width > s.page_height)
        section_info.append({
            'section_index': s_idx,
            'orientation': 'LANDSCAPE' if is_landscape else 'PORTRAIT',
            'width_mm': round(s.page_width.mm, 1),
            'height_mm': round(s.page_height.mm, 1)
        })

    body = doc._body._body
    p_idx = 0
    t_idx = 0
    s_idx = 0
    table_section_map = {}
    for elem in body:
        if elem.tag.endswith('p'):
            pPr = elem.find(qn('w:pPr'))
            if pPr is not None and pPr.find(qn('w:sectPr')) is not None:
                s_idx += 1
            p_idx += 1
        elif elem.tag.endswith('tbl'):
            cols = len(doc.tables[t_idx].columns)
            rows = len(doc.tables[t_idx].rows)
            table_section_map[t_idx] = {
                'section_index': s_idx,
                'columns': cols,
                'rows': rows,
                'orientation': section_info[s_idx]['orientation'] if s_idx < len(section_info) else 'UNKNOWN'
            }
            t_idx += 1

    return section_info, table_section_map

def verify_rules_compliance(doc_path, max_issues=20):
    """
    Kiểm tra toàn diện 4 quy tắc bắt buộc:
    1. Chữ 100% màu đen (RGB 0,0,0 / hex 000000 / AUTO).
    2. Bôi đậm (Bold) chỉ dành cho Heading của Bảng (Hàng 0). Toàn bộ thân bài ngoài bảng và ô dữ liệu bảng tuyệt đối không bôi đậm.
    3. Bảng biểu tuân theo format cơ bản: Border đen 1pt (sz="8"), Nền trắng thuần túy.
    """
    print(f"\n=======================================================")
    print(f"=== KIỂM TRA QUY CHUẨN ĐỊNH DẠNG BẮT BUỘC (RULES AUDIT) ===")
    print(f"  Tệp kiểm tra: {doc_path}")
    print(f"=======================================================")

    doc = docx.Document(doc_path)
    issues = []

    # 1. Kiểm tra các đoạn văn độc lập ngoài bảng
    for p_idx, p in enumerate(doc.paragraphs):
        text = p.text.strip()
        if not text:
            continue

        for r_idx, r in enumerate(p.runs):
            r_text = r.text.strip()
            if not r_text:
                continue

            # Kiểm tra màu chữ
            color = get_effective_color(r, p)
            if color not in ['000000', 'AUTO']:
                issues.append({
                    'category': 'Màu chữ không phải màu đen',
                    'location': f'Đoạn #{p_idx} (Run #{r_idx})',
                    'detail': f'Màu hiện tại: #{color} (Yêu cầu: #000000)',
                    'text': r_text[:50]
                })

            # Kiểm tra quy tắc Bold: Ngoài bảng tuyệt đối KHÔNG bôi đậm
            bold = get_effective_bold(r, p)
            if bold:
                issues.append({
                    'category': 'Vi phạm bôi đậm ngoài bảng (Bold ngoài bảng)',
                    'location': f'Đoạn #{p_idx} [Style: {p.style.name}] (Run #{r_idx})',
                    'detail': 'Bôi đậm chỉ dành riêng cho heading của bảng; đoạn thân bài/tiêu đề ngoài bảng không được bôi đậm',
                    'text': r_text[:50]
                })

    # 2. Kiểm tra các bảng biểu
    for t_idx, t in enumerate(doc.tables):
        # Kiểm tra border của bảng: màu đen và độ dày 1pt (sz="8")
        tblPr = t._tbl.tblPr
        tblBorders = tblPr.find(qn('w:tblBorders'))
        if tblBorders is None:
            issues.append({
                'category': 'Thiếu cấu hình tblBorders',
                'location': f'Bảng #{t_idx}',
                'detail': 'Bảng chưa có cấu hình tblBorders chuẩn 1pt màu đen',
                'text': ''
            })
        else:
            for b_tag in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
                b_elem = tblBorders.find(qn(f'w:{b_tag}'))
                if b_elem is not None:
                    color = b_elem.get(qn('w:color'))
                    sz = b_elem.get(qn('w:sz'))
                    if color and color.upper() not in ['000000', 'AUTO']:
                        issues.append({
                            'category': 'Border bảng không phải màu đen',
                            'location': f'Bảng #{t_idx} (Đường viền: {b_tag})',
                            'detail': f'Màu viền: #{color} (Yêu cầu: #000000)',
                            'text': ''
                        })
                    if sz and sz != '8':
                        issues.append({
                            'category': 'Độ dày border bảng không phải 1pt',
                            'location': f'Bảng #{t_idx} (Đường viền: {b_tag})',
                            'detail': f'Độ dày sz="{sz}" (Yêu cầu sz="8" tương đương 1pt)',
                            'text': ''
                        })

        # Kiểm tra từng ô trong bảng
        for r_idx, row in enumerate(t.rows):
            is_table_heading = (r_idx == 0)

            for c_idx, cell in enumerate(row.cells):
                tcPr = cell._tc.get_or_add_tcPr()
                # Kiểm tra màu nền ô (Shading)
                shd = tcPr.find(qn('w:shd'))
                if shd is not None:
                    fill = shd.get(qn('w:fill'))
                    if fill and fill.upper() not in ['FFFFFF', 'AUTO', 'NONE', 'CLEAR']:
                        issues.append({
                            'category': 'Nền bảng không phải màu trắng',
                            'location': f'Bảng #{t_idx} [Hàng {r_idx}, Cột {c_idx}]',
                            'detail': f'Màu nền: #{fill} (Yêu cầu: nền trắng #FFFFFF hoặc clear)',
                            'text': cell.text.strip()[:40]
                        })

                # Kiểm tra chữ trong ô
                for p_i, p in enumerate(cell.paragraphs):
                    for r_i, r in enumerate(p.runs):
                        r_txt = r.text.strip()
                        if not r_txt:
                            continue

                        # Màu chữ trong bảng
                        color = get_effective_color(r, p)
                        if color not in ['000000', 'AUTO']:
                            issues.append({
                                'category': 'Chữ trong bảng không phải màu đen',
                                'location': f'Bảng #{t_idx} [Hàng {r_idx}, Cột {c_idx}]',
                                'detail': f'Màu chữ: #{color} (Yêu cầu: #000000)',
                                'text': r_txt[:40]
                            })

                        # Bôi đậm trong bảng:
                        # Hàng 0 (Heading bảng) -> BẮT BUỘC BÔI ĐẬM
                        # Hàng >= 1 (Dữ liệu bảng) -> KHÔNG ĐƯỢC BÔI ĐẬM
                        bold = get_effective_bold(r, p)
                        if is_table_heading:
                            if not bold:
                                issues.append({
                                    'category': 'Heading bảng chưa được bôi đậm',
                                    'location': f'Bảng #{t_idx} [Hàng 0, Cột {c_idx}]',
                                    'detail': 'Dòng tiêu đề của bảng bắt buộc phải bôi đậm (Bold = True)',
                                    'text': r_txt[:40]
                                })
                        else:
                            if bold:
                                issues.append({
                                    'category': 'Dữ liệu bảng bị bôi đậm sai quy định',
                                    'location': f'Bảng #{t_idx} [Hàng {r_idx}, Cột {c_idx}]',
                                    'detail': 'Các ô dữ liệu của bảng tuyệt đối không được bôi đậm (Bold = False)',
                                    'text': r_txt[:40]
                                })

    if not issues:
        print("\n[XÁC NHẬN HOÀN TOÀN ĐẠT CHUẨN ĐỊNH DẠNG]:")
        print("  1. 100% font chữ trong tài liệu và bảng biểu là MÀU ĐEN THUẦN TÚY (#000000).")
        print("  2. Bôi đậm (Bold) CHỈ DÀNH CHO HEADING CỦA BẢNG (Hàng 0); thân bài và ô dữ liệu hoàn toàn không bôi đậm.")
        print("  3. 100% Bảng biểu đạt format cơ bản: BORDER ĐEN 1PT (sz=\"8\"), NỀN TRẮNG THUẦN TÚY (#FFFFFF).")
        return True
    else:
        print(f"\n[PHÁT HIỆN {len(issues)} VI PHẠM QUY CHUẨN ĐỊNH DẠNG]:")
        for idx, iss in enumerate(issues[:max_issues]):
            print(f"  {idx+1}. [{iss['category']}] tại {iss['location']}")
            print(f"     Chi tiết: {iss['detail']}")
            if iss['text']:
                print(f"     Đoạn văn: \"{iss['text']}\"")
        if len(issues) > max_issues:
            print(f"  ... và còn {len(issues) - max_issues} vi phạm khác.")
        return False

def verify_document_consistency(doc_path, expected_font=None):
    """Kiểm tra độ nhất quán của font chữ trên toàn bộ tài liệu."""
    doc = docx.Document(doc_path)
    default_font, default_size = get_doc_defaults(doc)
    font_counter = Counter()
    issues = []

    for p in doc.paragraphs:
        for r in p.runs:
            f = get_effective_font_name(r, p, default_font)
            if f:
                font_counter[f] += 1

    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        f = get_effective_font_name(r, p, default_font)
                        if f:
                            font_counter[f] += 1

    dominant_font = expected_font
    if not dominant_font:
        if font_counter:
            dominant_font = font_counter.most_common(1)[0][0]
        else:
            dominant_font = default_font or "Mặc định từ hệ thống theme"

    return dominant_font, font_counter, issues

def verify_against_base(target_path, base_path, max_issues=15):
    """Đối soát tài liệu đã chỉnh sửa so với tài liệu gốc để bảo đảm giữ nguyên 100% tính chất font, cỡ chữ và định dạng."""
    print(f"\n=======================================================")
    print(f"=== ĐỐI SOÁT ĐỊNH DẠNG VÀ TÍNH CHẤT CHỮ VỚI TỆP GỐC ===")
    print(f"  Tệp gốc (Base):   {base_path}")
    print(f"  Tệp đích (Target): {target_path}")
    print(f"=======================================================")

    doc_base = docx.Document(base_path)
    doc_target = docx.Document(target_path)

    base_def_font, base_def_size = get_doc_defaults(doc_base)
    targ_def_font, targ_def_size = get_doc_defaults(doc_target)

    discrepancies = []
    checks_passed = 0

    min_len = min(len(doc_base.paragraphs), len(doc_target.paragraphs))
    for i in range(min_len):
        pb = doc_base.paragraphs[i]
        pt = doc_target.paragraphs[i]

        txt_b = pb.text.strip()
        txt_t = pt.text.strip()

        if pb.style.name != pt.style.name:
            discrepancies.append({
                'type': 'Style đoạn văn',
                'location': f'Đoạn văn #{i}',
                'base': pb.style.name,
                'target': pt.style.name,
                'text': txt_t[:60]
            })

        if pb.alignment != pt.alignment:
            discrepancies.append({
                'type': 'Căn lề đoạn văn',
                'location': f'Đoạn văn #{i}',
                'base': str(pb.alignment),
                'target': str(pt.alignment),
                'text': txt_t[:60]
            })

        if pb.runs and pt.runs:
            rb = pb.runs[0]
            rt = pt.runs[0]

            fb = get_effective_font_name(rb, pb, base_def_font)
            ft = get_effective_font_name(rt, pt, targ_def_font)
            if fb != ft:
                discrepancies.append({
                    'type': 'Font chữ',
                    'location': f'Đoạn văn #{i}',
                    'base': fb or 'Mặc định',
                    'target': ft or 'Mặc định',
                    'text': txt_t[:60]
                })

            sb = get_effective_font_size(rb, pb, base_def_size)
            st = get_effective_font_size(rt, pt, targ_def_size)
            if abs(sb - st) > 0.1:
                discrepancies.append({
                    'type': 'Cỡ chữ (Pt)',
                    'location': f'Đoạn văn #{i}',
                    'base': f'{sb}pt',
                    'target': f'{st}pt',
                    'text': txt_t[:60]
                })

        checks_passed += 1

    # Kiểm tra hướng trang của các bảng nhiều cột
    sec_info, tbl_map = inspect_sections_and_tables(doc_target)
    wide_table_checks = []
    for t_idx, t_info in tbl_map.items():
        cols = t_info['columns']
        orient = t_info['orientation']
        if cols >= 7:
            if orient == 'LANDSCAPE':
                wide_table_checks.append((t_idx, cols, orient, True))
            else:
                wide_table_checks.append((t_idx, cols, orient, False))
                discrepancies.append({
                    'type': 'Hướng trang bảng nhiều cột',
                    'location': f'Bảng #{t_idx} ({cols} cột)',
                    'base': 'Yêu cầu LANDSCAPE (Xoay ngang)',
                    'target': f'{orient} (Dọc)',
                    'text': f'Bảng có {cols} cột cần được xoay ngang để bảo đảm độ rộng cột và tính dễ đọc'
                })

    print(f"\n[*] Đã kiểm tra đối soát {checks_passed} phân vùng đoạn văn tương ứng.")
    print(f"[*] Tình trạng xoay ngang (Landscape) của các bảng nhiều cột (>= 7 cột):")
    for t_idx, cols, orient, ok in wide_table_checks:
        status_txt = "[ĐẠT - XOAY NGANG]" if ok else "[CHƯA ĐẠT - ĐANG DỰNG DỌC]"
        print(f"    - Bảng #{t_idx} ({cols} cột): {orient} -> {status_txt}")

    if not discrepancies:
        print("\n[XÁC NHẬN HOÀN TOÀN HỢP LỆ VỚI BẢN GỐC]")
        return True
    else:
        print(f"\n[PHÁT HIỆN {len(discrepancies)} ĐIỂM SAI KHÁC SO VỚI GỐC]:")
        for idx, d in enumerate(discrepancies[:max_issues]):
            print(f"  {idx+1}. [{d['type']}] tại {d['location']}")
            print(f"     Gốc: {d['base']} <---> Đích: {d['target']}")
            print(f"     Văn bản: \"{d['text']}\"")
        return False

def main():
    parser = argparse.ArgumentParser(description="Kiểm tra, đối soát tính đồng nhất font chữ, màu sắc, bôi đậm heading bảng và border 1pt bảng Word")
    parser.add_argument("file", help="Đường dẫn tệp .docx đích cần kiểm tra")
    parser.add_argument("--base", "-b", help="Đường dẫn tệp .docx gốc để đối soát tính chất phân vùng")
    parser.add_argument("--check-rules", "-c", action="store_true", help="Kiểm tra quy chuẩn: 100% chữ đen, chỉ heading bảng bold, bảng border đen 1pt nền trắng")
    parser.add_argument("--expected-font", "-e", help="Font chủ đạo kỳ vọng (ví dụ: 'Times New Roman')")
    parser.add_argument("--max-issues", "-m", type=int, default=20, help="Số lượng sai khác tối đa cần in chi tiết")

    args = parser.parse_args()

    if args.check_rules:
        verify_rules_compliance(args.file, max_issues=args.max_issues)

    if args.base:
        verify_against_base(args.file, args.base, max_issues=args.max_issues)
    elif not args.check_rules:
        print(f"=== ĐỐI SOÁT ĐỒNG NHẤT FONT TỆP: {args.file} ===")
        dom_font, counter, issues = verify_document_consistency(args.file, expected_font=args.expected_font)
        print(f"[*] Font chủ đạo: '{dom_font}'")
        print(f"[*] Thống kê font: {dict(counter.most_common(5))}")
        verify_rules_compliance(args.file, max_issues=args.max_issues)

if __name__ == '__main__':
    main()
