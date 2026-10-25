---
name: contractor-bid-pm
description: >-
  Hướng dẫn Giám đốc Dự án phía Nhà thầu chuẩn bị hồ sơ dự thầu và đề xuất giải pháp cho dự án theo yêu cầu RFP của ABC Wear và chuẩn mực quản trị từ 7 bài giảng ICTPM. Hỗ trợ bóc tách RFP, lập phạm vi WBS, tính toán tiến độ CPM và PERT, dự toán chi phí, xây dựng ma trận RACI, kế hoạch rủi ro, cam kết SLA 24/7 và tốc độ phản hồi dưới 2 giây. Kích hoạt khi cần lập hoặc rà soát hồ sơ thầu, đề xuất kỹ thuật, kế hoạch triển khai của nhà thầu.
---

# Kỹ năng Quản trị Dự án Dành cho PM Nhà thầu (Contractor Bid PM)

Skill này trang bị đầy đủ phương pháp luận, quy trình và kỹ thuật thực chiến cho Giám đốc Dự án đại diện Nhà thầu trong giai đoạn chuẩn bị, bảo vệ hồ sơ dự thầu và đàm phán hợp đồng cho dự án xây dựng hệ thống kênh bán hàng qua Internet của Công ty Cổ phần ABC Wear.

---

## 1. Nguồn Tri thức và Căn cứ Nghiệp vụ

Khi thực hiện nhiệm vụ, PM nhà thầu tra cứu ba tài liệu tham chiếu cốt lõi:
1. [references/rfp_abc_wear.md](references/rfp_abc_wear.md): Toàn bộ thông tin, phạm vi In-Scope / Out-of-Scope, mốc cut-over ngày 01/07, điều khoản hợp đồng và 10 nội dung bắt buộc của RFP ABC Wear.
2. [references/ictpm_contractor_skills.md](references/ictpm_contractor_skills.md): Cẩm nang kỹ năng quản trị dự án thực chiến trích xuất từ 7 bài giảng ICTPM01 đến ICTPM07 (WBS, CPM, PERT, Bottom-up Costing, RACI, Risk Matrix, EVM, Hybrid Agile).
3. [references/hsdt_template_abc_wear.md](references/hsdt_template_abc_wear.md): Khung cấu trúc chuẩn 10 phần của Hồ sơ Đề xuất đáp ứng toàn diện tiêu chí đánh giá của Bên mời thầu.

---

## 2. Quy trình Thực hiện Chuẩn bị Hồ sơ Dự thầu

```
[Nhận RFP ABC Wear] 
       │
       ▼
[1. Bóc tách RFP & Đóng khung Phạm vi] ──► Loại trừ chức năng quản trị nội bộ của Main System
       │
       ▼
[2. Thiết kế Giải pháp & Luồng Vận hành] ──► Kiến trúc 24/7, Phản hồi < 2s, Tích hợp API
       │
       ▼
[3. Phân rã WBS & Lập Tiến độ CPM/PERT] ──► Kiểm soát Đường găng, Cam kết mốc Cut-over 01/07
       │
       ▼
[4. Dự toán Chi phí & Giá Chào thầu] ──► Bottom-up Estimating, Chi phí bản quyền, Dự phòng rủi ro
       │
       ▼
[5. Xây dựng Bộ máy Dự án & Ma trận RACI] ──► Nhân sự chủ chốt, Phân định trách nhiệm Bên A - Bên B
       │
       ▼
[6. Kế hoạch Quản lý Rủi ro & Cam kết Hợp đồng] ──► Ma trận PxI, Bảo hành 12 tháng, Sở hữu trí tuệ
       │
       ▼
[7. Tổng hợp Bộ Hồ sơ Đề xuất 10 Mục] ──► Soát lỗi bằng Checklist trước khi nộp 10 bản in
```

---

## 3. Các Lệnh Chuyên biệt (Workflow Commands)

Skill hỗ trợ thực hiện nhanh từng phần việc qua các lệnh sau:

### `@contractor-bid-pm:rfp-audit`
- Rà soát toàn bộ RFP của ABC Wear.
- Xuất bảng ma trận yêu cầu khách hàng, xác định rõ ranh giới:
  - In-Scope: Phân tích, thiết kế, lập trình Website bán hàng (Tìm kiếm sản phẩm, Thành viên, Đặt hàng, Selling DB), tích hợp Main System, kiểm thử vận hành.
  - Out-of-Scope: Chức năng quản trị nội bộ bên trong Main System của ABC Wear.
- Nêu rõ các rủi ro pháp lý và kỹ thuật cần làm rõ với đầu mối Yamada trước ngày 07/03.

### `@contractor-bid-pm:scope-wbs`
- Xây dựng cấu trúc phân rã công việc WBS tuân thủ nguyên tắc 100%.
- Phân rã tối thiểu 4 cấp đến các gói công việc cụ thể.
- Đính kèm từ điển WBS xác định rõ sản phẩm đầu ra và tiêu chí nghiệm thu cho từng gói.

