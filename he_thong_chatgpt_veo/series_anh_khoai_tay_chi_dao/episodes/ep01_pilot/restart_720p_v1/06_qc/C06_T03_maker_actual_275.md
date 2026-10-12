# REC275 — Kiểm bản gốc C06 T03: maker DIR / DOP / ACT / EDIT / CONT

Ngày 12-10-2026. RUN_ID `REC275_C06_T03_MAKER_ACTUAL`. **MAJOR_STORY_ENDPOINT_REWORK / STOP / C06_NOT_SELECTED / C07_HOLD.** Bản này đưa A vào bát Đào sớm, không giữ A còn kẹp và có khoảng hở tới cuối như nhiệm vụ C06. Không tự T04 hoặc đổi coverage. Đây là maker actual, không phải phản biện độc lập.

## Target và phạm vi thực kiểm

- Đã đọc đầy đủ exact final `04_requests/C06_T03_prompt_275.txt`, hash đã tự kiểm ở preflight275 **`42b412ec3bb6e7d3dd4b86fd980ad5a9c0a2a494dae899ae2f9bf077028e35d9`**; đọc đầy đủ `04_requests/C06_T03_run_275.json` hiện `NATIVE_RECEIVED_ACTUAL_REVIEW_PENDING`. Owner275 đã đọc ở preflight trong cùng chuỗi: cho phép một T03 có điều kiện, bỏ cue một khóe; **không yêu cầu late unilateral lift nữa**.
- Native `05_native/EP01_720_C06_T03_NATIVE.mp4`; **tự hash** `36f04086a2e3d6d3d688f64ca743909184955bf1a714094def5dd8cd3747ff7c`, khớp run và evidence. Run ghi một submit Ingredients/Omni 1.1 Flash/720p/9:16/4s/x1/Agent tắt/audio bật; K20 giữ nguyên; debit7, spent187/500, retake còn66. Số dư tăng có sẵn133 được root để riêng, không thêm quyền dự án. Maker chỉ đọc, không browser hoặc chi.
- Đọc đầy đủ `C:/Users/PC/Downloads/du_an_nem_bui/275_C06_T03/native_qc/native_evidence.json` và `action_all/manifest.json`: H.264720×1280/24fps/96frames/4s hình, AAC48k stereo/4,010s container; full decode success theo evidence. Không tự probe/decode lại.
- Trực tiếp xem **đủ12 bảng ảnh / ALL96 khung F0–95**. Xem thêm ảnh nguyên khung F0/F17/F33/F40/F64/F67/F70/F73/F80/F95 và exact START C05 F65. Khung xem nằm trong `all_native_frames`, file index=F+1. Manifest12 bảng có target hash trùng native.
- Capability **ALL_FRAME_STILLS_NOT_AV**. Chưa nghe, chưa xem chuyển động liên tục hoặc full AV; nguyên văn N06/K20/nhịp/sync và vị trí âm cuối vẫn UNKNOWN/NOT_CERTIFIED. Không đọc/dùng ASR, không đọc critic275, không script/tool/media edit/API/credit/git.
- T02 audio đã được owner275 duyệt **chỉ source T02**; không chuyển sang T03. Maker không nhận mình đã nghe T02 hoặc T03. F zero-based; Fn=n/24s; range half-open.

## Phát hiện actual

