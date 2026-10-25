---
name: word-editor
description: >-
  Chỉnh sửa, cập nhật và chuẩn hóa tài liệu Microsoft Word (.docx). Bắt buộc 100% font chữ màu đen. Bảng dùng format cơ bản với border đen 1pt (sz="8") và nền trắng thuần túy. Bôi đậm (Bold) chỉ dành cho heading của bảng (dòng tiêu đề bảng), toàn bộ nội dung thân bài và các ô dữ liệu tuyệt đối không bôi đậm. Kế thừa chuẩn xác font chữ, cỡ chữ, căn lề và đồng bộ thuộc tính OpenXML rFonts. Bảo đảm tính toàn vẹn và trang trọng tuyệt đối của tài liệu.
---

# Kỹ Năng Chỉnh Sửa Tài Liệu Word Chuẩn Định Dạng (Word Editor)

Kỹ năng này trang bị quy trình, công cụ và kỹ thuật lập trình chuyên sâu giúp chỉnh sửa, cập nhật và chuẩn hóa tệp tài liệu Microsoft Word (.docx) bảo đảm tính nhất quán, chuyên nghiệp và tuân thủ nghiêm ngặt thể thức tài liệu trang trọng.

---

## 1. Bốn Quy Tắc Định Dạng Cốt Lõi Bắt Buộc

Mọi thao tác tạo mới hoặc chỉnh sửa tệp Word phải tuân thủ nghiêm ngặt bốn quy tắc định dạng bất di bất dịch sau:

### 1.1 Font chữ 100% màu đen thuần túy
- **Toàn bộ văn bản bắt buộc dùng màu đen**: Tất cả các ký tự trong tài liệu (bao gồm nội dung thuyết minh thân bài, toàn bộ ô trong bảng biểu, tiêu đề, danh sách liệt kê, chú thích) chỉ được sử dụng màu đen thuần túy (Mã màu `#000000`, RGB `0, 0, 0` hoặc thẻ XML `<w:color w:val="000000"/>` / `<w:color w:val="auto"/>`).
- **Nghiêm cấm dùng màu trang trí**: Tuyệt đối không dùng màu xanh navy, xanh lam, đỏ, xám hay bất kỳ màu sắc nào khác cho chữ.

### 1.2 Bôi đậm (Bold) chỉ dành cho Heading của Bảng
- **Đặc quyền bôi đậm dành riêng cho Heading của bảng**: Duy nhất dòng tiêu đề của bảng (hàng đầu tiên / table header row) mới được áp dụng in đậm (`bold = True`, thẻ XML `<w:b/>`).
- **Không bôi đậm nội dung thân bài và các phần còn lại**:
  - Toàn bộ nội dung văn bản ngoài bảng (thân bài thuyết minh, Normal, Body Text, các tiêu đề của file...) tuyệt đối không bôi đậm.
  - Toàn bộ các ô dữ liệu trong bảng (từ hàng thứ hai trở đi) tuyệt đối không bôi đậm (`bold = False`).
  - Danh sách liệt kê, chú thích, ghi chú tuyệt đối không bôi đậm.
  - Nghiêm cấm bôi đậm tùy tiện các từ khóa, cụm từ hoặc số liệu nằm giữa câu văn thuyết minh hay ô dữ liệu.

### 1.3 Bảng dùng format cơ bản: Border đen 1pt, Nền trắng
Toàn bộ bảng biểu trong tài liệu bắt buộc sử dụng định dạng cơ bản, rõ ràng và trang trọng:
- **Border đen 1pt**: 100% các đường viền bao quanh (top, bottom, left, right) và các đường phân cách bên trong (insideH, insideV) đều là đường viền nét đơn màu đen với độ dày chuẩn **1pt** (`w:val="single"`, mã màu `w:color="000000"`, kích thước `w:sz="8"` - trong OpenXML, đơn vị là 1/8 pt nên 1pt = 8).
- **Nền trắng thuần túy**: Nền của bảng và toàn bộ các ô bắt buộc là nền trắng (`#FFFFFF` hoặc thẻ XML `<w:shd w:val="clear" w:color="auto" w:fill="FFFFFF"/>`).
- **Nghiêm cấm màu nền trang trí**: Tuyệt đối không tô màu nền cho dòng tiêu đề bảng (header shading), không tô xám, không đổ màu xen kẽ giữa các dòng (zebra striping), không sử dụng các mẫu bảng trang trí lòe loẹt.
- **Format của bảng đồng bộ màu đen**: Toàn bộ chữ và đường viền trong bảng đều là màu đen.

