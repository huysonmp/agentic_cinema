# EP01 — Cảnh còn thiếu và kiểm đầu vào

Ngày 2026-10-06. Owner yêu cầu “tiếp tục đi nào” sau bản xem 207. Quyền tiếp tục áp dụng trong ngân sách còn 43 credit; không suy thành nghiệm thu vị trí bát ở cut 207, cấp ngân sách mới hoặc chuyển sang Quality.

## Điều giữ nguyên

- Kịch bản C-v0.6 và toàn bộ tiếng trong bản 202 đã duyệt; không tạo lại giọng.
- Timeline 207-v0.4 vẫn là kế hoạch hiện hành, chưa phải bản dựng đạt kiểm tổng thể.
- Đầu lượt này còn U01, U02, U03, U08. Mỗi đơn vị một lượt Lite dự trù 10 credit, không thử thêm nhiều mẫu.

## Thực thi và ngân sách

Đã chạy **một lượt U03**, với cặp ảnh 195 đã được owner duyệt tại 196 theo chiều đảo: END 195 nhìn Khoai làm START, START 195 nhìn cốc làm END. Đây là tạo chuyển động mới, không đảo một video cũ.

Đã kiểm prompt khớp tệp, Video/Khung hình, 9:16, Veo 3.1 Lite, 720p, 8 giây, x1, Tác nhân tắt; quote 10 credit. Số dư tài khoản quan sát trực tiếp giảm từ 97 xuống 87. Tổng sử dụng trong sổ hiện hành tăng từ 379 lên **389/422**, còn **33 credit được phép dùng**. Không coi 87 credit trong tài khoản là ngân sách được cấp.

U03 tải được bằng lựa chọn 720p kích thước gốc. Sự kiện download chờ 20 giây không trả về, nhưng tệp mới có thực trong Downloads; đã nhận, hash, probe và giải mã. Không bấm tải lại hoặc tạo lại vì sự kiện chờ hết hạn.

## Kết quả U03: REWORK

Tệp gốc: `C:/Users/PC/Downloads/du_an_nem_bui/208_remaining_coverage/U03_NATIVE.mp4`.

- H.264, 720×1280, 24 fps, 192 frame, 8 giây; không có audio stream; giải mã exit 0.
- Ban đầu nhìn Khoai, sau đó chớp mắt và quay xuống về phía cốc; cốc không được nhấc lên. Tuy nhiên môi hé mở trong đoạn đầu cần dùng, rõ ở native frame 29; sau đó tiếp tục chuyển động môi.
- **Không đạt môi khép trong đoạn 33 frame/1,375 giây**; không bind vào timeline hoặc ghi PASS chỉ vì ảnh END đúng.
- Root kiểm qua `evidence/208/U03_first48.png`, `U03_full_grid.png`, `U03_frame29.png`. Không có agent phản biện độc lập hoặc kiểm full AV trong lượt này.

## Khung tham chiếu mới: chờ owner duyệt

Ảnh qua built-in imagegen, giữ từng phiên bản, không ghi đè ảnh cũ. Nguồn thiết kế: OPEN v0.7. Nguồn trạng thái/texture: native P02 frame 0 và U07 frame 77. Hai ảnh nem Bùi owner duyệt cũng đã mở lại để đối chiếu. Tạo ảnh này không tiêu credit Google Flow; không tuyên bố không dùng hạn mức dịch vụ khác.

Các đường dẫn ảnh dưới đây tính từ thư mục **series**, không phải thư mục episode.

| Khung | Bản chờ duyệt | Kiểm và giới hạn |
|---|---|---|
| U01 — bàn trước khi gắp | `assets/references/208/U01_START_v0.2_REVIEW.png` | Bốn tay nghỉ, hai bát rỗng, đủ rau/chấm/cốc/đũa, không còn miệng trong hình. v0.1 bị loại vì lọt miệng Đào. Chưa có chuyển động kéo đĩa/chạm cốc. |
| U02 — cận món hiện tại | `assets/references/208/U02_START_v0.1_REVIEW.png` | Rau và hai đồ chấm ở rìa, không mặt/tay/khói. Texture là diễn giải AI theo ảnh nguồn, không được gọi là trùng ảnh thật hoặc đã nghiệm thu món. |
| U08 — sau nhận nem | `assets/references/208/U08_START_v0.3_REVIEW.png` | Một phần nem trong bát Đào, bát Khoai rỗng, Khoai cầm đũa rỗng. v0.2 bỏ đôi đũa thừa bên Khoai; v0.3 sửa riêng texture. Góc rộng tái dựng từ U07, không phải khớp pixel hoặc bảo đảm cut mượt. |

Skill imagegen dẫn đến sửa từng điểm riêng: đũa thừa, texture, bố cục. Skill computer-use dùng kiểm Flow, chạy đúng một lượt và nhận bản gốc; không cài API hoặc yêu cầu key.

## Bài học ghi nhận

1. Ảnh đầu/cuối có môi khép và prompt rõ không bảo đảm video luôn khép môi. U03 sai lệch so với ràng buộc đã read-back; chưa có bằng chứng do gắn nhầm ảnh hoặc đổi prompt. “Biểu cảm cười khiến model tự thêm khẩu hình” chỉ là giả thuyết, chưa kiểm chứng.
2. Kiểm ảnh rộng theo trạng thái sau hành động: không dùng hai bát rỗng cho cảnh đã trao nem. Đưa đôi đũa từ bàn lên tay phải bỏ đôi tương ứng trên bàn.
3. Chỉnh ảnh có thể làm thay đổi texture ngoài vùng yêu cầu; phải mở lại kết quả. Không suy liên tục chỉ từ prompt hoặc tên tệp.
4. Download-event timeout không đồng nghĩa không tải được. Kiểm tệp mới đúng tên/thời gian, hash và decode trước khi thử lại.

## Quyết định còn mở — đã hỏi owner

- Đề xuất không dùng U03 lỗi. Đổi 1,375 giây S03 thành insert tay Đào chạm cốc, lấy từ phần tiếp của U01 sẽ tạo, giữ 30 giây. U01 khi đó cần đủ 7,4583 giây sạch; phải kiểm động tác kéo đĩa rồi chuyển tay sang cốc thực tế, không coi dự kiến là đã đạt. **Đổi cách quay này chưa được duyệt.**
- Giữ cảnh mặt cần quyết định riêng lượt sửa/ngân sách. Không lấy 3 credit dự phòng để chi lượt 10 credit.
- Ba khung U01/U02/U08 chờ duyệt ảnh đầu vào; chưa gửi sang Flow để tạo video.

## Bước tiếp theo

Owner chốt U03 và ba ảnh → cập nhật shot/prompt/timeline đúng quyết định → chạy các cảnh trong ngân sách → kiểm native và range → ráp cùng tiếng đã duyệt thành bản 30 giây khi đủ nguồn. Chưa full AV, master hoặc phát hành.
