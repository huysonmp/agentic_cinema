# 221 — CONT independent output review

Ngày 2026-10-06. `SAMPLED_FRAME_REVIEW / NOT_RELEASE / NO_FULL_FILM_PASS`.

## Phạm vi và nguồn

CONT đọc 220, 221 và prompt exact `evidence/220/N02-PA-edit-DRAFT.txt`; trực tiếp xem TABLE08/v0.8, PAIR03/v0.3, ba contact boards và các full frame liệt kê dưới đây bằng local image inspection. Không đọc các report reviewer khác hoặc kết luận root tại 221. Không browser, generate, chi credit, commit, sửa nguồn hay delegate.

- TABLE08/v0.8: chuẩn vị trí bàn, serving state, quán/ánh sáng; không suy ra công thức từ ảnh.
- PAIR03/v0.3: nhận diện và trang phục; không dùng nền studio làm chuẩn cảnh.
- OPEN7/N02 là nguồn diagnostic theo 220, không được nâng thành canon production. Những khác biệt chung của hình trial với TABLE08 vẫn là khoảng trống production, không mặc nhiên chứng minh model đã thay đổi nguồn trial.
- Các ảnh local được trích từ native trong `C:/Users/PC/Downloads/du_an_nem_bui/221_n02_pa_v_trial/inspection/N02_{A,B,C}_NATIVE/`. Đọc `inspection.json` và scene-change hints chỉ để định vị/đối soát; verdict hình dưới đây dựa trên ảnh thực sự đã mở.

Đây là kiểm ảnh lấy mẫu, **không playback liên tục hoặc actual listening**. Không chấm bảo toàn voice/lời, khẩu hình, đúng thời điểm hết câu, im lặng của Đào bằng âm thanh, hay chuyển động ở mọi frame. Có 240 decoded frames/output trong metadata; không tuyên bố đã xem hết 720 frame.

## Native identity đã rehash

Đã chạy lại SHA256 trên cả ba native; khớp `inspection.json`.

| Output | SHA256 thực đo | Video theo probe |
|---|---|---|
| `N02_A_NATIVE.mp4` | `35c1a0e527bf4171d8d92ed530f2058d5f7c0c005f372ff6d2f68dacbf524537` | 360×640, H.264, 24 fps, 240 frame, 10.000 s |
| `N02_B_NATIVE.mp4` | `660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535` | 360×640, H.264, 24 fps, 240 frame, 10.000 s |
| `N02_C_NATIVE.mp4` | `9bd637ed26b953d8ea87019c1fa93c1d09228551240f3b85be98815fbd2a494d` | 360×640, H.264, 24 fps, 240 frame, 10.000 s |

Audio/container duration trong probe là 10.005 s. Không lấy duration hoặc PCM hash làm bằng chứng nghe đạt.

## Mẫu thực sự đã xem

Mỗi contact board gồm 20 thumbnail gắn nhãn 0.000, 0.500, …, 9.500 s: tổng 60 thumbnail. Nhãn board là mốc lấy mẫu; ở biên thay đổi dùng full frame, index zero-based, `t = index / 24`.

| Output | Full frames đã mở (`all_frames/frame-NNNN.jpg`) | Số full frames |
|---|---|---|
| A | 0000, 0164, 0165, 0166, 0167, 0168, 0200, 0201, 0239 | 9 |
| B | 0000, 0164, 0165, 0166, 0167, 0168, 0239 | 7 |
| C | 0000, 0084, 0096, 0097, 0098, 0100, 0108, 0168, 0173, 0174, 0175, 0176, 0180, 0239 | 14 |

Tổng 30 full frames, có trùng nội dung với thumbnail. Severity: `P1` = blocker trực tiếp của phép repair/đầu ra; `P2` = lệch cần xử lý hoặc khóa trước production; `OBS` = chưa thấy lỗi trong mẫu, không full take PASS; `UNKNOWN` = mẫu/năng lực chưa đủ kết luận.

## A — sampled continuity FAIL

