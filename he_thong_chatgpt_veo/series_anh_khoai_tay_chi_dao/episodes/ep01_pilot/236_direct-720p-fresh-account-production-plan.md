# EP01 Nem Bùi — Kế hoạch làm lại trực tiếp ở 720p

**Phiên bản:** 236 / v1.0, ngày 07/10/2026.

**Để owner xem xét:** kế hoạch sản xuất, phân cảnh, ngân sách và cổng nghiệm thu. **Chưa được duyệt chạy trả phí.**

## 1. Quyết định mới và phạm vi

Owner: “thôi làm trực tiếp trên 720 đi, ta đã test rất nhiều rồi mà; vậy bạn đã có 1 bản plan chi tiết chưa, trình lên thành file cho tôi xem nào”.

Ghi nhận: **sản xuất trực tiếp ở 720p**; bỏ chặng thử 360p và tuyến 360p → sinh lại/nâng lên 720p của dự toán 235. Kế thừa kinh nghiệm, không tuyển giọng hoặc thử cơ học hàng loạt từ đầu. Đây là duyệt hướng độ phân giải và yêu cầu lập kế hoạch, chưa là duyệt ngân sách 500 hoặc từng request.

| Nội dung | Cách làm trong kế hoạch này |
| --- | --- |
| Đích bàn giao | Một video TikTok 30 giây, dọc 9:16, bản hình 720p gốc và tiếng Việt |
| Tài khoản | Project mới trên tài khoản Flow mới; chưa được cung cấp hoặc kiểm quyền truy cập |
| Creative | Giữ Khoai/Đào, câu chuyện Nem Bùi, lời C-v0.6 và tinh thần storyboard 214 |
| Media | Tạo mới toàn bộ footage, kể cả đoạn ký ức; không lấy clip cũ vào phim mới |
| Tư liệu được kế thừa | Kịch bản, research, thiết kế, ảnh gốc hợp lệ, thông số giọng và bài học đã ghi; không xóa project cũ |
| Voice | Tái tạo hướng K20/Orus và D06/Aoede trên tài khoản mới, ghi ID mới và xác nhận chất giọng; không hứa clone chính xác waveform cũ |
| Công cụ chính | Google Flow, tuyến tạo mới Gemini Omni Flash 1.1 ở 720p; chưa mặc định dùng Veo Quality |
| Dựng | Ưu tiên Scenebuilder của Flow để cắt–nối; local phục vụ QC/lưu bằng chứng. Chỉ dùng local cho công đoạn dựng mà Flow thực sự không đáp ứng, sau khi nêu cụ thể |
| Cách sinh | Một request, một đầu ra; kiểm ngay và ráp dần. Không batch thử x3 hoặc thử tay riêng |

**Trạng thái thực:** đã có kế hoạch này; chưa có tài khoản mới, project mới, giọng mới, bộ ảnh mới hoặc media 720p mới. Các phần dưới là thiết kế thực thi, không chứng nhận sẵn sàng sản xuất.

## 2. Tiêu chuẩn thành phẩm không được đánh đổi

- Hai nhân vật nguyên bản, trưởng thành; Khoai trái, Đào phải theo trục tương tác được thiết lập. Là bạn, không mặc định cặp đôi.
- Khoai chín chắn, kén ăn, giọng Bắc trầm ấm, kể thân mật với nét cười kín; hài ở nhịp và cách chữa cháy, không làm anh ngốc hoặc giọng MC. Đào cởi mở, tò mò và trêu duyên, không giọng trẻ em hay giám sát.
- Quán nhỏ ven phố bình dân, gọn gàng; ánh sáng ấm nhưng đọc rõ mắt, mặt, bàn và đường miếng nem. Không tự thêm thương hiệu/nhà hàng.
- Có mặt người nói và phản ứng người nghe ở các lượt thoại. Cận món/tay phải có nhiệm vụ rõ, không phủ cả câu để né lỗi miệng.
- Nem Bùi nguội, không hơi nóng/khói; dạng thịt/bì/thính phù hợp tư liệu. Có rau/lá, hai đồ chấm, hai bát cá nhân, hai đôi đũa và cốc ngoài phía Đào. Không tự dời rau để thuận tiện prompt.
- Đũa đúng chiều, tay hợp lý; miếng A chưa chạm miệng Khoai, được chuyển và thả một lần vào bát Đào. Miếng B cuối là miếng khác, về phía Khoai; không nhân đôi, đổi người cầm hoặc reset bát.
- Đúng lời, người nói, giọng được chọn và khẩu hình; không thêm lời/người dẫn/nhạc để lấp nhịp. Không tăng tốc hoặc đổi pitch để ép 30 giây khi chưa được duyệt.
- Ký ức gia đình là fiction nhân vật, không fact về món. Claim trọng yếu có nguồn và chữ AI disclosure phải đọc được, không che mặt/tay.
- Nghiệm thu trên bản export thực, không dựa vào file decode sạch, ASR đúng, preset đúng tên hoặc approval riêng từng ảnh.

