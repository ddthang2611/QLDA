import sys
import io
import argparse
import copy
import docx
from docx.shared import Pt, RGBColor
import docx.oxml.simpletypes as st
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

# Bao dam xuat UTF-8 tren moi moi truong Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Ho tro doc cac gia tri font size so thuc trong XML
orig_st_hps = st.ST_HpsMeasure.convert_from_xml
def safe_hps_convert(cls, xml_value):
    try:
        return orig_st_hps(xml_value)
    except ValueError:
        return Pt(float(xml_value) / 2.0)
st.ST_HpsMeasure.convert_from_xml = classmethod(safe_hps_convert)

def copy_rfonts_xml(source_run, target_run):
    """Sao chep the w:rFonts tu run nguon sang run dich de dong bo moi bo go va he thong font."""
    s_rPr = source_run._r.rPr
    if s_rPr is None:
        return
    s_rFonts = s_rPr.find(qn('w:rFonts'))
    if s_rFonts is None:
        return
    
    t_rPr = target_run._r.get_or_add_rPr()
    t_rFonts = t_rPr.find(qn('w:rFonts'))
    if t_rFonts is None:
        t_rFonts = OxmlElement('w:rFonts')
        t_rPr.append(t_rFonts)
    
    for attr in ['ascii', 'hAnsi', 'cs', 'eastAsia']:
        val = s_rFonts.get(qn(f'w:{attr}'))
        if val:
            t_rFonts.set(qn(f'w:{attr}'), val)

def set_explicit_rfonts(target_run, font_name):
    """Thiet lap ro rang w:rFonts cho run voi font_name duoc chi dinh tren moi thuoc tinh."""
    if not font_name:
        return
    t_rPr = target_run._r.get_or_add_rPr()
    t_rFonts = t_rPr.find(qn('w:rFonts'))
    if t_rFonts is None:
        t_rFonts = OxmlElement('w:rFonts')
        t_rPr.append(t_rFonts)
    for attr in ['ascii', 'hAnsi', 'cs', 'eastAsia']:
        t_rFonts.set(qn(f'w:{attr}'), font_name)

def enforce_black_color_and_bold_policy(target_run, is_table_heading=False):
    """
    Ap dung nghiem ngat quy chuan:
    1. 100% mau den (#000000).
    2. Chi Bold neu la Heading cua bang (Hang 0); con lai khong Bold.
    """
    target_run.font.color.rgb = RGBColor(0, 0, 0)
    target_run.bold = is_table_heading

    rPr = target_run._r.get_or_add_rPr()
    
    # Xu ly mau chu trong XML
    c_elem = rPr.find(qn('w:color'))
    if c_elem is None:
        c_elem = OxmlElement('w:color')
        rPr.append(c_elem)
    c_elem.set(qn('w:val'), '000000')

    # Xu ly the Bold trong XML
    b_elem = rPr.find(qn('w:b'))
    bCs_elem = rPr.find(qn('w:bCs'))
    if is_table_heading:
        if b_elem is None:
            rPr.append(OxmlElement('w:b'))
    else:
        if b_elem is not None:
            rPr.remove(b_elem)
        if bCs_elem is not None:
            rPr.remove(bCs_elem)

def copy_run_formatting(source_run, target_run, is_table_heading=False, fallback_font=None, fallback_size=None):
    """Sao chep toan dien dinh dang tu source_run sang target_run bao gom font, size, dong thoi chuan hoa mau den va bold."""
    font_name = source_run.font.name or fallback_font
    if font_name:
        target_run.font.name = font_name
        set_explicit_rfonts(target_run, font_name)
    else:
        copy_rfonts_xml(source_run, target_run)

    if source_run.font.size:
        target_run.font.size = source_run.font.size
    elif fallback_size:
        target_run.font.size = Pt(fallback_size)

    if source_run.italic is not None:
        target_run.italic = source_run.italic

    enforce_black_color_and_bold_policy(target_run, is_table_heading=is_table_heading)

