# EP01 — P6 next-gate readiness v0.1

2026-10-01. Run `EP01-P6-CONTEXT-CTD-02`; existing `AG-CTD-01`; P6 / `PAPER_REVIEW`.
Status: `PASS_FOR_OWNER_REVIEW / PAPER_DEPENDENCY_MAP_ONLY`; không P6 PASS, media/voice/motion PASS hoặc generation-ready.

## Scope, access và authority

Root dispatch ghi registered04 trước run; adviser không đọc log04. Đọc full common02 + section AG-CTD-01 role03, full stage-map02 và documents dưới; chỉ đọc approval72:1–5 để không đưa lịch sử prompt/root QC vào input. Không truy cập/dùng maker10/76, root QC, reviewer18/19 hoặc media v0.7/v0.8 trong run này. Không cold/media audit; chỉ local document read và report11. Voice chưa generated; motion `NOT_TESTED` theo dispatch; actual frame/reviews/owner selection pending. Không Flow, upload, generation, media edit, Git, video/voice/release hoặc authority mới.

## Sources thực đọc / status reconciliation

Paths tài liệu EP01 dưới là `episodes/ep01_pilot/`; số là prefix filename, source spans để tái kiểm.

| Exact source | Trạng thái dùng trong map |
|---|---|
| `32_p5-script-c-v0.5-approved-content.md`; `33_p5-c-v0.5-owner-content-approval.md` | Exact content C-v0.5 đã duyệt; pending paper review cũ không thắng36/38 |
| `36_p5-v0.5-final-paper-reviews-and-cue-decision.md`; `38_p5-content-handoff-and-p6-direction-approval.md` | Hai paper reviews complete; Q0 approved và P5 content handoff hợp lệ38:7,16–18; media performance chưa kiểm |
| `39_p6-character-voice-design-and-sample-plan-v0.1.md` | Design/sample plan draft; list sheets không evidence đã tạo và outfit draft không override45 |
| `45_p6-owner-v03-visual-baseline-approval.md` | Primary pair v0.3 approved; consistency/performance pending, không mọi variant |
| `62_p6-owner-existing-grip-reference-selection-2026-10-01.md` | I03/I05 owner-selected direction refs; motion/contact chưa chứng minh |
| `64_p6-input-decisions-approved-2026-10-01.md` | Quán ven phố chiều tối; ưu tiên Flow/Veo voice probe khi readiness/request approved; chưa mở voice/video |
| `71_p6-food-texture-approval-and-street-table-brief-2026-10-01.md`; approval extract72:1–5 | F05 texture + serving set approved; không integrated output/P6 approval |
| `75_p6-episode-context-ledger-v01.md` | Source context, không asset approval; reference use authorization khác independent commercial-rights clearance |
| `agents/quality_system/02_runtime-contract-and-stage-map-v0.1.md` | P6 visual/voice refs → P7 shot → P8 request approval → P9 actual generation/review; không gộp gate |

## Đã khóa — không hỏi lại

| Decision | Evidence / scope |
|---|---|
| C-v0.5, bạn trưởng thành, Khoai khựng/chữa cháy tỉnh, Đào hiểu và chủ động nhận bát | 32:25–46 +33; không đút, không nem đã chạm miệng, không romance/thoại nhai |
| F01 cùng nhận diện món; F02 cùng mạch mùi/rang gạo; nhãn AI bắt buộc | 38:7,16 ưu tiên pending cue36:49; layout/timing/readability vẫn cần media |
| Primary identity/outfit pair v0.3; 3D mềm, food/set gần thật | 45:11–20 +38:8–9; không kéo outfit39/demo/secondary lên thay primary |
| Grip direction exact I03/I05; không dùng I07/I09 | 62:24–27; không yêu cầu thumb/ngón khuất phải lộ để bác ref owner |
| Quán nhỏ ven phố chiều tối; F05; một đĩa nem, đĩa lá sung + ít đinh lăng, hai chén tương, hai bát, hai đôi đũa, một cốc ngoài Đào | 64:5;71:9;72:3–5;75:28; arrangement không claim tập quán duy nhất |
| Hướng hai giọng trưởng thành/Bắc nhẹ; Khoai ấm/tỉnh, Đào sáng/trêu kín; ưu tiên thử tiếng Flow/Veo | 38:10 +64:8; chưa actual voice identity/workflow performance approval; Canva assembly owner64:10 |

