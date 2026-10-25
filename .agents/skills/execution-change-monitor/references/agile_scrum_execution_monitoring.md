# Hướng Dẫn Giám Sát Thực Thi Dự Án Theo Chuẩn Mực Agile Scrum 2020

Tài liệu này chuẩn hóa phương pháp luận giám sát và kiểm soát thực thi dự án dựa trên tài liệu Hướng Dẫn Scrum 2020 (Scrum Guide 2020). Tài liệu cung cấp cơ chế vận hành kỷ luật, kiểm soát chất lượng và xử lý thay đổi thích ứng trong quá trình phát triển sản phẩm phần mềm.

---

## 1. Nền Tảng Thực Nghiệm và Nguyên Tắc Giám Sát

Scrum vận hành dựa trên Thuyết thực nghiệm và Tư duy tinh gọn. Giám sát thực thi dự án theo Agile Scrum tập trung vào ba trụ cột cốt lõi:
1. **Minh bạch (Transparency)**: Mọi quy trình, trạng thái công việc và sản phẩm tăng trưởng phải được hiển thị rõ ràng cho cả đội ngũ phát triển và các bên liên quan. Không che giấu lỗi, không báo cáo tiến độ ảo dựa trên khối lượng công việc đang dang dở.
2. **Thanh tra (Inspection)**: Các hạng mục công việc và tiến độ hướng tới mục tiêu phải được kiểm tra định kỳ, liên tục tại các sự kiện Scrum nhằm phát hiện sớm các sai lệch hoặc suy giảm chất lượng.
3. **Thích ứng (Adaptation)**: Khi một quy trình hoặc kết quả sản phẩm bị lệch ra ngoài giới hạn chấp nhận, quy trình hoặc tài liệu yêu cầu phải được điều chỉnh ngay lập tức để ngăn ngừa lãng phí và rủi ro.

Năm giá trị Scrum là kim chỉ nam cho hành vi giám sát: Cam kết, Tập trung, Cởi mở, Tôn trọng và Dũng cảm.

---

## 2. Trách Nhiệm Giám Sát Của Các Vai Trò Trong Đội Scrum

Đội Scrum là một tập thể thống nhất gồm các chuyên gia tập trung vào một Mục tiêu Sản phẩm duy nhất:

### 2.1 Các Nhà phát triển (Developers)
- Chịu trách nhiệm trực tiếp về việc lập kế hoạch cho Sprint (Sprint Backlog).
- Đảm bảo chất lượng bằng cách tuân thủ nghiêm ngặt Định nghĩa Hoàn thành (Definition of Done) cho từng tính năng.
- Tự tổ chức, chủ động thích ứng kế hoạch hằng ngày tại buổi Họp Scrum hằng ngày để đạt được Mục tiêu Sprint.
- Giữ trách nhiệm giải trình lẫn nhau về năng suất và chất lượng kỹ thuật.

### 2.2 Chủ sản phẩm (Product Owner)
- Là đại diện duy nhất chịu trách nhiệm tối đa hóa giá trị của sản phẩm phát triển.
- Quản lý hiệu quả Danh mục Sản phẩm (Product Backlog): Xây dựng và truyền đạt rõ ràng Mục tiêu Sản phẩm, tạo lập và giải thích rõ ràng các User Story, sắp xếp thứ tự ưu tiên của các hạng mục công việc.
- Đóng vai trò trọng tài quyết định việc đưa một yêu cầu thay đổi mới vào Product Backlog hay từ chối để bảo vệ phạm vi sản phẩm.

### 2.3 Chuyên gia Scrum (Scrum Master)
- Chịu trách nhiệm thiết lập và duy trì môi trường Scrum theo đúng Scrum Guide 2020.
- Giúp đội ngũ tập trung vào việc tạo ra các Phần tăng trưởng có giá trị cao đáp ứng Definition of Done.
- Chủ động loại bỏ các trở ngại (Impediments) cản trở tiến độ của đội phát triển.
- Đảm bảo tất cả các sự kiện Scrum diễn ra tích cực, đúng thời lượng quy định và đạt được mục tiêu đề ra.

---

## 3. Giám Sát Thực Thi Qua 4 Sự Kiện Scrum Chính

Mọi sự kiện trong Scrum đều là cơ hội chính thức để thanh tra và thích ứng, được giới hạn trong một khung thời gian cố định (time-box).

