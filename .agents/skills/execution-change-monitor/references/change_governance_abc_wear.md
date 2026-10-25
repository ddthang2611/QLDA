# Quy Chế Kiểm Soát Thay Đổi Và Giám Sát Thực Thi Dự Án ABC Wear

Tài liệu này xác lập quy chế kiểm soát thay đổi và giám sát thực thi đặc thù áp dụng cho Dự án Xây dựng Hệ thống Website Bán hàng Trực tuyến của Công ty Cổ phần ABC Wear. Quy chế kết hợp chặt chẽ giữa kỷ luật quản lý hợp đồng trọn gói với các phương pháp xử lý rủi ro và quản lý thay đổi linh hoạt từ chương trình đào tạo ICTPM.

---

## 1. Ranh Giới Phạm Vi và Các Ràng Buộc Hợp Đồng

### 1.1 Ranh giới ngoài phạm vi
Căn cứ tài liệu nguyên mẫu RFP của Công ty Cổ phần ABC Wear:
- Toàn bộ các chức năng quản trị nội bộ của ABC Wear nằm ngoài phạm vi của dự án này. Mọi đề xuất phát sinh liên quan đến quản trị hành chính nội bộ đều không thuộc phạm vi thực hiện của gói thầu.
- Thay thế hoặc nâng cấp hệ thống quản trị bán hàng hiện hữu Main System nằm ngoài phạm vi dự án. Nhà thầu chỉ xây dựng các bộ kết nối giao tiếp hai chiều qua lớp trung gian và mạng riêng ảo bảo mật, tuyệt đối không truy cập trực tiếp vào cơ sở dữ liệu Main System.

### 1.2 Ràng buộc thời hạn vận hành chính thức và định hướng xử lý linh hoạt
- Ngày đưa vào vận hành chính thức là ngày 01 tháng 07 năm 2026.
- Đây là mốc thời gian cam kết trọng yếu của dự án. Tuy nhiên, khi phát sinh các yêu cầu thay đổi mới từ chủ đầu tư hoặc từ thực tiễn thị trường, Ban quản lý dự án không áp dụng biện pháp bác bỏ cứng nhắc, mà bắt buộc phải chủ động áp dụng các phương pháp xử lý rủi ro và kỹ thuật nén tiến độ để hấp thu thay đổi tối đa mà vẫn bảo vệ an toàn mốc vận hành chính thức.

### 1.3 Ràng buộc ngân sách và loại hợp đồng
- Hợp đồng triển khai là hợp đồng trọn gói với tổng giá trị cố định 1.200.000.000 VNĐ đã bao gồm thuế giá trị gia tăng 10%.
- Định mức lao động toàn dự án đã được phê duyệt là 3.200 giờ công phân bổ cho 12 nhân sự chủ chốt.

---

## 2. Phân Định Ranh Giới Tuyệt Đối Giữa Lỗi Phần Mềm và Yêu Cầu Thay Đổi

Để ngăn ngừa tranh chấp và bảo vệ nguồn lực dự án, quy chế phân định rạch ròi bản chất giữa hai khái niệm:

### 2.1 Lỗi phần mềm
- **Định nghĩa**: Là trường hợp hệ thống hoạt động sai lệch, không chính xác, gián đoạn hoặc không đáp ứng các tiêu chí đã được xác lập trong tài liệu Đặc tả yêu cầu hệ thống, Đặc tả kỹ thuật, hoặc vi phạm các chỉ tiêu phi chức năng đã cam kết gồm thời gian phản hồi P95 vượt quá 2 giây ở mức tải 5.000 người dùng đồng thời, tỷ lệ sẵn sàng dưới 99,9%, sự cố an toàn thông tin OWASP.
- **Trách nhiệm chi phí**: Căn cứ thỏa thuận hợp đồng cơ sở tại Trang 3 của RFP, các sai sót về mặt logic trong sản phẩm bàn giao hoặc các sự cố khác thuộc trách nhiệm của nhà thầu, nhà thầu bắt buộc phải chỉnh sửa hoặc bổ sung bằng trách nhiệm và chi phí của chính nhà thầu trong thời gian sớm nhất có thể.
- **Quy trình xử lý**: Lỗi được ghi nhận vào Hệ thống Quản lý Lỗi, phân cấp độ nghiêm trọng từ 1 đến 4 và giao cho đội ngũ phát triển khắc phục ngay theo cam kết chất lượng, tuyệt đối không được tính phát sinh chi phí hoặc khấu trừ vào quỹ dự phòng.

