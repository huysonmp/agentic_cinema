# REC267 — C05 T02 actual: maker DIR / DOP / ACT / EDIT

Ngày: 12-10-2026. RUN_ID: `REC267_C05_T02_MAKER_ACTUAL`. Kết luận: **hình đủ điều kiện tiếp tục kiểm tiếng/AV và điểm nối; C05 NOT_SELECTED, C06 HOLD**. Không thấy lặp MAJOR mất bát Đào hoặc reset cốc xuống bàn của T01. Đây là đóng góp maker theo ảnh actual, không phải phản biện độc lập, không phải approval source/range/export.

## Target, authority và phạm vi thực hiện

- Target: `05_native/EP01_720_C05_T02_NATIVE.mp4`, SHA-256 tự kiểm đọc file hiện hành: `3df61217ddf6d09792fe1e5991c3668d115ce5648c00802f196d87abe57d23df`.
- Exact START: `02_refs/C05_START_from_C04_T02_selected_F143_263.png`, SHA-256 tự kiểm: `2e4f4a5fbf0d5f310010762d26d0c74f08bfb2da3eab792f69a3be568b94c2db`.
- Đã đọc đầy đủ `217_recovery-tier4-runtime-gates-and-questions.md`, resume266, scoped-autonomy238, rough-cut-35s-approval264, C05_T02_run265, run-registry265, REC264/265, maker264 và prompt cuối T02. Không đọc báo cáo độc lập T02 hoặc tự nhận đóng vai độc lập.
- Native evidence do root tạo: `C:/Users/PC/Downloads/du_an_nem_bui/265_C05/C05_T02_QC_267/native_evidence.json`: H.264, 720×1280, 24fps, 96 khung/4.000 giây hình; AAC stereo 48kHz, 4.010 giây container/audio; báo full decode success, 96 extracted frames. Maker kiểm hash, đọc evidence, không tự chạy lại decode/probe và không coi có audio stream là đã nghe.
- Đã xem **tất cả F0–95** trong 12 board `action_all/action_all_01.jpg` tới `_12.jpg` và đối soát manifest exact hash. Đã xem PNG nguyên khung F0/F9/F46/F48/F56/F65/F95 trong `all_native_frames` và exact START nguyên khung. `00001.png` là F0; tên PNG là frame zero-based +1.
- Evidence scope: **ALL_FRAME_STILLS**, không phải CONTINUOUS_VISUAL hoặc FULL_AV. `actual_listening = NOT_PERFORMED`; `heard_text = UNKNOWN`; `voice_identity = NOT_CERTIFIED`; `lip_sync = NOT_CERTIFIED`. Không phát/nghe nguồn, không browser/API/credit/git/cài mới/chỉnh media, không chọn take hay xuất endpoint.
- Frame zero-based Fn có thời điểm n/24 giây; range đề nghị dùng end-exclusive `[start,end)`. Thời điểm miệng bên dưới chỉ là hình dạng quan sát được, không gán từ/âm tiết theo phỏng đoán.

## Kiểm trạng thái bàn, A và điểm vào C04 → C05

