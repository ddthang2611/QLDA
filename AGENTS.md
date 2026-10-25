# ICTPM (Workspace QLDA)

Khi câu chat có `pm:` hoặc `@pm:` hoặc `/pm:`, đọc `.agents/skills/pm/SKILL.md` (hoặc `Smart PMP/.agents/skills/pm/SKILL.md`) và chỉ làm một lệnh, ví dụ `@pm:hsmt`.

Mọi câu trả lời và nội dung tài liệu viết bằng tiếng Việt ngay từ đầu.

File output ghi vào `Smart PMP/ictpm-flow/artifacts/`. Không tự đặt `status` thành `approved`.

---

## 1. Quy tắc Phê duyệt Chỉnh sửa Hồ sơ (Bắt buộc)
- **Chỉ sửa hồ sơ khi đã được duyệt và cho phép**: Tuyệt đối không tự ý chỉnh sửa, thêm bớt, ghi đè hoặc thay đổi bất kỳ nội dung nào của các hồ sơ, tài liệu, hợp đồng, kế hoạch khi Người dùng chưa kiểm tra, duyệt và cho phép rõ ràng.
- Mọi đề xuất thay đổi phải được báo cáo và chỉ được thực thi khi có sự đồng ý hoặc chỉ thị dứt khoát từ Người dùng.

---

## 2. Tài liệu Nguyên mẫu Duy nhất — Ưu tiên Cao nhất Tuyệt đối (Highest Priority)
- **RFP là nguồn chân lý duy nhất và cao nhất**: Tài liệu RFP (Request For Proposal của Công ty Cổ phần ABC Wear) là tài liệu nguyên mẫu DUY NHẤT đáng tin cậy tuyệt đối và sở hữu mức độ ưu tiên cao nhất trong toàn bộ dự án.
- **Xử lý mâu thuẫn**: Nếu có bất kỳ sự sai lệch, khác biệt hoặc mâu thuẫn nào giữa RFP và bất kỳ tài liệu nào khác (HSMT, HSDT, Master Plan, Bảng tiến độ, Dự toán chi phí), thông tin trong RFP LUÔN LUÔN là chuẩn mực tối thượng bắt buộc phải tuân theo. Mọi tài liệu khác đều phải phục tùng và căn chỉnh theo RFP.
- **Không trích dẫn nguồn nội bộ**: Khi tạo lập các văn bản chính thức của Bên mời thầu hoặc của Dự án, không được chú thích trích dẫn nguồn nội bộ như "theo RFP", "tham chiếu RFP".

---

## 3. Bản Dịch Toàn Văn Tài Liệu Nguyên Mẫu RFP ABC Wear

### Trang 1: Trang bìa
- **Tiêu đề**: RFP (Request For Proposal) - Yêu cầu Đề xuất Giải pháp
- **Ngày phát hành**: 22/02/20XX
- **Chủ đầu tư**: Công ty Cổ phần ABC Wear

### Trang 2: Tổng quan Hệ thống và Yêu cầu Đề xuất
#### 1. Tổng quan Hệ thống
- **Mục tiêu của Dự án**: Mở rộng tệp khách hàng qua không gian mạng Internet, xây dựng kênh bán hàng trực tuyến mới.
- **Chính sách Phát triển Cơ bản**:
  1. Thao tác dễ dàng đối với khách hàng (Easy Operation for the Customer).
  2. Sử dụng bất kỳ lúc nào: hệ thống vận hành liên tục 24 giờ mỗi ngày và 365 ngày mỗi năm (24hours and 365Days running).
  3. Thời gian phản hồi nhanh chóng: trong vòng không quá 2 giây (Quick response time within 2 seconds).
- **Sơ đồ Luồng Hệ thống Mới**:
  Khách hàng $\rightarrow$ Mạng Internet $\rightarrow$ **Web Site Selling System** (Tìm kiếm sản phẩm, Quản trị thành viên, Đặt hàng, CSDL Selling DB) $\xleftrightarrow{\text{Giao tiếp hai chiều}}$ **Main System** (Quản trị Bán hàng, Sản phẩm, Logistics, Giao dịch) $\rightarrow$ Khâu Vận chuyển Giao nhận (Transportation Operation) $\rightarrow$ Khách hàng.
