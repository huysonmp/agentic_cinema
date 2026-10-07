# REC228 — Brief sản xuất R01, chưa phải request sẵn sàng gửi

Mục đích: footage dùng cho phần mở phim, không bài thử tay độc lập. Một output cho request sản xuất được chốt; không x3/retry tự phát. Giữ C-v0.6, Khoai K20/Orus, Đào D06/Aoede, chuẩn hình N02 B và F0.

## Lời và diễn bắt buộc

1. Đào nói đúng “Anh nhìn mãi. Không hợp thì để em.” với mặt/miệng Đào nhìn rõ. Khoai nghe, không nói thay. Đào có ý định lấy đĩa, tay ngoài bên phải hình tiến nhẹ về vành đĩa quanh ngoài bát; chưa chuyển đĩa/món.
2. Khoai nói “Khoan.” đúng một lần bằng tiếng nguồn N02 B. Thấy mặt/miệng Khoai đang nói. Đào nghe rồi mới dừng động tác; không nói hoặc nhép câu của anh.
3. Sau cue dừng mới trở về pose tay nghỉ phù hợp cảnh ký ức N02. Không reset tay bằng jump-cut thiếu nguyên nhân. Nếu diễn cùng câu kế cần đo thời gian thực; không bịa mốc từ/cut.

## Nguồn và vai trò

- S v01: trạng thái tay nghỉ/nhận diện/khung mở.
- M v03: mid-pose ý định, không phải khung END nghỉ; đã owner duyệt ảnh tĩnh.
- E v02: đích thu tay, chỉ ứng viên ảnh đã kiểm, không chứng minh cô nghe “Khoan”.
- N01 audio: excerpt từ180A03 [0;2,15) theo manifest202/approval203. Giữ provenance; tên diagnostic UNVERIFIED không tự phủ định approval203, nhưng điểm cắt còn phải kiểm nghe/AV.
- N02 B native: `660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535`, owner222 đã chấp nhận. Không tự thay bằng source200 hoặc thu lại.

## Điểm chưa chốt, không được giấu trong prompt

M v03 còn tay vươn, B frame0 tay nghỉ. Giữ toàn picture B từ frame0 đồng thời chứng minh dừng rồi thu tay theo “Khoan” chưa có lời giải kiểm được. Cần owner chốt phạm vi đổi coverage đầu N02: đề xuất chỉ xử lý hình quanh “Khoan”, giữ nguyên tiếng B và phần ký ức phía sau. Không sửa native gốc; dựng thành phiên bản mới, kiểm lại cảnh mở và điểm nối.

Tuyến ưu tiên dự kiến: sửa hình từ thành phần video mang tiếng đúng, như tuyến Omni từng dùng cho N02; còn phải kiểm input support, duration, quote live và output speaker/voice. Không mặc định Lite nhận hoặc giữ nguyên WAV hay giọng từ tên preset. Không chồng lời lên cả hai miệng khép và gọi sync đạt. Nếu route không giữ tiếng/khẩu hình thì báo blocker, không chuyển công cụ/voice hoặc trả phí thêm để thử ngẫu nhiên.

Chưa có timestamp từ “Khoan” trong B được khóa, chưa input composite, chưa upload/sinh hoặc quote request này. Brief này không là media PASS hoặc final prompt executable.

## QC đầu ra sản xuất

Kiểm đúng native/hash/decode; xem frame/timecode tay qua bát/đũa/ly, dừng sau cue, thu tay và join. Đối soát đủ mặt, đúng người nói/người nghe, lời/voice thật và khẩu hình; audio-only metric/ASR không thay nghe. Món lạnh không khói, bộ phục vụ/đĩa/F0 giữ. Chỉ chọn range dùng được sau review, không chấp nhận toàn clip vì đã chi tiền. Sai thì ghi lỗi và khả năng sửa local; lượt trả phí sửa không tự được cấp.
