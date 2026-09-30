# EP01/P5 — Language quality diagnosis v0.1

- **Status:** `LANGUAGE_REWORK_REQUIRED`.
- **Scope:** P5-A01 và P5-B01; đây là chẩn đoán trước khi timed read, không phải bản sửa cuối.
- **Finding:** cả hai draft có nhiều câu đúng ý nghiên cứu nhưng nghe như diễn giải brief hoặc chú thích kiểm chứng, chưa phải thoại tự nhiên của Khoai–Đào.

## Lỗi cụ thể

| Draft line | Lỗi | Vì sao chưa đạt | Hướng sửa, chưa khóa câu cuối |
|---|---|---|---|
| “Một hạt gạo mà dẫn tới món này à?” | Mở chung chung | Không tạo được hình dung quan hệ giữa hạt gạo và món; nghe như câu hỏi minh họa | Cho Đào phản ứng vào một vật/hành động cụ thể, ngắn và có sắc thái tò mò |
| “Khoan gắn nó lên miếng nem. Mình đang lần theo một chi tiết thôi.” | Translation-like / abstract | Người thật ít nói “lần theo một chi tiết” trong tình huống này; Khoai nghe như điều phối nghiên cứu | Để Khoai ngăn một hành động cụ thể rồi nói bằng câu ngắn, có khẩu khí kỹ tính |
| “Rang rồi thành thính?” | Fact/timing risk | Câu hỏi này làm công thức nghe như điều chắc chắn, trong khi F02 chỉ cho phép diễn đạt hẹp | Đổi thành câu hỏi về cue minh họa, hoặc để Khoai nói qualifier tự nhiên hơn |
| “Trong các cách làm được mô tả…” | Report prose | Đây là văn phong báo cáo, không phải lời nói của một nhân vật 30 giây | Giữ qualifier trong câu nói đời thường mà không làm claim mạnh hơn; Fact Auditor phải read-back |
| “Vậy mình không bắt món kể hết trong một cái nhìn.” | Abstract/slogan risk | Gán ý niệm “món kể” khá văn vẻ, không gắn với hành động cụ thể | Cho Đào nói điều cô vừa làm/nhìn thấy, rồi để hình mang phần trừu tượng |
| “Một món, thêm một lớp để tò mò.” | Slogan | Không có chủ thể và dư vị cụ thể; dễ nghe như tagline | Kết bằng phản ứng hoặc lựa chọn nhỏ của hai người quanh món |
| “Cận thế này đẹp, nhưng ảnh không tự chứng minh thính.” | Awkward collocation | “Chứng minh thính” không phải kết hợp từ tự nhiên; câu kéo người xem vào bài giảng phương pháp | Khoai nói rõ mình không dám kết luận từ cận cảnh, bằng từ vựng đời thường hơn |
| “Vậy tớ không lấy cận cảnh làm kết luận.” | Translation-like | “Lấy cận cảnh làm kết luận” là khái niệm, không phải khẩu ngữ | Nói trực tiếp hành động anh sẽ không làm |
| “Nhưng vẫn nhìn kỹ hơn.” | Generic | Không cho thấy Đào muốn gì hoặc nhìn điều gì | Gắn câu với món/chi tiết nhìn thấy được mà không biến thành claim mới |
| “Câu hỏi ở lại.” | Slogan / empty payoff | Không trả lời điều gì đã thay đổi giữa hai người; dễ gây cảm giác viết để kết clip | Cần payoff cụ thể hoặc bỏ câu nếu hình đã kết đủ |

## Chẩn đoán nhân vật

- Khoai hiện bị kéo về giọng **fact-checker/biên tập viên**, chưa phải người quản lý vận hành chín chắn, kỹ tính nhưng hài tinh tế.
- Đào hiện bị kéo về giọng **người dẫn ý tưởng**, chưa đủ cởi mở, gần gũi và có phản ứng đời thường.
- Cả hai đang nói về “cách trình bày thông tin” nhiều hơn nói về món và phản ứng của chính mình.

## Quyết định xử lý

1. Không timed read hai bản hiện tại như bản đã đạt.
2. Chạy Vietnamese Dialogue & Voice Editor trên từng câu, giữ claim IDs và beat.
3. Sau khi sửa thoại, mới chạy timed read; nếu sửa câu làm hỏng cơ chế, trả lại Concept Doctor/P5 chứ không ép câu cho “mượt”.
4. Không mở Veo cho đến khi qua language gate cùng các gate fact/canon.

Kết quả agent chuyên trách đã được ghi tại `agents/script_workroom/05_vietnamese-dialogue-editor-review-v0.1.md`: cả A và B đều `REWRITE_REQUIRED`, nhưng chưa bị loại ở cấp concept.
