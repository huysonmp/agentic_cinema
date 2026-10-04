# Dự thảo thử hai câu mở — chưa cấp quyền tạo

Nguồn quyết định:176; giữ script32/K20/D06, không dùng A03 của170. Mục đích duy nhất: hoàn thiện L01–L02 và kiểm nối audio với B01 bộ175. Hình là đối chứng, chưa cảnh sản xuất.

## Điều kiện trước submit

- OPEN7 đúng ảnh; K20 ID `fb1188da-e6c8-4156-9bba-0576c01a8da6`; D06 ID `0ce1551e-e74b-481c-bb9e-d31e04f8b352`. Không lấy K12 cùng tên Orus.
- Omni 1.1 Flash / Thành phần / dọc / 360p / 10s / x3 theo route175; không gọi Veo Lite. Quote gần nhất21; đọc giá thực và quyền chi bổ sung trước chạy. Nếu route/giá khác phải ghi lại, không tự nâng model.
- Gắn token UI thật vào từng nguồn giọng. Đoạn dưới là text dự thảo, tên preset hoặc ID trong tài liệu không thay cho token audio đã gắn.
- Readback ảnh + hai audio + đúng token ID, không chip lỗi; xem screenshot cấu hình/compose cuối rồi submit, không bấm chip để xem detail hoặc đổi đầu vào sau kiểm.

## Lời và hướng diễn dự thảo

```text
Create a 10-second vertical dialogue diagnostic using the supplied image. Khoai is the adult golden potato character on the left; use the supplied K20 custom Orus audio reference as his only voice. Dao is the adult female peach character on the right; use the supplied D06 custom Aoede audio reference as her only voice. Preserve the supplied composition in a fixed medium two-shot. Both are adult friends at a small tidy ordinary street-side eatery. Hands stay at rest; this diagnostic is not enactment of pulling a plate, eating or transferring food. Food remains cold, with no steam or smoke.
Speak only these two lines once, in this order, without speaker names or extra words:
Dao: "Anh nhìn mãi. Không hợp thì để em."
Khoai: "Khoan. Mùi này làm anh nhớ cái chảo."
Keep the selected custom voice identities and their natural northern Vietnamese/Hanoi pronunciation. Dao retains D06: adult female, airy-open mid register, light brightness, clear words, conversational rather than childish, flirtatious or a presenter. Her first line is an easy friendly suggestion, not criticism of the food or scolding Khoai. Khoai retains K20: adult male, warm rounded mid-low tone, close intimate conversation, not a presenter. He gently interrupts on "Khoan", then recalls something familiar with a slight inward smile on "nhớ cái chảo", not a dramatic revelation. Allow a small natural beat between speakers. Aim to finish the two lines in about six seconds without rushing; remain quietly attentive afterwards. One speaker at a time, the other listens with mouth closed. No music, narration, additional speakers or sound effects. Do not read directions aloud.
```

## Review và điều kiện dùng

Tạo đủ ba theo quyết định test hiện hành; lỗi công cụ không coi là mẫu diễn fail và không tự retry vượt cap. Lưu prompt/token/config actual, native/hash/PCM, bảng charge, mọi kết quả. Nghe/nối với B01 nguyên tốc độ trước chọn; ASR chỉ hỗ trợ đúng lời, không thay kiểm identity/nhịp. Nếu lời dài hơn6s thì ghi timing thực và thử dựng lại trước đề xuất sửa lời. Không cắt mất âm để ép slot; hình diagnostic không tự dùng cho master. Mẫu nào đạt cần ghi phạm vi approval; không tự chuyển Quality.