### 1.4 Kế thừa font, kích thước và đồng bộ OpenXML rFonts
- **Kế thừa font chuẩn xác**: Kế thừa font chữ chủ đạo của tài liệu (ví dụ: Times New Roman, Calibri...). Đồng bộ đầy đủ thuộc tính `ascii`, `hAnsi`, `cs` trong thẻ `w:rFonts` để tránh nhảy font tiếng Việt.
- **Cỡ chữ chuẩn 12pt**: Thân bài thuyết minh sử dụng cỡ chữ 12pt (dãn dòng 1.15 đến 1.25, cách đoạn sau 3pt đến 4pt). Cỡ chữ trong bảng từ 10pt đến 12pt nhưng đồng nhất và không dưới 10pt.
- **Khoanh vùng can thiệp tối thiểu**: Chỉ tác động chính xác vào vị trí mục tiêu được chỉ định; giữ nguyên vẹn 100% cấu trúc, căn lề và các nội dung khác.
- **Quy chuẩn viết hoa tiếng Việt hành chính**: Không viết hoa tùy tiện danh từ chung giữa câu; chỉ viết hoa đầu câu/đầu dòng và danh từ riêng.

---

## 2. Quy Trình 5 Bước Chỉnh Sửa Tài Liệu Word

```
[1. Khảo sát Tài liệu] ──► Chạy inspect_docx.py để xác định font chủ đạo và các vị trí cần sửa
          │
          ▼
[2. Xác định Phần tử Tương tự] ──► Định vị ô tiêu đề bảng, ô dữ liệu bảng hoặc đoạn văn lân cận
          │
          ▼
[3. Trích xuất & Chuẩn hóa Định dạng] ──► Màu đen 100%, Border 1pt (sz="8"), nền trắng, chỉ Bold Heading bảng
          │
          ▼
[4. Thực thi Chỉnh sửa An toàn] ──► Sử dụng patch_docx.py hoặc áp dụng mã Python chuẩn hóa
          │
          ▼
[5. Đối soát Nghiệm thu Toàn diện] ──► Chạy verify_docx.py kiểm tra font, màu sắc, bold và table format
```

### Bước 1: Khảo sát và thanh tra hiện trạng tài liệu
Sử dụng công cụ thanh tra để quét toàn bộ tài liệu:
```powershell
.venv\Scripts\python .agents/skills/word-editor/scripts/inspect_docx.py "duong_dan_tep.docx" --summary
```
Tìm kiếm vị trí đoạn văn hoặc ô bảng chứa từ khóa cần chỉnh sửa:
```powershell
.venv\Scripts\python .agents/skills/word-editor/scripts/inspect_docx.py "duong_dan_tep.docx" --search "từ khóa"
```

### Bước 2: Xác định loại phần tử và quy tắc áp dụng
- **Nếu là Heading của Bảng (Hàng 0 của bảng)**: Áp dụng font chủ đạo, màu đen thuần túy (`#000000`), in đậm (`bold = True`).
- **Nếu là Ô dữ liệu của Bảng (Hàng từ 1 trở đi)**: Áp dụng font chủ đạo, màu đen thuần túy (`#000000`), KHÔNG in đậm (`bold = False`).
- **Nếu là Văn bản thân bài ngoài bảng**: Áp dụng font chủ đạo, cỡ chữ 12pt, màu đen thuần túy (`#000000`), KHÔNG in đậm (`bold = False`).

### Bước 3: Trích xuất và thiết lập thuộc tính chuẩn hóa
Thu thập và chuẩn hóa trọn bộ thuộc tính định dạng:
- Font Name: Gán từ font chủ đạo và đồng bộ `w:rFonts` (`ascii`, `hAnsi`, `cs`, `eastAsia`).
- Font Size: 12pt cho thân bài; 10pt - 12pt cho bảng biểu.
- Color: Bắt buộc `RGBColor(0, 0, 0)` hoặc hex `000000`.
- Border bảng: Bắt buộc nét đơn màu đen, độ dày 1pt (`w:sz="8"`).
- Nền bảng: Bắt buộc nền trắng (`#FFFFFF` / `clear`).
- Bold: Bắt buộc `True` DUY NHẤT cho dòng heading của bảng; bắt buộc `False` cho mọi nội dung khác.

