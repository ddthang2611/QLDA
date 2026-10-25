# BIÊN BẢN THẢO LUẬN NỘI BỘ PHÍA NHÀ THẦU
## Đánh Giá Rủi Ro, Tác Động Của Yêu Cầu Thay Đổi CR-2026-004, Định Lượng Làm Thêm Giờ OT Và Lựa Chọn Chiến Lược Ứng Phó
### Dự Án: Xây Dựng Hệ Thống Kênh Bán Hàng Qua Internet Cho Chuỗi Cửa Hàng ABC Wear — Gói Thầu: ABC-WSS-PM_26I_09

* **Đơn vị chủ trì:** Ban Điều hành Dự án phía Nhà thầu Nhóm 09 - 20261
* **Thời gian cuộc họp:** 09 giờ 00 ngày 15 tháng 04 năm 2026
* **Địa điểm:** Phòng họp Kỹ thuật Nhà thầu và kết nối trực tuyến
* **Thành phần tham dự:**
  - Giám đốc Dự án PM — Chủ trì cuộc họp
  - Kiến trúc sư Hệ thống SA — Báo cáo kỹ thuật tích hợp
  - Chuyên viên Phân tích Nghiệp vụ BA — Báo cáo tình trạng thông tin gian hàng
  - Trưởng nhóm Kỹ sư Lập trình DEV — Báo cáo khối lượng công việc và giờ công OT
  - Trưởng nhóm Chuyên viên Kiểm thử QC — Báo cáo kịch bản kiểm thử tải đa kênh
  - Kỹ sư Hạ tầng và Vận hành OPS — Báo cáo hạ tầng gateway và sandbox

---

### I. BỐI CẢNH VÀ NGUYÊN NHÂN PHÁT SINH RỦI RO LÀM THÊM GIỜ OT

Sau khi tiếp nhận Yêu cầu Thay đổi CR-2026-004 ngày 10 tháng 04 năm 2026 về việc mở rộng bán hàng đa kênh trên Shopee, TikTok Shop và Facebook Shop, Đội ngũ Kỹ thuật Nhà thầu đã tiến hành khảo sát thực tế và phát hiện hai nhóm rào cản phát sinh nghiêm trọng:

#### 1. Thiếu hụt và chậm trễ thông tin cấu hình gian hàng từ phía Chủ đầu tư ABC Wear
- Phía Chủ đầu tư chưa hoàn tất việc chuẩn hóa tài khoản doanh nghiệp chính thức trên Shopee Open Platform và TikTok Shop Partner Center.
- Bảng phân loại biến thể thời trang cha con, ma trận kích cỡ và bảng thuộc tính chi tiết ngành hàng của 25 cửa hàng chưa đồng bộ, dẫn đến việc thiếu hụt dữ liệu đầu vào để cấu hình ánh xạ Category Mapping.
- Bộ phận bán lẻ của Bên A liên tục bổ sung các yêu cầu nghiệp vụ chuyên biệt về chính sách giá bán khác nhau giữa sàn thương mại điện tử và website bán hàng chính thức, đòi hỏi phải tái lập trình logic tính toán giá và khuyến mại.

#### 2. Rào cản kỹ thuật phức tạp trong khâu tích hợp nền tảng số bên ngoài
- Cơ chế xác thực OAuth 2.0 của Shopee và TikTok Shop đòi hỏi chu kỳ làm mới Token tự động phức tạp và quản lý phiên bảo mật nghiêm ngặt.
- Tần suất giới hạn gọi API Rate Limiting của các sàn rất khắt khe. Nếu hệ thống đồng bộ tồn kho đẩy dữ liệu quá nhanh sẽ bị sàn tự động khóa cổng giao tiếp từ 15 đến 30 phút.
- Luồng Webhook nhận thông báo đơn hàng mới từ các sàn có độ trễ bất định, kèm theo nguy cơ gửi trùng lặp bản tin Webhook khi mạng gián đoạn, đòi hỏi phải thiết kế bổ sung tầng đệm xử lý khóa chống trùng lặp Idempotency Key và hàng đợi RabbitMQ độc lập.

#### 3. Hệ quả đối với đội ngũ triển khai Nhà thầu
Để hấp thu toàn bộ các yêu cầu phát sinh trên mà vẫn bảo vệ được mốc vận hành chính thức ngày 15 tháng 07 năm 2026 đã thỏa thuận tại Phụ lục Hợp đồng số 01/2026/PLHĐ-ABCWEAR, đội ngũ kỹ thuật Nhà thầu bắt buộc phải tổ chức làm thêm giờ tăng cường OT vào các buổi tối ngày trong tuần và các ngày Thứ Bảy xuyên suốt từ Sprint 4 đến Sprint 8.