### 2.2 Yêu cầu thay đổi
- **Định nghĩa**: Là trường hợp chủ đầu tư hoặc nhà thầu đề xuất bổ sung tính năng mới chưa từng có trong đặc tả đã phê duyệt, sửa đổi luồng nghiệp vụ đã nghiệm thu, thay đổi cấu trúc bảng cơ sở dữ liệu bán hàng ngoài thiết kế ban đầu, hoặc điều chỉnh quy cách tích hợp với hệ thống bên thứ ba phát sinh ngoài hợp đồng.
- **Trách nhiệm chi phí và tiến độ**: Yêu cầu thay đổi bắt buộc phải trải qua quy trình đánh giá tác động toàn diện về chi phí, giờ công và tiến độ, được cấp có thẩm quyền phê duyệt bằng văn bản trước khi bắt tay vào thực hiện.

---

## 3. Các Phương Pháp Xử Lý Rủi Ro và Quản Lý Thay Đổi Nhằm Bảo Vệ Tiến Độ

Thay vì từ chối hoặc bác bỏ các đề xuất thay đổi có nguy cơ làm ảnh hưởng tiến độ, chuyên gia quản lý dự án áp dụng hệ thống phương pháp luận xử lý rủi ro và thích ứng tiến độ toàn diện:

### 3.1 Năm chiến lược ứng phó rủi ro thực thi
Dựa trên chuẩn mực quản trị rủi ro dự án CNTT:
1. **Tránh rủi ro**: Điều chỉnh giải pháp kỹ thuật hoặc quy trình triển khai để triệt tiêu nguyên nhân gây rủi ro, ví dụ sử dụng kiến trúc lỏng lẻo với hàng đợi tin nhắn để tránh rủi ro sập luồng đơn hàng khi Main System bảo trì.
2. **Giảm thiểu rủi ro**: Thực hiện các hành động sớm nhằm giảm xác suất xảy ra hoặc giảm thiểu mức độ ảnh hưởng:
   - Thực hiện kiểm thử tích hợp sớm và liên tục ngay trong từng Sprint thay vì dồn vào cuối kỳ.
   - Xây dựng bản mẫu thử nghiệm đối với các giao diện phức tạp để chốt yêu cầu với người dùng.
   - Tổ chức đo tải hiệu năng sớm từ Sprint 4 để phát hiện các câu truy vấn cơ sở dữ liệu chạy chậm.
3. **Chuyển giao rủi ro**: Ký cam kết bảo lãnh ngân hàng BIDV đối với nghĩa vụ hợp đồng, thỏa thuận mức dịch vụ hỗ trợ kỹ thuật có điều khoản phạt với nhà cung cấp dịch vụ hạ tầng điện toán đám mây và cổng thanh toán trực tuyến.
4. **Chấp nhận rủi ro chủ động**:
   - Duy trì Quỹ dự phòng rủi ro kỹ thuật và quản lý thay đổi: 260.490.000 VNĐ sau VAT, chiếm 21,7% tổng giá trị hợp đồng.
   - Thiết lập vùng đệm tiến độ dự án an toàn từ ngày 21/06/2026 đến ngày 30/06/2026 để hấp thu các biến động công việc phát sinh.
5. **Kế hoạch ứng phó dự phòng**: Thiết lập sẵn kịch bản quay lui an toàn để khôi phục phiên bản phần mềm hoạt động ổn định trước đó trong vòng không quá 15 phút nếu việc triển khai bản cập nhật gặp sự cố nghiêm trọng.

### 3.2 Sáu chiến lược thích ứng thay đổi bảo vệ tiến độ
Khi một Yêu cầu Thay đổi được đề xuất và có nguy cơ tác động đến tiến độ mốc vận hành chính thức ngày 01/07/2026, Ban Kiểm soát Thay đổi đánh giá và áp dụng tuần tự 6 chiến lược thích ứng sau đây:

#### Chiến lược 1: Hoán đổi phạm vi tương đương Scope Swapping
- **Cơ chế**: Thương lượng với Chủ sản phẩm đại diện ABC Wear đưa tính năng mới có giá trị kinh doanh cấp thiết vào phạm vi Sprint, đồng thời rút bớt một hoặc một số tính năng có độ ưu tiên thấp hơn có quy mô giờ công tương đương ra khỏi Sprint đó để chuyển về Product Backlog.
- **Hiệu quả**: Tổng số giờ công của Sprint không đổi, chi phí không tăng, khách hàng nhận được tính năng mong muốn nhất và mốc vận hành 01/07/2026 được bảo vệ tuyệt đối.

