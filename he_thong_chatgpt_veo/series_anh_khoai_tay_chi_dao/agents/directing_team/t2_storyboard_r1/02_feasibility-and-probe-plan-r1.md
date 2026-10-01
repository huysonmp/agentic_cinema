# EP01 T2 — Feasibility và probe plan R1

2026-10-01; `EP01-T2-CTD-R1`; AG-CTD-01 / PAPER_TECHNICAL_PLAN. **PROPOSAL_COMPLETE / EXECUTION_UNKNOWN**. Không storyboard approved, generation-ready hoặc media PASS.

## Inputs, authority và intent ledger

Đọc FULL production02/03 (CTD addendum), directing01/10, pilot05/R1 và07/R2, episode32/C-v0.5,78/v0.8,79/v0.1,81/v0.1,84,88,89,93,95/draft,98; production13/2026-10-01. Không đọc SHOT draft, reviewer/oracle; không xem/nghe media hoặc account UI. Các refs được biết qua hồ sơ, chưa kiểm bytes trong run này.

98 chọn **T2: món→mặt Khoai/ký ức→bữa ăn hiện tại**; không duyệt từng move/crop/edit. Giữ chín câu32, warm78, địa lý/D2A84, bạn trưởng thành. B01 món/lá/chấm rõ cùng hai người; B02 attention nâng tới Khoai; B04 người kể và món vẫn liên hệ; B05–B06 trở lại bàn trước A. B07–B09 thấy định ăn→bắt gặp→đổi hướng trước contact→Đào hiểu/đưa bát. Ending trở về bữa ăn, không insert chứng minh công thức/mẹ làm Nem Bùi.

S04-A kết nem **trên đũa trên bát, chưa thả**; S05 mới thả một lần rồi gắp phần khác. CR-01 A-through-transfer vẫn PENDING. S01–S05 là coverage logic, không native request count. Quyền chỉ tài liệu/local read + public Google read-only; không UI/API/upload/generation/credit/git. Budget88 không tài trợ probes mới; V01 không chọn, V02 HOLD,95 chưa duyệt.

## Evidence kỹ thuật và giới hạn

