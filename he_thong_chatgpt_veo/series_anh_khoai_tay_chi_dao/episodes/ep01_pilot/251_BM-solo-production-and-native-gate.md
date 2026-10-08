# REC251 — Sản xuất BM solo từ ảnh v2 đã duyệt

Ngày: 08/10/2026. Owner: “duyệt nhé,” cho đúng ảnh v2 và một BM 720p/K20/x1, tối đa 15 credit. Đây không phải duyệt tiếng/hình nguồn mới hoặc toàn phim.

## Đã xác định và chốt

- Ảnh solo v2 được duyệt; chỉ Khoai trong khung, Đào vẫn ở ngoài khung bên phải. Không thay câu chuyện hoặc quan hệ nhân vật.
- Một lượt Omni 1.1 Flash, Thành phần, dọc 9:16, native 720p, 4 giây, x1; Tác nhân tắt; giữ watermark nhà cung cấp.
- Ảnh cloud `600c779c-d30d-4178-afb7-c53355ee29a9`; hash nguồn `ea705dc746d39d40240b21ebd21899cddd09f94b8b9a61250e219dbadc5fa67e`.
- Saved custom K20 UUID `b447b35c-b35e-4140-af72-ecd277282b1a` kiểm trực tiếp ở trường catalogue. Một ảnh + một K20, không D06. Prompt readback bằng file DRAFT250 sau trim, không thêm biến thể.
- Quote đầy đủ 7 credit, số dư trước 999. Reviewer độc lập `solo_critic_250` ghi GO_ONE_SUBMIT; root đọc toàn báo cáo trước một click duy nhất.

## Giới hạn và vấn đề mở

Ảnh 941×1672 là ingredient gần 9:16, không tự gọi native 720p. Tay Đào ngoài khung UNKNOWN; các điểm nối thật chưa nghiệm thu. Giọng preset đã chốt không đồng nghĩa nguồn mới đạt đúng sắc thái/khẩu hình.

Đã submit một lần; không tự retry, không chuyển lượt BR thành lượt sửa BM. Chờ nguồn tải native, kiểm raster/full decode/từng khung cần thiết, phản biện độc lập và nghe thực. BR giữ HOLD đến khi BM đủ hình/range và cổng tiếng mới đóng.

## Tài liệu kiểm soát

- `restart_720p_v1/00_decisions/C01B-solo-BM-image-and-run-approval-251.json`
- `restart_720p_v1/04_requests/C01B_BM_T02_solo_request_251.json`
- `restart_720p_v1/06_qc/C01B_BM_T02_solo_preflight_independent_251.md`
- Evidence: `C:/Users/PC/Downloads/du_an_nem_bui/251_BM_SOLO/`.

## Kết quả nguồn và thực chi

Một output `cae2fca6-bd20-4251-92e9-385c4a638f49`, tải native720p qua UI thành công. File `05_native/EP01_720_C01B_BM_T02_SOLO_NATIVE.mp4`, hash `780ab0b3fb29454f732d2f56ed30526a77f81ed98bbaf04ca04cdb5cf094b231`, bản tải/workspace/archive giống nhau. Video720×1280, 24fps, 96 khung/4s; audio4,01s; giải mã đủ sạch. Không resize, upscale hoặc sửa nguồn.

Root kiểm 24 mẫu6fps và 8 khung nguyên cỡ. Cảnh solo/tay nghỉ giữ được ở mẫu, nhưng “Khoan” tự sinh F23–F57, từ0,958333 đến trước2,416667s, chồng đoạn miệng mở. **NOT_SELECTED / BR_HOLD**: chưa chứng minh range sạch đủ từ/khẩu hình; không lấy đuôi môi khép để overlay tiếng. Actual listening NOT_PERFORMED, không xin owner duyệt một nguồn hình đã có blocker rõ.

Cùng account999→992, thực chi7. Đợt coverage đã dùng14/30 (hai output BM), không tự dùng slot BR cho retry. Tổng dự án88/500, còn412: lượt đầu133, tạo lại124, sau rough45, dự phòng110 vẫn chưa mở.

Tầng lỗi xác định: generation/native trước cắt ghép. Cơ chế cụ thể của model UNKNOWN; không khẳng định một câu prompt là nguyên nhân duy nhất. Xem bài học `09_lessons/REC251_solo_geometry_does_not_fix_generated_text.md`.

Bước tiếp theo cần owner chốt đúng một thay đổi: cho phép chữ nhấn “Khoan” trong cảnh này rồi kiểm tiếp tiếng/cut, hoặc giữ nguồn bắt buộc sạch và chuẩn bị hướng sửa mới có evidence/quote trước paid generation. Chưa thực hiện phương án nào, BR/C03A/finishing vẫn chưa mở.
