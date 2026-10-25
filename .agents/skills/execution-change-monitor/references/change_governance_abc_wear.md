# Quy Chế Kiểm Soát Thay Đổi Và Giám Sát Thực Thi Dự Án ABC Wear

Tài liệu này xác lập quy chế kiểm soát thay đổi và giám sát thực thi đặc thù áp dụng cho Dự án Xây dựng Hệ thống Website Bán hàng Trực tuyến của Công ty Cổ phần ABC Wear. Quy chế bảo đảm tính kỷ luật, sự minh bạch tài chính và bảo vệ tuyệt đối đường cơ sở tiến độ đã cam kết.

---

## 1. Ranh Giới Phạm Vi và Các Ràng Buộc Bất Khả Xâm Phạm

Mọi hoạt động giám sát thực thi và kiểm soát thay đổi phải tuyệt đối tuân thủ tài liệu nguyên mẫu duy nhất có mức độ ưu tiên cao nhất là RFP của Công ty Cổ phần ABC Wear:

1. **Ranh giới ngoài phạm vi (Out of Scope)**:
   - Toàn bộ các chức năng quản trị nội bộ của ABC Wear nằm ngoài phạm vi của dự án này. Mọi đề xuất bổ sung chức năng quản trị nội bộ đều bị từ chối ngay từ vòng tiếp nhận.
   - Thay thế hoặc nâng cấp hệ thống quản trị bán hàng hiện hữu (Main System) nằm ngoài phạm vi dự án. Nhà thầu chỉ xây dựng các bộ kết nối giao tiếp hai chiều qua lớp trung gian và mạng riêng ảo bảo mật, tuyệt đối không truy cập trực tiếp vào cơ sở dữ liệu Main System.

2. **Ràng buộc thời hạn vận hành chính thức (Cut-over)**:
   - Ngày đưa vào vận hành chính thức là ngày 01 tháng 07 năm 2026.
   - Đây là mốc thời gian bất khả xâm phạm. Bất kỳ yêu cầu thay đổi nào dẫn đến nguy cơ làm chậm mốc vận hành chính thức ngày 01 tháng 07 đều không được chấp thuận, hoặc bắt buộc phải chuyển sang giai đoạn phát triển nâng cao sau khi hệ thống đã vận hành chính thức.

3. **Ràng buộc ngân sách và loại hợp đồng**:
   - Hợp đồng triển khai là hợp đồng trọn gói với tổng giá trị cố định 1.200.000.000 VNĐ đã bao gồm thuế giá trị gia tăng 10%.
   - Định mức lao động toàn dự án đã được phê duyệt là 3.200 giờ công phân bổ cho 12 nhân sự chủ chốt.

---

## 2. Phân Định Ranh Giới Tuyệt Đối Giữa Lỗi Phần Mềm và Yêu Cầu Thay Đổi

Để ngăn ngừa tranh chấp và bảo vệ nguồn lực dự án, quy chế phân định rạch ròi bản chất giữa hai khái niệm:

### 2.1 Lỗi phần mềm (Defect / Bug)
- **Định nghĩa**: Là trường hợp hệ thống hoạt động sai lệch, không chính xác, gián đoạn hoặc không đáp ứng các tiêu chí đã được xác lập trong tài liệu Đặc tả yêu cầu hệ thống, Đặc tả kỹ thuật, hoặc vi phạm các chỉ tiêu phi chức năng đã cam kết (thời gian phản hồi P95 vượt quá 2 giây ở mức tải 5.000 người dùng đồng thời, tỷ lệ sẵn sàng dưới 99,9%, sự cố bảo mật OWASP).
- **Trách nhiệm chi phí**: Căn cứ thỏa thuận hợp đồng cơ sở tại Trang 3 của RFP, các sai sót về mặt logic trong sản phẩm bàn giao hoặc các sự cố khác thuộc trách nhiệm của nhà thầu, nhà thầu bắt buộc phải chỉnh sửa hoặc bổ sung bằng trách nhiệm và chi phí của chính nhà thầu trong thời gian sớm nhất có thể.
- **Quy trình xử lý**: Lỗi được ghi nhận vào Hệ thống Quản lý Lỗi, phân cấp độ nghiêm trọng từ 1 đến 4 và giao cho đội ngũ phát triển khắc phục ngay theo cam kết chất lượng, tuyệt đối không được tính phát sinh chi phí hoặc khấu trừ vào quỹ dự phòng.

