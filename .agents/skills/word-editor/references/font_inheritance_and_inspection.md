# Cẩm Nang Phân Tầng Định Dạng OpenXML và Kỹ Thuật Đối Soát Word Chuẩn Hóa

Tài liệu này cung cấp kiến thức chuyên sâu về mô hình cấu trúc OpenXML của Microsoft Word, kỹ thuật chuẩn hóa font chữ, quy chuẩn màu đen thuần túy, kiểm soát thuộc tính in đậm (Bold) cho heading của bảng và cấu trúc bảng cơ bản (border đen 1pt, nền trắng).

---

## 1. Cơ Chế Phân Tầng Thuộc Tính Trong OpenXML

Trong kiến trúc tệp Word (.docx), các thuộc tính hiển thị (font chữ, cỡ chữ, màu sắc, độ đậm nhạt) được kế thừa theo mô hình phân tầng từ thấp lên cao:

```
[Tầng 4: Theme Font Scheme] ──► a:fontScheme trong word/theme/theme1.xml
            │
            ▼
[Tầng 3: Mặc định cấp Tài liệu] ──► w:docDefaults / w:rPrDefault trong styles.xml
            │
            ▼
[Tầng 2: Paragraph Style] ──► w:pStyle (Normal, Table Grid...)
            │
            ▼
[Tầng 1: Thuộc tính trực tiếp tại Run] ──► w:rPr trong từng w:r (Độ ưu tiên cao nhất)
```

### 1.1 Kiểm soát màu sắc chữ thuần đen (Color Control)
- Thẻ XML: `<w:color w:val="000000"/>` nằm trong `<w:rPr>`.
- Gán tường minh là `000000` cho toàn bộ văn bản để tránh bị ảnh hưởng bởi theme của người dùng hoặc các style ngoại lai.
- Mã màu hợp lệ: `000000` hoặc `auto`. Mọi mã màu khác (`002060`, `4F81BD`, `1F497D`, `FF0000`...) đều vi phạm chuẩn định dạng.

### 1.2 Kiểm soát thuộc tính In Đậm (Bold Control)
- Thẻ XML: `<w:b/>` và `<w:bCs/>` nằm trong `<w:rPr>`.
- **Quy tắc**: Bôi đậm (Bold) chỉ áp dụng cho **Heading của bảng (hàng đầu tiên / table header row)**. Các đoạn văn thân bài ngoài bảng và các ô dữ liệu trong bảng (hàng 1 trở đi) tuyệt đối không được chứa thẻ `<w:b/>`.
- Khi lập trình:
  ```python
  # Đối với dòng heading của bảng (Hàng 0):
  run.bold = True
  
  # Đối với thân bài ngoài bảng và ô dữ liệu bảng (Hàng >= 1):
  run.bold = False
  if run._r.rPr is not None:
      for tag in ['b', 'bCs']:
          elem = run._r.rPr.find(qn(f'w:{tag}'))
          if elem is not None:
              run._r.rPr.remove(elem)
  ```

---

## 2. Cấu Trúc Bảng Biểu Cơ Bản Trong OpenXML (Border Đen 1pt, Nền Trắng)

Một bảng Word chuẩn định dạng cơ bản gồm 2 cấu phần chính trong cấu trúc OpenXML:

### 2.1 Đường viền bảng 1pt màu đen (w:tblBorders)
Đường viền của bảng được định nghĩa trong thẻ `<w:tblPr>` ở cấp bảng thông qua thẻ con `<w:tblBorders>`. Để tạo bảng cơ bản nét đơn màu đen với độ dày 1pt:

```xml
<w:tblBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>
  <w:left w:val="single" w:sz="8" w:space="0" w:color="000000"/>
  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>
  <w:right w:val="single" w:sz="8" w:space="0" w:color="000000"/>
  <w:insideH w:val="single" w:sz="8" w:space="0" w:color="000000"/>
  <w:insideV w:val="single" w:sz="8" w:space="0" w:color="000000"/>
</w:tblBorders>
```
- `w:val="single"`: Nét kẻ đơn.
- `w:sz="8"`: Độ dày 8/8 pt = **1pt** (trong OpenXML đơn vị đo của border size là 1/8 pt).
- `w:color="000000"`: Mã màu đen thuần túy.

Lưu ý: Cần xóa bỏ các thuộc tính `<w:tcBorders>` ở cấp ô (`w:tcPr`) nếu có, để toàn bộ bảng tuân thủ đồng nhất theo cấu hình `w:tblBorders`.

### 2.2 Nền ô màu trắng thuần túy (w:shd)
Màu nền của ô được quy định bởi thẻ `<w:shd>` trong `<w:tcPr>`. Bảng cơ bản bắt buộc có nền trắng thuần túy:

```xml
<w:shd xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" 
       w:val="clear" 
       w:color="auto" 
       w:fill="FFFFFF"/>
```
- `w:val="clear"`: Không có mẫu hoa văn (pattern).
- `w:fill="FFFFFF"`: Nền trắng tuyệt đối.
- Nghiêm cấm các giá trị fill khác như `E7E6E6`, `D9D9D9`, `4F81BD`, `1F497D`... hoặc bất kỳ màu xám/xanh trang trí nào.

---

## 3. Bảng Tra Cứu Quy Chuẩn Định Dạng

| Thành phần | Font chữ | Cỡ chữ | Màu sắc | Kiểu dáng (Bold) | Định dạng nền / Viền |
|---|---|:---:|:---:|:---:|---|
| **Văn bản thân bài ngoài bảng** | Font chủ đạo | 12 pt | Đen (`#000000`) | **Không đậm (Regular)** | Dãn dòng 1.15-1.25, cách đoạn 3-4pt |
| **Danh sách liệt kê ngoài bảng** | Font chủ đạo | 12 pt | Đen (`#000000`) | **Không đậm (Regular)** | Bullet hoặc số thứ tự chuẩn |
| **Tiêu đề bảng (Heading của bảng - Hàng 0)** | Font chủ đạo | 10 - 12 pt | Đen (`#000000`) | **In đậm (Bold)** | Border đen 1pt (`sz="8"`), nền trắng |
| **Dữ liệu bảng (Hàng 1 trở đi)** | Font chủ đạo | 10 - 12 pt | Đen (`#000000`) | **Không đậm (Regular)** | Border đen 1pt (`sz="8"`), nền trắng |
| **Ghi chú chân bảng / Trang** | Font chủ đạo | 10 - 11 pt | Đen (`#000000`) | **Không đậm (Regular)** | Nghiêng (Italic) nếu cần, không Bold |
