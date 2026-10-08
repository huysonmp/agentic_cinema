# REC255 — Review độc lập bản “Khoan” rút gọn

Kết luận: **GO_FOR_OWNER_SHORT_AV_CHECK**. Chưa thấy blocker hình/mapping buộc loại candidate; chỉ trình owner nghe/xem đúng bản ngắn, không chọn BM hoặc mở BR.
Target theo native evidence: `07_edits/C01B_KHOAN_SHORT_0p75S_T01_FOR_REVIEW.mp4`, SHA256 `c6bbc9de803badf608f576f5dc47f126581db317434dcd92c00abd06698887bc`. Hash này lấy từ evidence, reviewer không rehash MP4 ngoài allowlist đọc của lượt.
Đã đọc đầy đủ governance217, registry254, `scripts/check_ep01_khoan_trim_255.py`, trim_check/native_evidence255; xem cả ba board comparison chứa đủ18 output frame và PNG output F0/F17. Không chạy script/render, sửa media, nghe AV, UI/network/API/Git/cài tool hoặc dùng credit.

- Nguồn là bản local254 hash `cd4213d393798ca3baf45603a9c40215b7f08ffcf7091418238e183abb76b198` theo registry; vẫn owner AV pending, không chuyển thành nguồn đã nghiệm thu chỉ vì rút gọn.
- **Offset nguồn20 frame, không phải0**: output F0–F17 map source F20–F37, range half-open `[20,38)` ở24fps = `[0,833333;1,583333)` giây nguồn. Video và audio cùng dịch−20/24s; output0,75s/18frame.
- Native evidence ghi720×1280/24fps, video và audio0,75s, giải mã đủ18frame; timestamps output0 đến0,708333s. Không có frame bỏ/lặp hoặc retiming trong bảng map1:1.
- Cả18 frame nhìn thấy sạch chữ, toàn mặt/miệng Khoai rõ, cỡ cảnh solo giữ. Tay nghỉ, bát/đũa/chén/mép món và camera không thấy đổi rõ so từng source frame tương ứng; không thấy crop/che mặt/freeze mới.
- Điểm vào outputF0/sourceF20 miệng khép nhẹ; F1/sourceF21 bắt đầu mở, F2–F13 thấy chuỗi mở/đổi hình, F14–F17 trở về khép. Điểm ra F17/sourceF37 khép. Đây là quan sát hình, không chứng minh onset/end âm hoặc đã giữ trọn “Khoan”.
- Vùng áo phục hồi còn hơi mềm/chuyển sắc nhẹ như254, chưa thấy seam/nút lỗi lớn trong18 frame; kiểm shimmer/jitter khi phát liên tục vẫn cần owner.
- Script kiểm slice PCM nguồn254 stereo48kHz16bit từ sample40000 tới75999, đúng `[20/24,38/24)` và36000sample/channel. trim_check ghi companion bằng tuyệt đối slice đó, SHA256 payload PCM `6fc5ecf3a51a61cdfb85d86e9d71b7259f96358722acf9b99ccf3827f4b3ae26`; không phải hash cả WAV/container.
- Audio AAC của MP4 ngắn đã mã hóa lại: PCM **không bit-exact** với slice, zero-lag correlation0,9992246982 theo check. Không gọi copy stream nguyên vẹn; correspondence/timing kỹ thuật không chứng minh không cắt phụ âm/đuôi, đúng K20/sắc thái hoặc sync nghe–nhìn.

Human checkpoint theo217: owner phát đúng candidate/hash này, nghe đủ một “Khoan” không hụt đầu/cuối và xem mouth sync/nhịp vào–ra cùng vùng áo. Reviewer chưa actual listening/continuous AV; word completeness, K20, sync và chất lượng nhịp vẫn UNKNOWN/HOLD nghiệm thu tới checkpoint đó.
Không chốt EDL/selected BM range từ technical map; không kiểm A→BM→BR→C02. Contact Đào ngoài khung UNKNOWN, BR vẫn HOLD/chưa được chi; paid generation/retry/reserve không mở từ task trim.
Root đọc full report trước trình bản ngắn. Nếu owner nghe hụt âm hoặc thấy điểm cắt/áo lỗi, ghi finding theo target này và giữ HOLD; không kế thừa approval source hoặc gọi full-film PASS.