### 3.1 Họp Kế hoạch Sprint (Sprint Planning)
- Thời lượng: Tối đa 8 giờ cho Sprint 1 tháng (tương đương 4 giờ cho Sprint 2 tuần).
- Nội dung giám sát gồm 3 chủ đề then chốt:
  - Chủ đề 1: Tại sao Sprint này lại có giá trị? (Xác lập Mục tiêu Sprint - Sprint Goal rõ ràng, ngắn gọn).
  - Chủ đề 2: Những gì có thể làm xong trong Sprint này? (Lựa chọn các User Story từ Product Backlog dựa trên năng lực và vận tốc thực tế).
  - Chủ đề 3: Công việc đã chọn sẽ được hoàn thành như thế nào? (Phân rã các User Story thành các nhiệm vụ kỹ thuật cụ thể dưới 1 ngày làm việc).
- Điều kiện tiên quyết: Các User Story đưa vào Sprint bắt buộc phải đạt tiêu chuẩn Định nghĩa Sẵn sàng (Definition of Ready).

### 3.2 Họp Scrum Hằng Ngày (Daily Scrum)
- Thời lượng: Cố định 15 phút vào cùng một khung giờ và địa điểm trong mỗi ngày làm việc.
- Mục đích: Thanh tra tiến độ hướng tới Mục tiêu Sprint và thích ứng Kế hoạch Sprint cho ngày làm việc tiếp theo.
- Trọng tâm giám sát: Đánh giá những việc đã làm được hôm qua, những việc sẽ thực hiện hôm nay để hỗ trợ đạt Mục tiêu Sprint, và nhận diện tức thì mọi trở ngại đang cản trở tiến độ để loại bỏ ngay.

### 3.3 Sơ Kết Sprint (Sprint Review)
- Thời lượng: Tối đa 4 giờ cho Sprint 1 tháng (tương đương 2 giờ cho Sprint 2 tuần).
- Bản chất giám sát: Đây là buổi nghiệm thu thực tế, không chỉ là buổi thuyết trình lý thuyết.
- Quy trình nghiệm thu:
  - Đội phát triển trình diễn trực tiếp Phần tăng trưởng sản phẩm vừa hoàn thành trên môi trường thử nghiệm hoặc vận hành thực tế.
  - Chủ sản phẩm và các bên liên quan trực tiếp thao tác, kiểm tra và xác nhận các tính năng đạt chuẩn nghiệm thu.
  - Đánh giá tiến độ tổng thể hướng tới Mục tiêu Sản phẩm, thảo luận về những thay đổi trên thị trường hoặc phản hồi của người dùng để điều chỉnh Product Backlog cho các Sprint tiếp theo.

### 3.4 Cải Tiến Sprint (Sprint Retrospective)
- Thời lượng: Tối đa 3 giờ cho Sprint 1 tháng (tương đương 1,5 giờ cho Sprint 2 tuần).
- Trọng tâm giám sát: Nhìn nhận lại con người, mối quan hệ, quy trình và công cụ trong Sprint vừa qua.
- Kết quả bắt buộc: Xác định ít nhất một hành động cải tiến cụ thể có mức ưu tiên cao nhất để đưa vào Kế hoạch Sprint tiếp theo nhằm nâng cao chất lượng và hiệu quả làm việc.

---

## 4. Kiểm Soát Chất Lượng Bằng Cam Kết Tạo Tác (Artifact Commitments)

Mỗi tạo tác Scrum đều chứa một cam kết nhằm bảo đảm cung cấp thông tin minh bạch và đo lường chính xác tiến độ:

### 4.1 Danh mục Sản phẩm (Product Backlog) và Mục tiêu Sản phẩm (Product Goal)
- Product Backlog là nguồn công việc duy nhất cho đội Scrum.
- Cam kết: Mục tiêu Sản phẩm mô tả trạng thái tương lai của sản phẩm, đóng vai trò là mục tiêu dài hạn để đội Scrum lập kế hoạch.
- Hoạt động làm mịn (Backlog Refinement): Diễn ra liên tục nhằm phân tích sâu, ước lượng kích thước và làm rõ tiêu chí chấp nhận cho các User Story trước khi đưa vào Sprint Planning.

### 4.2 Danh mục Công việc Sprint (Sprint Backlog) và Mục tiêu Sprint (Sprint Goal)
- Sprint Backlog gồm Mục tiêu Sprint, tập hợp các User Story được chọn và kế hoạch hành động kỹ thuật.
- Cam kết: Mục tiêu Sprint là cam kết duy nhất của Sprint Backlog, tạo ra sự linh hoạt về phạm vi công việc cần thiết để đạt được mục tiêu đó.

