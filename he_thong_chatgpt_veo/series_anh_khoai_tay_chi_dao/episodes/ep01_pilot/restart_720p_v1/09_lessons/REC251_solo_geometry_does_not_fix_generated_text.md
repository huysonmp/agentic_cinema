# REC251 — Solo coverage không tự sửa chữ do model sinh

## Quan sát đã kiểm

Một request được owner duyệt, preflight độc lập và live gate đầy đủ: ảnh v2 không chữ, chỉ Khoai; saved custom K20 đúng UUID; prompt readback bằng nguồn; Agent OFF; Ingredients / Omni 1.1 Flash / 720p / 9:16 / 4s / x1, quote7. Native gốc vẫn có chữ “Khoan” trên áo trong đoạn miệng chuyển động. Root xem 24 mẫu 6fps và 8 khung full resolution, gồm các biên F22/23 và F57/58; đây là evidence hình lấy mẫu và biên, không phải nghe/AV liên tục.

Lỗi chữ có trong file native mới, trước trim/EDL/export. Cảnh solo/hai tay nghỉ được giữ ở mẫu kiểm, nhưng không thể coi việc đó đóng blocker chữ. Duyệt preset hoặc ảnh không chuyển thành duyệt tiếng, hình hoặc khẩu hình nguồn mới.

## Truy chuỗi nguyên nhân

- Reference: không có chữ ở ảnh đã duyệt; không có chữ Khoan để model sao chép từ ảnh.
- Request: nói một từ Khoan và yêu cầu spoken audio only / không lettering, captions, speech bubbles. Không thiếu ràng buộc chữ trong bản gửi; nội dung UI đã đối chiếu bằng file.
- Take: chữ xuất hiện ngay ở native. Tầng phát sinh xác định được là generation, không phải tải xuống, cắt ghép hoặc caption local.
- Model/provider mechanism: UNKNOWN. Hai take BM249/251 cùng model/route/voice và một từ thoại đều sinh chữ; ảnh/cỡ cảnh và wording thay đổi không loại lỗi. Không đủ controlled experiment để nói một từ prompt, preset hay việc thoại quá ngắn là nguyên nhân duy nhất.
- Process: preflight bảo đảm input/quyền/configuration đúng, không bảo đảm model tuân thủ. Native QC đã chặn lỗi trước BR và trước bàn giao; phải giữ checkpoint này.

## Hệ quả và bước cần quyết định

Không tự thử lại cùng route khi chữ đã lặp; không chuyển lượt BR thành retry, không lấy đoạn môi khép rồi overlay tiếng để giả đạt, không crop chữ mà mất mặt/tay hoặc giả clean source. Tạm giữ nguồn để đối chiếu; chưa đưa vào EDL.

Có thể trình owner một thay đổi tiêu chí nghệ thuật: giữ chính chữ thoại như một chữ nhấn có chủ ý, nhưng chỉ nếu owner chấp nhận và sau đó kiểm tiếng/khẩu hình/cut thực. Nếu vẫn bắt buộc nguồn sạch, cần một hướng xử lý mới có giả thuyết, evidence khả năng công cụ và quote được duyệt, không chỉ đổi vài tính từ rồi chạy lại. Đây là lựa chọn chưa chốt, không là authority sinh thêm hoặc nghiệm thu.

Thực chi7, cùng account999→992; đợt coverage14/30; tổng scoped project88/500; còn412 gồm110 dự phòng vẫn đóng. BR chưa chạy, actual listening NOT_PERFORMED.