| Thuộc tính / expected | Observed thực xem và timecode | Severity / hệ quả |
|---|---|---|
| Thay food-only cutaway bằng mặt/miệng Khoai hiện rõ | Frame 0167 (6.958333 s) còn mặt; 0168 (7.000000 s) là món, không có mặt hai người; 0200 (8.333333 s) vẫn món; 0201 (8.375000 s) trở lại two-shot. Scene hint cùng biên 7.000/8.375. Khoảng cutaway được định vị `[7.000, 8.375)`; không đã xem từng frame trong khoảng này. | **P1:** food-only coverage còn tồn tại, không đạt yêu cầu thay cutaway. CONT không gán khoảng này vào chính xác từ nào do không nghe. |
| Không lá mới trên món / không bát chất lỏng mới | Full frames 0168, 0200: một nhánh lá xanh trên đỉnh ụ nem, không có trên wide F0/return. Bát bên phải chứa chất lỏng nâu/cam, khác hai personal bowls trống và hai dipping dishes đỏ ở wide. | **P1:** trạng thái phục vụ ở insert không khớp. Không đoán đây là nước gì hoặc công thức gì; không thể xác nhận bát phải là bát cá nhân đổi trạng thái hay bát thêm, nhưng trạng thái hình đã khác chuẩn. |
| F0 tay nghỉ, chưa gắp; meal lạnh không khói | 0000 (0 s), 0164–0167, 0201, 0239 (9.958333 s): tay đặt trên bàn, không cầm đũa/thức ăn; boards không thấy gắp/đưa bát/uống/khói từ món. | OBS; không chứng nhận mọi chuyển động giữa mẫu. |
| Herbs front-left; hai dip, hai personal bowls, hai resting chopstick pairs; glass ngoài Đào phải | Wide 0000/0201/0239 và thumbnail wide: đủ bố trí này; glass nằm mép phải và bị cắt một phần. Insert chỉ thấy một phần bàn. | OBS ở wide. Không quy đĩa/bát/đũa/glass khuất trong insert là bị xóa. Lỗi chất lỏng/lá là thay đổi nhìn thấy, khác vấn đề crop. |
| Nhận diện, outfit, trục | Khoai screen-left, jacket tối/shirt kem; Đào screen-right, blouse kem và waist tie, lá trên đầu. Không thấy đổi người/trang phục hoặc đảo trái-phải trong mẫu. | OBS; phần thân dưới không đủ lộ để chấm toàn outfit. |
| Không captions | Không thấy caption trong 20 thumbnail và 9 full frames đã mở; native watermark còn nhìn thấy ở wide/insert. | OBS, không quét hết frame. |

Source-fix: cần loại food-only insert và những biến đổi serving-state trong insert, giữ coverage mặt. Report này không cho phép tự sửa/chồng tiếng/retime hoặc chạy batch mới.

## B — chưa thấy blocker serving-state trong mẫu, HOLD nghiệm thu

| Thuộc tính / expected | Observed thực xem và timecode | Severity / hệ quả |
|---|---|---|
| Mặt/miệng Khoai hiện qua phần repair; không food-only cutaway | Boards: close Khoai khoảng 3.0–6.5 s, trở lại two-shot tại 7.0 s. Full 0167 (6.958333) còn close; 0168 (7.000000) two-shot có cả mặt. Không thấy food-only shot trong board. | OBS về mặt hiện trong mẫu. **UNKNOWN** việc return tại 7.0 s có sau từ cuối hay không; phải AV/time alignment riêng. |
| F0 tay nghỉ, chưa gắp; meal lạnh | 0000, 0164–0168, 0239 và board: hands resting, món còn trên đĩa chung; không thấy khói, food transfer, gắp, uống hoặc kéo đĩa. | OBS. |
| Serving geography không đổi; không garnish/liquid bowl mới | Wide 0000/0168/0239: herbs front-left, dip nhỏ bên trái và dip front-right, personal bowls trước hai người, đũa nghỉ hai bên, glass mép phải ngoài Đào. Không nhánh lá trên đỉnh món hoặc bát chất lỏng mới nhìn thấy. Các vật khuất trong close là ngoài crop. | OBS trong mẫu; không báo object deletion. |
| Nhận diện/outfit/trục | Khoai trái / Đào phải, jacket tối + shirt kem / blouse kem + tie. Không thấy mirror hoặc identity swap. | OBS; lower-body outfit UNKNOWN. |
| Không captions | Không thấy caption trong board hoặc 7 full frames; watermark vẫn visible. | OBS. |

