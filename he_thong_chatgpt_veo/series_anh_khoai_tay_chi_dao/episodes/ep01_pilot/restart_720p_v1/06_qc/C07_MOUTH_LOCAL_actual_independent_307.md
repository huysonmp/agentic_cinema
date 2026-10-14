# REC307 — Kiểm actual độc lập bản sửa miệng local C07 v1

**READY_FOR_BUNDLED_OWNER_REVIEW / REVIEW_ONLY / NOT_PRODUCTION_SELECTED.** Chuỗi mở miệng MAJOR của Khoai ở F5–14 đã hết trên các khung encoded thực kiểm. Không thấy lỗi vá hình MAJOR buộc sửa local thêm trước trình owner; độ mượt khi phát, AV, clearance và điểm nối vẫn chưa được chứng nhận.

## Authority và phạm vi

- Đọc đủ authority307, acceptance306, script `scripts/repair_ep01_c07_mouth_307.py`, năm scope tests trong script test, repair_manifest và encoded native_evidence.
- Owner307 cho sửa local vùng miệng F5–14, giữ tiếng exact3s đã duyệt306 và hành động khác, reviewer và join review-only. Không mở paid/budget/production EDL/release.
- Reviewer chỉ local read/view/hash và report; không chạy compositor/test/decoder, không sửa media, nghe/phát AV, browser/API/chi/Git/EDL.
- Tự kiểm native305 SHA `12a0baa2d7ccedfaa16631b7cddd2c4331480e4fa8784880403eb425a8fb397b` và exact clip owner đã nghe306 SHA `7a7d2bc4d4fdd7a4ec220daa67477e3063583d1b2f9366a089318b9ab1104e18`.
- Tự kiểm output `07_edits/C07_TWOREF_LOCAL_MOUTH_v1_REVIEW_ONLY_307.mp4`, SHA `3637542889efc4dacbd1c86ebd67988b3e65472dd990fbc4a7ebc7ec9dc94d9c`, khớp manifest/evidence/root.
- Trực tiếp xem đủ sáu `full12_01..06.png`:72 khung F0–71, không padding; hai mouth_compare đủ F0–19; full encoded F0/F4/F5–16/F48/F71 (16 khung).
- Đối chiếu full original F4/F10/F15, preencode composite F10, encoded F10; đối chiếu source/reference và findings305 đã thực kiểm ở lượt trước. F bắt đầu0; PNG=F+1; t=F/24.
- Phạm vi **ALL_FRAME_STILLS_NOT_CONTINUOUS_AV**. Evidence đọc H.264720×1280/24fps/72F/3s, AAC48kHz stereo3s, full decode success; không biến metadata thành AV PASS.

## Script, phạm vi sửa và invariance

- Script kiểm exact hash hai nguồn, đủ96 PNG và fps24, decode lại rồi so hash đủ96; chỉ lấy F0–71. Không ghi đè đường dẫn output/evidence có sẵn.
- Compositor chỉ F5–14 trong rectangle `(180,526,296,590)`; dùng donor native F4/F15 cùng nhân vật, không vẽ mới/toàn mặt/đổi actor. Registration quanh texture `(158,490,315,640)` loại vùng miệng và tìm translation ±8px, dừng khi chạm biên.
- Hai donor pha dần theo frame, feather10px nằm trong rectangle. Manifest ghi dx/dy nhỏ −1..2px, không chạm search limit; không dùng scaling/warping toàn đầu hoặc frame hold toàn cảnh.
- Code có assert ngoài patch không đổi, ngoài10frame không đổi, PNG lưu đúng array; manifest ghi outside patch exact và62frame không sửa exact trước encode. Reviewer đã đọc code/evidence, không tự tính lại toàn bộ pixel arrays.
- Năm test kiểm phạm vi pixel/frame, translation và feather bằng ảnh synthetic; root báo pass. Chúng không chứng nhận mỹ thuật, donor thật, AV hoặc physics.
- Encode lại H.264 có mất mát nên **không** gọi mọi pixel encoded ngoài patch exact. So hình encoded F10 với original/composite không thấy biến dạng mắt/mũi/cổ/Đào hoặc props do encode/sửa.
- Script copy AAC của exact clip306 và so mọi packet hash/pts/dts/duration; manifest ghi142packet/timing equal, nguồn còn đúng hash. Đây là bằng chứng kỹ thuật giữ tiếng đã duyệt, không reviewer nghe lại media307.

