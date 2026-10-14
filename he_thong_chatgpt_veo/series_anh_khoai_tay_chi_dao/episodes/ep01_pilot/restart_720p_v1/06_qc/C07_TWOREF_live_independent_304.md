# REC304 — Preflight độc lập C07 RECEIVE TWOREF T01

**CONDITIONAL_READY_TO_PRESENT / PAID_SUBMIT_HOLD.** Gói giấy và proof chuẩn bị đủ trình quyết định một lượt; chưa có quyền trả phí, chuyển bucket hay approval output.

## Phạm vi thực kiểm

- Local read/view/hash theo quyền reviewer REC217 root giao; không browser/API/chi/Git, không nghe hoặc xem output mới.
- Đọc đủ acceptance304, prompt FINAL304, regression pack303, independent303, actual T01/T02 REC277, root actual280 và independent actual302.
- Xem F47, portrait303 và năm proof `PREPARED_NOT_SUBMITTED`, `CONFIG_QUOTE_7`, `D06_PICKER`, `SOURCE_AUDIO_ON`, `BALANCE_BEFORE`.
- Tự kiểm prompt SHA `e07e76d6b798e59d4443bcad016655b9ab72e204e67dfc52a3c84631dde9e435`; hai PNG khớp hash acceptance304.
- Preparation JSON chưa hiện trong danh sách local304 khi kiểm. Root cần lưu manifest/read-back/IDs/status cuối; report này không giả định đã đọc file ấy.

## Đúng phạm vi input đã duyệt

- Acceptance304 chỉ nhận portrait v1 làm neo phụ cùng F47 với caveat redraw; loại trừ paid/retry, reallocation/reserve, voice/AV/output/EDL approval.
- F47 là authority duy nhất về camera, scale, expression, clothes, light, props và inherited state; portrait chỉ hình thái/mặt hai nhân vật, không endpoint.
- Trực tiếp thấy F47: Khoai trái giữ A trên đũa, tay kia nghỉ; Đào phải là quả đào có cuống/lá, tay ngoài nâng cốc, tay trong rảnh cạnh bát; hai bát riêng và đũa nghỉ còn.
- Portrait vẫn cùng loài/tạo hình, không tóc/tai người; mắt/mày/môi/texture/scale/cuống/lá được redraw. Không gọi exact pixel hoặc landmark lock; F47 thắng khác biệt.
- FINAL nêu đúng hierarchy; chỉ tay trong Đào nâng đúng bát rỗng lên trước rồi sang dưới A, có khoảng hở tay/bát Khoai; tay ngoài giữ cốc nâng suốt cảnh.
- A giữ kẹp, không release/ăn/cho tới miệng/gắp lại; Khoai nghe môi khép; chỉ Đào nói nguyên N07 “Thế em quay lại đúng lúc rồi.” bằng saved D06.
- Không thấy MAJOR tự mâu thuẫn trên giấy. Grip một tay, clearance, nhịp 4s, bát dưới A và identity vẫn là rủi ro thực, không physics/voice/acting PASS.

## Proof chuẩn bị và giới hạn

- Proof thấy hai chip ảnh cảnh/portrait và một chip voice; picker hiển thị saved `EP01_Dao_D06_Aoede_720p_v1` với performance nữ Bắc. K20/base Aoede là mục khác, không là chip chọn.
- Screenshot không chứng minh toàn prompt; root báo read-back exact. Scene ID `e40803c5-9a46-44af-84d6-a588ef762895`, pair ID `4612c33b-de15-456c-8fbf-1e441f1791a3` là DOM img-src do root đọc, không reviewer đọc live.
- Voice opaque ID không hiện; không gọi UUID D06 mới được xác minh hoặc suy giọng output từ tên saved/SoT238.
- Config proof: Ingredients / Omni 1.1 Flash / 720p / 9:16 / 4 giây / x1 / quote 7. Default 8s đã sửa theo root và proof hiện 4s.
- Proof no-audio toggle ở off, Agent không được chọn; root báo cả hai aria=false. Không suy flags thành bảo đảm AV. Giữ native watermark.
- Balance proof 1.022; account balance không thay ngân sách dự án. Tab mới phục hồi sau CUA reset là root báo; phải refresh inputs/config/quote nếu trạng thái đổi trước click.

## Hồi quy và cổng actual bắt buộc

- REC277 T01 chọn bát Khoai; T02 hóa người/mất bát/reset state. REC280 giữ loài nhưng reset entry, cho ăn, Khoai mở miệng, cốc hạ và endpoint sai; review độc lập280 chưa hoàn tất.
- REC302 hóa người F0–95, cốc về bàn, hai tay nâng bát, đũa nghỉ mất, Khoai mở miệng. Gói mới phải kiểm riêng từng lỗi; hai ảnh không khóa choreography.
- Hai ảnh và wording cùng thay nên không phải thử một biến, không chứng minh D06 gây lỗi hoặc portrait sẽ sửa được.
- Actual F0 phải so F47 đủ hai mặt/loài, A, hai bát, tay/cốc/đũa và pose; MAJOR reset → loại. Toàn nguồn kiểm ownership, lift-before-sideways, clearance, glass và A chưa thả.
- Nghe exact native và kiểm AV thực để chốt D06/N07/âm cuối/speaker/lip-sync/nhịp; ASR/prompt/preset không thay nghe. Chỉ range đạt mới làm exit cho C08; không prefix/crop che identity.

## Blocker quyền và ngân sách

- Retake còn 5 < quote 7: **HOLD** cho tới owner chốt chuyển bucket và quyền một request mới; REC302 đã tiêu hết, acceptance304 không mở lại.
- Đề xuất tối thiểu 2 từ first-pass82→80, retake5→7; nếu duyệt rồi debit đúng7 thì retake0, project258→265/500, remaining242→235; post45/reserve110 giữ nguyên, reserve CLOSED.
- Các con số trên là phương án điều kiện, không ledger đã áp dụng. Không tự retry/chuyển bucket/submit/đổi route hoặc đảm bảo output; food seam và conflict final30/rough35 vẫn mở.
