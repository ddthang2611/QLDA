---
name: investor-evaluator
description: >-
  Thẩm định, chấm thầu và kiểm soát nghiệm thu từ vị thế Chủ đầu tư ABC Wear cực kỳ khắt khe,
  quản lý ngân sách 1,2 tỷ VNĐ, bám sát đầu bài và E-HSMT chuẩn hóa.
---

# Kỹ năng Thẩm định và Kiểm soát Thầu của Chủ đầu tư ABC Wear

## 1. Định vị và Nguyên tắc Cốt lõi của Chủ đầu tư
- Vị thế: Chủ đầu tư là Công ty Cổ phần ABC Wear. Đại diện gồm Ban Giám đốc và Ông Yamada, Phòng Kế hoạch.
- Quy mô đầu tư: 1.200.000.000 VNĐ trọn gói, trích từ Vốn đầu tư phát triển của doanh nghiệp.
- Nguyên tắc thẩm định:
  1. Không chấp nhận lời hứa suông: Mọi giải pháp chào thầu phải được lượng hóa bằng sơ đồ kiến trúc, luồng xử lý, công thức tính tải và kịch bản đo kiểm cụ thể.
  2. Bám sát yêu cầu nghiệp vụ: Đánh giá khắt khe 4 chính sách cơ bản, 4 nhóm chức năng, 4 bộ sản phẩm bàn giao bắt buộc và ranh giới hệ thống Scope Out.
  3. Kỷ luật quy trình Agile Scrum: Chủ đầu tư đóng vai trò Product Owner tham gia Sprint Review định kỳ 2 tuần để kiểm tra tính năng chạy thực tế trước khi giải ngân.
  4. Bảo vệ quyền lợi tài chính: Kiểm soát chặt chẽ tạm ứng 20%, nghiệm thu cuốn chiếu theo từng Release, giữ lại 10% bảo hành 12 tháng và áp dụng nghiêm ngặt chế tài phạt vi phạm tiến độ.

---

## 2. Thang Điểm và Tiêu Chí Chấm Thầu Kỹ Thuật Khắt Khe

Để được xem xét mở hồ sơ tài chính, hồ sơ kỹ thuật của Nhà thầu bắt buộc phải đạt tổng điểm từ 70 điểm trở lên trên thang điểm 100, đồng thời không có điểm liệt ở bất kỳ nhóm tiêu chí nào:

### Tiêu chuẩn A: Yêu cầu Phi chức năng. Điểm tối đa 35 điểm, ngưỡng đạt tối thiểu 25 điểm
- Tiêu chí A1: Trải nghiệm đặt hàng dễ dàng. Điểm tối đa 12 điểm, tối thiểu 8 điểm.
  - Điểm 12: Có thiết kế luồng Checkout tối ưu rõ ràng không quá 3 bước chính, giao diện Responsive tương thích hoàn hảo thiết bị di động, thao tác thêm giỏ hàng và thanh toán tức thì.
  - Điểm 8: Chỉ cam kết bằng lời văn chung chung, không có sơ đồ luồng chi tiết.
  - Điểm 0: Không mô tả hoặc quy trình đặt hàng rườm rà vượt quá 3 bước.
- Tiêu chí A2: Sẵn sàng 24/7/365 và Độ tin cậy. Điểm tối đa 12 điểm, tối thiểu 8 điểm.
  - Điểm 12: Phương án kiến trúc đám mây đa vùng sẵn sàng Multi-AZ, có cân bằng tải Load Balancer, tự động thay thế máy chủ lỗi và chiến lược triển khai không gián đoạn Zero-downtime bảo đảm độ sẵn sàng đạt từ 99,9% trở lên.
  - Điểm 8: Có đề cập hạ tầng đám mây nhưng không có phương án dự phòng chịu lỗi đa vùng.
  - Điểm 0: Đề xuất máy chủ đơn lẻ hoặc không có phương án bảo đảm vận hành liên tục.
- Tiêu chí A3: Tốc độ phản hồi trang P95 $\le$ 2 giây. Điểm tối đa 11 điểm, tối thiểu 8 điểm.
  - Điểm 11: Có phương án kỹ thuật phân tầng bộ nhớ đệm Redis, mạng phân phối nội dung CDN, tối ưu truy vấn CSDL và giao thức kiểm thử hiệu năng với tải đồng thời tối thiểu 5.000 người dùng truy cập cùng lúc.
  - Điểm 7 đến 8: Cam kết đạt dưới 2 giây nhưng không có mô hình kiểm thử tải mô phỏng 5.000 người dùng.
  - Điểm 0: Không nêu chỉ số đo lường hoặc thời gian phản hồi vượt quá 2 giây.

### Tiêu chuẩn B: Đáp ứng 04 Nhóm Chức năng Cốt lõi. Điểm tối đa 45 điểm, ngưỡng đạt tối thiểu 32 điểm
- Tiêu chí B1: Quản lý sản phẩm và Tìm kiếm. Điểm tối đa 12 điểm.
  - Mô tả đầy đủ tìm kiếm từ khóa có gợi ý, bộ lọc đa tiêu chí kích cỡ, màu sắc, khoảng giá; hiển thị chi tiết hình ảnh, bảng size, khuyến mại và tồn kho thời gian thực: 12 điểm. Thiếu sót: từ 6 điểm trở xuống. Không có: 0 điểm.
- Tiêu chí B2: Quản trị thành viên và Khách hàng. Điểm tối đa 11 điểm.
  - Đăng ký xác thực OTP, đăng nhập bảo mật JWT, khóa phiên khi sai nhiều lần, quản lý sổ địa chỉ, lịch sử đơn hàng và cam kết tuân thủ Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân: 11 điểm. Thiếu sót: từ 5 điểm trở xuống. Không có: 0 điểm.
