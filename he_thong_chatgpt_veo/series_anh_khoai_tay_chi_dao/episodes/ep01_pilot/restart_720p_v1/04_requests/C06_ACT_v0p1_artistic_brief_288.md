# C06_ACT v0.1 — Khoai chữa cháy kín

REC288, ngày 13-10-2026. **BRIEF NGHỆ THUẬT ĐỂ RÀ VÀ CHỐT — KHÔNG PHẢI PROMPT ĐÃ SẴN SÀNG CHẠY.** Hướng “hơi chững → giữ bình thản trả lời → chuyển đũa” đã được owner duyệt cho việc cụ thể hóa. Chi tiết dưới đây là bản triển khai đề xuất, chưa có video chứng minh đạt.

## 1. Đích diễn: người đang tự cứu một cái cớ nhỏ

Khoai biết Đào đã thấy anh định lấy phần cho mình. Đào biết, và anh cũng biết cô biết. Anh giữ thể diện bằng một câu chữa cháy rất bình thường, rồi chuyển phần đang cầm về phía cô để làm cái cớ ấy có vẻ hợp lý. Chất hài nằm ở khoảng cách giữa ý định thật và hành động chữa cháy, không nằm ở cười lớn hoặc làm mặt hài.

Hơi ngượng nhưng không sợ, không xin lỗi, không thuyết trình món ăn. Giữ chất trưởng thành, trầm, có hài hước kín của Khoai. Hai người là bạn; không thêm diễn tình tứ hoặc câu chuyện công việc.

**Câu duy nhất, không đổi:** “Anh gắp cho em mà.” Giọng định hướng K20/Orus đã chọn; nhẹ, chắc, thân mật như tìm một cái cớ ngay lúc bị phát hiện. Brief không cho tạo preset mới hoặc tự nhận output sau sẽ giữ nguyên tiếng/khẩu hình.

## 2. Ba nhịp liên kết

| Nhịp | Điều Khoai đang cố làm | Mắt–mặt | Đầu–thân và nối sang hành động |
| --- | --- | --- | --- |
| **1. Hơi chững** | Tiếp nhận việc mình đã bị bắt, chọn cách giữ bình tĩnh | Giữ chú ý ở Đào; một thoáng căng nhỏ quanh mắt/mày. Môi đang khép trước lượt nói | Giữ tư thế đang có, không cứng khóa người. Một thay đổi rất nhỏ trong cách giữ đầu/vai giúp đọc được sự tự kiềm lại; tay vẫn kẹp cùng phần A |
| **2. Trả lời bình thản** | Nói cái cớ như một chuyện thường ngày, chờ xem Đào có chịu nhận không | Ánh mắt tiếp tục có đối tượng; miệng phát âm tự nhiên, không thêm nụ cười chào mời. Mày/mắt giữ cùng ý định hơi ngượng, không diễn vòng ngạc nhiên→hân hoan | Chuyển từ hơi gồng sang ổn định một cách liền mạch. Cue ưu tiên là **cằm ổn định/hạ rất nhẹ theo ý định tự trấn tĩnh**, không gật theo từng chữ. Vai/ngực có độ sống tự nhiên, không buộc đồng thời hạ cằm + nhún vai + nghiêng thân |
| **3. Chuyển đũa để chứng thực cái cớ** | Dùng động tác cho Đào như thể đó vốn là ý định của mình | Sau âm cuối “mà”, miệng kết câu tự nhiên; nét mặt còn kín, có thể một chút ngượng chứ không nở cười đắc ý. Ánh nhìn theo quan hệ với Đào và vùng nhận khi cần | Bắt đầu chuyển cùng phần A về phía bát Đào theo ranh giới hành động đang giữ. Đầu/thân hỗ trợ rất nhỏ cho cánh tay, không thành cú xoay/vươn toàn người. C06 có thể ra **đang chuyển động**, không đặt thêm đoạn dừng/giữ bắt buộc |

Ba nhịp là một ý định liên tục, không phải ba tư thế để mô hình lần lượt trình diễn. “Hơi chững” là độ căng tiếp nối từ cảnh trước, không một nhịp ngạc nhiên mới hoặc khoảng lặng dài để diễn lại việc bị phát hiện. Không mặc định phải có đủ từng cử động nêu trong bảng; chỉ dẫn nhỏ phục vụ ý định, không phải danh sách bắt gật/nhún/chớp.

## 3. Nhịp thời gian — theo lời và chuyển lượt, chưa khóa số giây

- Đầu C06 kế thừa trạng thái **đã bị bắt** ở cuối C05 “Chờ em quay lưng nữa à?”. Không quay đầu phát hiện Đào lại, không reset tay về ngực hoặc đổi phần A.
- Lời bắt đầu trước chuyển tay. Sau khi nói trọn âm cuối “mà” mới bắt đầu chuyển A; không thêm nhìn món/ho/ngập ngừng hoặc chờ lâu giữa câu và động tác.
- Kết C06 đang chuyển cùng A nhưng **chưa thả**. Điểm cắt và trạng thái tay/bát/cốc phải đo trên take thực; giữ tinh thần cut-on-motion đã duyệt, không áp endpoint stop-and-hold cũ.
- Nhịp Đào đưa bát/nói N07 và Khoai bỏ A vào bát thuộc brief REC281 tiếp sau. C09/B giữ nguyên hướng đã chốt; không đưa vào C06 để bù timing.
- Không ấn định 0,2/0,5 giây, không ép đoạn 57 khung của nguồn hoặc khung F66 của bản nối lên take mới. Thời lượng/lời/âm cuối phải đo, rồi trình tác động đến mục tiêu 30 giây và trần bản dựng nháp 35 giây trước khi thay EDL. Các giới hạn thời lượng cũ chưa được tự nới.

