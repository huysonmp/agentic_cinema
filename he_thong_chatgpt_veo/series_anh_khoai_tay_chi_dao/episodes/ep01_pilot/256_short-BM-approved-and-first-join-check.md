# 256 — Chốt BM ngắn và kiểm điểm nối đầu

## Owner chốt

Owner trả lời “ok r đấy” sau preview REC255 và câu hỏi đủ từ “Khoan”/khớp miệng. Ghi nhận chấp nhận đúng bản ngắn 0,75 giây, SHA-256 `c6bbc9de803badf608f576f5dc47f126581db317434dcd92c00abd06698887bc`; chọn toàn bộ 18 khung output, ứng với F20–37 nguồn REC254. Đây là human acceptance đúng clip, không phải agent đã nghe, duyệt cả nguồn 4 giây hoặc cả phim. Quyết định: `restart_720p_v1/00_decisions/C01B-short-Khoan-owner-selection-256.json`.

## Kiểm thực bước kế tiếp — local, 0 credit

Đã tạo `restart_720p_v1/07_edits/C01A_BM_4p125S_JOIN_QC_NOT_FINAL.mp4`, SHA-256 `4cb1b2d7c94081ec1c301eec57f9fdfcb7d08bceb40ada089f081991ed030510`. Ghép C01A đã chọn 81 khung/3,375 giây → BM đã chọn 18 khung/0,75 giây; tổng 99 khung, 24 fps, 720×1280, 4,125 giây. Điểm cắt ở F81 / 3,375 giây.

Nguồn C01A được rehash `e22c113204c404e928683c69465237921f601f2b33a3eb9a9187eb0648f4b803`; BM được rehash như trên. Chỉ nối nguồn, không đổi lời, tốc độ, âm lượng, chồng thoại hoặc tạo frame mới. A audio 3,370667 giây được pad silence tới 3,375 giây (xấp xỉ 4,333 ms) để khớp thời lượng hình; BM audio đặt đúng 3,375 giây. H.264/AAC được mã hóa lại; không bit-exact. Đây là QC một điểm nối, không phải bản phim cuối hoặc bản 30 giây.

Root và reviewer độc lập xem liên tiếp 26 khung encoded F73–98 (8 khung cuối A, đủ 18 khung BM). Cắt từ góc hai người sang cận Khoai, giữ mặt người nói rõ. Thấy đổi cỡ cảnh/bố cục và gaze nhìn thấp → sang phải, không ghi match pixel. Không thấy chữ mới hoặc động tác gắp/ăn trong BM. Đào ngoài khung BM, contact và phản ứng của Đào vẫn UNKNOWN. Chưa nghe thực bản ghép hoặc chốt nhịp/âm nền qua cut. Reviewer: **GO_FOR_OWNER_JOIN_AV_CHECK_AND_BR_PREFLIGHT_ONLY**, root đã đọc đầy đủ report `C01A_BM_join_independent_256.md`; không đóng hai điểm nối còn thiếu. Trạng thái: `restart_720p_v1/06_qc/run-registry-256.json`.

Evidence: `C:/Users/PC/Downloads/du_an_nem_bui/256_A_BM_JOIN/`; native được giải mã đầy đủ 99 khung; script tạo board `scripts/board_ep01_a_bm_join_256.py`.

## BR — phần thiếu tiếp theo và quyền cần hỏi

BR là cảnh Đào nghe “Khoan”, nâng mắt về Khoai, buông ngón khỏi vành phải rồi thu tay về cạnh bát; tay trong hạ vào phía thân/bát, không đưa tới vành trái. Đĩa đứng yên, chưa kéo/lấy/gắp/ăn. Khoai im lặng, tay nghỉ. Cảnh trở lại góc bàn gốc, không thoại/voice mới.

Giữ hai nguồn đã duyệt, rehash khớp: START exact A80 `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb`; END exact C02F0 `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`. Prompt dự thảo hiện có: `04_requests/C01B_BR_T01_prompt_DRAFT_249.txt`; đoạn cuối “DRAFT ONLY” là ghi chú vận hành, không được gửi vào prompt sản xuất.

REC253 nâng trần đợt lên 34 và nói rõ chưa bao gồm BR; đã chi hết 34/34. Không lấy approval clip BM làm quyền chi BR hoặc mở reserve. Đề xuất **một output BR native720p/dọc/x1, tối đa 15 credit**, không tự retry; chỉ chạy sau owner chấp nhận nhịp A→BM và cấp quyền, kiểm tuyến Frames nhận START/END, kiểm im lặng/tắt voice và giá cuối live không vượt 15. Nếu tính năng không đáp ứng hoặc quote vượt trần thì dừng trình lại, không tự fallback. Chưa biết giá thực, chưa submit.

Nếu owner cấp tối đa 15: tổng trần đợt tăng từ 34 lên 49; dự án thực vẫn 108/500, chi BR tối đa sẽ thành 123, còn tối thiểu 377. Đây là dự toán, không debit thực. Reserve110 vẫn đóng. Đầu ra BR phải kiểm hành động/continuity thật rồi mới chọn range và ghép BM→BR→C02; không cho phép chế ảnh đứng hoặc cảnh món thay động tác.

## Tổng hợp vòng

- Đã xác định/chốt: BM ngắn đúng clip được owner chấp nhận và chọn; C01A/C02 giữ nguyên.
- Giả định làm việc: BR vẫn thực hiện coverage đã chốt; thời lượng chọn phụ thuộc hành động nguồn thật, không giữ 4 giây dư mặc định.
- Còn mở: owner nhịp/AV bản nối mới, BR authority/route/quote/native/selected range, hai điểm nối còn lại; chưa mở C03A hoặc finishing.
- Tiếp theo: trình bản nối và xin quyền một BR có điều kiện; không thêm test tay riêng hoặc tạo lại giọng.