### Bước 4: Thực thi chỉnh sửa bằng công cụ hoặc mã Python
- Thay thế chuỗi văn bản an toàn (tự động áp dụng chuẩn màu đen và quy tắc bold):
```powershell
.venv\Scripts\python .agents/skills/word-editor/scripts/patch_docx.py "input.docx" -o "output.docx" -r "nội dung cũ" "nội dung mới"
```
- Chuẩn hóa toàn bộ bảng về format cơ bản (border đen 1pt, nền trắng, chữ đen, bold chỉ ở heading bảng):
```powershell
.venv\Scripts\python .agents/skills/word-editor/scripts/patch_docx.py "input.docx" -o "output.docx" --format-tables
```
- Chuẩn hóa toàn diện định dạng văn bản (100% chữ đen, chỉ heading bảng mới bold, bảng border đen 1pt nền trắng):
```powershell
.venv\Scripts\python .agents/skills/word-editor/scripts/patch_docx.py "input.docx" -o "output.docx" --normalize-all
```

### Bước 5: Đối soát nghiệm thu sau khi chỉnh sửa
Chạy công cụ đối soát để kiểm tra toàn diện tính tuân thủ:
```powershell
.venv\Scripts\python .agents/skills/word-editor/scripts/verify_docx.py "output.docx" --check-rules
```
Đối soát so với tệp gốc để bảo đảm không bị nhảy font hoặc sai lệch cấu trúc ngoài ý muốn:
```powershell
.venv\Scripts\python .agents/skills/word-editor/scripts/verify_docx.py "output.docx" --base "input.docx"
```

---

## 3. Hướng Dẫn Kỹ Thuật Lập Trình Python-docx Chuẩn Mực

### 3.1 Hàm chuẩn hóa Bảng biểu về Format Cơ Bản (Border đen 1pt, Nền trắng, Chữ đen, Bold chỉ ở Heading bảng)

```python
import docx
from docx.shared import Pt, RGBColor
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import qn, nsdecls

def format_basic_black_white_table(table, default_font="Times New Roman", font_size_pt=11):
    """
    Format bang co ban:
    - 100% border den net don, do day 1pt (w:sz="8", w:color="000000").
    - 100% nen trang thuan tuy (val="clear", fill="FFFFFF").
    - 100% chu mau den (#000000).
    - Chi dong tieu de cua bang (Hang 0) duoc boi dam (bold = True).
    - Cac hang du lieu (Hang >= 1) tuyet doi KHONG boi dam (bold = False).
    """
    tblPr = table._tbl.tblPr
    
    # 1. Thiet lap Border den 1pt (sz="8") cho toan bo bang
    old_tblBorders = tblPr.find(qn('w:tblBorders'))
    if old_tblBorders is not None:
        tblPr.remove(old_tblBorders)
    
    # sz="8" tuong ung voi 1pt (1pt = 8 eighths of a point)
    tblBorders_xml = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:left w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:right w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:insideH w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:insideV w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders_xml)

    # 2. Duyet tung hang: dat nen trang, chu mau den va phan dinh bold
    for r_idx, row in enumerate(table.rows):
        # Hang 0 la heading cua bang -> bold = True; cac hang du lieu -> bold = False
        is_table_heading = (r_idx == 0)
        
        for cell in row.cells:
            tcPr = cell._tc.get_or_add_tcPr()
            
            # Xoa shd cu (neu co mau nen)
            old_shd = tcPr.find(qn('w:shd'))
            if old_shd is not None:
                tcPr.remove(old_shd)
            # Thiet lap nen trang thuan tuy
            shd_xml = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="FFFFFF"/>')
            tcPr.append(shd_xml)
            
            # Xoa tcBorders rieng de dung chung tblBorders 1pt dong nhat
            old_tcBorders = tcPr.find(qn('w:tcBorders'))
            if old_tcBorders is not None:
                tcPr.remove(old_tcBorders)

            # Chuan hoa toan bo doan van va run trong o
            for p in cell.paragraphs:
                for r in p.runs:
                    # Mau chu bat buoc mau den
                    r.font.color.rgb = RGBColor(0, 0, 0)
                    # Chi boi dam cho heading cua bang
                    r.bold = is_table_heading
                    
                    # Dong bo the XML
                    if r._r.rPr is not None:
                        b_elem = r._r.rPr.find(qn('w:b'))
                        bCs_elem = r._r.rPr.find(qn('w:bCs'))
                        if is_table_heading:
                            if b_elem is None:
                                r._r.rPr.append(OxmlElement('w:b'))
                        else:
                            if b_elem is not None:
                                r._r.rPr.remove(b_elem)
                            if bCs_elem is not None:
                                r._r.rPr.remove(bCs_elem)

                        color_elem = r._r.rPr.find(qn('w:color'))
                        if color_elem is not None:
                            color_elem.set(qn('w:val'), '000000')
                    
                    # Dong bo font name va rFonts
                    if default_font:
                        r.font.name = default_font
                        rPr = r._r.get_or_add_rPr()
                        rFonts = rPr.find(qn('w:rFonts'))
                        if rFonts is None:
                            rFonts = OxmlElement('w:rFonts')
                            rPr.append(rFonts)
                        for attr in ['ascii', 'hAnsi', 'cs', 'eastAsia']:
                            rFonts.set(qn(f'w:{attr}'), default_font)
                    
                    if font_size_pt and not r.font.size:
                        r.font.size = Pt(font_size_pt)
```

