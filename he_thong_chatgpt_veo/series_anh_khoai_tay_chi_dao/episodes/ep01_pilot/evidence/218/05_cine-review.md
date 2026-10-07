# REC218-CINE-R1 — Review hình ảnh độc lập

## Ghi nhận cold — lưu trước khi đọc script, approval và board

Đã đọc đầy đủ contract02 và09. Cold chỉ xem reference và tám JPEG, trước episode178/214/217 và board216; không suy tiếng/chuyển động/lip-sync.

- **T2-CODEX-OPEN_v0.7.png:** khung dọc, khoai trái, đào phải; mặt/tay rõ. Hai bát, món dưới giữa, rau trái/cốc phải. Mặt bàn rộng; nền phố sâu, đèn cam/điểm sáng trắng, người/xe mờ. Tông ấm, mắt có phản sáng, mặt tách nền. Mắt hướng xuống bàn, miệng cười nhẹ.
- **frame-0000:** hai người và món cùng khung; khoai nhìn gần hướng trước, miệng hé nhỏ; đào hướng mắt xuống trái. Đĩa món ở trung tâm thấp, bát và đôi tay rõ; cốc phải bị sát/cắt mép. Nền trời xanh xám và đèn ấm; dấu hình thoi sáng ở bàn phía dưới phải.
- **frame-0071:** bố cục hai người tương tự; khoai và đào hướng mắt về phía nhau, miệng khép/cười. Mặt hai người nổi rõ hơn món ở vùng dưới. Lá trên đầu đào sát mép phải; cốc vẫn chỉ có phần trong khung.
- **frame-0072:** cận khoai, mặt chiếm phần lớn chiều cao; mắt hướng trước/hơi xuống, miệng khép. Hai bàn tay và bát còn rõ, chỉ thấy một phần đũa; đào và đĩa món không thấy. Nền đèn mờ ấm, đỉnh đầu còn khoảng trống.
- **frame-0163:** khung chủ yếu khoai với miệng mở, mắt hướng phải; chỉ một lát mặt/thân đào ở mép phải. Bát, tay khoai rõ; đĩa món chỉ lộ phần mép dưới. Nền đèn sáng cam, mặt đọc được; không xác định người nói từ trạng thái miệng này.
- **frame-0164:** cận đĩa món, không mặt/người/tay; đĩa gần đầy khung ngang, lá xanh trên đỉnh món. Rau trái, bát trống phía sau, chén ớt và đũa phía trên phải; một bát chứa chất lỏng bị cắt mép phải. Món/bàn ấm, hậu cảnh mờ; dấu hình thoi sáng ở góc dưới phải.
- **frame-0200:** cùng loại khung món như0164; lá trên đỉnh, bát/đũa/rau giữ vị trí nhìn tương tự trong hai mẫu. Không có mặt/tay; không suy tính ổn định của đoạn giữa hai ảnh.
- **frame-0201:** trở lại khung hai người, mắt hướng về phía nhau, miệng khép/cười. Hai mặt rõ cùng bát và món ở phía dưới; cốc sát mép phải, trời xanh xám/đèn ấm.
- **frame-0239:** hai người cùng khung; khoai hướng mắt phải, đào hướng mắt xuống trái; tay đặt vùng cạnh bát. Đĩa món rõ ở trung tâm thấp. Bố cục/tông sáng gần0201; hai mẫu không chứng minh diễn biến liên tục.

## Input, capability và đối chiếu sau cold

**Run:** REC218-CINE-R1, PAPER/SAMPLED_FRAMES theo owner217 A/A/A. Target là `C:/Users/PC/Downloads/du_an_nem_bui/200_n02_replacement/N02_NATIVE.mp4`; SHA-256 kiểm read-only khớp `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153`. 360×640, 24fps là thông tin dispatch, chưa probe lại vì `ffprobe` không có trên PATH. Time dưới tính từ số frame/24, không là timecode audio đã nghe.

