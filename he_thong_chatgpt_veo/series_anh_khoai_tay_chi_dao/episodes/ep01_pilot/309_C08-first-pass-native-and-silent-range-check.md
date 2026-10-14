# REC309 — C08 lượt đầu: đã thả A, chuẩn range không thoại

Ngày 14/10/2026. Gói C06→C07 được owner duyệt tại REC308. C08 là lượt sản xuất đầu trong kế hoạch236 theo quyền tự vận hành REC238, không sử dụng lại quyền tạo lại C07 tại REC305 hoặc mở dự phòng.

## Chạy và lưu thực

Preflight308 qua reviewer, root đọc toàn report. FINAL309 khớp byte draft đã review, SHA `2295314fe3e26e7bb81bc9be6a5c2ae692cf7a02982bc9e09857eaf30902ca74`. Một START đúng J119 acceptedjoin, ID355f1b27-79a2-4d27-89b6-a15459e62cc1; không END tự chế, không voice. UI Frames/Omni1.1Flash/720p/9:16/4s/x1, Agent OFF, return-without-audio TRUE, quote7 và prompt exact readback.

Đã bấm tạo đúng một lần, asset `37a82feb-5e7a-42d7-b267-f241fbac5a52`. Số dư tài khoản 1.015 → 1.008: chi đúng 7 credit. Sổ dự án: 272/500 đã dùng, còn 228; tạo mới 73 / tạo lại 0 / hậu kỳ 45 / dự phòng 110 đóng. Không chạy lại.

Native `EP01_720_C08_DEPOSIT_A_T01_NATIVE_309.mp4`: SHA `32542320b20b2c6dc2dd9673c0a6bec46c904e3e23917e0620d0baecf61efc0e`,793.562byte,720×1280/24fps/96F/4s, decode toàn tệp sạch. Download/repo/owner copy khớp hash. Skill computer-use giữ thao tác qua UI, chọn720p kích thước gốc và đối soát quote/balance; không API ẩn hoặc tạo lại vì tải.

## Root kiểm actual

Đã xem đủ sáu bảng dày, bao phủ 96 khung, và ảnh nguyên khung F0/F32/F42/F52/F60/F64/F68/F72; đối chiếu START nguyên khung. Khoai vẫn củ khoai, Đào vẫn quả đào; hai bát, tay riêng, cốc và bàn giữ. A hạ tới bát Đào đang cầm, nhìn nằm trong bát, đầu đũa rút ra trống về phía Khoai; không thấy gắp phần khác, ăn hoặc trả A về đĩa chung. Môi nhìn khép, không khói. Tiếp xúc bị che một phần bởi vành bát; đây là kiểm toàn ảnh khung, không phải đã xem chuyển động liên tục hoặc chứng nhận vật lý.

Đuôi sau rút đũa có thêm động tác Đào hạ bát/cốc và đặt bát về bàn; không chọn cả 4 giây. Root khảo sát [0,64), F0–63 / 2,666667 giây: đầu đũa đã rời và A còn trong bát tay trong, cốc vẫn nâng tay ngoài. Chưa chốt range production từ kết quả root riêng.

## Âm thanh thực khác suy đoán UI

Native vẫn có AAC và PCM khác0 dù toggle TRUE; không báo “native không tiếng”. ASR “Ơm...” chỉ là nhận dạng máy, root chưa nghe. Không kết luận giọng Khoai/Đào hoặc nguyên nhân model từ dữ liệu này. Đã tạo derivative riêng của C08 không thoại, bỏ track âm phát sinh, giữ nguyên native; không đổi các track K20/D06 đã duyệt.

Candidate `C08_DEPOSIT_F0_F63_SILENT_REVIEW_309.mp4`, SHA `a152f5bf1b4070df58aede9c55d45226d8b5cd1ef91833e0807bd7a3d2f9a724`:64F/24fps/2,666667s, videoONLY, decode sạch. Root xem đủ4 denseboard64F và fullencodedF63; không thấy lỗi nhận diện/miệng/props mới. EDL trial309 ghi đúng trim và loại audio riêng. Không giả native im tiếng hoặc dùng silence làm chứng nhận điểm nối âm thanh.

## Review, timing và bước tiếp

Nhiệm vụ actual độc lập đã giao; khi đóng report phải root đọc toàn văn trước chọn range hoặc dùng endpoint C09. Không ghi reviewerPASS chỉ từ dispatch. Audit timing toàn tập đã giao EDIT, chưa có báo cáo ở thời điểm viết.

Cập nhật trong cùng vòng: reviewer `/root/c08_actual_309` đã hoàn tất `C08_actual_fresh_independent_309.md`, root đọc toàn văn. Reviewer tự hash/count, xem toàn96 native +64 encoded và từng full nativeF32–64, full encodedF63. Không thấy MAJOR trong prefix; release nhìn thấy F34–39 và tips clear F56–63. Conditional GO dùng exact encodedF63 cho chuẩn C09; hidden clearance/continuousAV và owner rough/final giữ mở. Không đồng nhất conditional source với owner đã duyệt C08 hoặc toàn native4s. Nhánh reviewer cũ đang pending không được ghi hoàn tất thay cho report mới có bằng chứng.

Nếu dùng64F này: throughC07=752F→throughC08=816F/34s; rough35 chỉ còn24F/1s cho C09, final30 đã vượt96F/4s trước cảnh kết. Không tự bỏ B/C09, tăng tốc hoặc chốt final35; cần range C09 thực và audit phần đệm/cut phía trước. Food seam C05→C06 vẫn riêng. Đây là lý do phải đo, không hứa đã xong video30s.

Timing audit độc lập mới đã hoàn tất tại `06_qc/EP01_TIMING_candidate_margin_audit_fresh_309.md`; root đọc toàn báo cáo. Số đếm 632 + 120 + 64 = 816 khung khớp. Candidate khảo sát C02 [16,173) và C04 [12,144) có thể tiết kiệm 36 khung nếu kiểm nghe–nhìn và điểm nối đạt; hiện chưa dựng, chưa có tiết kiệm được nghiệm thu. Giữ nguyên block308, lời, giọng và tốc độ; không dùng phép tính này để hứa final30.

Folder owner `C:/Users/PC/Downloads/du_an_nem_bui/309_C08_DEPOSIT_A_T01/` giữ native và bản xem im tiếng. Chưa chạy C09, chưa thay EDL toàn tập hoặc duyệt bàn giao. Bước tiếp là đóng kiểm range/đường A, kiểm nối từ C07 đã duyệt và chuẩn C09 từ khung ra đạt, rồi nghiệm thu toàn tập theo cổng bản dựng thô REC238; không hỏi lại từng thao tác nội bộ.
