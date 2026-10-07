# 234 — Dự báo sản xuất dựa trên kết quả và kinh nghiệm thực

Ngày: 2026-10-07. Trạng thái: **AUDIT_AND_FORECAST / NO_GENERATION / NOT_PAID_APPROVAL**.

Owner yêu cầu kiểm lại kinh nghiệm và kết quả để tăng khả năng đạt chuẩn, tránh thử đi thử lại. Đây là audit của root trên hồ sơ, prompt, báo cáo cũ và một số ảnh thực; không phải một lượt reviewer độc lập mới hoặc chứng nhận đã nghe/xem liên tục toàn kho. Không tạo media, đổi giọng, sửa nguồn hoặc dùng credit.

## 1. Kết luận điều chỉnh dự toán 233

**49 credit cho 7 lượt đầu là dự toán chi phí có điều kiện, không phải dự báo 7 cảnh sẽ đạt. Chưa đủ bằng chứng gọi khả năng hoàn thành đúng chuẩn trong 77 credit là cao.** Phần thoại có hướng khả thi, nhưng chuỗi hành động và điểm nối đang là rủi ro chính. Không đưa xác suất 80–90% vì không có tập mẫu tương đương, đủ lớn và được chấm cùng tiêu chí.

Không hủy kịch bản hoặc bỏ mục tiêu nghệ thuật để khớp ngân sách. C-v0.6/178, storyboard214, giọng K20/D06, quan hệ bạn bè, món nguội và đường miếng A → bát Đào → miếng B vẫn là khóa hiện hành. Số dư dùng lập kịch bản ngân sách là 77, từ kiểm UI tại233; lượt234 không kiểm số dư live lại, không chi.

## 2. Bằng chứng thực và giới hạn tái sử dụng

| Hồ sơ | Kết quả đã ghi nhận | Điều có thể học | Điều không được suy ra |
| --- | --- | --- | --- |
| 154 — Omni Ingredients, ảnh + hai giọng, 8s | Có 3 native; giữ dạng Khoai/Đào và bộ bàn trong 8 ảnh mẫu mỗi bản; món còn giống sợi mì, hình tái dựng khác nguồn | Mô tả rõ loại nhân vật, phục trang và bộ phục vụ có ích trong bộ này | Không có 3/3 cảnh cuối đạt; không chứng minh giữ đúng miệng/giọng qua thao tác gắp |
| 180 — Omni Ingredients, 4 lượt thoại/10s | Có 3 native; cả 3 hình REWORK do drift món/bàn/chữ. N02 trong nguồn A03 sau đó bị owner báo sai người/giọng ở199 | Đủ lời theo ASR và đúng chip không bảo đảm đúng vai hoặc hình | Không lấy audio được chọn một phần làm PASS cả take |
| 200 → 201 — Omni Ingredients, chỉ K20/10s | Một output có nguồn N02 được owner duyệt đúng Khoai/K20 xuyên suốt và nhịp | Có positive baseline cho câu dài, một người nói, một voice ID | Chưa chứng minh mọi câu mới hoặc cảnh hai người nói đều đạt; hình200 là diagnostic |
| 221 → 222 — Omni video-edit trên N02, x3 | A/C có blocker hình; B được owner chọn về lời/giọng/nhịp/khẩu hình và cách về khung chung | Có clip N02 B thật để giữ; repair hình trên đúng N02 từng có kết quả dùng được | Không lấy 1/3 của một batch thành xác suất chung 33%; không coi đây là tuyến tạo mới Ingredients |
| 160 — Lite Frames, nâng nem gần miệng | 3/3 loại: vượt điểm dừng, mở miệng, nhìn lại sớm hoặc đổi đường món | Trạng thái nguồn và ý định diễn phải cùng rõ; endpoint tốt chưa khóa đường đi | Không quy lỗi cho một từ hoặc mọi model |
| 162 — ma trận Lite Frames | 17 yêu cầu, 7 video, 10 lỗi âm thanh; 0/7 video qua gate hình của bộ này | Đổi câu lệnh/tách nhịp chưa giải quyết overshoot và hành vi ngoài yêu cầu | Không gộp 10 job không có video thành lỗi hình; không chuyển tỷ lệ này sang Omni |
| 193 + 194 — phản ứng im lặng Lite Frames | Hai bộ, mỗi bộ 0/3 đạt phản ứng theo gate lúc đó; vẫn mở miệng/đổi gaze | Tắt tiếng hoặc viết môi khép không đủ kiểm soát môi; sửa chữ tiếp không phải phương án đã chứng minh | Không chứng minh cảnh Đào có thoại không làm được |
| 191 → 192 — gắp P02 | Owner duyệt nhịp đầu 2,5s; full take và continuity chưa đạt | Có đoạn cơ học gắp thực để tham khảo/tái kiểm nếu hợp ngữ cảnh | Không dùng nó thay khung có mặt, ánh mắt và ý định của R04 |
| 206 → 207 — đưa bát rồi chuyển–thả | U06 thiếu chuyển hướng, bát không còn thấy ở đoạn sau. Sau tách nhiệm vụ, U07 có range chuyển–thả thực f20–77; còn lệch bát ở cut | Tách nhiệm vụ hành động đã cho một kết quả bộ phận dùng để xét; chọn range theo hành động thật, không timestamp prompt | Không chứng minh tích hợp mặt + thoại + đưa bát + release sẽ đạt; không mặc định U07 match chuẩn B |
| 209 → 211 — bản ghép cũ | 7/7 lượt thoại không thấy mặt người nói; 92,9% phim không có mặt đầy đủ theo phân loại cảnh | Lỗi mục tiêu dựng và gate thực thi, không phải chỉ lỗi model | Không sửa bằng đổi FFmpeg sang Flow rồi giữ nguyên shot map sai |
| 227 | S/M đúng nguồn; M được duyệt ảnh tĩnh, motion chưa chạy | Có pose đầu vào mở cảnh, không bắt đầu trắng | Ảnh tĩnh không là hear–stop–return đạt |
| 232 | Một video-edit request bị từ chối chỉnh lời nói, không output, chi0 | Không lặp nguyên tuyến/brief này như đã khả thi | Không kết luận toàn bộ Flow không hỗ trợ thoại; nguyên nhân backend còn giả thuyết |

