import sys
import io
import argparse
import copy
import docx
from docx.shared import Pt, RGBColor
import docx.oxml.simpletypes as st
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# Bao dam xuat UTF-8 tren moi moi truong Windows console
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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

def copy_run_formatting(source_run, target_run, fallback_font=None, fallback_size=None):
    """Sao chep toan dien dinh dang tu source_run sang target_run bao gom font, size, style va XML."""
    # 1. Font Name
    font_name = source_run.font.name or fallback_font
    if font_name:
        target_run.font.name = font_name
        set_explicit_rfonts(target_run, font_name)
    else:
        copy_rfonts_xml(source_run, target_run)

    # 2. Font Size
    if source_run.font.size:
        target_run.font.size = source_run.font.size
    elif fallback_size:
        target_run.font.size = Pt(fallback_size)

    # 3. Kieu chu: Bold, Italic, Underline
    if source_run.bold is not None:
        target_run.bold = source_run.bold
    if source_run.italic is not None:
        target_run.italic = source_run.italic
    if source_run.underline is not None:
        target_run.underline = source_run.underline

    # 4. Mau chu
    if source_run.font.color and source_run.font.color.rgb:
        target_run.font.color.rgb = source_run.font.color.rgb

def find_reference_formatting(paragraph, doc=None):
    """Tim kiem dinh dang chuan tu doan van muc tieu hoac cac doan van tuong tu lan can."""
    # 1. Kiem tra run hien co trong chinh doan van
    for r in paragraph.runs:
        if r.font.name or (r._r.rPr is not None and r._r.rPr.find(qn('w:rFonts')) is not None):
            return r

    # 2. Kiem tra doan van lien ke neu co doc
    if doc and paragraph in doc.paragraphs:
        idx = doc.paragraphs.index(paragraph)
        # Kiem tra doan truoc
        for prev_i in range(idx - 1, -1, -1):
            prev_p = doc.paragraphs[prev_i]
            if prev_p.style.name == paragraph.style.name:
                for r in prev_p.runs:
                    if r.font.name or (r._r.rPr is not None and r._r.rPr.find(qn('w:rFonts')) is not None):
                        return r
        # Kiem tra doan sau
        for next_i in range(idx + 1, len(doc.paragraphs)):
            next_p = doc.paragraphs[next_i]
            if next_p.style.name == paragraph.style.name:
                for r in next_p.runs:
                    if r.font.name or (r._r.rPr is not None and r._r.rPr.find(qn('w:rFonts')) is not None):
                        return r

    return None

def find_reference_cell_formatting(cell, table, row_idx, col_idx):
    """Tim kiem dinh dang chuan cho o bang tu cac o cung cot hoac cung hang."""
    # 1. Kiem tra run trong chinh o do
    for p in cell.paragraphs:
        for r in p.runs:
            if r.font.name or (r._r.rPr is not None and r._r.rPr.find(qn('w:rFonts')) is not None):
                return r

    # 2. Kiem tra cac o cung cot o cac hang khac
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

    # 3. Kiem tra cac o cung hang
    row = table.rows[row_idx]
    for c_i, c in enumerate(row.cells):
        if c_i == col_idx:
            continue
        for p in c.paragraphs:
            for r in p.runs:
                if r.font.name or (r._r.rPr is not None and r._r.rPr.find(qn('w:rFonts')) is not None):
                    return r

    return None

def replace_exact_text_in_paragraph(paragraph, old_text, new_text, doc=None):
    """Thay the chinh xac van ban trong doan van, giu nguyen tuyet doi font va style."""
    if old_text not in paragraph.text:
        return False

    # Truong hop don gian: van ban nam gon trong 1 run duy nhat
    for r in paragraph.runs:
        if old_text in r.text:
            r.text = r.text.replace(old_text, new_text)
            return True

    # Truong hop phuc tap: van ban bi ngat qua nhieu run
    ref_run = find_reference_formatting(paragraph, doc)
    saved_font = ref_run.font.name if ref_run else None
    saved_size = ref_run.font.size.pt if (ref_run and ref_run.font.size) else None
    saved_bold = ref_run.bold if ref_run else None
    saved_italic = ref_run.italic if ref_run else None

    full_text = paragraph.text
    updated_text = full_text.replace(old_text, new_text)

    # Xoa toan bo run hien tai
    for r in list(paragraph.runs):
        r._r.getparent().remove(r._r)

    # Tao run moi voi dinh dang tham chieu da duoc bao toan
    new_r = paragraph.add_run(updated_text)
    if ref_run:
        copy_run_formatting(ref_run, new_r, fallback_font=saved_font, fallback_size=saved_size)
    elif saved_font:
        new_r.font.name = saved_font
        set_explicit_rfonts(new_r, saved_font)
        if saved_size:
            new_r.font.size = Pt(saved_size)
        new_r.bold = saved_bold
        new_r.italic = saved_italic

    return True

