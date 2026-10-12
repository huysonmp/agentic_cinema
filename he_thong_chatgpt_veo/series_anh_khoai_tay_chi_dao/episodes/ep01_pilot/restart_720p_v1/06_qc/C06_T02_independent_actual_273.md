# REC273 — C06 T02: phản biện độc lập trên bản gốc

Ngày 12-10-2026. RUN_ID: REC273-C06-T02-INDEPENDENT-ACTUAL.

Kết luận: **ACTING_MAJOR_REPEATED / STOP_FOR_DIAGNOSIS / C06_NOT_SELECTED / AUDIO_AV_HOLD / C07_HOLD**. Cốc và bát đã giữ đúng trạng thái trong toàn bộ ảnh của bản gốc. Không dùng kết quả đó để bù lỗi diễn xuất theo hướng A mà owner đã chốt.

## Target và bằng chứng đã trực tiếp xem

Bản gốc: `05_native/EP01_720_C06_T02_NATIVE.mp4`. Reviewer tự tính lại SHA-256 **`a2422a7e827ef80be3b95ff07335bd66e8ec1207d14af64a3763098e90c91b6a`**, khớp manifest và evidence.

Đã đọc đầy đủ prompt cuối `04_requests/C06_T02_prompt_273.txt`, với hash đã xác minh ở preflight: `cbe71e5a5a2085a2d6f27723a230dd5e6707659aa08ae436b3787782348db5b4`. Đã đọc toàn bộ `04_requests/C06_T02_run_273.json`. Khi bắt đầu kiểm, registry còn ghi `SUBMITTED_AWAITING_OUTPUT` và `native: null`. Đây là snapshot cũ tại thời điểm đọc, không phải hiện trạng: root đã cập nhật run thành **NATIVE_RECEIVED_ACTUAL_REVIEW_PENDING** và gắn bản gốc đúng hash nêu trên.

Đã đọc đầy đủ authority217, scoped238, acting-A273, rejection272, C05 acceptance269 và actual independent271 trong cùng chuỗi nhiệm vụ. Không đọc báo cáo maker actual273.

Thư mục bằng chứng: `C:/Users/PC/Downloads/du_an_nem_bui/273_C06_T02/native_qc/`. Đã đọc đầy đủ `native_evidence.json` và `action_all/manifest.json`. Đã trực tiếp xem **tất cả 12 board action_all_01–12.jpg, đủ F0–95**, tám khung gốc mỗi board. Đã xem thêm PNG nguyên khung F0, F24, F42, F48, F72, F95 (tên file = F+1), cùng ảnh START chính xác từ C05 native F65. Hash START đã tự kiểm: `f091e35fc7c779591c918c47ba34752a8a2c3b30de507cd99dc0e76143e83196`.

Phạm vi năng lực: **ALL_FRAME_STILLS_NOT_AV**. Không nghe tiếng hoặc phát hình–tiếng liên tục. Bằng chứng kỹ thuật đã đọc: H264 720×1280, 24 fps, 96 khung / 4 giây, AAC stereo 48 kHz, giải mã thành công và nguồn không đổi. Reviewer không chạy lại probe hoặc decode. Không dùng metadata, preset hoặc ASR làm bằng chứng đã nghe, đúng K20, đúng một người nói trong tiếng hay khẩu hình đồng bộ. Không thao tác browser/API/credit/git, không thêm công cụ/script và không chỉnh media.

## Findings thực tế

Chỉ số F tính từ 0; thời gian = F÷24.

