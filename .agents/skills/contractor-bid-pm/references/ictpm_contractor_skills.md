# Kỹ năng Quản trị Dự án Thực chiến Dành cho PM Nhà thầu — Trích xuất từ 7 Bài giảng ICTPM

Tài liệu này hệ thống hóa các nguyên lý, kỹ thuật, công thức và quy trình từ 7 bộ bài giảng ICTPM01 đến ICTPM07, được tinh chỉnh theo góc nhìn và trọng trách của Giám đốc Dự án nhà thầu khi chuẩn bị hồ sơ dự thầu và cam kết triển khai hợp đồng.

---

## 1. Định vị Vai trò và Trách nhiệm PM Nhà thầu — ICTPM01

- **Đầu mối liên lạc duy nhất (Single Point of Contact)**: PM nhà thầu là đại diện toàn quyền về kỹ thuật và tiến độ trước Chủ đầu tư và Ban điều hành nhà thầu.
- **Cân bằng tam giác ràng buộc dự án**:
  - Quản lý đồng thời bốn đỉnh: Phạm vi, Thời gian, Chi phí và Chất lượng.
  - Khi một yếu tố thay đổi (ví dụ: khách hàng rút ngắn ngày cut-over), PM phải đánh giá ngay tác động lên chi phí và chất lượng để đàm phán lại.
- **Tư duy hướng kết quả kinh doanh**:
  - Không dừng lại ở việc bàn giao sản phẩm phần mềm (Output).
  - Phải chứng minh hệ thống vận hành ổn định giúp khách hàng mở rộng doanh thu và tối ưu quy trình kinh doanh (Outcome).
- **Yếu tố quyết định thành bại từ Standish Group Chaos Report**:
  - Làm rõ phạm vi ngay từ khâu dự thầu để tránh rão phạm vi.
  - Duy trì sự tham gia chặt chẽ của người dùng đầu cuối từ phía khách hàng.
  - Thiết lập kỳ vọng thực tế về thời gian và ngân sách.

---

## 2. Kỹ thuật Phân rã Phạm vi và Lập Tiến độ — ICTPM02, ICTPM06

### 2.1. Phân rã Cấu trúc Công việc WBS
- **Quy tắc 100% (100% Rule)**: WBS bao quát toàn bộ khối lượng công việc cam kết trong hợp đồng, không thừa và không thiếu.
- **Gói công việc (Work Package)**: Tầng phân rã thấp nhất của WBS. Mỗi gói công việc phải xác định rõ:
  - Khối lượng cụ thể.
  - Người chịu trách nhiệm duy nhất.
  - Định mức thời gian và chi phí.
  - Tiêu chí nghiệm thu rõ ràng.

### 2.2. Lập Lịch trình và Phương pháp Đường găng CPM
- **Quan hệ phụ thuộc giữa các công việc**: Finish-to-Start (FS), Start-to-Start (SS), Finish-to-Finish (FF), Start-to-Finish (SF).
- **Tính toán đường găng**:
  - Thực hiện tính toán tiến để xác định thời điểm bắt đầu sớm và kết thúc sớm.
  - Thực hiện tính toán lùi để xác định thời điểm bắt đầu muộn và kết thúc muộn.
  - Tính độ dự trữ thời gian tổng thể: Độ dự trữ = Bắt đầu muộn - Bắt đầu sớm = Kết thúc muộn - Kết thúc sớm.
  - Đường găng là chuỗi các công việc có độ dự trữ bằng 0, quyết định tổng thời gian hoàn thành dự án.
- **Ước lượng ba điểm PERT**:
  - Áp dụng khi ước lượng thời gian cho các module phức tạp hoặc tích hợp chưa rõ ràng.
  - Thời gian kỳ vọng: $T_e = \frac{O + 4M + P}{6}$ với O là kịch bản lạc quan, M là kịch bản khả dĩ nhất, P là kịch bản bi quan.
  - Độ lệch chuẩn: $\sigma = \frac{P - O}{6}$
  - Phương sai: $V = \sigma^2 = \left(\frac{P - O}{6}\right)^2$