def find_reference_formatting(paragraph, doc=None):
    """Tim kiem dinh dang chuan tu doan van muc tieu hoac cac doan van tuong tu lan can."""
    for r in paragraph.runs:
        if r.font.name or (r._r.rPr is not None and r._r.rPr.find(qn('w:rFonts')) is not None):
            return r

    if doc and paragraph in doc.paragraphs:
        idx = doc.paragraphs.index(paragraph)
        for prev_i in range(idx - 1, -1, -1):
            prev_p = doc.paragraphs[prev_i]
            if prev_p.style.name == paragraph.style.name:
                for r in prev_p.runs:
                    if r.font.name or (r._r.rPr is not None and r._r.rPr.find(qn('w:rFonts')) is not None):
                        return r
        for next_i in range(idx + 1, len(doc.paragraphs)):
            next_p = doc.paragraphs[next_i]
            if next_p.style.name == paragraph.style.name:
                for r in next_p.runs:
                    if r.font.name or (r._r.rPr is not None and r._r.rPr.find(qn('w:rFonts')) is not None):
                        return r

    return None

def find_reference_cell_formatting(cell, table, row_idx, col_idx):
    """Tim kiem dinh dang chuan cho o bang tu cac o cung cot hoac cung hang."""
    for p in cell.paragraphs:
        for r in p.runs:
            if r.font.name or (r._r.rPr is not None and r._r.rPr.find(qn('w:rFonts')) is not None):
                return r

    for r_i in range(len(table.rows)):
        if r_i == row_idx:
            continue
        try:
            other_cell = table.cell(r_i, col_idx)
            for p in other_cell.paragraphs:
                for r in p.runs:
                    if r.font.name or (r._r.rPr is not None and r._r.rPr.find(qn('w:rFonts')) is not None):
                        return r
        except Exception:
            pass

    return None

def replace_exact_text_in_paragraph(paragraph, old_text, new_text, doc=None, is_table_heading=False):
    """Thay the chinh xac van ban trong doan van, chuan hoa mau den va ap dung quy tac bold."""
    if old_text not in paragraph.text:
        return False

    for r in paragraph.runs:
        if old_text in r.text:
            r.text = r.text.replace(old_text, new_text)
            enforce_black_color_and_bold_policy(r, is_table_heading=is_table_heading)
            return True

    ref_run = find_reference_formatting(paragraph, doc)
    saved_font = ref_run.font.name if ref_run else None
    saved_size = ref_run.font.size.pt if (ref_run and ref_run.font.size) else None

    full_text = paragraph.text
    updated_text = full_text.replace(old_text, new_text)

    for r in list(paragraph.runs):
        r._r.getparent().remove(r._r)

    new_r = paragraph.add_run(updated_text)
    if ref_run:
        copy_run_formatting(ref_run, new_r, is_table_heading=is_table_heading, fallback_font=saved_font, fallback_size=saved_size)
    else:
        if saved_font:
            new_r.font.name = saved_font
            set_explicit_rfonts(new_r, saved_font)
        if saved_size:
            new_r.font.size = Pt(saved_size)
        enforce_black_color_and_bold_policy(new_r, is_table_heading=is_table_heading)

    return True

def update_paragraph_content(paragraph, new_text, doc=None):
    """Cap nhat toan bo noi dung mot doan van ngoai bang: chu den 100%, KHONG bold."""
    ref_run = find_reference_formatting(paragraph, doc)

    saved_font = ref_run.font.name if ref_run else None
    saved_size = ref_run.font.size if ref_run else None

    for r in list(paragraph.runs):
        r._r.getparent().remove(r._r)

    new_run = paragraph.add_run(new_text)
    if ref_run:
        copy_run_formatting(ref_run, new_run, is_table_heading=False)
    else:
        if saved_font:
            new_run.font.name = saved_font
            set_explicit_rfonts(new_run, saved_font)
        if saved_size:
            new_run.font.size = saved_size
        enforce_black_color_and_bold_policy(new_run, is_table_heading=False)

    return True