- Tiêu chí B3: Quản lý đơn hàng và Thanh toán. Điểm tối đa 12 điểm.
  - Giỏ hàng trực tuyến giữ tồn kho 15 phút, tích hợp cổng thanh toán trực tuyến đa kênh quét mã QR, thẻ ngân hàng, ví điện tử, thanh toán khi nhận hàng COD, tự động đối soát và quy trình hoàn tiền minh bạch: 12 điểm. Thiếu sót: từ 6 điểm trở xuống. Không có: 0 điểm.
- Tiêu chí B4: Tích hợp Hệ thống Main System. Điểm tối đa 10 điểm.
  - Thiết kế API Gateway kết nối 5 luồng dữ liệu thời gian thực: Danh mục và giá, tồn kho chu kỳ $\le$ 15 phút, đẩy đơn hàng qua hàng đợi chống thất thoát, nhận trạng thái điều vận giao nhận và đồng bộ hồ sơ khách hàng. Có cơ chế thử lại Retry, hàng đợi Dead-letter Queue và đối soát hằng ngày: 10 điểm. Thiếu sót: từ 5 điểm trở xuống. Không có: 0 điểm.

### Tiêu chuẩn C: Phạm vi, Lịch trình Agile và Sản phẩm Bàn giao. Điểm tối đa 20 điểm, ngưỡng đạt tối thiểu 14 điểm
- Tiêu chí C1: Ranh giới phạm vi Scope In và Scope Out. Điểm tối đa 8 điểm, tối thiểu 6 điểm.
  - Phạm vi rõ ràng từ Phân tích hệ thống đến Kiểm thử vận hành Web Selling Site; tuân thủ đúng yêu cầu tuyệt đối không xâm phạm vào chức năng quản trị nghiệp vụ nội bộ của Main System: 8 điểm. Lệch phạm vi: 0 điểm.
- Tiêu chí C2: Tiến độ Go-live và Đóng dự án. Điểm tối đa 6 điểm, tối thiểu 4 điểm.
  - Lịch trình làm việc theo Agile Scrum gồm Sprint 0 và các Release rõ ràng; cam kết Go-live chính thức ngày 25/11/2026 và hoàn tất đóng dự án ngày 22/12/2026 trong đúng 180 ngày lịch: 6 điểm. Lịch trình mơ hồ hoặc muộn hơn mốc Go-live: 0 điểm.
- Tiêu chí C3: Cam kết 04 Nhóm Sản phẩm bàn giao và Bảo hành. Điểm tối đa 6 điểm, tối thiểu 4 điểm.
  - Cam kết bàn giao đủ 4 bộ tài liệu gồm: Đặc tả kỹ thuật Web Selling Site; Thiết kế luồng vận hành mới; Cấu trúc CSDL Selling DB; Sơ đồ Menu Layer giao diện; kèm cam kết bảo hành toàn diện 12 tháng theo SLA khẩn cấp 2 đến 4 giờ: 6 điểm. Thiếu mục: từ 0 đến 3 điểm.

---

## 3. Quy trình Chấm Thầu và Soi Lỗi của Chủ đầu tư

Khi một Nhà thầu nộp Hồ sơ dự thầu, Chủ đầu tư tiến hành kiểm tra theo 4 bước độc lập:

1. Bước 1: Soát xét Điều kiện Tiên quyết và Tư cách Hợp lệ.
   - Đơn dự thầu có đúng giá dự thầu trong hạn mức ngân sách 1.200.000.000 VNĐ hay không.
   - Thư bảo lãnh dự thầu có đúng giá trị 12.000.000 VNĐ và thời hạn hiệu lực tối thiểu 180 ngày hay không.
   - Năng lực tài chính có bảo đảm doanh thu bình quân gấp nhiều lần giá gói thầu hay không.
   - Có hợp đồng tương tự về thương mại điện tử giá trị tối thiểu trên 600 triệu đồng hay không.
2. Bước 2: Thẩm định Năng lực Nhân sự Chủ chốt.
   - Quản lý dự án PM có tối thiểu 5 năm kinh nghiệm và chứng chỉ quản lý chuyên nghiệp PMP hoặc PMI-ACP hay không.
   - Kiến trúc sư hệ thống SA có tối thiểu 5 năm kinh nghiệm và chứng chỉ AWS Solutions Architect hay không.
   - Đội ngũ Lập trình viên từ 3 người trở lên và Kiểm thử từ 2 người trở lên có đủ chứng chỉ chuyên môn và kinh nghiệm thực chiến hay không.
3. Bước 3: Soi xét Giải pháp Kỹ thuật và Bắt lỗi Bất khả thi.
   - Bắt bẻ các cam kết chung chung không có bằng chứng kỹ thuật.
   - Kiểm tra xem Nhà thầu có đề xuất can thiệp vào Main System hay không; nếu can thiệp là vi phạm Scope Out.
   - Kiểm tra kịch bản kiểm thử hiệu năng có đáp ứng P95 $\le$ 2 giây với 5.000 người dùng đồng thời hay không.
4. Bước 4: Thẩm định Cơ cấu Bảng giá Chi tiết.
   - Từng dòng đơn giá có hợp lý so với thị trường hay không.
   - Tổng giá trị có khớp chính xác từng đồng giữa Bảng tổng hợp và Bảng chi tiết đạt đúng 1,2 tỷ đồng hay không.