### 2.2 Yêu cầu thay đổi (Change Request - CR)
- **Định nghĩa**: Là trường hợp chủ đầu tư hoặc nhà thầu đề xuất bổ sung tính năng mới chưa từng có trong đặc tả đã phê duyệt, sửa đổi luồng nghiệp vụ đã nghiệm thu, thay đổi cấu trúc bảng cơ sở dữ liệu bán hàng ngoài thiết kế ban đầu, hoặc điều chỉnh quy cách tích hợp với hệ thống bên thứ ba phát sinh ngoài hợp đồng.
- **Trách nhiệm chi phí và tiến độ**: Yêu cầu thay đổi bắt buộc phải trải qua quy trình đánh giá tác động toàn diện về chi phí, giờ công và tiến độ, được cấp có thẩm quyền phê duyệt bằng văn bản trước khi bắt tay vào thực hiện.

### 2.3 Trường hợp đặc thù: Sửa lỗi dẫn đến thay đổi kiến trúc
Khi việc khắc phục một sự cố kỹ thuật đòi hỏi phải tái cấu trúc kiến trúc hệ thống hoặc sửa đổi giao tiếp với Main System, Kiến trúc sư hệ thống phải lập hồ sơ phân tích nguyên nhân gốc rễ:
- Nếu lỗi xuất phát từ thiết kế ban đầu của nhà thầu: Toàn bộ chi phí tái cấu trúc do nhà thầu tự chi trả.
- Nếu xuất phát từ việc hệ thống bên ngoài thay đổi cấu trúc dữ liệu không báo trước: Vấn đề được chuyển thành Yêu cầu Thay đổi và đưa vào quy trình xử lý của Ban Kiểm soát Thay đổi.

---

## 3. Cơ Chế Quản Lý Tài Chính Cho Thay Đổi: Quỹ Dự Phòng 260.490.000 VNĐ

Trong cơ cấu ngân sách 1,2 tỷ VNĐ đã được phê duyệt, dự án đã trích lập một quỹ tài chính chuyên biệt:
- **Tên quỹ**: Chi phí dự phòng rủi ro kỹ thuật và quản lý thay đổi (Contingency Reserve).
- **Giá trị quỹ**: 236.809.091 VNĐ trước VAT, tương đương **260.490.000 VNĐ sau VAT 10%** (chiếm tỷ lệ 21,7% tổng giá trị gói thầu).

### Nguyên tắc trích lập và giải ngân quỹ dự phòng:
1. **Nguồn chi trả duy nhất**: Mọi chi phí phát sinh hợp lệ từ các Yêu cầu Thay đổi được phê duyệt hoặc các chi phí ứng phó rủi ro kỹ thuật bất khả kháng đều được trích từ quỹ dự phòng này, bảo đảm không làm vượt tổng giá trị hợp đồng 1,2 tỷ VNĐ.
2. **Quy định đơn giá thanh toán**: Chi phí nhân công phát sinh từ yêu cầu thay đổi được tính đúng theo Bảng đơn giá giờ công đã chốt trong hồ sơ dự thầu (từ 208.947 VNĐ/h đến 320.000 VNĐ/h tùy theo chức danh chuyên môn).
3. **Thẩm quyền phê duyệt trích quỹ**:
   - Yêu cầu thay đổi có giá trị dưới 50.000.000 VNĐ và không làm chậm tiến độ Sprint: Thuộc thẩm quyền phê duyệt chung của Giám đốc Dự án nhà thầu và Đại diện nghiệp vụ CĐT (Yamada).
   - Yêu cầu thay đổi có giá trị từ 50.000.000 VNĐ đến hết hạn mức quỹ dự phòng, hoặc có nguy cơ tác động đến tiến độ các Sprint: Bắt buộc phải có quyết định bằng văn bản của toàn thể Ban Kiểm soát Thay đổi.
   - Vượt hạn mức 260.490.000 VNĐ: Trường hợp các yêu cầu thay đổi vượt quá tổng quỹ dự phòng, hai bên bắt buộc phải đàm phán ký kết Phụ lục hợp đồng kinh tế bổ sung trước khi triển khai.