#### Chiến lược 2: Nén tiến độ Schedule Crashing
- **Cơ chế**: Tăng cường nhân lực vào các công việc nằm trên đường găng, huy động các lập trình viên làm việc song song hoặc bố trí làm việc thêm giờ có định mức.
- **Nguồn tài chính**: Toàn bộ chi phí làm việc thêm giờ hoặc bổ sung nhân sự chuyên trách được trích chi trả từ Quỹ dự phòng rủi ro kỹ thuật và quản lý thay đổi 260.490.000 VNĐ đã được phê duyệt trong hợp đồng.
- **Hiệu quả**: Rút ngắn thời lượng thực hiện công việc trên đường găng để hoàn thành tính năng mới mà không làm dịch chuyển ngày hoàn thành dự án.

#### Chiến lược 3: Triển khai gối đầu Fast-tracking
- **Cơ chế**: Tái cấu trúc tiến độ, chuyển đổi các công việc vốn được lập kế hoạch làm tuần tự sang thực hiện song song hoặc gối đầu sớm:
  - Bắt đầu phát triển giao diện người dùng ngay khi khung dây được phê duyệt sơ bộ, không chờ hoàn thiện 100% bản mẫu chi tiết.
  - Tiến hành kiểm thử tích hợp từng thành phần API ngay khi lập trình viên hoàn thành việc viết mã, không đợi hoàn thành trọn vẹn cả phân hệ.
  - Chuẩn bị sẵn dữ liệu kiểm thử, kịch bản chuyển đổi dữ liệu và môi trường thử nghiệm song song với quá trình phát triển tính năng.
- **Hiệu quả**: Tiết kiệm thời gian chờ đợi, nén tổng thời lượng của Sprint từ 10% đến 20%.

#### Chiến lược 4: Phân kỳ phát hành lát cắt mỏng tối thiểu MVP
- **Cơ chế**: Chia nhỏ Yêu cầu Thay đổi thành hai giai đoạn phát hành:
  - Giai đoạn 1: Lát cắt cốt lõi tối thiểu Core MVP. Chỉ tập trung phát triển và kiểm thử phần cốt lõi nhất của tính năng thay đổi để kịp đưa vào vận hành chính thức ngày 01/07/2026, đáp ứng nhu cầu giao dịch thực tế của người dùng.
  - Giai đoạn 2: Hoàn thiện tính năng nâng cao. Các chức năng giao diện nâng cao, báo cáo thống kê mở rộng hoặc các tiện ích phụ trợ được chuyển sang triển khai trong thời gian 01 tháng trực vận hành tăng cường Hypercare từ 01/07 đến 31/07/2026 hoặc giai đoạn bảo hành 12 tháng.
- **Hiệu quả**: Khách hàng vẫn có tính năng để sử dụng ngay tại ngày khai trương mà không chịu rủi ro quá tải hệ thống.

#### Chiến lược 5: Khai thác vùng đệm tiến độ dự án
- **Cơ chế**: Theo kế hoạch tiến độ Mẫu số 10A đã chốt, toàn bộ 23 dịch vụ được lập lịch hoàn tất kiểm thử trước ngày 14/06/2026 và chuyển giao trước ngày 21/06/2026. Khoảng thời gian từ ngày 21/06/2026 đến ngày 30/06/2026 đóng vai trò là Vùng đệm Tiến độ an toàn của dự án.
- **Hiệu quả**: Nếu một đề xuất thay đổi có ý nghĩa chiến lược sống còn đối với hoạt động kinh doanh của ABC Wear, Ban Kiểm soát Thay đổi có thể cho phép sử dụng một phần vùng đệm tiến độ này để kiểm thử và đóng gói hoàn thiện mà vẫn kịp ngày Cut-over 01/07/2026.

#### Chiến lược 6: Đàm phán phụ lục hợp đồng hoặc lộ trình phân kỳ
- **Cơ chế**: Trường hợp yêu cầu thay đổi có quy mô quá lớn vượt ngoài khả năng hấp thu của 5 chiến lược trên:
  - Nếu ABC Wear kiên quyết triển khai trước ngày 01/07/2026: Hai bên đàm phán ký kết Phụ lục hợp đồng kinh tế, bổ sung kinh phí vượt hạn mức dự phòng và bổ sung nhân sự hỗ trợ đặc biệt.
  - Nếu không thể bổ sung kịp nguồn lực: Ban Kiểm soát Thay đổi phê duyệt chấp thuận yêu cầu thay đổi nhưng xác lập lộ trình triển khai chính thức trong Giai đoạn 2 ngay sau mốc Cut-over ngày 01/07/2026 nhằm bảo đảm hệ thống cốt lõi vận hành ổn định trước.

