# REC282 — Kiểm ảnh nhận–bỏ: START v1 và END v2 chờ owner

Ngày 13-10-2026. **STILL_CANDIDATES_FOR_OWNER_REVIEW / NOT_VIDEO / NOT_PRODUCTION_GO.** Root kiểm ảnh, không review độc lập; không nghiệm thu movement, D06, khẩu hình, điểm nối hoặc toàn phim.

## Đã tạo và lưu bằng công cụ có sẵn

Theo “ok nhé” sau REC281, tiếp tục chuẩn đầu vào. Dùng skill imagegen, công cụ ảnh tích hợp ChatGPT, không API/CLI/key, browser hoặc Flow submit. Ba lượt ảnh: START sửa món → END v1 → END v2 sửa riêng lượng món trong bát. Không sửa ảnh bằng Python hoặc ghi đè nguồn; giữ ảnh gốc và các bản khác tên.

| Ảnh | SHA-256 / kích thước | Disposition |
| --- | --- | --- |
| START v1 `02_refs/RECEIVE_START_food_v1_CHATGPT_FOR_REVIEW_282.png` | `491575988bbbea26e16fda3a7f02401b874f9abcc24eda7cdef340764ab232d8`, 941×1672, 1.899.987 byte | Ứng viên sửa món/entry, chưa owner duyệt. |
| END v1 `02_refs/RECEIVE_END_v1_PORTION_REWORK_282.png` | `89e90f76c4bbe49336ae80ead4bfd619e90682f82e8dd1b6bdc7bafdc629cd9c`, 1.927.308 byte | Root bác vì tự thêm lượng món trong bát lớn hơn phần gắp. Không dùng làm ảnh đích. |
| END v2 `02_refs/RECEIVE_END_v2_CHATGPT_FOR_REVIEW_282.png` | `82057aba35ffd8182f4624696d209750767452b842413013bd9d94f87b1a596d`, 941×1672, 1.878.801 byte | Ứng viên sau sửa phần nhận, chưa owner duyệt. |

Ảnh đã được copy vào repo và folder `C:/Users/PC/Downloads/du_an_nem_bui/282_RECEIVE_REFS/`, hash khớp bản sinh. Original ở `C:/Users/PC/.codex/generated_images/01a0eb0e-6ec3-7121-a6a5-ea0ccdb77744/` vẫn giữ.

## Phần root trực tiếp kiểm

Đã xem nguyên ảnh source C06 F56, hai ảnh thật Nem Bùi, START mới, END v1 và END v2. Không lấy tên prompt làm bằng chứng output. START mới có lớp thính và cấu trúc rời, phân biệt thịt/bì hơn nguồn cũ; phần trên đũa không còn lát chữ nhật đặc. END v2 giảm lượng trong bát, giữ phần lớn lòng bát trống; chưa chứng minh số lượng/hình từng sợi được bảo toàn chính xác từ START.

Hai nhân vật vẫn là Khoai/Đào thực phẩm, môi khép ở đầu/cuối. Cả hai bát còn; START rỗng, END bát Đào có phần nhỏ và bát Khoai rỗng. Đào đỡ bát riêng ở nửa phải bằng tay trong; cốc vẫn nâng ở tay ngoài. END tips đũa trống, có khoảng hở với bát; không đút ăn hoặc xuất hiện miếng khác ở miệng. Rau/chấm/đĩa giữ trong bối cảnh; không thấy khói.

## Caveat không được bỏ qua

- Đây là redraw có điều kiện, **không pixel-exact C06 F56**. Chi tiết mắt/mặt, chất liệu/ánh sáng, tỷ lệ và hình món có thay đổi nhỏ; chưa có đo geometry hoặc seam AV. Không gọi identity/camera invariant đã khóa tuyệt đối.
- START/END v2 là 941×1672, gần 9:16 chứ không đúng tuyệt đối tỷ lệ 720×1280; chưa crop/resize ảnh. Native video tương lai vẫn phải kiểm 720p dọc thực, không suy từ ảnh.
- Grain/coating món mới cần owner đối chiếu trực tiếp ảnh thật; một ảnh trông ngon không là chứng nhận đúng Nem Bùi. Không đổi toàn món thành sợi mì hoặc gọi bản này recipe chuẩn.
- END v2 đã bớt món thừa, nhưng lượng/dạng trong bát chưa có chứng minh vật lý liên tục; native sau này phải kiểm không sinh thêm A. Đào hơi nâng bát ở ảnh đích theo “đưa bát”; không kế thừa quy tắc cũ buộc đáy bát nằm trên bàn trong suốt shot.
- Dấu sao Flow trong frame nguồn không được giữ trong các PNG redraw mới. Các PNG được ghi là **ảnh ChatGPT sinh**, không frame native Flow hoặc native đã chỉnh. Source C06/T03 và watermark video gốc không bị sửa/xóa. Native tương lai phải giữ watermark nền tảng; không dùng ảnh này để nhận đã xóa hoặc được phép xóa watermark nguồn.
- Không có lời/tiếng trong ảnh. START/END kín môi không giải quyết phần nói N07; cần thiết kế/kiểm articulation trên native thật, không ghép tiếng lên miệng kín rồi gọi đạt.
- Chưa upload Flow hoặc chọn Frames/Ingredients; chưa chốt một take, giá, timing hay phương án sửa những cảnh cũ. Review độc lập ảnh mới chưa chạy; lần actual REC280 trước thất bại vì giới hạn sử dụng không được ghi thành PASS.

Kết luận root: có thể **trình hai ảnh ứng viên về ngoại hình món và tư thế nhận–bỏ**; không trình END v1. Owner approval nếu có chỉ đúng ảnh/hash/phạm vi, không là quyền sinh video, đổi master/canon, cho phép lệch toàn phim hoặc mở ngân sách.
