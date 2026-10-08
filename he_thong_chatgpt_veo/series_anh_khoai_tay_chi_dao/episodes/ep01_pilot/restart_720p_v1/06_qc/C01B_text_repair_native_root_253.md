# REC253 — Kết quả một lượt sửa chữ trên T02

Kết luận root: **REWORK / NOT_SELECTED / BR_HOLD**. Flow nhận request và tạo video, nhưng chữ “Khoan” vẫn còn. Không gọi có output là sửa thành công. Không chạy lại, không mở BR hoặc reserve.

## Nguồn và thực thi

Owner duyệt đúng một lượt tối đa 20 credit, nâng trần đợt 34. Source/draft hash kiểm lại khớp phản biện độc lập 252; live readback khớp, đúng video ingredient T02, Omni 1.1 Flash, 720p, 9:16, 4s, x1, Agent OFF, quote 20. Submit đúng một lần. Agent preflight mới trả lỗi giới hạn lượt dùng; root lúc submit đóng delta authority/live dựa trên review giấy 252 còn đúng artifact. Closeout phát hiện agent đã lưu report 253 (GO_FOR_ONE_AUTHORIZED_SUBMIT); root đọc đầy đủ **sau submit**, không backdate thành đã đọc trước click. Không có review độc lập output mới.

Kết quả editor asset `c770979b-e6ff-48f4-995f-8aab825b8f39`, tên “Remove white dialogue from shirt”, history đúng prompt sửa. Tải bằng menu **720p kích thước gốc**; không tăng độ phân giải. File tải `C:/Users/PC/Downloads/Remove_white_dialogue_from_shirt_20261008133127.mp4`. Bản workspace và archive đều cùng SHA-256 `f239491082af1f1f1cdcd55fd9a5afdb1ab9fb5d3ca923ee06665bcef6f7193c`. Không ghi đè T02 gốc.

## Kiểm kỹ thuật và hình

- H.264, 720×1280, 24 fps, 96 frame/video 4s; AAC stereo 48 kHz/audio 4,01s; tổng 4,01s. Full decode thành công.
- Trích đủ 96 PNG và timestamp, hai board 6 fps; tạo thêm 12 board đối soát, **mỗi output frame đều xuất hiện**, source ghép theo timestamp gần nhất. Root đã xem cả 12 board; xem riêng native F23 và F58. Đây là kiểm frame, không xem AV liên tục hoặc review độc lập.
- F0–22 không có chữ thoại. **F23–57 vẫn có “Khoan”**, 35 frame, khoảng `[0,958333; 2,416667)` giây. F58–95 sạch chữ thoại. Biên chữ không được loại bỏ so với T02 gốc. Khẩu hình tại F23–32 nằm trong vùng có chữ; không có căn cứ lấy đầu/đuôi môi khép thay wholeword.
- Ở mức quan sát board, mặt, ánh nhìn sang phải, tay đặt bàn, bát/đũa nằm yên và món nguội tương ứng nguồn; chưa thấy sai khác lớn mới. Không suy mọi pixel, performance hay các điểm nối đạt. Không crop, freeze, mux hoặc cắt để che failure.

Evidence: `C:/Users/PC/Downloads/du_an_nem_bui/253_BM_TEXT_REPAIR/native_qc/` và `comparison/`. F bắt đầu từ 0; PNG bắt đầu từ 1.

## Tiếng và giới hạn

Decoded PCM hai nguồn cùng channels/rate/width và 192.480 frame audio, nhưng **không bit-exact**. Hash PCM nguồn `4c4bbe1c14ad2f6184c6b64bd310c9187245929e323dc64685fdff5484686c0c`; bản sửa `bf9607c8d17e4f10ced7faa73921df4fdb5ff2d7f0f37d406a5990183495b896`. Tương quan zero-lag overlap 0,985992 chỉ là số đo tương ứng, không chứng minh giọng hoặc khẩu hình đúng; khác biệt có thể do encoding hoặc xử lý khác, chưa cô lập nguyên nhân. **Chưa thực nghe, chưa owner duyệt tiếng T02/bản sửa, lip-sync NOT_CERTIFIED**. Không yêu cầu owner nghiệm thu toàn take lỗi rõ.

## Chẩn đoán và quyền kế tiếp

Đã loại trừ nhầm source/draft/quote trước submit và nhầm bản tải theo provenance hiện có. Failure quan sát được ở output video-to-video: vùng chữ cần sửa vẫn giữ. Chưa biết backend bỏ qua yêu cầu, tái tạo chữ hay áp dụng biến đổi quá ít; không kết luận một cụm prompt là nguyên nhân duy nhất. Tuyến prompt-only edit này chưa chứng minh khả năng xoá chữ, vì vậy không lặp lại chỉ bằng nhấn mạnh câu cấm chữ.

Review output độc lập **chưa thực hiện** vì agent bị giới hạn; không cần reviewer PASS để root chặn lỗi hiển nhiên, nhưng không tự đóng gate độc lập. Số dư live 992→972, thực chi 20; dự án 108/500, còn 392; đợt 34/34. BR, retry và reserve không được cấp quyền. Bước tiếp cần trình hướng xử lý khác có capability/quote/nguồn cụ thể; chưa chọn hoặc triển khai công cụ mới.