Sau lưu cold, đọc trọn episode178,214,217; xem ba board216 `speech_anchors.png`, `face_to_dish_boundary.png`, `dish_to_faces_boundary.png`. Tên “speech” không chứng minh tiếng. Không đọc211,215,216.md, maker218/reviewer khác. Thiếu recovery master, map lời đã kiểm nghe, motion qua cut và chữ render.

| Khả năng thực hiện | Evidence / giới hạn |
|---|---|
| Ảnh tĩnh, composition, ánh sáng nhìn thấy | Reference, tám JPEG và ba board; MET trong mẫu |
| Đối chiếu yêu cầu | PAPER:178 khóa lời,214 khóa nhiệm vụ hình,217 khóa gate |
| Danh tính target | Hash khớp; JPEG/board do dispatch cấp, chưa tự tái trích từ bytes |
| Nghe, continuous visual, sync | UNKNOWN; không thực nghe/xem liên tục |
| Full scene, timing30s, action A/B, finishing | UNKNOWN; chưa có recovery master |

214 yêu cầu R02 lấy mặt Khoai làm điểm tựa, nhìn từ món lên Đào; insert phải có nhiệm vụ. Mẫu cận có mặt, bát/tay rõ. f71→72 đổi từ hai người sang cận; f163→164 từ mặt sang món; f200→201 từ món về hai người. Chưa biết động cơ cắt/âm tiết/nhịp ký ức. Tông ấm, mặt/mắt rõ trong mẫu; chưa có căn cứ đổi ánh sáng toàn cảnh.

## Coverage và findings

| Tiêu chí | Trạng thái và lý do |
|---|---|
| Mặt/mắt Khoai, hierarchy R02 | MET tại mẫu cận; **gap xác nhận** ở mẫu món; phân bố theo lời UNKNOWN |
| Món trong quan hệ bữa ăn | MET ở khung chung; cận món rõ nhưng mất quan hệ mắt/người |
| Gaze người kể–người nghe | Có hướng mắt về nhau ở f71,201; toàn hành trình và đúng beat UNKNOWN |
| Ánh sáng, phân tách mặt/nền | MET trong mẫu; flicker/exposure liên tục UNKNOWN |
| Geography/cut/motion | Boundary framing có evidence; continuity và động cơ cut UNKNOWN |
| R04–R09, A/B, toàn phim | UNKNOWN; N02 không cung cấp bằng chứng đủ chuỗi này |

Severity ưu tiên closure; thiếu evidence không thành lỗi đã nghe.

