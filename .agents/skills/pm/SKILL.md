---
name: pm
description: >-
  Lập một tài liệu ICTPM bằng tiếng Việt theo lệnh pm:hsmt, pm:hsdt, pm:wbs,
  pm:master-schedule, pm:master-plan, pm:cost-estimate, pm:stakeholder,
  pm:risk-management-plan, pm:change-management-plan, pm:progress-report,
  pm:responsibilities, pm:issues, pm:phase-exit, pm:closure-summary,
  pm:evaluation, pm:lessons, pm:payroll, pm:version-control, pm:peer-eval,
  pm:stakeholder-post, pm:post-survey, pm:closure-report, pm:selection-matrix,
  pm:portfolio. Dùng khi câu chat có @pm:, /pm: hoặc pm:.
---

# PM

Một skill, nhiều lệnh. Cách gọi cùng nghĩa: `@pm:hsmt`, `/pm:hsmt`, `pm:hsmt`.

Chỉ làm một lệnh trong câu. Lấy phần sau dấu `:`. Không có lệnh thì hỏi lại, không làm hết danh sách.

Mọi câu trả lời cho người dùng, mọi checklist và mọi chuỗi trong `body` viết bằng tiếng Việt ngay từ bản đầu. Không viết tiếng Anh rồi dịch. Giữ nguyên tên riêng, email và mã định danh đúng như brief.

## Quy trình

Khi cần tra cứu chuẩn mực chuyên môn, công thức (EVM, CPM, PERT, PxI, EMV), quy trình (CCB, SCM, Tuckman, Phase Exit) hoặc nguyên tắc quản trị của một PM thực thụ từ 7 bài giảng ICTPM, đọc [references/ictpm_body_of_knowledge.md](references/ictpm_body_of_knowledge.md).

1. Nếu có `references/<lệnh>.md` thì chỉ đọc file đó. Chưa có thì đọc đúng mục trong bảng, tại `Smart PMP/ictpm-flow/thiet-ke-tong-quan.md` (hoặc `ictpm-flow/thiet-ke-tong-quan.md`).
2. Đọc `Smart PMP/ictpm-flow/artifacts/00_project_brief.json` và các file bắt buộc đã `approved`. File optional chưa `approved` thì ghi vào `inputs_missing_optional`, không bịa nội dung.
3. Viết `body`.
4. Chấm bằng checklist của lệnh đó. Không sửa bài trong lúc chấm. Ghi issue: trường, bằng chứng, cách sửa.
5. Còn issue thì sửa và chấm lại, tối đa 2 vòng.
6. Ghi `Smart PMP/ictpm-flow/artifacts/<file>`. Hết lỗi, vai PM → `ready_for_review`. Hết lỗi, vai SP → `waiting_sponsor`. Còn lỗi → `blocked`.
7. Dừng. Không tự ghi `approved`.

```json
{
  "artifact_id": "01_hsmt",
  "command": "pm:hsmt",
  "status": "ready_for_review",
  "inputs_used": ["00_project_brief.json"],
  "inputs_missing_optional": [],
  "validation": { "attempts": 1, "issues": [] },
  "body": {}
}
```

## Lệnh

| Lệnh | File artifact | Khi chưa có reference, đọc mục |
|---|---|---|
| pm:stakeholder | c6_stakeholder.json | C6. Stakeholder analysis |
| pm:selection-matrix | c6_selection_matrix.json | C6. Project Selection Decision Matrix |
| pm:portfolio | c6_portfolio.json | C6. Project Portfolio Management Template |
| pm:hsmt | 01_hsmt.json | 1. Hồ sơ mời thầu |
| pm:hsdt | 02_hsdt.json | 2. Hồ sơ dự thầu |
| pm:wbs | 03_wbs.json | 3. WBS |
| pm:master-schedule | 04_master_schedule.json | 4. Master schedule |
| pm:cost-estimate | 06_cost_estimate.json | 6. Cost estimate |
| pm:master-plan | 05_master_plan.json | 5. Master plan |
| pm:risk-management-plan | 07_risk_plan.json | 1. Risk management plan |
| pm:change-management-plan | 08_change_plan.json | 2. Change management plan |
| pm:responsibilities | 10_responsibilities.json | 4. Danh sách phân chia công việc |
| pm:progress-report | 09_progress.json | 3. Báo cáo tiến độ |
| pm:issues | c6_issues.json | C6. Issues and Action Items Management Database |
| pm:phase-exit | c6_phase_exit.json | C6. Project Control Phase Exit Review Checklist |
| pm:closure-summary | 11_closure_summary.json | 1. Báo cáo tổng kết dự án |
| pm:evaluation | 12_evaluation.json | 2. Báo cáo đánh giá dự án |
| pm:lessons | 13_lessons.json | 3. Báo cáo bài học kinh nghiệm |
| pm:payroll | 14_payroll.json | 4. Bảng phân chia lương |
| pm:version-control | 15_version_control.json | 5. Tài liệu quản lý phiên bản |
| pm:peer-eval | c6_peer_eval.json | C6. Project Team Member Peer Evaluation Form |
| pm:stakeholder-post | c6_stakeholder_post.json | C6. Stakeholder Post Project Evaluation Form |
| pm:post-survey | c6_post_survey.json | C6. Post Implementation Survey |
| pm:closure-report | c6_closure_report.json | C6. Project Review and Closure Report |

`pm:phase-exit` và `pm:closure-report` là cổng, vai SP. `pm:lessons` cũng vai SP. Các lệnh còn lại vai PM.

`pm:hsdt` và `pm:wbs` cần `01_hsmt.json` đã approved. `pm:master-schedule` và `pm:cost-estimate` cần `03_wbs.json` đã approved.

## Thêm lệnh

Người nhận ô thêm `references/<lệnh>.md`, theo mẫu [references/hsmt.md](references/hsmt.md). Không sửa reference của lệnh khác. `<lệnh>` là phần sau dấu `:`, ví dụ `risk-management-plan`.
