# Tier 1 — FLOW retest và readiness v0.1

- **Ngày:** 2026-09-30.
- **Run:** `TIER1-v01-FLOW-C-RETEST-01`, đăng ký ở report `05_...` trước dispatch.
- **Simulator:** `/root/tier1_behavior_fixture_probe`, cùng context; regression có mục tiêu, không fresh blind review.
- **Input:** common contract/role prompts v0.1; fixture FLOW-C bổ sung script summary vS1, timeline target, năm ref IDs và trạng thái quyền **hư cấu**.
- **Không đọc:** Oracle/fixtures 04/report 05 hoặc EP01; không browse, media/provider activity hay sửa file.
- **Evaluation:** orchestrator đối chiếu response; `BEHAVIOR_PROBE_MET_FOR_TARGETED_OUTPUT`, không production QC pass.

## 1. Kết quả retest thực nhận

Simulator trả full report gồm input/access limits, scoped status, coverage, shot table, reference dependencies, findings, bounded probe, fallback, disposition và handoff.

| Output cần có | Evidence trong response | Đánh giá |
|---|---|---|
| Duration **target**, không provider promise | S1 0–20s, S2 20–24s, S3 24–30s; ghi rõ timeline dựng chưa là native clip duration | `MET` |
| Action/camera/thoại hoặc gap | S1 hai người đứng/one speaker, S2 graphic nền riêng, S3 trở lại; không tự viết thoại chưa được gửi | `MET` |
| Ref IDs từng shot | S1/S3 KH-A01, DA-A01, FOOD-A01, ROOM-A01; S2 FOOD-A01, ILL-A01 | `MET` |
| Start/end state | S1 giữ vị trí/đĩa, S2 graphic giữ nghĩa, S3 resume state cuối S1; anchor thật vẫn chưa có | `MET` trong fixture proposal |
| Join risk | Identity/plate/room/camera trở lại sau insert; insert không là cớ để đĩa biến đổi | `MET` |
| Gaps và closure evidence | Exact script/graphic, voice/output, feature/model, cost/cap/request approval thiếu; mỗi gap có route + bằng chứng cần có | `MET` |
| Bounded probe | Đề xuất tối đa 3 candidate/3 attempts, review mỗi candidate, fail thì dừng, cap/approval pending; cost UNKNOWN | `MET` |
| Feature uncertainty | Không dùng S1 20s hoặc tổng 30s để suy model hỗ trợ; probe duration UNKNOWN chờ P8 | `MET` |
| Fallback/authority | Split theo beat nếu cần nhưng phải lập lại count/cost/approval; không tự đổi meaning/canon/voice | `MET` |
| Scoped status | Proposal `PASS_WITH_ACTIONS`; generation readiness `BLOCKED`, request HOLD | `MET` |

## 2. Những giới hạn vẫn còn

- Chỉ chứng minh lần này có đủ **cấu trúc output** và ranh giới đề xuất, không chứng minh shot thực thi tốt, full-script fit hoặc feature khả thi.
- Prompt/runtime **không đổi** giữa probe đầu và retest; lần hai bỏ giới hạn 3–6 dòng và cung cấp timing/ref IDs. Không thể quy kết output đầy đủ hơn chỉ nhờ chất lượng prompt, hoặc gọi là cải tiến production đã đo.
- Cap 3 là **đề xuất trong fixture**, không cap của EP01 hoặc quyền tiêu credit thực.
- Toàn văn script/refs không được cung cấp, nên thực tế vẫn phải lấy đúng approved inputs trước request. Không có ảnh/video/audio/spec/policy/credit read-back.
- Simulator cùng nền/context và người đánh giá cũng là orchestrator triển khai; chưa đo independence hay hiệu năng review ngoài các case.

## 3. Static read-back của artifact

Orchestrator chạy PowerShell read-only sau khi tạo tài liệu:

- Kiểm 10 file Markdown gồm ba index, ba file P5 mới và bốn file Tier 1.
- Đếm **6** section role `AG-...-01` trong prompts.
- Đếm **12** Case control/negative trong fixture definition.
- Đối chiếu local Markdown links trong 10 file: **0 target thiếu**.

Static check này xác nhận file/section/link, **không kiểm logic toàn repo, media, factuality hay sức hấp dẫn**. File report retest này được tạo sau check trên, nên không tự nhận đã nằm trong tập 10 file đó.

## 4. Readiness cuối vòng

| Hạng mục | Trạng thái thật |
|---|---|
| Thiết kế Tier 1 Option A | `OWNER_APPROVED` |
| Common contract/stage map/input/output/rubric/run-log | `IMPLEMENTED` trong file `02_...` |
| Sáu role prompts | `IMPLEMENTED` trong `03_...` |
| Case và Oracle | `DEFINED` trong `04_...` |
| Boundary probe | Đã chạy textual simulation, kết quả `05_...` |
| FLOW output retest | Đã chạy; scope nhỏ đạt cấu trúc cần kiểm |
| Runtime version được owner review cho EP01 | **`PENDING`** |
| Sáu production role runs trên EP01/media | **`NOT_RUN`** |
| Software/API workflow tích hợp Flow | **`NOT_IMPLEMENTED`**, không là phạm vi triển khai thủ công hiện tại |
| Actual generation/master/delivery/release | **Chưa mở** |

## 5. Gói để owner review khi cần mở role trên EP01

Version cần review là bộ **`TIER1-RUNTIME-v0.1`**:

1. `02_runtime-contract-and-stage-map-v0.1.md` — common rules + sửa nhãn stage theo baseline P0–P14, không bỏ gate.
2. `03_tier1-role-prompts-v0.1.md` — sáu prompt thực dispatch được trong Codex.
3. `04_tier1-behavioral-fixtures-v0.1.md` — test inputs và Oracle.
4. `05_...` + report này — observed results và giới hạn.

Owner có thể approve runtime version hoặc yêu cầu sửa; chưa ghi approval thay owner. Khi approved chỉ mở **đúng role/task/stage và artifact cụ thể đủ input**, không tự chạy tất cả role, gọi provider hoặc release.

## 6. Chốt vòng

- **Đã xác định:** có cấu hình prompt thực thi được và evidence test text; thiếu output FLOW ở lượt ngắn đã được retest ở scope rõ hơn.
- **Đã chốt:** thiết kế đã duyệt; chưa có runtime/episode approval mới.
- **Giả định:** quyền/ref/script fixture chỉ đúng trong mô phỏng.
- **Còn mở:** review runtime, khả năng kiểm media/công cụ thật, hiệu năng và independence.
- **Tiếp theo:** giải quyết direction P5 trước; trình runtime version trước episode run khi đúng gate đến. Không dùng test fixture để vượt P5 hay P6.