---

### II. ĐÁNH GIÁ TOÀN DIỆN TÁC ĐỘNG CỦA YÊU CẦU THAY ĐỔI CR-2026-004

Ban Điều hành Dự án Nhà thầu tiến hành đánh giá tác động của CR-2026-004 trên 5 khía cạnh trọng yếu:

#### 1. Tác động về Phạm vi công việc
- Bổ sung 4 nhóm module kỹ thuật kết nối: Module API Gateway Omnichannel Connector độc lập kết nối Shopee Open Platform, TikTok Shop Open API và Facebook Graph API; Cấu trúc Selling DB mở rộng bảng ánh xạ danh mục Category Mapping và biến thể thời trang; Bộ thu nhận sự kiện Webhook Receiver kèm cơ chế khóa chống trùng lặp Idempotency Key; Cơ chế đồng bộ tồn kho thời gian thực chu kỳ 15 phút với thuật toán kiểm soát tần suất Rate Limiting.
- Kiểm soát nghiêm ngặt ranh giới hợp đồng: Giữ vững cam kết loại trừ toàn bộ các chức năng quản trị nội bộ của 25 cửa hàng ABC Wear gồm bán hàng tại quầy, quản trị sản phẩm tổng thể, logistics kho bãi, giao dịch kế toán nội bộ và điều phối giao nhận của Main System ra khỏi phạm vi dự án; tuyệt đối không can thiệp trực tiếp cơ sở dữ liệu Main System.

#### 2. Tác động về Tiến độ thực hiện
- Khối lượng kỹ thuật phát sinh: 120 giờ công kỹ thuật tiêu chuẩn trong giờ hành chính gồm Kiến trúc sư Hệ thống SA 30 giờ, Kỹ sư Lập trình DEV 90 giờ; bổ sung 250 giờ làm thêm giờ ngoài giờ OT gồm SA 30 giờ, DEV 160 giờ, Chuyên viên Kiểm thử QC 60 giờ.
- Tái cấu trúc chu kỳ phát triển: Mở rộng từ 15,5 tuần gồm 8 Sprint sang 17,5 tuần gồm 9 Sprint Agile Scrum.
- Điều chỉnh mốc vận hành chính thức: Căn cứ Phụ lục Hợp đồng Kinh tế số 01/2026/PLHĐ-ABCWEAR ký ngày 14 tháng 04 năm 2026, mốc Go-live được lùi 02 tuần hợp pháp từ ngày 01 tháng 07 năm 2026 sang ngày 15 tháng 07 năm 2026, hoàn toàn nằm trong giới hạn tối đa 03 tuần theo Điều 1 và Điều 4 của hợp đồng gốc.
- Mốc bảo vệ hỗ trợ vận hành Hypercare: Điều chỉnh kéo dài 01 tháng từ ngày 15 tháng 07 năm 2026 đến ngày 15 tháng 08 năm 2026.
- Thời hạn bảo hành: 12 tháng tính từ ngày 15 tháng 07 năm 2026 đến ngày 14 tháng 07 năm 2027.

#### 3. Tác động về Chi phí và Ngân sách
- Bảo toàn tuyệt đối giá trị hợp đồng trọn gói: Tổng giá trị hợp đồng trọn gói giữ nguyên 1.200.000.000 VNĐ sau thuế, Bên A không phát sinh bất kỳ khoản kinh phí ngoài hợp đồng nào.
- Kinh phí giải ngân xử lý rủi ro OT: Đúng 103.950.000 VNĐ sau thuế, tương đương 94.500.000 VNĐ trước thuế và 9.450.000 VNĐ tiền thuế GTGT 10%, được trích chi trả 100% từ Quỹ dự phòng rủi ro kỹ thuật và quản lý thay đổi 260.490.000 VNĐ, chiếm tỷ lệ giải ngân 39,91% tổng quỹ.
- Số dư Quỹ dự phòng an toàn khả dụng còn lại: 156.540.000 VNĐ sau thuế, tương đương 142.309.091 VNĐ trước thuế, chiếm 13,05% tổng giá trị hợp đồng, tiếp tục đóng vai trò vùng đệm tài chính dự phòng an toàn cho toàn bộ các Sprint tiếp theo.

