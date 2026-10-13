# REC299 — Tiếng/diễn C06 duyệt; range ngắn và bản nối thử đã dựng

13-10-2026. Owner xác nhận trên exact native REC298: **“Tiếng/K20 và nét diễn chấp nhận được”**, **“Chấp nhận ánh nhìn đầu, chuẩn bản nối thử”**. [Approval](restart_720p_v1/00_decisions/C06-KEEP-A-native-voice-acting-and-entry-exception-299.json) chỉ chốt tiếng/diễn native và ngoại lệ gaze cho bước nối; không tự duyệt range encode/điểm nối/toàn phim hoặc chi thêm.

## Bản cần xem

**C05→C06, 4,75 giây**, hai câu đúng vai Đào rồi Khoai theo nguồn đã chọn:

`C:/Users/PC/Downloads/du_an_nem_bui/299_C05_C06_KEEP_A_JOIN/C05_C06_KEEP_A_4p75S_JOIN_QC_NOT_FINAL_299.mp4`

SHA256 `b4408c44d47de9b80c3e3b735a3ddc093008593d24189604b15142e3356cc469`.

Bản C06 ngắn riêng 2 giây: `C06_KEEP_A_F0_F47_2S_PROPOSAL_299.mp4`, cùng folder; SHA256 `521c5d3cfe35c20260ded48a42389c7c414377e2b51de69144d0bd395b635f51`.

## Lựa chọn dựng thử và giới hạn

- C05 giữ range đã duyệt REC269 **[0,66)**, 2,75 giây; đúng native SHA `3df61217…23df`. Không sinh lại hoặc âm thầm thay C05 bằng bản sửa món bị bác.
- C06 đề nghị **[0,48)**, 2 giây, giữ F0 để không mất đầu câu. ASR native khoảng0,46–1,60 giây; mouth activity quan sát tới khoảng F41, F42/43–47 đã khép. Kết 2 giây để có đệm sau lời/diễn, không dừng ngay khi ASR báo hết. Đây là căn cứ chọn nháp, **không heard âm cuối/sync PASS**.
- Cắt bỏ đuôi native F48–95 khỏi **bản thử**, không xóa native4s hoặc chọn range production tự động. C06 tiếp theo nhịp Đào đưa bát, không cần đuôi pose bất động2s.
- Cut thử tại **F66/2,75 giây**, tổng **114F/24fps=4,75 giây**. Giữ native audio Đào rồi Khoai, trim theo sample48k:132.000 +96.000; concat và AAC encode mới. Không mute, revoice, speed/pitch/gain/crossfade hoặc thêm âm thanh tổng hợp. Encode mới không bit-identical audio nguồn.
- Lip-sync không nằm trong câu hỏi native owner vừa chốt; không tự mở rộng approval thành sync trên bản encode mới. [Trial EDL](restart_720p_v1/07_edits/C05_C06_KEEP_A_join_trial_edl_299.json) không thay EDL chính hoặc nguồn được duyệt trước.

## Kiểm thực đã làm

Hash cả hai native đối soát trước dựng. Prefix48F/2s và join114F/4,75s,720×1280/24fps/AAC48kstereo; join giải mã toàn file thành công, tách114khung và audio. Source native giữ nguyên.

Root xem dense cut F50–81 và đủ encoded C06 F66–113, critical full frames F65/F66/F113; không actual nghe/continuous AV. Hai mặt và tay–A/bát/cốc còn thấy; A còn trên tips tới F113. Ánh nhìn đầu đã có ngoại lệ owner, không gọi đã sửa gaze.

**Finding toàn cảnh không được che:** tại cut, món C05 còn tạo hình cũ với các dải dày/đều hơn, C06 có món rời/thính theo input mới; phần A/diện mạo/môi Đào cũng có sai khác. Ngoại lệ gaze **không** là waiver món/identity hoặc proof seam vô hình. Bản thử giúp chốt range, đối thoại/nhịp và sync; lỗi hình món vẫn mở, chưa xin duyệt toàn chất lượng hình hoặc bàn giao.

Board extraction v1 của vòng này bị lặp page do FFmpeg đồng bộ output sau select/tile. Root phát hiện nhãn F50–65 và F66–81 lặp, tạo **v2 với `-fps_mode passthrough`**; chỉ v2 đủ labels đúng liên tiếp dùng làm bằng chứng. Không đếm số board thành đủ coverage, không sửa native/video để chữa lỗi công cụ QC. Cảnh báo fontconfig còn nhưng lệnh thành công/nhãn hiển thị; không nhầm với media decode lỗi.

Offline ASR trên **join encode** đọc hai lượt “Chờ em quay lưng nữa à?” (0–1,9s) và “Anh gấp cho em mà.” (3,18–4,30s). Transcript máy không kiểm K20/D06, accent hoặc sync; riêng “gấp” không bác chữ “gắp” owner đã nghe duyệt native. Audio/miệng/âm cuối nhịp cắt mới vẫn cần owner actual trên file/hash này.

## Timing và bước tiếp

Nếu range48 được chọn, qua C06 toàn tập là **680F/28,333333s**, chỉ còn **40F/1,666667s** tới30 cho N07/nhận/cho/C09; **không đủ bằng chứng vừa30**, không gọi tiết kiệm2s là đã giải quyết ending. Cần rà range phía trước trong gói toàn tập trước thay EDL, không cắt lời/C09, tăng tốc giọng hoặc tự nới mục tiêu.

[Phản biện độc lập](restart_720p_v1/06_qc/C05_C06_KEEP_A_encoded_trial_independent_299.md) đã kiểm V2 dense boards và ba full-resolution frames; root đọc toàn report. Không thấy lỗi hành động mới trong range C06 cấm checkpoint riêng, nhưng **food/held-A continuity là blocker thật để chốt hình production**. Không giấy hoặc tiếng/diễn approved tự đóng hình. Bước owner tiếp chỉ duyệt **range C06 ngắn và đối thoại/nhịp/sync C05→C06**; hình món/identity drift và full-film vẫn mở. Sau chốt range, mới chuẩn nhịp nhận từ exit thực F47 và khoảng hở, không lấy P1/P2 redraw làm điểm nối production.

**Đã xác định:** native tiếng/diễn và ngoại lệ gaze được owner chấp nhận. **Quyết định mới:** chuẩn bản nối thử; range/encode còn pending. **Giả định:** range2s đủ đệm, cần actual nghe/AV. **Còn mở:** cut/range/sync, hình món ở seam, thời lượng ending. **Bước tiếp:** review bản thử và chốt đúng phạm vi, rồi chuẩn nhận từ nguồn thật.

Chi mới **0**; sổ **251/500**, còn **249**, phần tạo lại **12**, dự phòng **110 đóng**. Không browser Flow action, paid, preset mới, production EDL replacement hoặc release.
