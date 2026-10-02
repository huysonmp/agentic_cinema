# EP01 — đăng ký ba lượt Lite cho hai câu mở

Ngày: 2026-10-02. Trạng thái: ĐÃ TẠO ĐỦ BA CLIP / CHỜ FILE LOCAL ĐỂ QC.

## Quyết định chủ dự án

Yêu cầu chạy ba lượt Lite và đối chiếu đã thay thế đề nghị một lượt tại tài liệu 126. Gói này dùng nguyên văn prompt tại `126_opening-dialogue-action-lite-request.md`, không thay kịch bản hoặc staging giữa các lượt.

- Mục tiêu: kiểm hai câu mở, lượt nói và động tác tay trái Đào định kéo đĩa rồi dừng khi Khoai ngăn.
- START: `C:/Users/PC/Downloads/du_an_nem_bui/T2-CODEX-OPEN_v0.7.png`; SHA256 `A3D80F09BFB7242BAE3007AD7B4F37473BB2F0ED019A84CC4956C4D32A8DBF9A`. END để trống.
- Dự kiến: Veo 3.1 Lite, Frames, 9:16, 720p, 8 giây, x1; ba lần gửi độc lập R01–R03. Phải kiểm cấu hình và báo giá thực tế trước khi gửi.
- Giới hạn: 10 credit/lượt, 30 credit/bộ. Ngân sách thử cũ đã dùng 130/200 theo hồ sơ trước; cần đối soát số dư hiện tại. Không dùng ngân sách Quality 100 hoặc khoản V02.
- Không retry sau bộ ba, không nâng OPEN7 thành chuẩn sản xuất cuối, không tự duyệt giọng hoặc điểm nối.

## Nhật ký

| Lượt | Gửi | Tài sản | File / hash | Chi phí | Trạng thái |
|---|---|---|---|---|---|
| R01 | 10:30:43, giờ Việt Nam | `61bf42a2-f657-49a4-919f-5f4c2faa64d1` | Chưa nhận file local | Báo giá 10 | Đã tạo, tải chưa đối soát được |
| R02 | 10:31:00, giờ Việt Nam | `cee4efc6-5ac8-489c-9239-6c2b4e7f35f0` | Chưa nhận file local | Báo giá 10 | Đã tạo, tải chưa đối soát được |
| R03 | 10:31:10, giờ Việt Nam | `420ba168-25fc-44ab-a05f-3c64337d3f20` | Chưa nhận file local | Báo giá 10 | Đã tạo, tải chưa đối soát được |

Số dư trước: 920; sau: 890 credit, đọc trực tiếp trên Flow. Chênh lệch quan sát 30, khớp ba báo giá 10; đây không phải hóa đơn riêng từng lượt. Tổng thử cũ cập nhật 160/200, còn 40; Quality 100 chưa dùng trong bộ này. Giao diện đã xác nhận Veo 3.1 Lite, Khung hình, 9:16, x1, 720p/8 giây, 10 credit. Bằng chứng local: `artifacts/opening127-r1/settings.png`, `pre-r01.png` đến `pre-r03.png`, `result-r01.png` đến `result-r03.png` và `batch-results.png`. R02/R03 dùng chức năng sử dụng lại câu lệnh, đã kiểm ảnh đầu trở lại và END vẫn trống. Không sửa prompt giữa các lượt.

## Điểm cần review

Đúng người/thứ tự và đủ hai câu; giọng Khoai ấm, trầm vừa và kể thân mật; Đào trưởng thành, trêu nhẹ; tay trái tiếp cận đúng đĩa, tay phải và hai tay Khoai giữ nguyên; không đổi món, rau, chấm, bát, đũa hoặc cốc. Đồng bộ môi và chất giọng cần nghe/xem thật. Điểm nối từ B chưa đạt chỉ vì cùng ảnh: phải kiểm sai lệch scale và frame thực tế.

## Gián đoạn trước khi gửi

Kết nối trình duyệt đã đổi phiên trong lúc khôi phục tab. Đã tìm lại đúng dự án Flow, chưa bấm tạo và chưa phát sinh credit trong các thao tác này. Không gửi lại một yêu cầu chỉ vì mất kết nối; phải kiểm trạng thái dự án trước.

Đã xác định: bộ ba cùng điều kiện đã có kết quả trên Flow, số dư giảm 30. Đã chốt: dừng tại ba lượt. Giả định chưa kiểm: hai câu vừa cửa sổ 8 giây. Còn mở: file native, QC và đánh giá nghe/xem. Tiếp theo: chủ dự án hỗ trợ tải ba clip → kiểm local → hoàn thiện so sánh 128. Quality vẫn HOLD.
