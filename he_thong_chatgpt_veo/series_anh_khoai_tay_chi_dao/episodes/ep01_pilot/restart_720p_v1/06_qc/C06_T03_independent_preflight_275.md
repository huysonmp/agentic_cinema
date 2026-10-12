# REC275 — C06 T03: phản biện độc lập đầu vào

Ngày 12-10-2026. RUN_ID: REC275-C06-T03-INDEPENDENT-PREFLIGHT. Kết luận: **PAPER_CONDITIONAL_GO / LIVE_GATES_PENDING / NO_OUTPUT_OR_AUDIO_APPROVAL**. Không thấy blocker MAJOR mới trên giấy. C06 chưa chọn; C07 HOLD.

## Target, authority và năng lực

Đã đọc đầy đủ `04_requests/C06_T03_prompt_275.txt`, `04_requests/C06_T03_run_275.json` và `00_decisions/C06-one-run-and-T02-audio-approval-275.json`. Tự tính SHA-256 của prompt: **`42b412ec3bb6e7d3dd4b86fd980ad5a9c0a2a494dae899ae2f9bf077028e35d9`**. Báo cáo chỉ có hiệu lực cho đúng nội dung/hash này; prompt đổi phải refresh.

Đã đối chiếu với geometry của final273 và can thiệp274 đã đọc đầy đủ trong cùng chuỗi nhiệm vụ. Đã trực tiếp xem lại exact START `02_refs/C06_START_from_C05_T02_selected_F65_269.png`, tự tính hash khớp **`f091e35fc7c779591c918c47ba34752a8a2c3b30de507cd99dc0e76143e83196`**. Đây là ảnh cuối native C05 F65 trong range [0,66) đã chốt, không lấy T02 chưa được duyệt làm START mới.

Phạm vi: **PAPER_PLUS_EXACT_REFERENCE**. Không đọc maker275; không nghe hoặc xem AV; không browser/API/credit/git/script/media/new tool. Không xác minh live route, quote, tài khoản hoặc binding ID ẩn từ file trên giấy.

Approval275 cho phép một T03, native720p, x1, dự kiến4 giây, debit≤15 từ retake sau current-final và live gates. Owner đã nghe và chấp nhận **tiếng T02** đúng K20, trọn N06, sắc thái hơi ngượng; đó là HUMAN_SOURCE_AUDIO_ONLY trên T02 hash `a2422a7e827ef80be3b95ff07335bd66e8ec1207d14af64a3763098e90c91b6a`. Không duyệt hình T02, sync, điểm nối, T03 mới, đổi preset hoặc tự chạy T04.

## Đối soát can thiệp và dependency

