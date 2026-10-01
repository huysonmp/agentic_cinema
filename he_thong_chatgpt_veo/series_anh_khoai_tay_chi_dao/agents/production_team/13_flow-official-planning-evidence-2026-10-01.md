# P7/P8 — Tư liệu Google chính thức cho thiết kế cảnh

Root kiểm web ngày 2026-10-01. `OFFICIAL_DOCUMENTATION_CHECKED / ACCOUNT_UI_NOT_CHECKED / NO_EXECUTION`.

## Nguồn và phạm vi

1. [Flow: models & supported features](https://support.google.com/flow/answer/16352836?hl=en), phần Veo3.1 Lite/Fast/Quality, source lines25–81 tại lần đọc.
   - Tài liệu liệt kê 4/6/8 giây cho text và frames-to-video của các model này; cả hai tỷ lệ khung.
   - Ingredients: Lite/Fast hỗ trợ clip8 giây; Quality không hỗ trợ.
   - Extend: chỉ Lite trong bảng hiện hành; không suy Fast/Quality hỗ trợ extend.
   - Phải kiểm model/resolution/credit thực tại ô cài đặt trước tạo. Đây chưa xác nhận tài khoản/project có đúng tính năng đó.
2. [Flow: create videos](https://support.google.com/flow/answer/16353334?co=GENIE.Platform%3DDesktop&hl=en), sections frames, references, voice references, best practices; source lines52–125.
   - Với frames, mô tả hành động/chuyển tiếp giữa ảnh đầu–cuối; tính năng có thể khác theo vùng.
   - Hình và lời hướng dẫn không nên mâu thuẫn; refs cần nhất quán phong cách, tránh đối tượng thừa ngoài ý định.
   - Mục voice-reference mô tả workflow Omni Flash/Ingredients, không là bằng chứng Veo có cùng control. Không đổi model dự án hoặc tạo voice qua tài liệu này.
3. [DeepMind: Veo prompt guide](https://deepmind.google/models/veo/prompt-guide/), sections framing/motion/style/lighting/character/location/action/dialogue; source lines122–156.
   - Brief cần chỉ rõ nhân vật, camera, hành động, bối cảnh và lời nói theo người. Hướng dẫn có dialogue không bảo đảm phát âm tiếng Việt, giọng ổn định hoặc timing của EP01.

## Hệ quả thiết kế — suy luận của root, chưa test

- Logical shot10 giây không được gọi là một native Veo request10 giây dựa trên bảng trên. Nếu cần giữ payoff liên tục lâu hơn8 giây: P8 phải có phương án chia/nối hoặc route-supported extension được kiểm; không tự dùng model khác, cắt thoại hoặc tăng tốc diễn.
- Chọn model vì chữ “Quality” mà đồng thời yêu cầu ingredients có thể xung đột. P8 phải kiểm exact mode/input, thay vì gom mọi chức năng Veo vào một prompt.
- v0.8 là baseline cảnh, không tự phù hợp start-state mọi shot. Nhịp đã có đũa/bát/cốc trong tay cần đúng start-state; hình neutral có thể gây conflict nếu prompt gọi nó là keyframe hành động đã bắt đầu.
- Chưa kiểm UI tài khoản, active model, audio, cost/count hoặc native output; chưa READY và không generate. Không lấy giới hạn API Vertex để thay Flow.