Working staging: Khoai screen-left/Đào screen-right, cùng cạnh dài; camera phía đối diện là phương án75:30, chưa owner-selected final frame. Camera height/crop/table/prop distances còn điều chỉnh để thấy mặt, plate, bát và cốc/đường tay; không đổi meaning/count. Không thêm cuốn/chấm/ăn để hợp still (71:34–36).

## Dependency map — bằng chứng tối thiểu theo shot

| Gate / owner-role | Cần gì / đủ đến đâu | Còn thiếu; closure đúng surface |
|---|---|---|
| P6 visual reference closeout / CHAR+ART+CONT+owner | Exact integrated version/provenance, primary/food/leaf/serving comparisons, visibility phù hợp staging; owner chọn frame sau review | v0.7/v0.8 và reviews pending, không suy nội dung. Selected neutral still chỉ đóng **visual reference line**, không toàn P6 |
| P6 shot-dependent consistency / CHAR+SHOT+CONT | So primary ở góc thật sẽ dùng; expression Khoai chú ý/khựng/chữa cháy và Đào nhận ra/trêu; grip62, bát/cốc/portion có đường thao tác | Neutral frame không chứng minh expressions/holding/transfer. Dùng refs hiện có; chỉ xin bổ sung khi planned shot thiếu evidence cụ thể. Không cần toàn360°/mọi sheet hoặc chứng minh từng ngón khuất |
| P6 voice / VOICE+AV+owner | Actual samples từng người + đối đáp exact; nghe “cái chảo”, chữa cháy/trêu; duration measured và workflow khả dụng (39:43–60) | Chưa generated/nghe. Hướng38 đã khóa; sample/probe request mới cần authority phù hợp64:8; không ghi voice ready từ text |
| P7 paper shot plan / SHOT+FLOW | Map mọi beat32, speaker, TARGET duration, camera/axis, start/end states, cup turn, plate→miệng→bát, joins, cue F01/F02/AI và ref IDs/status | Có thể lập DRAFT ngay với dependencies PENDING; chưa approved production shots. Không cần motion PASS trước draft hoặc video đầu tiên |
| P8 request readiness / PROMPT+FLOW+RIGHTS+owner | Approved refs dùng trong exact request, shot/probe scope, actual feature/model/audio evidence, rights/input roles, settings/count/cap/cost/stop và approval đúng request | Missing packet/read-back/approval trong run; không lấy direction64, still approval hoặc UI estimate cũ làm quyền video |
| P9 rồi P10–P12 / PERF+CONT+AV+owner | Playable media: ý định ăn thấy rõ, đổi trước contact, bát Đào nhận, hai agency; grip/object states/audio/lip-sync/actual duration; cue đọc đúng | Motion/performance `NOT_TESTED`; kiểm actual output sau authorized request, không ép motion proof vào một still để “đóng P6” |

P6 không complete khi voice/ref needs cho shot còn mở. Nếu voice cần native video probe, giữ status voice PENDING, cho P7 paper design/P8 **bounded probe planning** tiến hành với dependency rõ; không đòi motion đã đạt trước khi cấp phép test chính motion đó. Chưa generation package được approve chỉ vì map này đủ.

## Bước nhỏ nhất, theo thứ tự