---

## 4. Ban Kiểm Soát Thay Đổi (Change Control Board - CCB)

Ban Kiểm soát Thay đổi là cơ quan quyền lực cao nhất chịu trách nhiệm thẩm định và ra quyết định đối với mọi thay đổi trong dự án.

### 4.1 Thành phần nhân sự của CCB
1. **Đại diện Chủ đầu tư ABC Wear**: Ông Yamada - Phòng Kế hoạch (giữ vai trò Chủ tịch CCB, đại diện quyền lợi kinh doanh và quyết định tài chính).
2. **Giám đốc Dự án Nhà thầu**: Ông Nguyễn Đức Tân (giữ vai trò Thư ký CCB, chịu trách nhiệm điều hành, đánh giá tác động tổng thể và kiểm soát hợp đồng).
3. **Kiến trúc sư Hệ thống**: Ông Nguyễn Hải Đăng (chịu trách nhiệm đánh giá tác động kỹ thuật, kiến trúc sẵn sàng 24/7/365, giao tiếp Main System và bảo mật).
4. **Chuyên viên Phân tích Nghiệp vụ**: Ông Đinh Đức Thắng (chịu trách nhiệm phân tích quy trình nghiệp vụ, ranh giới phạm vi và cập nhật Product Backlog).

### 4.2 Ma trận phân công trách nhiệm RACI của CCB

| Hoạt động kiểm soát thay đổi | Yamada (CĐT) | Nguyễn Đức Tân (PM) | Nguyễn Hải Đăng (SA) | Đinh Đức Thắng (BA) |
| :--- | :---: | :---: | :---: | :---: |
| Tiếp nhận và sơ loại đề xuất thay đổi | I | A/R | C | C |
| Phân tích tác động nghiệp vụ và phạm vi | C | A | C | R |
| Đánh giá tác động kiến trúc và an toàn hệ thống | I | A | R | C |
| Dự toán chi phí và giờ công phát sinh | C | A/R | C | C |
| Đánh giá ảnh hưởng tiến độ Sprint và Cut-over | C | A/R | C | C |
| Quyết định phê duyệt trích quỹ dự phòng | A | R | C | I |
| Cập nhật Product Backlog và lập kế hoạch Sprint | I | A | C | R |
| Nghiệm thu kết quả triển khai thay đổi | A | R | C | C |

*Ghi chú: A = Người chịu trách nhiệm giải trình cuối cùng; R = Người trực tiếp thực hiện; C = Người được tham vấn chuyên môn; I = Người nhận thông tin báo cáo.*

---

## 5. Quy Trình 5 Bước Phê Duyệt Yêu Cầu Thay Đổi Thực Chiến

```
[Bước 1: Tiếp nhận Đề xuất CR]
       │
       ▼
[Bước 2: Phân tích Tác động Kỹ thuật & Chi phí] (Tối đa 48 giờ)
       │
       ▼
[Bước 3: Lập Hồ sơ Thẩm định & Trình CCB]
       │
       ▼
[Bước 4: Ban Kiểm soát Thay đổi CCB Họp Quyết định]
       │
       ├─► [Bác bỏ / Yêu cầu làm rõ] ──► Thông báo lý do cho Người đề xuất
       │
       └─► [Chấp thuận Phê duyệt]
              │
              ▼
[Bước 5: Trích Quỹ Dự phòng, Cập nhật Backlog & Triển khai Lập trình / Kiểm thử]
```

