# P6 — F-NB-03: approval và lượt thử ảnh món

Ngày: 2026-10-01. Trạng thái: APPROVED_REQUEST / SUBMITTED_ONCE / MODERATION_FAILED / NO_OUTPUT.

## Quyết định owner

Owner: “duyệt, làm tiếp đi”. Duyệt đúng request F-NB-03 trong tài liệu 65: một ảnh food-only, text-only, không upload ảnh nguồn, Nano Banana Pro, 9:16, x1. Không tự duyệt asset, ghép nhân vật, video hoặc tiếng. F-NB-02 vẫn UNRECONCILED.

## Preflight trực tiếp

Flow project EP01_P6_Khoai_Dao_Pilot, project ID 9276788e-9781-44fb-ba5b-083006667374. Đã chọn Nano Banana Pro thay mặc định Nano Banana 2. UI xác nhận Hình ảnh, 9:16, x1; giá hiển thị 0 tín dụng. Đây là giá UI cho lượt này, không phải xác nhận billing hoặc miễn phí vô hạn.

Prompt giữ nguyên block trong [request65](65_p6-food-evidence-set-spec-and-f03-request-v01.md). Chỉ submit một lần. Nếu lỗi hoặc không đối soát được kết quả, dừng, không tự tạo lại.

## Kết quả

Đã nhấn Bắt đầu tạo đúng một lần. UI xuất hiện tiến trình 0% cùng nguyên văn prompt; composer được xóa sau submit. Sau đó UI trả về “Không thành công” và:

> Lượt tạo này có thể vi phạm các chính sách của chúng tôi. Vui lòng thử một câu lệnh khác hoặc gửi ý kiến phản hồi. Bạn chưa bị tính phí cho lượt tạo này.

Không có ảnh đầu ra, không có food asset/hash/QC ảnh. Không bấm Thử lại, không sửa prompt hoặc submit lần hai. Thông báo chưa tính phí là bằng chứng UI, chưa kiểm billing ledger. Không biết lý do cụ thể bị từ chối; không suy đoán tên món, nguyên liệu hoặc từ khóa là nguyên nhân.

Bằng chứng local: `media/raw/ep01_p6_food/F-NB-03_flow-failure-proof.png`. SHA256: `EB6C54F44052DD6C04DE14CE333CE122F4E635A0D72F65B662108D820E456E11`. Đã xem screenshot thực tế. Binary nằm trong media gitignored; Git chỉ lưu hồ sơ và hash, không lưu ảnh này lên remote.

## Đề xuất tiếp theo — chưa chạy

Ưu tiên owner cung cấp ảnh nem Bùi tự chụp hoặc có quyền sử dụng rõ ràng, rồi kiểm provenance/texture và chuẩn bị một request dùng ảnh tham chiếu nếu phù hợp chính sách nền tảng. Không lấy ảnh tư liệu nghiên cứu có quyền UNKNOWN để upload. Không tìm cách vượt bộ lọc; có thể gửi phản hồi cho Flow về lượt từ chối, nhưng chưa gửi thay owner trong lượt này.

Trong lúc chờ đầu vào món, có thể chuẩn bị hồ sơ bối cảnh/bàn và mẫu tiếng theo 64–65; không coi approval F03 là lệnh tạo những đầu ra đó. Chưa ghép món vào nhân vật, chưa chạy voice/video, chưa đóng P6.

## Tổng hợp vòng

- Đã xác định: F03 có terminal rõ ràng, khác F02 vẫn UNRECONCILED.
- Quyết định đã chốt: exact request F03 được duyệt và thực hiện một lần; dừng khi bị từ chối.
- Giả định đang dùng: đĩa trắng ngà và tabletop là styling, không phải fact địa phương; chưa có asset món được duyệt.
- Còn mở: đầu vào hình món có quyền sử dụng; hình phần nem khi gắp; style frame; giọng và chuyển động.
- Bước tiếp theo: owner chọn cung cấp ảnh món có quyền sử dụng hoặc xử lý phản hồi với Flow; kiểm đầu vào trước request mới, không chạy lại F03.
