# Review M1 — câu cấm hơi và bằng chứng nhân quả

Ngày 2026-10-02. Owner duyệt phép thử đề xuất 138; request và prompt nguyên văn ở 139. Root thực kiểm local, không gọi là review agent độc lập. Không chọn winner, không Quality.

## Dữ liệu thực

Ba MP4 tại `D:/Workspace/agentic_cinema/artifacts/opening139-r1`, bản xem tại `C:/Users/PC/Downloads/du_an_nem_bui/139_negative_sentence_control`. Cả ba 720×1280, 24 fps, 8 giây, có stream hình/âm thanh, giải mã ffmpeg exit 0. Âm thanh chưa nghe thật; không chứng nhận ambient, giọng, lời hoặc lip-sync. Số dư đọc trực tiếp 770 → 740, ròng 30, tổng thử 310/400 còn 90; không mua/nạp thêm và không dùng Quality.

| Mẫu | Asset ID | Tên file gốc | Byte | SHA-256 |
|---|---|---|---:|---|
| C01 | 7ac9fcb5-d812-4c3d-9157-d7b1c72afd65 | Subjects_holding_starting_poses_20261002154601.mp4 | 3861783 | DE66862B687E6706D3D68611DAEF91E0CBAC515338671BB21F3EBAFC89203567 |
| C02 | dea7fa72-fc3c-4c36-b397-a1712308cd01 | Subjects_holding_starting_poses_20261002154707.mp4 | 2457646 | 953E88EEC02EEA0A88BA0386CC9E10E0B3059BD5FFCE8715D3CB2BF6C240868F |
| C03 | a59dd562-d4bc-4634-9ad1-f4ed39e79ae5 | Subjects_holding_starting_poses_20261002154829.mp4 | 2682319 | C4F813CE9BA45C95013D4CBCC00D4B7A69D20EBD1C75786C80ED75A67D98B375 |

Bằng chứng UI: `preflight.png`, `download-C03.png`. Mỗi clip có contact sheet `C01-sheet.png` đến C03, lấy 16 mẫu mỗi 0,5 giây (0–7,5). Khung C02 2,5 giây `C02-2p5.png` được xem ở độ phân giải gốc để xác minh vệt trắng; không chỉ suy từ thumbnail. Media/ảnh không commit vào Git.

## Quan sát và đánh giá

| Mẫu | Hơi trắng | Lỗi khác trong ảnh mẫu |
|---|---|---|
| C01 | Có vệt trắng vùng trên đĩa/bát và giữa hai nhân vật từ khoảng 1,5–2 giây, rõ ở giữa clip | Khung tiến gần dần dù yêu cầu locked tripod; nhân vật mở miệng và Khoai giơ tay cuối clip |
| C02 | Có, rõ khoảng 2,5–3 giây và lặp ở giữa/cuối clip; khung 2,5 giây thấy vệt trắng từ vùng bàn lên giữa hai nhân vật | Cả hai mở miệng/giơ tay ngoài yêu cầu; chưa thấy chữ thêm ngoài watermark |
| C03 | Có, thấy khoảng 1,5–3,5 giây và những mẫu cuối | Khoai giơ hai tay đầu clip; Đào mở miệng; chưa thấy chữ thêm ngoài watermark |

Thời điểm là nhãn mẫu xấp xỉ, không đo onset/offset toàn clip. Có thể xác nhận vệt hơi không mong muốn hiện diện trong native video, trước Canva/ghép/xuất master. Không thể từ một khung xác định chính xác điểm phát hơi hoặc nhiệt độ thực của món; không phân loại vệt giữa hai người là hơi thở khi chưa có căn cứ. Vệt trắng ở vùng serving không phù hợp mô tả món nguội. Bàn/serving vẫn tương đối giữ nhưng C01 camera drift làm khung thay đổi. Không dùng kỹ thuật file sạch để bù lỗi nội dung.

Kết luận: **STEAM_OBSERVED_3_OF_3 / POSE_REWORK / C01_CAMERA_REWORK / NO_PRODUCTION_WINNER**. Không cần xem hết mọi frame để xác nhận lỗi đã hiện diện, nhưng chưa kiểm toàn bộ chuyển động hoặc âm thanh và chưa có review độc lập.

## Đối chiếu M0 và truy nguyên nhân

- M0 (137/138): cùng OPEN7, 3 mẫu, chưa thấy hơi trong 16 mẫu mỗi clip; vẫn có cử chỉ tay/miệng tự sinh.
- M1 (139/140): chỉ thêm câu cấm `No steam, smoke, vapor, heat shimmer or animated scent trails rise from the food.`; 3 mẫu đều thấy vệt hơi trắng. Trước gửi đã xác minh fallback câm tắt; M0 có audio stream nhưng switch không được đọc lại khi gửi, cần giữ giới hạn này trong hồ sơ.
- **SUPPORTED, chưa CONFIRMED:** kết quả hỗ trợ câu thêm trong prompt chính Flow là yếu tố góp phần. Chưa biết cơ chế, không xác nhận từ riêng `steam`, không kết luận mọi negative prompt/API đều gây lỗi. Hai bộ khác thời điểm, không ghép seed và chưa tái lập control.
- **Đã khoanh vị trí phát sinh:** lỗi hiện trong video native, không phải do tải xuống, ghép Canva hoặc master export. Ảnh OPEN7 không buộc mọi đầu ra đều có hơi, nhưng vẫn có thể tương tác với prompt/ngữ cảnh. Không kết luận ảnh nguồn vô can tuyệt đối.
- **Lỗi lọt cổng:** các lần thêm câu cấm trước kia chưa có control một nhóm; nhầm nỗ lực sửa prompt với hiệu quả đã kiểm chứng. Quy trình cần actual input + phép thử tách nhóm + reviewer kiểm lỗi vật lý món, không chỉ kiểm cảnh đẹp.

## Bước tiếp đề xuất — chưa gửi

Tái lập đúng M0 một bộ ba Lite cùng phiên tài khoản, giữ OPEN7/Frames/9:16/720p/8 giây và fallback tắt; chỉ bỏ câu thêm của M1. Tối đa 30 trong 90 còn lại. Nếu M0 lại chưa thấy hơi trong mẫu, tăng bằng chứng cho mối liên hệ câu cấm; nếu M0 có hơi, hạ độ tin cậy giả thuyết và kiểm biến thiên ngữ cảnh/model. Cả hai kết quả vẫn không giải quyết lỗi tự diễn tay/miệng.

Chưa tự chạy bộ này sau M1 vì đăng ký 139 dừng sau ba mẫu để review. Không thêm nhiệt độ, mô tả món, thoại hoặc hành động trong phép tái lập. Không nâng Quality và không đưa M0/M1 vào cảnh bàn giao chính thức. Sau khi truy đủ bằng chứng, xử lý diễn xuất bằng phép thử riêng; không gọi nguyên nhân gốc đã đóng chỉ vì tìm được workaround.
