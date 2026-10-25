# Bóc tách Yêu cầu Hồ sơ Mời thầu RFP — Dự án ABC Wear

Tài liệu tổng hợp các yêu cầu, phạm vi, ràng buộc và tiêu chuẩn từ hồ sơ mời thầu của Công ty Cổ phần ABC Wear phục vụ công tác lập hồ sơ dự thầu của Giám đốc Dự án nhà thầu.

---

## 1. Thông tin Chung Dự án

- **Bên mời thầu (Bên A)**: Công ty Cổ phần ABC Wear (Chuỗi cửa hàng ABC Wear).
- **Tên dự án**: Xây dựng hệ thống kênh bán hàng qua Internet (Web Site Selling System).
- **Thời điểm phát hành RFP**: Ngày 22 tháng 02 năm 20XX.
- **Thời hạn đóng nộp hồ sơ**: Trước ngày 08 tháng 03 năm 20XX (Số lượng: 10 bản in).
- **Địa điểm thuyết trình**: Phòng họp A, Trụ sở chính ABC Wear.
- **Đầu mối giải đáp thắc mắc**: Yamada — Phòng Kế hoạch, email: yamada@abc.com (Thời gian tiếp nhận: 22/02 đến 07/03).
- **Tính bảo mật**: Tài liệu RFP chứa thông tin bảo mật của ABC Wear, nhà thầu phải quản lý và bảo mật theo quy định.

---

## 2. Mục tiêu và Định hướng Phát triển Hệ thống

### 2.1. Mục tiêu Dự án
- Mở rộng tệp khách hàng tiềm năng qua không gian mạng.
- Xây dựng kênh bán hàng trực tuyến mới, kết nối đồng bộ với chuỗi cửa hàng hiện hữu.

### 2.2. Định hướng Phát triển Nền tảng
- **Dễ dàng thao tác cho khách hàng**: Giao diện trực quan, tối ưu trải nghiệm mua sắm, quy trình đặt hàng và thanh toán nhanh chóng.
- **Sẵn sàng vận hành 24/7/365**: Kiến trúc bảo đảm tính sẵn sàng cao, không gián đoạn dịch vụ.
- **Tốc độ phản hồi tức thì dưới 2 giây**: Thời gian phản hồi cho các tác vụ tìm kiếm, xem chi tiết và đặt hàng không vượt quá 2 giây.

---

## 3. Phạm vi Công việc và Ranh giới Dự án

### 3.1. Phạm vi Trong Dự án (In-Scope)
Thực hiện toàn trình từ Phân tích hệ thống đến Kiểm thử vận hành:
- **Phân hệ Tìm kiếm sản phẩm (Product Search)**: Tìm kiếm nhanh, bộ lọc thông minh theo danh mục, kích thước, màu sắc, giá bán.
- **Phân hệ Quản trị thành viên (Member Administration)**: Đăng ký, đăng nhập, bảo mật thông tin cá nhân, lịch sử đơn hàng, tích điểm thành viên.
- **Phân hệ Đặt hàng (Order)**: Giỏ hàng, xử lý đơn hàng, tích hợp thanh toán trực tuyến, quản lý trạng thái xử lý đơn.
- **Cơ sở dữ liệu Bán hàng (Selling DB)**: Thiết kế mô hình dữ liệu bán hàng tối ưu tốc độ đọc ghi và đồng bộ.
- **Tích hợp với Hệ thống Chính (Main System)**: Kết nối và đồng bộ hai chiều dữ liệu Bán hàng, Thông tin sản phẩm, Dữ liệu logistics giao nhận và Giao dịch.
- **Kiểm thử vận hành (Operation Test)**: Kiểm thử tải, kiểm thử bảo mật, kiểm thử tích hợp hệ thống và kiểm thử chấp nhận người dùng.

### 3.2. Giới hạn Nằm ngoài Dự án (Out-of-Scope)
- Toàn bộ các chức năng quản trị nội bộ bên trong Main System của ABC Wear (Quản lý chuỗi cung ứng nội bộ, hạch toán kế toán tổng hợp, điều phối kho tổng) nằm ngoài phạm vi gói thầu này.
- Nhà thầu chỉ xây dựng cổng giao tiếp API và lớp đệm middleware kết nối tới Main System, không sửa đổi logic lõi của Main System.

---

## 4. Các Mốc Tiến độ Ràng buộc

- **Ngày bàn giao và vận hành chính thức (Cut over)**: Ngày 01 tháng 07 năm 20XX.
- Lịch trình từ ngày ký hợp đồng đến ngày cut-over cần được chia nhỏ thành các mốc bàn giao kiểm soát rõ ràng.

---

