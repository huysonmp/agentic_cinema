# REC307 — Đã sửa khẩu hình local và kiểm gói nối C06→C07

Ngày 14/10/2026. Owner giao: “làm đi, sao cứ nhỏ nhỏ rồi hỏi tôi suốt vậy, agent check đâu rồi”. Thực hiện phương án A tại REC306 và gom các thao tác kỹ thuật/review nội bộ, không xin lại từng thao tác.

## Kết quả đã làm

- Tạo bản C07 local 3 giây, sửa đúng vùng miệng Khoai ở F5–14 bằng hình môi khép từ native F4/F15, có đo dịch chuyển texture và feather. Không sinh mặt/voice mới hoặc đóng băng toàn người.
- Trước encode, chỉ vùng (180,526)–(296,590) trong 10F được phép khác; 62F còn lại và mọi pixel ngoài vùng nguyên. Decode lại native kiểm đủ 96 PNG khớp nguồn. Output H.264 re-encode nên không tuyên bố pixel bit-exact trên tệp nén.
- Copy nguyên AAC từ đúng bản 3 giây owner duyệt REC306. Root kiểm lại qua một phép đo mới sau review: 142 packet có hash và pts/dts/duration giống nhau; decoded PCM cũng giống hệt, SHA `ae70a7bc1b0b1f3cb40f57065a2a0e6835c0485b585ad48dd37bed0176d45fcf`. Không cần hỏi lại tiếng D06 riêng cho standalone được giữ stream này.
- Chạy 5 unit test phạm vi/registration/feather, đều đạt. Full decode C07 local: 72F,24fps,720×1280,3 giây cả video/audio.
- Dựng bản nối thử C06_KEEP_A298 [0,48) + C07 local [0,72), tổng 120F/5 giây, cut tại 2 giây. Tiếng nối được concat và encode AAC mới, không gọi bit-exact; không revoice, đổi lời, gain, speed hoặc crossfade.

## Hai agent đã thực kiểm gì

**QA actual — `/root/bm_preflight_249`:** đọc script/quyền/manifest, tự hash nguồn và output, xem toàn72F encoded qua sáu denseboard cùng full khung critical và crop miệng. Report `C07_MOUTH_LOCAL_actual_independent_307.md`: chuỗi miệng mở MAJOR đã hết; không thấy MAJOR viền vá/miệng kép buộc sửa v2 trước trình. Pixel và packet invariance trong report là evidence root, không reviewer tự đo lại.

**EDIT/continuity — `/root/c07_edit_context_307`:** đọc đủ lịch sử/range/EDL liên quan, viết context checklist rồi kiểm actual join: tự hash, ffprobe count120F5s và full decode; xem cut J36–59/fullcritical, sequence và toàn range C07. Report `C06_C07_LOCAL_JOIN_actual_EDIT_307.md`: không thấy reset lớn tại cut, vai nói trên hình hợp Khoai→Đào, hành động và hai bát giữ trong range; đủ trình một gói5s.

Hai lượt agent kết thúc bằng thông báo giới hạn sử dụng sau khi đã ghi hai report actual. Root tìm thấy và đọc đầy đủ cả hai; không coi status lỗi là hoàn tất mọi kiểm bổ sung. Yêu cầu QA tự đo audio packet bổ sung không hoàn tất; root đã làm phép đo mới ở `C07_ROOT_fresh_audio_verify_307.json` và không gán công trạng đó cho agent.

Root cũng xem đủ72F encoded, hai bảng crop F0–19, full F4/F5/F10/F14/F15/F48/F71 và hai cutboard J36–59; không thấy chuỗi mở miệng còn sót hoặc vùng vá cứng rõ. Đây là kiểm toàn frame bằng ảnh, **không phải đã nghe/xem AV liên tục**. ASR nối offline nhận hai câu; “gắp” bị máy viết “gấp”, không sửa lời thoại theo ASR và không dùng ASR làm chứng nhận giọng/sync.

## Tệp bàn giao để xem một thể

Gói chính: `C:/Users/PC/Downloads/du_an_nem_bui/307_C07_LOCAL_REPAIR_REVIEW/C06_C07_LOCAL_MOUTH_JOIN_5s_REVIEW_ONLY_307.mp4`, SHA `e97dd894d5225d64953145008494854fa154c691373b243e16490fdf41269fef`.

Bản C07 riêng: `C:/Users/PC/Downloads/du_an_nem_bui/307_C07_LOCAL_REPAIR_REVIEW/C07_TWOREF_LOCAL_MOUTH_v1_REVIEW_ONLY_307.mp4`, SHA `3637542889efc4dacbd1c86ebd67988b3e65472dd990fbc4a7ebc7ec9dc94d9c`.

Repo giữ bản tương ứng ở `restart_720p_v1/07_edits/`; owner copies khớp hash. Native305, bản tiếng306 và production EDL không bị ghi đè.

## Điều đã chốt, giả định và còn mở

Chốt: quyền sửa local, lời/tiếng D06 của exact3s; kỹ thuật copy audio giữ nguyên. Không biến quyền sửa thành phê duyệt output hoặc approval toàn phim.

Giả định làm việc: giữ C07 đủ3s để bảo toàn lời và hành động; không tự cắt đầu, dời tiếng hoặc kéo đuôi qua F77 có bát nhân đôi.

Cần xem gói5s để chốt perceived độ mượt miệng sửa, khẩu hình Đào, nhịp nâng bát và điểm nối/đối đáp. Đó là một cổng nghiệm thu media có ý nghĩa, không một loạt câu hỏi kỹ thuật. C06 tiếng K20 và C07 tiếng D06 standalone đã chốt; không hỏi lại các voice option.

Clearance sau bát bị che, chưa thấy xuyên rõ nhưng không đủ chứng nhận mọi contact. F71 Đào đang chớp mắt; chưa tự dùng nó làm input C08. C08 chỉ đặt cùng nem A vào **bát riêng Đào đang cầm**, không về đĩa chung hoặc miệng. Phải chốt range/exit hợp lệ trước mở input production của nhịp thả.

Food seam C05→C06 vẫn riêng, không được đóng nhờ sửa miệng C07. Nếu candidate3s được chọn, quaC07=752F/31,333s; vượt final30 32F/1,333s trước phần thả/C09. Rough35 còn88F/3,667s, chưa phải final35 đã duyệt. Không tự bỏ lời/C09 hoặc tăng tốc. Bước tiếp sau gói: chuẩn nhịp thả/thu đũa, đóng continuity và đối soát thời lượng cả tập trước bản cuối.

## Ngân sách và trạng thái

Flow submit0, debit0 trong REC307. Sổ vẫn265/500, còn235: tạo mới80 / tạo lại0 / hậu kỳ45 / dự phòng110 đóng. Không mở dự phòng hoặc chạy lại. Trạng thái **READY_FOR_BUNDLED_REVIEW, NOT_PRODUCTION_SELECTED**; không thay EDL, chưa phê duyệt C08/fullfilm/release.
