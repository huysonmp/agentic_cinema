# Tuyển 10 giọng Khoai — câu dài, câu ngắn và biểu cảm

2026-10-02. Owner yêu cầu tạo mười giọng để nghe một lượt, tùy chỉnh kỹ hơn và kiểm câu dài/câu ngắn/biểu cảm. Mười ứng viên preset preview trong Flow, không mười video, không tự duyệt voice hoặc pipeline Omni. Không hứa viral từ tên preset hay chỉ dẫn.

## Đoạn audition chung

109 ký tự, dưới giới hạn UI120:

> Hồi bé, mỗi lần mẹ rang gạo trong bếp, anh cứ đứng cạnh cái chảo, đợi mẹ quay lưng. Khoan! Anh gắp cho em mà.

Câu đầu dài 83 ký tự (tính cả dấu chấm) để kiểm cụm hơi và mạch kể; câu ngắn kiểm bật phản xạ; câu cuối kiểm lời chữa cháy. Đây là lời thử được dựng theo tình huống nhân vật, không sửa kịch bản tập hoặc claim văn hóa. Một đoạn chung cho cả mười giúp so sánh, không chứng minh khả năng nói các đoạn dài hơn 120 ký tự hoặc ổn định cả tập.

Gate nghe gồm: (1) đúng giọng nam miền Bắc xuyên suốt, (2) câu dài không hụt hơi/nuốt tiếng/ngắt vụn, (3) câu ngắn có phản xạ nhưng không hét, (4) chuyển từ ấm áp sang bất ngờ rồi tỉnh bơ nghe tự nhiên, (5) giữ cùng một chất giọng qua ba trạng thái. Sai accent là loại trước khi xếp hạng sức hấp dẫn. Các giọng lọt vòng tiếp theo cần thử thêm đoạn dài hơn giới hạn preview và nhiều lượt để kiểm độ ổn định; không coi đoạn preview này là nghiệm thu voice toàn tập.

## Chỉ dẫn chung

```text
Giọng nam trưởng thành, tiếng Việt giọng Hà Nội miền Bắc tự nhiên; giữ phát âm và ngữ điệu miền Bắc suốt đoạn. Nói như người đang trò chuyện với bạn ngồi cạnh, không đọc bản tin, quảng cáo hay nhại người nổi tiếng. Đọc đúng toàn bộ đoạn mẫu, không nói các chỉ dẫn.
```

Mỗi giọng có thêm hướng âm sắc/nhịp/ngắt/nhấn/chuyển trạng thái riêng. Đây là requested direction, chưa kết quả nghe. Preset base chỉ mô tả chất âm, không chứng nhận giọng Bắc; nghe sai accent phải loại dù diễn hấp dẫn.

| Mã | Base | Hướng diễn |
|---|---|---|
| K01 | Algieba | Ấm và cười kín |
| K02 | Alnilam | Nghiêm mà buồn cười |
| K03 | Achird | Ông anh dễ mến |
| K04 | Algenib | Mộc và có độ sạn |
| K05 | Iapetus | Sắc nét và nhanh trí |
| K06 | Enceladus | Thân mật như kể bí mật |
| K07 | Charon | Ký ức có hình ảnh |
| K08 | Fenrir | Trẻ và tinh nghịch |
| K09 | Algieba | Kén chọn nhưng mềm lòng |
| K10 | Achird | Chậm một nhịp, bật duyên |

## Giới hạn và review

Owner yêu cầu breadth10 thay vòng chỉ một candidate ở147; giữ gate nghe, không tự gọi accent đạt. Preview UI không xuất file qua audio ẩn ở147; bàn giao dự kiến preset lưu để owner nghe trực tiếp. Đọc lại tên/ID actual sau save, không dùng tên requested nếu UI không giữ. Không sửa preset cũ, không xóa nguồn, không attach production prompt hoặc tạo video. Đối soát số dư sau cả bộ. Record từng preview completion và save ID; nếu chưa nghe thật thì không chấm viral/diễn/giọng.

Trạng thái thực thi: 10_PREVIEWS_COMPLETED / 10_PRESETS_SAVED / OWNER_LISTENING_PENDING. Audio DOM của từng preview có readyState 4 và duration trước khi lưu; đây là xác nhận kỹ thuật, không review bằng tai. Chưa có file âm thanh local, chưa duyệt accent/biểu cảm hoặc tích hợp vào video.

## Kết quả actual và cách nghe

Trong Flow, mở Thành phần → Giọng nói; tìm `tuỳ chỉnh`. Tại thời điểm bàn giao, mười mục mới xếp từ trên xuống K10 → K01, rồi hai mục cũ. Chọn một mục để xem chỉ dẫn và bấm Xem trước / Phát bản nghe trước; không bấm Thêm vào câu lệnh để tuyển giọng. Thứ tự này là snapshot, không định danh bền vững; nếu thay đổi, dùng base + performance ở dưới và ID actual để đối chiếu. Tên K01–K10 nhập trước save không được UI giữ; tên actual đều là `<Base> tuỳ chỉnh`. Không gọi đây là rename thành công.

