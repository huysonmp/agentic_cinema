# Series Anh Khoai Tây & Chị Đào

## Trạng thái hiện hành — 2026-09-30, P6

Mới nhất: [vòng sửa49](episodes/ep01_pilot/49_p6-targeted-profile-eyeline-grip-rework-v01.md), thêm6output versions đã lưu local/QC. Edit cục bộ sửa eyeline Đào ở mức root provisional; profile Khoai và grip đũa chưa đạt. Primary45 không đổi, P6 chưa complete, chưa video; số dư1.050/observed delta0. Các thông tin46–48 sau đây giữ mốc trước rework.

Ưu tiên bản ghi này hơn các dòng lịch sử bên dưới. [Approval45](episodes/ep01_pilot/45_p6-owner-v03-visual-baseline-approval.md) khóa hướng hình bộ đôi v0.3; không tự duyệt mọi angle/expression. [Vòng46](episodes/ep01_pilot/46_p6-consistency-front-profile-run-v01.md), [47](episodes/ep01_pilot/47_p6-expression-diagnostics-v01.md), [48](episodes/ep01_pilot/48_p6-static-hand-prop-diagnostics-v01.md) đã tạo và lưu local9still mới, root QC. Exact Khoai profile, Đào eyeline và grip đũa chưa đạt brief; geometry phần khuất cần owner review. P6 chưa complete, chưa voice/motion/food visual lock/video. Primary duo giữ nguyên; media gitignored, commit chỉ metadata/docs. Cumulative cap200credit theo41, số dư Flow1.050 sau vòng và observed delta0.

Folder làm việc chính thức của series TikTok AI về món ăn và văn hóa vùng miền.

## Trạng thái

- P0: `APPROVED` (P0-v1, 2026-09-29)
- P1: `APPROVED` (Series Bible v0.9, 2026-09-29; hình/giọng nhân vật còn phải thử ở P6)
- P2 EP01: `APPROVED` — `EP01-P2-v0.2 + E1`, [biên bản duyệt](episodes/ep01_pilot/08_p2-approval-record.md)
- P3 EP01: `APPROVED` — brief v0.1 với D1=A, D2=A, [biên bản duyệt](episodes/ep01_pilot/10_p3-approval-record.md)
- P4 EP01: đã chạy concept/rework; owner chọn hướng C qua hội thoại, ghi ở [approval](episodes/ep01_pilot/33_p5-c-v0.5-owner-content-approval.md); không giả quality panel PASS
- P5 EP01: `C_V0.5_OWNER_CONTENT_APPROVED / FINAL_REVIEW_PENDING / AI_PERFORMANCE_UNTESTED` — [bản đầy đủ](episodes/ep01_pilot/32_p5-script-c-v0.5-approved-content.md) và [biên bản](episodes/ep01_pilot/33_p5-c-v0.5-owner-content-approval.md); kết Khoai gắp cho Đào để chữa cháy. Chưa media/generation hoặc toàn bộ P5 quality pass. Giữ A; D chưa tiếp tục, không tự DROP
- Tier 1: thiết kế Option A `APPROVED`; [runtime v0.1](agents/quality_system/02_runtime-contract-and-stage-map-v0.1.md) có prompt/rubric/fixture, [probe đầu](agents/quality_system/05_tier1-behavior-probe-report-v0.1.md) và [retest/readiness](agents/quality_system/06_flow-fixture-retest-and-runtime-readiness-v0.1.md); chờ review version trước run trên EP01
- Agent production: [bảy vị trí đầu đã được duyệt chuẩn bị](agents/production_team/01_owner-preparation-approval.md); PROD7-v0.1 có [contract](agents/production_team/02_common-runtime-contract-v0.1.md), [7 prompts](agents/production_team/03_role-prompts-v0.1.md), [14 fixtures chưa chạy](agents/production_team/04_behavioral-fixtures-v0.1.md); version review/episode run pending, không generation. Bốn role downstream trong đề xuất 07 vẫn chưa duyệt
- Media automation: [khảo sát official Veo/image API và Flow v0.1](agents/08_google-media-api-feasibility-discovery-v0.1.md); owner muốn auto sau approval/lệnh thử, route/account/budget chưa chốt. Chưa adapter, chưa access tài khoản, chưa paid run; Flow manual baseline chưa bị thay ngầm
- Route hiện hành: owner chọn C; [Flow UI read probe và kế hoạch ghép](agents/09_flow-ui-route-c-probe-and-assembly-plan.md) đã đọc/click được project/settings/menu trên flow.google.com, giữ “Luôn luôn xác nhận”; chưa generation/editing/download test, chưa cap/request approved. Tài liệu 08 giữ lịch sử trước chọn route
- P6–P14: chưa mở sản xuất; chưa gọi Veo hoặc release
- Phạm vi bàn giao EP01: [owner tự dựng Canva, hỗ trợ bàn giao clip cảnh/đoạn có QC và chỉ dẫn nối](episodes/ep01_pilot/35_owner-canva-assembly-and-shot-delivery-decision.md); chưa có media, chưa miễn QC master hoặc duyệt request tạo.
- Script Lab EP01: đã chạy thử `NON-FINAL`; [kết quả vòng 1](episodes/ep01_pilot/script_lab/08_script-lab-pilot-evaluation-v0.1.md) — chưa có kịch bản sẵn sàng sản xuất
- Episode đang mở: `EP01_PILOT`
- Cập nhật review cuối P5: [hai paper reviews độc lập đã hoàn tất](episodes/ep01_pilot/36_p5-v0.5-final-paper-reviews-and-cue-decision.md), không yêu cầu đổi thoại; cue thính/món/nơi chờ xác nhận. Có [đề xuất hướng hình/giọng P6](episodes/ep01_pilot/37_p6-visual-voice-direction-proposal-v0.1.md), chưa tạo asset hoặc mở production.

