# REC278 — Kiểm tổ hợp tính năng trước khi hứa neo hình

Ngày 13-10-2026. Owner chọn A để chuẩn bị, không trả phí. Kiểm trực tiếp Flow và hai trang Google được ghi tại `06_qc/C07_live_feature_check_278.json`.

## Quan sát

Omni1.1Flash có modeFrames với Start/End. UI và [hướng dẫn Google](https://support.google.com/flow/answer/16353334?hl=en) cho thấy savedvoice references thuộc Ingredients, không là kết hợp Start+End+voice. [Bảng model](https://support.google.com/flow/answer/16352836?hl=en) liệt kê mỗi tính năng nhưng không chứng minh dùng chung trong một request. Không sinh thử một tổ hợp trái hướng dẫn để kiểm điều đã rõ.

Ảnh C06F56 từng mang tên START nhưng ở request277 là **image ingredient**, không phải explicitSTART slot. Tên file/ý đồ/prompt không thay loại trường nhập thực. Trong278 đã đưa chính ảnh đó vào explicitSTART để quan sát rồi trở vềIngredients; không có output hay bằng chứng chuyển động nào từ bước chuẩn bị này.

## Kiểm soát áp dụng

- Đọc tổ hợp tính năng, không chỉ từng feature. Chốt voice identity là dependency nghệ thuật; không đổi voice để lấy mode neo hình thuận hơn.
- Tách vai reference: scene giữ camera/props/pose; portrait giữ identity; voice giữ speaker. Thêm ảnh portrait không biến Ingredients thành pixel-exactF0.
- Ảnh sinh từ predecessor vẫn có drift; kiểm side-by-side mặt, lá/cuống, màu/material, cỡ đầu và quần áo trước owner dùng. Không lấy ảnh đẹp làm master mới hoặc dùng portrait cho movement endpoints.
- Preflight đủ mới trình một request sauSTOP; approval chuẩn bị/ảnh không cấp paid. Quote phải đọc lại sau đủ inputs, không dùng quote cấu hình chưa đủ làm biên lai hoặc dự báo đạt.
- Xem toàn source mới theoidentity→props/owner/hands→entry→action→seam→voiceAV. Khóa tác dụng thật bằng thực kiểm, không bằng nội dung prompt hoặc giấy maker/reviewer.

Nguồn278 mới là portrait ứng viên; chưa uploadFlow/submit/video/voicepreview,0Flowcredit. C08HOLD;293projectremaining và reserve110 đóng giữ nguyên. Không bổ sung memory cá nhân hoặc thay công cụ/API/cài đặt.