B là ứng viên sạch hơn **chỉ theo continuity đã lấy mẫu** so với hai blocker nhìn thấy ở A/C; chưa duyệt N02. Đặc biệt việc return two-shot tại 7.0 s phải so lời/thời gian thực; CONT không chứng nhận khẩu hình/gaze/voice hay full-AV. Gaze close hướng gần trước/meal ở nhiều thumbnail; chưa đủ căn cứ kết luận động cơ ánh nhìn đạt.

## C — sampled visual FAIL do added captions

| Thuộc tính / expected | Observed thực xem và timecode | Severity / hệ quả |
|---|---|---|
| Không added captions | Full 0096 (4.000000 s) không chữ; 0097 (4.041667 s) xuất hiện “Hồi bé, mẹ rang gạo, anh đứng chờ.” trên ngực Khoai. Còn ở 0098/0100/0108/0168/0173/0175 (đến 7.291667 s); 0176 (7.333333 s) two-shot không chữ. 0174 (7.250000 s) chữ đầu bị cắt bên trái. | **P1:** added captions trái prompt exact; lỗi nhìn trực tiếp, không cần nghe để xác định. Biên 4.041667–7.333333 được định vị bằng cặp frame hai đầu; chưa xem liên tục mọi frame bên trong. |
| Mặt/miệng Khoai hiện, không food-only shot | Boards giữ close khoảng 2.5–7.0 s; full 0175 close có mặt, 0176 two-shot có mặt. Không thấy food-only cutaway trong board. | OBS; return 7.333333 s có đúng sau từ cuối là UNKNOWN cần AV. |
| F0 tay nghỉ/chưa gắp; meal lạnh | 0000, 0084, 0096–0108, 0168, 0173–0176, 0180, 0239 và board: tay trên bàn; không thấy khói, ăn/uống/chuyển thức ăn. | OBS trong mẫu. |
| Herbs/dips/bowls/chopsticks/glass đúng geography; không garnish/liquid mới | Wide 0000/0176/0180/0239: tương tự bố trí B; glass mép phải khuất một phần; close không lộ toàn bàn. Không thấy lá mới trên món hoặc bát chất lỏng mới ở wide đã xem. | OBS; crop không là object deletion. |
| Identity/outfit/trục | Khoai trái, Đào phải khi cùng khung; outfit phần lộ phù hợp PAIR03. | OBS; không chấm lower-body hoặc mọi frame. |

Source-fix: cần đầu ra không captions; không xem việc xóa/crop chữ là nghiệm thu tự động. Giữ hold nghe/xem liên tục, lời/nhịp và khẩu hình.

## Khoảng trống chung với production canon

Ở F0 0.000 s và các wide cuối của **A/B/C**, ụ món rộng/sáng hơn hình thái ụ gọn TABLE08. Khung gần hơn, quán/nền được dựng theo nguồn diagnostic. Đây là **P2 / production-anchor HOLD**, đã phù hợp cảnh báo source hierarchy tại 220: không dùng approval trial30 để duyệt variation OPEN7 thành TABLE08 mới. Không gọi các sợi/miếng trong hình là công thức sai, không suy ra định lượng. Bố trí phục vụ wide cơ bản vẫn còn đúng; hai nhận xét này cùng tồn tại.

Ba bản không đủ để chứng minh toàn outfit, độ ổn định chuyển động, đúng từ cuối hoặc giọng. Không thấy steam trong mẫu không chứng minh không có trong toàn take. Không thấy captions B không thay thế scan hết frame. Không có full-film PASS hoặc quyền finishing/release phát sinh.

## Kết luận gửi root

- A: **FAIL ảnh lấy mẫu** do food-only cutaway 7.000–8.375 s và serving-state insert (lá đỉnh + bát chất lỏng khác wide).
- B: **HOLD**; chưa thấy lỗi continuity trọng yếu trong mẫu, nhưng return two-shot 7.000 s cần kiểm lời/AV và production-anchor gap còn mở.
- C: **FAIL ảnh lấy mẫu** do caption xuất hiện từ frame0097/4.041667 s, còn hiện tại frame0175/7.291667 s, mất tại return frame0176/7.333333 s.
- Khóa đã rõ: TABLE08/PAIR03 vẫn giữ vai trò chuẩn; trial không production approval. Không có quyết định chọn native cuối trong report này.
- Bước tiếp: root kết hợp nghe/xem AV đúng capability với hash từng output; giữ blocker A/C và baseline gap công khai. Không tự chi thêm hoặc ghép audio đã duyệt để giả bảo toàn.