### 4.3 Phần Tăng Trưởng (Increment) và Định Nghĩa Hoàn Thành (Definition of Done)
- Phần tăng trưởng là bước đệm cụ thể hướng tới Mục tiêu Sản phẩm. Mỗi Phần tăng trưởng phải có khả năng sử dụng được (usable), bất kể Chủ sản phẩm có quyết định phát hành hay không.
- Cam kết: Định nghĩa Hoàn thành là bản mô tả chính thức về trạng thái của Phần tăng trưởng khi nó đáp ứng đầy đủ các tiêu chuẩn chất lượng theo yêu cầu của sản phẩm.
- Quy tắc giám sát nghiêm ngặt: Một công việc không thể được coi là một phần của Phần tăng trưởng và không được phép trình diễn tại Sprint Review nếu nó chưa đáp ứng 100% Định nghĩa Hoàn thành.

---

## 5. Cơ Chế Quản Lý Thay Đổi Thích Ứng Trong Sprint

Scrum Guide 2020 quy định rất chặt chẽ về việc kiểm soát thay đổi để vừa bảo đảm tính linh hoạt vừa bảo vệ nhịp độ làm việc của đội dự án:

### 5.1 Nguyên tắc bảo vệ Mục tiêu Sprint
- Trong suốt quá trình Sprint đang diễn ra, tuyệt đối không được phép thực hiện bất kỳ thay đổi nào làm nguy hại đến Mục tiêu Sprint đã cam kết.
- Mục tiêu chất lượng không được phép suy giảm dưới bất kỳ hình thức nào.
- Phạm vi công việc có thể được làm rõ và thương lượng lại giữa Chủ sản phẩm và Đội phát triển khi hai bên thu nhận thêm nhiều thông tin chi tiết hơn trong quá trình triển khai.

### 5.2 Xử lý yêu cầu phát sinh mới từ khách hàng
- Khi khách hàng hoặc người dùng đề xuất một tính năng mới hoặc thay đổi đặc tả, yêu cầu này không được chèn ép trực tiếp vào Sprint đang chạy.
- Quy trình xử lý:
  1. Ghi nhận yêu cầu thành một User Story mới trong Product Backlog.
  2. Chủ sản phẩm đánh giá giá trị kinh doanh, sắp xếp thứ tự ưu tiên so với các yêu cầu hiện có.
  3. Đội phát triển tiến hành định cỡ và ước lượng nỗ lực trong các buổi làm mịn Backlog.
  4. Lựa chọn đưa vào kế hoạch của Sprint tiếp theo một cách chủ động và có kiểm soát.

### 5.3 Hủy bỏ Sprint trong trường hợp đặc biệt
- Chỉ có duy nhất Chủ sản phẩm mới có thẩm quyền hủy bỏ một Sprint đang diễn ra.
- Điều kiện hủy bỏ: Mục tiêu Sprint trở nên lỗi thời hoặc không còn giá trị kinh doanh do sự thay đổi đột ngột từ định hướng chiến lược của doanh nghiệp hoặc điều kiện công nghệ.
- Hệ quả: Các hạng mục đã hoàn thành đáp ứng DoD được xem xét nghiệm thu; các hạng mục chưa hoàn thành được ước lượng lại và đưa trở lại Product Backlog.

---

## 6. Bộ Chỉ Số Giám Sát Tiến Độ và Năng Suất Thực Thi

Để giám sát khách quan quá trình thực thi, chuyên gia giám sát sử dụng hệ thống chỉ số định lượng:
1. **Biểu đồ Cháy Hết Sprint (Sprint Burndown Chart)**: Theo dõi khối lượng công việc còn lại hằng ngày so với đường tiến độ lý tưởng, phát hiện sớm nguy cơ trễ hạn trong Sprint.
2. **Vận tốc Đội Dự án (Team Velocity)**: Tổng số điểm câu chuyện hoặc số giờ công hoàn thành thực tế sau mỗi Sprint, dùng làm căn cứ dự báo chính xác năng lực cho các Sprint tiếp theo.
3. **Tỷ lệ Hoàn thành Đúng Hạn (Say/Do Ratio)**: Tỷ lệ giữa khối lượng công việc cam kết tại Sprint Planning so với khối lượng thực tế hoàn thành đạt chuẩn DoD tại Sprint Review (mục tiêu đạt từ 85% đến 100%).
4. **Mật độ và Tốc độ Giải quyết Lỗi (Defect Resolution Rate)**: Số lượng lỗi phát sinh trong Sprint, tỷ lệ lỗi mức độ nghiêm trọng và thời gian trung bình để khắc phục lỗi triệt để.
5. **Thời gian Chu kỳ (Cycle Time)**: Thời gian trung bình từ khi bắt đầu lập trình một tính năng đến khi tính năng đó vượt qua kiểm thử và sẵn sàng triển khai.