#### 4. Tác động về Chất lượng và Cam kết Mức Dịch vụ SLA
- Gia tăng độ phức tạp trong kiểm thử tích hợp: Phải tiến hành kiểm thử thông luồng SIT và UAT trong môi trường mạng diện rộng phụ thuộc chính sách của bên thứ ba.
- Giữ vững các cam kết chất lượng phi chức năng: Tốc độ phản hồi giao dịch tổng thể P95 không vượt quá 2 giây ở mức tải đỉnh 5.000 người dùng; Tốc độ phản hồi Webhook tiếp nhận đơn hàng trong vòng dưới 100ms; Độ sẵn sàng Uptime đạt tối thiểu 99,9% trong chế độ vận hành 24/7/365.

#### 5. Tác động về Nguồn lực và Tổ chức
- Gia tăng áp lực công việc lên đội ngũ kỹ thuật Nhà thầu: SA, DEV, QC phải làm việc ngoài giờ tập trung trong 5 Sprint liên tiếp từ Sprint 4 đến Sprint 8, đòi hỏi kỷ luật điều hành và chế độ đãi ngộ thỏa đáng.
- Nâng cao trách nhiệm phối hợp của Chủ đầu tư ABC Wear: Phía Bên A phải cử đầu mối nghiệp vụ hỗ trợ kịp thời và hoàn tất bàn giao thông tin gian hàng đúng thời hạn cam kết.

---

### III. MAPPING VỚI KHUNG QUẢN TRỊ THAY ĐỔI

Ban Điều hành Dự án Nhà thầu áp dụng chuẩn xác Quy trình 6 bước Quản lý Thay đổi quy định trong Kế hoạch Quản lý Thay đổi của dự án:

#### 1. Bước 1 — Nhận diện thay đổi
- Tiếp nhận văn bản đề xuất thay đổi CR-2026-004 từ Chủ đầu tư ngày 10 tháng 04 năm 2026.
- Phân loại thay đổi: Thuộc nhóm thay đổi kiến trúc kết nối nền tảng thương mại điện tử bên ngoài.
- Rà soát ranh giới phạm vi: Xác định việc kết nối bán hàng đa kênh thuộc phạm vi xây dựng hệ thống kênh số của Nhà thầu; kiên quyết loại trừ các nghiệp vụ bán hàng tại quầy và điều phối kho bãi nội bộ của Bên A.

#### 2. Bước 2 — Chi tiết hóa thay đổi
- Phân tích chi tiết yêu cầu kỹ thuật: Xây dựng Omnichannel Connector, mở rộng Selling DB bảng ánh xạ danh mục, thiết kế Webhook Receiver và hàng đợi RabbitMQ.
- Bóc tách WBS bổ sung: Xác lập 4 gói công việc WBS 3.9, 3.10, 3.11, 3.12.
- Định lượng giờ công và chi phí: Xác định 120 giờ công kỹ thuật hành chính và 250 giờ OT ngoài giờ với kinh phí 103.950.000 VNĐ sau thuế.

#### 3. Bước 3 — Phương pháp tiếp cận chuyển đổi
- Vận hành cơ chế Hội đồng CCB: Trình phương án kỹ thuật và kế hoạch điều chỉnh đường cơ sở để Hội đồng Ban Kiểm soát Thay đổi CCB thẩm định.
- Áp dụng trường phái Thích ứng Môi trường và Mô hình 5 bước ADKAR: Chuẩn bị nhận thức Awareness và năng lực Ability cho đội ngũ kỹ thuật Nhà thầu; phối hợp tạo sự đồng thuận từ phía bộ phận bán lẻ và khối kinh doanh ABC Wear.

#### 4. Bước 4 — Xây dựng chiến lược thực thi thích ứng
Nhà thầu kích hoạt đồng thời 3 trong 6 chiến lược thích ứng để hấp thu thay đổi:
- **Chiến lược Nén tiến độ Schedule Crashing:** Huy động làm thêm giờ ngoài giờ OT có định mức 250 giờ cho SA, DEV, QC trên đường găng; kinh phí trích từ Quỹ dự phòng rủi ro.
- **Chiến lược Triển khai gối đầu Fast-tracking:** Cho phép SA thiết kế kiến trúc Gateway song song với việc DEV dựng khung Adapter và QC xây dựng kịch bản kiểm thử tải đa kênh.
- **Chiến lược Khai thác vùng đệm gia hạn tiến độ:** Đàm phán lùi mốc Go-live thêm 02 tuần đến ngày 15 tháng 07 năm 2026 để san sẻ áp lực và tạo Sprint 9 chuyên biệt cho UAT trên dữ liệu thật.