| ID / mức độ | Khung / giây | Yêu cầu → quan sát / hệ quả |
|---|---|---|
| END01 / **MAJOR — A vào bát sớm, thiếu hold endpoint** | Đường hạ tới rim khoảng F67–73 / 2,792–3,042; A thấp vào vùng lòng bát rõ F80–95 / 3,333–3,958 | Final giữ một A còn kẹp trên phía Khoai của bát Đào, có khoảng hở giữa A/tips và rim, không đưa A vào bát hoặc thả đến hết. Actual sau khi đưa sang, đầu đũa tiếp tục hạ; A chồng vành rồi xuống lòng bát. Full F80 A thấp trong bowl; F95 miếng A nằm trong bowl, tips ở trên/vùng vành, không còn trạng thái còn kẹp và cách vành. Không cần chứng minh chính xác frame release để kết luận trạng thái cuối sai: **A đã vào lòng bát**, thiếu nhịp dừng giữ ngoài bát. Không lấy full C06 làm C07 START vì bỏ qua Đào chuẩn bị bát và C08 thả. |
| CLEAR01 / **MAJOR endpoint, cùng END01** | Khoảng F70–95 / 2,917–3,958 | Có vùng đang tiến tới bát với khoảng hở ở F64; sau đó gap đóng khi A/tips hạ qua rim, không dừng giữ ở mức cao như T02. Chồng hình ở F70 không tự chứng minh contact vật lý, nhưng F80/F95 A trong bát xác nhận endpoint không đạt, không chỉ là projection chưa rõ. Không đếm thêm một lỗi độc lập để cộng mức. |
| ENTRY01 / caught entry phù hợp theo ảnh | F0–8 / 0–0,333 | Môi cụp, mắt Khoai hướng Đào, mày còn căng, A ở phía mình, cốc nâng và hai bát rỗng. Không cười vui ngay entry hoặc diễn phát hiện lại. Chưa kiểm encoded join/AV nên không seamless PASS. |
| ACT01 / **HOLD — đánh toàn diễn theo275, không máy móc lỗi hai khóe** | Hình nói khoảng F9–39 / 0,375–1,625; rõ F16–19 / 0,667–0,792 và F32–37 / 1,333–1,542; mouth khép F40+ | Có miệng mở ngang/hai khóe nâng/răng hiển thị. F17 khá giống cười nén, nhưng phần trong mày nâng/căng và mắt chưa thành vẻ vui mời. F33 mở miệng trong vùng nói, không lấy răng đơn độc làm grin. Sau F40 khóe mềm nhẹ, má không nâng lớn, mày vẫn chút ngượng và gaze theo Đào/A. Theo hướng275, **răng do articulation được phép, không đòi một khóe muộn**; bằng stills không đủ gọi vẻ vui mời rõ thành MAJOR chỉ dựa symmetry. Không ACT PASS: sắc thái cười có còn quá vui cần owner xem AV/nhịp. END01 đã đủ chặn bất kể kết quả ACT. |
| ACTION01 / redirect có; âm cuối/thứ tự lời UNKNOWN | Tay bắt đầu khoảng F40–43 / 1,667–1,792; đi F44–67 / 1,833–2,792; hạ tail F68+ | Một A trên own pair và tay ngoài trái, đi trước ngực/trên bàn từ phía mình sang bát Đào. Không lấy miếng thứ hai, đổi tay/pair, nhân đôi hoặc ăn được thấy. Hand move gần lúc hình miệng khép sau group nói. Chưa nghe nên không chứng minh sau âm “mà”, đúng voice hoặc sync. Sau đó hành động vượt nhiệm vụ, đưa A vào bát. |
| GLASS01 / lỗi T01 không thấy lặp | ALL F0–95 | Cốc vẫn nâng trong tay ngoài phải Đào, đáy trên bàn, không vào/che lòng bát như T01. Pose variation nhỏ không thành hành động hạ cốc. |
| BOWL01 / không nhận gesture sớm; **không còn rỗng cuối vì A** | Bát/tay giữ toàn nguồn; A trong bát rõ F80–95 | Hai bát đứng trên bàn, inner hand hai người nghỉ, Đào own pair nghỉ ngoài phải. Không thấy bát bị cốc thay, nhấc bát hoặc receiving gesture. Nhưng bát Đào bị A vào sớm cuối; không dùng glass fix để bù lỗi này. |
| MOUTH01 / vai hình miệng phù hợp; tiếng HOLD | Khoai F9–39; Đào ALL F0–95 | Chỉ Khoai có nhóm khẩu hình như đang nói. Đào môi kín/chớp mắt và nhìn A. Không certify single male audio/full N06/no extras/K20/lip sync. |
| DOP/FOOD/TABLE01 / không thấy MAJOR khác | ALL F0–95 | Hai mặt/A/tay/bát/cốc đọc được; khung, ánh sáng ấm, camera giữ. Rau trước trái, hai chấm, đĩa nem nguội/no smoke và watermark giữ. Không cut/zoom/props mới/identity redesign rõ. |

## Beat thực và disposition EDIT ban đầu

Theo hình: F0–8 caught stillness → F9–39 khẩu hình nam → F40+ môi khép/tay chuyển → khoảng F60–67 A tới vùng bát → F68+ tiếp tục hạ → A vào lòng bát F80–95. Không thấy ăn/miếng mới; lỗi là **model hoàn tất việc đưa món vào bát**, vượt “chỉ đưa mời, còn kẹp” của C06.

Ban đầu chưa đề nghị selected range. Vùng trước F68 có thể phục vụ chẩn đoán, nhưng chưa thấy plateau ổn định chứng minh dừng giữ đủ; tiếng/âm cuối/AV cũng chưa kiểm. Không tự cắt sớm để gọi nhiệm vụ C06 đã xong rồi ép C07 vào trạng thái khác. Phần rà bổ sung dưới đây chỉ mở một phương án đổi ranh giới điểm cắt để owner xem xét.

T03 full4s nếu chọn sẽ đưa phim qua C06 tới30,333333s, còn4,666667s tới35 cho C07–09. Vì endpoint chưa đạt nên không đưa số đó thành readiness hoặc tự bỏ C07/C08 chỉ vì actual đã sớm thả. Không tăng tốc voice/cắt lời/đổi canon hoặc coverage để cứu timing.

## Rà bổ sung prefix trước F72 — đề xuất cut-on-motion có điều kiện

Theo yêu cầu root, đã xem thêm nguyên khung **F56/F59/F62/F63/F65/F67/F70**, đối chiếu với các bảng ảnh đã kiểm. Đây không phải media mới hoặc sửa native.