def update_table_cell(table, row_idx, col_idx, new_text):
    """Cap nhat noi dung mot o trong bang: chu den, chi bold neu row_idx == 0."""
    cell = table.cell(row_idx, col_idx)
    ref_run = find_reference_cell_formatting(cell, table, row_idx, col_idx)
    saved_font = ref_run.font.name if ref_run else None
    saved_size = ref_run.font.size if ref_run else None
    is_table_heading = (row_idx == 0)

    while len(cell.paragraphs) > 1:
        p_elem = cell.paragraphs[-1]._p
        p_elem.getparent().remove(p_elem)

    p0 = cell.paragraphs[0]
    for r in list(p0.runs):
        r._r.getparent().remove(r._r)

    new_run = p0.add_run(new_text)
    if ref_run:
        copy_run_formatting(ref_run, new_run, is_table_heading=is_table_heading)
    else:
        if saved_font:
            new_run.font.name = saved_font
            set_explicit_rfonts(new_run, saved_font)
        if saved_size:
            new_run.font.size = saved_size
        enforce_black_color_and_bold_policy(new_run, is_table_heading=is_table_heading)

    return True

def format_basic_table(table, default_font=None):
    """
    Dinh dang bang co ban:
    - 100% border den net don, do day chuan 1pt (val="single", sz="8", color="000000").
    - 100% nen trang thuan tuy (val="clear", fill="FFFFFF").
    - 100% chu mau den (#000000).
    - Chi dong tieu de cua bang (Hang 0) duoc boi dam (bold = True).
    - Cac hang du lieu (Hang >= 1) tuyet doi KHONG boi dam (bold = False).
    """
    tblPr = table._tbl.tblPr
    old_tblBorders = tblPr.find(qn('w:tblBorders'))
    if old_tblBorders is not None:
        tblPr.remove(old_tblBorders)

    # sz="8" la 1pt (1pt = 8 eighths of a pt)
    borders_xml = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:left w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:right w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:insideH w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:insideV w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders_xml)

    for r_idx, row in enumerate(table.rows):
        is_table_heading = (r_idx == 0)

        for cell in row.cells:
            tcPr = cell._tc.get_or_add_tcPr()
            old_shd = tcPr.find(qn('w:shd'))
            if old_shd is not None:
                tcPr.remove(old_shd)
            shd_xml = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="FFFFFF"/>')
            tcPr.append(shd_xml)

            old_tcBorders = tcPr.find(qn('w:tcBorders'))
            if old_tcBorders is not None:
                tcPr.remove(old_tcBorders)

            for p in cell.paragraphs:
                for r in p.runs:
                    enforce_black_color_and_bold_policy(r, is_table_heading=is_table_heading)
                    if default_font:
                        r.font.name = default_font
                        set_explicit_rfonts(r, default_font)

def normalize_all_document_formatting(doc, default_font=None):
    """
    Chuan hoa toan bo tai lieu theo quy chuan bat buoc:
    - 100% chu mau den.
    - Toan bo van ban ngoai bang: KHONG boi dam.
    - Toan bo bang bieu dinh dang co ban: Border den 1pt (sz="8"), nen trang, chi heading bang (Hang 0) moi bold.
    """
    # 1. Chuan hoa cac doan van doc lap ngoai bang: khong bold
    for p in doc.paragraphs:
        for r in p.runs:
            enforce_black_color_and_bold_policy(r, is_table_heading=False)
            if default_font and not r.font.name:
                r.font.name = default_font
                set_explicit_rfonts(r, default_font)

    # 2. Chuan hoa toan bo cac bang bieu: border 1pt, nen trang, bold hang 0
    for t in doc.tables:
        format_basic_table(t, default_font=default_font)