#### 5. Bước 5 — Đóng gói triển khai
- Thống nhất ký kết Phụ lục Hợp đồng Kinh tế số 01/2026/PLHĐ-ABCWEAR ghi nhận mốc vận hành chính thức mới 15 tháng 07 năm 2026.
- Cập nhật số liệu vào Tài liệu quá trình thực thi thay đổi và Báo cáo tiến độ dự án.

#### 6. Bước 6 — Đánh giá và duy trì sau thay đổi
- Đo kiểm nghiêm ngặt tiêu chuẩn SLA P95 dưới 2 giây và độ sẵn sàng 99,9% trong các phiên diễn tập tải Sprint 8 và Sprint 9.
- Thiết lập kế hoạch trực hỗ trợ Hypercare 30 ngày bảo vệ doanh thu bán hàng đa kênh cho ABC Wear.

---

### IV. MAPPING VỚI KHUNG XỬ LÝ RỦI RO VÀ LỰA CHỌN CHIẾN LƯỢC ỨNG PHÓ

Hội nghị tiến hành phân tích sâu 4 chiến lược xử lý rủi ro kinh điển và định danh phương án ứng phó tối ưu:

#### 1. Chiến lược Phòng tránh rủi ro — Risk Avoidance
- **Đánh giá Phương án 1 — Từ chối làm thêm giờ OT và yêu cầu Chủ đầu tư lùi lịch 1 đến 2 tháng:**
  - *Bản chất:* Đây là nỗ lực phòng tránh rủi ro kỹ thuật và áp lực quá tải nhân sự một cách cực đoan.
  - *Hậu quả tiêu cực:* Khiến Nhà thầu vi phạm thỏa thuận khung hợp đồng về giới hạn gia hạn tối đa 03 tuần; làm lỡ chiến dịch bán hàng trọng điểm mùa hè của ABC Wear; gây thiệt hại uy tín doanh nghiệp và phát sinh nguy cơ tranh chấp pháp lý giữ tiền bảo lãnh thực hiện hợp đồng 30.000.000 VNĐ.
  - *Kết luận:* Bác bỏ hoàn toàn phương án né tránh tiêu cực này.
- **Ứng dụng phòng tránh có chọn lọc đối với Lạm phát phạm vi:**
  - Nhà thầu kiên quyết áp dụng chiến lược phòng tránh rủi ro lạm phát phạm vi bằng cách từ chối tuyệt đối mọi yêu cầu can thiệp vào các chức năng quản trị nội bộ của 25 cửa hàng và cơ sở dữ liệu Main System, bảo vệ tính toàn vẹn của ranh giới hợp đồng.

#### 2. Chiến lược Chuyển giao rủi ro — Risk Transfer
- **Đánh giá Phương án 2 — Đòi tăng giá gói thầu thêm 103,95 triệu đồng qua Phụ lục bổ sung ngân sách:**
  - *Bản chất:* Đây là nỗ lực chuyển giao toàn bộ rủi ro chi phí phát sinh sang cho Chủ đầu tư Bên A.
  - *Hậu quả tiêu cực:* Hợp đồng đã ký kết là Hợp đồng trọn gói 1,2 tỷ VNĐ. Thủ tục xin phê duyệt bổ sung ngân sách từ Hội đồng Quản trị ABC Wear mất từ 4 đến 6 tuần, gây tê liệt tiến độ toàn dự án và làm xấu đi quan hệ đối tác chiến lược.
  - *Kết luận:* Bác bỏ phương án chuyển giao chi phí này.
- **Ứng dụng chuyển giao có chọn lọc đối với Trách nhiệm thông tin:**
  - Nhà thầu áp dụng chuyển giao rủi ro thiếu hụt thông tin bằng cách xác lập văn bản yêu cầu Chủ đầu tư ABC Wear cam kết hoàn tất 5 điều kiện phối hợp gồm đăng ký tài khoản, cấp quyền API Sandbox và bàn giao 500 mặt hàng mẫu trước ngày 22 tháng 04 năm 2026. Nếu Bên A chậm trễ, trách nhiệm làm chậm mốc kiểm thử sẽ thuộc về Bên A.

