# Khung Cấu trúc Hồ sơ Đề xuất Kỹ thuật và Tài chính — Dự án ABC Wear

Tài liệu này cung cấp mẫu chuẩn 10 phần bắt buộc của Hồ sơ Đề xuất (Proposal / HSDT) theo đúng yêu cầu tại Hồ sơ mời thầu của ABC Wear, kết hợp với các sản phẩm bàn giao kỹ thuật chi tiết.

---

## Cấu trúc Tổng thể Bộ Hồ sơ Đề xuất

```text
HỒ SƠ ĐỀ XUẤT (PROPOSAL) — DỰ ÁN ABC WEAR
├── PHẦN I: THÔNG TIN TỔNG QUAN VÀ ĐƠN DỰ THẦU
├── PHẦN II: 10 NỘI DUNG ĐỀ XUẤT CỐT LÕI THEO YÊU CẦU RFP
│   ├── Mục 1: Precondition (Điều kiện tiên quyết & Giả định)
│   ├── Mục 2: Estimated Cost (Dự toán chi phí & Căn cứ tính toán)
│   ├── Mục 3: Project Scope (Phạm vi công việc & Ranh giới In-Scope / Out-of-Scope)
│   ├── Mục 4: Deliverables (Danh mục sản phẩm bàn giao theo hợp đồng)
│   ├── Mục 5: Schedule (Kế hoạch tiến độ & Đường găng đến mốc Cut-over)
│   ├── Mục 6: Organization (Cơ cấu tổ chức & Đội ngũ nhân sự chủ chốt)
│   ├── Mục 7: Meeting Plan (Kế hoạch họp, báo cáo & Kênh giao tiếp)
│   ├── Mục 8: Roles & Responsibilities (Ma trận phân định trách nhiệm RACI)
│   ├── Mục 9: Other Conditions (Điều kiện thương mại, pháp lý, SLA & Bảo hành)
│   └── Mục 10: Request for Client (Yêu cầu phối hợp gửi Chủ đầu tư ABC Wear)
└── PHẦN III: PHỤ LỤC ĐẶC TẢ KỸ THUẬT CHI TIẾT
    ├── Phụ lục 1: Specification (Đặc tả chức năng & Cấu hình CSDL Web Selling Site)
    ├── Phụ lục 2: New Operational Flow (Sơ đồ luồng vận hành mới)
    ├── Phụ lục 3: Database Structure (Mô hình CSDL bán hàng Selling DB)
    └── Phụ lục 4: Menu Layer (Cấu trúc phân tầng Menu giao diện)
```

---

## Chi tiết Từng Mục Đề xuất

### Mục 1: Precondition (Điều kiện tiên quyết)
- Các giả định về hạ tầng máy chủ và dịch vụ điện toán đám mây.
- Giả định về giao diện kết nối API của Main System từ phía ABC Wear.
- Quy định về thời gian phản hồi phê duyệt hồ sơ, thiết kế và kết quả kiểm thử của ABC Wear.

### Mục 2: Estimated Cost (Dự toán chi phí)
- Bảng tổng hợp giá dự thầu theo các khối công việc chính:
  1. Phân tích hệ thống (System Analysis).
  2. Thiết kế và phát triển Web Selling Site System.
  3. Tích hợp Main System.
  4. Kiểm thử vận hành (Operation Test).
  5. Bàn giao, chuyển giao và đào tạo vận hành.
  6. Dịch vụ bảo hành và khắc phục sự cố 12 tháng.
- Thuyết minh căn cứ định mức chi phí: Đơn giá công thợ theo vị trí chuyên môn, chi phí công cụ và hạ tầng phục vụ dự án, tỷ lệ giảm giá thương mại.

### Mục 3: Project Scope (Phạm vi công việc)
- Khẳng định phạm vi thực hiện trọn gói từ khâu khảo sát phân tích đến kiểm thử vận hành nghiệm thu.
- Bốn trụ cột hệ thống:
  - Phân hệ Tìm kiếm sản phẩm (Product Search).
  - Phân hệ Quản trị thành viên (Member Administration).
  - Phân hệ Đặt hàng và Giỏ hàng (Order).
  - Cơ sở dữ liệu Bán hàng (Selling DB).
