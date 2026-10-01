# EP01 — Review boundary coverage B v0.1

2026-10-01. Run `EP01-P7-FLOW-02`; `AG-FLOW-01 / P7 / PAPER_REVIEW`; retained context từ FLOW-01, không fresh-blind.

## Actual access, target và giới hạn

- Đọc section FLOW-02 cập nhật trong production_team12; đọc toàn81 và đọc lại toàn80. Kế thừa việc đã đọc toàn79/script32/contracts/allowlist và xem static T08 trong FLOW-01; không media access mới.
- Kiểm local SHA256:81 v0.1 khớp `0CA2C8FC6AEC57C3124AA0DE2C60C3DAA70099D6C6A216FA76915F403A06366A`;79 giữ `77876F589D0F2090DCEFC6B75941167752C9809E12E6E6AA8635C7975945C0D7`.
- Target là composed proposal79+81;81 chỉ thay coverage S04 bằng B1/B2 nếu owner chọn B.80 được giữ nguyên làm report lịch sử.
- Không đọc maker chat, CTD11,74/76,18/19 hoặc root83. Không network/browser/audio/video/generation/upload/credit/Git/agent con; chỉ tạo82 bằng apply_patch.
- Scope chỉ đóng thiếu specification FLOW-F04 và kiểm regression lời/cause/joins; authority78 vẫn P7 paper, không owner chọn B/shot lock/request approval.

**Verdict closure: `PASS_FOR_NEXT_GATE / PAPER_SPEC_ONLY`. FLOW-F04 (MINOR) = `VERIFIED_CLOSED_PAPER_SPEC` trên composed79+81.** Boundary đã có mô tả đủ để trình lựa chọn A/B và chuẩn bị action-state/request; chưa xác nhận clip nối được.
**P7 proposal tổng thể vẫn `PASS_WITH_ACTIONS`; generation readiness vẫn `BLOCKED`.** FLOW-F01/02/03/05 giữ UNKNOWN và dependency từ80; không timing/motion/runtime PASS.

## Coverage và regression

| Check | Status giấy | Evidence exact / limitation |
|---|---|---|
| J3B1 / start | MET |81 B1 start kế đuôi câu6, P0/chưa gắp, đũa còn bàn, Đào phải chưa lấy cốc/trái cạnh bát. Khớp79 end S03 và mở khung trước thực quay; không lặp setup. |
| Cốc B1→B2 | MET |81 B1 end: Đào phải vẫn giữ cốc ngoài phải thân, chưa đặt/không uống. B2 start lặp đúng state; bát chưa nâng nên không reset cả cốc và bát. |
| Tay/bát/đũa/A B1→B2 | MET |81 B1 end = B2 start: Khoai phải kẹp A ngoài miệng, chưa contact/chưa đổi hướng; trái cạnh bát. Đào trái cạnh bát còn bàn; P0−A; đũa Đào/chén/lá đứng yên. |
| Eye-line/bắt gặp | MET |81 B1 end Đào nhìn vùng A/miệng Khoai, Khoai nhìn cô/khựng; B2 bắt đầu từ đã thấy, không replay quay lại. Camera cùng phía trục/Khoai trái–Đào phải; hướng này giữ cause trước chữa cháy. |
| Câu7 tại boundary | MET |81 B1 chứa trọn Đào: “Chờ em quay lưng nữa à?”; cut sau câu7/đuôi âm, trước đổi hướng. B2 không lặp câu7 hoặc làm A hướng cô ngay đầu. |
| Câu8→9 / B2 | MET |81 B2: Khoai “Anh gắp cho em mà.” rồi Đào “Thế em quay lại đúng lúc rồi.”; đúng32/79. Đào nhìn A rồi anh, đặt cốc trước nhấc bát nhận, giữ trò đùa và thái độ trêu kín. |
| End B2→S05 | MET |81 end: A chưa thả trên đũa trên bát Đào cầm trái; cốc đã về bàn ngoài phải, phải rời cốc; P0−A.79 S05 start cùng state, đặt A đúng một lần→gắp B→P0−A−B, không ăn/đút. |
| Regression9 câu/cue | MET |79 S01 có câu1–2, S02 câu3–4, S03 câu5–6;81 B1 câu7, B2 câu8–9; S05 không thoại. F01/F02/AI kế thừa79, không thêm lời/claim/cue giải thích joke. |

Causal coverage giấy còn đủ: Đào quay tạo cơ hội→A từ đĩa về miệng Khoai→Đào quay lại thấy→khựng ngoài miệng→đổi hướng→bát nhận→câu trêu→đặt A/gắp B. B1 vẫn phải thấy cả đường A và mắt Đào; B2 không neutral reset. Không suy mô tả này thành khán giả thực đã hiểu hoặc motion hợp cơ học.

## Findings và closure evidence

- FLOW-F04: yêu cầu80 thiếu exact cốc/tay/bát/A/đũa/eye-line tại B1→B2 đã được hai boundary rows81, JB1B2 và B-JOIN trả lời nhất quán; phần B-END/JB2S05 khớp S05. Không defect giấy mới trong phạm vi này.
- Closure chỉ thiếu specification; kiểm media join còn mở ở FLOW-F02: actual boundary frames/playable audio phải giữ A ngoài miệng/chưa đổi hướng, cốc trên tay/bát chưa nâng ở join; end B2 cốc trên bàn/bát nâng/A chưa thả; transfer không lặp/biến mất/nhân đôi.
- FLOW-F01: route/native/account feasibility UNKNOWN. FLOW-F03: TARGET4–6s/6–8s và tổng≈30s vẫn không MEASURED. FLOW-F05: mode/rights/count/cap/stop/cost/request approval chưa có.81 không thêm feature promise hoặc quyền execution.
- Disposition: KEEP79+81 làm proposal có boundary B đầy đủ trên giấy; KEEP80 nguyên lịch sử; HOLD shot lock/media acceptance/generation readiness. Không cần sửa script hoặc dùng feature/model mới để đóng FLOW-F04.

## Handoff năm phần

1. Đã xác định: thiếu boundary specification B đã đóng trên giấy; đủ9 câu và không regression cause/portion/joins.
2. Quyết định owner hiện có: upstream content/refs/P7 paper/Canva; chưa chọn A/B hoặc duyệt choreography/request.
3. Giả định: W-HAND/W-PROP, crop cùng phía trục và điểm cắt sau câu7 tại nhịp khựng; TARGET ranges là proposal.
4. Còn mở: owner coverage/staging; action inputs, actual voice/timing/motion, route/account/rights/cap/cost/request từ80.
5. Tiếp theo: root trình A/B với81/82 cho owner; sau lựa chọn mới hoàn thiện P8 packet và bounded probe đúng quyền. Chỉ media thực mới kiểm boundary frames/audio/in-out rồi clip pack/Canva export.