Ở F56–63, A vẫn kẹp giữa tips, cốc nâng, bát Đào rỗng và hai môi đã khép trong hình. A đã sang đúng vùng nhận phía Khoai của bát Đào; F62/F63 còn khoảng hở nhỏ đọc được giữa A/tips và vành. Tuy vậy, A/tay vẫn hạ từng khung F56→59→62→63, tiếp tục hạ qua F65/F67/F70. **Không thấy đoạn dừng giữ ổn định để gọi “stop and hold” đạt.** F65–70 khoảng hở thu hẹp và projection sát vành hơn, nên không ưu tiên cắt ở F67 chỉ để kéo dài range.

Để có biên an toàn khoảng hở lớn hơn, **ưu tiên preview bảo thủ `[0,57)` = F0–56 / 57 khung / 2,375s**, endpoint F56 ở2,333333s. Ở F56, A còn kẹp và cách vành rõ hơn F63, nhưng tay vẫn đang chuyển; không nhận nhiệm vụ dừng giữ đã đạt. Phạm vi muộn hơn **`[0,64)` = F0–63 / 64 khung / 2,666667s**, endpoint F63 ở2,625s, chỉ là lựa chọn phụ để đối chiếu nếu actual AV/điểm nối cần thêm nhịp và khoảng hở được chấp nhận.

Cả hai đều là **CUT_ON_MOTION_CONDITIONAL — CHƯA SELECT**: cắt khi đường đưa A còn đang tiến tới bát, không phải nghiệm thu endpoint dừng giữ cũ. Chủ trương chỉ dùng được nếu:

1. Owner chấp thuận ranh giới mới: C06 kết trên chuyển động còn kẹp, C07 nối tiếp từ đó; không cần nhịp stop-and-hold riêng, vẫn không thả trước Đào chuẩn bị bát.
2. Human/actual AV trên target mới xác nhận N06 đủ âm cuối, đúng K20, sắc thái chữa cháy chấp nhận được, sync và nhịp không bị cắt. Hình miệng khép từ F40 không thay xác nhận đủ lời.
3. Điểm nối mới kiểm được tốc độ/hướng tay, A/tips/recipient/glass/bowl/eye-line; không magically reset tay hoặc nhảy vào A đã nằm trong bát. C07 phải kế thừa một endpoint đang chuyển động, không giả ghi source “đã dừng”.
4. Root và critic cùng đối soát scope/range/hash, giữ disclosure full native có END01; owner chọn đúng bản encode/range. Không kéo approval source tiếng T02 sang target này.

Range57 nếu được chọn sẽ đưa qua C06 thành689 khung =28,708333s, còn151 khung =6,291667s tới35 cho C07–09. Range64 sẽ đưa qua C06 thành696 khung =29s, còn144 khung =6s. Số này giúp xét timing, **không bảo đảm** ba cảnh sau đủ nhiệm vụ trong thời gian còn lại, cũng không cấp quyền coverage hoặc generation mới. Đây chỉ là phương án tận dụng nguồn trước lỗi; không chuyển full native thành PASS, không đóng END01.

## Nguyên nhân và giới hạn kết luận

Lỗi END01 ở native trước cut/encode. Final275 đã cấm thả/A trong bát, nên không coi chỉ thiếu một câu cấm; input trên giấy không thắng output thật. Quan sát cho thấy model tiếp tục đường đưa món và hạ đũa thay vì dừng trạng thái đưa mời. **Chưa chứng minh vì sao**: độ khó giữ động tác, ý nghĩa xã hội của hành động, route/model/mật độ yêu cầu đều là giả thuyết. Không gán nguyên nhân duy nhất hoặc mặc định tách coverage sẽ chữa.

Bỏ cue khóe môi không được dùng làm bằng chứng chắc chắn diễn đã sửa hoặc gây lỗi endpoint: mới một output với nhiều variation. ACT phải xét hướng275 mới, không quay lại tiêu chí late unilateral lift đã bỏ.

## Kết luận và cổng tiếp

**Full C06 T03 NOT_SELECTED / MAJOR_STORY_ENDPOINT_REWORK / STOP.** Giữ cốc và entry đúng; tổng diễn275 cần human AV/ACT decision, không nhận lỗi chỉ vì “không một khóe”. MAJOR rõ là A vào lòng bát/không giữ end gap, vượt C06 và dependency C07–08.

Có phương án **prefix57 cut-on-motion bảo thủ, hoặc prefix64 muộn hơn, đều cần owner thay ranh giới điểm cắt**; không selected range hoặc approval source. Theo approval275/run275: **không automatic T04, không fallback coverage hoặc C07**. Root đọc actual độc lập, đối soát finding/range hiện hành rồi trình quyết định cụ thể; không chi thêm dưới quyền một T03 đã dùng. Tiếng T03 vẫn chưa nghe/duyệt; T02 audio approval không thay.