## 3. Khóa lời thoại và nguồn quyết định

| Mã | Người nói | Nguyên văn |
| --- | --- | --- |
| N01 | Đào | Anh nhìn mãi. Không hợp thì để em. |
| N02 | Khoai | Khoan. Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ. |
| N03 | Đào | Anh chờ ăn à? |
| N04 | Khoai | Chờ mẹ quay lưng. |
| N05 | Đào | Chờ em quay lưng nữa à? |
| N06 | Khoai | Anh gắp cho em mà. |
| N07 | Đào | Thế em quay lại đúng lúc rồi. |

N02 tách biên tập sau “Khoan.”: C01B chỉ sinh từ này; C02 sinh phần ký ức còn lại. Không sinh Khoan hai lần hoặc cho Đào đọc đoạn “Hồi bé”. Ranh giới thực phải kiểm bằng nghe và hình, không tự cắt theo timestamp mẫu.

Nguồn thẩm quyền: [178 — sửa thoại](178_owner-dialogue-amendment-c-v0.6.md), [214 — storyboard](214_recovery-storyboard-r1-and-acceptance.md), [217 — gate và vai](217_recovery-tier4-runtime-gates-and-questions.md), [152 — cặp giọng](152_owner-selected-voice-pair-k20-d06.md). Các mẫu giọng cũ chỉ làm đối chứng; ID cũ không dùng làm binding trên tài khoản mới.

## 4. Bài học được chuyển thành hành động kiểm soát

| Bằng chứng đã có | Biện pháp trong kế hoạch mới |
| --- | --- |
| 200/201: một giọng K20 xuyên N02 được owner chấp nhận; 180/199 từng lẫn vai | Mỗi đơn vị có thoại chỉ dùng một người nói/voice. Giữ người nghe nhưng không thêm voice của họ vào request đó |
| 160/162: đầu–cuối tốt chưa ngăn vượt điểm dừng/tự ăn | Nêu trạng thái và cue theo nhịp; kiểm cả đường đi, không chỉ ảnh cuối. Không coi chia shot hoặc prompt mới là fix chắc chắn |
| 193/194: tắt tiếng vẫn có miệng diễn sai | Kiểm miệng người nghe/shot không lời bằng hình thực; không tin toggle là chứng minh môi khép |
| 206/207: đưa bát và chuyển–thả gộp bị thiếu bước; tách đã có kết quả bộ phận | R07 có thoại và đưa bát; R08 chỉ đặt nem. Đầu R08 kế thừa trạng thái thật của R07, vẫn kiểm match qua cut |
| 209/211: dựng để phủ lời làm 7/7 câu không thấy mặt | Bảng câu→mặt→vai→shot là điều kiện chặn; DIR/ACT/EDIT review bản ghép thực, không chỉ hợp đồng trên giấy |
| 232: video-edit bị từ chối chỉnh speech | Không dùng video thoại cũ làm nguồn để yêu cầu tái tạo miệng. Cảnh nói sinh mới từ ảnh + đúng customvoice |
| 172: thao tác kiểm chip làm gỡ ảnh | Kiểm input/mentions bằng readback không gỡ chip; xem screenshot cuối sau mọi thay đổi rồi mới gửi |
| Nhiều lượt download timeout nhưng file đã tải | Kiểm tên/file/hash/decode trước báo tải thất bại; không tiêu credit để chữa tín hiệu tải |

Chi tiết dự báo/rủi ro tại [234](234_evidence-based-production-forecast.md). Không khẳng định số thử cũ đã đủ chứng minh mọi cảnh 720p mới sẽ đạt.

## 5. Bộ đầu vào phải chuẩn bị trên tài khoản mới

### 5.1. Master hình và bàn ăn

Root chuẩn bị một master hình EP01 mới từ thiết kế đã duyệt và tư liệu hợp lệ, có đủ hai mặt/bàn/món/phục vụ. Không trộn nhiều chuẩn cũ để model tự chọn. N02 B cũ là kinh nghiệm bố trí cảnh, không là footage/track nguồn của phim mới.

Tạo ảnh theo nhiệm vụ và góc máy, không bắt mọi cảnh bám cùng cỡ khung. Master được duyệt về hình là chuẩn kiểm nhân vật/ánh sáng/bàn; các trạng thái hành động khác vẫn phải kiểm riêng. Ảnh miễn phí chỉ được tạo nếu quote thực 0; có phí phải trình khoản riêng.

### 5.2. Giọng

