# EP01 — Duyệt và thực thi thử gắp x3 Lite

Ngày 2026-10-05. Owner trả lời “duyệt” cho câu hỏi ở 189: thử riêng gắp từ đĩa về trước bát Khoai bằng ba Lite, bổ sung 7 credit, tổng chi batch không quá 30; phải đọc giá live trước chạy. Đây là approval gói thử cơ chế, không duyệt video/FOOD toàn cảnh hoặc mở Quality.

## Quyền và đầu vào đã khóa

- Trần dự án mới 262 (=255+7); đã dùng 232 trước lượt này, phần được phép còn 30. Account balance là nguồn đối soát riêng, không tự tăng quyền chi.
- Một bộ x3; không thêm batch hoặc chạy nâng/chuyển/đặt từ approval này. Giá vượt 30 phải hỏi lại. Refund/lỗi và chi ròng phải đối soát trước retry.
- START: `START_pickup_food_v0.1.png`, SHA256 `d91d902df4abac2f374616c9a3d2866f1478dce2a8fde39ebfcf027b287af16a`.
- END: `END_pickup_food_v0.1.png`, SHA256 `9b34523091aad6a679690b67f1e08df686bd3bf0138d5325bae142016f345f2f`.
- Giữ C-v0.6/K20/D06; SIA HOLD theo hoãn kiểm. Chất liệu188 đã duyệt; lượng/tỷ lệ, conservation và diễn động chưa đạt. Không dùng thử này để cấp FOOD toàn cảnh PASS.

## Trạng thái thực thi

Preflight đã kiểm trên đúng project `9276788e-9781-44fb-ba5b-083006667374`: Frames, Veo 3.1 Lite, 9:16, 720p, 8 giây, x3, giá live 30; Agent OFF, tùy chọn trả video không âm thanh ON. Hai ảnh188 đã upload và chọn riêng START/END; không giữ nhầm ảnh185 do picker chọn mặc định. Prompt trong compose đọc lại khớp văn bản lưu.

Gửi đúng một yêu cầu x3 lúc **2026-10-05T14:24:24.906Z** (21:24:24 giờ Việt Nam). Cả ba thẻ trả `Không thành công` với thông báo `We noticed some unusual activity` và `Bạn chưa bị tính phí cho lượt tạo này.` Không có video native, ID đầu ra, file tải, probe hoặc motion QC để báo đạt. [Ảnh lỗi](evidence/190/submitted.png) lưu sau khi ba thẻ báo thất bại.

- Account trước 244, sau lỗi 244, sau làm mới vẫn 244: chi ròng vòng này **0**, sổ dự án **232/262**, còn **30** trong quyền chi. Số dư account không thay thế trần dự án.
- Đã làm mới trang đúng một lần. Các thẻ lỗi biến khỏi lưới sau reload; không có bằng chứng lượt tạo thành công. Banner lỗi kết nối reCAPTCHA trước reload không còn trong snapshot sau reload, nhưng chưa chứng minh lần submit tiếp sẽ được chấp nhận.
- Không retry từng thẻ x1, không đổi trình duyệt/cơ chế để né chặn, không tắt bảo vệ hoặc xử lý CAPTCHA. Lỗi xảy ra trước khi có media nên không quy cho prompt/food/chopsticks hoặc đường tải. Cơ chế gốc của cảnh báo unusual activity **chưa xác định**.
- Nạp lại START/END và prompt nguyên bản; kiểm lại quote30, Lite/x3/Frames/9:16, silent ON. **Chưa resubmit.** Tab Flow giữ mở để owner bấm `Bắt đầu tạo` trực tiếp và tự xử lý xác minh nếu xuất hiện. [Gói chờ thao tác](evidence/190/handoff-ready-not-resubmitted.png).

## Gate và bước tiếp

Trạng thái: **EXECUTION BLOCKED — OWNER ACTION**, không phải motion REWORK/PASS. Chất liệu188 vẫn APPROVED_TEXTURE_ONLY; coverage mới0; SIA HOLD, C-v0.6/K20/D06 và bản ráp182 giữ nguyên. Chưa mở Quality/master hoặc hành động kế tiếp.

Owner thử bấm chạy đúng gói đang chờ (chỉ khi quote vẫn30), xử lý xác minh bình thường nếu có, rồi báo kết quả. Sau đó Codex đối soát đủ ba đầu ra/credit, tải native, kiểm hash/probe/full decode và review toàn đoạn trước lựa chọn. Nếu giá đổi hoặc tiếp tục bị chặn, dừng để xử lý phiên dịch vụ, không gửi lặp.

Nhật ký cấu trúc: [results.json](evidence/190/results.json). Không ghi pending card hoặc ảnh tĩnh là video đã tạo.
