# EP01 — U06: đưa bát Đào vào và chuyển hướng miếng nem

Ngày 2026-10-06. Owner “ok” sau bản ráp hình205 và đề nghị tiếp tục U06. Giữ C-v0.6, tiếng202, phản ứng15 frame đã duyệt205; không suy “ok” thành nghiệm thu phim cuối hoặc cho thêm ngân sách.

## Mục tiêu và nguồn đầu vào

Tiếp sau U04 đang giữ một miếng nem chưa ăn. Bát riêng của Khoai vẫn rỗng trên bàn. Đào đưa **bát riêng thứ hai** vào từ phía phải, đỡ ở vành ngoài; Khoai chuyển cùng miếng nem sang ngay trên lòng bát Đào, chưa thả. Không biến bát Khoai thành bát Đào, không cho tay Khoai cầm bát, không lấy thêm miếng hoặc đút vào miệng.

START duy nhất: native U04 frame143, `C:/Users/PC/Downloads/du_an_nem_bui/205_u04_production/U04_OUT_frame143.png`, SHA256 `2fcdb78f592c1e4ee25cfb5c571d8beb70eb99c465a717f6e9211bcb5b9a070e`, 720×1280. Root xem lại ảnh và hash; cùng camera/miếng nem/tay/bộ bàn với điểm ra U04. END189 chỉ tham khảo động tác, không upload: khung rộng và vị trí bát/đĩa/rau khác, không ép model đổi bố cục theo ảnh đó.

Trong khung cận hiện hành, Đào và bát của chị ngoài mép phải; bát đi vào vùng trước tay nghỉ của Khoai, hai bát phải còn phân biệt được. Tay nhỏ của Đào có da đào hồng, tay áo kem; bàn tay lớn vàng khoai đang nghỉ giữ nguyên. Đây là giả định dàn cảnh để thực hiện trong góc đã có, cần kiểm đầu ra; chưa có ảnh hoặc video chứng minh bát xuất hiện đúng. Mặt vẫn ngoài khung, không cần thêm giọng/lipsync.

Chỉ đạo: khoảng0–0,9s đưa bát vào; khoảng0,9–1,9s đổi hướng đũa; giữ phần nem chưa thả sau đó. S08 đích frame590–647, cần2,375s chuyển động sử dụng được; thời điểm actual quyết định range và endpoint U07, không giả video sẽ tuân đúng mốc prompt. Bát Đào là bát đã có trong OPEN7, không bát thứ ba hoặc vật thể tự xuất hiện ở giữa khung.

## Preflight và ngân sách

Một Lite/Frames/9:16/720p/8s/x1 trong gói198; kiểm trực tiếp model/quote/nguồn/prompt trước gửi. Không END tái tạo, audio reference hoặc lời thoại. AAC nếu có không dùng cho thoại202. Giữ watermark.

Trước lượt: đã chi359/trần422/còn63. Nếu quote và debit10: chi369/còn53; năm đơn vị U01/U02/U03/U07/U08 dự kiến50, dự phòng3. Không tự chi sửa10 từ ngân sách earmark cảnh khác. Nếu U06 không đủ hành động/range an toàn, ghi ngoại lệ và trình phương án không trả phí hoặc điều chỉnh kế hoạch; không tự sinh lần nữa.

## Kiểm đầu ra bắt buộc

Nhận native/hash/probe/decode. Kiểm điểm vào với U04, đường bát đi vào, phân biệt hai tay/hai bát, phần nem giữ nguyên trên tips và chưa thả, đũa đúng chiều, mặt ngoài khung, rau/chấm cùng bàn, nem lạnh không hơi nóng. Chỉ chọn đoạn actual kiểm được, giữ tiếng202 ngoài hình, không freeze/loop/slowdown để giả đạt timing. U07 phải dùng frame ra thực của U06 được chọn, không ảnh hướng dẫn189.

## Thực thi và kết quả — REWORK

Đã gửi đúng một lượt sau preflight: Lite, Frames, dọc9:16,720p,8s,x1, quote10. Prompt được đọc lại và so khớp với [file thực gửi](evidence/206/prompt-U06.txt); START đúng hash nêu trên, không END. Agent checkbox0. Account117→107, debit10; sổ **369/422, còn53**. Không gửi lại hoặc nâng Quality.

Flow tạo `Person placing bowl on table`, media `b20d33ce-098d-4805-b80c-48d7d0ded4cf`. Đã tải một lần bằng menu720p kích thước gốc. Download-event timeout20s nhưng UI báo đã tải; file thật tồn tại, không bấm tải lần hai. Nguồn `C:/Users/PC/Downloads/Person_placing_bowl_on_table_20261006134124.mp4` và bản lưu `C:/Users/PC/Downloads/du_an_nem_bui/206_u06_production/U06_NATIVE.mp4` cùng SHA256 `e6df660be02f7b723e6b20a39a21876b164eefb22fc6b4bd7a9f3a1243d22926`.

