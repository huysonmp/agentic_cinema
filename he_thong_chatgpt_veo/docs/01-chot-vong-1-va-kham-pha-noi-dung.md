# Chốt vòng 1 và khám phá nội dung vòng 2

- **Ngày:** 2026-09-29
- **Trạng thái:** đang khám phá
- **Mục tiêu vòng 2:** xác định định vị series TikTok và cấu trúc một tập trước khi thiết kế workflow, agent hoặc skill.

## 1. Decision lock từ vòng 1

| ID | Quyết định | Trạng thái |
|---|---|---|
| D1 | Sản phẩm là series video TikTok dạng kể chuyện/giải thích | locked |
| D2 | Mỗi pilot là một sequence nhiều clip | locked |
| D3 | Người dùng và Codex co-work từ ý tưởng đến quyết định sáng tạo ban đầu | locked |
| D4 | Thao tác Google Flow thủ công trước; chỉ đánh giá Gemini API sau khi workflow được chứng minh | locked |
| D5 | Dùng bốn gate: brief, creative/shot, generation và selection/export | locked |
| D6 | Người dùng là operator Veo và người phê duyệt chính | locked |
| D7 | Điều kiện tài khoản khai báo: Google AI Pro, khoảng 100 credit, có các mode Veo cần dùng | cần read-back trong Flow |
| D8 | Tối ưu ưu tiên là chất lượng và khả năng làm chủ đầu ra bàn giao; không phải tốc độ hay tự động hóa | locked |

Các quyết định `locked` chỉ thay đổi khi có bằng chứng pilot hoặc người dùng chủ động mở lại.

## 2. Bài toán lõi đã rõ hơn

Ta không chỉ cần “tạo video bằng Veo”. Ta cần một hệ thống giúp phát triển **một series có bản sắc, khả năng lặp lại và chất lượng bàn giao có thể kiểm soát**, trong đó mỗi tập:

1. bắt đầu từ một ý tưởng chưa hoàn chỉnh;
2. được người dùng và Codex cùng phát triển thành premise/brief;
3. được chia thành sequence và generation package có thể duyệt;
4. được người dùng tạo trong Flow với credit hữu hạn;
5. lưu được lý do chọn, loại và sửa để tập sau tốt hơn.

Giải thích mới của từ “mini”: tối giản hạ tầng, integration và automation; không lược bỏ stage, quality gate, review, versioning hay hồ sơ bàn giao cần thiết. Khung khám phá quy trình tiếp tục tại `02-dinh-huong-quality-first.md`.

## 3. Năm quyết định ưu tiên vòng 2

### Q1 — Series nói về chủ đề nào và tạo giá trị gì? — **Cần bạn trả lời**

Mô tả bằng một câu theo cấu trúc:

> Series giúp `[đối tượng]` hiểu/cảm nhận/làm được `[giá trị]` thông qua `[cách kể đặc trưng]`.

Nếu chưa có chủ đề cố định, hãy đưa 2–3 vùng ý tưởng bạn đang quan tâm. Codex sẽ cùng bạn so sánh và chốt, thay vì yêu cầu bạn tự hoàn thiện concept.

### Q2 — Audience đầu tiên là ai và họ xem trong ngữ cảnh nào? — **Cần bạn trả lời**

| Phương án | Hệ quả |
|---|---|
| A. Khán giả đại chúng tìm nội dung giải trí | Hook và cảm xúc quan trọng nhất; thông tin phải cực gọn |
| B. Một cộng đồng/ngách chuyên môn | Có thể sâu và khác biệt hơn; quy mô ban đầu hẹp hơn |
| C. Khách hàng/đối tượng gắn với thương hiệu | Cần CTA và độ chính xác thương hiệu; dễ biến thành quảng cáo |
| D. Xây personal brand | Cần quan điểm/giọng kể nhất quán và liên kết với hình ảnh người sáng tạo |

**Khuyến nghị sơ bộ:** bắt đầu từ một audience đủ hẹp để biết họ vì sao dừng lại xem, nhưng không khóa quá sâu vào persona giả định chưa có dữ liệu.

### Q3 — Lời hứa và engine lặp lại của series là gì? — **Cần bạn cùng quyết định**

Các engine thường gặp:

| Engine | Ví dụ cấu trúc | Hệ quả |
|---|---|---|
| Một câu chuyện, một insight | tình huống → chuyển biến → điều rút ra | Cân bằng kể chuyện và giải thích |
| Điều tưởng đúng nhưng sai | niềm tin phổ biến → twist → giải thích | Hook mạnh; phải kiểm chứng fact |
| Thế giới/nhân vật định kỳ | nhân vật gặp vấn đề mới mỗi tập | Xây nhận diện tốt; continuity khó hơn |
| Giải thích bằng ẩn dụ điện ảnh | câu hỏi → thế giới hình ảnh → lời giải | Phù hợp Veo; dễ đẹp nhưng có nguy cơ mơ hồ |