- **Kỹ thuật nén tiến độ**:
  - Crashing: Bổ sung nhân lực chất lượng cao hoặc tăng ca tập trung vào các công việc trên đường găng.
  - Fast Tracking: Chuyển đổi các công việc vốn tuần tự sang làm song song gối đầu, đi kèm biện pháp kiểm soát lỗi phát sinh.

---

## 3. Dự toán Chi phí và Định giá Chào thầu — ICTPM02

- **Ước lượng từ dưới lên (Bottom-up Estimating)**:
  - Tính toán chi phí cho từng gói công việc trong WBS dựa trên định mức công thợ theo vị trí chuyên môn.
  - Tổng hợp chi phí nhân công trực tiếp, chi phí bản quyền công cụ, hạ tầng đám mây và chi phí quản lý dự án.
- **Thiết lập quỹ dự phòng**:
  - Dự phòng rủi ro đã nhận diện (Contingency Reserve): Đưa vào đường cơ sở chi phí để xử lý rủi ro kỹ thuật.
  - Dự phòng quản lý (Management Reserve): Dành cho các tình huống bất khả kháng ngoài tầm kiểm soát.
- **Quản lý giá trị thu được EVM trong quá trình triển khai**:
  - Lập đường cơ sở chi phí (Cost Baseline) theo dạng đường cong S-Curve.
  - Các chỉ số kiểm soát:
    - Giá trị kế hoạch: PV
    - Giá trị thu được: EV
    - Chi phí thực tế: AC
    - Sai lệch chi phí: $CV = EV - AC$
    - Sai lệch tiến độ: $SV = EV - PV$
    - Chỉ số hiệu quả chi phí: $CPI = \frac{EV}{AC}$
    - Chỉ số hiệu quả tiến độ: $SPI = \frac{EV}{PV}$
    - Dự báo chi phí hoàn thành: $EAC = \frac{BAC}{CPI}$

---

## 4. Cơ cấu Tổ chức và Ma trận Trách nhiệm RACI — ICTPM03

### 4.1. Cấu trúc Đội ngũ Nhà thầu
- **Mô hình Ma trận Mạnh hoặc Chuyên trách theo Dự án**:
  - PM nhà thầu có toàn quyền điều động và đánh giá nhân sự trong suốt vòng đời dự án.
  - Thành phần chủ chốt: Project Manager, Solution Architect, Business Analyst, Tech Lead, Frontend Developer, Backend Developer, QA/QC Lead, DevOps Engineer.

### 4.2. Ma trận Phân công Trách nhiệm RACI
Xác lập rõ trách nhiệm giữa Chủ đầu tư và Nhà thầu trong từng mốc bàn giao:
- **R (Responsible)**: Người trực tiếp thực hiện.
- **A (Accountable)**: Người chịu trách nhiệm giải trình cuối cùng (mỗi công việc chỉ có duy nhất một bên A).
- **C (Consulted)**: Bên được tham vấn ý kiến chuyên môn trước khi thực hiện.
- **I (Informed)**: Bên được nhận thông báo sau khi công việc hoàn thành.

### 4.3. Quản trị Đội ngũ theo Mô hình Tuckman
- Chủ động dẫn dắt đội ngũ qua các giai đoạn: Hình thành, Sóng gió, Chuẩn hóa, Thể hiện và Kết thúc.
- Áp dụng kỹ thuật giải quyết xung đột trên tinh thần hợp tác tìm nguyên nhân gốc rễ.

---

## 5. Quản trị Rủi ro và Kiểm soát Chất lượng — ICTPM04