### 3.2 Hàm chuẩn hóa Đoạn văn Ngoài Bảng (Thân bài và Thuyết minh)
Văn bản ngoài bảng: Màu đen 100%, tuyệt đối KHÔNG bôi đậm:

```python
def apply_standard_run_formatting(target_run, font_name="Times New Roman", font_size_pt=12):
    """
    Thiet lap chuan hoa cho van ban ngoai bang:
    - Mau chu: 100% mau den (#000000).
    - Bold: False (Khong boi dam; bôi dam chi danh cho heading cua bang).
    - Dong bo OpenXML rFonts.
    """
    target_run.font.name = font_name
    if font_size_pt:
        target_run.font.size = Pt(font_size_pt)
        
    target_run.font.color.rgb = RGBColor(0, 0, 0)
    target_run.bold = False
    
    rPr = target_run._r.get_or_add_rPr()
    
    # Xoa bo the bold khoi XML neu co
    b_elem = rPr.find(qn('w:b'))
    if b_elem is not None:
        rPr.remove(b_elem)
    bCs_elem = rPr.find(qn('w:bCs'))
    if bCs_elem is not None:
        rPr.remove(bCs_elem)
            
    # Thiet lap mau den trong XML
    color_elem = rPr.find(qn('w:color'))
    if color_elem is None:
        color_elem = OxmlElement('w:color')
        rPr.append(color_elem)
    color_elem.set(qn('w:val'), '000000')
    
    # Dong bo the rFonts
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    for attr in ['ascii', 'hAnsi', 'cs', 'eastAsia']:
        rFonts.set(qn(f'w:{attr}'), font_name)
```

### 3.3 Quy Chuẩn Thể Thức Văn Bản Hành Chính và Văn Bản Trang Trọng
Áp dụng bắt buộc cho toàn bộ tài liệu dự án, hợp đồng kinh tế, hồ sơ thầu, quyết định, biên bản nghiệm thu:
1. **Màu sắc chữ**: 100% văn bản sử dụng màu đen thuần túy (`#000000`, RGB `0, 0, 0`). Tuyệt đối không dùng màu khác.
2. **Quy tắc Bold dành riêng cho Heading của Bảng**: Bôi đậm chỉ dành cho dòng tiêu đề của bảng (hàng đầu tiên). Toàn bộ nội dung thân bài ngoài bảng và các ô dữ liệu trong bảng tuyệt đối không bôi đậm.
3. **Format bảng cơ bản**: Border đen nét đơn độ dày **1pt** (`w:sz="8"`), nền trắng thuần túy. Tuyệt đối không tô màu nền tiêu đề bảng, không tô xám, không đổ sọc xen kẽ.
4. **Cỡ chữ nội dung thuyết minh**: Nội dung thuyết minh sử dụng cỡ chữ 12pt (căn đều hai lề, dãn dòng 1.15 đến 1.25 dòng, cách đoạn sau từ 3pt đến 4pt).
5. **Quy chuẩn canh lề trang (Page Margins theo thể thức hành chính)**:
   - Lề trên (Top margin): **25 mm** (khoảng 0.98 inch).
   - Lề dưới (Bottom margin): **20 mm** (khoảng 0.79 inch).
   - Lề trái (Left margin): **30 mm** (khoảng 1.18 inch).
   - Lề phải (Right margin): **20 mm** (khoảng 0.79 inch).