- **Thời điểm vận hành chính thức (Cut over)**: Ngày 01 tháng 07 năm 20XX (20XX. July. 1).
- **Phạm vi Dự án**:
  - Phát triển hệ thống Web Site Selling System từ khâu Phân tích hệ thống đến Kiểm thử vận hành (System Analysis to Operation Test).
  - *Lưu ý ràng buộc đặc biệt*: Toàn bộ chức năng quản trị nội bộ nằm ngoài phạm vi của dự án này (The internal administrative function are out of scope in this project).

#### 2. Yêu cầu Đối với Hồ sơ Đề xuất (Request for Proposal)
Hồ sơ đề xuất của nhà thầu bắt buộc phải bao gồm đầy đủ 10 thông tin sau đây:
1. **Precondition**: Nêu rõ các tiền đề, giả định kỹ thuật và điều kiện tiên quyết trong đề xuất.
2. **Estimated Cost**: Nêu rõ dự toán chi phí cho dự án kèm theo lý do và căn cứ tính toán cụ thể.
3. **Project Scope**: Nêu rõ phạm vi các hoạt động liên quan đáp ứng tiêu chuẩn của ABC Wear.
4. **Deliverables**: Liệt kê đầy đủ danh mục các sản phẩm bàn giao theo hợp đồng.
5. **Schedule**: Lập bảng tiến độ chi tiết từ khi khởi động đến ngày Cut-over ngày 01 tháng 07.
6. **Organization**: Trình bày cơ cấu tổ chức nhân sự của công ty tham gia dự án.
7. **Meeting**: Đề xuất kế hoạch tổ chức các cuộc họp phù hợp giữa hai bên.
8. **Roles**: Phân định rõ vai trò và trách nhiệm của các bên.
9. **Other Conditions**: Trình bày các điều kiện khác liên quan đến thỏa thuận hợp đồng nếu có.
10. **Request for us**: Nêu rõ các đề xuất hoặc yêu cầu phối hợp gửi tới ABC Wear.

### Trang 3: Quy trình Nộp Đề xuất và Thỏa thuận Hợp đồng Cơ sở
#### 1. Quy trình Nộp và Trình bày Đề xuất
- **Thuyết trình**:
  - Thời hạn nộp hồ sơ: Nộp 10 bản in của hồ sơ đề xuất trước hoặc chậm nhất vào ngày **08 tháng 03** (10 copies of proposal should be submitted by March 8th). Thời gian thuyết trình chính xác sẽ được thông báo sau.
  - Địa điểm: Phòng họp A, Trụ sở chính của ABC Wear.
- **Tính bảo mật của RFP**: Tài liệu RFP chứa thông tin bảo mật của ABC Wear. Nhà thầu có trách nhiệm bảo mật và quản lý an toàn.
- **Giải đáp thắc mắc về RFP**:
  - Nếu có bất kỳ câu hỏi nào về RFP, gửi thư điện tử hoặc đến trực tiếp trụ sở của ABC Wear.
  - Đầu mối phụ trách: Yamada - Phòng Kế hoạch, địa chỉ thư điện tử: yamada@abc.com.
  - Thời gian tiếp nhận câu hỏi: Từ ngày **22 tháng 02 đến ngày 07 tháng 03**.