- Cổng tích hợp hai chiều với Main System (Bán hàng, Thông tin sản phẩm, Logistics và Giao dịch).
- Ranh giới Out-of-Scope: Nêu rõ toàn bộ logic quản trị nội bộ của Main System nằm ngoài phạm vi thực hiện của nhà thầu.

### Mục 4: Deliverables (Sản phẩm bàn giao)
- Bàn giao cuốn chiếu các Phần tăng trưởng (Increments) có thể sử dụng được theo từng Sprint:
  - Sprint 1: Phần tăng trưởng Tìm kiếm và Xem chi tiết sản phẩm thời trang chạy thực tế trên Web, bộ lọc đa tiêu chí và từ khóa gợi ý Elasticsearch.
  - Sprint 2: Phần tăng trưởng Đăng ký, Đăng nhập bảo mật JWT, xác thực OTP và Quản lý sổ địa chỉ giao hàng.
  - Sprint 3: Phần tăng trưởng Giỏ hàng thông minh Persistent Cart và Quy trình đặt hàng Checkout tối giản 3 bước.
  - Sprint 4: Phần tăng trưởng Cổng thanh toán trực tuyến đa kênh (quét mã QR, thẻ ngân hàng, ví điện tử, COD) và cơ chế đối soát tự động.
  - Sprint 5: Phần tăng trưởng Tích hợp 05 luồng dữ liệu hai chiều với Main System và kết nối điều phối đội xe logistics nội bộ của ABC Wear.
  - Sprint 6: Phần tăng trưởng Tối ưu hiệu năng P95 dưới 2 giây chịu tải 5.000 người dùng đồng thời và rà soát an toàn thông tin OWASP.
  - Sprint 7: Toàn bộ hệ thống hoàn chỉnh sau kiểm thử vận hành Operation Test, đạt 100% tiêu chí nghiệm thu UAT, tài liệu hướng dẫn vận hành và đào tạo người dùng.
- Đi kèm 04 bộ sản phẩm tài liệu bắt buộc theo phụ lục hợp đồng: Đặc tả kỹ thuật Web Selling Site, Luồng vận hành mới New Operational Flow, Mô hình CSDL Selling DB, và Sơ đồ phân tầng Menu Layer.

### Mục 5: Schedule (Kế hoạch tiến độ Agile Scrum)
- Thời điểm nộp thầu sớm: Ngày 03 tháng 03 năm 2026.
- Thời điểm đóng thầu & mở thầu: Ngày 08 tháng 03 năm 2026.
- Thời điểm khởi động dự án: Ngày 16 tháng 03 năm 2026.
- Chu kỳ: 2 tuần mỗi Sprint, gồm 8 Sprint liên tục bảo đảm tạo ra sản phẩm tăng trưởng usable ngay từ Sprint 1:
  - Sprint 0 (16/03 – 27/03): Chuẩn bị môi trường DEV/CI-CD, VPN Main System, làm mịn Product Backlog, thống nhất DoR và DoD.
  - Sprint 1 (30/03 – 10/04): Bàn giao Phần tăng trưởng Tìm kiếm & Sản phẩm thời trang (Product Discovery).
  - Sprint 2 (13/04 – 24/04): Bàn giao Phần tăng trưởng Quản trị Thành viên & Xác thực OTP (Member Auth).
  - Sprint 3 (27/04 – 08/05): Bàn giao Phần tăng trưởng Giỏ hàng & Luồng Checkout 3 bước (Cart & Checkout).
  - Sprint 4 (11/05 – 22/05): Bàn giao Phần tăng trưởng Thanh toán Đa kênh & Đối soát (Payment Integration).
  - Sprint 5 (25/05 – 05/06): Bàn giao Phần tăng trưởng Cổng tích hợp 05 luồng Main System & Logistics nội bộ.
  - Sprint 6 (08/06 – 19/06): Bàn giao Phần tăng trưởng Tối ưu tải P95 dưới 2 giây chịu tải 5.000 CCU & Bảo mật OWASP.
  - Sprint 7 (22/06 – 30/06): Kiểm thử vận hành Operation Test, nghiệm thu UAT toàn trình và đào tạo người dùng.
