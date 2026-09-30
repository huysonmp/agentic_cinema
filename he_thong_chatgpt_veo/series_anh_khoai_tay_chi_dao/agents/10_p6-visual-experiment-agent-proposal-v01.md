# P6 — Bổ sung năng lực kiểm hình và điều phối thử nghiệm

Ngày 2026-09-30. Status PROPOSED / OWNER_APPROVAL_PENDING. Owner hỏi có cần build thêm agent; đây là đề xuất cụ thể, không tự duyệt runtime mới hoặc dispatch reviewer. Không thay authority image-only hiện hành và không mở voice/video.

## Hiện trạng đã đọc

PROD7 prompts03: CHAR thiết kế tay/góc/nhân vật; ART có appearance ledger và food fidelity; CTD lập probe; PROMPT có request manifest/acceptance. Tier1 prompts03: CONT đối chiếu identity/food/props và UNKNOWN; FLOW lập bounded probes; RIGHTS giữ research-only boundary. Các file có prompt implementation nhưng vẫn chứa runtime-review/test-pending; không gọi đây là agent đã tự động chạy hoặc reviewer độc lập đã kiểm các ảnh52–54. QC các ảnh hiện tại là root operator observation.

Khoảng trống thực tế: nhiều lượt repair53 vẫn lỗi grip; chưa có role sở hữu xuyên suốt hypothesis → một thay đổi → input read-back → ảnh thật → failure taxonomy → lựa chọn lượt thử sau. CONT có continuity nhưng chưa có checklist cơ học tay/đạo cụ chi tiết. Thêm agent không bảo đảm model tạo đúng tay.

## Khuyến nghị: một role mới, một amendment

### AG-VEXP-01 — Visual Experiment Lead

Vai trò mới độc lập với maker và reviewer: quản lý thiết kế thí nghiệm, không tạo hình thay CHAR/ART, không tự QC-pass hoặc thao tác Flow. Dùng common contract PROD7 cùng envelope/allowlist; operator vẫn root dưới authority owner, quyết định final vẫn owner.

Input: mục tiêu hình/approved invariants, raw refs với role/hash/status, request history/settings/UI evidence, actual outputs và reviewer findings, authority/cap. Thiếu ảnh thật thì chỉ planning; không kết luận từ prompt.

Prompt nhiệm vụ đề xuất:

> Đọc lịch sử được cấp. Chọn lỗi quan trọng nhất còn mở và viết giả thuyết có thể bị bác bỏ. Đề xuất tối đa hai test phân biệt được nguyên nhân, mỗi test thay một yếu tố; ghi đối chứng, refs/canvas riêng, settings, expected visual signal và tiêu chí fail/unknown. Không lặp một prompt đã fail nếu không nêu thay đổi có ý nghĩa. Tách identity drift, input binding, framing/visibility, anatomy/contact, food fidelity và integration failure. Sau output, đối chiếu bằng ảnh thật và báo kết quả không trùng role reviewer; nếu chưa có reviewer ghi rõ. Đề xuất route CHAR/ART/CONT/FLOW hoặc owner, không tự promote asset, giảm chuẩn, đổi script hay cấp quyền generate. Giá UI và credit thực thanh toán là hai dữ kiện khác nhau. Một lượt submit chưa rõ kết quả phải reconcile, không submit lại mù.

Output bắt buộc: experiment_id; open defect; hypothesis; one changed factor; controls; input manifest; exact request proposal; current price evidence; authority; expected signal; result/unknown; comparison; next test/stop rationale. Mỗi cycle không quá hai phương án đề xuất, không tạo trần credit mới thay owner.

Fixture trước pilot: (1) đẹp nhưng grip sai → không promote; (2) thiếu thumb vì bị khuất → UNKNOWN; (3) cùng prompt fail nhiều lần → test khác nguyên nhân; (4) ref chỉ trong history → input ambiguity, không giả explicit attachment; (5) giá0 → không unlimited authority; (6) food AI giống candidate → không coi là evidence món thật. Fixture chỉ paper/behavior, không chi credit.

### CONT amendment — Anatomy & Prop Interaction checklist

Không thêm reviewer thứ hai trùng CONT. Đề xuất bổ sung checklist: đúng tay theo canon và góc thấy được; số ngón visible/hidden tách rõ; hai đũa liên tục, không xuyên tay; thumb/index/middle control upper, lower có điểm tựa; tip/handle và hướng màn hình; tỷ lệ tay/cánh tay; vật gắp/contact/gravity/readability. Static still không chứng minh opening/closing/transfer motion. Nếu không đọc được cấu trúc, UNKNOWN hoặc REWORK theo acceptance, không PASS bằng vẻ đẹp. Findings có crop-region description/version, severity và closure evidence. Reviewer không nhận maker rationale trước lượt quan sát đầu.

ART không cần agent food mới: bổ sung source provenance, visual evidence vs text/caption, serving variant và phần có thể gắp theo54. Nguồn món cần human am hiểu nếu provenance/biến thể chưa rõ, không giả lập chuyên gia địa phương bằng thêm agent.

## Gate và bước tiếp

Owner cần duyệt role VEXP + amendment CONT trước triển khai prompts/fixtures và pilot dispatch. Chưa build runner/API integration: không cần cho việc thử Flow hiện tại. Nếu approved: triển khai versioned contract/role/fixtures → kiểm behavior → pilot bounded trên grip/food thật → đánh giá role có giúp phát hiện/phân loại lỗi, tránh retry mù và giữ traceability không. Không hứa nâng chất lượng chỉ nhờ số lượng agent.
