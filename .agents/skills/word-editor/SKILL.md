---
name: word-editor
description: >-
  Chỉnh sửa, cập nhật và chuẩn hóa tài liệu Microsoft Word (.docx). Bắt buộc kiểm tra và kế thừa chuẩn xác font chữ, cỡ chữ, kiểu dáng, style và thuộc tính OpenXML từ các nội dung tương tự (đoạn lân cận, ô bảng cùng cột, tiêu đề cùng cấp). Nghiêm cấm tự ý sửa đổi lan man ngoài phạm vi yêu cầu, bảo đảm tính toàn vẹn và đồng nhất tuyệt đối của tài liệu văn phòng.
---

# Kỹ Năng Chỉnh Sửa Tài Liệu Word Chuẩn Định Dạng (Word Editor)

Kỹ năng này trang bị quy trình, công cụ và kỹ thuật lập trình chuyên sâu giúp chỉnh sửa, cập nhật tệp tài liệu Microsoft Word mà vẫn bảo toàn nguyên vẹn cấu trúc trình bày, font chữ, cỡ chữ, kiểu dáng và thuộc tính thẩm mỹ ban đầu của văn bản.

---

## 1. Nguyên Tắc Cốt Lõi Khi Chỉnh Sửa File Word

Mọi thao tác chỉnh sửa tệp Word phải tuân thủ nghiêm ngặt các nguyên tắc sau:

1. **Nguyên tắc khoanh vùng phạm vi chỉnh sửa tối thiểu**: Nghiêm cấm tự ý can thiệp, chỉnh sửa, thêm thắt hoặc xóa bỏ các nội dung nằm ngoài phạm vi yêu cầu cụ thể. Chỉ tác động chính xác vào vị trí mục tiêu được giao việc; toàn bộ các đoạn văn, điều khoản, số liệu, cấu trúc và bảng biểu khác phải được giữ nguyên trạng 100%, tuyệt đối không tự tiện viết lại theo ý chủ quan.
2. **Nguyên tắc kiểm tra nội dung tương tự**: Tuyệt đối không tự ý áp đặt font chữ ngẫu nhiên hoặc sử dụng font mặc định của thư viện lập trình. Trước khi sửa hoặc thêm nội dung, bắt buộc phải kiểm tra font chữ, cỡ chữ, kiểu dáng của các nội dung tương tự trong cùng tài liệu để áp dụng đồng bộ.
3. **Nguyên tắc bảo toàn định dạng gốc**: Giữ nguyên toàn bộ cấu trúc bảng, lề trang, màu sắc, khoảng cách dòng, thụt đầu dòng và hệ thống Style hiện có. Chỉ tác động chính xác vào phần nội dung văn bản cần thay đổi.
4. **Nguyên tắc đồng bộ hóa OpenXML rFonts**: Với tiếng Việt, việc chỉ thiết lập tên font bề nổi thường làm xuất hiện lỗi nhảy font khi mở tệp trên các hệ điều hành khác nhau. Bắt buộc cập nhật đồng thời các thuộc tính `ascii`, `hAnsi` và `cs` trong thẻ XML `w:rFonts`.
5. **Không ghi đè mù quáng**: Phải đọc và hiểu rõ nội dung hiện tại của đoạn văn hoặc ô bảng trước khi chỉnh sửa.

---

## 2. Quy Trình 5 Bước Chỉnh Sửa Tài Liệu Word

```
[1. Khảo sát Tài liệu] ──► Chạy inspect_docx.py để xác định font chủ đạo và phân bố style
          │
          ▼
[2. Xác định Phần tử Tương tự] ──► Định vị đoạn lân cận, ô cùng cột hoặc heading cùng cấp
          │
          ▼
[3. Trích xuất Định dạng Chuẩn] ──► Lấy font name, size pt, bold, italic, color và rFonts XML
          │
          ▼
[4. Thực thi Chỉnh sửa An toàn] ──► Sử dụng patch_docx.py hoặc áp dụng cơ chế sao chép Run
          │
          ▼
[5. Đối soát Nghiệm thu] ──► Chạy verify_docx.py để bảo đảm không có run nào lệch font
```