- Khoai: base Orus, đúng chỉ dẫn chung/performance K20 theo 148/149; không K12 hay Orus nền. Chất Bắc tự nhiên, ấm chắc, thân mật, nhịp thay đổi, ngượng kín khi chữa cháy.
- Đào: base Aoede, đúng chỉ dẫn chung/performance D06 theo 150/151; nữ Bắc trưởng thành, thoáng và gần gũi, trêu nhẹ không chói/nũng nịu.
- Lưu base, performance nguyên văn, sample, custom ID mới, ngày tạo và phạm vi owner chấp nhận. Preview kiểm phục hồi lựa chọn trên nick mới, không mở một cuộc tuyển giọng mới. Nếu quote preview >0, dừng trình lại.
- Không chỉ dựa vào cùng tên hoặc ID input để báo output đúng giọng. Tiếng thực của C02 và C01A là hai mốc nghe bắt buộc trước mở rộng các cảnh cùng nhân vật.

### 5.3. State vật thể chung

F0: nem trên đĩa, chưa gắp; bát Đào trống. F1: A đã gắp về Khoai, chưa chạm miệng. F2: A còn kẹp, Khoai khựng khi bị thấy. F3: A đổi hướng về bát Đào, cô nhận. F4: A nằm trong bát Đào; sau đó B mới rời đĩa về Khoai.

Khi Khoai cầm đôi đũa, đôi ấy không còn nghỉ trên bàn; không giữ thêm một đôi giống hệt trước anh. Không đổi hai bát hoặc để A xuất hiện lại trên đĩa. Cảnh sau dùng trạng thái ra **thực của range được chọn**, không dùng ảnh cuối đẹp nhưng video không đạt.

## 6. Shot list và ngân sách lượt đầu — 11 đơn vị

Đây là **đề xuất triển khai storyboard 214**, cần owner duyệt đặc biệt ở cách tách R01/R03/R07–R08. Chưa có đủ ảnh/prompt/input ID mới. Thời lượng sinh là thời gian để model diễn, không bắt buộc đưa cả clip vào phim.

| Clip / nhiệm vụ | Tuyến / giọng | Khung và diễn cụ thể | Trạng thái vào→ra | Duration sinh đề xuất / giá tham chiếu |
| --- | --- | --- | --- | --- |
| C01A — N01 | Ingredients / chỉ D06 | Khung hai người đủ mặt/tay/bàn. Đào nhìn anh, nói thân mật và đưa tay ngoài về gần mép đĩa; Khoai nghe, chưa nói | F0→F0; kết tay đang định lấy, chưa chạm món |6s /10|
| C01B — “Khoan.” | Ingredients / chỉ K20 | Khung hai người hoặc cận vừa tương thích vẫn thấy tay Đào. Khoai ngắt nhẹ; Đào nghe rồi dừng, thu tay. Không reset tay qua cut | F0→F0; tay nghỉ trước ký ức |4s /7|
| C02 — N02 phần ký ức | Ingredients / chỉ K20 | Cận vừa Khoai thấy mặt/miệng; nhìn món rồi chia sẻ với Đào, cười kín. Có thể về khung chung nếu đúng nhịp, không phủ lời bằng cận món | F0→F0; tay nghỉ |10s /15|
| C03A — N03 | Ingredients / chỉ D06 | Khung hai người, Đào hỏi tò mò thật; Khoai nghe, không nói thay | F0→F0 |4s /7|
| C03B — N04 | Ingredients / chỉ K20 | Khung chung tương thích; Khoai đáp tỉnh bơ, Đào nhận ra ý đùa rồi chuyển chú ý tới cốc | F0→F0; chưa gắp |4s /7|
| C04 — tranh thủ gắp | Frames / không voice | Khung mở đủ hai mặt/cốc/đũa/đĩa. Đào quay lấy cốc trước; Khoai gắp A hướng về mình, dừng rõ trước mặt, không ăn | F0→F1 |6s /10|
| C05 — N05, bắt gặp | Ingredients / chỉ D06 | Cô quay lại, thấy A rồi nhìn anh; anh nhận ra bị thấy, khựng. Cô nói sau phát hiện, giữ cả hai mặt và đường A rõ | F1→F2 |6s /10|
| C06 — N06, chữa cháy | Ingredients / chỉ K20 | Thấy mặt Khoai và đũa; nói bình thản rồi đổi hướng cùng A về phía bát Đào. Không làm như gắp cho cô ngay từ đầu | F2→F3 |6s /10|
| C07 — N07, nhận lời chữa cháy | Ingredients / chỉ D06 | Khung hai mặt; cô nhìn A rồi anh, hiểu và trêu nhẹ, đưa bát riêng trống nhận. Khoai giữ A chờ, không nói thay | F3→F3; A còn trên đũa trên vùng nhận |6s /10|
| C08 — thả A | Frames / không voice | Insert ngắn có lý do: nhìn rõ cùng A vào bát Đào một lần, đũa rời. Không sinh thêm miếng hoặc lấy thêm | F3→F4 |4s /7|
| C09 — kết ăn ý | Frames / không voice | Khung hai mặt và bàn. A còn trong bát Đào; cô cười nhẹ, Khoai gắp miếng B khác về mình; kết ở nét hiểu nhau | F4→F4+B |4s /7|
| **Tổng giá tham chiếu lượt đầu** | | | |**100 credit**|