| Scope | Kiểm trên current final275 | Kết luận / gate thực |
|---|---|---|
| Thay đổi diễn theo274-A | Không còn cue yêu cầu ONE mouth corner lift. Ngượng được đặt vào mắt hướng Đào, lực căng nhỏ ở mày, má thả lỏng và nhịp chữa cháy. Môi khép cuối câu, giữ nét bị bắt gặp nhưng điềm tĩnh trong redirect/end. | Khớp can thiệp owner đã chốt. Câu “No instructed mouth-corner lift” là ràng buộc không thêm cue, không phải lệnh diễn một nét nhếch khác. Actual vẫn phải kiểm khóe/má/nụ cười; không hứa bỏ cue sẽ hết cười. |
| Entry và mắt | START đã bị bắt gặp, hai môi khép. Prompt giữ quan hệ nét mặt thừa kế, không repeat discovery; Khoai hướng mắt tới Đào và không thêm nhìn lại A trước chuyển tay. | Không phát sinh beat phát hiện lại hoặc tự nhìn món kéo dài. Mắt có thể chuyển nhỏ tự nhiên; không yêu cầu cứng cơ học để giữ eye target. |
| Khẩu hình | Prompt cho phép phát âm bình thường và răng hiện tự nhiên; không đông cứng miệng hoặc cấm chuyển động nói. Chỉ yêu cầu thấp mặt không chuyển thành nụ cười vui mời món. | Khắc phục rủi ro hiểu sai “không lộ răng”. MAJOR diễn không được chấm chỉ vì thấy răng; phải xem trạng thái khóe/má/ý định trong lời. Sync T03 vẫn phải kiểm mới. |
| N06 và K20 | Chỉ Khoai nói đúng một lần “Anh gắp cho em mà.”; saved K20 giữ nguyên. Đào nghe khép môi, không thoại nữ hoặc câu mới. | Không thay canon/preset. Approval tiếng T02 không chuyển sang T03: cần nghe output mới đúng người, giọng, đủ âm cuối và nhịp. |
| Thứ tự lời–tay | Nói trước khi chuyển; ngay sau âm cuối “mà” chuyển SAME A, không pause diễn thêm và không liếc món mới. | Giữ can thiệp tập trung vào diễn, không tự đổi beat tay thành chạy song song lời. Timing actual4 giây vẫn là giả thuyết; nếu ép nhanh/lời cắt hoặc không đủ redirect/hold thì REWORK, không tự tăng thời lượng. |
| SAME A / own pair | A một miếng, vẫn kẹp tại tip đôi đũa riêng, tay ngoài trái Khoai; đường trên bàn hướng bát Đào, không ăn/thả/nhân miếng/đổi tay/đổi đũa. Tay trong nghỉ. | Geometry kiểm soát giống273, không thay thành hand test riêng. Kiểm toàn native mới, không suy ra đạt từ T02. |
| Air gap và bát nhận | Dừng phía Khoai của bát Đào, cao hơn vành, khoảng hở đọc được; A chưa được nhận. Không chạm/thả sớm vào bát, đĩa chung hoặc chấm. | Giữ ranh giới handoff. Khoảng hở lời prompt không tự là chứng minh vật lý; cần ảnh dày và chuyển động thực ở endpoint. |
| Cốc/bát Đào | Cốc giữ nâng trong tay ngoài cả cảnh và ending; bát riêng rỗng trên bàn, lòng và vành đọc được. Không hạ/đặt/uống/đổi tay/nhấc bát nhận sớm. | Tách cốc và bát đúng START. “Không phản ứng mới” vẫn cho cô nhìn miếng được mời cuối cảnh như prompt mô tả, không cho thêm beat nhận món. Toàn T03 phải giữ đủ trạng thái, không chỉ prefix. |
| Bối cảnh và món | Giữ two-shot, hai mặt, áo, ánh sáng, bàn/rau trước trái/hai chấm/hai bát, nem nguội không hơi và native watermark. | Không cứu diễn bằng crop/insert món khiến người nói mất mặt. Không dùng props đẹp bù diễn. |

## Live gates và điều kiện dừng

Trước submit, root đọc đầy đủ hai report current-final và kiểm đúng hash; một START đã chốt + một saved K20, không thêm D06. UI phải chứng minh route Video Ingredients, Omni1.1 Flash, native720p/9:16/4s/x1, Agent off, âm thanh bật; quote≤15, đủ retake và đúng quyền một output. Run hiện giấy còn quote/balance/native null, submit0: **chưa phải live readiness**. Không mở reserve hoặc mua/topup.

Sau submit, nhận nguồn mới/hash/decode, kiểm đủ khung, báo cáo maker và critic độc lập, nghe K20/N06/sắc thái và kiểm AV/sync trên đúng T03, cùng điểm nối C05→C06. Không chuyển owner audio approval T02 thành PASS T03. Nếu diễn vẫn vui, cốc vào bát, geometry/ý nghĩa/lời có MAJOR, **STOP**; không tự T04 hoặc fallback tách coverage.

Run trước chi ghi180/500, còn320, retake73, reserve110 đóng. Đây là ledger đọc trên giấy; debit thực phải đối soát live. Through-C05 hiện26,333 giây; nếu dùng4 giây C06 thì C07–09 còn4,667 giây đến35 giây. Chưa có actual timing đủ chuỗi sau: không bảo đảm vừa trần hoặc tự bỏ beat. C07 chỉ mở sau chọn exact range và đóng các gate của C06.

## Tổng hợp

Current final đã bỏ cue nhếch môi, giữ nói tự nhiên và dùng mắt–mày–nhịp cho hướng ngượng; không thấy thay geometry hoặc canon ngoài phạm vi owner275. **PAPER_CONDITIONAL_GO không là output PASS hay dự báo chắc chắn.** Bước tiếp do root thực hiện là live gates rồi tối đa một T03 đã được owner cho phép; critic không thao tác paid/browser trong nhiệm vụ này.
