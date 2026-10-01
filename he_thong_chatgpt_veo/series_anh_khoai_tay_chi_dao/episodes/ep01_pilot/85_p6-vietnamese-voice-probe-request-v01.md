# EP01 — Request thử tiếng Việt v0.1

2026-10-01 (Asia/Saigon). `PREPARED / EXACT_REQUEST_APPROVAL_PENDING / NOT_GENERATED`. Tiếp nối84, giữ hướng38 và ưu tiên Flow/Veo64. Owner yêu cầu tiếp tục các phần; chưa coi là approval cho request mới bên dưới.

## Preflight thực tế

Root đọc đúng project9276788e-9781-44fb-ba5b-083006667374 trên IAB. Cài đặt tác nhân: Luôn luôn xác nhận được chọn; video mặc định16:9/x1. Menu có Omni1.1Flash, Veo3.1Lite/Fast/Quality. Mở thao tác Expand ở Quality làm menu đóng và màn hình hiển thị Quality; không bấm Lưu, đóng panel. Không xác nhận đã đổi model mặc định được lưu. Lỗi kết nối reCAPTCHA hiện lúc đầu, không còn trong AX sau một lần reload; không giải CAPTCHA hoặc suy lỗi đã vĩnh viễn hết. Chưa thấy cấu hình duration/audio/voice-ID hoặc giá exact request. Không submit, upload, tạo media hay đối soát billing trong vòng này.

## Mục tiêu và phạm vi

Hai clip thử riêng, không clip sản xuất cuối: nghe chất giọng Khoai ở ký ức và cả hai ở đối đáp. Không thử động tác ăn vụng/đũa trong cùng vòng nhằm tránh lẫn lỗi chuyển động với lỗi tiếng. Hành động trong test là tối giản, không thay shot79/81 hoặc kịch bản32. Mẫu không đủ để khóa giọng toàn series; cần kiểm lặp lại sau lựa chọn.

Target cho mỗi mẫu: Flow / Veo3.1Quality / frames-to-video nếu UI hỗ trợ /9:16 /8 giây /x1. Nếu mode không hỗ trợ hoặc model khác, dừng và trình lại, không tự dùng Omni/provider khác. 8 giây là chiều dài request dự kiến, chưa duration thoại đo được. Reference duy nhất đề nghị dùng: T-NB-03_v0.8 đã duyệt78, ảnh hiện có trong đúng project; không upload ảnh người thật hoặc clone. Phải kiểm chọn đúng version trước attach. Input ref approval cho thử voice nằm trong request này, không suy từ static approval.

Chạy V01 trước, lưu và nghe rồi mới chạy V02 khi terminal/output và chi phí V01 đã đối soát. Tối đa hai generation/output, không retry/biến thể tự động. Giá mỗi lượt `UNKNOWN`: cần exact UI read-back; cap200 tổng hiện hành không được gia hạn. Chỉ chạy khi đối soát chi phí thử trước đây đủ để biết phần cap còn lại và hai lượt nằm trong phần đó; không lấy số dư tài khoản làm cumulative spend. Không mua credit. Lỗi/CAPTCHA/moderation/không rõ terminal/giá không xác định → dừng, không duplicate.

## Prompt V01 — Khoai, ký ức

```text
Create one vertical 9:16, 8-second diagnostic video using the supplied approved table image as the starting frame. Preserve the adult potato character Khoai on the left and adult peach character Dao on the right, their exact faces, outfits, warm Vietnamese street-side eatery, food, leaves, sauces, bowls, chopsticks and glass. Locked camera; both remain seated. No picking up utensils, eating, drinking, plate pulling or food transfer. Only subtle natural facial movement and speech; Dao listens silently. No added people, captions, music or narration; preserve the platform watermark. Keep ambience quiet so speech is easy to judge.
Khoai alone speaks in Vietnamese, in this exact order with no added words: "Khoan. Mùi này làm anh nhớ cái chảo." Then: "Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ."
His voice is an original adult male medium-low warm voice with a light Northern Vietnamese accent. Calm and mature, natural conversational rhythm, a memory occurring to him rather than an explanatory voiceover; no exaggerated sadness, old-man caricature or celebrity imitation. Preserve natural short pauses, do not rush or truncate the words to fit. No speech from Dao. Synchronize mouth movement only to the speaking character.
```