#### 2. Thỏa thuận Hợp đồng Cơ sở (Bên A là ABC Wear, Bên B là Nhà thầu trúng thầu)
- Bên B bắt đầu triển khai phát triển hệ thống ngay sau khi hai bên ký kết thỏa thuận hợp đồng.
- Bên A hoặc Bên B đều có quyền yêu cầu thay đổi đặc tả kỹ thuật khi cần thiết và phải được hai bên thống nhất bằng văn bản.
- Trường hợp Bên B cần thuê thầu phụ bên ngoài, Bên B bắt buộc phải gửi văn bản yêu cầu và phải được Bên A chấp thuận bằng văn bản.
- Bên B có trách nhiệm bàn giao các sản phẩm bàn giao đúng địa điểm và thời hạn đã thỏa thuận.
- Bên A tiến hành kiểm tra nghiệm thu các sản phẩm bàn giao theo các điều kiện được ghi trong tài liệu đặc tả kỹ thuật và thông báo kết quả cho Bên B. Việc vượt qua kỳ kiểm tra này đồng nghĩa với việc sản phẩm được chấp nhận nghiệm thu.
- Toàn bộ quyền sở hữu và bản quyền liên quan đến các sản phẩm bàn giao được phát triển và các thành quả kỹ thuật trong suốt dự án này đều thuộc về Bên A. Khi Bên B muốn sử dụng cho bất kỳ bên thứ ba nào khác thì bắt buộc phải được Bên A chấp thuận bằng văn bản.
- Các sai sót về mặt logic trong sản phẩm bàn giao hoặc các sự cố khác thuộc trách nhiệm của Bên B, Bên B bắt buộc phải chỉnh sửa hoặc bổ sung bằng trách nhiệm và chi phí của chính Bên B trong thời gian sớm nhất có thể.
- Thời hạn Bên B phải chịu trách nhiệm bảo hành và khắc phục sai sót là trong vòng **01 năm** (12 tháng).

### Trang 4 & Trang 5: Danh mục Sản phẩm Bàn giao Cụ thể
1. **Specification**: Đặc tả kỹ thuật hệ thống Web Selling Site System gồm Cấu hình cơ sở dữ liệu (DB Configuration) và Danh mục chức năng (Function). Chức năng quản trị nội bộ nằm ngoài phạm vi dự án.
2. **New Operational Flow**: Sơ đồ luồng vận hành mới thể hiện sự tương tác giữa Khách hàng, Website bán hàng, Hệ thống chính (Main System) và Khâu vận chuyển.
3. **Database Structure**: Thiết kế cấu trúc cơ sở dữ liệu bán hàng (Selling DB).
4. **Menu Layer**: Cấu trúc phân tầng và điều hướng Menu giao diện người dùng.

---

## 4. Quy tắc Chỉnh sửa Tài liệu Dự án Văn phòng (Word, Excel)
- Khi chỉnh sửa các tệp tài liệu văn phòng như Word .docx hay Excel .xlsx, tuyệt đối giữ nguyên định dạng gốc, font chữ, cỡ chữ, kiểu dáng style, căn lề, màu sắc và cấu trúc trình bày ban đầu. Chỉ tác động và cập nhật chính xác nội dung văn bản cần thay đổi.
- Nghiêm cấm tự ý chỉnh sửa, thêm thắt, xóa bỏ hoặc viết lại bất kỳ nội dung nào nằm ngoài phạm vi yêu cầu cụ thể. Chỉ khoanh vùng và tác động đúng vị trí, đoạn văn, điều khoản hoặc ô bảng được chỉ định; giữ nguyên vẹn 100% toàn bộ phần còn lại của tài liệu.
- Khi chỉnh sửa tệp Word .docx, kích hoạt và tuân thủ kỹ năng tại `.agents/skills/word-editor/SKILL.md`. Bắt buộc kiểm tra font của các nội dung tương tự gồm đoạn văn liền kề, ô bảng cùng cột hoặc hàng, tiêu đề cùng cấp để áp dụng chính xác tên font, cỡ chữ pt và đồng bộ thuộc tính XML rFonts, tuyệt đối không dùng font mặc định của thư viện lập trình. Sau khi sửa phải đối soát lại để bảo đảm tính đồng nhất font 100%.
- Bắt buộc luôn luôn đọc file hiện có để nắm bắt đặc điểm font chữ, in đậm, nhạt, nghiêng, căn chỉnh, kích thước... của chính đoạn văn cần sửa. Sau đó mới fill nội dung mới vào để giữ nguyên vẹn 100% định dạng (format) tại đoạn đó.
- Nghiêm cấm chèn số tiền, dự toán kinh phí vào dòng tiêu đề, tên gói thầu hoặc tên dự án. Giá gói thầu chỉ ghi tại các điều khoản giá gói thầu hoặc bảng giá quy định.
- Tuyệt đối không sử dụng dấu ngoặc đơn để chú thích hoặc giải thích thuật ngữ trong tài liệu và câu trả lời; toàn bộ nội dung hướng tới đối tượng chuyên gia, diễn đạt trực tiếp, gãy gọn và tự nhiên.