Root đã đọc các phần liên quan trong hồ sơ nêu trên, đối chiếu prompt thực tại 200 và hai chẩn đoán tại 232. Một số nhận định về chuyển động/âm thanh ở bảng là bằng chứng lịch sử, không phải root kiểm lại toàn bộ hình–tiếng trong lượt 234. Approval theo đúng file/range/scope vẫn giữ, không viết lại thành toàn phim đạt.

## 3. Kiểm nguồn hiện hành trong lượt này

Đã đọc lại SHA-256 của các file sau, khớp hồ sơ cũ:

| Nguồn | SHA-256 |
| --- | --- |
| N02 B native | `660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535` |
| REF01-S v01 | `eba9a13c86f359df458022a5a54664264e5bb29fcca08d6181454cb1ee482422` |
| REF01-M v03 | `66defd18afc0845da8b34968446b98f547dcad951e6712e2e6a81ff2d5e2017c` |
| REF01-E v02 | `8df19973fa6595cd166cab67b08a2009256091fb05bf14be322b1371308dbc03` |
| U07 native207 | `9792a637316692967383990b0eb174471e4ede21edb37b470ef1d7fe60f0bdad` |

Đã xem ảnh thực S/M/E, bảng khung N02 B lấy mẫu chính xác mỗi 0,5 giây và khung native số 24, cùng khung ra U07 số 77. Đây là kiểm ảnh tĩnh/lấy mẫu, không đo khoảng cách 3D hoặc nghe/xem liên tục. S/M cho thấy tay ngoài Đào tiến sát vùng vành đĩa qua phía trước bát; đường đi động chưa chứng minh. E về tay nghỉ nhưng nét mặt/ánh nhìn khác S; không gọi khung cuối đã khớp diễn và điểm cắt sang B. Khung B số 24 bố cục rộng hơn bộ tham chiếu, nhân vật đang chớp/nhìn xuống; không mặc định mốc B ở giây 1 là điểm nối đẹp. Khung ra U07 cho thấy hai bát có chất liệu lốm đốm, bố cục cận không mặt, khác bát/khung của chuẩn B. Chưa đóng kiểm tính liên tục chỉ vì có nem trong bát.

