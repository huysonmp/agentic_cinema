# REC267 — C05 T02 actual: phản biện độc lập

Ngày: 12-10-2026. RUN_ID: REC267-C05-T02-INDEPENDENT. Trạng thái: VISUAL_NO_MAJOR_OBSERVED / AUDIO_AV_HOLD / NOT_SELECTED / C06_HOLD.

## Target, authority và phạm vi thực chạy

Target duy nhất: `05_native/EP01_720_C05_T02_NATIVE.mp4`, SHA-256 `3df61217ddf6d09792fe1e5991c3668d115ce5648c00802f196d87abe57d23df`. Reviewer tự tính lại hash native và START, khớp hồ sơ. START thật: `02_refs/C05_START_from_C04_T02_selected_F143_263.png`, SHA-256 `2e4f4a5fbf0d5f310010762d26d0c74f08bfb2da3eab792f69a3be568b94c2db`.

Đã đọc đầy đủ `217_recovery-tier4-runtime-gates-and-questions.md`, `266_resume_C05_T02.md`, scoped238, rough35/264, request265, registry265, prompt cuối T02/264, hồ sơ264 và265. Đây là bounded local critic run theo 217; không đọc báo cáo maker hoặc tổng hợp root REC267. Không browser, API, credit, git, cài công cụ, script mới hoặc chỉnh media trong run này.

Đã xem trực tiếp tất cả `action_all/action_all_01.jpg` đến `_12.jpg`: đủ F0–95, tám khung mỗi board, không bỏ board. Đã đọc manifest đối soát target hash và số khung. Xem thêm PNG nguyên khung `all_native_frames/00001.png` (F0), `00049.png` (F48) và `00096.png` (F95), cùng START nguyên khung. Evidence root: `C:/Users/PC/Downloads/du_an_nem_bui/265_C05/C05_T02_QC_267/`.

Capability: ALL_FRAME_STILLS_NOT_AV. Không phát/xem chuyển động liên tục, không nghe nguồn. Native evidence đã có báo cáo 720×1280, 24 fps, 96 khung, hình4s, AAC stereo48kHz, decode đủ; reviewer đọc kết quả đó, không tự chạy probe/decode lại. Đây không phải FULL_AV, ACTUAL_LISTENING hoặc lip-sync certificate. Không dùng ASR làm heard_text.

## Findings actual theo scope

Timecode dưới đây tính F/24, zero-based; cuối khung F95 ở 3,958333s, duration hình4s.

