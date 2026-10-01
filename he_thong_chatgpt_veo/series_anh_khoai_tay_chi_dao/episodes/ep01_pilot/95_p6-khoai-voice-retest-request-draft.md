# V01-R2 — Request thử lại giọng Khoai, bản đề xuất

2026-10-01. Hướng diễn xuất đã duyệt trong 93, exact request và ngân sách mới CHƯA duyệt. Không submit; không dùng 10 credit dành V02. Giá/current UI UNKNOWN; phải đọc lại trước chạy. Một output/lượt đề xuất, Lite như baseline, không tự chuyển Quality. Giữ reference T-NB-03_v0.8/hash trong 78; không đổi crop/ánh sáng đồng thời trong vòng voice so sánh. Nếu owner muốn sửa hình cùng lúc phải tách thành experiment khác.

## Exact prompt đề xuất

```text
Create one vertical 9:16, 8-second diagnostic video using the supplied approved table image as the starting frame. Preserve the adult potato character Khoai on the left and adult peach character Dao on the right, their faces, outfits, the street-side eatery and the entire approved meal: food plate, leaves, sauces, bowls, chopsticks and glass. Locked camera; both remain seated with their hands resting on the table. No utensil handling, eating, drinking, food transfer or raised-hand gestures. Only subtle facial expression and speech. Dao listens silently. Do not generate any captions, character-name labels or other text; preserve the existing platform watermark. No music or narration. Quiet ambience.
Khoai alone speaks these exact Vietnamese lines, once, in this order, without adding or omitting words:
"Khoan. Mùi này làm anh nhớ cái chảo."
"Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ."
Use an original mature adult male voice with a comfortably low register, warm resonance and clear diction, with a light Northern Vietnamese accent. Not gravelly, forced-deep, elderly, announcer-like or an imitation of a real person.
He is quietly sharing a memory with Dao, not presenting information to an audience. "Khoan" is a soft moment of recognition, not a command. The first sentence has gentle curiosity, lightly emphasizing "mùi này" and "cái chảo". "Bếp nhà anh, hồi bé" softens and slows slightly as the memory returns. "Mẹ rang gạo" feels warmer; "anh đứng chờ" ends with a restrained smile audible in his voice, not a laugh. Use subtle variations in pace, emphasis and pitch with natural short pauses. No monotonous delivery, exaggerated sadness, theatrical intonation or romantic delivery. Keep every word clear and complete; do not rush or truncate speech to fit. Synchronize mouth movement only with Khoai's speech.
```

## Kiểm và quyết định sau output

- Giữ nguyên lời, Lite và reference để so A/B với V01; thêm constraints tay/chữ là sửa lỗi probe được ghi rõ, không gọi pure single-variable voice experiment.
- Nghe V01 vs R2: độ ấm/trầm, rõ dấu thanh, nhịp chuyển vào ký ức và nét cười kín. Giọng sâu hơn mà giả/gằn/đều vẫn REWORK. Actual take acceptance do owner; mô tả voice không là voice-ID lock.
- Kiểm đủ lời, đúng người, không tiếng Đào/thêm lời, không dồn/nuốt cuối câu. ASR chỉ dẫn chỗ nghe, không quyết định giọng hay phát âm.
- Tay/chữ/meal layout có visual gate riêng; voice phù hợp không tự duyệt final video. Không ghép lại chữ/từ để cứu giọng.
- 8 giây chỉ target probe. Nếu không đủ nhịp tự nhiên, trình cách chia hai probe/thời lượng có actual UI hỗ trợ và budget riêng; không tự làm hoặc viết lại thoại.
- Fresh preflight đọc model/mode/9:16/720p/8s/x1/ref/giá, owner duyệt exact scope/budget; khác cấu hình hoặc terminal không rõ → HOLD.

Đã xác định: V01 không được chọn, hướng93 đã duyệt. Đã chốt: chưa generation. Giả định: Lite cùng ref vẫn phù hợp thử có kiểm soát, chưa chứng minh model làm theo prosody. Còn mở: exact request/budget/giá UI và nghe output. Bước tiếp: owner duyệt request trước thử lại.