def main():
    parser = argparse.ArgumentParser(description="Tien ich cap nhat va chuan hoa file docx: chu mau den, chi heading bang bold, bang border den 1pt nen trang")
    parser.add_argument("input_file", help="File Word dau vao (.docx)")
    parser.add_argument("--output", "-o", required=True, help="File Word xuat ra sau khi sua")
    parser.add_argument("--replace", "-r", nargs=2, metavar=('OLD', 'NEW'), help="Thay the chuoi van ban cu bang chuoi moi")
    parser.add_argument("--p-index", type=int, help="Chi so doan van can thay the noi dung")
    parser.add_argument("--p-text", type=str, help="Noi dung moi cho doan van p-index")
    parser.add_argument("--cell", nargs=4, metavar=('TABLE_IDX', 'ROW', 'COL', 'NEW_TEXT'), help="Cap nhat noi dung mot o trong bang")
    parser.add_argument("--format-tables", action="store_true", help="Chuyen toan bo bang ve format co ban (border den 1pt, nen trang, chi heading bang bold)")
    parser.add_argument("--normalize-all", action="store_true", help="Chuan hoa toan dien tai lieu: 100% chu den, chi heading bang bold, bang border den 1pt nen trang")
    parser.add_argument("--default-font", default="Times New Roman", help="Font mac dinh dong bo (mac dinh: Times New Roman)")

    args = parser.parse_args()

    doc = docx.Document(args.input_file)
    modified = False

    if args.normalize_all:
        normalize_all_document_formatting(doc, default_font=args.default_font)
        print("[+] Da chuan hoa toan dien tai lieu: 100% chu den, chi heading bang bold, bang border den 1pt nen trang")
        modified = True

    if args.format_tables and not args.normalize_all:
        for idx, t in enumerate(doc.tables):
            format_basic_table(t, default_font=args.default_font)
        print(f"[+] Da dinh dang {len(doc.tables)} bang ve format co ban (border den 1pt, nen trang, chi heading bang bold)")
        modified = True

    if args.replace:
        old_txt, new_txt = args.replace
        count = 0
        for p in doc.paragraphs:
            if old_txt in p.text:
                if replace_exact_text_in_paragraph(p, old_txt, new_txt, doc, is_table_heading=False):
                    count += 1
        for t in doc.tables:
            for r_idx, row in enumerate(t.rows):
                is_tbl_heading = (r_idx == 0)
                for cell in row.cells:
                    for p in cell.paragraphs:
                        if old_txt in p.text:
                            if replace_exact_text_in_paragraph(p, old_txt, new_txt, doc, is_table_heading=is_tbl_heading):
                                count += 1
        print(f"[+] Da thay the {count} vi tri xuat hien cua '{old_txt}' bang '{new_txt}'")
        modified = True

    if args.p_index is not None and args.p_text is not None:
        if 0 <= args.p_index < len(doc.paragraphs):
            p = doc.paragraphs[args.p_index]
            update_paragraph_content(p, args.p_text, doc)
            print(f"[+] Da cap nhat doan van #{args.p_index} thanh: \"{args.p_text[:80]}...\"")
            modified = True
        else:
            print(f"[-] Loi: Chi so doan van {args.p_index} vuot qua tong so {len(doc.paragraphs)} doan.")

    if args.cell:
        t_idx, r_idx, c_idx, new_cell_text = int(args.cell[0]), int(args.cell[1]), int(args.cell[2]), args.cell[3]
        if 0 <= t_idx < len(doc.tables):
            table = doc.tables[t_idx]
            update_table_cell(table, r_idx, c_idx, new_cell_text)
            print(f"[+] Da cap nhat o [Bang {t_idx}, Hang {r_idx}, Cot {c_idx}] thanh cong")
            modified = True
        else:
            print(f"[-] Loi: Chi so bang {t_idx} vuot qua tong so {len(doc.tables)} bang.")

    if modified:
        doc.save(args.output)
        print(f"[OK] Tep da duoc luu thanh cong tai: {args.output}")
    else:
        print("[!] Khong co thay doi nao duoc thuc hien.")

if __name__ == '__main__':
    main()