### Chi tiết các bước thực hiện:
- **Bước 1: Điền Phiếu Yêu cầu Thay đổi**: Người đề xuất (thuộc CĐT hoặc Nhà thầu) điền đầy đủ các thông tin: Tiêu đề yêu cầu, lý do đề xuất, mô tả chi tiết tính năng, lợi ích mang lại và phòng ban thụ hưởng.
- **Bước 2: Phân tích tác động**: Trong vòng 48 giờ làm việc kể từ khi tiếp nhận, Giám đốc Dự án cùng Kiến trúc sư hệ thống và Chuyên viên phân tích nghiệp vụ tiến hành:
  - Xác định các mô-đun bị ảnh hưởng trên Web Selling Site System và Main System.
  - Tính toán số giờ công cần thiết theo từng vai trò chuyên môn.
  - Tính toán chi phí phát sinh dựa trên đơn giá giờ công đã chốt.
  - Đánh giá ảnh hưởng đối với lịch trình 8 Sprint và mốc Cut-over ngày 01/07.
- **Bước 3: Lập hồ sơ thẩm định**: Giám đốc Dự án tổng hợp Báo cáo Thẩm định Thay đổi, nêu rõ khuyến nghị kỹ thuật, phương án trích lập kinh phí từ quỹ dự phòng 260.490.000 VNĐ.
- **Bước 4: Quyết định của CCB**: CCB họp xem xét và ban hành Biên bản Quyết định Thay đổi. Quyết định có thể là: Chấp thuận, Bác bỏ hoặc Hoãn thực hiện sang giai đoạn 2.
- **Bước 5: Triển khai có kiểm soát**:
  - Nếu được chấp thuận, Chuyên viên phân tích nghiệp vụ tạo User Story tương ứng trong Product Backlog kèm tiêu chí nghiệm thu chi tiết.
  - Giám đốc Dự án cập nhật số dư quỹ dự phòng và đường cơ sở tiến độ.
  - Đội phát triển tiến hành lập trình, kiểm thử và bàn giao sản phẩm tăng trưởng trong Sprint được chỉ định.

---

## 6. Chế Độ Báo Cáo Và Nhật Ký Giám Sát Thay Đổi (Change Log)

Mọi yêu cầu thay đổi từ khi phát sinh đến khi hoàn tất nghiệm thu đều phải được ghi nhận và cập nhật trạng thái liên tục trong Nhật ký Quản lý Thay đổi dự án:

| Mã CR | Ngày tiếp nhận | Tiêu đề thay đổi | Người đề xuất | Giờ công ước tính | Chi phí sau VAT (VNĐ) | Tác động tiến độ | Tình trạng phê duyệt | Sprint triển khai | Ngày nghiệm thu |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| CR-01 | 18/03/2026 | Bổ sung phương thức thanh toán ví điện tử ShopeePay | ABC Wear | 45h | 11.250.000 | Không trễ Sprint | Đã phê duyệt | Sprint 5 | 22/05/2026 |
| CR-02 | 05/04/2026 | Mở rộng cấu trúc Selling DB lưu trữ 5 địa chỉ giao hàng | ABC Wear | 30h | 7.500.000 | Không trễ Sprint | Đã phê duyệt | Sprint 3 | 24/04/2026 |
| CR-03 | 15/05/2026 | Tích hợp kênh bán hàng qua mạng xã hội TikTok Shop | ABC Wear | 180h | 45.000.000 | Nguy cơ trễ 01/07 | Chuyển Giai đoạn 2 | Sau Cut-over | 15/08/2026 |

Báo cáo tình trạng xử lý thay đổi và số dư quỹ dự phòng được Giám đốc Dự án báo cáo định kỳ hằng tuần trong Báo cáo Tiến độ Dự án gửi tới Ban Giám đốc ABC Wear.
