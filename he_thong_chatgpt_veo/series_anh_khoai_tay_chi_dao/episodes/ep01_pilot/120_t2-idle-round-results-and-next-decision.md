# T2 — kết quả 10 lượt Lite và quyết định tiếp theo

Ngày: 2026-10-02. Trạng thái: **VÒNG THỬ ĐÃ KẾT THÚC / CHƯA CÓ BẢN ĐẠT ĐỂ SẢN XUẤT**.

## 1. Điều đã thực hiện và xác định

Theo owner “cứ thử đi, tầm 10 lần cũng dc”, đã chạy đủ 10 lượt mới trên Flow, Veo 3.1 Lite, Frames, dọc 9:16, x1. Tất cả native output dài8s,720×1280,24fps, có audio stream và full technical decode không báo lỗi. Mỗi lượt có quote10 trước khi bấm tạo, ảnh bằng chứng, prompt, asset ID, file và SHA256 trong [nhật ký119](119_t2-idle-performance-experiment-round.md).

Đối soát số dư UI: **1.020 → 920, giảm100credit**, phù hợp10 quotes. Tổng từ mốc1.050 trướcV01 tới920 là130credit trong cap200 hiện có. Không phải sao kê charge từng giao dịch; không mua thêm credit, không nâng Quality.

Input thống nhất: OPEN7 đã được duyệt cho chẩn đoán. Không tạo input mới hoặc thay script/canon. Đối chứng dùng START riêng hoặc START=END cùng ảnh; không dùng frame của clip lỗi làm chuẩn mới.

## 2. Kết quả đối chiếu

Đánh giá sau đây do root kiểm16 ảnh mẫu/clip, không phải independent agent review. Thời điểm lỗi xấp xỉ theo samples; không thay thế xem liên tục toàn clip. Tất cả audio content vẫn **UNKNOWN**: có stream không có nghĩa đã nghe hoặc đã đạt.

| Lượt | Điều kiện | Điều thấy trong ảnh mẫu | Kết luận |
|---|---|---|---|
| R01 | A: nghỉ tự nhiên, START riêng | Tay ổn, giữ bàn ăn; tự thêm mist/steam khoảng1.75–3.75s | Candidate riêng về tay; tổng thể REWORK |
| R02 | A: lặp nguyên promptR01 | Khoai giơ tay/mở miệng; rau và món bị dịch/biến đổi | REWORK |
| R03 | B: living photograph, START riêng | Khoai giơ tay đầu clip; trạng thái mặt thay đổi | REWORK |
| R04 | B: cùng ảnh START=END | Đào giơ hai tay khoảng1.25–2.75s; miệng thay đổi | REWORK |
| R05 | C: chỉ chớp mắt, START=END | Cả hai vẫn cử động tay; mắt/miệng ngoài chỉ dẫn | REWORK |
| R06 | D: motion-only ngắn, START=END | Đào cử động tay khoảng0.75–1.25s; phần sau trông ổn hơn | REWORK toàn8s; chỉ cân nhắc đoạn sau nếu kiểm liên tục |
| R07 | D: START riêng | Hai người giơ tay đầu clip, Khoai còn cử động cuối | REWORK |
| R08 | E: đứng yên tuyệt đối, START riêng | Vẫn có tay, đầu và miệng chuyển động | REWORK |
| R09 | E: đứng yên tuyệt đối, START=END | Khoai giơ tay khoảng1.25s; miệng mở nhiều mẫu | REWORK |
| R10 | A: lặp nguyên lần thứ ba | Khoai giơ hai tay khoảng0.75–3.25s; miệng/đầu thay đổi | REWORK |

Điểm tích cực: nhiều lượt giữ được cả món, rau, đồ chấm và hai nhân vật trong khung hình. Điểm chưa đạt: **khóa diễn xuất nghỉ**, không phải chỉ bố trí lại bàn ăn. R01 không lặp lại được ởR02/R10; START=END cũng không giữ yên phần giữa ở các lượt đã thử.

Đây là bằng chứng của bộ input/prompt/route hiện tại, không kết luận Veo nói chung hoặc Quality luôn thất bại. Không fixed seed, số mẫu ít và nhiều nhóm prompt thay đổi; không suy ra quan hệ nhân quả từ so sánh này.