### Bước 1: Khảo sát và thanh tra font hiện hữu
Sử dụng công cụ thanh tra để quét toàn bộ tài liệu, xác định font chữ chủ đạo, các kích thước font phổ biến và các style đang được áp dụng:
```powershell
python .agents/skills/word-editor/scripts/inspect_docx.py "duong_dan_tep.docx" --summary
```
Nếu cần tìm kiếm vị trí đoạn văn hoặc ô bảng chứa từ khóa cụ thể:
```powershell
python .agents/skills/word-editor/scripts/inspect_docx.py "duong_dan_tep.docx" --search "từ khóa"
```

### Bước 2: Xác định phần tử tham chiếu tương tự
Xác định chính xác loại phần tử cần chỉnh sửa và nguồn tham chiếu tương ứng:
- **Sửa một cụm từ trong đoạn văn**: Tham chiếu chính Run đang chứa cụm từ đó hoặc Run đứng ngay bên cạnh.
- **Sửa toàn bộ đoạn văn hoặc thêm đoạn mới**: Tham chiếu đoạn văn đứng ngay trước, đoạn đứng ngay sau có cùng Style.
- **Sửa ô trong bảng hoặc thêm dòng mới**: Tham chiếu các ô khác trong cùng cột hoặc cùng hàng.
- **Sửa tiêu đề**: Tham chiếu các tiêu đề khác có cùng cấp Heading.

### Bước 3: Trích xuất trọn bộ thuộc tính định dạng tham chiếu
Đối tượng định dạng cần thu thập đầy đủ:
- Tên font: Trích xuất từ `run.font.name` hoặc từ thẻ `w:rFonts`.
- Kích thước font: Trích xuất từ `run.font.size` tính theo đơn vị pt.
- Kiểu dáng: Các giá trị `bold`, `italic`, `underline`.
- Màu sắc: Giá trị `font.color.rgb`.
- Căn lề đoạn văn: Giá trị `paragraph.alignment`.
- Thuộc tính XML `w:rFonts`: Các trường `ascii`, `hAnsi`, `cs`.

### Bước 4: Thực thi chỉnh sửa an toàn
Thực hiện chỉnh sửa thông qua CLI tiện ích hoặc trực tiếp qua mã nguồn Python:
- Thay thế chuỗi văn bản giữ nguyên định dạng:
```powershell
python .agents/skills/word-editor/scripts/patch_docx.py "input.docx" -o "output.docx" -r "nội dung cũ" "nội dung mới"
```
- Cập nhật toàn bộ một đoạn văn theo chỉ số:
```powershell
python .agents/skills/word-editor/scripts/patch_docx.py "input.docx" -o "output.docx" --p-index 15 --p-text "Nội dung cập nhật mới"
```
- Cập nhật một ô trong bảng:
```powershell
python .agents/skills/word-editor/scripts/patch_docx.py "input.docx" -o "output.docx" --cell 0 2 1 "Giá trị ô mới"
```

### Bước 5: Đối soát nghiệm thu sau khi chỉnh sửa
Chạy công cụ đối soát để kiểm tra độ đồng nhất font của tệp sau khi lưu:
```powershell
python .agents/skills/word-editor/scripts/verify_docx.py "output.docx"
```
Bảo đảm không xuất hiện bất kỳ cảnh báo lệch font nào so với font chuẩn của tài liệu.

---

## 3. Hướng Dẫn Kỹ Thuật Lập Trình Cho Các Ngữ Cảnh Đặc Thù

