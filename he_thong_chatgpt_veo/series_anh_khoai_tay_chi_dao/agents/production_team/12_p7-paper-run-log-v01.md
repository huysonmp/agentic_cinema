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
| EP01-P7-SHOT-01 | AG-SHOT-01 / P7 / PAPER_PROPOSAL | episode79 v0.1 | COMPLETED / ROOT_READBACK_COMPLETE; đọc sources35/13 bổ sung và xem actual5refs;99lines | Frame78 approved; shot design not approved; independent review next |

Không ghi COMPLETED khi chưa có artifact và read-back. Nếu runtime bị ngắt, giữ lỗi thực và phân biệt nội dung đã lưu với lượt chạy thành công.

Addendum trước khi maker chốt và trước reviewer dispatch: cho cả hai run đọc `13_flow-official-planning-evidence-2026-10-01.md`. Root kiểm ba nguồn Google chính thức, có dates/URLs/sections; model/mode tài liệu AVAILABLE, account UI/cost/audio vẫn MISSING. Không mở browser/network cho subagents. Maker nhận bổ sung này bằng message; không giả đã có trong input ban đầu.

### EP01-P7-FLOW-01 — đăng ký reviewer trước dispatch

- Role/stage/mode: `AG-FLOW-01 / P7 / PAPER_REVIEW`; target episode79 v0.1, chỉ dispatch sau khi maker lưu đủ bản.
- Task: phản biện coverage, tải hành động, địa lý tay/đũa/bát/cốc và joins; phân biệt logical shot, thời lượng mục tiêu và native generation request. Không chứng nhận clip hoặc capability chưa kiểm.
- Authority: chỉ local paper review theo scope78 và Tier1 thiết kế đã duyệt; không chạy production hoặc cấp quyền media.
- AVAILABLE lúc dispatch: exact79, script32, decisions35/38/45/62/71/78, source ledger75, approved refs v0.8/primary/F05/I03/I05. MISSING: actual voice/motion, video model/feature/cost/account evidence, approved request. Không gán UNKNOWN thành MET.
- Allowlist: toàn Tier1 runtime02 + chỉ section AG-FLOW-01 prompts03, envelope này; target79 đọc trước rồi sources/refs trên. Forbidden: maker chat/rationale ngoài79, report CTD11, maker74/76, reviews18/19, root recommendation chưa nằm trong target, báo cáo reviewer khác.
- Output: episode80 `80_p7-shot-feasibility-paper-review-v01.md`, v0.1, tối đa khoảng120lines; actual access, scoped coverage FLOW1–5, findings severity/evidence/route/closure, alternatives critique và tối đa ba quyết định owner có bằng chứng. `P7 paper` và `generation readiness` phải có status riêng; chưa feature/cost/request thì không generation-ready.
- Tools: local read/view + apply_patch đúng output80; không browser/network/upload/generation/credit/Git/voice hoặc agent con. Không sửa79/upstream.
- Independence: context riêng, không maker chat; target là tài liệu thiết kế nên phải đọc ý định và phương án trong79, không gọi fresh-blind audience test.
- Status preregistration: `REGISTERED_NOT_DISPATCHED / TARGET79_PENDING`; cập nhật trước dispatch bên dưới sau maker read-back.

Root read-back79: toàn file đã đọc, SHA256 `77876F589D0F2090DCEFC6B75941167752C9809E12E6E6AA8635C7975945C0D7`; chín câu và các beat hiện diện. Đây completeness check, không reviewer verdict. Maker disclosure regex lộ sections khác trong role03 được giữ ở79; chưa input maker/reviewer cấm, không gọi clean access tuyệt đối.

| Run | Role/stage/mode | Exact target / output | Status tại dispatch | Limits |
|---|---|---|---|---|
| EP01-P7-FLOW-01 | AG-FLOW-01 / P7 / PAPER_REVIEW | 79 v0.1 / hash77876F…45C0D7; output80 v0.1 | COMPLETED / ROOT_READBACK_COMPLETE | Paper PASS_WITH_ACTIONS; generation BLOCKED; B boundary còn cần specification |

## Vòng đóng thiếu specification phương án B — đăng ký trước dispatch