| Yêu cầu / vị trí | Quan sát actual | Đánh giá maker |
|---|---|---|
| Hai bát cá nhân rỗng riêng biệt | F0–95 có bát Khoai bên trái dưới A, bát Đào bên phải plate. Vành và lòng bát Đào đọc được cả F0/F48/F95; không bị cốc thay thế hay che lòng bát. | MAJOR mất bát T01 không lặp. Bát nhận còn sẵn cho chuỗi sau. |
| Cốc Đào giữ nâng trong tay ngoài bên phải | F0–95 vẫn ở dưới mặt và cao hơn bàn/bát; không đặt xuống, uống hay đổi tay. | MAJOR reset thấp sát bàn T01 không lặp. |
| Exact vị trí cốc tại join | START đáy cốc khoảng y740–745; F0 khoảng y755–760; F95 lại gần y740–745, quan sát bằng ảnh 720×1280, không đo track bằng phần mềm. | **MINOR continuity drift** khoảng 10–20px ở entry, có dịch nhẹ trong take. Không gọi exact pixel/pose lock hoặc không hề di chuyển; phải xem join thực. Không tương đương reset xuống bàn của T01. |
| Cùng một miếng A / đôi đũa riêng Khoai | F0–95 chỉ một miếng trên cùng đầu đôi đũa ở tay ngoài màn hình-trái, giữ trên phía bát Khoai, xa miệng. Hình dáng/màu/độ xiên liên tục trong ảnh; không thấy mất/nhân đôi. | Không thấy gắp mới, ăn, trao, thả; tính liên tục thị giác phù hợp SAME A, không là chứng minh định danh pixel của vật thể sinh. |
| Tay, đũa và bát Đào | Tay trong nghỉ bên trái bát Đào; own pair vẫn nằm trên bàn phía phải bát. Tay trong Khoai nghỉ cạnh bát mình. | Không thấy thêm cặp đũa, đổi tay hay reach gây đứt chuỗi. |
| Mặt/mắt entry | START Khoai nhìn xuống A; F0 actual đã nhìn Đào. Đào đã nhìn lại Khoai từ F0, không lặp quay đầu từ cốc. Hai môi kín ở F0. | **MINOR/PERF coverage**: eye shift Khoai từ A sang Đào diễn ra giữa hai source, không có beat chuyển mắt đó bên trong T02. Cần xem cut có đọc thành phản ứng tự nhiên; không quảng cáo T02 chứa đầy đủ eye-shift yêu cầu. |
| Nem nguội, rau và hai chấm | Plate chính, herbs trước-trái và hai chấm đỏ trước-trái plate / trước-phải còn đọc được F0–95. Không thấy khói/hơi nóng. | Giữ logic bàn rộng, không dùng crop để che prop hoặc diễn. Không chứng nhận thành phần món từ ảnh. |

Miếng A/tay có tái dựng nhỏ về góc/độ cao so START, nhưng vẫn cùng vùng dưới ngực/trên bát riêng và không tiến về miệng. Framing/đồ/ánh sáng/face identities giữ được ở mức ảnh actual. Sai số nhỏ của join chưa được đóng bằng việc native decode tốt hoặc bảng trên.

## DIR: nhiệm vụ kể chuyện và beat map quan sát được

C05 tiếp boundary A đã chốt: Đào đã nhìn lại cuối C04, bắt tình huống Khoai giữ A; câu nói của cô tạo nhịp biết chuyện, Khoai im và khựng trước chữa cháy C06. T02 không đưa A vào miệng, không đưa qua bát Đào và không làm excuse sớm. Không đổi canon, câu N05 hoặc voice D06.

| Khung / giây | Beat hình thực | Ý nghĩa dựng và giới hạn |
|---|---|---|
| F0–8 / 0.000–0.333 | Hai người nhìn nhau, miệng kín, A giữ yên; Đào đã aware. | Entry ngắn đúng hướng boundary; Khoai đã chuyển gaze tại entry. |
| F9–17 / 0.375–0.708 | Môi Đào hé/mở, blink rõ F13–15, mắt trở lại; Khoai giữ môi kín. | Có hình diễn lời nữ. Không suy ra đã nói từ gì. |
| F18–19 / 0.750–0.792 | Miệng Đào thu gần kín, mắt vẫn về Khoai. | Khoảng ngắt/khẩu hình; không tự chia thành hai câu. |
| F20–45 / 0.833–1.875 | Miệng Đào tiếp tục đổi dạng, nét nhẹ biết chuyện, không quát; nam vẫn im. | Vùng hình phù hợp một lượt lời nhưng chỉ actual nghe mới xác nhận đúng N05, duy nhất một người nói, âm điệu. |
| F46–55 / 1.917–2.292 | Môi Đào kín. Khoai blink F49–52, mở lại F53–55, tay/đũa hầu như giữ. | Chuyển vào reaction, chưa excuse. |
| F56–65 / 2.333–2.708 | Khoai mắt mở rõ hơn, môi hơi cụp, bất động dè dặt; Đào kín môi, nhìn chờ. | Nhịp bị bắt/khựng đọc được tiết chế; endpoint F65 giữ cả hai mắt/mặt và A. |
| F66–95 / 2.750–3.958 | Tiếp tục giữ trạng thái, Đào đổi nhẹ hướng mắt xuống rồi về; không có action mới rõ. | Tail kéo dài có thể giảm nếu lời/âm hậu/cảm giác ngừng cho phép. Không mặc định phải dùng cả 4 giây. |

Không có confirming glance của Đào từ A rồi quay sang mắt Khoai tách thành một beat rõ; cô đã nhìn anh. Không thiếu hành động lõi boundary A, nhưng là coverage hạn chế của tiểu cue. Không dùng một từ chung như “diễn tốt” để thay quan sát này.

## DOP và ACT: đóng góp maker