## Cấu trúc

**Quyết định mới nhất:** [approval38](episodes/ep01_pilot/38_p5-content-handoff-and-p6-direction-approval.md) xác nhận Q0 + V1A/V2A/V3A. P5 nội dung được chuyển giao có dependency media; P6 mở chuẩn bị thiết kế, chưa asset/generation approval. [Design/sample plan39](episodes/ep01_pilot/39_p6-character-voice-design-and-sample-plan-v0.1.md) là draft. Các dòng pending cue/direction ở trên là lịch sử trước approval38.

| Folder | Chức năng |
|---|---|
| `00_governance/` | Project Foundation Pack và phê duyệt P0 |
| `01_series_foundation/` | Series bible, định vị, format và character canon tại P1 |
| `02_shared/` | Register và asset dùng chung |
| `episodes/` | Hồ sơ tuần tự của từng episode |
| `agents/` | Contract, thử nghiệm và báo cáo của agent theo stage; gồm [P2 Auditor](agents/p2_fact_source_auditor/design-v1.md) và [vòng kịch bản P3–P5](agents/script_workroom/02_pilot-workflow-contract-v0.1.md) |
| `media/` | Nơi owner lưu media thật; file media không commit Git |

## Nguyên tắc

P6 mới: [reference intake và request thử base40](episodes/ep01_pilot/40_p6-reference-intake-and-character-trial-request-v0.1.md) đã kiểm text nguồn/Flow UI read-only, chưa visual food verification. Hai prompt nhân vật text-only chờ duyệt chạy, chưa media/credit spent.

- `Markdown/JSON/CSV` là source of truth cho quyết định và metadata.
- Bản đã duyệt không ghi đè; tạo revision mới.
- Agent tạo proposal; owner quyết định.
- Flow chỉ nhận generation package đã duyệt.
- `DONE`, `DELIVERED`, `ACCEPTED` và `PUBLISHED` là trạng thái khác nhau.

P0 đã được owner duyệt tại [07_p0-review-and-approval.md](00_governance/07_p0-review-and-approval.md). P1 được owner duyệt ở [Series Bible v0.9](01_series_foundation/02_series-bible-proposal.md). EP01 đã duyệt P2 và P3, đang thử kịch bản P5 theo ngoại lệ có ghi nhận; không approval nào ở trên tự duyệt script, prompt hoặc đầu ra video.

**Quy tắc đọc trạng thái:** một số tài liệu thành phần P0 giữ dòng `Status: proposed` như bản tại thời điểm soạn; [biên bản duyệt P0](00_governance/07_p0-review-and-approval.md) là nguồn quyết định hiện hành cho pack P0-v1. Tương tự, các câu hỏi trước duyệt trong Bible P1-v0.9 là lịch sử soạn thảo; [biên bản duyệt P1](01_series_foundation/19_p1-approval-record.md) xác định phạm vi đã duyệt. Không sửa nội dung bản đã duyệt chỉ để xóa dấu vết này.