| ID / mức độ | Mong đợi và quan sát | Bằng chứng và xử lý |
|---|---|---|
| ENTRY01 — không thấy MAJOR reset | START có nét bị bắt gặp, môi cụp và mắt nhìn Đào. F0 giữ gần nguyên trạng thái đó, không cười sẵn như T01 F0. | Exact START → full F0, board01–02. Entry cải thiện; chưa có bản nối C05→C06 được encode nên không chứng nhận điểm nối đạt. |
| ACT01 — **MAJOR, hướng diễn vẫn chưa đạt và đã lặp** | Owner A yêu cầu điềm tĩnh, hơi ngượng; nét cười rất nhẹ chỉ ở cuối câu. Bản mới giữ nét ngượng trước khi nói và nhấc phần trong chân mày, nhưng trong nhiều nhóm khẩu hình, cả hai khóe môi cùng nâng, má/môi cười rõ và có răng. Sau đó giữ nụ cười hai bên. | Board03–06: F22–27 / 0,917–1,125 giây; F34–35 / 1,417–1,458 giây; F40–46 / 1,667–1,917 giây. Full F24/F42. F48–95 vẫn cười khép môi. MAJOR không chỉ vì thấy răng: vấn đề là tổ hợp khóe môi, má và nụ cười xuất hiện nhiều lần trong câu, thay vì nét nhếch kín ở cuối. Chân mày có nét ngượng nhưng chưa đủ đóng phản hồi272. **REWORK / STOP_FOR_DIAGNOSIS**; không tự giảm thành MINOR. |
| MOUTH01 — attribution hình phù hợp, chưa đạt AV | Khoai có chuỗi khẩu hình khoảng F16–46. Đào khép môi nghe qua F0–95; không thấy nhóm khẩu hình nói. | Board03–06 và toàn bộ 12 board; full F24/F42. Không xác nhận N06 đủ/đúng, giọng K20 hoặc sync. Chưa nghe nên không gán âm cuối “mà” vào một frame. |
| GLASS01 — **không thấy lỗi cốc MAJOR lặp lại** | Cốc giữ nâng trong tay ngoài của Đào từ đầu đến cuối. Không hạ, đặt xuống hoặc uống; đáy cốc còn lơ lửng, tách riêng khỏi bát. | Toàn bộ 96 khung; full F0/F48/F72/F95. Có thể đóng finding hình trên T02 trong phạm vi ALL_FRAME_STILLS, không chứng nhận chuyển động vật lý hoặc AV liên tục. Lỗi cốc ở đuôi T01 vẫn giữ trong lịch sử. |
| BOWL01 — không thấy MAJOR | Bát Đào giữ trên bàn, rỗng; vành và lòng bát đọc được suốt cảnh. Cốc không vào hoặc thay bát. Bát Khoai vẫn rỗng bên trái. | Đủ 12 board; full F0/F72/F95. Không nhận Đào đã làm C07: cô chưa nhấc bát, tay trong vẫn nghỉ trên bàn. |
| ACTION01 — đường chuyển SAME A có thực trên ảnh | Một miếng A vẫn kẹp tại tip đôi đũa riêng, trong tay ngoài bên trái của Khoai. Sau chuỗi khẩu hình, anh đưa sang phải khoảng F47–63, tới vùng phía Khoai của bát Đào rồi giữ. Không thấy ăn, thả, rơi, nhân miếng, đổi tay hoặc đổi đũa. | Board06–09; full F48/F72/F95. A còn kẹp đến F95, chưa được nhận. Không dùng ảnh tĩnh để chứng minh mọi chuyển động vật lý giữa khung hoặc sync với âm cuối. |
| ENDPOINT01 — khoảng hở rõ, ý nghĩa nhịp chờ cần kiểm AV | Miếng A và tip cao hơn vành bát, ở phía Khoai / phía tay trong của Đào; khoảng hở chiều dọc rõ, không chồng vành như T01 F75. Endpoint khá cao và bên trái bát, chưa nằm trong bát. Có thể đọc là đưa mời, nhưng nhịp chờ thực cần kiểm AV. | Full F72/F95, board09–12. Không thấy chạm hoặc thả. Không tự kéo A xuống sát bát hoặc tạo ref C07 dù props endpoint có thể dùng được; gate diễn xuất vẫn chặn. |
| CONT/FOOD01 — không thấy MAJOR khác | Hai mặt, tạo hình, trang phục và bố cục được giữ. Nem Bùi nguội, không hơi; rau trước trái và hai chấm còn đúng vị trí. Đũa riêng của Đào nghỉ bên phải, hai tay trong ở bàn. Không thêm hành động ở đuôi. | Đủ 96 khung; full F0/F95. Bố cục và ánh sáng ổn định trên ảnh tĩnh. Finding món ăn không thay đánh giá diễn xuất. |

