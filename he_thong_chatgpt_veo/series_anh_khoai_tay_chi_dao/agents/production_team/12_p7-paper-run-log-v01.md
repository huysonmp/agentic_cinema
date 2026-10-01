# EP01 — Nhật ký P7 thiết kế và phản biện

2026-10-01. `P7_PAPER_PLANNING_OPEN / NO_GENERATION_AUTHORITY_ADDED`.

Căn cứ: common PROD7-v0.1, role prompts03, stage map Tier1-02 và owner approval78. Bảy vị trí được chuẩn bị theo01; những lần chạy paper này không xác nhận mọi fixture đã qualified hoặc production runtime tự động đã tồn tại.

## Đăng ký trước dispatch

### EP01-P7-SHOT-01

- Role/stage/mode: `AG-SHOT-01 / P7 / PAPER_PROPOSAL`.
- Task: lập coverage toàn bộ script C-v0.5, bảo toàn nguyên nhân–chữa cháy–Đào hiểu, đề xuất hai phương án quay phần rủi ro và shot table cho phương án khuyến nghị.
- Target/output: `episodes/ep01_pilot/79_p7-shot-design-draft-v01.md`, v0.1; maker được tạo đúng file này, không sửa upstream.
- Authority: approval33/38 nội dung/Q0; approval45 primary; approval62 grip; approval71–72 bộ phục vụ; approval78 khung v0.8 và tiếp tục P7 paper. Không dùng approval78 làm quyền chạy video.
- AVAILABLE: script32, approvals38/45/62/78, ledger75, CTD11, serving71 và ba ảnh v0.8/primary/F05 cùng I03/I05 trong project.
- MISSING/NOT_TESTED: actual voice/audio duration, action/keyframe media theo shot, actual model/feature/cost account evidence hiện hành cho video, approved generation request.
- Allowlist: toàn common02, section AG-SHOT-01 role03, stage map Tier1-02; chỉ các episode sources32/35/38/45/62/71/75/78, CTD11 và exact refs trên.35 là quyết định owner tự dựng Canva, giao clip pack và chỉ dẫn nối. Có thể đọc approval33 khi cần scope; không đọc maker76/74 hoặc reviewer18/19.
- Output spec: tiếng Việt dễ đọc; beat→shot coverage, exact lời thoại, duration TARGET không MEASURED, camera/axis, tay/đũa/bát/cốc và portion states, start/end, joins/audio, F01/F02/AI, refs/status; alternatives/trade-offs; gaps tối thiểu theo shot; findings/closure và 5-part handoff. Không giả thời lượng native hoặc capability Veo.
- Open findings: giọng và motion NOT_TESTED; native v0.8 chưa exact9:16; reference cho động tác/biểu cảm chưa đối soát. Không tự dựng 360° hoặc bắt ngón khuất phải lộ.
- Tool quyền: local read/view và apply_patch output; không Flow/browser/network/upload/generation/credit/voice/Git/release; không tạo agent con.
- Reviewer kế tiếp: independent paper coverage/action/join review sau khi file79 tồn tại. Maker không tự duyệt.

| Run | Role/stage/mode | Output | Actual access / status | Owner decision / next |
|---|---|---|---|---|
| EP01-P7-SHOT-01 | AG-SHOT-01 / P7 / PAPER_PROPOSAL | episode79 v0.1 | DISPATCHED / OUTPUT_PENDING | Frame78 approved; shot design not approved; independent review after maker |

Không ghi COMPLETED khi chưa có artifact và read-back. Nếu runtime bị ngắt, giữ lỗi thực và phân biệt nội dung đã lưu với lượt chạy thành công.

### EP01-P7-FLOW-01 — đăng ký reviewer trước dispatch

- Role/stage/mode: `AG-FLOW-01 / P7 / PAPER_REVIEW`; target episode79 v0.1, chỉ dispatch sau khi maker lưu đủ bản.
- Task: phản biện coverage, tải hành động, địa lý tay/đũa/bát/cốc và joins; phân biệt logical shot, thời lượng mục tiêu và native generation request. Không chứng nhận clip hoặc capability chưa kiểm.
- Authority: chỉ local paper review theo scope78 và Tier1 thiết kế đã duyệt; không chạy production hoặc cấp quyền media.
- AVAILABLE lúc dispatch: exact79, script32, decisions35/38/45/62/71/78, source ledger75, approved refs v0.8/primary/F05/I03/I05. MISSING: actual voice/motion, video model/feature/cost/account evidence, approved request. Không gán UNKNOWN thành MET.
- Allowlist: toàn Tier1 runtime02 + chỉ section AG-FLOW-01 prompts03, envelope này; target79 đọc trước rồi sources/refs trên. Forbidden: maker chat/rationale ngoài79, report CTD11, maker74/76, reviews18/19, root recommendation chưa nằm trong target, báo cáo reviewer khác.
- Output: episode80 `80_p7-shot-feasibility-paper-review-v01.md`, v0.1, tối đa khoảng120lines; actual access, scoped coverage FLOW1–5, findings severity/evidence/route/closure, alternatives critique và tối đa ba quyết định owner có bằng chứng. `P7 paper` và `generation readiness` phải có status riêng; chưa feature/cost/request thì không generation-ready.
- Tools: local read/view + apply_patch đúng output80; không browser/network/upload/generation/credit/Git/voice hoặc agent con. Không sửa79/upstream.
- Independence: context riêng, không maker chat; target là tài liệu thiết kế nên phải đọc ý định và phương án trong79, không gọi fresh-blind audience test.
- Status preregistration: `REGISTERED_NOT_DISPATCHED / TARGET79_PENDING`.
