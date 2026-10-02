# Thử giọng Bắc Khoai — K2/K3/K4

Ngày 2026-10-02. Owner yêu cầu “giọng vùng miền bắc nhé; cứ tạo đi tôi sẽ check cho”. Đã thông báo chọn ba hướng khuyến nghị K2/K3/K4 trước, mỗi hướng ba mẫu Lite, tổng tối đa 90 trong ngân sách thử còn 90. K1/K5 chưa chạy nếu vượt trần; không dùng ngân sách Quality 100 riêng, không mua thêm. Đây là approval tạo mẫu giọng, không duyệt take hoặc đổi kịch bản.

## Phương pháp và đầu vào

Ba request x3; cùng TABLE v0.8 đã duyệt (78), START duy nhất, END trống, Frames/Lite/9:16/720p/8 giây. Hash TABLE `AEB6DFAEE1773109243F9F952235A44F2417C6FB7FB4FAF15BE61C34CA40D924`, kiểm local trước gửi. Không dùng OPEN7 của phép thử khói làm thay đổi nguồn so với V01 cũ. Không chèn câu cấm khói, không nghiên cứu thêm RCA.

Cùng ba trích đoạn của lời Khoai đã duyệt ở 32, ghép riêng để thử sắc thái, không là thứ tự đối thoại hoàn chỉnh của tập. Không tự dùng bản audition làm cảnh chính thức. K2 giọng ấm có nụ cười; K3 ký ức trở về; K4 điềm tĩnh tỉnh bơ. Giọng Bắc tự nhiên, không mô phỏng người thật, không cường điệu địa phương. Thay mô tả diễn giữa ba gói, không giả là voice-ID cố định; Veo có thể thay âm sắc giữa lượt.

## Prompt chung nguyên văn

```text
Locked tripod shot for eight seconds. The adult potato man on screen left speaks to his friend, the adult peach woman on screen right. She listens with a relaxed closed mouth. Both keep their hands resting on the table. Preserve the starting composition and stationary table setting. Quiet street ambience. Only the man speaks, using an original mature warm low male voice with a natural Northern Vietnamese accent, clear Vietnamese tones and conversational diction. Deliver these exact three lines once, in order, with natural brief pauses: "Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ." "Chờ mẹ quay lưng." "Anh gắp cho em mà." This is a voice audition of separate excerpts, not a complete episode scene. Keep every word complete and synchronize only his mouth to his speech.
```

Nối một khoảng trắng rồi đúng một đoạn dưới đây để thành prompt actual; không gửi tiêu đề K2/K3/K4 cho model.

### K2

```text
A restrained smile is audible in the rounded warm voice. Lightly playful, intimate and mature. Gentle rhythmic variation. The smile is subtle, not a laugh; the last line is a quiet amused explanation.
```

### K3

```text
Start matter-of-fact. Soften and slow slightly on "Bếp nhà anh, hồi bé". Let "Mẹ rang gạo" sound warmer as a small childhood memory returns. Reveal quiet mischief on "Chờ mẹ quay lưng" and finish with a restrained smile. The memory is affectionate, not sad or theatrical.
```

### K4

```text
Calm, dry understated humor. Clear compact phrasing and purposeful tiny pauses. Tell the memory naturally. On "Anh gắp cho em mà", remain perfectly composed and casually convincing, as if the excuse is obvious. Warm conversational tone, not a presenter or business briefing.
```

## Kiểm và dừng

Đọc model/START/END/count/ratio/giá/số dư và fallback trước gửi. Không trả video câm để cứu audition. Nếu lỗi server, ghi phí thực và dừng/thử lại chỉ trong tổng trần; không gọi lỗi âm thanh là giọng không đạt. Lưu MP4 native và audio trích lossless để owner nghe. Kỹ thuật/ASR không thay nghe giọng; không tự chọn winner. Nếu lời bị cắt, sai người nói, âm thanh thiếu hoặc giọng không phù hợp, trình rõ mẫu lỗi thay vì normalize/ghép từ để cứu. Chưa nghe thật không tự chứng nhận giọng Bắc/độ ấm/tự nhiên. Visual gate riêng, không cản việc nghe mẫu nhưng chặn dùng làm clip production.

Trạng thái đăng ký: INPUT_SELECTED / NOT_YET_SUBMITTED. Kết quả và phí ghi sau thao tác thực.

## Kết quả thực hiện

Đã gửi ba request Lite x3, mỗi request UI báo 30 credit; cả chín mẫu có kết quả và tải thành công qua nút 720p gốc. Số dư actual 740 → 650, ròng 90. Tổng ngân sách thử đã dùng 400/400; không còn khoản Lite trong trần này. Quality 100 riêng chưa sử dụng. Không retry, không chọn video không âm thanh, không tự chọn winner.

Trạng thái hiện hành: GENERATED / DOWNLOADED / TECHNICAL_DECODE_PASS / OWNER_LISTENING_PENDING. Bản đăng ký phía trên là lịch sử trước submit. [Manifest, gói nghe và các gate còn mở — 143](143_voice-audition-owner-listening-packet.md).