## Vì sao phải STOP dù một lỗi đã được sửa

Owner bác T01 ở cả cốc và mặt. Quyết định A xác định vấn đề mặt là diễn quá vui, không phải thiết kế lại tạo hình. Prompt cuối T02 đã ghi cụ thể cách nói chữa cháy tiết chế và nét cười kín cuối câu. T02 cải thiện entry, cốc, bát và khoảng hở, nhưng vẫn cười khá rõ trong nhịp nói và sau đó.

Đây là **cùng mục tiêu diễn chưa đạt qua hai take C06**, không phải một lỗi kỹ thuật mới hoặc một khẩu hình tình cờ. Scoped238 và run273 yêu cầu STOP khi MAJOR lặp lại. Vì vậy không tự chạy T03, không dùng trim bỏ phần cười nếu phải mất N06.

Nhận định diễn từ ảnh có giới hạn: reviewer chưa nghe giọng và độ nhấn để đánh giá toàn bộ sắc thái. Root cần đối chiếu video thực và có thể trình owner đúng phạm vi. Nếu owner chủ động chấp nhận mức diễn nhẹ hơn, đó là quyết định mới, không phải reviewer đã thấy A đạt. Báo cáo không tuyên bố mọi nụ cười sau chữa cháy đều sai; finding cụ thể là cười rõ trong câu, trước cue kết, với cả hai khóe môi thay vì chỉ nhếch một khóe rất nhẹ ở cuối.

## Tầng phát sinh và hướng xử lý

Root closeout: sau khi đọc báo cáo và đối chiếu đủ 96 ảnh, run đã được cập nhật thành `STOP_FOR_DIAGNOSIS_ACTING_MAJOR_REPEATED`. Trạng thái receipt ở phần target là bước trước khi chốt actual, không phải trạng thái cuối.

- Finding mặt đã xuất hiện trong native T02 trước khi ghép; không đổ lỗi cho encode hoặc cut. START không cười, T02 giữ entry tốt, nhưng diễn khi nói phát triển thành nụ cười. Prompt không thiếu chỉ đạo cấm. Chưa chứng minh nguyên nhân riêng lẻ là mô hình, ngữ điệu voice, từ “cho em”, mật độ prompt hay route.
- Việc rút 6→4 giây và neo end hold trùng với kết quả cốc được bảo toàn. Một lượt không thiết lập quan hệ nhân quả; không ghi “4 giây luôn chặn hạ cốc”.
- Giữ T01/T02 và đúng ref; dừng chi. Chẩn đoán bằng đối chiếu T01/T02/START và nhịp voice hiện có. Không sinh thêm, đổi voice/route hoặc thêm công cụ dưới danh nghĩa QC.
- Nếu có quyết định sửa mới, phải khóa can thiệp và các scope giữ nguyên, rồi review lại prompt cuối hiện hành; không chỉ thêm nhiều câu cấm. Nếu owner đổi mức diễn chấp nhận được, phải lưu approval đúng artifact/scope và vẫn giữ gate audio, AV, điểm nối.

**C06 NOT_SELECTED; C07 HOLD; AUDIO/K20/LIP_SYNC NOT_CERTIFIED.** Không chọn candidate prefix nào trong báo cáo này. Nếu dùng toàn bộ T02 4 giây, tổng qua C06 sẽ là 30,333 giây, còn 4,667 giây đến trần 35 giây cho C07–09. Phải đo timing thực phần sau, không hứa đủ trước khi chọn.

Run ghi chi 7 credit, tổng 180/500, còn 320; reserve 110 vẫn đóng. Critic đọc ledger, không tự đối soát account live.
