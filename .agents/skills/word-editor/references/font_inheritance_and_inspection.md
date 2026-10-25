# Cẩm Nang Phân Tầng Font và Kỹ Thuật Đối Soát Định Dạng Word

Tài liệu này cung cấp kiến thức chuyên sâu về mô hình phân tầng định dạng font chữ trong cấu trúc OpenXML của Microsoft Word và các nguyên tắc kiểm tra, kế thừa font khi chỉnh sửa tài liệu.

---

## 1. Cơ Chế Phân Tầng Font Trong OpenXML

Trong kiến trúc tệp Word, định dạng hiển thị của một ký tự hoặc chuỗi ký tự được xác định theo mô hình thừa kế từ thấp lên cao qua bốn tầng:

### Tầng 1: Định dạng trực tiếp tại Run
- Thẻ XML: `<w:rPr>` nằm trực tiếp bên trong thẻ `<w:r>`.
- Đây là tầng có độ ưu tiên cao nhất. Mọi thiết lập tại đây sẽ ghi đè lên các tầng bên dưới.
- Các thuộc tính cốt lõi của font:
  - `<w:rFonts w:ascii="..." w:hAnsi="..." w:cs="..." w:eastAsia="..."/>`: Xác định tên font chữ. Thuộc tính `ascii` dùng cho các ký tự chuẩn; thuộc tính `hAnsi` dùng cho vùng mã mở rộng; thuộc tính `cs` dùng cho hệ ký tự phức hợp; thuộc tính `eastAsia` dùng cho ngôn ngữ Đông Á. Đối với tiếng Việt, việc thiếu đồng bộ giữa `ascii`, `hAnsi` và `cs` thường dẫn đến lỗi nhảy font sang font mặc định của hệ thống.
  - `<w:sz w:val="..."/>`: Kích thước chữ tính bằng đơn vị half-point, ví dụ giá trị 24 tương ứng 12pt, giá trị 28 tương ứng 14pt.
  - `<w:b/>`, `<w:i/>`, `<w:u/>`: Các thuộc tính in đậm, in nghiêng, gạch chân.
  - `<w:color w:val="..."/>`: Mã màu RGB dạng hex.

### Tầng 2: Định dạng Paragraph Style
- Thẻ XML: `<w:pPr><w:pStyle w:val="..."/></w:pPr>` liên kết tới một style cụ thể trong `styles.xml`.
- Nếu Run không khai báo font hoặc cỡ chữ trực tiếp trong `w:rPr`, Word sẽ tìm kiếm định dạng trong phần khai báo style của đoạn văn.

### Tầng 3: Định dạng mặc định cấp tài liệu
- Thẻ XML: `<w:docDefaults><w:rPrDefault><w:rPr>...` nằm trong `styles.xml`.
- Thiết lập này áp dụng cho toàn bộ các đoạn văn và bảng biểu không có style riêng hoặc style sử dụng thiết lập mặc định.

### Tầng 4: Lược đồ phông chữ Theme
- Thẻ XML: `<a:fontScheme>` nằm trong `word/theme/theme1.xml`.
- Chứa hai nhóm font: Major Font dành cho các tiêu đề và Minor Font dành cho nội dung thân bài.

---

## 2. Phương Pháp Kiểm Tra Font Của Các Nội Dung Tương Tự

Khi chỉnh sửa bất kỳ vị trí nào trong tài liệu Word, nguyên tắc bất di bất dịch là phải xác định và sao chép chính xác định dạng từ các nội dung tương tự. Quá trình kiểm tra tiến hành theo các trường hợp sau:

### Trường hợp 1: Chỉnh sửa hoặc thay thế văn bản trong một đoạn văn hiện có
- Nguồn kiểm tra ưu tiên: Các Run hiện diện ngay trong chính đoạn văn đó.
- Cách thực hiện:
  1. Trích xuất tên font, cỡ chữ, kiểu in đậm, in nghiêng từ Run đang chứa văn bản cần sửa hoặc Run đứng ngay liền kề trước hoặc sau nó.
  2. Đọc thẻ `w:rFonts` để nắm rõ cấu hình đầy đủ của các thuộc tính `ascii`, `hAnsi`, `cs`.
  3. Áp dụng toàn bộ các thuộc tính này vào văn bản mới thay thế.