---

## 4. Quản Lý Quỹ Dự Phòng Rủi Ro Và Thay Đổi: 260.490.000 VNĐ

Trong cơ cấu ngân sách 1,2 tỷ VNĐ đã được phê duyệt:
- **Tên quỹ**: Chi phí dự phòng rủi ro kỹ thuật và quản lý thay đổi.
- **Giá trị quỹ**: 236.809.091 VNĐ trước VAT, tương đương **260.490.000 VNĐ sau VAT 10%**, chiếm 21,7% tổng giá trị hợp đồng.

### Nguyên tắc giải ngân quỹ dự phòng:
1. **Nguồn thanh toán cho các giải pháp thay đổi**: Quỹ này được sử dụng để chi trả cho các giờ công phát sinh do thực hiện Yêu cầu Thay đổi, chi phí làm thêm giờ khi nén tiến độ Schedule Crashing và chi phí mua sắm công cụ, bản quyền phát sinh phục vụ thay đổi.
2. **Đơn giá thanh toán minh bạch**: Giờ công phát sinh được tính toán đúng theo Bảng đơn giá giờ công đã phê duyệt trong hồ sơ dự thầu từ 208.947 VNĐ/h đến 320.000 VNĐ/h tùy vị trí chuyên môn.
3. **Phân cấp thẩm quyền phê duyệt trích quỹ**:
   - Yêu cầu thay đổi có chi phí dưới 50.000.000 VNĐ và đã có phương án nén tiến độ bảo đảm an toàn Sprint: Giám đốc Dự án nhà thầu và Đại diện nghiệp vụ chủ đầu tư Yamada đồng phê duyệt.
   - Yêu cầu thay đổi có chi phí từ 50.000.000 VNĐ đến hết hạn mức quỹ: Ban Kiểm soát Thay đổi họp xem xét và ra quyết định bằng văn bản.
   - Vượt quá hạn mức 260.490.000 VNĐ: Hai bên tiến hành đàm phán ký kết Phụ lục hợp đồng kinh tế theo quy định.

---

## 5. Ban Kiểm Soát Thay Đổi CCB

### 5.1 Thành phần nhân sự
1. **Đại diện Chủ đầu tư ABC Wear**: Ông Yamada - Phòng Kế hoạch, Chủ tịch CCB, đại diện lợi ích kinh doanh và thẩm quyền tài chính.
2. **Giám đốc Dự án Nhà thầu**: Ông Nguyễn Đức Tân, Thư ký CCB, điều hành quy trình thẩm định, đề xuất giải pháp tiến độ và chi phí.
3. **Kiến trúc sư Hệ thống**: Ông Nguyễn Hải Đăng, Thành viên CCB, chịu trách nhiệm thẩm định kiến trúc, an toàn thông tin và giải pháp kỹ thuật nén tiến độ.
4. **Chuyên viên Phân tích Nghiệp vụ**: Ông Đinh Đức Thắng, Thành viên CCB, phân tích quy trình nghiệp vụ, ranh giới phạm vi và cập nhật Product Backlog.

### 5.2 Ma trận phân công trách nhiệm RACI của CCB

| Hoạt động kiểm soát thay đổi | Yamada (CĐT) | Nguyễn Đức Tân (PM) | Nguyễn Hải Đăng (SA) | Đinh Đức Thắng (BA) |
| :--- | :---: | :---: | :---: | :---: |
| Tiếp nhận và sơ loại đề xuất thay đổi | I | A/R | C | C |
| Phân tích tác động nghiệp vụ và hoán đổi phạm vi | C | A | C | R |
| Đánh giá kỹ thuật và xây dựng phương án nén tiến độ | I | A | R | C |
| Dự toán chi phí và xây dựng phương án trích quỹ | C | A/R | C | C |
| Lựa chọn chiến lược thích ứng tiến độ bảo vệ mốc 01/07 | C | A/R | C | C |
| Quyết nghị phê duyệt giải pháp thay đổi và trích quỹ | A | R | C | I |
| Cập nhật Product Backlog và điều phối thực thi | I | A | C | R |
| Nghiệm thu kết quả triển khai thay đổi | A | R | C | C |

---

## 6. Quy Trình 5 Bước Phê Duyệt Và Thích Ứng Thay Đổi Thực Chiến