#### 3. Chiến lược Giảm thiểu rủi ro — Risk Mitigation
Nhà thầu áp dụng đồng bộ các giải pháp giảm thiểu rủi ro kỹ thuật, tiến độ và nhân sự:
- **Giảm thiểu rủi ro chậm trễ tiến độ:** Kích hoạt chiến lược Nén tiến độ Schedule Crashing qua việc tổ chức 250 giờ làm thêm giờ ngoài giờ OT từ Sprint 4 đến Sprint 8, bù đắp thời gian chờ đợi thông tin gian hàng và xử lý kỹ thuật phức tạp.
- **Giảm thiểu rủi ro lỗi kỹ thuật kết nối:** Xây dựng bộ giả lập Mock Server để lập trình độc lập; thiết kế bộ nhớ đệm kiểm soát tần suất Leaky Bucket chống khóa API Rate Limiting; tích hợp tầng đệm Idempotency Key và hàng đợi RabbitMQ độc lập chống trùng lặp Webhook.
- **Giảm thiểu rủi ro quá tải nhân lực:** Khống chế định mức OT không quá 3 giờ mỗi buổi tối và không quá 12 giờ mỗi tuần; tổ chức nghỉ bù luân phiên sau các đợt phát hành tải ban đêm; chi trả phụ cấp làm đêm và bồi dưỡng ăn uống đầy đủ.
- **Giảm thiểu rủi ro hiệu năng vi phạm SLA:** Tách biệt hoàn toàn luồng đồng bộ tồn kho 15 phút với luồng phục vụ người mua hàng trên website; cấu hình bộ nhớ đệm Redis và CDN ảnh WebP giữ thời gian phản hồi P95 luôn dưới 2 giây.

#### 4. Chiến lược Chấp nhận rủi ro — Risk Acceptance
- **Áp dụng chiến lược Chủ động chấp nhận rủi ro tài chính:**
  - Ban Quản lý Dự án Nhà thầu nhận diện chi phí phát sinh làm thêm giờ OT và hạ tầng kiểm thử 103.950.000 VNĐ sau thuế là hệ quả tất yếu để hoàn thành yêu cầu kết nối đa kênh theo đúng tiến độ gia hạn 15 tháng 07 năm 2026.
  - Nhà thầu chủ động chấp nhận rủi ro tài chính này bằng việc kích hoạt **Quỹ dự phòng rủi ro kỹ thuật và quản lý thay đổi 260.490.000 VNĐ** đã được thỏa thuận tại Điều 5 và Điều 9 Hợp đồng gốc.
  - Toàn bộ kinh phí 103.950.000 VNĐ sau thuế được hạch toán giải ngân từ quỹ dự phòng nội bộ, bảo toàn nguyên vẹn giá trị hợp đồng trọn gói 1.200.000.000 VNĐ của Chủ đầu tư và duy trì số dư dự phòng khả dụng 156.540.000 VNĐ cho các Sprint tiếp theo.
- **Đánh giá quyết định:** Đây là giải pháp xử lý rủi ro tối ưu nhất, giải quyết đồng thời bài toán kỹ thuật, tiến độ, tài chính và quan hệ đối tác.

---

### V. ĐỊNH LƯỢNG CHI TIẾT KHỐI LƯỢNG GIỜ CÔNG VÀ KINH PHÍ LÀM THÊM GIỜ OT

Ban Điều hành Dự án và các Trưởng nhóm chuyên môn đã tính toán chi tiết định mức 250 giờ công làm thêm ngoài giờ cần thiết để giải quyết rủi ro kỹ thuật và bù đắp thông tin gian hàng:

| Vị trí chuyên môn | Khối lượng OT kế hoạch | Đơn giá công nhật OT thỏa thuận | Thành tiền trước thuế | Mục đích sử dụng giờ công OT |
| :--- | :---: | :---: | :---: | :--- |
| **Kiến trúc sư Hệ thống SA** | 30 giờ OT | 570.000 đ/giờ — Hệ số OT 150% | 17.100.000 đ | Xử lý kiến trúc Gateway, giải pháp làm mới Token OAuth2, tối ưu thuật toán Leaky Bucket chống khóa API sàn |
| **Kỹ sư Lập trình DEV** | 160 giờ OT | 360.000 đ/giờ — Hệ số OT 150% | 57.600.000 đ | Lập trình ngoài giờ 3 bộ kết nối Omnichannel Connector, xây dựng bảng ánh xạ danh mục và xử lý Webhook Receiver |
| **Chuyên viên Kiểm thử QC** | 60 giờ OT | 330.000 đ/giờ — Hệ số OT 150% | 19.800.000 đ | Kiểm thử tích hợp SIT tải cao ban đêm, đo kiểm khả năng chịu tải Webhook đồng thời từ 3 sàn và kịch bản Rollback |
| **Hạ tầng Sandbox và Proxy Test** | Trọn gói | — | 2.327.273 đ | Thuê tài khoản môi trường thử nghiệm nâng cao và dịch vụ mạng kiểm thử độc lập cho các sàn |
| **Tổng chi phí trước thuế** | **250 giờ OT** | — | **94.500.000 đ** | **Khối lượng kỹ thuật trực tiếp xử lý rủi ro** |
| **Thuế giá trị gia tăng 10%** | — | — | **9.450.000 đ** | **Thuế GTGT theo quy định** |
| **Tổng chi phí OT sau thuế** | — | — | **103.950.000 đ** | **Đẩy toàn bộ vào Quỹ dự phòng rủi ro kỹ thuật** |