Giá trên là bảng công bố ngày 07/10, **chưa là quote trên tài khoản mới**. Dùng thời lượng dài hơn khi thoại/hành động thực cần; giữ trần lượt đầu 165 =11×15, không ép cảnh vào 4s để khớp 100. Frames không thêm custom voice. Ingredients có voice không được gọi là khóa START/END chính xác. Không đổi mode trong im lặng nếu composer tự fallback.

Mỗi clip có phiếu riêng trước submit: nguồn ảnh/hash và cloud ID mới, prompt nguyên văn/hash, người nói/voice ID, camera/nhịp, model/mode/aspect/resolution/duration/x1/Agent OFF, giá thực, trần request, kết quả kỳ vọng và điều kiện loại. **Bảng này chưa phải 11 prompt sẵn sàng sản xuất.**

## 7. Nhịp phim 30 giây — phân bổ thời gian, chưa khóa điểm cắt

| Nhịp | Khoảng dựng đề xuất | Phần cần thấy/nghe |
| --- | --- | --- |
| R01 / C01A+B |0–4,5s|Đào nói/vươn → Khoai ngắt → cô dừng/thu |
| R02 / C02 |4,5–13s|Ký ức thân mật, mặt Khoai và người nghe |
| R03 / C03A+B |13–16s|Hỏi–đáp và nhịp nhận ra ý hài |
| R04 / C04 |16–19s|Cô lấy cốc; khán giả thấy anh tranh thủ |
| R05 / C05 |19–21,5s|Nhìn A→nhìn anh→khựng→câu trêu |
| R06 / C06 |21,5–23,5s|Chữa cháy và đổi hướng |
| R07 / C07 |23,5–26s|Cô hiểu, nói và đưa bát |
| R08 / C08 |26–27,5s|Thả A một lần |
| R09 / C09 |27,5–30s|Gắp B về mình, hai người cùng hiểu |

Tổng 30 giây để kiểm thiết kế, **không phải timing audio/EDL đã được đo**. Có thể điều chỉnh khoảng nghỉ và cho hành động diễn cùng thoại khi hợp nghĩa. Mốc nguy cơ chật: C01B dừng–thu tay, C05 phát hiện–nói, C06 nói–đổi hướng. Trước master phải nghe/đo lời thực và kiểm chuyển động. Nếu không vừa, trình phân bố lại; không cắt âm/cuối lời, tua nhanh, bỏ nhịp hoặc bịa thời lượng nguồn.

Cắt tại câu/ánh nhìn/hành động có lý do, giữ cùng phía trục; không dùng hòa cảnh để che bát/mặt thay đổi. Cận tay C08 là bằng chứng thả, không thay cảnh nói C06/C07. Không thêm flashback hoặc lời mới.

## 8. Các chặng thực thi và điều kiện chuyển

P0–P6 trong bảng này chỉ là mã công việc của **kế hoạch làm lại**, không phải mở lại các stage P0–P6 của hệ thống phát triển series. Dự án EP01 hiện vẫn ở phần khắc phục sản xuất; không ghi các chặng mới đã hoàn thành.