## 5. Ràng buộc Hợp đồng và Pháp lý Cốt lõi

- **Thời điểm khởi động**: Nhà thầu bắt đầu phát triển hệ thống ngay sau khi ký kết thỏa thuận hợp đồng.
- **Kiểm soát thay đổi đặc tả**: Mọi thay đổi về đặc tả kỹ thuật giữa Bên A và Bên B phải được hai bên thống nhất bằng văn bản.
- **Thuê thầu phụ (Outsourcing)**: Trường hợp nhà thầu cần thuê thầu phụ, bắt buộc phải có văn bản xin phép và được Bên A chấp thuận trước khi triển khai.
- **Bàn giao và Nghiệm thu**: Nhà thầu phải bàn giao sản phẩm đúng địa điểm và thời hạn đã thỏa thuận. Việc kiểm tra nghiệm thu căn cứ theo đúng tài liệu đặc tả kỹ thuật. Kết quả nghiệm thu đạt đồng nghĩa với việc chấp nhận bàn giao.
- **Quyền sở hữu trí tuệ**: Toàn bộ bản quyền và quyền sở hữu đối với sản phẩm bàn giao, kết quả kỹ thuật thuộc về Bên A. Nhà thầu muốn sử dụng cho bên thứ ba phải có văn bản chấp thuận của Bên A.
- **Bảo hành và Khắc phục sự cố**: Mọi sai sót logic hoặc lỗi phát sinh thuộc trách nhiệm của nhà thầu phải được khắc phục kịp thời bằng chi phí của nhà thầu. Thời hạn trách nhiệm bảo hành là 01 năm (12 tháng).

---

## 6. Danh mục 10 Yêu cầu Bắt buộc trong Hồ sơ Đề xuất (HSDT)

1. **Precondition (Điều kiện tiên quyết)**: Nêu rõ các tiền đề, giả định kỹ thuật, môi trường và điều kiện hợp tác từ phía khách hàng.
2. **Estimated Cost (Dự toán chi phí)**: Đưa ra mức giá dự thầu kèm căn cứ tính toán, phân rã chi phí minh bạch và lý do thuyết phục.
3. **Project Scope (Phạm vi công việc)**: Mô tả chi tiết phạm vi các hoạt động đáp ứng chuẩn mực và yêu cầu của ABC Wear.
4. **Deliverables (Sản phẩm bàn giao)**: Liệt kê đầy đủ các sản phẩm bàn giao theo hợp đồng, gồm tài liệu phân tích, tài liệu thiết kế, mã nguồn, cơ sở dữ liệu và kịch bản kiểm thử.
5. **Schedule (Kế hoạch tiến độ)**: Lập bảng tiến độ tổng thể và chi tiết từ khi khởi động đến mốc cut-over ngày 01/07.
6. **Organization (Cơ cấu tổ chức)**: Trình bày sơ đồ tổ chức dự án của nhà thầu, cam kết nhân sự chủ chốt.
7. **Meeting (Kế hoạch họp và giao tiếp)**: Đề xuất ma trận cuộc họp định kỳ, cơ chế báo cáo tiến độ và kênh phối hợp giữa hai bên.
8. **Roles (Phân định vai trò và trách nhiệm)**: Ma trận trách nhiệm phân định rõ nhiệm vụ của Bên A và Bên B.
9. **Other Conditions (Điều kiện thương mại và pháp lý khác)**: Điều khoản thanh toán, bảo mật thông tin, bảo hành 1 năm và sở hữu trí tuệ.
10. **Request for us (Đề xuất phối hợp gửi Chủ đầu tư)**: Nêu rõ các yêu cầu về cung cấp tài liệu API Main System, cử nhân sự đầu mối nghiệp vụ và phê duyệt nghiệm thu đúng hạn.

---

## 7. Yêu cầu Sản phẩm Bàn giao Cụ thể theo Phụ lục RFP

1. **Specification (Đặc tả hệ thống Web Selling Site System)**:
   - Cấu hình cơ sở dữ liệu (DB Configuration).
   - Danh mục chức năng chi tiết (Function List).
2. **New Operational Flow (Luồng vận hành mới)**:
   - Sơ đồ tương tác giữa Khách hàng, Website bán hàng, Hệ thống chính (Main System) và Bộ phận vận chuyển giao nhận (Transportation Operation).
3. **Database Structure (Cấu trúc CSDL bán hàng)**:
   - Thiết kế mô hình dữ liệu của Selling DB bảo đảm đồng bộ và hiệu năng cao.
4. **Menu Layer (Cấu trúc phân tầng Menu)**:
   - Sơ đồ điều hướng và phân cấp chức năng của giao diện người dùng.
