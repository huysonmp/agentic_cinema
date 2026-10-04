# EP01 — Gói chuẩn bị thử lời mới C-v0.6

Chưa có audio hoặc video mới trong folder này. Đây là gói chuẩn bị, không phải kết quả thử để nghe.

## Lời cần thử — giữ đúng nguyên văn

**Đào:** “Anh nhìn mãi. Không hợp thì để em.”

**Khoai:** “Khoan. Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.”

**Đào:** “Anh chờ ăn à?”

**Khoai:** “Chờ mẹ quay lưng.”

Ba câu kết không đổi: Đào “Chờ em quay lưng nữa à?”; Khoai “Anh gắp cho em mà.”; Đào “Thế em quay lại đúng lúc rồi.”

## File và trạng thái

- `dialogue-package.json`: bảy lượt lời, giọng K20/D06 theo đúng ID, nội dung phụ đề và cue món/nhãn AI; timing chưa đo để null.
- `prompt-dialogue-draft.txt`: prompt dự thảo cho bốn lượt đầu. Phải gắn token audio thật và kiểm giao diện; tên giọng trong text không đủ. Bỏ đoạn ghi chú hành chính ở đầu trước khi dùng vào ô tạo.
- `local-text-qc.json`: kết quả kiểm nhất quán văn bản tại chỗ; không chứng nhận chất giọng, khả năng vừa thời lượng, hình hoặc diễn.

## Cần owner duyệt trước tạo

Đề nghị bổ sung tối đa17 credit, dùng cùng4 còn lại theo sổ177, cho một batch ba mẫu tổng không vượt21. Cấu hình đề nghị kế thừa Omni 1.1 Flash / Thành phần / 360p / dọc / 10 giây / x3; không phải Veo Lite hoặc Quality. Giá21 là lịch sử, chưa kiểm trực tiếp cho lượt mới. Nếu giá hoặc cấu hình ngoài phạm vi, dừng để trình lại.

Khi có mẫu mới, nghe cả ba để so độ ấm/nhịp kể của Khoai, câu hỏi tự nhiên của Đào, đúng lời/đúng vai và điểm nối với ba câu kết. Không bỏ âm hay tăng tốc để ép thời lượng. Bản ráp v0.4 và audio175/177 vẫn là lịch sử lời cũ, không thay phụ đề để giả thành audio mới.