def update_paragraph_content(paragraph, new_text, doc=None):
    """Cap nhat toan bo noi dung mot doan van, ke thua chinh xac font tu chinh no hoac doan tuong tu."""
    ref_run = find_reference_formatting(paragraph, doc)
    
    # Neu doan co run, luu lai thuoc tinh
    saved_props = {}
    if ref_run:
        saved_props['font_name'] = ref_run.font.name
        saved_props['size'] = ref_run.font.size
        saved_props['bold'] = ref_run.bold
        saved_props['italic'] = ref_run.italic
        saved_props['color'] = ref_run.font.color.rgb if ref_run.font.color else None

    # Xoa cac run cu
    for r in list(paragraph.runs):
        r._r.getparent().remove(r._r)

    new_run = paragraph.add_run(new_text)
    if ref_run:
        copy_run_formatting(ref_run, new_run)
    elif saved_props.get('font_name'):
        new_run.font.name = saved_props['font_name']
        set_explicit_rfonts(new_run, saved_props['font_name'])
        if saved_props.get('size'):
            new_run.font.size = saved_props['size']
        new_run.bold = saved_props.get('bold')
        new_run.italic = saved_props.get('italic')
        if saved_props.get('color'):
            new_run.font.color.rgb = saved_props['color']

    return True

def update_table_cell(table, row_idx, col_idx, new_text):
    """Cap nhat noi dung mot o trong bang, kiem tra va dong bo font voi cac o tuong tu."""
    cell = table.cell(row_idx, col_idx)
    ref_run = find_reference_cell_formatting(cell, table, row_idx, col_idx)
    
    # Xoa cac doan cu tru doan dau tien
    while len(cell.paragraphs) > 1:
        p_elem = cell.paragraphs[-1]._p
        p_elem.getparent().remove(p_elem)

    p0 = cell.paragraphs[0]
    for r in list(p0.runs):
        r._r.getparent().remove(r._r)

    new_run = p0.add_run(new_text)
    if ref_run:
        copy_run_formatting(ref_run, new_run)
    return True

def main():
    parser = argparse.ArgumentParser(description="Tien ich cap nhat van ban va bang trong file docx voi do chinh xac font tuyet doi")
    parser.add_argument("input_file", help="File Word dau vao (.docx)")
    parser.add_argument("--output", "-o", required=True, help="File Word xuat ra sau khi sua")
    parser.add_argument("--replace", "-r", nargs=2, metavar=('OLD', 'NEW'), help="Thay the chuoi van ban cu bang chuoi moi")
    parser.add_argument("--p-index", type=int, help="Chi so doan van can thay the noi dung")
    parser.add_argument("--p-text", type=str, help="Noi dung moi cho doan van p-index")
    parser.add_argument("--cell", nargs=4, metavar=('TABLE_IDX', 'ROW', 'COL', 'NEW_TEXT'), help="Cap nhat noi dung mot o trong bang")

    args = parser.parse_args()

    doc = docx.Document(args.input_file)
    modified = False

    if args.replace:
        old_txt, new_txt = args.replace
        count = 0
        for p in doc.paragraphs:
            if old_txt in p.text:
                if replace_exact_text_in_paragraph(p, old_txt, new_txt, doc):
                    count += 1
        for t in doc.tables:
            for row in t.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        if old_txt in p.text:
                            if replace_exact_text_in_paragraph(p, old_txt, new_txt, doc):
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
        print(f"[OK] Tep da duoc luu tai: {args.output}")
    else:
        print("[!] Khong co thay doi nao duoc thuc hien.")

if __name__ == '__main__':
    main()
