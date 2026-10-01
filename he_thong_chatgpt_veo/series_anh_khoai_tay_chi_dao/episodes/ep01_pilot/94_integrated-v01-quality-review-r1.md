# EP01 — Đối soát chất lượng tổng thể V01 / R1

2026-10-01. Authority93. Root integration, không toàn bộ quality panel cold-run mới. CINE-LIGHT độc lập thực hiện report06; root đối chiếu script32, approvals78/84, paper shots79/81, request85, actual evidence90/91 và owner feedback92/93. Không tạo media/credit.

## Inputs và capability

Root trực tiếp xem table v0.8 và native V01 n24/1 giây bằng view_image; kiểm Get-FileHash ref `AEB6DFAEE1773109243F9F952235A44F2417C6FB7FB4FAF15BE61C34CA40D924`, V01 `A291BF77C9B913DE43A006F4737DFCB5D27DA2E9811CA6812BDC045C6E81BF76`, trùng hồ sơ78/88. Frame/source linkage dựa phép trích91; root không tự nghe hoặc xem full playback trong vòng này. Dùng owner nghe làm bằng chứng voice, không gán cho critic. Root không maker sửa ảnh hoặc có quyền duyệt take thay owner.

## Coverage tổng thể

| Scope | Kết quả / action | Giới hạn và người xử lý |
|---|---|---|
| Story/context | 32 giữ nguyên chín câu; 84 giữ causal intention→caught→redirect, không feeding/romance. V01 chỉ có hai câu Khoai để thử voice, không được coi mất bảy câu là lỗi final script. | Chưa actual S04, PERF không có production performance pass. |
| Character/performance | Root thấy ở frame1s Khoai đưa tay lên ngực, miệng mở; không phải chỉ subtle facial movement theo85. | Constraint defect khác phán đoán hài hay diễn xuất; nhịp phát hiện/chữa cháy chưa test. |
| Cinematography/light | Baseline78 vẫn được duyệt; mặt và bàn đọc được ở ảnh. Nền phố/ghế/khoảng tối chiếm nhiều khung có thể cạnh tranh focal story. | Aesthetic concern, không technical exposure failure; report06 nêu scoped evidence và phương án. Không tự đổi reference hoặc relight. |
| Food/table | Món giữa, đĩa lá bên trái, chấm/bát/đũa/cốc cùng bữa vẫn nhìn thấy. | Quan sát gross layout tại ảnh, không food specialist rerun hoặc chứng minh contact/texture/serving mọi frame. Không tách rau/chấm sang cảnh ngoài chỉ để dễ generate. |
| Voice/prosody | Owner không chọn V01: chưa đủ ấm/trầm, đều và thiếu truyền cảm. Direction93 đã duyệt, draft95 chuẩn bị. | Nguyên nhân Lite/prompt/duration UNKNOWN; actual R2 chưa tạo, phát âm/lip-sync chưa đóng. |
| Text/disclosure | Chữ tên Khoai có trong native1s, trái85. F01/F02/AI cue trong32 và79 vẫn là hậu kỳ cần actual render. | Không erase/crop watermark để chữa nhãn tên; probe sạch không loại nghĩa vụ AI disclosure của final. |
| Motion/continuity | Gross left/right/table ở sampled evidence91 ổn, tay lệch probe. | Full path/identity/flicker/tất cả contact chưa kiểm. Không nâng static approved thành motion approved. |
| Editorial/transition | Paper79/81/84 có boundary cụ thể,90 technical concat bằng cùng V01 đã thử. | Không có multi-scene production join; cut rhythm, end→start light/props và audio handles UNKNOWN. Không ghi chuyển cảnh đã đạt. |
| Delivery | V01 là diagnostic8s/720×1280 theo evidence, không master30s. | Cue readability/safe-zone/audio mix/export/final approval chưa thực hiện. |

## Sửa theo ưu tiên và dependency

## Root read-back report06 — không dùng reviewer verdict nguyên xi

