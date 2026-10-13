# REC294 — Đổi thiết kế điều khiển hành động trước khi chạy tiếp

13-10-2026. Owner phản đối hành động trả nem về đĩa chung và yêu cầu tiếp tục. **CHẨN ĐOÁN + PHƯƠNG ÁN CHỜ CHỐT; KHÔNG VIDEO/ẢNH/EDL MỚI.** Native REC293 giữ không chọn, request7 đã dùng. Không suy yêu cầu tiếp tục thành quyền thử thêm.

## 1. Trách nhiệm ở gói triển khai, không chỉ ở model

Kịch bản đúng: Khoai chữa cháy “Anh gắp cho em mà”, rồi thực sự cho Đào. Không có beat nào trả A về đĩa chung. Prompt REC292 đã ghi đích bát Đào/chưa thả/tay trong nghỉ; actual REC293 vẫn đi về đĩa và cuối tips trống. Như vậy không thể chỉ giải thích rằng tôi quên chữ “không thả”, hoặc thêm nhiều câu cấm là khắc phục đủ.

Lỗ hổng quy trình đã xác định: dùng ảnh đầu kiểu reference + chữ để yêu cầu một chuyển động trọng yếu nhưng **chưa có chứng cứ điều khiển được entry/đích/đường đi**. Preflight giấy xác nhận prompt đúng ý không chứng minh công cụ thực hiện được. Local composite đã bảo toàn ảnh đầu, không khóa hành động video. Đây là khoảng trống kiểm soát; chưa chứng minh một từ khóa, model hoặc độ dài prompt là nguyên nhân duy nhất.

Giả thuyết cần kiểm, không kết luận thực nghiệm: Đào bị yêu cầu giữ bát cố định và không nhận trong C06, nên tín hiệu tương tác hướng tới người nhận chưa rõ; tay diễn/đũa được model diễn giải theo bữa ăn thông thường. Đĩa chung nổi bật không tự chứng minh nguyên nhân gây chọn sai đích.

## 2. Không hứa tổ hợp tính năng không hỗ trợ

Đã đọc lại bài học REC278 và kiểm nguồn Google ngày13-10-2026:

- [Create videos in Google Flow](https://support.google.com/flow/answer/16353334?hl=en): Frames nhận ảnh đầu/cuối; voice references chỉ dùng được với video Ingredients, các kiểu generation khác sẽ lỗi.
- [Models and supported features](https://support.google.com/flow/answer/16352836?hl=en): Omni Flash1.1 hỗ trợ từng tuyến Frames/Ingredients, nhưng danh sách từng tính năng không chứng minh chúng dùng chung một request.

Vì vậy **không** lập kế hoạch “Start+End khóa hình cùng saved K20/D06 trong một request” như khả năng đã có. Vòng này kiểm tài liệu primary hiện hành, **không vào UI hoặc chạy một tổ hợp sai để thử**. Khả năng giữ giữa hai endpoint, camera và chuyển động vẫn phải kiểm actual, kể cả nếu dùng Frames. Không nâng Quality để sửa nghĩa hành động.

## 3. Khuyến nghị nghệ thuật–kỹ thuật: tách lời khỏi chuyển đũa xa, không tách câu chuyện

**Phương án A — khuyến nghị, chờ owner:**

| Nhịp kể | Trạng thái/chuyển động được thiết kế | Voice và điểm cắt |
| --- | --- | --- |
| **C06: lời chữa cháy** | Khoai giữ cùng A phía mình; bình thản nói, mắt chú ý Đào, nét B. Không phát triển đường chuyển dài hoặc hạ A. Đầu/thân vẫn có độ sống, không freeze | Một K20, đúng N06. Đo range đủ âm cuối và nét diễn; không bắt dùng trọn4s hoặc57F |
| **Nhịp nhận REC281: Đào làm rõ đích** | Đào dùng tay rảnh đưa **bát riêng** vào vùng nhận cạnh A; cốc tay ngoài vẫn nâng. Khoai giữ A đến khi bát đã vào vị trí | Đào nói đúng N07/D06, Khoai im miệng. Hai mặt và bát/đũa phải thấy; không voice chạy trên cận món |
| **Cho vào bát, chứng thực cái cớ** | Từ trạng thái bát đã ở vùng nhận, Khoai hạ A quãng ngắn vào lòng bát Đào, nhả một lần, rút đũa. Không mới gắp/đút miệng/đổi tay/cốc vào bát | Có thể hoàn tất liền với nhịp trên nếu actual đạt, hoặc cắt sang khoảng hành động không thoại. Không bắt ba clip riêng; không tự cắt lời để chia |

**Thay đổi phải công bố:** C06 không còn chuyển A sau “mà”; động tác ấy chuyển sang nhịp nhận, sau khi Đào đưa bát. Đây thay ranh giới đã duyệt REC276/290, **không** được gọi là chỉ sửa prompt. Không tự thu hồi đoạn nguồn REC276; nếu chốt A thì chỉ áp dụng cho thiết kế mới.

Tinh thần chuyện/sắc thái B/lời/canon/voice và C09 giữ. Khoai vẫn biến cái cớ thành thật; Đào có hành động đời thường chủ động, không thành thao tác kiểm món. Đây là thay choreography để đích vật lý rõ hơn, không rút bớt vị trí chuyên môn hoặc đổi mục tiêu chất lượng.

## 4. Vì sao chưa chốt số take/route toàn nhịp nhận

Frames phù hợp xem xét cho **khoảng hành động không thoại**, không cho savedvoice trực tiếp. Ingredients phù hợp cho lời với preset nhưng không phải exactF0. Nếu N07 chưa xong mà đã đổi clip hành động, không tự đưa tiếng D06 lên mặt không khớp; phải có trọn lượt Đào nói với khẩu hình trước điểm cắt hoặc chốt phương án khác.

Trước bất kỳ trả phí nào, gói nhịp nhận cần một bảng vị trí tay–A–bát–cốc và ảnh đầu/đích thực đã QC. Muốn sinh ảnh mới hoặc composite thay pose nhân vật, phải chốt phạm vi; quyền REC291 chỉ sửa món, không tự cho di chuyển tay/bát/đũa. Endpoint không phải bằng chứng middle frames đạt. Nếu UI cần upload/route khác, kiểm tổ hợp tài nguyên live, quote và bound request riêng trước submit.

Không tự mute/revoice/preset mới/API/cài công cụ. Tách thao tác hình và thoại không đồng nghĩa tiếng ghép sẽ sync. Công cụ có sẵn chỉ giúp kiểm/biên tập trong phạm vi được phép, không thay owner approval.

## 5. Phương án khác và hệ quả

- **B — giữ choreography C06 chuyển trước, Đào nhận sau:** bảo toàn ranh giới đang duyệt nhưng cần cơ chế kiểm soát đích thực hoặc sửa video có bảo toàn giọng được chứng minh. Không chọn cách chỉ thêm nhiều negative prompt rồi gửi lại; chưa có gói khả thi đã kiểm.
- **C — rà khả năng dùng đoạn đầu REC293:** không chi thêm generation trước khi biết có salvage. Nhưng entry nhìn thẳng/tay phụ đã lệch, thiếu nghe/diễn; chưa chọn range. Cắt trước thả chỉ loại tail, **không tự chữa entry, động tác hoặc sắc thái**. Nếu muốn tái sử dụng cần scoped diagnostic, kiểm actual và owner quyết định đúng đoạn.

Khuyến nghị A vì giảm nhu cầu điều khiển một đường chuyển dài trong lượt nói, làm người nhận và đích hiện rõ trước thả. **Không báo xác suất đạt cao hoặc cam kết tiết kiệm credit:** chưa có output của choreography mới để đo. B giữ nguyên nhưng chưa có cơ chế mới; C chỉ khả năng, không thành lựa chọn mặc định.

Không đặt điều kiện bất khả thi “phải chứng minh video mới chắc đạt trước khi sinh”. Việc trước trả phí là xác minh tổ hợp tính năng, đúng vai tài nguyên, đích nhận và điểm cắt, giảm rủi ro có thể tránh. Nếu vẫn cần một lượt kiểm thực nghiệm có trả phí, trình đúng giả thuyết/cap và điều kiện dừng; kết quả sinh mới trả lời phần chuyển động chưa biết.

## 6. Trình tự và gates sau khi owner chọn

Phản biện PAPER độc lập đã hoàn tất và root đọc toàn bộ [báo cáo](restart_720p_v1/06_qc/action_control_recovery_independent_294.md): A hợp lý để trình đúng một quyết định ranh giới, chưa control/physics/voice/AV PASS. Reviewer nhấn mạnh vị trí bát–A–cốc–đĩa chung và phải trọn N07 trước khi tách sang hành động không thoại; không cấp quyền chỉnh pose hoặc trả phí từ paper.

1. Chốt đúng một quyết định về ranh giới hành động A/B/C; ghi authority. Không hỏi lại sắc thái B hoặc tuyển giọng.
2. Với A, cụ thể hóa nhịp nhận cùng ảnh/cơ chế control phù hợp; C06 chỉ thoại, giữA. Chốt phạm vi ảnh/pose mới cần tạo, không dùng END sau nhận làm START trước nhận.
3. Maker/đạo diễn kiểm toàn nhịp trước–sau, không tạo riêng một món/đũa rồi gọi whole-scene ready; phản biện kiểm recipient/food/voice/timing.
4. Gói live nêu exact tài nguyên/route/giá, rủi ro chưa đóng, điều kiện dừng và bound request; owner duyệt trước paid.
5. Actual: full-frame screen + playback diễn/giọng/sync + trajectory/recipient + điểm nối. Chỉ thả trong bát Đào; wrong-target/release hoặc thiếu lời là không chọn. Không lấy still/paper/ASR thay actual.

Timing chưa đủ final30: theo range cũ trước C06 là632F/24fps; C06 mớiN, phần kết mục tiêu30 còn88−N. Phải đo cả nhận/N07/C09 và trình thay range nếu cần, không bỏC09/nhanh giọng/rút lời hoặc tự nới mục tiêu. Proposal A không tự giải quyết food các cảnh trước.

**Đã xác định:** lỗi control request293, compatibility Frames/voice kiểm lại. **Đã chốt từ trước:** sắc thái B, N06/K20, N07/D06 và mục tiêu cho Đào. **Giả định:** đưa bát vào vùng nhận giúp đích rõ hơn, chưa thử. **Còn mở:** owner chọn ranh giới mới, ảnh/control/route/timing/paid. **Bước tiếp:** owner chốt A/B/C rồi chuẩn đúng gói, không chạy tiếp từ quyền7 đã dùng.

Chi mới0; sổ **244/500**, còn **256**, retake **19**, dự phòng **110** đóng. Không browser action, media edit, voice/source/EDL replacement hoặc release trong REC294.