### 3.1 Chỉnh sửa văn bản trong bảng biểu
Bảng biểu trong Word có cấu trúc phân cấp nghiêm ngặt. Khi sửa hoặc thêm nội dung trong ô:
- Tuyệt đối không xóa toàn bộ các đoạn văn trong ô vì sẽ làm mất cấu trúc căn lề của ô.
- Giữ lại đoạn văn đầu tiên trong ô, xóa các Run cũ và thêm Run mới với định dạng được sao chép từ ô cùng cột:
```python
import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def apply_font_to_run(target_run, font_name, font_size_pt, bold=False, italic=False):
    target_run.font.name = font_name
    if font_size_pt:
        target_run.font.size = docx.shared.Pt(font_size_pt)
    target_run.bold = bold
    target_run.italic = italic
    
    # Dong bo OpenXML rFonts
    rPr = target_run._r.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    for attr in ['ascii', 'hAnsi', 'cs', 'eastAsia']:
        rFonts.set(qn(f'w:{attr}'), font_name)
```

### 3.2 Thêm hàng mới vào bảng biểu
Khi thêm hàng mới vào bảng, hàng mới phải kế thừa toàn bộ định dạng của hàng liền trước:
```python
def add_row_with_style_inheritance(table, source_row_idx=-1):
    source_row = table.rows[source_row_idx]
    new_row = table.add_row()
    
    for c_idx, cell in enumerate(new_row.cells):
        src_cell = source_row.cells[c_idx]
        # Ke thua can le va style cua doan van mau
        if src_cell.paragraphs:
            cell.paragraphs[0].alignment = src_cell.paragraphs[0].alignment
            cell.paragraphs[0].style = src_cell.paragraphs[0].style
            # Neu co run mau, ghi nho de su dung khi chen du lieu
```

---

## 4. Bảng Kiểm Tra Chất Lượng Nghiệm Thu (Quality Checklist)

Trước khi xác nhận hoàn thành công việc chỉnh sửa tệp Word, người thực hiện phải rà soát toàn bộ các tiêu chí trong bảng sau:

| STT | Tiêu chí Kiểm tra | Trạng thái Đạt |
|:---:|---|---|
| 1 | Khoanh vùng đúng phạm vi yêu cầu | Chỉ tác động đúng đoạn văn hoặc ô bảng được chỉ định; tuyệt đối không sửa đổi, thêm bớt ngoài nội dung yêu cầu |
| 2 | Khảo sát font trước khi sửa | Đã chạy kiểm tra và xác định rõ font chủ đạo của tài liệu cùng định dạng của đoạn tương tự |
| 3 | Kế thừa font chuẩn xác | Nội dung mới hoặc nội dung sửa đổi sử dụng chính xác font của các nội dung tương tự xung quanh |
| 4 | Đồng bộ kích thước font | Kích thước font tính theo pt khớp hoàn toàn với các đoạn văn cùng cấp hoặc các ô cùng bảng |
| 5 | Đồng bộ thẻ OpenXML rFonts | Đã cập nhật đầy đủ các thuộc tính ascii, hAnsi, cs để tránh lỗi font tiếng Việt |
| 6 | Bảo tồn kiểu in đậm, in nghiêng | Các ký tự quan trọng giữ đúng quy cách nhấn mạnh của tài liệu gốc |
| 7 | Giữ nguyên căn lề và style | Căn lề trái, căn giữa hoặc căn đều hai bên không bị xáo trộn sau khi sửa |
| 8 | Cấu trúc bảng không bị xô lệch | Các cột, hàng và độ rộng bảng giữ nguyên hiện trạng |
| 9 | Đối soát sau khi lưu | Đã chạy xác minh và xác nhận không có vị trí nào bị lệch font |

---

## 5. Tài Liệu Tham Khảo Kỹ Thuật

- [references/font_inheritance_and_inspection.md](references/font_inheritance_and_inspection.md): Phân tích chi tiết mô hình kế thừa OpenXML và xử lý kỹ thuật nâng cao.
