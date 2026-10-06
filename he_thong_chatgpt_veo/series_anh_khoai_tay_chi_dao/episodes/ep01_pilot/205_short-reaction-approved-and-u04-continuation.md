# EP01 — Duyệt phản ứng ngắn, tiếp tục cảnh nâng/khựng tay

Ngày 2026-10-06. Owner trả lời: **“Duyệt phản ứng ngắn, tiếp tục theo ngân sách còn lại”**. Approval đúng bản cắt 0–0,625 giây/15 frame tại204, SHA256 `3470254b657ecc371fb29d7def13a972302b6f05f8ec5afb2e7cccc7996f7e81`; không duyệt cả clip tám giây có môi mở. Giữ nguyên tiếng202/C-v0.6/K20/D06.

[Timeline205-v0.3](evidence/205/timeline-v0.3.json) là bản làm việc hiện hành, chưa render phim cuối: S05 frame431–512, S06 frame512–527, S07 frame527–590. Bù21 frame phản ứng vào nhịp nâng/khựng tay Khoai; tổng720 frame/30 giây. U04 cần sáu giây sạch: dự kiến0–3,375s và3,375–6s, không dùng một range hai lần. Timing thoại không đổi; việc đạt nhịp vẫn phải kiểm actual.

## Kiểm nguồn U04

Root đã xem lại actual START: `C:/Users/PC/Downloads/du_an_nem_bui/192_approved_pickup_join/inputs/P02_APPROVED_OUT_frame59.png`; SHA256 đúng `db95be527d709dd39bb1107f5ac94a036bc480be28691d2c64b694112ae640c8`, 720×1280. Đây là frame cuối đoạn P02 đã chọn về nhịp, không thay bằng endpoint ảnh sinh188.

END ứng viên198 tái tạo làm đổi góc lòng bát, chi tiết món và ánh sáng. Không chứng nhận continuity hoặc upload như endpoint đã duyệt. Quyết định triển khai: **dùng START native duy nhất**, bỏ END tái tạo để tránh ép clip biến đổi đồ trên bàn theo nguồn khác. Đây là lựa chọn kỹ thuật trong gói sản xuất đã giao, không thêm lượt hoặc đổi câu chuyện. Endpoint chuyển động phải lấy từ output thật; không tự báo input một frame bảo đảm tay/món không biến dạng.

Chỉ đạo U04: nâng đúng một phần nem đã gắp, dừng trước cổ áo/miệng, giữ tay và miếng nem đến sáu giây; bát riêng còn rỗng, đĩa/rau/chấm và tay nghỉ không đổi; không nhai, thêm phần ăn hoặc hơi nóng. Mặt nằm ngoài khung, tiếng N05 ngoài hình. Phải kiểm quote/model/x1 và nguồn trước gửi, sau đó decode/frame/entry–exit; không chi lượt sửa nếu vượt dự phòng3.

Sổ trước U04:349/422/còn73. Dự kiến một x1 giá10 →359/còn63; sáu đơn vị sau dự kiến60, dự phòng3. Không coi số dư account127 là quyền chi. Chưa Quality/API/phát hành hoặc AV/master PASS.
