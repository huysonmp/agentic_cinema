# REC293 — Chạy đúng một C06 ACT B, tải native và dừng vì sai đích hành động

13-10-2026. Owner duyệt một lượt **cap7/x1/no retry** theo đề nghị REC292. Đã ghi authority trước submit, dùng skill computer-use trên trình duyệt tích hợp, kiểm lại prompt/chips/config/Agent/tiếng/tài khoản rồi gửi đúng **một** lần.

## File và ngân sách có bằng chứng

Output Flow: `https://flow.google.com/project/bcb1f53c-13b6-4719-b866-01348dfcddd6/edit/8a14641f-0dea-4f93-a0a1-95e06b3f4399`.

Đã chọn **720p — Kích thước gốc**, đặt listener tải trước click, nhận tệp thật và copy riêng vào folder owner/repo. Native: `C:/Users/PC/Downloads/du_an_nem_bui/293_C06_ACT_B_T01/C06_ACT_B_T01_NATIVE_720p_293.mp4`, SHA `6fc5f1dab04e19e51a169eea5f763f36677eae0a5842f297e6a2b29c36f0b71c`. **720×1280, 24fps, 96 khung/4 giây**, có AAC stereo48kHz; giải mã toàn bộ thành công. Không dùng preview hoặc nguồn cũ làm output.

UI quote7, balance trước993/sau986 ⇒ **debit7**. Sổ dự án **244/500**, còn **256**, phần tạo lại **19**, dự phòng110 đóng. Không đồng nhất số dư986 của tài khoản với ngân sách256 của dự án.

Folder owner có `BALANCE_BEFORE.png`, `SUBMITTED.png`, `OUTPUT_NATIVE_DOWNLOAD.png`, `BALANCE_AFTER.png`, native, `native_qc/` và `asr_qc/`. Native/root source/ảnh/preset/EDL không bị sửa.

## Root đã kiểm, không phải đã nghiệm thu nghe/xem liên tục

Dùng helper read-only có sẵn REC243 trong Python bundled/Pillow; xuất đủ96 PNG, tiếng WAV, metadata và boards. FFmpeg tạo thêm `full16_01.png`…`06.png`: **6 trang ×16 khung, không padding**, trái→phải/trên→dưới; trang1 F0–15, trang6 F80–95. Root xem cả6 trang và khung full-res **F0/F16/F48/F72/F95**.

- **Hình món/props giữ đúng hướng hơn:** nem rời và có thính, không thấy khói; Đào blouse trắng/không yếm, cốc vẫn nâng ngoài bát, hai bát riêng còn. Hậu cảnh/camera không có cú đổi lớn kiểu REC286 trên range đã xem. Không gọi đây là toàn pixel giữ hoặc FOOD whole-film PASS.
- **Sai đích chuyển A:** từ đoạn đuôi, Khoai hạ đũa về ụ nem/đĩa chung. Full F72 (3,0s) cho thấy A trên vùng đĩa giữa, không bát Đào; **F95 (3,958s) tips không còn phần A đọc rõ và nằm trên ụ nem**. Cả take không đáp ứng “chuyển A về bát Đào, chưa thả”. **Root NOT_SELECTED cho full native**; không tự lấy đoạn đầu/cắt/mute/overdub làm bản đã đạt.
- **Entry/diễn phụ:** F0 Khoai nhìn phía trước hơn là chú ý Đào như ảnh đầu; trong lượt miệng hoạt động tay trong nâng lên (F16 thấy rõ), trái chỉ dẫn tay nghỉ. Chưa đo pixel/velocity hoặc nghe nên không suy một hình miệng thành cười sai, sai phoneme hoặc giọng đổi. Nét diễn B cần playback thực cùng tiếng và owner, không chấm từ grin/teeth một khung.

ASR offline trên tiếng native ghi **“Anh gấp cho em mà.”**. Đây là nhận dạng máy, không bằng chứng đã nghe “gấp” thay “gắp”, đúng K20/nam Bắc hoặc sync. Chưa actual listening/continuous AV PASS bởi root. Người dùng có thể xem/nghe đúng file native để phản hồi tiếng/diễn riêng; phản hồi tiếng không xóa lỗi hành động full take.

Phản biện độc lập actual đã hoàn tất, root đọc đầy đủ [báo cáo](restart_720p_v1/06_qc/C06_ACT_B_actual_independent_293.md). Reviewer xem đủ96 khung qua boards và12 fullres, xác nhận đích sai, entry gaze reset và tay trong nâng; không continuous AV/nghe. F80–92 có contact/occlusion giữa A và ụ nem, **không chốt exact frame thả**, nhưng F95 tips trống/không còn A riêng; bát Đào vẫn rỗng. Root và reviewer thống nhất fulltake NOT_SELECTED, không tự chọn prefix hoặc retry.

## Truy nguyên và bước tiếp

Prompt có nêu đúng một A, đích bát Đào, chưa thả, không dừng–giữ, tay trong nghỉ; input ảnh đúng phase, nhưng route Ingredients không được chứng minh khóa F0 hoặc điều khiển trajectory. Output vẫn reset ánh nhìn và đi về đĩa chung. **Đây là không tuân thủ phạm vi output có bằng chứng, chưa đủ cô lập nguyên nhân thành một keyword/model.** Sửa vật liệu bằng local composite đã giải quyết drift ảnh ngoài mask, không giải quyết ràng buộc chuyển động khi sinh video.

Giữ fullnative/job/input/hash, không retry. Cần kiểm phạm vi đoạn hợp lệ trước khi đề xuất tái sử dụng, nhưng chưa tự chọn range khi tiếng/nhịp/entry chưa chốt; không kéo video bằng cận món hoặc dùng Quality để sửa sai ý nghĩa. Request7 đã tiêu thụ, lượt mới cần quyền riêng; dự phòng không mở.

**Đã xác định:** thực chạy/tải/giải mã đúng720p, chi7; phản biện actual hoàn tất, fulltake sai đích và không giữ A tới cuối. **Giả định còn kiểm:** đoạn trước lỗi có thể cung cấp thoại/diễn/redirect hợp lệ; chưa chứng minh hoặc chọn. **Còn mở:** owner tiếng–diễn, entry/pointcut/nhịp nhận, food C05/các cảnh trước và timing toàn tập. **Bước tiếp:** gửi native để owner thấy lỗi và có thể kiểm tiếng/diễn riêng; không xin miễn lỗi hành động, tự chạy lại hoặc thay EDL.
