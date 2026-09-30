# P6 — Food-only Nem Bùi v0.1

Ngày 2026-09-30. Owner tiếp tục still trials sau54; image-only, không video/voice. Food identity vẫn VISUAL_LOCK_PENDING. Dùng mô tả nghiên cứu54, không upload ảnh báo/tư liệu hoặc dùng AI output làm bằng chứng món thật. Không tự thay claim/script.

## F-NB-01 — text-only

Flow Image / Nano Banana Pro /9:16/x1, không component. UI trước submit0credit. Exact prompt:

```text
Food-only concept study for Nem Bui of Bac Ninh, no characters. A modest loose mound of irregular thin pork and pork-skin strips mixed with finely ground toasted rice powder on a plain small off-white ceramic plate. Pale beige and light golden tones; visible non-uniform short strips, a softly crumbly powder coating, loose edges, not a smooth solid ball. A few green fig leaves beside the mound and one small bowl of amber dipping sauce with tiny red chilli pieces. Neutral warm ivory studio tabletop and backdrop, three-quarter overhead close-up showing the food texture clearly. Tactile stylized 3D animated-film rendering with believable food structure, gentle warm light. No packaging, brands, lettering, garnish flowers, fried rolls, pink cured pork blocks, noodles, chopsticks, people or extra dishes. Single vertical image. Preserve platform watermark.
```

UI kết quả: Không thành công, có thể vi phạm chính sách, chưa bị tính phí. Không output image; không thể QC món. Nguyên nhân moderation không được giải thích chi tiết; không tự suy từ một từ trong prompt. Proof local `media/raw/ep01_p6_food/F-NB-01_failed-flow-proof.png`. Giữ thẻ lỗi, không xóa.

## F-NB-02 — làm rõ món đã chế biến

Một revision text-only, không nút retry lặp prompt cũ. Giữ brief món ăn lành tính, mô tả rõ prepared/ready to eat; không vượt/bypass access control. Flow Image/Pro/9:16/x1; UI0credit trước submit. Exact prompt:

```text
Create a food-only visual concept of a traditional Vietnamese prepared rice-powder dish called Nem Bui from Bac Ninh, served ready to eat. Show a modest loose mound of irregular thin beige strips coated with finely ground golden toasted rice powder on one plain off-white ceramic plate. The texture is fibrous and softly crumbly with loose edges, not smooth or solid. A few green edible leaves beside the mound and one small bowl of amber dipping sauce with tiny red chilli pieces. Warm ivory studio tabletop, three-quarter overhead close-up. Tactile stylized 3D animation rendering with believable appetizing food texture and soft warm light. Only the prepared dish and serving props, no characters, packaging, branding or lettering. Single vertical image. Preserve platform watermark.
```

Result: đã submit và UI ghi0% trước khi thẻ tiến trình biến mất; thư viện không hiện candidate món. Browser cũ mất kết nối; đã bind lại đúng project trên in-app browser hiện hành, bỏ filter tìm kiếm để đối soát. Không có output truy cập được hoặc thông báo cuối riêng cho F-NB-02. **UNRECONCILED / NO_MEDIA_FOR_QC**, không ghi success/fail hoặc credit thực thanh toán khi chưa có bằng chứng. Không submit duplicate. Lá chung trong revision là open design, không nguồn để nhận dạng lá sung chính xác. Acceptance: món sợi/thính không thành roll/noodle/khối trơn; food texture đọc được; props không brand/text; final food identity phải qua evidence/reviewer và owner, không tự PASS từ prompt adherence.

## Tổng hợp vòng

Đã xác định: F-NB-01 trả moderation fail/no-charge; F-NB-02 chưa đối soát được kết quả. Quyết định: giữ cả request trong log, không tạo thêm bản trùng để che trạng thái mất. Giả định: source54 là research-only, món chưa canonical. Còn mở: terminal status F-NB-02, provenance món thật và phần gắp. Bước tiếp: kiểm thư viện sau reload/kết nối ổn định; nếu vẫn không có terminal evidence thì owner xác nhận trạng thái trên Flow trước một request mới. Grip vẫn REWORK theo55. P6 OPEN, chưa video/voice.