6. **Xoay ngang trang cho bảng nhiều cột**: Các bảng có từ 7 cột trở lên bắt buộc đặt trong Section xoay ngang trang (Landscape) để bảo đảm độ rộng cột và tính dễ đọc.
7. **Hạn chế tối đa dấu ngoặc đơn**: Tuyệt đối không dùng dấu ngoặc đơn để chú thích hoặc giải thích thuật ngữ thông thường. Hướng tới đối tượng chuyên gia, diễn đạt trực tiếp, gãy gọn và tự nhiên.
8. **Quy chuẩn viết hoa tiếng Việt hành chính**:
   - Tuyệt đối không viết hoa tùy tiện các danh từ chung giữa câu.
   - Chỉ viết hoa chữ cái đầu dòng, đầu câu hoặc đầu các điểm liệt kê.
   - Chỉ viết hoa danh từ riêng: Tên người (Yamada), tên địa danh (Hà Nội, Việt Nam), tên cơ quan, tổ chức cụ thể (Công ty Cổ phần ABC Wear), tên sản phẩm/công nghệ riêng biệt (PostgreSQL, Redis, Elasticsearch, Docker).

---

## 4. Bảng Kiểm Tra Chất Lượng Nghiệm Thu (Quality Checklist)

Trước khi xác nhận hoàn thành công việc chỉnh sửa tệp Word, bắt buộc rà soát toàn bộ các tiêu chí trong bảng sau:

| STT | Tiêu chí Kiểm tra | Yêu cầu Chuẩn hóa Nghiêm ngặt | Trạng thái Đạt |
|:---:|---|---|---|
| 1 | Khoanh vùng đúng phạm vi yêu cầu | Chỉ tác động đúng đoạn văn hoặc ô bảng được chỉ định; tuyệt đối không can thiệp ngoài phạm vi | Đúng 100% tọa độ |
| 2 | Màu chữ 100% màu đen | Toàn bộ chữ trong văn bản, tiêu đề và bảng biểu đều mang mã màu `#000000` / RGB `0, 0, 0` | Không có chữ màu khác |
| 3 | Bôi đậm chỉ dành cho Heading Bảng | Chỉ có dòng tiêu đề của bảng (Hàng 0) mới được in đậm. Thân bài và ô dữ liệu bảng đều KHÔNG in đậm | Bold chuẩn vị trí |
| 4 | Border bảng 1pt màu đen | 100% border nét đơn màu đen với độ dày chuẩn 1pt (`w:sz="8"`) | Border đen 1pt chuẩn |
| 5 | Nền bảng trắng thuần túy | 100% nền ô màu trắng thuần túy; không có nền màu tiêu đề, không tô xám, không zebra | Bảng nền trắng sạch |
| 6 | Kế thừa font chủ đạo | Sử dụng đúng font của tài liệu; đồng bộ đầy đủ thuộc tính `ascii`, `hAnsi`, `cs` trong thẻ `w:rFonts` | Không lỗi font tiếng Việt |
| 7 | Cỡ chữ chuẩn | Thân bài thuyết minh đúng 12pt; bảng biểu từ 10pt đến 12pt đồng nhất | Cỡ chữ chuẩn mực |
| 8 | Bảng nhiều cột xoay ngang | Các bảng từ 7 cột trở lên được bố trí trong section trang xoay ngang (Landscape) | Đạt chuẩn trình bày bảng |
| 9 | Đối soát tự động | Chạy `verify_docx.py` không xuất hiện bất kỳ cảnh báo lệch màu, sai bold, border không 1pt hay nền bảng màu | Vượt qua đối soát |
| 10 | Quy chuẩn viết hoa | Toàn bộ danh từ chung không viết hoa tùy tiện; chỉ viết hoa đầu câu và danh từ riêng | Đúng chính tả hành chính |

---

## 5. Tài Liệu Tham Khảo Kỹ Thuật

- [references/font_inheritance_and_inspection.md](references/font_inheritance_and_inspection.md): Phân tích chi tiết mô hình kế thừa OpenXML, kỹ thuật xử lý thẻ table borders 1pt (`sz="8"`), table shading trắng và kiểm soát thuộc tính bold cho heading của bảng.