| Chặng | Việc root/vai thực hiện | Đầu ra phải có | Điều kiện chuyển / owner checkpoint |
| --- | --- | --- | --- |
| P0 — Nhận tài khoản mới | Owner đăng nhập; root kiểm đúng account/project/gói/tính năng/giá qua UI, không lấy mật khẩu | Hồ sơ account, số dư, bảng tính năng, project URL mới | Có quyền dùng Omni 720p/voices; chưa sinh nếu chưa rõ tuyến/quote |
| P1 — Khóa đầu vào | Chuẩn master hình, bảng trạng thái, hai custom voices, phân cảnh và nhịp 30 giây | Asset manifest, voice bindings mới, bảng ảnh có nhãn giới hạn, brief từng nhiệm vụ | Owner duyệt hình/giọng tái dựng và cách tách; DIR/DOP/ACT/EDIT đóng lỗi đầu vào |
| P2 — C02 đầu tiên | Sinh cảnh ký ức 720p, một voice/mặt rõ; đây là footage sản xuất, không bài test rời | Native/hash/bản nghe/khung/timecode và report | Owner nghe/xem chất Khoai, lời/nhịp/khẩu hình; nếu đạt giữ clip, không sinh lại vì tên “test” |
| P3 — Mở và hỏi–đáp | C01A→C01B; kiểm giọng Đào và dừng–thu tay, sau đó C03A→C03B | Bản dựng thô phần mở/ký ức/hỏi–đáp, EDL và speaker map | Có hai giọng đúng, mặt–tay–cue nối được. Không kéo tiếp chuỗi nếu đầu vào kế sai |
| P4 — Đường món | C04→C05→C06→C07→C08→C09; mỗi clip kiểm rồi lấy trạng thái ra thật chuẩn bị clip sau | Native/range chọn, sổ A/B, khối hành động và report độc lập | Chuỗi ý định→phát hiện→chữa cháy→nhận→kết đọc được; không ăn A trước trao |
| P5 — Ráp toàn 30 giây | Flow trim/arrange/download; đối soát EDL bằng native frame thực | Bản dựng thô đúng version/hash, bản đồ câu–hình, audit điểm cắt | DIR/DOP/ACT/EDIT + reviewer kiểm toàn phim; owner duyệt, không chỉ phụ đề/âm lượng |
| P6 — Hoàn thiện | Chữ món/fact, phụ đề, nhãn AI, âm thanh nền/mix và export | Master 720p dọc, gói nguồn và report | Không đổi hình/voice đã duyệt mà không tái kiểm phần ảnh hưởng; owner duyệt đúng file cuối |

Thứ tự tạo mới: **C02 → C01A → C01B → C03A → C03B → C04 → C05 → C06 → C07 → C08 → C09.** C02 khóa tiếng Khoai và phong cách; C01A xác nhận tiếng Đào; chuỗi hành động phải theo phụ thuộc. Root có thể chuẩn bị brief sau song song nhưng không submit khi trạng thái nguồn trước chưa đạt.

Không tách P2 thành một vòng 360p hoặc tuyển 20 mẫu giọng. Nếu output 720p đầu không đạt, đây là lỗi sản xuất có hồ sơ; sửa có mục tiêu sau chẩn đoán, không tự gọi kinh nghiệm cũ vô giá trị hoặc mở test hàng loạt.

## 9. Vận hành các vai đã có — không chỉ liệt kê tên

Phân công theo hồ sơ 217; không thiết kế thêm bộ agent mới trong lượt lập kế hoạch này:

| Vai / scope | Kiểm trước tạo | Kiểm media thực / đầu ra |
| --- | --- | --- |
| DIR — đạo diễn tập | Nhịp và ý nghĩa cảnh, hệ quả của việc tách shot | Chuỗi kể đúng chuyện; không biến thành review món hoặc quảng cáo |
| DOP + CINE-LIGHT | Cỡ cảnh, trục và hướng nhìn, vùng mặt–món–tay, ánh sáng mắt | Bố cục/ánh sáng và lý do chuyển cảnh; không dùng bóng tối hoặc crop che lỗi |
| ACT + PERF | Tín hiệu nghe–dừng, nhớ, tranh thủ, bị thấy, chữa cháy | Hành vi có quan hệ nhân quả; không đánh giá chỉ bằng tính từ |
| EDIT + DLG-EDIT | Phân bổ thời gian, độ phủ và trạng thái đầu–cuối | Danh sách điểm dựng/range/hash, giữ lời và nhịp; tính liên tục quanh điểm cắt |
| CTD/PROMPT/FLOW | Tuyến tạo, đầu vào, tính năng và giá phù hợp | Đúng cấu hình thực, nguồn gốc và dấu vết sai lệch; không tự chi |
| CONT + FOOD | Trạng thái A/B, tay/đũa/bát/cốc và cách phục vụ | Không biến mất/reset/nhân đôi; nem nguội, chất liệu và cách dùng đúng |
| SIA + AV-VOICE/AV-CUT | Câu→người nói→giọng và mặt người nghe/nói | Nghe đúng giọng/lời, kiểm khẩu hình và đối ứng; transcript không thay nghe |
| Fact & Source Auditor | Hai claim và tư liệu đi cùng chữ | Không biến fiction thành fact; mọi claim mới phải có nguồn/duyệt |
| Root | Tích hợp hồ sơ, quyền và các phụ thuộc | Đọc toàn báo cáo, xử lý bất đồng, trình lỗi/phần chưa biết và nhật ký quyết định |

Mỗi lượt làm việc có artifact/version/hash, phạm vi và năng lực kiểm thực. Maker không tự phản biện độc lập chính output mình. Trước các chặng P2/P4/P5/P6 phải có nhiệm vụ chuyên môn hiện hành theo quyền tại 217; **lượt 236 chỉ lập kế hoạch, chưa giao agent kiểm video mới**. Nếu thiếu năng lực nghe, phải có mốc kiểm của con người cụ thể; không viết PASS giả hoặc giao owner toàn bộ audit.

