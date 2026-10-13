# REC290 — Đúng sắc thái không tự giải quyết bảo toàn ảnh vào

Owner chọn sắc thái B; brief v0.2 bỏ gồng/dò phản ứng. Điều đó không cấp diễn xuất đạt cho một ảnh hoặc take mới.

Một phép sửa ảnh tích hợp đã yêu cầu chỉ đổi đĩa nem và A, giữ toàn vùng khác. Nguồn là đúng cuối C05, không START ở cuối C06 hoặc END sau nhận. Đã xem nguồn/hai ảnh nem thật và ghi prompt exact trước chạy. Candidate 941×1672 có món rời hơn nhưng redraw vùng ngoài món, mất dấu nguồn và thay hình/độ rủ của A. Root không chọn, không upload hoặc thay refs hoạt động; nguồn/hash giữ nguyên.

**Phân biệt nguyên nhân:** prompt có yêu cầu giữ nguyên; output vẫn không giữ. Đây là bằng chứng giới hạn bảo toàn ở lượt sửa whole-image này, không đủ quy một từ khóa hoặc mọi model. Không chấm món cải thiện rồi bỏ qua mặt, trang phục, hậu cảnh và dấu nguồn. Resize/redraw không phải bảo toàn pixel; ảnh gần 9:16 không phải native 720×1280 đã khóa F0.

**Cơ chế tiếp theo cần đề xuất:** giới hạn vùng sửa thật hoặc ghép riêng món vào nguồn, có vùng biên/light/shadow và continuity check. Chưa có mask-lock hoặc composite được thực hiện/kiểm; không nhận là đã có công cụ hay chắc sửa được. Nếu cần script/media-edit khác phương thức đã thống nhất, trình trước; không tự dùng Python sửa ảnh hoặc tự xóa/vẽ lại dấu nguồn.

Chỉ một ảnh được tạo, không Flow/video request hoặc retry. Không kết luận mọi tạo ảnh miễn phí. Sổ Flow không trừ trong vòng này; 237/500 còn 263, dự phòng 110 đóng. Cổng hình món C05/các cảnh trước còn mở dù candidate C06 có vật liệu tốt hơn.
