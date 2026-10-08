# 253 — Một lượt sửa chữ đã chạy, kết quả chưa đạt

Owner duyệt một lượt sửa tối đa 20 credit, trần đợt 34, chưa bao gồm BR và không mở dự phòng. Đã chạy đúng một lượt video-to-video từ T02 solo, quote/thực chi 20, số dư 992→972. Đã tải native 720×1280/24fps/96 frame/4s riêng, đối soát hash ba bản tải/workspace/archive.

**Kết quả: chữ “Khoan” vẫn còn F23–57. Không chọn take, không tự chạy lại, BR giữ.** Root đã xem đủ 96 frame qua 12 board so nguồn và kiểm native F23/F58; chưa nghe thực hoặc chứng nhận sync. Agent mới báo giới hạn lượt dùng nhưng đã lưu preflight253; root phát hiện/đọc lúc closeout, không backdate thành đọc trước submit. Lúc click dùng review giấy252 cùng hash và kiểm delta authority/live; chưa có review độc lập output mới, không thành media PASS.

Tổng dự án đã chi **108/500**, còn **392** gồm 133 lượt đầu, 104 tạo lại, 45 sau rough và 110 dự phòng chưa mở. Đợt hiện tại đã chi **34/34**; số dư tài khoản 972 không phải quyền chi tiếp.

Đã xác định: tuyến sửa nhận được request nhưng không xoá được chữ ở lượt này. Đã chốt: giữ yêu cầu hình sạch, một lượt không retry. Giả định chưa được chứng minh: edit có thể giữ performance/audio; PCM tương ứng nhưng không bit-exact, chưa kết luận đổi voice. Còn mở: cách xoá chữ khả thi, review độc lập output, tiếng/sync và chuỗi BM→BR. Bước tiếp: trình phương án khác với bằng chứng capability/nguồn/giá trước khi chạy; không sinh thêm cùng prompt.

Hồ sơ chi tiết: [kiểm native](restart_720p_v1/06_qc/C01B_text_repair_native_root_253.md), [registry](restart_720p_v1/06_qc/run-registry-253.json), [kinh nghiệm](restart_720p_v1/09_lessons/REC253_prompt_only_video_text_repair_failure.md).

Evidence và footage trong `C:/Users/PC/Downloads/du_an_nem_bui/253_BM_TEXT_REPAIR/` và `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/05_native/EP01_720_C01B_BM_T02_TEXT_REPAIR_T01_NATIVE.mp4`. Original T02 được giữ nguyên.

## Đề xuất kế tiếp, chưa triển khai

Xin duyệt một bản hậu kỳ **cục bộ vùng chữ** bằng công cụ local đã có, từ T02 gốc; lấy vùng áo sạch ở khung gần làm nguồn phục hồi, chỉ tác động phần áo bị chữ che. Không sinh lại, không dùng credit, không cài hoặc kết nối thêm. Giữ face/mouth/hands ngoài vùng sửa và copy audio stream nguồn; không crop hoặc freeze toàn cảnh. Khả năng vùng áo khớp chuyển động chưa chứng minh, phải kiểm cả 96 frame và file đầu ra; không hứa đạt. Nếu viền/nếp áo rung, giữ NOT_SELECTED. Source voice vẫn chưa được nghe/duyệt; hình sửa đạt không thay cổng tiếng/sync. Đây là phương án cần owner cho phép, chưa tạo bản sửa local.
