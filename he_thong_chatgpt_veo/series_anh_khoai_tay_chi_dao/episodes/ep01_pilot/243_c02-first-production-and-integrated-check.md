# REC243 — C02 sản xuất đầu và kiểm cắt–xuất

Ngày 07/10/2026. Owner trả lời “1a”: dùng chính C02 đầu tiên để kiểm hình–tiếng và cắt–xuất trên Flow, không tạo clip thử riêng.

## Đã thực hiện

- Kiểm lại đủ ảnh v5, một K20, Omni 1.1 Flash, Ingredients, 720p, 9:16, 10 giây, x1, Agent OFF và giá 15. Gửi một lượt, không chạy lại.
- Tải và giữ bản gốc: SHA256 `5ba2878f2e59bbe03a49345217a0bccbf00b5d8c7864dac64d22cf26ceb6d4d4`; video 720×1280, 24 fps, 240 khung, 10 giây; audio 10,005 giây. Giải mã toàn file thành công.
- Trích đủ 240 khung. Lập bảng mẫu 1 fps và 6 fps theo timestamp thực. Root xem các bảng; reviewer độc lập xem 61 mẫu khác nhau, gồm một số khung đầy đủ độ phân giải. Root đã đọc toàn báo cáo. Không nhận đã xem/nghe liên tục toàn clip.
- Chạy ASR offline bằng công cụ đã có, không đưa lời chuẩn làm prompt. Kết quả ghi “mẹ Giang Gạo”; phải nghe để phân biệt lỗi nhận dạng với phát âm thực. ASR không xác nhận giọng K20.
- Cắt trên Scenebuilder: điểm đầu 0, điểm cuối UI 9 giây, tỷ lệ 9:16. Tải bản xuất thực: 720×1280, 24 fps, 217 khung, 9,041667 giây; audio 9,002667 giây. Tương quan PCM với phần nguồn là 0,9999898. Giữ tiếng đã được kiểm bằng tín hiệu, không thay nghe.
- Chi thực 15 credit; tab cập nhật báo 1.035. Còn 485 trong trần 500; chưa dùng dự phòng 110.

## Kết quả chất lượng

**REWORK_VISUAL_SCOPE — chưa mở C01A.**

1. Nền bị đổi từ phố mở, đèn lồng và mái bạt của v5 sang tường quán, cửa cuốn, quạt và bảng món.
2. Khung còn thấy chân và nhiều nền, không phải cận vừa hai người theo thiết kế.
3. Đào chắp tay ở đầu cảnh thay vì tay nghỉ. Các mẫu 0–0,667 giây cho thấy cử chỉ này; ở 0,833 giây tay đang hạ, tới 1 giây mới nghỉ.

Hai mặt, món và bàn đọc được; không thấy khói trong mẫu đã xem. Các điểm đó không bù được ba lỗi trên. Không trình duyệt phần hình như thể đã đạt.

## File và bằng chứng

Trong folder owner `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/`:

- Native: `05_native/EP01_720_C02_T01_NATIVE.mp4`.
- Khung và tiếng gốc: `06_qc/C02_T01_243/`.
- ASR: `06_qc/C02_T01_243_ASR/`.
- Kiểm bản xuất Flow: `06_qc/C02_FLOW_TRIM_243/`.
- Bản cắt thử: `07_edits/C02_T01_FLOW_TRIM_0_9S_QC_NOT_APPROVED.mp4`.

Bản cắt chỉ kiểm công cụ, chưa là range bàn giao được duyệt. Native và các nguồn cũ giữ nguyên.

## Còn mở và bước tiếp

Cần human nghe đúng K20, toàn lượt và cụm “mẹ rang gạo”; chưa PASS giọng hoặc khẩu hình. Hướng sửa đề xuất: chuẩn bị reference cận vừa riêng C02 từ v5, giữ nguyên nền và tay nghỉ, rồi chỉ yêu cầu chuyển mắt/đầu/miệng nhẹ. Không đổi lời, voice hoặc chuyển Quality để chữa lỗi này. Chưa chạy hướng sửa hoặc hứa xác suất đạt.

Trước take mới phải kiểm nguồn, prompt và phần bị ảnh hưởng; không chuyển báo cáo/hash cũ thành PASS cho output mới. Công cụ đã chứng minh được cắt–xuất một clip và giữ track tiếng, chưa chứng minh điểm nối nhiều clip, finishing hoặc toàn phim 30 giây.

Skill [computer-use](C:/Users/PC/.codex/plugins/cache/openai-bundled/computer-use/26.1002.51308/skills/computer-use/SKILL.md) giúp đối soát UI/nguồn/giá và lưu bằng chứng. Công cụ local đã có chỉ phục vụ QC; không gọi API mới.