Native H264720×1280/24fps,192frame/8s, có AAC48kHz stereo; full decode exit0. AAC không dùng, không kết luận đã tắt sinh âm thanh. Bản xem riêng57frame/2,375s không tiếng có SHA256 `04b75eabd5a206207c8cdbca9e96fe9f01a03f0dab5e5b5217462f31fc4ab105`, tên `U06_FIRST57_REVIEW_REWORK_NOT_FOR_TIMELINE.mp4`. Đây là file chẩn đoán, không ứng viên đã duyệt.

Root xem toàn57frame đầu trong contact sheet và48 mẫu/8s; xem thêm native frame35,56,191 ở khung lớn. Chưa chạy agent phản biện độc lập hoặc kiểm AV.

- Bát riêng Khoai còn ở giữa bàn; Đào đưa bát thứ hai từ phải vào, còn thấy ở frame35/1,4583s.
- Khoai giữ miếng nem trên đũa nhưng **không chuyển sang trên lòng bát Đào** trong đoạn yêu cầu hoặc48 mẫu toàn clip. Không đủ hành động chữa cháy.
- Bát Đào không còn thấy ở frame56/2,3333s dù tay còn trong vùng hình; REWORK về tồn tại vật thể. Chưa xác định từ ảnh liệu bát bị model làm biến mất hay đi khỏi khung theo quỹ đạo thiếu liên tục; không kết luận nguyên nhân nội bộ model.
- Có thêm tay Đào ở tiền cảnh gần đĩa; chưa đủ bằng chứng duyệt giải phẫu/grip/continuity toàn cảnh. Không tự báo FOOD hoặc ACT PASS. Các mẫu không thấy hơi nóng rõ; không suy từ đó thành FOOD toàn tập PASS.

**Không đưa U06 vào timeline205-v0.3, không xuất bản ráp11,5s như đã đạt; chưa có START U07 được duyệt.** Giữ nguyên tiếng202 và các range205 hiện hành.

## Điểm cần chốt và phương án tiếp theo

Khuyến nghị **tách lại trách nhiệm hành động trong hai slot đã có**, không tăng số lượt: S08 dùng đoạn đưa bát vào khoảng0–1,5s (36frame, còn là đề xuất); chuyển21frame còn lại sang S09. S09 trở thành2,4167s/58frame để U07 chuyển cùng miếng nem sang bát Đào rồi thả. Tổng S08+S09 vẫn94frame/3,9167s, khối thoại202 và phim30s không đổi. Endpoint đề xuất là native U06 frame35, [ảnh kiểm](evidence/206/PROPOSED_U07_START_frame35_NOT_APPROVED.png), không native end8s. Cần kiểm từng frame đoạn36frame, nối U04 và tiền cảnh tay trước khi coi là usable.

U07 dự kiến vẫn **một** lượt10 trong50 earmark còn lại; U01/U02/U03/U08 dự kiến40, dự phòng3. Đây là thay đổi đạo diễn/phân bố hành động, **chờ owner chốt**, chưa sửa timeline hoặc gửi U07. Thành công không được bảo đảm; nếu U07 cũng hỏng sẽ ghi ngoại lệ, không tự tiêu thêm10 từ3 dự phòng hoặc đổi credit dành cảnh khác.

Phương án khác: giữ U07 chỉ-thả theo thiết kế cũ và xin sửa U06 riêng; cần thêm quyền chi/điều chỉnh earmark trước khi gửi. Không đề xuất lúc này vì thiếu53 cho cả sửa10 và năm lượt50. Không bỏ động tác gắp cho Đào hoặc đổi ý nghĩa lời N06 để che thiếu coverage.

## Kinh nghiệm công cụ và kiểm nguồn lỗi

Prompt đã tách thứ tự đưa bát→chuyển đũa→giữ, nhưng vẫn chứa hai chủ thể chuyển động và nhiều khóa vật thể trên START không có bát Đào. Đầu ra thực hiện bước đầu, bỏ bước hai và mất bát; đây là quan sát, **giả thuyết** là tải nhiều hành động/khóa không tương thích khiến model ưu tiên giữ pose Khoai. Chưa thử đối chứng nên không gắn nhãn nguyên nhân gốc đã chứng minh. Lần tiếp theo phải kiểm từng trạng thái hành động/vật thể trước khi dùng làm nguồn scene kế; tránh coi “video tạo xong” là “cảnh đạt”.

Tải: timeout sự kiện không đồng nghĩa download thất bại. Đối chiếu toast, tên file mới, thời gian, byte/hash/probe/decode trước retry. Xuất range theo `trim=end_frame=57` và encode, không stream-copy `-t` vì kinh nghiệm205 về B-frame thừa frame.

Áp dụng skill computer-use (đã đọc đầy đủ): thao tác qua browser được hỗ trợ, kiểm trạng thái/cấu hình trước submit, tải bằng menu native và lưu [bằng chứng Flow](evidence/206/flow-completed.png) không panel tài khoản. Ghi root QC, không giả agent đã chạy. Chưa AV/master PASS, Quality hoặc phát hành.
