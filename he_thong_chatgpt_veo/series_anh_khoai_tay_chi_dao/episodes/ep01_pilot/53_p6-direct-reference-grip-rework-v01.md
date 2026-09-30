# P6 — Sửa grip với reference trực tiếp v0.1

Ngày 2026-09-30. Owner: “ok làm đ”, tiếp tục hai việc đề xuất sau52: sửa tay có gắn reference cận tay trong composer và nghiên cứu hình Nem Bùi. Không có approval voice/video hoặc toàn P6. P6 OPEN; duo45 v0.3 vẫn primary identity.

## Run H-K-I03

Target canvas: H-K-I02, Flow asset `dba187f0-f6c0-4ef0-8cc1-7efe8a176e53`. Đã gắn trực tiếp component `Hand holding wooden chopsticks` (H-K-C01) vào composer editor; kiểm UI trước submit. Khắc phục input ambiguity ở52, không giả định history tự gửi lại reference.

Editor image, Nano Banana Pro inherited, 9:16, một output; UI trước submit hiển thị 0 credit. Một generation thực tế. Không dùng credit0 để kết luận mọi request miễn phí; không kiểm billing tổng. Thông báo kết nối reCAPTCHA xuất hiện trước run, reload trang một lần đã hết; không giải CAPTCHA hoặc bypass.

Exact prompt:

```text
Edit the potato portrait on the canvas. The attached CLOSE-UP HAND is a grip-only reference, not a replacement character. Replace ONLY the raised right hand and its two chopsticks with the clearly visible thumb-and-finger arrangement from that close-up. Rotate the palm toward camera as in the close-up: visible thumb across upper stick, separate curved index and middle fingers controlling upper stick, ring finger supporting lower stick. Keep hand size proportional to this character and connect naturally to his existing forearm. Exactly two wooden sticks extending to screen right with separated empty tips; not a fist. Preserve the canvas character face, potato silhouette, body, outfit, other hand, framing, light and background unchanged. No new objects, food or text. Preserve platform watermark.
```

Đã tải và xem ảnh thật. Local `media/raw/ep01_p6_consistency/H-K-I03_v0.1.jpg`; SHA256 `AF53408253A1B24E9D6F31C8462A2EB890F2F790972ED2AF7C77D3238A54AF9F`. Proof UI: `media/raw/ep01_p6_consistency/H-K-I03_flow-proof.png`. Media gitignored, chỉ manifest/docs được push.

## QC và kết luận

- Mặt, silhouette, trang phục và nền khá sát target. Đây là quan sát root, không độc lập reviewer hoặc owner approval.
- Hai đũa đã thay đổi và tách ra; chưa đủ để chứng minh grip đúng.
- Ngón cái chưa thể hiện rõ điểm tựa; các ngón vẫn gần song song ôm que; phân vai giữ upper/lower không đọc được. Palm chưa xoay như yêu cầu.
- **GRIP_INTEGRATION_STILL_FAIL**. Không promote thành asset dùng cảnh gắp. Không chứng minh khả năng motion.

Đã xác định: input gắn trực tiếp không tự bảo đảm adherence. Quyết định giữ quality gate và primary45, không sửa script để che lỗi. Giả định hiện dùng: component cận tay chỉ provisional, không canon. Còn mở: grip trên nhân vật toàn thân/scene và chuyển nem bằng đũa. Bước tiếp theo: thử reverse integration (giữ tay cận làm canvas, mở rộng nhân vật theo primary) thay vì lặp repair tương tự; phải kiểm đồng thời anatomy và identity trước scene. Food research ghi riêng54.