## Findings actual encoded

| Mục | Quan sát độc lập | Kết luận trong phạm vi ảnh |
| --- | --- | --- |
| Miệng Khoai | Original F10 há miệng rõ; encoded F5–14 là đường môi khép, không còn khoang tối/lưỡi/răng của chuỗi phát âm cũ. F0–4/F15–71 cũng nhìn khép. | Blocker visual mouth305 đã được xử lý trên72F. Không suy anh im tiếng từ hình. |
| Donor / edges | F4 vàF15 donor đều môi khép; F4→5 vàF14→15 không thấy nhảy vị trí môi rõ. F10 ở full resolution không thấy rectangle cứng, viền sáng hoặc hai đường miệng tách nhau. | Không thấy MAJOR patch/ghost trong ảnh; chuyển texture pha donor có thể hơi mềm, không đủ khẳng định stutter/flicker khi phát. |
| Khuôn mặt và diễn | Mắt/mày/mũi/đường đầu/cổ của Khoai không bị thay bằng donor; blink F54–57 còn. Đào vẫn quả đào có cuống/lá và khẩu hình phản hồi; thân/tay tiếp diễn trong đoạn sửa. | Không thấy freeze toàn đầu/toàn cảnh hoặc swap actor; không cấp continuous-motion/acting PASS. |
| Canon / bát | Hai bát từ F0; Đào nâng đúng bát của cô bằng tay trong, bát Khoai vẫn trên bàn; không có bát thứ ba trong F0–71. | Lỗi duplicate bắt đầuF77 của native305 nằm ngoài approved3s, không phải đã được vá/xóa. |
| Tay–cốc / A | Cốc nâng trong tay ngoài xuyên72F, A còn trên tips, không thấy thả/ăn/gắp mới/cho miệng; bát rỗng được đưa tới dưới A. | Giữ hành động đã quan sát305; không suy force/contact/miếng nem bất biến từng pixel. |
| Clearance / endpoint | F48 vàF71 bát/tay đỡ che một phần tay nghỉ Khoai; không đọc đủ khoảng hở phía sau. F71 Đào đang khép mắt trong blink. | CLEARANCE_OPEN; F71 không tự thành C08 approved input, blink phải xét nhịp và exit thực. |

## Cổng trình gói và production

- Đủ trình **gói review owner** sau khi root có review-only C06→C07 trial và EDIT reviewer; báo rõ sửa local10frame và bằng chứng kỹ thuật giữ AAC306.
- Không thấy lý do hình hiện hành buộc làm v2 trước trình gói. Nếu phát thực phát hiện flicker/stutter hoặc lệch môi/tiếng, quay lại sửa local trong scope đã duyệt rồi review exact output mới; không tự miễn lỗi.
- Reviewer không actual listening/continuous AV; owner306 chỉ đã duyệt exact3s tiếng D06/N07/âm cuối/nhịp. Bản307 còn cần xem AV để đánh giá độ mượt vá và lip-sync; không mở rộng approval306 thành full-media PASS.
- C06→C07 seam, clearance sau bát, exit/blinkF71, C08 endpoint và timing final30/rough35 giữ OPEN. Không có join mới được kiểm ở report này, không thay production EDL hoặc chọn range.
- Giữ native305/clip306 và evidence; không paid/retry/budget transfer. Review local không làm thay ledger265/500,remaining235,first80/retake0/post45/reserve110 CLOSED.

## Bổ sung sau báo cáo ban đầu — kiểm packet độc lập trong lượt REC308

- Dùng FFprobe hiện có do root cung cấp path, reviewer tự trích audio packets từ exact approved3s306 và localmouthv1; mỗi nguồn142packet.
- So toàn bộ danh sách có thứ tự `data_hash` SHA-256 và `pts_time/dts_time/duration_time`: **bằng nhau**. Không chỉ lấy boolean từ manifest root.
- Đây là read-only xác minh giữ AAC/timing, không actual listening/PCM/continuousAV của reviewer; không hồi tố phạm vi kiểm ban đầu hoặc mở approval media/production.