Root đọc toàn79/80; kiểm cơ học trên nội dung32 và79:9/9 câu, speaker và thứ tự trùng nguyên văn. Parser đầu chỉ nhận nhãn speaker đơn giản nên không bao phủ nhãn có stage direction; đã sửa parser và chạy lại đạt, không coi lần đầu là lỗi thoại.79 không đổi hash.80 SHA256 `C6CCBCE80A2AC239BD6B4297B54EFFB50D5F9756D59D8052D29E0FF681CF261C`.

### EP01-P7-SHOT-02

- Existing maker AG-SHOT-01 / P7 PAPER_PROPOSAL; targeted addendum, không viết lại79.
- Task: đóng specification còn thiếu tại FLOW-F04 bằng bảng B1/B2 có start/end/join cốc/tay/bát/A/đũa/eye-line và đúng ba câu cuối. Chỉ làm proposal để owner so sánh đầy đủ, không owner chọn B, không nâng motion/timing thành PASS.
- Inputs: common02 + role SHOT đã đọc;79/80 + sources/refs allowlist SHOT01,13,78. Báo cáo reviewer80 được maker đọc ở vòng sửa sau độc lập, không hồi tố làm mất independence FLOW01.
- Output: episode81 `81_p7-b-coverage-boundary-addendum-v01.md`, tối đa60lines. Chỉ ghi file81, không sửa79/80/upstream.
- Authority/tools/limits: cùng scope78, local read/view/apply_patch; không browser/network/generate/credit/Git/agent con. Durations TARGET; câu7 kết B1, câu8/9 tại B2; không thêm uống/nhai/đút/romance. Tay/cốc staging là proposal.
- Status: `COMPLETED / ROOT_READBACK_COMPLETE`;45lines, chỉ output81;79/80 giữ nguyên. FLOW-F04 specification supplied, closure chờ reviewer02.

### EP01-P7-FLOW-02

- Existing reviewer AG-FLOW-01 / P7 PAPER_REVIEW, retained context; không fresh-blind claim.
- Chỉ dispatch sau81 read-back. Target composed paper proposal79+81; closure check FLOW-F04 và regression lời/cause/states, không review runtime/model mới.
- Allowlist: Tier1 runtime02 + đúng section FLOW;79/80/81 và sources/refs FLOW01,13,78. Không maker chat/rationale ngoài artifact, không CTD11/74/76/18/19.
- Output episode82 `82_p7-b-boundary-paper-review-v01.md`, tối đa60lines. Closure phải ghi paper-spec-only, motion/timing/request vẫn UNKNOWN/BLOCKED. Không sửa maker docs/approve/generate/Git.
- Status: `COMPLETED / ROOT_READBACK_COMPLETE`; root đọc toàn82, composed target79+81. FLOW-F04 `VERIFIED_CLOSED_PAPER_SPEC`, không defect giấy mới trong scope; generation vẫn BLOCKED. Không gửi root verdict hoặc maker chat cho reviewer.

## Closeout paper — trình quyết định, không thực thi

Root đọc toàn79/80/81/82, checksums đối soát:79 `77876F589D0F2090DCEFC6B75941167752C9809E12E6E6AA8635C7975945C0D7`;80 `C6CCBCE80A2AC239BD6B4297B54EFFB50D5F9756D59D8052D29E0FF681CF261C`;81 `0CA2C8FC6AEC57C3124AA0DE2C60C3DAA70099D6C6A216FA76915F403A06366A`;82 `14184CB06992BFD684105554CBD57623F7702616B636D2B0AD31A836848A7428`.79/80 không bị sửa trong vòng bổ sung.

| Run | Actual result | Stage/readiness | Handoff |
|---|---|---|---|
| SHOT-01 | Success final + artifact79/read-back | PROPOSAL_COMPLETE; không self-pass | FLOW01 |
| FLOW-01 | Success final + artifact80/read-back | P7 paper PASS_WITH_ACTIONS / generation BLOCKED | Boundary thiếu FLOW-F04 + owner choices |
| SHOT-02 | Success final + artifact81/read-back | Specification supplied, không verified-close | FLOW02 |
| FLOW-02 | Success final + artifact82/read-back | FLOW-F04 closed paper-spec-only; tổng thể giữ actions/blockers | Owner packet83 |

Gói83 tổng hợp hai quyết định coverage/choreography, trạng thái `OWNER_DECISION_PENDING`; không quay lại hỏi approvals đã khóa. Không audio/video/image mới, không clip pack hoặc master đã bàn giao; source13 là official docs, không account UI. Role runtime fixture/production qualification chưa được tự nâng từ các paper runs này.