Hai câu Khoai trích nguyên văn32, nhưng bỏ lượt Đào xen giữa chỉ trong probe đơn giọng; không phải revision nội dung episode. V01 không kiểm full dialogue continuity.

## Prompt V02 — Đối đáp chữa cháy

```text
Create one vertical 9:16, 8-second diagnostic video using the same approved table image as the starting frame. Preserve the same adult characters, faces, outfits, left-right placement, table, food, leaves, sauces, utensils and glass. Locked camera, both stay seated with hands resting. Do not animate chopstick handling, food transfer, drinking or eating. This is a voice-and-expression test, not the final action shot. No added people, captions, music or narrator; preserve platform watermark. Quiet ambience.
Speak the following exact Vietnamese dialogue once, in order, without overlap or extra words:
Dao, the adult peach woman on the right: "Chờ em quay lưng nữa à?"
Khoai, the adult potato man on the left: "Anh gắp cho em mà."
Dao: "Thế em quay lại đúng lúc rồi."
Dao has an original adult female bright, flexible and approachable voice, a light Northern Vietnamese accent. She knows what he is doing and teases lightly; not a child voice, scolding mother or romantic delivery. Khoai has the same adult male medium-low warm voice direction as V01, calm dry humor, a matter-of-fact excuse rather than panic or flirtation. Keep natural short response pauses; never rush or omit words to fit. Only the active speaker's mouth moves for each line. Do not imitate any real person.
```

Giữ nguyên ba câu cuối32. Prompt nói same voice direction không chứng minh model giữ cùng voice identity; phải nghe so V01/V02. Đây chưa phải voice reference hoặc voice-ID lock.

## QC và hồ sơ bắt buộc

- Lưu prompt thực, input/version, UI model/mode/aspect/duration/count/giá, generation ID nếu hiển thị, terminal và file/hash. Không ghi requested settings thành actual settings.
- Nghe thực từng mẫu: tiếng Việt đủ nguyên văn, đúng speaker/thứ tự, không thêm/nuốt câu, dấu thanh rõ; lỗi trọng yếu không lấy transcript tự sinh để phủ nhận.
- Kiểm Khoai ấm/tỉnh, Đào sáng/trêu kín/trưởng thành; không đọc quảng cáo, không mẹ mắng/romance. Ghi mốc thời gian và lỗi nghe cụ thể, không chấm từ prompt.
- So Khoai V01↔V02: chỉ hai mẫu vẫn chưa đủ chứng minh consistency cả series. Đo speech/response pauses thực và tổng clip; không suy episode đạt30 giây.
- Nếu reviewer/root không có kênh nghe audio thực, đánh dấu LISTENING_PENDING và đưa owner nghe; tuyệt đối không báo audio PASS từ hình hoặc văn bản. Lip-sync có trạng thái riêng.
- Chọn candidate chỉ sau nghe/QC và owner duyệt take cụ thể. D1A/D2A vẫn giữ; test tối giản này không chứng minh choreography đạt.

## Tổng hợp

Đã xác định: model options và confirmation UI được đọc thực; hai probe exact đã so với32. Đã chốt: hướng giọng38, route ưu tiên64, coverage/choreography84 không đổi. Giả định:8 giây phù hợp mỗi probe, Quality phù hợp thử; phải kiểm bằng đầu ra. Còn mở: approval request85, exact mode/cost/cap remaining, chọn ref đúng version, nghe/đo thật. Bước tiếp: owner duyệt hai probe và reference; operator preflight, dừng nếu khác cấu hình/không rõ giá; chỉ sau đó mới submit từng lượt.
