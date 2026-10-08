# REC257 — Kiểm path thật và chứng minh output không tiếng

## Quan sát đã chứng minh

Một Frames START/END đúng source, prompt đọc lại khớp, quote7, đã sinh native96khung/4s. START tay trong cong gần bát; outputF3..8 tay trong tiến tới mép trái/sau đĩa, giữ cùng tay ngoài ở vành phải trước buông/thu. SauF44 release/retract dùng được về mặt dense frames. Không phải chọn nhầmref, đảoSTART/END, sai file hoặc lỗi cắt tạo ra renewed reach: lỗi có ở native trước dựng.

Giả thuyết: model hoàn thiện tư thế hai tay giữ đĩa từ bố cục/động tác, hoặc endpoint constraints không giữ được đường đi tay. Chưa phép thử phân biệt nguyên nhân model/wording/tương tác ảnh; không tuyên bố đã chứng minh gốc là một từ nào hoặc tăngQuality sẽ sửa. Prompt đã cấm renewed reach/two-handed plategrip nhưng chưa bảo đảm enforcement.

## Cổng cần giữ

1. Đối soát nguồn/reference UUID/hash/slot trước submit; paperPASS chỉ cho request, không cho motion.
2. Xuất đủframes, xem tay/mặt/đĩa theo frame/time; nativeF0 đúng không miễn kiểmF3..8. Reviewer độc lập đọc actual, root đọc fullreport.
3. Trim `[28,78)` bỏ pha tay tiến ra nhưng vẫn giữ tư thế hai tay sát đĩa. Không ghi resolved hoặc compliant vì crop/trim che thời điểm lỗi phát sinh. Ngoại lệ nghệ thuật thuộc owner, có target/range/hash và điều kiện không kéo/lấy món.
4. Candidate phải kiểm cả điểm nối thật: BM ngoài khung Đào là UNKNOWN, không là chứng cứ cô đã giữ đúngpose. BR nghỉ xong trướcC02, người nói/mặt/tiếng phải ở đúng nguồn.

## Tùy chọn âm thanh và lời prompt

Switch “Trả về video không có âm thanh” nằm trong Cài đặt lưới ô; đã ON, nhưng native tải gốc vẫn có AAC và PCMnonzero. Chưa đủ dữ liệu xác định switch điều khiển generation, playback hay phạm vi khác; không kết luận là bug hoặc âm thanh nghe thấy gì khi chưa nghe. Prompt còn “Quiet street ambience only”, mâu thuẫn với đích silent nếu hiểu đích là không bất kỳ sound nào. Đây là điểm phải chuẩn hóa đầu vào, không lấy setting làm hợp đồng output.

Với silent BR đã được giao, dùng derivative -map0:v -c:v copy -an, giữ original và xác minh tất cảdecodedframes bằng tuyệt đối +audio_stream_count0; không cần voice mới hoặc trả phí để bỏ tiếng. Ghép silence đúng50frame/100000audioframe ở48k, kiểm alignment/zero interior; AACedge leakage và độ hụt ambience qua cut còn humanAV, không gọi waveform/sourcecorrelation là heard/sync PASS.

Nếu có request silent sau này: bỏ các câu cho phép ambience/nhạc/voice; kiểm semantics UI hiện hành hoặc ghi UNKNOWN; vẫn probeoutput. Tự phục hồi setting cũ sau request, log rõ để không ảnh hưởng cảnh thoại sau. Những điều này không tự cấp quyền sinh lại.

## Dừng và học từ kết quả

Thực chi7, outputcount1, no retry. Không reset giới hạn lặp lỗi từ việc đổi tên shot hoặc cắt range. Nhận “tiếp tục” không phải owner đã nới no-inner-reach. Hỏi một lựa chọn về exactcandidate có caveat, không tự dùng số dư965 hoặc phần trần49 chưa chi làm quyền test tiếp.