DOP: bố cục two-shot dọc giữ hai mặt, A/own pair, hai bát, cốc và plate; không thấy cut/zoom/face morph/caption/logotype mới trong 96 ảnh. Ánh sáng ấm ổn, depth/background không giành beat chính; native watermark còn. Góc tay/cốc không che miệng người nói hay bát nhận. Không thấy lỗi tay lớn tại các PNG đủ khung đã xem, nhưng không nhận đã kiểm hoàn hảo giải phẫu mỗi ngón ở mọi khung.

ACT Đào: intent biết chuyện thể hiện bằng gaze đã trở lại, miệng nhẹ và nụ cười kín cuối, không head turn discovery lặp. Blink trong vùng diễn lời không tự là lỗi. Không thấy broad laugh/quát bằng hình; âm lượng, thân mật hay “nữa à” nâng giọng chưa nghe nên UNKNOWN.

ACT Khoai: silent listener rõ vì môi kín F0–95; giữ A xa miệng, không bắt đầu chữa cháy. Blink và mắt mở sau câu hình F49–65 tạo phản ứng ngượng/khựng khá nhẹ. Tay dịch rất nhỏ, không có arrested hand gesture tách rõ; phần caught vẫn nhờ nét mắt/môi và sự dừng. Nếu owner cần ngượng rõ hơn phải đánh giá AV/story join trước, không tự coi đây là quyền tạo take mới.

## EDIT: range đề nghị có điều kiện, chưa chọn

Ứng viên maker để kiểm: **`[0,66)`**, giữ **F0–65**, 66 khung = **2.750000 giây**, endpoint F65/t=2.708333. Giữ entry 0.375 giây trước miệng hé, toàn vùng biến đổi môi nhìn thấy, blink nam và khoảng 0.833 giây từ F46 tới ranh giới cut 2.750. Khoảng 10 khung F56–65 giữ nét caught mắt mở trước cắt; không cắt ngay lúc mắt nhắm F49–52. Không đổi source hoặc tạo media trong task này.

Điều kiện bắt buộc trước SELECT/endpoint C06:

1. Nghe **đúng target hash T02** đủ một câu “Chờ em quay lưng nữa à?”, đúng Đào/D06, không lời nam/extra; đánh giá âm cuối/ambience không bị range cắt. Nếu audio kéo sau 2.750 hoặc reaction cần lâu hơn, nới range từ source thay vì ép cắt lời. Không chuyển approval tiếng T01 sang T02.
2. Kiểm miệng–tiếng và timing phản ứng trên exact source/range có AV capability hoặc owner checkpoint; marker F9–45 không tự là lip-sync PASS.
3. Xem actual C04 selected F143 → C05 F0 ở tốc độ dựng để kiểm chuyển gaze, glass drift và A. Chưa ghép hay xem join trong scope maker này, nên JOIN = NOT_BUILT/NOT_CERTIFIED.
4. Root đọc đủ phản biện độc lập và xử lý bất đồng trước dùng F65 làm input C06. Không suy ra downstream được GO chỉ vì bát/cốc T01 đã sửa.

Giả sử range này qua gate, tổng tới C05 là `(566+66)/24 = 26.333333` giây; còn **8.666667 giây** cho C06–09 tới trần rough35. Dùng cả source4s sẽ là27.583333, còn7.416667. Chưa có timing actual C06–09 nên không hứa fit35, không ép tốc độ hay bỏ beat/câu để đạt số học.

## Findings mở và bước tiếp

- Hai MAJOR đạo cụ của T01 **không được quan sát lặp** trên target actual T02; không kích hoạt same-major-twice từ chỉ riêng những lỗi này.
- MINOR entry glass/pose drift và eye-shift ngoài take: chưa có join evidence để đóng. Không sửa bằng crop, đặt cốc xuống, làm bát xuất hiện lại hoặc retake tự động.
- FULL_AV / ACTUAL_LISTENING / voice / lời / sync còn HOLD. Audio có thật theo probe chưa giải quyết scope nghe. Source visual dùng được cho bước kiểm tiếp, chưa selected.
- C05 candidate `[0,66)` và F65 là **PROPOSAL_CONDITIONAL**, không phải EDL approved hoặc START C06 đã tạo. C06 tiếp tục HOLD.
- Bước tiếp: root tích hợp report actual độc lập, checkpoint nghe/AV exact native và kiểm điểm nối; chỉ sau đó chọn range/endpoint. Không generation mới, không chi hoặc mở dự phòng từ kết quả maker này.