```
[Bước 1: Tiếp nhận Đề xuất CR]
       │
       ▼
[Bước 2: Phân tích Tác động & Xây dựng Giải pháp Thích ứng] (Tối đa 48 giờ)
       │ (Đánh giá: Hoán đổi phạm vi / Nén tiến độ Crashing / Gối đầu Fast-tracking / Phân kỳ Lát cắt mỏng MVP)
       ▼
[Bước 3: Lập Hồ sơ Thẩm định & Đề xuất Phương án Kỹ thuật]
       │
       ▼
[Bước 4: Ban Kiểm soát Thay đổi CCB Họp Quyết định Lựa chọn Giải pháp]
       │
       ├─► [Chấp thuận Triển khai Ngay] ──► Kích hoạt Hoán đổi phạm vi hoặc Nén tiến độ (Crashing / Fast-tracking)
       ├─► [Chấp thuận Phân kỳ MVP]    ──► Phát hành phần cốt lõi trước 01/07, phần nâng cao đưa vào Hypercare
       └─► [Hoãn có Lộ trình]          ──► Chuyển sang Giai đoạn 2 sau khi hệ thống vận hành chính thức ổn định
       │
       ▼
[Bước 5: Trích Quỹ Dự phòng, Cập nhật Backlog & Triển khai Lập trình / Kiểm thử]
```

### Chi tiết các bước thực hiện:
- **Bước 1: Tiếp nhận đề xuất**: Người đề xuất điền đầy đủ Phiếu Yêu cầu Thay đổi nêu rõ lý do, mô tả tính năng và giá trị mang lại.
- **Bước 2: Phân tích tác động và tìm kiếm giải pháp thích ứng**: Trong vòng 48 giờ làm việc, nhóm quản lý dự án không chỉ tính toán chi phí và giờ công phát sinh, mà bắt buộc phải chủ động xây dựng ít nhất một phương án nén tiến độ (hoán đổi phạm vi hoặc làm song song) để duy trì mốc Cut-over ngày 01/07/2026.
- **Bước 3: Lập hồ sơ thẩm định**: Giám đốc Dự án lập Báo cáo Thẩm định Thay đổi, so sánh các phương án thực hiện (làm ngay bằng crashing/fast-tracking, làm lát cắt mỏng MVP, hoặc hoãn có lộ trình), dự toán kinh phí trích từ quỹ dự phòng 260.490.000 VNĐ.
- **Bước 4: Quyết định của CCB**: CCB họp thống nhất lựa chọn giải pháp tối ưu nhất cho hoạt động kinh doanh của ABC Wear.
- **Bước 5: Triển khai có kiểm soát**: Cập nhật Product Backlog, giải ngân kinh phí từ quỹ dự phòng, phân bổ công việc vào các Sprint và giám sát thực thi theo Definition of Done.

---

## 7. Chế Độ Báo Cáo Và Nhật Ký Giám Sát Thay Đổi (Change Log)

Mọi yêu cầu thay đổi từ khi phát sinh đến khi hoàn tất nghiệm thu đều được theo dõi tập trung trong Nhật ký Quản lý Thay đổi:

| Mã CR | Ngày tiếp nhận | Tiêu đề thay đổi | Người đề xuất | Giờ công ước tính | Chi phí sau VAT (VNĐ) | Chiến lược thích ứng áp dụng | Tình trạng phê duyệt | Sprint triển khai | Ngày nghiệm thu |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| CR-01 | 18/03/2026 | Bổ sung phương thức thanh toán ví điện tử ShopeePay | ABC Wear | 45h | 11.250.000 | Nén tiến độ Crashing | Đã phê duyệt | Sprint 5 | 22/05/2026 |
| CR-02 | 05/04/2026 | Mở rộng cấu trúc Selling DB lưu trữ 5 địa chỉ giao hàng | ABC Wear | 30h | 7.500.000 | Hoán đổi tính năng | Đã phê duyệt | Sprint 3 | 24/04/2026 |
| CR-03 | 15/05/2026 | Tích hợp kênh bán hàng qua mạng xã hội TikTok Shop | ABC Wear | 180h | 45.000.000 | Phân kỳ phát hành MVP | Đã phê duyệt | MVP Sprint 6, mở rộng Hypercare | 05/06/2026 (MVP) & 20/07/2026 |

Báo cáo tình trạng xử lý thay đổi, việc áp dụng các chiến lược thích ứng và số dư Quỹ dự phòng được Giám đốc Dự án báo cáo định kỳ vào thứ Sáu hằng tuần trong Báo cáo Tiến độ Dự án gửi tới Ban Giám đốc ABC Wear.