| Mã | Tên actual | ID actual | Preview (giây) |
|---|---|---|---:|
| K01 | Algieba tuỳ chỉnh | a5476283-2971-412f-9cdb-f4b228ee4f55 | 9.561 |
| K02 | Alnilam tuỳ chỉnh | 2873bf79-b5ab-4314-b3ea-026f70a1318a | 9.241 |
| K03 | Achird tuỳ chỉnh | f76c36ae-dfa5-48a0-8ff3-7677e1183f48 | 8.081 |
| K04 | Algenib tuỳ chỉnh | 4583cc99-313a-4614-a55e-95cfb034f0ae | 9.201 |
| K05 | Iapetus tuỳ chỉnh | 77c56f8b-4817-439a-8b27-2a0d503cf969 | 8.681 |
| K06 | Enceladus tuỳ chỉnh | 07ea0359-7164-4117-a60c-40c48bb188bd | 10.001 |
| K07 | Charon tuỳ chỉnh | 30a523f0-dd3f-4dc4-9d8e-1cc6d0dac50a | 8.321 |
| K08 | Fenrir tuỳ chỉnh | d2e5ac0f-db09-42de-a28f-ae2e67f8c65d | 8.681 |
| K09 | Algieba tuỳ chỉnh | dc1e8d42-95ce-467b-9c92-a1cbfcda8b60 | 11.681 |
| K10 | Achird tuỳ chỉnh | 0c14ac52-e863-4176-84a2-42dda80e25db | 8.601 |

Đã đọc lại sample và ID sau mỗi save; danh sách cuối có đầy đủ exact performance chung + riêng cho cả mười. Screenshot từng preset và catalog: `D:/Workspace/agentic_cinema/artifacts/voice148-ten-presets/`; bản copy owner: `C:/Users/PC/Downloads/du_an_nem_bui/148_10_giong_Khoai/`. Các ảnh chỉ là bằng chứng thao tác, không audio.

Số dư cuối UI: **670**; mốc trước gần nhất 147 là **620**. Chênh +50 chưa giải thích, không đủ để kết luận chi phí preview bằng 0 hay có hoàn tín dụng. Không bấm tạo video; không dùng ngân sách Quality. Phần còn lại của quyền thử 200 sau 145 vẫn ghi 170 cho video; tách quyền chi khỏi số dư tài khoản actual.

## Kinh nghiệm thao tác

- Lưu thêm custom làm preset phía cuối không còn nằm trong viewport/danh sách dựng sẵn. Tìm theo tên base để đưa vào view.
- Nếu tìm kiếm chỉ còn một base, Flow có thể tự chọn. Kiểm ID `voices/<base>-sample-dialogue` trước click; click lại item đang chọn có thể thêm vào prompt và đóng picker. Một lần Iapetus xảy ra như vậy, đã xóa compose thử trống và mở lại; không generation.
- Tìm kiếm thành phần không tìm theo nội dung performance trong phép thử này; không dùng mô tả diễn làm search key. Đã xóa bộ lọc và kiểm exact performance bằng danh sách UI cuối.
- Không đổi nhiều nội dung mẫu giữa ứng viên. Nhịp, hơi và biểu cảm phải được nghe, không suy từ chỉ dẫn hoặc duration.

## Tổng kết vòng

Đã xác định: có 10 preset preview lưu thành công, chung lời thử dài/ngắn và chuyển trạng thái. Đã chốt: tuyển giọng qua preview, không đổi script hoặc pipeline production. Giả định đang dùng: Hà Nội là hướng Bắc cụ thể cho audition, chưa khóa giọng. Còn mở: owner nghe accent, sức hấp dẫn, độ diễn; file audio riêng; lời dài hơn 120 ký tự; độ ổn định và tích hợp video. Bước tiếp: owner chọn tối đa ba mã đúng Bắc và đáng thử; sau đó kiểm đoạn dài hơn và ba lượt video Lite theo gate hiện hành, với route/settings/credit rõ trước chạy.

## Performance nối sau chỉ dẫn chung — nguyên văn

### K01 — Algieba

Âm sắc tròn, trung trầm, gần tai. Câu dài kể thong thả nhưng liền mạch; ngắt rất nhẹ sau "Hồi bé", mềm hơn ở "mẹ rang gạo", hơi cười ở "đợi mẹ quay lưng". "Khoan!" bật gọn, cao hơn chút, không quát. Dừng một nhịp ngắn rồi "Anh gắp cho em mà" như giải thích rất hiển nhiên; nhấn nhẹ "em", hạ cuối "mà". Nụ cười nằm trong tiếng, không bật cười.

### K02 — Alnilam