## 3. Các quyết định đã chốt và ranh giới

- Đã dùng đủ10 lượt được duyệt; dừng vòng này, không tự chạy lượt11.
- Không chọn production winner từ bộ10clip; không nâng Quality để chữa lỗi điều khiển chưa giải quyết.
- Không đổi kịch bản32C-v0.5, nhân vật, claim món ăn hoặc trạng thái canon.
- P6/P7 vẫn OPEN. VoiceV02, kiểm tiếng Việt/đồng bộ môi và CR-01 bàn giaoS04→S05 chưa được giải quyết trong vòng này.
- Media và screenshots lưu local, không đưa lênGit; tài liệu/manifest được commit và push.

## 4. Hướng tiếp theo đề xuất — chưa được duyệt hoặc triển khai

**Khuyến nghị A: tách chức năng cảnh mở khỏi diễn xuất nhân vật.**

Cảnh cần giữ nguyên bàn ăn và điều khiển góc nhìn chính xác: dùng ảnh đã duyệt, thử chuyển động2D có kiểm soát trong khâu ghép; còn cảnh có hành động theo kịch bản mới giaoVeo tạo chuyển động. Đây là thay đổi phương pháp sản xuất cần owner duyệt, không tự thay T2 đã chọn.

Lợi ích dự kiến: không để model tự thêm tay/miệng trong cảnh chỉ cần dẫn mắt. Đánh đổi: chuyển động2D không tạo parallax/góc nhìn3D thật; nếu T2 cần lộ vùng chưa có trong ảnh, có thể phải chuẩn bị thêm khung tham chiếu, kiểm mép món và duyệt lại. Chỉ prototype mới xác định được có giữ chất điện ảnh không; chưa tuyên bố cải thiện chất lượng.

**B: giữ hoàn toànVeo, chuyển từ yêu cầu “nghỉ bất động” sang một hành động nhỏ có chủ đích theo kịch bản.** Phải có chỉ đạo diễn xuất/góc máy cụ thể trước chạy; không hợp thức hóa cử chỉ lỗi hiện có. Có thể tự nhiên hơn nhưng vẫn phải chứng minh timing, continuity và bàn ăn không trôi. Cần duyệt thử mới và credit riêng.

**C: xem liên tụcR06 và kiểm audio trước, thử tận dụng một đoạn ngắn phía sau.** Chi phí credit mới bằng0 cho kiểm/ghép local; rủi ro mất thời lượng hoặc nhịp cảnh. Chưa cắt clip hay duyệt đoạn; ảnh mẫu chưa đủ chứng minh đoạn nào liên tục sạch.

Đề xuất bước kế tiếp: owner chọnA/B/C. Tôi ưu tiênA để kiểm khả năng điều khiển cảnh mở, với một prototype local trước, rồi trình cạnh bảnVeo để so sánh. Không cần thêm agent mới chỉ để đổi prompt: cần chạy đúng vai trò đạo diễn/EDIT/QC đã thiết kế và ghi output thật; agent độc lập chỉ được ghi đã review khi thực sự thực hiện.

## 5. Bàn giao để xem

Folder local owner: `C:\Users\PC\Downloads\du_an_nem_bui`.

Cả10nativeclip: `119_R01.mp4` đến `119_R10.mp4`. Ảnh kiểm theo thời gian: `119_R01_sheet.png` đến `119_R10_sheet.png`. Bằng chứng UI: `119_R##_PRE.jpg` và `119_R##_RESULT.jpg`. Accountpanel balance lưu local riêng, không nhúng công khai.

Để xem nhanh tương phản: R01 (tay tốt nhưng thêm khói), R06 (đầu clip lỗi, sau có thể đáng kiểm tiếp), R10 (lặpA vẫn giơ tay). Native watermark được giữ nguyên.

**Giả định đang dùng:** OPEN7 phù hợp để chẩn đoán, chưa đồng nghĩa duyệt mọi biến thể hoặc toàn tập. **Còn mở:** phương pháp cảnh mở; full audiovisual/independentQC; hành động có chủ đích; voice; continuity; ghép30s và owner duyệt final. Chưa có đầu ra bàn giao hoàn chỉnh của tập1.
