# REC304 — Khôi phục trình duyệt phải kiểm cấu hình mới

- Phiên cua mới làm mất handle cũ. Inventory hiện trình duyệt tích hợp với danh sách tab rỗng; mở đúng URL project đã biết trong IAB, không tự chuyển sang Chrome hoặc công cụ khác.
- Trong phiên mới, model/route/720p/dọc/x1 còn đúng nhưng thời lượng tự về 8 giây, quote 12. Không dùng last-known 4 giây/7 credit. Đã chọn lại 4 giây và đọc lại quote của cả gói.
- Chọn option có thể chỉ mở preview hoặc có thể gắn trực tiếp tùy loại/trạng thái UI. Sau chọn phải đọc state rồi mới quyết định bấm “Thêm vào câu lệnh”; không lặp chọn hoặc bấm add theo giả định. Lỗi locator trước không được diễn giải là đã gửi request.
- Reuse ảnh F47 hiện có; chỉ upload portrait mới một lần. Kiểm tên preview, hai image chip và một saved D06. Không click chip để “xem” vì có thể tháo thành phần; đọc DOM/saved picker và screenshot.
- Duyệt ảnh không duyệt chi. Khi bucket tạo lại còn5 nhưng quote7, đề xuất chuyển2 phải ghi riêng là PENDING và chờ owner; không trừ chi, đổi sổ hoặc tự lấy ngân sách dự phòng.