1. Kết thúc actual integrated-frame reviews đang pending; root tổng hợp version-specific findings → owner chọn exact frame hoặc rework. Không hỏi lại food/serving/primary direction.
2. SHOT lập P7 paper draft từ32/38 và selected refs/status; chỉ ra góc/biểu cảm/hand-object nào thực cần. Working recommendation: giữ causal payoff trong coverage liên tục thấy Khoai và bát Đào; cut/insert là alternative nếu visibility cần, phải có start/end/join evidence và không cắt mất ý định ăn. Chưa khóa winning method.
3. CHAR/ART/VOICE đóng đúng reference gaps draft phát hiện. Voice paper map có thể làm ngay; actual voice samples và dynamic grip/transfer chỉ chạy qua request đúng quyền. Không generate bộ360° hoặc sửa selected grip vô cớ.
4. PROMPT đóng gói **một probe video/audio có scope cụ thể** theo shot rủi ro, FLOW/RIGHTS kiểm feature/input/request, root đối soát authority hiện có và trình exact request/count/cap/stop cho owner nếu scope mới cần; không suy whole-episode authority.
5. Khi authorized: P9 actual probe → PERF/CONT/AV evidence → owner selection; ghi rõ visual/voice/reference closure và motion còn mở/đã đo riêng, rồi hoàn thiện P7/P8 production package. Text timing/readability kiểm tiếp P11/P12.

## Tối đa ba quyết định owner về sau — chưa hỏi khi thiếu bằng chứng

1. **Chọn exact integrated frame sau reviews:** chọn bản đạt visibility/fidelity hoặc rework nếu chưa bản nào đạt; khuyến nghị không chọn bằng “ảnh đẹp” để miễn finding.
2. **Chọn actual voice samples/workflow sau nghe probe:** giữ native Flow/Veo nếu đúng hướng38 và usable; nếu actual fail, sửa mẫu hoặc trình workflow hậu kỳ với sync trade-off. Không hỏi lại hướng hai giọng hoặc hứa tiếng Việt/lip-sync.
3. **Duyệt exact bounded P8 request:** approve concrete packet với cap/stop hoặc yêu cầu sửa/hold. Chỉ hỏi sau refs/feature/cost/scope đã reviewable; quyền vẫn theo record hiện có, không xin lại approval đã có.

## Coverage/findings và handoff

| Rule / status / severity | Evidence → action, owner need, closure |
|---|---|
| CTD-1/2 MET paper | 32:25–46 +38:25–27: giữ causal payoff/agency; SHOT cover, PERF kiểm actual. Không media pass |
| CTD-3 MET bounded planning | Coverage-liên-tục vs insert ở bước2 có trade-off/join gate; SHOT đề xuất sau evidence góc, owner duyệt shot/request sau |
| G-VIS UNKNOWN / MAJOR | 45:7,75:58 + pending dispatch: actual review/selection chưa có; root+owner đóng bằng exact version/reviews/approval, không approval75 |
| G-VOICE/MOTION UNKNOWN / MAJOR | 39:54,60;45:27;64:8: samples thiếu, motion untested; route VOICE/AV + P8/P9, closure actual audio/video; không dựng thời lượng từ thoại |
| G-AUTH/FEATURE UNKNOWN / MAJOR | Stage-map02:20–23,125–126/common02:32: packet/feature/cost/authority record chưa đọc; FLOW/RIGHTS/root rà records đúng scope trước owner request decision |
| CTD-4/5 MET uncertainty/handoff; execution UNKNOWN | Missing evidence giữ PENDING; map route đúng P6/P7/P8/P9, không implementation/runtime mới. Audio tool N/A cho paper run vì không audio input |

Đã xác định/khóa: content/Q0/primary/grip/food/serving/voice direction; working staging chưa final selection. Còn mở: exact frame, shot-dependent refs, actual voice, feature/request authority và motion. Next: frame review→owner selection + P7 paper draft; adviser không cấp pass/credit hoặc chạy media.

Run log: `EP01-P6-CONTEXT-CTD-02 | AG-CTD-01/P6/PAPER_REVIEW | sources32/33/36/38/39/45/62/64/71/72:1–5/75 + common02/role03/stage-map02 | document-only | report11/PASS_FOR_OWNER_REVIEW-paper map | no owner decision created | root/SHOT + pending frame selection, P8 separately`.