Âm trung trầm chắc, gọn, chín chắn. Câu dài có nhịp kể rõ, không ê a; "đợi mẹ quay lưng" chậm nửa nhịp như vừa để lộ bí mật. "Khoan!" ngắn, dứt khoát nhưng không gay gắt. Câu cuối giữ vẻ nghiêm túc tuyệt đối, hơi nhấn "gắp cho em", hạ giọng cuối câu; hài đến từ sự tỉnh bơ, không lên giọng làm trò.

### K03 — Achird

Giọng nam khoảng ba mươi, trung âm ấm và có sức sống; không quá bass. Câu dài như kể chuyện với bạn thân, có nhịp tiến về "đợi mẹ quay lưng", rõ phụ âm mà không đọc từng tiếng. "Khoan!" là phản xạ nhanh bất ngờ. Câu cuối sáng lên một chút, tự tin pha lém lỉnh, nhấn "em" nhẹ rồi thu giọng ở "mà"; không nũng nịu hoặc tán tỉnh.

### K04 — Algenib

Âm thấp, có lớp sạn rất nhẹ tự nhiên, không khàn bệnh hay già nua. Câu dài đủ hơi, kể mộc mạc; câu "mẹ rang gạo" mềm và ấm hơn phần đầu. Đoạn "đợi mẹ quay lưng" lộ chút tinh nghịch. "Khoan!" gọn có lực, không gằn. Câu cuối như vừa bị bắt quả tang nhưng vẫn ung dung: nhấn "anh gắp", dừng nhỏ trước "cho em mà", kết nhẹ.

### K05 — Iapetus

Trung trầm sạch, rõ, âm đầu gọn; tốc độ hội thoại linh hoạt, không nhanh xuyên suốt. Câu dài có hai cụm hơi nối tự nhiên, chậm ở hình ảnh "cái chảo" rồi tăng nhẹ ở "đợi mẹ quay lưng". "Khoan!" bật nhanh sắc nét, không chói. Câu cuối đáp nhanh như đã nghĩ sẵn lời chữa cháy; nhấn "cho em", giữ âm cuối đầy đủ, không nuốt "mà".

### K06 — Enceladus

Giọng nam thấp vừa, gần và mềm, một chút hơi nhưng mỗi tiếng vẫn rõ; không thì thào ASMR. Câu dài mở nhỏ và thân mật, ấm lên ở "mẹ rang gạo", cuối ký ức có nét cười. "Khoan!" dùng giọng thật, rõ hơn phần kể, không hét. Dừng ngắn rồi câu cuối hạ âm lượng như giải thích riêng với bạn; không buồn, không lãng mạn, không kéo dài âm cuối.

### K07 — Charon

Âm trung trầm sâu, giàu cộng hưởng nhưng không giọng thuyết minh. Câu dài đầu bình thường; tới "mẹ rang gạo trong bếp" nhịp mềm hơn như vừa nhớ mùi bếp, ngắt theo ý, không theo từng dấu phẩy máy móc. "đợi mẹ quay lưng" hơi cười kín. "Khoan!" kéo khỏi ký ức, ngắn bất ngờ. Câu cuối trở về giọng đời thường gọn, tỉnh bơ, không diễn bi kịch.

### K08 — Fenrir

Nam trưởng thành trẻ, trung âm sáng vừa, không giọng thiếu niên hoặc hoạt hình the thé. Câu dài có năng lượng và nhịp rõ, hơi tăng tốc ở kế hoạch "đợi mẹ quay lưng" nhưng không nuốt tiếng. "Khoan!" bất ngờ, bật gọn. Câu cuối hơi vội ở "Anh gắp" rồi tự lấy lại vẻ bình thản ở "cho em mà"; hài nhờ chuyển trạng thái, không cười lớn.

### K09 — Algieba

Trung trầm ấm, đầu câu hơi dè dặt và tiết chế. Câu dài bắt đầu khô gọn, tới "mẹ rang gạo" tự mềm lại, kể liền hơi rồi thu giọng ở cuối ký ức. "Khoan!" phản xạ giữ thể diện, ngắn không ra lệnh. Câu cuối cố nói tự tin nhưng có một khoảng chần chừ nhỏ sau "Anh"; cuối "mà" vẫn rõ, hơi cười ngượng kín. Không thành nói lắp hoặc hoảng hốt.

### K10 — Achird

Âm nam trung trầm dễ gần, tiết tấu đối lập rõ. Câu dài kể tự nhiên, đoạn giữa hơi nhanh hơn, cuối "đợi mẹ quay lưng" thả chậm một nhịp với vẻ thích thú. "Khoan!" gọn bất ngờ như sực nhớ. Chừa một khoảng im lặng ngắn rồi câu cuối nói chắc và đơn giản, nhấn vừa đủ "em", kết "mà" có nụ cười. Không kéo dài câu chốt, không dùng giọng MC.