Kiểm trực tiếp ngày2026-10-01: [Flow models](https://support.google.com/flow/answer/16352836?hl=en), sections Veo3.1: text/frames Lite/Fast/Quality 4/6/8s; Ingredients Lite/Fast 8s, Quality unsupported. Extend được liệt kê cho Lite, với video Veo3.1 8s; Fast/Quality không có tính năng Extend. Đây docs tổng quát, không xác nhận account hay seamless output. Target10–14s trong79 không thành một native request10–14s.

[Create videos](https://support.google.com/flow/answer/16353334?co=GENIE.Platform%3DDesktop&hl=en), kiểm cùng ngày: frames mô tả hành động giữa ảnh đầu/cuối; availability tùy vùng. Voice-reference hướng dẫn Omni Flash/Ingredients, không chứng minh control này cho Veo. Không chuyển model theo suy đoán. Camera move, identity ổn định, tiếng Việt/prosody/lip-sync và audio qua extension: **UNKNOWN**, không được docs bảo đảm.

89 ghi Scenebuilder từng có UI/evidence; [URL help trong89](https://support.google.com/labs/answer/16935718?hl=en) fetch timeout lượt này. Khả năng ráp hiện tại, xuất/audio/timing account còn UNKNOWN. Concatenation không tự chứng minh A nhìn liền. Không dùng Vertex API thay bằng chứng Flow.

## Probe briefs — đề xuất, chưa requests

Mọi probe giữ exact ref/version, warm, geography, nhân vật/meal và dialogue liên quan làm controls. Không tự đặt duration/count/cap thành approved. Một vòng chỉ thay biến đã khai báo; phát hiện confound phải ghi, không quy nguyên nhân chắc chắn.

| ID / câu hỏi | Biến và input dependencies | Quan sát đạt / lỗi, closure |
|---|---|---|
| V / giọng |95 là vòng riêng: cùng ref/crop/máy khóa; thay direction giọng93 và constraints probe đã khai báo trong95. Không thêm camera/prop. | Nghe đủ exact lời/đúng Khoai, ấm/tỉnh/nét cười kín; lỗi nuốt câu, gằn, Đào nói sai. Owner nghe + AV; ASR chỉ dẫn vị trí. Không khóa voice-ID từ prompt. |
| R / reframing tĩnh | CHAR/ART cần approved framing candidates từ78/P03, không sinh trong run này. Biến crop/composition ngoài A; không camera motion, không prop action. | Hai mặt/identity/outfit và toàn meal được bảo toàn; nem rõ, vùng cue còn dùng được. Fail mất lá/chấm/cốc/watermark hoặc mặt quá nhỏ. CONT/CINE/ART kiểm actual still; không gọi motion PASS. |
| C / chuyển attention | DOP/SHOT khóa start/end composition T2 sau R; thử food→face riêng, props nghỉ, không transfer. Voice chưa đạt thì không dùng để chấm giọng. | Món dẫn lên Khoai, còn bạn/bữa ăn; không biến mặt/đạo cụ, không “zoom” chỉ bằng món phình. Fail camera che món/mất relation hoặc move làm nghĩa ký ức sai. PERF/CINE cold playback rồi đối chiếu. |
| P / causal motion | Keyframes đúng trạng thái79/81, approved grip/refs; camera A ổn định, không thử camera C đồng thời. Biến choreography/biên độ sau owner shot choice. | Plate→miệng chưa contact→khựng→đổi hướng; Đào thấy rồi đặt cốc trước đưa bát; A không nhân đôi/đút/biến mất. CONT/PERF xem actual path và agency; vẫn cần audio gate riêng. |
| L / A dài và joins | Chỉ sau UI route evidence và timing tiếng thật; input là source clip đủ điều kiện, boundary states/audio. Biến route kéo dài/assembly được duyệt. | A đọc liên tục không replay/reset/âm bị cắt; J12/J23/J34 khớp; J45 giữ A chưa thả→thả một lần. Fail drift mặt/grip/cốc/bát/portion hoặc voice đổi. Lưu boundary frames/playable audio, đo actual in/out. |

## Findings và request gate

CTD-1/2: MET giấy về intent/boundary, không self-review chất lượng. CTD-4: UNKNOWN/MAJOR cho move, full-meal/identity, lời/audio, long-A và joins. Cue F01/F02/AI giữ exact32, xử lý hậu kỳ theo79; không chữ sinh máy/name labels. P11/AV/Fact phải đọc actual export, không bịa safe-zone/dwell.

Nếu C thất bại: trình evidence và choices sửa biên độ/ref/move hoặc owner chọn hold alternative; hold có sensory trade-off, không tương đương T2 move. Không tự chuyển E1/B. Nếu L thất bại: FLOW phản biện route, root trình owner A rework/B hoặc CR-01; không nối ngầm qua transfer.

Trước bất kỳ chạy: PROMPT lập exact request/version, probe-ID, inputs/rights/hash, mode/model/settings, native duration, outputs/count, current UI credit/cap, retry/stop và reviewer scope. FLOW kiểm tương thích; RIGHTS kiểm input; owner duyệt request/spend riêng. Giá/cap/features account hiện UNKNOWN. UI khác approved hoặc terminal không rõ→HOLD, không duplicate/retry.95 có gate riêng; không dùng nó làm quyền R/C/P/L.

## Handoff năm mục

1. Đã xác định intent T2 và technical questions phân tách.
2. Đã chốt upstream32/78/84/93/98; chưa shot/probe approval.
3. Giả định working: composition/diễn có thể dẫn attention; cần actual evidence.
4. Còn mở refs theo state, giọng, move, route/audio/cost và CR-01.
5. SHOT cụ thể hóa; reviewer giấy độc lập→root/owner choices→P8 exact request; media reviews sau quyền. R1 chỉ tạo file này, không đóng P6/P7 hoặc fixtures.
