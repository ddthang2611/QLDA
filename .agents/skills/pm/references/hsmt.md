# pm:hsmt — Hồ sơ mời thầu

Đây là hướng dẫn của lệnh `pm:hsmt` trong skill `pm`, không phải một skill riêng. File này không chứa tên dự án, ngày, tiền hay phạm vi. Những thứ đó chỉ nằm trong `ictpm-flow/artifacts/00_project_brief.json`.

Ghi `ictpm-flow/artifacts/01_hsmt.json`. Vai PM.

Input bắt buộc: brief. Optional, chỉ khi `approved`: `c6_stakeholder.json`, `c6_selection_matrix.json`, `c6_portfolio.json`.

Được gắn mã `OP-`, `ACT-`, `MS-` và `input_ref`. Không thêm trường sự thật mà brief không có.

`hsmt-example.json` là một bản đã viết cho brief hiện tại. Đổi brief thì không sao chép tên hay số từ file ví dụ đó.

## Trường body

Lấy đúng giá trị trong brief, theo tên trường dưới đây. Brief không có trường nào thì để null, không tự điền.

- `package_name` = `project_name`
- `bidding_entity` = `bidding_entity`
- `procurement_form` = `procurement_form`
- `party_a`, `party_b` nếu brief có
- `issue_date` = `rfp_issue_date`
- `submission_deadline` = `proposal_submission.deadline`
- `submission` lấy các trường có trong `proposal_submission`
- `question_window` lấy nguyên khối trong brief
- `cut_over_date`, `warranty_period`, `budget_ceiling` lấy đúng brief, kể cả khi giá trị là null
- `objectives` đủ impacts, outcome, outputs. Tên output đúng brief
- `development_policy`, `system_parts`, `scope_in`, `scope_out`, `deliverables`, `proposal_required_sections`, `contract_terms` đúng danh sách trong brief
- `activities[].verb_noun` đúng `activity_hints`. Mỗi activity có `output_id` tồn tại. Mỗi output có ít nhất một activity
- `milestones` đúng `milestone_hints`: tên, ngày, `kind` thuộc `end_of_task`, `decision`, `end_of_phase`
- `stakeholders_cited` rỗng nếu chưa có file stakeholder approved. Có file thì mỗi tên phải nằm trong `body.stakeholders`
- `assumptions` chỉ được nhắc điều brief đã ghi trong `date_convention` hoặc một trường ghi chú tương đương. Không dùng assumptions để thêm phạm vi hay số tiền
- `input_refs_used` gồm `00_project_brief.json`

## Checklist sau khi viết

Chấm như người kiểm tra. Không sửa bài trong lúc chấm. Ghi issue nếu:

- Một chuỗi hoặc một số khác brief
- `budget_ceiling` khác giá trị trong brief
- Có tiền, trọng số hoặc đơn giá mà brief không có
- Activity không phải cụm động từ-danh từ, hoặc trỏ tới output không tồn tại
- Một output không có activity
- Milestone thiếu ngày, hoặc `kind` không thuộc ba loại trên
- `scope_in` chứa một mục đang nằm trong `scope_out`
- `proposal_required_sections` thiếu hoặc thừa so với brief
- `stakeholders_cited` có tên khi chưa có file stakeholder approved
- `assumptions` đưa ra sự thật không có trong brief