Report06 đã lưu và root đọc toàn bộ; reviewer thực xem ref/native1s/grid rồi mới đọc SoT. Không có confirmed lighting defect, không yêu cầu relight baseline. Cold-context ở đây nghĩa context mới và không đọc root verdict trước pass; reviewer có đọc maker paper79/81 sau cold-view như dispatch đã cấp.

Root điều chỉnh hai điểm reviewer còn thiếu:

- CL01 giữ provenance UNKNOWN vì không đọc91. Root đã có native-source extraction evidence91 không drawtext và hash actual file, nên tại lớp aggregate **nguồn chữ trong video được xác nhận**; không cần owner lại giải nghi vấn này. Severity root giữ MAJOR theo no-caption probe, khác reviewer MINOR; không sửa lén report06 hoặc yêu cầu generation chỉ để nghe mẫu đã có.
- CL03 chỉ ghi aesthetic concern, nhưng prompt85 giới hạn **only subtle facial movement and speech**: giơ tay ngực ở samples là confirmed visual constraint mismatch, không cần chứng minh đó là utensil action. Root giữ VIS-01 MAJOR trong scope probe; gesture có hấp dẫn hay không và cường độ liên tục vẫn UNKNOWN.
- Recommendation KEEP của critic chỉ hiểu là **giữ bằng chứng diagnostic**, không chọn voice; owner92 đã bác chất giọng và approval93 không thu hồi phản hồi đó. Không có owner exception cho lỗi chữ/tay hoặc final take.

Do đó role đã thiết kế và chạy actual scoped R1, nhưng chưa independently fixture-qualified; cần dùng hai misses trên làm adversarial fixture cho vòng kế tiếp. Không gọi năm expected oracle answers là test PASS. Root critique này là lý do phải có read-back độc lập, không chỉ thêm agent rồi tin mọi kết luận.

1. Voice R2: giữ chữ, direction93; draft95 gồm yêu cầu không nhãn tên/không giơ tay. Tách actual voice acceptance, visual constraint và identity consistency. Không tự chạy hoặc tiêu phần10credit V02.
2. Shot-specific framing: đề nghị cảnh kể ký ức gần hơn để đọc mắt/mặt, nhưng giữ món và bữa ăn trong ngữ cảnh. Cảnh payoff S04 cần khung đủ cốc, đũa, miệng và bát; không áp một crop chặt cho mọi cảnh. Khung/version mới cần owner review.
3. Giữ warm baseline78, ưu tiên giảm cạnh tranh nền bằng framing/depth/lighting proposal có kiểm. Chỉ đổi hướng sáng khi thấy bằng chứng bản thử mất mắt/món hoặc không tách nền. Không coi “cinematic” là tiêu chí đủ.
4. Khi có actual scenes: lưu end/start cùng version/hash, kiểm tay/cốc/A/bát/axis/light và trọn đuôi âm; PERF kiểm người xem có thấy intention trước excuse, AV/CONT kiểm continuity, MASTER kiểm export. Không tự chuyển A sang B vì khó generate.

## Verdict và handoff

`INTEGRATED_EVIDENCE_REVIEW / V01_NOT_SELECTED / P6_OPEN / V02_HOLD / MOTION_AND_MULTI_SCENE_CUT_UNKNOWN`. Đây là đối soát các scope với evidence hiện có, không xác nhận mọi quality technique đã được test.

Đã xác định: voice bị owner bác, nhãn tên và cử chỉ lệch probe; baseline vẫn giữ. Đã chốt: direction93 và quyền CINE review, không quyền generation. Giả định: framing theo chức năng shot có thể giảm cạnh tranh nền, cần test. Còn mở: actual giọng mới, full motion/audio, multi-scene joins/cue/master và request/budget. Bước tiếp: đọc report06, chọn hướng hình thử nếu cần, duyệt exact request95/budget riêng trước voice R2; không bắt owner trả lại những quyết định đã chốt.
