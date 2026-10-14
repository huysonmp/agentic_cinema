# REC309 — Không suy tùy chọn UI thành tệp im tiếng

Trước C08, UI “Trả về video không có âm thanh” đã được đọc TRUE và có toast. Native tải đúng asset vẫn chứa AAC48kHz stereo, PCM đo maxAbs0,192046 / RMS0,04169, không phải toàn0. Tên setting, quote hoặc không có voice chip không chứng minh output không tiếng.

Đây là counterexample quan sát, chưa chứng minh nguyên nhân nội bộ hoặc ý nghĩa đầy đủ của setting. Tôi đã tìm và đọc tài liệu Google: [tạo video](https://support.google.com/flow/answer/16353334?hl=en), [model và tính năng](https://support.google.com/flow/answer/16352836). Trang model xác nhận Omni hỗ trợ Frames-first và4s; hai trang này không giải thích setting đủ để kết luận đó là lỗi UI hoặc toggle bắt buộc mute. Không lấy forum/community hoặc trang của sản phẩm Flow khác làm nguồn kết luận kỹ thuật.

ASR offline nhận “Ơm...”, không bằng chứng đủ về speaker/giọng hay tiếng thực. Root chưa nghe. C08 đã được brief là hành động không thoại; giữ native và tạo riêng derivative review0–64F bỏ track âm phát sinh, không đụng tiếng K20/D06 đã duyệt. Ghi rõ cắt track nào/nguồn/hash; không gọi derivative là native silent hoặc hồi tố approval tiếng khác.

Kiểm clip không thoại gồm hai nhánh riêng: probe/PCM của output và miệng nhân vật trên wholeframes. Khi finishing, ambience/mix phải xử lý nhất quán ở toàn tập; không dùng mọi đoạn silence để mặc định audio cut đã mượt. Không tiêu credit tạo lại chỉ để sửa phần âm có thể loại khỏi clip không thoại trong phạm vi đã giao.