Nếu các góp ý chuyên môn mâu thuẫn, root trình bảng lựa chọn/hệ quả thay vì hòa trộn prompt. Cổng local chỉ kiểm hồ sơ ở đường dựng đã tích hợp; không hứa code ngăn được nút Flow. Bản ghép Flow tải về là target mới phải kiểm, không được bỏ gate vì dựng ngoài repo.

## 10. Checklist nghiệm thu mỗi clip và điểm nối

### Trước gửi

1. Đúng lời/vai/hành động/phiên bản đã duyệt; nguồn không REWORK hoặc lấy từ nick cũ mà chưa đối soát.
2. Ảnh đúng trạng thái và trục; người nghe/lượng món/đũa/bát/rau/chấm/cốc đúng. Không đưa ảnh đối nghịch vào cùng request.
3. Một voice duy nhất đúng custom ID mới ở clip nói; đủ mention và chip, không còn lời thử giọng cũ. Clip Frames không có voice chip.
4. Omni 1.1 Flash, 720p, 9:16, x1, Agent OFF, thời lượng phù hợp; giá thực và quyền chi đúng request còn hợp lệ. Không Quality hoặc fallback tự động.
5. Xem screenshot cuối sau readback; không bấm chip làm mất input; mọi sửa đổi ô nhập phải được kiểm lại.

### Sau tạo

1. Ghi job ID/kết quả/số dư/phí/hoàn phí thực. Lỗi không tính phí không cấp quyền thử lại; job chưa có output không được chấm lỗi chuyển động.
2. Tải qua UI, kiểm file thật/hash/ffprobe/giải mã toàn file; giữ native nguyên bản. Timeout sự kiện không là bằng chứng tải thất bại.
3. Trích toàn khung hoặc đoạn kiểm theo FPS thực; chọn native frame chính xác, bảng toàn clip và mẫu dày quanh tay/miệng/gắp/dừng/thả/cắt. Ghi cụ thể phần nào đã xem; không gọi bảng mẫu thưa là xem hình–tiếng liên tục.
4. SIA/owner nghe đúng người nói/giọng/lời/âm cuối; ACT/DIR xem chuyển động thực trong khả năng công cụ. File có audio hoặc ASR đúng không đủ.
5. Lưu phát hiện: timecode/frame, kỳ vọng/quan sát, mức nghiêm trọng, tầng nguồn→prompt→take→cut, cách sửa và phần phụ thuộc.
6. Chọn range **đạt nhiệm vụ**, không chỉ vài frame đẹp; nối với clip trước ở tư thế/hướng nhìn/miệng/đũa/món/bát/cốc/ánh sáng. Clip đạt riêng không tự đạt điểm nối.

**Lỗi chặn không được bỏ qua:** sai người/giọng/lời; mất mặt người nói ở nhịp quan trọng; miếng A chạm miệng trước khi cho Đào; mất/nhân đôi/đổi A; thiếu nguyên nhân bị bắt gặp; món có khói hoặc sai nghiêm trọng; không đủ lời/hành động vào 30 giây; input hoặc report sai target.

Phân biệt MINOR có thể trình chấp nhận với MAJOR phải sửa, không tự xếp mọi sai lệch là “nhỏ”. Owner không bị yêu cầu nghe lại clip lỗi đã rõ chỉ để hợp thức hóa PASS.

## 11. Ngân sách mới — bỏ khoản thử 360p

**Trần đề xuất vẫn 500 credit, chưa được owner duyệt.** Không cộng 500 với 77 cũ hoặc chuyển ngân sách nick cũ tự động.

| Nhóm | Khoản đề xuất | Cách dùng |
| --- | ---: | --- |
| 11 lượt sản xuất đầu ở 720p |165| Bảng clip dự kiến 100; cap 165 khi cần thời lượng dài hơn, tối đa 15/output |
| Tạo lại có mục tiêu |180| Tối đa 12 output nếu ≤15; sửa clip nguồn sai sau chẩn đoán, không quyền retry mặc định |
| Bổ sung cảnh/điểm nối sau bản dựng thô |45| Tối đa 3 output nếu ≤15; không tính phí xem/ghép |
| Dự phòng chưa phân bổ |110| Tính năng/ảnh/voice có phí, clip thêm hoặc tuyến khác sau trình duyệt |
| **Tổng** |**500**| Không bắt buộc dùng hết |