**Khuyến nghị sơ bộ:** “một câu chuyện, một insight” hoặc “giải thích bằng ẩn dụ điện ảnh” cho pilot đầu. Chỉ dùng format fact-heavy khi đã có quy trình kiểm chứng nguồn.

### Q4 — Giọng kể và audio thuộc loại nào? — **Cần bạn trả lời**

| Phương án | Hệ quả |
|---|---|
| A. Voice-over dẫn chuyện | Dễ truyền đạt ý; cần script, voice và mix ổn định |
| B. Nhân vật nói trong cảnh | Immersive; khó giữ giọng/lip-sync/continuity hơn |
| C. Text-on-screen + nhạc/SFX | Dễ kiểm soát thông tin; cần hậu kỳ chữ và nhịp dựng |
| D. Kết hợp voice-over và text | Linh hoạt và hợp TikTok; workflow nhiều lớp hơn |

**Khuyến nghị sơ bộ:** D, nhưng coi audio/text là lớp hậu kỳ riêng cho đến khi test cho thấy native audio của Veo đủ ổn định.

### Q5 — Một tập pilot được coi là đạt dựa trên điều gì? — **Cần bạn chọn ưu tiên**

Chọn tối đa ba tiêu chí chính và xếp thứ tự:

- người xem hiểu đúng một thông điệp;
- hook đủ mạnh trong vài giây đầu;
- hình ảnh có bản sắc và nhất quán;
- câu chuyện hoàn chỉnh trong thời lượng ngắn;
- tạo được với ngân sách credit giới hạn;
- workflow có thể lặp lại cho tập tiếp theo;
- đạt chỉ số TikTok thực tế sau khi đăng.

**Khuyến nghị sơ bộ cho pilot hệ thống:** ưu tiên `(1) hiểu đúng thông điệp`, `(2) workflow lặp lại`, `(3) credit nằm trong giới hạn`. Chỉ số nền tảng là vòng đánh giá sau khi nội dung đã đủ tốt và được phép đăng.

Đồng thời cần chốt trần credit cho pilot đầu. Với tổng khoảng 100 credit do người dùng cung cấp, giả định thận trọng ban đầu là chỉ dùng tối đa 20–30 credit cho pilot, giữ phần còn lại cho thử nghiệm có kiểm soát sau retrospective. Chi phí thực tế theo mode phải được read-back trong Flow trước G3.

## 4. Có thể tạm giả định

- Format dọc `9:16`.
- Mỗi tập là một sequence ngắn, cấu thành từ nhiều clip Veo.
- Codex giữ vai trò một orchestrator co-creative; chưa tạo nhiều agent.
- Voice, nhạc, subtitle và dựng cuối có thể nằm ngoài Veo nếu native output không đủ kiểm soát.
- Chưa publish tự động và chưa gọi API trong pilot đầu.

## 5. Bắt buộc nghiên cứu hoặc thử nghiệm

| Task | Thời điểm | Kết quả cần có |
|---|---|---|
| T1. Read-back tài khoản Flow | trước generation | model/mode, duration, resolution và credit cost thực tế |
| T2. Kiểm tra TikTok spec hiện hành | trước khi khóa export profile | aspect ratio, duration, codec, safe area và giới hạn upload |
| T3. Test audio strategy | sau khi có một scene mẫu | so sánh native audio, voice-over riêng và text-on-screen |
| T4. Credit budget test | trong pilot | credit dùng theo shot, candidate đạt và số vòng sửa |
| T5. Rights manifest | trước G3 | nguồn, quyền và hạn chế của asset/reference/voice/music |

## 6. Không mở rộng ở vòng này

- Chưa quyết định số lượng agent hoặc viết skill.
- Chưa thiết kế Gemini API client.
- Chưa chọn công cụ dựng/hậu kỳ hoặc lịch xuất bản cả series.
- Chưa tự động nghiên cứu fact, upload hay publish TikTok.

## 7. Tổng hợp trạng thái

### Đã xác định

- Series TikTok kể chuyện/giải thích, sequence nhiều clip, co-creative với Codex.
- Manual Flow trước, API sau; bốn human gate; người dùng trực tiếp vận hành.

### Quyết định đã chốt

- D1–D6 trong bảng decision lock.

### Giả định đang sử dụng

- Video dọc, manual-first, một orchestrator, hậu kỳ tách khỏi Veo khi cần.

### Vấn đề còn mở

- Chủ đề, audience, engine nội dung, audio strategy, success criteria và credit budget mỗi tập.

### Bước tiếp theo

Trả lời Q1–Q5. Sau đó chọn 2–3 concept series để so sánh bằng cùng một rubric và chốt concept pilot tại G1.