### `@contractor-bid-pm:schedule`
- Thiết lập kế hoạch tiến độ theo chuẩn mực Scrum Guide 2020 kết hợp kiểm soát hợp đồng chặt chẽ đến mốc Cut-over ngày 01/07.
- Bảo đảm nguyên lý cốt lõi của Scrum: Ngay từ Sprint 1 đã phải tạo ra Phần tăng trưởng (Increment) có thể dùng được để Product Owner nghiệm thu tại buổi Sprint Review; cấm kỵ chia Sprint theo kiểu phân tích, thiết kế tuần tự của Thác nước.
- Sử dụng phương pháp đường găng CPM và kỹ thuật nén tiến độ Crashing (bổ sung 2 DEV nâng quy mô lên 5 DEV) cùng Fast Tracking triển khai song song các lát cắt tính năng để về đích đúng hạn 01/07.
- Đính kèm định nghĩa sẵn sàng (DoR) và định nghĩa hoàn thành (DoD) chuẩn hóa cho từng Sprint.

### `@contractor-bid-pm:cost-estimate`
- Dự toán chi phí từ dưới lên (Bottom-up) chi tiết theo từng gói công việc WBS.
- Phân bổ định mức công thợ cho từng vai trò: Giám đốc Dự án, Kiến trúc sư Giải pháp, Phân tích nghiệp vụ, Kỹ sư Lập trình, Chuyên viên Kiểm thử, Kỹ sư Vận hành.
- Tính toán quỹ dự phòng rủi ro kỹ thuật và lập bảng tổng hợp giá dự thầu kèm thuyết minh căn cứ.

### `@contractor-bid-pm:tech-proposal`
- Soạn thảo đề xuất giải pháp kiến trúc tổng thể đáp ứng ba tiêu chuẩn phi chức năng cốt lõi:
  - Tính sẵn sàng cao 24/7/365: Kiến trúc Cloud-Native, Cân bằng tải, Triển khai không gián đoạn.
  - Thời gian phản hồi dưới 2 giây: Bộ nhớ đệm Redis, CDN, tối ưu truy vấn Selling DB, công cụ tìm kiếm Elasticsearch.
  - Tích hợp Main System: Cổng giao tiếp API bảo mật, Message Queue đồng bộ dữ liệu đơn hàng và giao nhận logistics nội bộ.
- Hoàn thiện 4 phụ lục kỹ thuật: Đặc tả hệ thống, Luồng vận hành mới, Cấu trúc Selling DB và Phân tầng Menu.

### `@contractor-bid-pm:bid-package`
- Tổng hợp và hoàn thiện toàn bộ 10 nội dung bắt buộc của Hồ sơ Đề xuất theo đúng danh mục yêu cầu trong RFP ABC Wear:
  1. Precondition
  2. Estimated Cost
  3. Project Scope
  4. Deliverables
  5. Schedule
  6. Organization
  7. Meeting Plan
  8. Roles & Responsibilities
  9. Other Conditions
  10. Request for Client

---

## 4. Bảng Kiểm Tra Chất Lượng Hồ Sơ Đề Xuất (Quality Checklist)

Trước khi đóng gói xuất bản 10 bản in nộp cho ABC Wear, PM phải tự kiểm tra các tiêu chí sau:

| STT | Tiêu chí Kiểm tra | Yêu cầu Đạt |
|:---:|---|---|
| 1 | Tuân thủ 10 mục của RFP | Đủ 10 phần, không bỏ sót bất kỳ đề mục nào theo yêu cầu của ABC Wear |
| 2 | Giới hạn ranh giới phạm vi | Nêu rõ loại trừ chức năng quản trị nội bộ của Main System |
| 3 | Cam kết hiệu năng kỹ thuật | Cam kết bằng giải pháp khả thi cho SLA 24/7 và phản hồi < 2s |
| 4 | Mốc thời gian Cut-over | Kế hoạch tiến độ bảo đảm vận hành chính thức đúng ngày 01/07 |
| 5 | Tính toán đường găng CPM | Xác định rõ các công việc găng và độ dự trữ thời gian |
| 6 | Dự toán chi phí minh bạch | Giá dự thầu khớp với phân rã WBS và có thuyết minh căn cứ logic |
| 7 | Ma trận trách nhiệm RACI | Mỗi gói công việc chỉ có duy nhất một bên giữ vai trò chịu trách nhiệm giải trình |
| 8 | Cam kết thời hạn bảo hành | Thể hiện cam kết bảo hành và khắc phục sai sót trong 12 tháng |
| 9 | Cơ chế họp và báo cáo | Đủ các hình thức họp định kỳ, báo cáo tuần và cơ chế leo thang sự cố |
| 10 | Bản quyền & Bảo mật | Cam kết tôn trọng quyền sở hữu trí tuệ của ABC Wear và bảo mật dữ liệu |