## 4. Giới hạn công cụ ảnh hưởng trực tiếp đến dự báo

Đã đọc tài liệu chính thức của Google ngày 2026-10-07:

- [Tạo video/voice references](https://support.google.com/flow/answer/16353334?hl=en): voice references chỉ dùng trên video Ingredients; các loại generation khác báo lỗi. Không dự toán Frames START/END + customvoice như một tổ hợp đã hỗ trợ.
- [Model/features](https://support.google.com/flow/answer/16352836?hl=en): Omni có cả Frames và Ingredients 4–10s, không có nghĩa mọi feature kết hợp với nhau. Có customvoice và upscale Omni360→720 cho Pro/Ultra0credit, nhưng UI/account/quote thực và kết quả còn phải kiểm.
- [Credit](https://support.google.com/flow/answer/16526234?hl=en): native Omni360p4/6/8/10s tương ứng4/5/6/7credit. Quote thực của request đủ inputs vẫn phải đọc trước submit; không dùng giá base để cấp quyền tự chạy. Public video-edit40 khác quote lịch sử23210; giữ riêng, không viết đè evidence.

**Hệ quả quan trọng:** S/M/E trong Ingredients là ảnh tham chiếu được mô tả vai trò, không được gọi là ba mốc chuyển động đã khóa. Nạp nhiều ảnh không bảo đảm model đi theo thứ tự S→M→E đúng nhịp thoại. Tuyến mới tránh yêu cầu sửa speech của video nguồn, nhưng không tự giải quyết voice attribution, drift và conservation của món.

## 5. Dự báo theo nhiệm vụ, không chấm toàn bộ bằng một tỷ lệ

Các mức dưới là phán đoán có điều kiện của root, không phải xác suất thống kê. Đánh giá cho **đạt toàn nhiệm vụ lần đầu**, không chỉ tạo được file. Không có cảnh mới nào được nâng thành production-ready bằng bảng này.

| Nhiệm vụ | Dự báo hiện tại | Rủi ro chính | Điều cần hoàn thiện trước chi |
| --- | --- | --- | --- |
| R02 — ký ức B | Ít rủi ro phát sinh vì tái dùng clip đã chọn | Điểm cắt và nối hình/tiếng với R01/R03, không phải cần sinh lại | Chọn boundary theo lời/mặt thực; giữ nguồn B nguyên bản, không Khoan hai lần |
| R03 — hỏi/đáp, tay nghỉ | Trung bình; thuận lợi hơn nhóm thao tác món nhưng chưa đủ gọi cao | Hai speaker/voice và miệng người nghe, drift hình | Chốt đúng hai line/ID; cân nhắc hai lượt một speaker nếu cần, không hứa giảm chi |
| R01 — mở, hai người nói, vươn→nghe→dừng→thu | Thấp đến trung bình với brief gộp hiện tại | Nhiều sự kiện, hai speaker, tay qua bát, endpoint chưa match B | Làm rõ cue nào gây dừng, ưu tiên task diễn, kiểm refs nhất quán và timing; chỉ tách nếu vẫn giữ hear→stop→return |
| R04 — Đào lấy cốc, Khoai gắp về mình | Thấp với cảnh tích hợp chưa khóa nguồn | Hai chủ thể/ánh nhìn và pick→lift; ăn ngoài ý định, gap, món dài ra | Ảnh nguồn phải chưa gắp ở đầu, cô chưa thấy anh, đầu/cuối cùng bộ bàn; kiểm ý định với mặt không che bằng insert |
| R05 — Đào bắt gặp, Khoai khựng, cô nói | Thấp đến trung bình | Giữ cùng miếngA trên đũa + hai ánh nhìn + speaker, không tự ăn | Khung đầu lấy trạng thái đạt thực của R04; một voiceD06; xác định nhìnA→nhìnKhoai→anh khựng |
| R06 — Khoai chữa cháy và đổi hướng | Thấp với tích hợp hiện tại | Nói đồng thời đổi hướng cùngA, giữ bát/đũa | Một voiceK20, mặt rõ; đầu vào thực từ R05, đườngA về bát cô; không biến lời thành voiceover trên tay |
| R07–R08 — Đào nói/đưa bát, Khoai thả | Thấp nếu gộp mọi việc vào một lượt | Vật thể bát/miếng và nhiều chủ thể; lỗi206 từng xảy ra | Không mặc định gộp; kiểm khả năng dùng lại insert207 hoặc tách theo trạng thái thật, vẫn có mặt Đào khi nói |
| R09 — cùng hiểu, A trong bát cô, Khoai gắpB mới về mình | Thấp đến trung bình | Reset bát, đổi miếng, model đưaB vềĐào như209 | Khung đầu kế thừa A đã trao; đườngB rõ vềKhoai, không lời mới; giữ kết đã chốt |

Không tính xác suất toàn phim bằng trung bình các dòng: nhiều cảnh phụ thuộc cùng identity, bàn, voice và endpoint. Một cảnh lỗi có thể làm cảnh sau thiếu input và làm điểm nối hỏng. Tái dùng B có cơ sở hơn sinh lại B; chọn đúng preset có cơ sở hơn chỉ mô tả giọng Bắc, nhưng đều không bảo đảm output mới.

## 6. Công việc không trả phí để nâng độ sẵn sàng

Đây là đề xuất chuẩn bị, không paid test hoặc sửa cảnh đã duyệt. Chưa ghi đã hoàn thành các việc dưới.

1. **Một gói nguồn cho từng cảnh:** câu/lượt nói, ảnh nguồn đúng nhiệm vụ, ID giọng, trạng thái A/B/bát/cốc/đũa đầu→cuối, nhiệm vụ mặt người nói/nghe và điểm nối dự kiến. Không dùng lại prompt thử giọng hay ảnh cầm sẵn A để chứng minh gắp từ đĩa.
2. **Kiểm tương thích input–prompt–route:** Ingredients có voice, không tự nhận khóa S/M/E theo timeline; Frames chỉ cho action không cần customvoice khi phù hợp. Mỗi ảnh có vai trò rõ, không trộn baseline TABLE08/B/U07. Đủ budget không thay kiểm capability.
3. **Dựng kế hoạch nhịp toàn bộ 30 giây:** dùng lời/nghỉ đã có để đo, đánh dấu tiếng mới còn UNKNOWN; phân bổ động tác theo quan hệ nhân quả, không lấp giây bằng cận món. Không ép mọi lượt sinh dài 4 giây hoặc dùng toàn bộ 10 giây; không coi ảnh tạm là chuyển động đạt.
4. **Phân tách nhiệm vụ có chủ đích:** ưu tiên một người nói/voice ở cảnh phù hợp, một đường chuyển đồ ăn chính; cho phép coverage và góc máy có lý do. Việc tách phải giữ câu chuyện, mặt khi nói, nghe→dừng và đường A/B; không giản lược thành hai người đứng nói hoặc toàn cận tay.
5. **Khóa tiêu chí và ngoại lệ trước submit:** dự kiến defect dễ gặp, frame/range cần kiểm, điều kiện loại, chi phí nếu phải tách và tác động tới cảnh kế. Screenshot/readback cuối sau tất cả thao tác; bất kỳ thay compose phải kiểm lại nguồn/mentions/quote.
6. **QC ngay trên cảnh sản xuất và điểm nối:** hash nguồn, lời/vai/giọng qua nghe thật, mặt/miệng, chuyển động thực và khung lấy mẫu dày quanh gắp/dừng/thả/cắt; không chỉ thumbnail/ASR/decode. Sau mỗi cảnh đạt, ráp dần trong Flow khi chức năng thực đáp ứng; local dùng kiểm bằng chứng, không mặc định phải dựng local. Agent/reviewer chỉ ghi PASS trong phạm vi năng lực đã thực dùng; thiếu nghe thực cần human checkpoint, không gán agent đã nghe.

Nếu thay tiếng ở phần làm mới, cần owner cho phép đúng scope, giữ K20/D06 và nguyên văn; proposal233 chưa được duyệt. Nếu tách nhịp thay staging214, phải trình ảnh hưởng liên quan, không tự coi user yêu cầu forecast là quyền đổi kịch bản. Không phải tuyển thêm nhiều agent mới; audit211 cho thấy lỗ hổng là chạy/đóng gate trên đúng media và phiên bản.

## 7. Dự báo ngân sách chịu lỗi

Các phép tính là **kịch bản ngân sách chịu lỗi có điều kiện**, không phải tỷ lệ thất bại dự đoán, không cấp quyền chạy và không phải báo giá cho prompt mới. Giả sử mỗi output trong tuyến native đã chọn giá tối đa 7 credit và không cần công đoạn trả phí khác:

| Kịch bản | Số output tính phí | Chi trần | So với 77 |
| --- | ---: | ---: | --- |
| Giữ 7 đơn vị, đạt lượt đầu |7|49|Còn 28; chưa có bằng chứng toàn bộ đạt lần đầu |
|7 đơn vị + 3 output sửa |10|70|Còn 7 |
|7 đơn vị + 4 output sửa |11|77|Hết dự phòng |
|7 đơn vị + 2 output do tách + 2 sửa |11|77|Hết dự phòng |
|7 đơn vị + 2 output do tách + 3 sửa |12|84|Vượt 7 |
|7 đơn vị, mỗi đơn vị phải tạo hai lần tính phí |14|98|Vượt 21 |

Một clip sửa có thể vẫn không đạt. Tách R01/R03/R07–R08 có thể giảm tải cho model nhưng tăng số output và điểm nối; không gọi tách là tối ưu chi đã chứng minh. Thời lượng thực ngắn hơn có thể giảm chi, nhưng chưa khóa timing nên không dùng giá4 làm cam kết. Không dựa vào dailycredits, refund giả định, Quality hoặc chi phí công cụ chưa kiểm để bù thiếu.

**Dự báo toàn phim hiện tại: có đường thực hiện, nhưng mức bảo đảm ngân sách/đạt chuẩn chưa cao.** Sau gói nguồn/nhịp/capability đã kiểm, có thể cập nhật readiness của từng cảnh; vẫn không có cơ sở gắn tỷ lệ phần trăm chính xác trước các output thực tương đương.

Ưu tiên chứng minh nhiệm vụ trên đường găng bằng chính cảnh sản xuất: hoàn thiện brief R01, rồi chuỗi gắp–bị thấy–chữa cháy–nhận món trước khi tiêu nhiều cho cảnh phụ hoặc finishing. Không thử tay riêng/x3; một output rồi QC và điểm nối. Nếu có lỗi trọng yếu, ghi phát hiện cụ thể, nguyên nhân đã xác nhận/giả thuyết và thay đổi nguồn/route cần thiết trước xin quyền sửa; không lặp vài câu cấm hoặc tăng Quality để mong hết lỗi.

## 8. Tổng hợp vòng

- **Đã xác định:** có positive baseline N02, cơ học gắp và chuyển–thả bộ phận; nhiều kết quả không đủ tích hợp toàn cảnh. Proposal233 đánh giá được giá nhưng chưa đủ độ tin cậy đầu ra. Giọng chỉ trên Ingredients là ràng buộc công cụ đã đọc lại.
- **Quyết định đã chốt trước:** giữ script/voice/anchorB/storyboard và no standalone handtest/x3/Quality; chưa nhận approval route/thay tiếng/gói chi233 từ request audit này.
- **Giả định:** trần 7 mỗi native output, 7 đơn vị ban đầu và tái dùng B; không xem ba giả định là số cảnh/số tiền chắc chắn của bản cuối.
- **Còn mở:** nguồn và timing của cảnh tích hợp R04–R09, attribution hai giọng, nối R01/B, phần thay tiếng, khả năng ghép/mix/caption thực của Flow và readiness cuối.
- **Bước tiếp đề xuất:** đóng gói nguồn–nhịp–route cho những cảnh rủi ro, trình bảng readiness và exactquote trước một lượt sản xuất. Không chạy thêm trong lượt234.

Lưu kinh nghiệm trong tài liệu này để tra cứu cùng `learning/01_flow-tool-lessons.md` và `learning/02_root-cause-tracing-protocol.md`. Quy tắc x3 cũ trong learning02 mục3.6 là lịch sử đã bị owner hủy tại228, không hồi sinh để phục vụ audit. Không sửa memory cá nhân hoặc lịch sử approval.