- Mốc Cut-over / Vận hành chính thức: Ngày 01 tháng 07 năm 2026 (đúng 100% thời hạn bắt buộc trong RFP).
- Giai đoạn Hypercare (01 tháng) và Bảo hành toàn diện (12 tháng): Từ 02/07/2026 đến 01/07/2027.

### Mục 6: Organization (Cơ cấu tổ chức dự án)
- Sơ đồ cơ cấu tổ chức nhóm dự án của nhà thầu.
- Bảng danh sách nhân sự chủ chốt, vai trò đảm nhiệm, số năm kinh nghiệm và chứng chỉ chuyên môn:
  - Giám đốc Dự án (Project Manager).
  - Kiến trúc sư Giải pháp (Solution Architect).
  - Chuyên viên Phân tích Nghiệp vụ (Business Analyst).
  - Trưởng nhóm Kỹ thuật (Technical Lead).
  - Kỹ sư Lập trình Cấp cao (Senior Developers).
  - Trưởng nhóm Kiểm thử (QA/QC Lead).
  - Kỹ sư Vận hành và Triển khai (DevOps Engineer).

### Mục 7: Meeting Plan (Kế hoạch họp và giao tiếp)
- Cơ chế họp định kỳ:
  - Họp khởi động dự án (Kick-off Meeting).
  - Họp rà soát tiến độ tuần (Weekly Status Meeting) giữa PM hai bên.
  - Họp kiểm điểm Sprint (Sprint Review & Demo) định kỳ 2 tuần/lần.
  - Họp bất thường xử lý sự cố khẩn cấp (Ad-hoc Problem Solving).
- Quy định chế độ báo cáo: Báo cáo tuần, Báo cáo kết thúc giai đoạn, Báo cáo rủi ro và vấn đề phát sinh.

### Mục 8: Roles & Responsibilities (Phân định trách nhiệm)
- Bảng ma trận RACI chi tiết cho từng giai đoạn giữa Bên A (ABC Wear) và Bên B (Nhà thầu):
  - Phê duyệt yêu cầu nghiệp vụ: Bên A (A), Bên B (R).
  - Thiết kế và lập trình hệ thống: Bên B (A, R), Bên A (C, I).
  - Cung cấp API và môi trường Main System: Bên A (A, R), Bên B (C).
  - Kiểm thử UAT: Bên A (A, R), Bên B (Support).
  - Quyết định Go-live: Bên A (A), Bên B (Consult).

### Mục 9: Other Conditions (Điều kiện thương mại và pháp lý)
- Điều khoản thanh toán theo mốc bàn giao đã được phê duyệt nghiệm thu.
- Cam kết bảo mật thông tin và dữ liệu kinh doanh của ABC Wear.
- Cam kết chuyển giao toàn bộ bản quyền và quyền sở hữu trí tuệ cho ABC Wear.
- Cam kết dịch vụ bảo hành, khắc phục lỗi logic và sự cố kỹ thuật trong vòng 12 tháng kể từ ngày nghiệm thu bàn giao.
- Cam kết mức độ sẵn sàng của hệ thống đạt tiêu chuẩn 24/7/365 và thời gian phản hồi dưới 2 giây.

### Mục 10: Request for Client (Đề xuất phối hợp gửi ABC Wear)
- Đề xuất cử một đầu mối quản lý nghiệp vụ duy nhất từ ABC Wear để làm việc thường xuyên với PM nhà thầu.
- Đề xuất cung cấp tài liệu đặc tả kỹ thuật và tài khoản thử nghiệm của Main System chậm nhất sau 05 ngày làm việc kể từ ngày khởi động.
- Đề xuất bố trí thời gian phê duyệt tài liệu và kết quả kiểm thử trong vòng 03 đến 05 ngày làm việc để không ảnh hưởng đường găng dự án.