---

### VI. KẾ HOẠCH HÀNH ĐỘNG VÀ BIỆN PHÁP BẢO VỆ NHÂN SỰ

Để bảo đảm việc làm thêm giờ OT đạt hiệu quả kỹ thuật cao nhất và không gây suy giảm sức khỏe của đội ngũ, Giám đốc Dự án PM chỉ đạo thực hiện 4 biện pháp kiểm soát:
1. **Quy chế giới hạn giờ làm thêm OT:**
   - Mỗi nhân sự làm thêm không quá 03 giờ mỗi buổi tối và không quá 12 giờ OT mỗi tuần.
   - Bố trí các ngày nghỉ bù luân phiên sau các đợt phát hành kiểm thử tải ban đêm.
   - Nhà thầu chi trả chế độ bồi dưỡng ăn tối và phụ cấp đi lại ca đêm đầy đủ cho nhân sự tham gia OT.
2. **Kỷ luật bàn giao từ phía Chủ đầu tư ABC Wear:**
   - Gửi văn bản chính thức yêu cầu Chủ sản phẩm PO và Phòng Kế hoạch ABC Wear phải bàn giao dứt điểm mã kết nối API gian hàng và bộ dữ liệu sản phẩm mẫu trước ngày 22 tháng 04 năm 2026.
   - Trường hợp Bên A chậm trễ vượt quá thời hạn cam kết, Nhà thầu sẽ lập biên bản sự việc và kích hoạt điều khoản bảo vệ tiến độ hợp đồng.
3. **Ưu tiên kiểm thử tự động hóa CI/CD:**
   - SA và DEV xây dựng các bộ giả lập Mock Server để kiểm thử kết nối API Shopee và TikTok Shop trong thời gian chờ sàn cấp quyền Production, giảm thiểu tối đa thời gian chờ đợi thụ động.
4. **Cập nhật hồ sơ quá trình thực thi:**
   - Giao PM chỉ đạo cập nhật toàn bộ phương án chi phí OT 103.950.000 VNĐ, số dư Quỹ dự phòng 156.540.000 VNĐ và chiến lược ứng phó rủi ro vào tài liệu quá trình thực thi thay đổi và báo cáo tiến độ dự án.

---

### VII. KẾT LUẬN VÀ NGHỊ QUYẾT HỘI NGHỊ NỘI BỘ
1. Toàn thể Ban Quản lý Dự án và Đội ngũ Kỹ thuật Nhà thầu thống nhất 100% lựa chọn phối hợp hai chiến lược: **Giảm thiểu rủi ro: nén tiến độ qua 250 giờ OT** và **Chủ động chấp nhận rủi ro tài chính: giải ngân 103.950.000 VNĐ từ Quỹ dự phòng**.
2. Phê duyệt định mức giải ngân 103.950.000 VNĐ sau thuế từ Quỹ dự phòng rủi ro kỹ thuật và quản lý thay đổi để chi trả cho các hoạt động làm thêm giờ OT và xử lý kỹ thuật tích hợp đa kênh.
3. Bảo toàn nguyên vẹn giá trị hợp đồng trọn gói 1.200.000.000 VNĐ, không phát sinh chi phí ngoài hợp đồng cho Chủ đầu tư ABC Wear.
4. Bảo đảm số dư Quỹ dự phòng an toàn khả dụng còn lại 156.540.000 VNĐ sau thuế để kiểm soát toàn diện các biến động trong các Sprint tiếp theo.
5. Biên bản này được lưu trữ nội bộ làm căn cứ đối soát chi phí nhân công và giải ngân tài chính của Nhà thầu.