| ID / loại / mức | Expected → observed, vị trí | Method, chắc chắn và closure |
|---|---|---|
| CINE01 — **DEFECT coverage cục bộ**, MAJOR nếu dùng làm toàn bộ R02 | R02 cần mặt Khoai làm điểm tựa. f164=6,8333s và f200=8,3333s không có mặt; board còn xác nhận các mẫu món f166/167/168/176/192/194/196/198/199. Chưa kết luận toàn khoảng giữa các mẫu hoặc từ nào bị che. | Xem JPEG + board: chắc chắn cao về mặt vắng ở mẫu, UNKNOWN về vi phạm theo lời. DOP/EDIT tại G1–G2: lập map lời↔frame và range có mặt. Đóng bằng candidate/hash mới hoặc mapping chứng minh insert có nhiệm vụ và coverage nói đáp ứng214; AV kiểm lời/sync riêng. |
| CINE02 — **UNKNOWN cut rationale**, MAJOR | Cut phải theo chú ý/kết ý. f71(2,9583s)→72(3s), f163(6,7917s)→164, f200→201(8,375s) đổi cỡ/đối tượng khung. Chưa biết rơi trước/sau ý kể hoặc có động tác dẫn. | Cặp frame kề nhau xác nhận đổi hình; không nghe/xem liên tục. EDIT/DIR tại G1–G2: nêu lý do từng cut, kiểm đoạn trước/sau trên đúng export. Closure cần EDL và continuous visual + actual AV, không chỉ bảng time. |
| CINE03 — **UNKNOWN gaze/staging**, MAJOR | R02 từ món lên Đào khi chia sẻ. f72 nhìn trước/hơi xuống; f163 hướng phải; f201 hai người hướng về nhau. Mẫu không chứng minh tuyến nhìn liền hoặc Đào nghe trong đoạn cận. | Quan sát mắt tĩnh: cao về từng mẫu, thấp về ý định. DOP/ACT/PERF: kiểm đoạn liên tục không tiếng và có tiếng, giữ geography trái/phải. Closure là evidence đúng version cho cue và phản ứng, không suy từ miệng mở. |
| CINE04 — **Aesthetic concern**, MINOR | Cận cần tập trung Khoai, vẫn đọc quan hệ nghe. f163 chỉ lát mặt/thân Đào sát mép phải; đèn nền sáng phía trên, món bị cắt dưới. Có nguy cơ mép nhân vật phân tán chú ý, chưa là lỗi continuity. | Xem trực tiếp/reference: quan sát rõ, tác động thẩm mỹ cần lựa chọn. DOP/EDIT đề xuất cận sạch hoặc cận vừa có Đào đủ rõ; không crop để giấu khẩu hình. Closure bằng ảnh/range đề xuất và owner chọn nếu đổi nhiệm vụ shot. |
| CINE05 — **UNKNOWN motion/light**, MAJOR cho gate media |214 yêu cầu mặt/đường hành động rõ trên media. Mẫu sáng ấm, mắt/mặt đọc được, nhưng không kiểm flicker, biến dạng hoặc độ ổn định qua cut. | SAMPLED_FRAMES; không phép đo Kelvin/lens/exposure. DOP/CINE tại G2/G4: kiểm playback đúng hash. Closure cần continuous evidence; không yêu cầu relight chỉ vì thiếu evidence. |

## Ba hướng xử lý và verdict

1. **Chọn range có mặt:** kiểm map N02 và cut. Ít thay hình nhưng có thể thiếu chiều dài/cue cho nguyên lời; không tự kéo dài hoặc che bằng món.
2. **Reframe/pickup R02:** khi range thiếu, đề xuất đủ mặt/hướng nhìn, giữ tông và quan hệ nghe. Cần kiểm khả thi/approval riêng, chưa cấp generation.
3. **Insert món có chức năng:** cần map/playback chứng minh phục vụ mùi/ký ức. Món rõ hơn nhưng có thể mất nét diễn hoặc cut lấp giây; mặt kể vẫn làm điểm tựa.

Khuyến nghị kiểm hướng1 trước; nếu thất bại thì trình hướng2, hướng3 chỉ có điều kiện. **KEEP** tông/reference và khả năng đọc mặt trong mẫu; **NEED_MORE_EVIDENCE** cho source selection, gaze, cut và motion; **REFRAME/REWORK đề xuất** cho coverage R02 nếu map xác nhận thiếu. Không có căn cứ **RELIGHT** bắt buộc. Paper review hoàn thành; source N02 chưa đủ chứng minh G2, full-film/AV/lip-sync/production giữ HOLD, không PASS.

## Tổng hợp năm mục

- **Đã xác định:** hash khớp; mặt rõ ở cận, vắng ở món; ba boundary có evidence.
- **Quyết định đã chốt:**178/214/217 giữ hiệu lực; chưa đổi canon/lời hoặc mở approval.
- **Giả định đang sử dụng:** số frame0-based và fps24 theo dispatch/nhãn board; time là quy đổi hình, không timing tiếng.
- **Còn mở:** map lời–hình, cue mắt, tính liên tục/cut/light, đủ range R02, recovery master và chuỗi A/B.
- **Bước tiếp:** DOP/EDIT lập candidate/range và map; kiểm lại đúng hash theo từng scope trước G2, chưa chuyển finishing.