### Trường hợp 2: Chèn thêm đoạn văn mới hoặc thay thế toàn bộ đoạn văn
- Nguồn kiểm tra ưu tiên: Đoạn văn liền trước, đoạn văn liền sau hoặc các đoạn văn cùng cấp Style.
- Cách thực hiện:
  1. Nếu chèn một mục nội dung thân bài: Đối chiếu với đoạn văn thân bài đứng ngay trước đó. Kiểm tra xem đoạn trước đang dùng font gì, cỡ bao nhiêu pt, căn lề trái hay căn lề hai bên, độ giãn dòng bao nhiêu.
  2. Nếu chèn hoặc sửa tiêu đề: Tìm đến các tiêu đề cùng cấp Heading trong tài liệu để trích xuất font chuẩn và cỡ chữ quy định cho cấp độ đó, bảo đảm sự đồng bộ xuyên suốt từ đầu đến cuối văn bản.

### Trường hợp 3: Chỉnh sửa hoặc thêm dòng trong bảng biểu
- Nguồn kiểm tra ưu tiên: Các ô cùng cột hoặc cùng hàng trong bảng.
- Cách thực hiện:
  1. Nếu sửa nội dung ô dữ liệu: Lấy định dạng từ ô đứng ngay bên trên hoặc bên dưới trong cùng cột. Thông thường các ô trong cùng một cột dữ liệu sẽ có chung font chữ, cỡ chữ và kiểu căn lề.
  2. Nếu sửa ô tiêu đề bảng: Trích xuất định dạng từ các ô tiêu đề khác trong hàng đầu tiên của bảng.
  3. Nếu thêm dòng mới vào bảng: Sao chép toàn bộ định dạng font, cỡ chữ, căn lề và viền từ dòng liền kề trước đó.

---

## 3. Quy Trình Kỹ Thuật Khi Sử Dụng Thư Viện Lập Trình

Khi lập trình can thiệp tệp Word bằng python-docx, việc gán trực tiếp thuộc tính text qua lệnh `paragraph.text = "nội dung mới"` sẽ xóa toàn bộ các Run hiện có và đưa đoạn văn về trạng thái không có định dạng Run trực tiếp, dẫn đến nguy cơ sai lệch font. Do đó, cần tuân thủ quy trình kỹ thuật sau:

### Bước 1: Thu thập định dạng tham chiếu
Trước khi xóa hoặc sửa, trích xuất đối tượng Run tham chiếu từ chính đoạn văn hoặc đoạn tương tự lân cận:
- Tên font: `target_font = ref_run.font.name`
- Kích thước: `target_size = ref_run.font.size`
- In đậm: `target_bold = ref_run.bold`
- In nghiêng: `target_italic = ref_run.italic`
- Căn lề: `target_alignment = ref_paragraph.alignment`

### Bước 2: Khởi tạo Run mới và thiết lập font tường minh
- Gán tên font qua giao diện cấp cao: `new_run.font.name = target_font`
- Gán cỡ chữ: `new_run.font.size = target_size`
- Gán kiểu dáng: `new_run.bold = target_bold`, `new_run.italic = target_italic`

### Bước 3: Đồng bộ thẻ OpenXML rFonts
Đây là bước tối quan trọng để xử lý triệt để lỗi nhảy font trên tiếng Việt. Bắt buộc cập nhật trực tiếp vào cây XML:
- Lấy hoặc tạo phần tử `w:rFonts` trong `w:rPr` của Run mới.
- Thiết lập đồng thời cả bốn thuộc tính `w:ascii`, `w:hAnsi`, `w:cs` và `w:eastAsia` về cùng một tên font mục tiêu.

### Bước 4: Đối soát sau khi lưu
Sau khi lưu tệp, kích hoạt công cụ thanh tra để quét lại toàn bộ tài liệu, bảo đảm không có Run nào bị sai lệch font hoặc mang giá trị rỗng ngoài ý muốn.

---

## 4. Nguyên Tắc Can Thiệp Tối Thiểu và Kiểm Soát Ranh Giới Sửa Đổi

Để bảo đảm tính nguyên vẹn của văn bản gốc, thao tác kỹ thuật phải tuân thủ kỷ luật can thiệp tối thiểu:

1. **Khoanh vùng chính xác tọa độ mục tiêu**: Xác định duy nhất đoạn văn, ô bảng hoặc cụm từ cụ thể cần cập nhật. Nếu chỉ sửa một câu trong đoạn, chỉ tác động vào đúng các Run chứa câu đó, không ghi đè lại toàn bộ đoạn văn.
2. **Nghiêm cấm sửa đổi ngoài phạm vi**: Toàn bộ các đoạn văn lân cận, tiêu đề, bảng biểu, chú thích chân trang và số liệu khác nằm ngoài yêu cầu phải được giữ nguyên trạng 100%.
3. **Kiểm soát số lượng tác động**: Luôn kiểm tra và đếm số lượng vị trí bị thay đổi. Tuyệt đối không thực hiện các lệnh thay thế toàn cục nếu từ khóa có thể xuất hiện ở những ngữ cảnh khác không thuộc phạm vi yêu cầu.
