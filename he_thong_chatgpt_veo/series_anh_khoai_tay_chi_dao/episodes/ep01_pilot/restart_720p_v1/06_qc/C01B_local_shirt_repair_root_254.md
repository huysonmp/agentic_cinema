# REC254 — Sửa riêng vùng áo, giữ tiếng nguồn

Trạng thái: **GO_FOR_OWNER_AV_CHECK / NOT_SELECTED**. Owner cho phép thử hậu kỳ vùng chữ bằng công cụ local đã có, không dùng credit. Đã tạo một bản MP4 riêng từ **T02 gốc**, không từ bản Flow sửa lỗi 253. Root đọc đầy đủ review độc lập 254 trước khi trình actual media cho owner; đây chưa phải nghiệm thu nguồn/range BM hoặc phim.

## Phương pháp và các lượt local

Lần căn chỉnh phạm vi nhỏ ban đầu chạm biên dò, script dừng trước khi xuất video. Giữ evidence dở dang, không overwrite. Phân tích riêng phạm vi ±12 pixel vẫn chạm biên dọc; phân tích tiếp x±8/y±40 đo được dịch x đến 6 pixel, y đến 24 pixel so hai anchor. Không cài OpenCV hoặc công cụ mới; dùng NumPy/Pillow và FFmpeg đã có. Hai lượt analysis không tạo video; một lần render hoàn tất.

Vùng được thay là `[260,463)×[830,918)` trên F23–57. Lấy vải sạch ở F22/F58, đăng ký dịch chuyển theo vùng áo còn thấy quanh chữ, trộn hai anchor theo thời gian và feather viền 8 pixel. Đây là phục hồi xấp xỉ phần vải đã bị che, không biết chính xác vải gốc dưới chữ. Không sửa mặt/miệng/tay, không freeze hoặc crop toàn cảnh. Toàn bộ pixel ngoài vùng sửa và 61 frame không có chữ **trước encode** được so bằng tuyệt đối; MP4 được mã hóa lại H.264/yuv420p nên không hứa video sau encode pixel-identical.

## Provenance và kiểm thực

- Source SHA-256 `780ab0b3fb29454f732d2f56ed30526a77f81ed98bbaf04ca04cdb5cf094b231`, rehash sau render vẫn nguyên. Không ghi đè original hoặc các take lỗi trước.
- Output `07_edits/C01B_BM_T02_LOCAL_SHIRT_REPAIR_T01_FOR_REVIEW.mp4`, SHA-256 `cd4213d393798ca3baf45603a9c40215b7f08ffcf7091418238e183abb76b198`; bản preview và archive cùng hash.
- 720×1280, H.264, 24 fps, 96 frame, video 4s; AAC stereo48kHz/audio 4,01s; tổng 4,01s. Full decode thành công, frame/time map 1:1 nguồn.
- Root xem đủ 12 board encoded source/output và PNG native F32. Reviewer độc lập xem đủ 96 frame cùng PNG F23/F36/F57. Không còn chữ “Khoan” trong vùng áo; không thấy sai khác rõ của mặt/mắt/miệng/tay/đạo cụ/nền/timing. Không thấy nút nhân đôi hoặc đứt đường áo rõ trên ảnh. Reviewer ghi vùng áo giữa đoạn hơi mềm/chuyển sắc nhẹ, cần playback để xét jitter/shimmer. Không gọi review frame thành continuous AV.
- Audio dùng `-c:a copy` từ source. Đối soát đủ **189 packet audio**: hash dữ liệu, PTS/DTS/duration bằng nguồn. PCM decoded bằng tuyệt đối: cùng 192.480 audio frame/stereo48kHz, SHA-256 `4c4bbe1c14ad2f6184c6b64bd310c9187245929e323dc64685fdff5484686c0c`. Giữ nguồn tiếng đã được chứng minh; **đúng K20/sắc thái/lời và sync chưa được thực nghe/owner duyệt**.

Evidence ở `C:/Users/PC/Downloads/du_an_nem_bui/254_LOCAL_SHIRT_REPAIR/`: compositor_v2, encoded_qc, encoded_comparison và hai hồ sơ registration. Unit sanity identity registration =0/0/error0, phạm vi patch dưới mặt/trên bát và assertions thật qua 96 frame đều qua; đây không là test nghệ thuật.

## Cổng owner và dependency

Đã gửi đúng MP4 hash trên cho owner. Hai câu hỏi riêng: (1) khi phát áo sạch, không rung/nhấp nháy khó chịu; (2) “Khoan” đúng Khoai/K20, rõ lời và khẩu hình chấp nhận được. Trạng thái tại lúc viết: cả hai **PENDING**. Approval thao tác local không là media approval; giữ audio gốc chưa được nghe không kế thừa approval C02/preset.

Chưa chọn BM range/EDL, chưa kiểm A→BM→BR→C02; contact Đào ngoài khung UNKNOWN. BR, paid retry, reserve và finishing giữ. Nếu owner phát hiện áo/voice/sync lỗi, ghi đúng artifact/range và giữ HOLD; không tự mở Flow hoặc ghép tiếng che lỗi.

Chi REC254=0, Flow submit0, không cài mới. Ledger dự án108/500, còn392, đợt34/34, reserve110 đóng; account balance972 là lần kiểm REC253, không truy vấn lại ở lượt local này.