## 4. Bất biến và quyền thay đổi

**Được thiết kế lại trong đề nghị diễn:** mức căng mắt/mày, ý định ánh nhìn, độ ổn định của đầu/cằm/vai/ngực, sự liên kết của chúng với lượt nói và chuyển tay. Không yêu cầu sao y toàn bộ chuyển động mặt–thân của nguồn rồi đồng thời yêu cầu nó có chất diễn khác.

**Phải giữ:** lời N06; hướng giọng K20; nhận diện/trang phục đã duyệt; quán nhỏ ven phố/bàn/ánh sáng; mặt cả hai và vùng đũa/bát đủ thấy; cùng phần A đã gắp; một đôi đũa của Khoai trong tay ngoài; bát riêng của Đào còn rỗng trước nhận; cốc ở tay ngoài Đào, không đặt vào bát; rau/lá, nước chấm và bát đúng bối cảnh. Phần A và đĩa phải theo chất liệu nem đã duyệt, không khói hoặc lát đặc đồng dạng.

Tay trong của Khoai vẫn nghỉ; Đào nghe, không thêm lượt nói hay động tác uống. “Tay nghỉ/cốc giữ” không được biến thành khóa bất động đầu/thân của Khoai. Không tự tăng độ khó bằng thêm nhún vai, cười, xoay người, nghiêng sát Đào hoặc gắp lần nữa.

Nguồn REC276 vẫn giữ phê duyệt riêng đã có; không nói owner đã bác đích danh nguồn. Take REC286 vẫn không chọn vì lỗi ngoài phạm vi và phản hồi diễn xuất của owner. Ảnh START/END REC283 chỉ được duyệt về ảnh/vật liệu/tư thế, không thay phê duyệt diễn xuất hoặc dùng END nhận–bỏ làm đích cho C06.

## 5. Cách chấm ACT/PERF trên kết quả sau này

### Cần đọc được khi xem chuỗi

1. Khoai nghe và nhận ra mình đã bị bắt **một lần**; trạng thái đó có mặt trước khi nói, không reset thành người vui vẻ giới thiệu món.
2. Câu nói nghe/nhìn như một lời chữa cháy kín. Mắt–đầu–thân cùng giữ bình tĩnh, không chỉ miệng đổi hình trên một thân người giữ nguyên tư thế.
3. Phát âm còn tự nhiên. Miệng mở/lộ răng/chớp mắt không tự là lỗi; xét toàn câu cùng mày/mắt/thân, không cấm lộ răng hoặc khóa môi bất động để “tiết chế”.
4. Chuyển từ nói sang đưa A là hành động có lý do, không một động tác xuất hiện tách rời hoặc đột ngột bắt đầu lại. Phải giữ cùng A, chưa vào miệng hoặc thả trước nhịp nhận.
5. Tiết chế không đồng nghĩa đứng im; sinh động không đồng nghĩa nhiều chuyển động. Nhân vật có thể rất ít cử động nếu ý định vẫn đọc được. Không chấm số lần chớp/gật hoặc lấy điểm props bù cảm giác diễn chưa đạt.

### Bằng chứng kiểm, không nhận bằng giấy

- DIR/ACT đánh giá khả năng đọc ý định khi xem chuỗi không tiếng; SIA/AV và owner kiểm trên **bản có tiếng** để xét câu–giọng–nhịp–khẩu hình. Silent compare chỉ là dẫn xuất QA, không bằng chứng đã nghe hoặc sync.
- Reviewer chỉ xem chuỗi ảnh dày thì ghi đúng phạm vi đó; phải giao bước kiểm phát video thực khi chưa có khả năng xem liên tục. Kiểm kỹ thuật/giải mã/ASR/hash không cấp kết luận diễn xuất đạt.
- Mỗi finding gắn target hash, moment/frame, expected/observed, scope và severity. Lộ răng ở một âm không tự thành “cười sai”; vòng cảm xúc mới/khóa thân/rõ diễn mời ăn cần kiểm bằng chuỗi.
- So điểm vào C05→C06 và điểm ra nhận–bỏ với clip thực kế cận; không nhìn C06 riêng rồi chốt continuity toàn phim.
- Nếu lệch mặt/trang phục/bối cảnh/món/props/speaker hoặc diễn không đọc đúng ý định, không chọn. Không che mặt bằng cận đĩa, tự cắt lời, mute/revoice, tăng tốc hay dùng Quality như cách sửa ý nghĩa.

## 6. Chuyển brief sang kỹ thuật — việc kế tiếp, chưa thực hiện

Đích mới có **thay đổi diễn**, nên không đóng gói như food-only edit với lệnh “preserve every expression/movement”. CTD/PROMPT cần chọn phạm vi C06 hay chuỗi rộng hơn, nguồn/ảnh/voice, phương thức tạo hoặc sửa, cấu hình/giá live, timing/continuity và giả thuyết kiểm trước đề nghị trả phí. Không coi giữ K20 blueprint là chắc giữ tiếng trên take mới.

Phải đánh giá đồng thời cổng kiểm hình món đang mở và phần mặt–thân mới. Không chọn phương thức chỉ vì trước có đầu ra 720p; REC286 đã chứng minh đầu ra có thể đổi vùng ngoài yêu cầu. Không tự viết prompt cuối/đổi ảnh tham chiếu, làm script/composite hoặc chạy lại từ brief này.

**Trạng thái cuối:** hướng nghệ thuật đã duyệt; bản chi tiết v0.1 chờ rà và owner chốt; gói thực thi/phương thức/thời lượng/đề nghị ngân sách chưa có. Chi mới 0; sổ 237/500, còn 263 credit; phần tạo lại còn 26, dự phòng 110 đang đóng.