| ID / severity | Expected và observed | Frame/time evidence | Kết luận |
|---|---|---|---|
| CONT01 / MAJOR cũ được kiểm lại | Hai bát riêng rỗng còn tách biệt. T02 hiện rõ bát Khoai bên trái và bát Đào bên phải đĩa chính, vành/lòng rỗng đọc được, không bị cốc thay thế. | F0–95 / 0–3,958333s, đủ12 board; xác nhận nguyên khung F0/48/95 và START. | Không thấy lỗi mất bát T01 lặp trên target này. Không cần trim để che lỗi. |
| CONT02 / MAJOR cũ được kiểm lại | Đào giữ cốc trong tay ngoài phải, nâng dưới mặt, trên bàn và bát của mình. T02 giữ pose nâng suốt, không đặt cốc xuống/sip/đổi sang vị trí bát. | F0–95; nguyên khung F0/48/95 so START. | Không thấy reset cốc xuống bàn T01 lặp. Sai biệt nhỏ về hình cốc/độ cao vài pixel ở entry không làm đổi trạng thái nâng, chưa phải MAJOR. |
| ACTION01 / không thấy MAJOR | Cùng một miếng A dạng lát dài màu be được kẹp ở đôi đũa trong tay ngoài trái của Khoai, phía ngực dưới/trên bát mình, xa miệng. Không thấy miếng thứ hai, biến mất, ăn, trao, rơi hoặc thả. Đôi đũa Đào vẫn nằm riêng phía phải bàn; tay trong hai người vẫn trên bàn. | F0–95, crops tay/món trên12 board, PNG F0/48/95. | Chuỗi vật thể/hành động giữ được trong các ảnh đã xem. Không đồng nhất điều này với chứng minh vật lý chuyển động liên tục. |
| PERF01 / quan sát đạt scope hình | Cả hai mặt, mắt và miệng luôn đọc được, không cắt/zoom/che mặt. Đào đã nhìn Khoai ở entry và không lặp quay lưng/quay đầu phát hiện. Đào có chuỗi miệng mở/khép khi nhìn Khoai; Khoai môi khép, không có chuỗi khẩu hình trả lời rõ. | Entry F0–7 /0–0,291667s; Đào bắt đầu thay đổi miệng F8–17 /0,333333–0,708333s, tiếp F20–44 /0,833333–1,833333s; môi Đào trở về khép khoảng F45 trở đi. | Mouth attribution trong ảnh phù hợp Đào nói/Khoai nghe. Không xác nhận câu nói, một người nói thực trong audio, hoặc sync. |
| PERF02 / MINOR theo dõi điểm nối và nhịp | START Khoai còn nhìn xuống miếng A; F0 T02 đã nhìn Đào. Đây là một eye shift giữa hai khung ở boundary, không đổi head pose hay prop state. Phản ứng sau thoại chủ yếu blink F48–53 rồi mắt mở hơn F56–63; không có cử động tay lớn/ăn/chữa cháy sớm. | START→F0; F48–63 /2–2,625s; F64–95 /2,666667–3,958333s gần như giữ pose. | Không phải blocker hình quan sát được. Cần xem nối thực để đánh giá eye shift và nhịp; phản ứng khá tiết chế, chưa gọi đã đạt toàn beat bằng ảnh. |
| FOOD01 / không thấy MAJOR | Đĩa nem nguội, rau phía trước trái và hai bát chấm ở hai phía còn đọc được. Không thấy hơi/khói, thay sang món nóng hoặc prop mới trong phần bàn ăn. | F0–95, crops bàn ăn và PNG F0/48/95. | Không thấy vấn đề food/continuity lớn trong scope hình. Không xác nhận mùi/vị hoặc chi tiết món ngoài khả năng ảnh. |

Đào không có một confirming glance xuống miếng A rõ ràng và tách biệt ở các ảnh; phần mắt nhìn/khép có thể là diễn trong câu. Đây là giới hạn diễn đọc từ stills, không đủ để coi mất nhiệm vụ câu chuyện khi nàng đã bắt gặp Khoai từ C04. Nếu owner cần beat nhìn miếng A thật rõ, đánh giá cùng điểm nối/AV trước quyết định, không tự xin sinh thêm.

## Kết luận và range chỉ là đề xuất có điều kiện

Không quan sát cùng MAJOR mất bát hoặc reset cốc ở T02. Vì vậy điều kiện STOP_FOR_DIAGNOSIS do hai lỗi đó lặp hai lần chưa được kích hoạt bởi evidence target này. C05 T02 có khả năng dùng về hình, nhưng report này không chọn take/range, không đóng tiếng/AV, không mở C06 và không duyệt rough/final.

Giữ F0–95 làm ứng viên kiểm owner nguồn nguyên4s. Đề xuất hình có điều kiện: F0–63 (64 khung /2,666667s) chứa entry, chuỗi khẩu hình quan sát và một beat phản ứng; tail F64–95 có thể là vùng cân nhắc cắt nếu owner nghe/xem xác nhận toàn câu và ngữ điệu đã kết thúc, giữ khoảng thở và sync, rồi kiểm boundary sang C06. Đây không là EDL đã chọn. Nếu audio còn lời/nhịp cần giữ sau F63 thì range này không hợp lệ. Không lấy mouth-close ước lượng thay thời điểm kết thúc tiếng.

Scope tiếng “Chờ em quay lưng nữa à?”, đúng Đào/D06, không giọng Khoai/extra words/music, nhấn “nữa à”, ngữ điệu và lip sync: HOLD / NOT_PERFORMED. C04→C05 join: NOT_BUILT_BY_REVIEWER / NOT_CONTINUOUSLY_VIEWED. Owner checkpoint phải gắn đúng native/hash trên; approval T01 hoặc preset không chuyển sang target này. Reviewer không cung cấp heard_text hoặc audio PASS.

Root cần đọc toàn báo cáo, đối soát báo cáo maker độc lập và bằng chứng nhận nguồn; sau checkpoint tiếng/AV và kiểm nối mới chốt range/khả năng tiếp C06 trong scoped authority. Không tự tạo T03 hoặc thay shot để đóng lỗi chưa quan sát.
