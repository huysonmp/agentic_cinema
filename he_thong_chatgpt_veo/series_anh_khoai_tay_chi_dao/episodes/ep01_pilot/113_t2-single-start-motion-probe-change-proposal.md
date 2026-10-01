# T2 — Đề nghị đổi phương pháp thử, không đổi cách quay

2026-10-02. PROPOSAL / NOT_APPROVED / NOT_SUBMITTED. Chuẩn bị theo vòng batch111, không tự biến “làm một loạt” thành quyền chạy video. Không ghi Veo có route/settings này khi chưa UI evidence.102 giữ lịch sử start/end method; direction100 giữ nguyên.

## Vì sao trình phương pháp khác

Các lượt sửa ảnh độc lập hoặc đổi cảnh quá nhiều, hoặc gần như giữ nguyên OPEN. Không có camera-only endpoint đã đạt. Đề nghị thử tạo chuyển động trực tiếp từ một ảnh đầu được chọn, thay vì ép hai still tự vẽ lại khớp nhau. Đây hypothesis kỹ thuật để kiểm thực, không khẳng định cải tiến chất lượng trước test; không đổi tilt thành zoom/cut hoặc bỏ bữa ăn để dễ tạo.

| Phương án | Hệ quả | Khuyến nghị sơ bộ |
|---|---|---|
| A — Một start frame, mô tả small upward tilt trong Veo Lite nếu UI hỗ trợ | Không cần END lỗi làm constraint; actual có thể vẫn đổi mặt/món hoặc không làm tilt; cần full-motion review, owner chọn OPEN7/đầu khác và approve count/price riêng | Đề nghị kiểm UI rồi trình exact request; chưa chạy |
| B — Tiếp tục tạo END tĩnh bằng imagegen | Giữ method102, thêm phiên bản/review; chưa thấy cặp hợp lệ từ các lượt vừa làm | Chỉ chạy bounded khi có sửa chiến lược cụ thể, không lặp cùng prompt vô hạn |

## Draft của phương án A — các trường chưa kiểm ghi UNKNOWN

Input dự kiến OPEN7 hash A3D80F09BFB7242BAE3007AD7B4F37473BB2F0ED019A84CC4956C4D32A8DBF9A, chưa owner-selected, appearance hierarchy cần chốt. Single-start route, Lite,9:16,x1 là đề xuất; availability/resolution/duration/price/accountbalance UNKNOWN.4s ở102 không suy được account hiện tại hỗ trợ. Không dùng10credit đã reserve V02. Không retry/Extend/Quality tự động. Tạo đúng một diagnostic clip khi exact settings/count/spend được duyệt.

Exact prompt draft:

```text
Use the supplied start image as the fixed visual anchor for a vertical camera-only diagnostic. The adult potato man sits screen left and adult peach woman screen right at a small tidy street-side eatery. Begin with attention on the complete shared Nem Bui meal, then make one very small smooth upward camera tilt toward the potato man's eyes and settle. No push-in, zoom, orbit, cut, shaking or axis change. Both full faces and the whole food presentation, all herb leaves, both sauces, two eating bowls, both resting chopstick pairs and water glass remain visible throughout. Preserve original identities, clothing, facial expression, hands at rest, food texture/quantity, table geography, background and warm light. No new sky area or exaggerated headroom. Both characters remain quietly seated with minimal natural breathing; no gestures, food touching, eating, drinking or speaking. No dialogue, voice-over, singing, music or added text/signage. Preserve any native watermark on the actual video output. This tests camera movement, not acting or voice.
```

Không hứa tool giữ pixels hoặc silent audio. Ghi actual audio nghe được/UNKNOWN; từ chối out-of-scope speech/music nếu có, không coi “no audio” trong prompt là enforcement. Probe gắn nhãn AI qua manifest; publication disclosure vẫn riêng.

## Gates và kiểm thực

1. Owner chốt phương pháp A/B và chọn start image sau review; không lấy thích aesthetic thay source/continuity check.
2. Operator kiểm UI live route/model/count/duration/ratio/price/input file/account. Nếu khác draft: báo exact options trước submit. Source preserved/provenance109 không chứng nhận rights upload tuyệt đối.
3. Owner approve exact request + spend riêng. Chỉ lúc đó submit một lần, giữ native output/watermark, lưu actual file/hash/settings/cost.
4. Reviewer full playback đầu/giữa/cuối và lỗi: tilt đọc được, mặt/món/props ổn định, whole meal giữ, không motionwarp/flicker/mouth/action ngoài scope; nghe audio nếu có capability. Nếu không xem full-motion thì UNKNOWN, không lấy still làm PASS.
5. Owner chọn/REWORK/HOLD; camera pass không voice/production/full30s pass. CR-01 và V02 vẫn mở.

Đã xác định: new END methods còn failure; quyết định chốt: direction100/provenance109 giữ; giả định: single-start có thể giảm mismatch inputs, chưa test; mở: source selection/UI/price/request/change approval; tiếp theo: trình phương án và read-only UI preflight nếu owner chọn A. Không bổ sung agent mới chỉ để đổi tên một kiểm tra đã có CINE/CONT/FLOW.