### 5.1. Quy trình Quản lý Rủi ro 6 Bước
1. **Lập kế hoạch quản lý rủi ro**: Xác định ngân sách dự phòng và tần suất rà soát.
2. **Nhận diện rủi ro**: Sử dụng cấu trúc phân rã rủi ro RBS bao gồm các nhóm: Yêu cầu nghiệp vụ, Kỹ thuật và Tích hợp, Tiến độ và Nhân lực, Khách hàng và Hợp đồng.
3. **Phân tích định tính rủi ro**: Đánh giá Xác suất (P) và Mức độ tác động (I) trên thang điểm 1 đến 5. Điểm rủi ro = $P \times I$.
4. **Phân tích định lượng rủi ro**: Tính giá trị tiền tệ kỳ vọng: $EMV = P \times I$ để lập quỹ tài chính bù đắp sự cố.
5. **Chiến lược ứng phó rủi ro**:
   - Né tránh (Avoid): Tái cấu trúc giải pháp kỹ thuật để triệt tiêu nguyên nhân gây lỗi.
   - Chuyển giao (Transfer): Sử dụng dịch vụ điện toán đám mây có cam kết SLA cao hoặc mua bảo hiểm trách nhiệm nghề nghiệp.
   - Giảm thiểu (Mitigate): Tích hợp thử nghiệm sớm (Mock API), tăng cường kiểm thử tự động, đào tạo nhân sự dự phòng.
   - Chấp nhận (Accept): Lập kế hoạch dự phòng khi sự cố xảy ra.
6. **Theo dõi và cập nhật Nhật ký Rủi ro (Risk Register)**: Cập nhật định kỳ trong các báo cáo tiến độ tuần.

### 5.2. Quản lý Chất lượng và Cam kết SLA
- **Đảm bảo chất lượng (QA)**: Đánh giá quy trình phát triển, kiểm tra việc tuân thủ quy chuẩn viết mã, rà soát kiến trúc.
- **Kiểm soát chất lượng (QC)**: Thực hiện kiểm thử chức năng, kiểm thử hiệu năng dưới tải cao (Load Testing) bảo đảm thời gian phản hồi dưới 2 giây, kiểm thử an toàn bảo mật.
- **Chi phí chất lượng (COQ)**: Đầu tư tối đa vào chi phí phòng ngừa và thẩm định để triệt tiêu chi phí sửa lỗi sau khi vận hành.

### 5.3. Cơ sở Dữ liệu Vấn đề và Cơ chế Leo thang
- Ghi nhận mọi sự cố vào Cơ sở dữ liệu Vấn đề và Hành động khắc phục.
- Kích hoạt cơ chế leo thang lên Ban Giám đốc hai bên khi sự cố vượt thẩm quyền hoặc chậm xử lý quá 48 giờ.

---

## 6. Quản trị Thay đổi và Quản lý Cấu hình — ICTPM07

### 6.1. Quy trình Kiểm soát Thay đổi Tích hợp
1. Tiếp nhận Phiếu yêu cầu thay đổi (CR) từ khách hàng hoặc đội ngũ kỹ thuật.
2. Đăng ký vào Nhật ký Thay đổi (Change Log).
3. Đánh giá tác động toàn diện lên Phạm vi, Tiến độ đường găng, Chi phí và Rủi ro.
4. Trình Hội đồng Kiểm soát Thay đổi (CCB) phê duyệt.
5. Cập nhật các đường cơ sở khi được phê duyệt.
6. Phổ biến quyết định và triển khai.

### 6.2. Quản lý Cấu hình Phần mềm SCM
- Xác định các phần tử cấu hình: Tài liệu kiến trúc, Mã nguồn, Kịch bản triển khai, Dữ liệu khởi tạo.
- Chiến lược phân nhánh Git: Nhánh main ổn định, nhánh develop tích hợp, các nhánh tính năng, nhánh release và nhánh hotfix.
- Áp dụng quy chuẩn đánh mã phiên bản Semantic Versioning gồm phiên bản chính, phiên bản phụ và bản vá lỗi.

---

## 7. Đóng gói Nghiệm thu, Bảo hành và Đánh giá Bài học — ICTPM05

