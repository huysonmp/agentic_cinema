# REC275 — C06 T03: phản biện độc lập bản đề xuất 57 khung

Ngày 12-10-2026. RUN_ID: REC275-C06-T03-PREFIX57-INDEPENDENT.

Kết luận: **PLANNING_PROPOSAL_PRESENTABLE / OWNER_BOUNDARY_DECISION_REQUIRED / NOT_SELECTED / AUDIO_AV_HOLD / C07_HOLD**. Bản này có A còn kẹp và bát rỗng, không chứa lỗi thả ở đuôi native. Tuy nhiên kết thúc khi tay đang di chuyển, không chứng minh endpoint “dừng và giữ chờ” của brief cũ.

## Target và bằng chứng thực xem

Target duy nhất: `C:/Users/PC/Downloads/du_an_nem_bui/275_C06_T03/C06_T03_CUT_F0_F56_PROPOSAL_ONLY.mp4`. SHA-256 tự tính lại **`58f13ea424300e0cde09000d37cf42839ac7b8ba7c6d2d6f64c02eeb9022594d`**, khớp manifest và evidence.

Nguồn: `05_native/EP01_720_C06_T03_NATIVE.mp4`, hash đã tự xác minh trong actual275: `36f04086a2e3d6d3d688f64ca743909184955bf1a714094def5dd8cd3747ff7c`. Proposal dùng range **[0,57)**, F0–56, 57 khung / 24 fps = **2,375 giây**. F56 có timestamp2,333333 giây và được giữ tới hết frame. Đây là derivative encode, không được gọi bản native4 giây đạt.

Thư mục kiểm: `C:/Users/PC/Downloads/du_an_nem_bui/275_C06_T03/prefix57_qc/`. Đã đọc đầy đủ `native_evidence.json` và `action_all/manifest.json`. Đã trực tiếp xem **toàn bộ tám board action_all_01–08.jpg, đủ57 encoded frames F0–56**; board08 chỉ có F56. Xem PNG nguyên khung endpoint F56 (`all_native_frames/00057.png`) và START đã chốt từ C05 nativeF65, hash ref `f091e35fc7c779591c918c47ba34752a8a2c3b30de507cd99dc0e76143e83196`.

Scope: **ALL_ENCODED_FRAME_STILLS_NOT_AV**. Không nghe hoặc xem AV liên tục; không browser/credit/API/new tools/scripts/ASR hoặc chỉnh media. Không đọc maker prefix. Root báo packet check113 payload/PTS khớp source prefix; reviewer không tự thực hiện packet comparison, không dùng thông báo đó chứng nhận lời hoặc sync.

Evidence kỹ thuật đã đọc: H264720×1280, 24 fps,57 khung/video2,375 giây; AAC48 kHz stereo, audio/container2,389333 giây, decode thành công. Audio dài hơn video **14,333 ms** do boundary packet được bảo toàn. Không tự kết luận lệch khẩu hình nghe thấy hoặc làm mất lời từ số này; khi nối thực phải kiểm tail/mix và không lấy duration container thay frame EDL.

## Findings trên đúng derivative

| Scope | Quan sát | Disposition |
|---|---|---|
| Người nói và mặt | Khoai có chuỗi khẩu hình, Đào môi khép. Mặt và mắt hai người hiện rõ; entry gần START. Khoai có mày/mắt ngượng và vài nhóm miệng mở ngang có nét cười như nguồn T03. | Không chấm chỉ vì thấy răng hoặc áp cue một khóe đã bỏ. Diễn nghệ thuật cần owner kiểm trên proposal cùng tiếng; chưa acting/voice/sync PASS. |
| SAME A / own pair | Một miếng A vẫn kẹp trong đôi đũa riêng tay ngoài trái Khoai qua toàn57 khung; không ăn, lấy miếng khác, đổi tay/đũa hoặc thả. | Không thấy early release trong prefix này. Lỗi release của full native từ F80 vẫn giữ trong actual report và không bị xóa bởi trim. |
| Cốc và hai bát | Đào giữ cốc nâng trong tay ngoài, đáy tách bát; hai bát riêng còn rỗng, đọc được. Không hạ cốc hoặc nhấc bát nhận. | Hình props đạt điều kiện để trình proposal trong scope ảnh. Không tự tạo C07 reference từ endpoint chưa chọn. |
| Đường A và endpoint | A chuyển về phía Đào sau nhóm khẩu hình. F56 còn ở phía Khoai của bát, trên bàn, khoảng hở tới vành rõ; chưa vào bát hoặc chạm đĩa/chấm. | Endpoint an toàn hơn vùng F63–72 gần vành, nhưng tay vẫn tiếp tục chuyển trong chuỗi F48–56. Đây là **cut-on-motion**, không phải end hold. |
| Bối cảnh | Two-shot, bàn/món nguội/rau trước trái/hai chấm, trang phục, ánh sáng và watermark giữ. | Không có insert/crop che người nói để giấu lỗi. Actual motion liền mạch và seam chưa được xem/duyệt. |

## Boundary mới cần được owner chốt

Trong [0,57), không thấy đoạn dừng ổn định sau redirect; frame cuối vẫn thuộc quá trình đưa A. Nếu chọn phương án này, C07 phải tiếp nhận **chuyển động đang diễn ra**, không mặc định Khoai đã giữ A ở điểm chờ. Phải kiểm hướng, tốc độ, vị trí A/tip, cốc và bát qua seam để không nhảy tay hoặc thành pause vô lý.

Do đó có thể trình proposal để owner xem, nhưng không nói “C06 đã hoàn thành endpoint giữ chờ theo brief”. Chấp nhận cut-on-motion là quyết định về boundary, không phải nghiệm thu full nativeT03 hoặc tự bỏ C07 nhận/C08 thả. Chưa có cảnh nối để chứng minh giải pháp dựng đạt; khả năng nối tốt chỉ là dự kiến.

Phần lời/giọng: môi khép trước chuyển tay không chứng minh đủ N06 hoặc âm “mà”. Metadata và copy packet không thay nghe. Owner approval tiếng T02 chỉ áp T02; **T03/proposal tiếng mới vẫn cần nghe đúng Khoai/K20, trọn câu và nhịp**, rồi kiểm sync trên đúng derivative và cut tiếp theo.

Nếu owner chọn [0,57), thời lượng hình qua C06 là26,333333+2,375 = **28,708333 giây**, còn **6,291667 giây** đến trần35 cho C07–09. Đây là tính điều kiện, không bảo đảm đủ nhận–thả–kết, không tăng trần hoặc thay lời.

## Handoff

Cho phép **trình bản PLANNING proposal này với disclosure đầy đủ**, không SELECT, không old-hold PASS, không audio/AV PASS hoặc C07 ref. Owner cần chốt boundary giữa chuyển động và phạm vi diễn/tiếng trên đúng file; root vẫn phải kiểm seam và timing thực khi có cảnh tiếp. Báo cáo này không authorize generation, T04 hoặc công cụ/voice/coverage mới. Full nativeT03 STOP vì thả sớm giữ nguyên.