So với 235: bỏ 60 thử 360p; tăng khoản tạo lại 30 và dự phòng 30. Không coi hủy test là giảm tiêu chuẩn hoặc tiền chắc chắn đã tiết kiệm. C02/C01A lần đầu là sản xuất thật kiêm kiểm tích hợp; nếu đạt dùng luôn, không tính thành cả test và production.

Kịch bản tham chiếu (không phải xác suất): lượt đầu 100 + 6 lượt sửa×15 + 2 clip bổ sung×15 =220 trước phát sinh; trần lượt đầu 165 + 10 lượt sửa×15 + 3 clip bổ sung×15 =360 trước dự phòng. **Các phép tính không cam kết ngân sách hoàn thành**; 500 là trần xin giữ để không bị ép dùng clip lỗi vì hết tiền. Không có bằng chứng để dự báo 80–90% thành công chỉ từ hạn mức này.

Nếu phải video-edit, giá không nằm trong 7–15 của tạo mới; phải đọc quote và tính lại. Không chọn Quality 100 chỉ để mong chữa người nói/hành động. Không dự toán daily credits/hoàn phí giả định; không mua/nạp tự động.

**Duyệt kế hoạch không bằng quyền chi mọi request.** Theo 215/217 hiện hành, mỗi request cần phạm vi/input/thời lượng/quote/số lượng/trần và owner approval riêng. Nếu owner muốn cấp quyền theo chặng thay vì từng request, phải chốt chính sách mới rõ loại tác vụ/trần/điều kiện dừng trước chạy; root không suy từ “720 đi” thành quyền chi toàn bộ.

## 12. Xử lý lỗi và giới hạn không chạy lặp

- Thất bại upload/job/tool: giữ lỗi UI, kiểm đúng nguồn và file. Nếu tab lỗi, lưu evidence → đóng tab lỗi → mở tab mới cùng project theo 231; không chỉ reload, không né bảo vệ/CAPTCHA. Mở tab mới không cấp quyền submit lại.
- Lỗi nội dung: đóng băng native/prompt/inputs/config; truy nguồn trước, không đổi nhiều điểm vô danh. Đề xuất thay đổi có lý do và tiêu chí; vẫn kiểm hồi quy mặt/giọng/món/bàn/nhịp.
- **Hai output liên tiếp còn cùng lỗi chặn:** dừng mở rộng sản xuất phụ thuộc, trình nguyên nhân đã biết/giả thuyết và cách dàn cảnh/tuyến khác. Đây là ngưỡng dừng, không phải quyền chạy hai lượt khi chưa duyệt.
- Không lấy clip im chồng tiếng lên môi khép, crop bỏ mặt, lấp giây bằng bát nem hoặc bỏ nhịp để ghi đã xong.
- Lượt sửa làm đổi khung ra/master/voice phải đánh dấu tất cả clip/điểm nối bị ảnh hưởng cần tái kiểm. Không giữ report hash cũ khi cut hoặc tiếng đã đổi.
- Nếu ngân sách không đủ, trình cụ thể thiếu nhiệm vụ nào/giá/đề xuất, không cứ chạy hết rồi gọi thiếu credit là nguyên nhân duy nhất.

## 13. Finishing và bàn giao

Scenebuilder có trim/arrange/preview/download theo Google; **chưa kiểm tính năng audio riêng, subtitle/mix của tài khoản mới**. Trước chi clip phải kiểm công cụ dựng đủ các bước cần thiết, không chờ hết credit mới phát hiện không ghép được.

Nếu Flow không có chức năng chữ/track/mix cụ thể: giữ bản hình đã khóa từ Flow và đề xuất hoàn thiện phần đó bằng công cụ đã có, nêu input/output và không đổi cut đã duyệt. Không tự thuê dịch vụ, thêm Gemini API hoặc cài công cụ mới. Không hứa ghép tiếng độc lập là có lip-sync; clip nói vẫn cần diễn xuất nguồn đúng.

Chữ theo nguồn đã duyệt: “Nem Bùi — gắn với Bùi Xá, Bắc Ninh.”; “Thính gạo rang góp một phần vào mùi vị của Nem Bùi.”; “Video được tạo bằng AI.” Phụ đề theo tiếng thực, khớp nguyên văn. Vị trí/thời lượng/kích thước kiểm trên màn hình dọc, tránh UI TikTok và mặt/tay; không ghi vùng an toàn bằng số chưa kiểm. Giữ watermark native, không tự xóa để sạch hình.

Mix ưu tiên thoại rõ, âm thanh quán nhỏ không lấn, không thêm nhạc khi quyền chưa rõ. Kiểm tiếng của toàn phim thực, không chỉ đo peak/dB hoặc nghe sample. Xuất 720×1280/9:16 nếu tuyến thực cho đúng kích thước; FPS theo native và quy trình dựng được kiểm, không hứa 24fps trước probe. Target 30 giây, nguyên vẹn lời/nhịp; encode không lỗi và xem/nghe lại sau xuất.

