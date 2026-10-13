# REC299 — Duyệt native không duyệt range/cut; board phải kiểm nhãn coverage

Owner duyệt exact C06 native298 về tiếng/K20, đủ câu và nét diễn; chấp nhận ngoại lệ gaze đầu cho chuẩn nối. Không suy thành lipsync approval khi câu hỏi không nêu, không mở rộng thành waiver món/identity hoặc video cuối.

1. Giữ F0 của range mới để bảo toàn đầu lời. Đề nghị48F/2s dựa ASR kết1,60s, mouth shape tới41 rồi khép42–47; vẫn owner nghe/xem bản encode để chốt âm cuối/sync/nhịp. Không cắt ngay theo timestamp ASR hoặc khi mắt hướng ĐàoF18.
2. Trial EDL tách khỏi EDL chính. C05 range đã duyệt66F giữ; C0648F còn đề nghị. Không chèn replacement into final bởi native tiếng được duyệt.
3. Cắt/concat source audio cần trim sample theo cùng duration hình; mã hóa AAC lại không bit-identical. Không revoice/mute/pitch/speed/gain/crossfade tự ý; owner audio source không thay encode checkpoint.
4. FFmpeg select→tile có thể tạo **page ảnh lặp do output đồng bộ default**, dù số file đúng. Lần v1 ở đây lặp F50–65 và F66–81; nhãn frame làm lộ lỗi. Sửa `-fps_mode passthrough`, tạo v2 không overwrite, đọc labels thực đủ F50–81/F66–113. Đếm file hoặc command exit0 không chứng minh coverage đủ.
5. Ngoại lệ ánh nhìn đã được chấp nhận không đồng nghĩa liên tục hoàn chỉnh: món cũ và A đặc ở C05 chuyển sang món rời ở C06 vẫn có jump. Ghi finding đó trong trial, không dùng cận món/che người nói hoặc gọi điểm nối đạt để tránh xử lý nguồn cũ.
6. Range giảm 2 giây từ native 4 giây vẫn không bảo đảm final 30: 680 khung/28,333 giây, còn 40 khung/1,667 giây cho N07/nhận/cho/C09. Không ép cắt lời/C09 hoặc coi bản thô 35 giây thành mục tiêu cuối.

Chi mới 0; 251/500, còn 249, phần tạo lại 12, dự phòng đóng. Approval native lịch sử giữ đúng scope, không trả phí lại hoặc thay EDL chính trong REC299.