- **Nghiệm thu chấp nhận người dùng (UAT)**: Xây dựng tiêu chí nghiệm thu rõ ràng gắn liền với các kịch bản kiểm thử đã được hai bên phê duyệt.
- **Bàn giao và Chuyển giao vận hành**: Bàn giao mã nguồn, tài liệu hướng dẫn vận hành, tài liệu đào tạo người dùng và cơ sở dữ liệu.
- **Trách nhiệm bảo hành 12 tháng**: Thiết lập quy trình tiếp nhận sự cố, thời gian phản hồi và cam kết thời gian khắc phục triệt để lỗi logic phát sinh.
- **Đúc kết Bài học Kinh nghiệm**: Lập báo cáo tổng kết những thành công và bài học hạn chế để lưu trữ vào kho tài sản quy trình của tổ chức.

---

## 8. Chuẩn Mực Quản Trị Agile Scrum Thực Chiến — Tinh Hoa Từ Scrum Guide 2020

### 8.1. Nguyên Lý Tăng Trưởng Giá Trị Bắt Buộc Ngay Từ Sprint 1
- **Bản chất Phần tăng trưởng (Increment)**: Mỗi Sprint bắt buộc tạo ra một hoặc nhiều phần tăng trưởng có thể sử dụng được (usable). Sản phẩm tăng trưởng của Sprint sau cộng dồn trực tiếp vào các Sprint trước, tạo thành sản phẩm hoàn chỉnh và hoạt động ổn định.
- **Cam kết Định nghĩa Hoàn thành (Definition of Done - DoD)**: Tiêu chuẩn kỹ thuật bắt buộc để một hạng mục Product Backlog được công nhận hoàn thành. Bất kỳ tính năng nào chưa đáp ứng đầy đủ DoD thì tuyệt đối không được mang ra nghiệm thu hay bàn giao tại buổi Sprint Review.
- **Nghiêm cấm biến tướng Thác nước giả danh Sprint (Water-Scrum-Fall)**:
  - Tuyệt đối không chia Sprint thành các pha tuần tự như Sprint 1 làm khảo sát, Sprint 2 làm kiến trúc, Sprint 3 mới viết mã. Đó là cách tiếp cận thác nước trá hình, triệt tiêu tính linh hoạt của Scrum.
  - Mỗi Sprint phải triển khai theo lát cắt dọc (Vertical Slice): trong cùng 1 Sprint, nhóm thực hiện trọn vẹn từ khảo sát yêu cầu chi tiết, thiết kế UI/UX, lập trình Front-end/Back-end đến kiểm thử tự động cho cụm tính năng đó.
  - Ngay tại Sprint 1, Chủ đầu tư với vai trò Product Owner phải được trực tiếp thao tác, thử nghiệm tính năng chạy thực tế trên môi trường Staging/DEV để nghiệm thu và phản hồi.

### 8.2. Các Nghi Thức và Cơ Chế Tương Tác Giữa Nhà Thầu và Chủ Đầu Tư
- **Sprint Planning**: Đầu mỗi Sprint, Product Owner và nhóm phát triển thống nhất Mục tiêu Sprint (Sprint Goal) và lựa chọn các hạng mục công việc từ Product Backlog đưa vào Sprint Backlog.
- **Daily Scrum**: Họp ngắn 15 phút đầu ngày giữa các thành viên nhóm phát triển nhằm kiểm tra tiến độ hướng tới Mục tiêu Sprint và nhận diện rủi ro cản trở.
- **Sprint Review**: Tổ chức vào ngày cuối cùng của Sprint. Nhóm phát triển trình diễn sản phẩm tăng trưởng chạy thực tế (không dùng slide hay tài liệu lý thuyết). Product Owner kiểm tra, nghiệm thu tính năng đạt chuẩn và cập nhật các yêu cầu mới vào Product Backlog.
- **Sprint Retrospective**: Nhóm nội bộ nhà thầu rà soát quy trình, công cụ, quan hệ phối hợp để đúc kết giải pháp cải tiến hiệu suất cho Sprint kế tiếp.