Gói bàn giao:

1. `EP01_NEM_BUI_30S_720P_vNN_FOR_APPROVAL.mp4`; chỉ đổi nhãn APPROVED sau owner duyệt đúng file/hash.
2. Bản không phụ đề nếu phần finishing có xử lý chữ; không xuất biến thể vô cớ để tăng phí.
3. Natives đầy đủ + refs/voice bindings + prompts/request/UI + EDL/source ranges + fact sources + QC/findings + decisions + credit ledger + lessons.
4. `README_HANDOFF.md` chỉ rõ bản nào cuối, file đã duyệt, giới hạn và cách truy lại; không gọi bản dựng thô/bản QC là final.

## 14. Nơi lưu và mẫu hồ sơ

**Đề xuất tạo khi kế hoạch được duyệt**, chưa có media mới trong các đường này:

- Repo: `he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/restart_720p_v1/`.
- Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/`.
- Nhóm thư mục: `00_decisions`, `01_research`, `02_refs`, `03_voices`, `04_requests`, `05_native`, `06_qc`, `07_edits`, `08_delivery`, `09_lessons`.
- Tên đơn vị: `EP01_720_C05_T01`; native/source hash/Flow ID trong manifest. `T02` là output thứ hai, không giả approval.
- Hồ sơ request: phạm vi, owner approval, exact inputs, prompt/config/quote, số lần gửi, output ID/status, phí thực và ngân sách còn lại.
- Hồ sơ QC: target hash/range, reviewer/capability, criteria/findings/closure, điểm nối liên quan và quyết định. Không có PASS trống bằng chứng.
- Sổ credit: số dư trước/sau, quote, charged/refund và UI nguồn; không dùng số dư account làm quyền chi. Commit/push theo nhóm quyết định/run; không commit secrets/tài khoản hoặc media lớn mặc định.

Kế hoạch/dự toán/report dùng Markdown làm nguồn quyết định. Media gốc giữ nguyên, các biến thể hậu kỳ dùng file mới. Root chịu trách nhiệm lưu từng bước và đối soát; owner không cần tự chuẩn bị khung tham chiếu hay gom báo cáo.

## 15. Những điều cần owner duyệt và bước tiếp

1. **Phân cảnh 11 đơn vị** ở mục 6: giữ chuyện, tách R01/R03 và tách lời/đặt A ở R07–R08. Mốc mục 7 là phân bổ thời gian dự kiến, được điều chỉnh theo media nhưng không tự đổi lời/nhịp chuyện.
2. **Trần dự trù 500 credit** theo mục 11, không buộc dùng hết; mỗi request vẫn xin duyệt phạm vi/quote theo quyền hiện hành.
3. **Tài khoản mới và tiếp nhận:** owner tự đăng nhập, root kiểm tính năng/giá; phục hồi hai preset theo hướng đã chọn và nghiệm thu lại, không bắt buộc giống tuyệt đối waveform cũ.

Không cần owner chọn lại nhân vật, tên, món, script hoặc 20 mẫu giọng. Sau duyệt plan: tiếp nhận account → chuẩn master/voice/briefs → chuyên môn/reviewer đóng lỗi đầu vào → trình một request C02 sản xuất 720p với quote thực. Không sinh bài test trả phí trước đó.

## 16. Tổng hợp trạng thái

- **Đã xác định:** owner chọn 720p trực tiếp; kinh nghiệm và nguồn quyết định đã đối soát, kế hoạch chi tiết này đã viết.
- **Đã chốt:** độ phân giải/hướng sản xuất, giữ creative; chưa chốt 500, split 11 clip hoặc quyền submit mới.
- **Giả định:** có Omni/voices trên nick mới, không tái dùng footage cũ, giá 720p tạo mới 7–15, ảnh/preview chỉ khi quote 0; các giả định phải được kiểm lại.
- **Còn mở:** account/tính năng, master/voice ID mới, prompt/ảnh cho hành động, timing thực, độ ổn định và finishing Flow.
- **Bước tiếp:** owner review ba điểm ở mục 15; sau đó root chuẩn bị, không giao owner làm thay công việc sản xuất.

### Nguồn công cụ chính thức — đọc 07/10/2026

- [Credit và giá từng đầu ra](https://support.google.com/flow/answer/16526234?hl=en).
- [Tạo video, Frames/Ingredients và voice references](https://support.google.com/flow/answer/16353334?hl=en).
- [Scenebuilder: trim, arrange, preview, download](https://support.google.com/flow/answer/16935718?hl=en).

Tài liệu Google xác nhận tính năng/giá công bố, không bảo đảm chất lượng clip hoặc thay quote/UI trên account thực.
