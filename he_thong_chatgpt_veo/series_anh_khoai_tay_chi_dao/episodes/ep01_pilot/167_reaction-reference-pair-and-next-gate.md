# 167 — Cặp khung cận phản ứng và cổng chạy tiếp

Ngày 2026-10-03. Owner: “ok nhé, làm đi” (gửi lại sau lượt bị ngắt). Đã kiểm worktree sạch, không thấy thay đổi dở dang. Tiếp chuẩn bị hình theo hướng chuyển động được khuyến nghị; không tự ghi audio R01 đã đạt hoặc quyền điều chuyển100 Quality. Đã gửi hai câu xác nhận cụ thể qua UI: trần134 hay giữ34; audio R01 duyệt tái dùng hay chưa.

## Đầu ra đã làm

Hai ảnh bằng công cụ imagegen tích hợp, không gọi CLI/API, không chạy Flow hoặc tiêu credit Flow. Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/167_reaction_reference_pair/`.

| Khung | Tệp | SHA256 |
| --- | --- | --- |
| START | START_Dao_close_v0.1.png | B3F6A0A1CF6B875DED2D76A47AF206CDDDF93F3FAE7EE4C62E7932B1CFA84AA9 |
| END | END_Dao_close_v0.1.png | ADA9AE45E2E31BFD58B338C7D7F544F7C0A05197F1A7FE0CBD64785A55D5098C |

START dựng từ source `161_source_retest/START_short_tuft_v0.1.png`; END sửa từ START mới. Original output giữ nguyên tại `C:/Users/PC/.codex/generated_images/01a0eb0e-6ec3-7121-a6a5-ea0ccdb77744/exec-25ff57c5-2a8f-48b8-9ad8-01d5a8b32f01.png` và `exec-672b1871-5ec7-4e4e-9048-4c60f4b0e2ab.png`. Không thay canon hoặc overwrite source.

## Review hình actual

- START: Đào nhìn xuống/phải, môi khép, giữ quả đào/crèase/cuống/lá; áo kem và nơ hồng, cốc góc dưới phải; Khoai là mép má vàng/vai áo tối ở tiền cảnh trái. END: nhìn lên/trái về Khoai, nét cười kín, môi khép; thân/áo/nơ/cốc/nền tương đối nhất quán. Không thấy thêm chữ hoặc đạo cụ mới rõ rệt.
- Đây là tái dựng góc cận, không crop chứng minh cảnh wide cũ đã hết lỗi. Khuôn mặt có thay đổi phối cảnh theo hướng đầu; phải kiểm identity qua chuyển động actual, không chứng nhận pixel-identical từ hai ảnh.
- Không thấy tay/món/miệng Khoai là lựa chọn coverage phản ứng, không phải gate PASS cho gắp/nâng/ăn. START/END này không kiểm chính xác món do món ngoài shot.
- Camera giả định vẫn giữ địa lý Khoai trái/Đào phải; cần nhìn bản dựng nối wide/cận để xác nhận eyeline, khoảng cách và trục máy, không suy trục đã chuẩn chỉ từ prompt.

## Chức năng trong câu chuyện và continuity

| Điểm nối | Đã có | Còn phải có/kiểm |
| --- | --- | --- |
| Đào quay đi → gắp | C01 chọn2,75–5,25s trong166 | Shot Đào quay đi actual, nguồn tay và vị trí cốc |
| Gắp → nâng về miệng, khựng trước tiếp xúc | C01 kết ở tuft thấp | Chưa có động tác nâng-khựng đạt; không dùng cận Đào để tự suy nhịp này đã xong |
| Khựng → Đào bắt gặp | Cặp cận167 ứng viên | Chuyển động một lần nhìn từ cốc sang Khoai, eye-line/nét cười đúng, không tự nói/gesture |
| Bắt gặp → chữa cháy | Audio R01 có file, chưa nghiệm thu | Khoai đúng giọng/lời và diễn bình thản; nếu miệng thấy rõ phải đồng bộ |
| Chữa cháy → chuyển vào bát → kết | Script32 đã duyệt | Shot chuyển-nhận không ăn/đút, cùng tuft và đúng bát; Khoai gắp miếng khác |

Không thay nội dung script32, không biến hai nhân vật thành cặp đôi. Phản ứng chỉ là một nhiệm vụ, không gộp đoạn bàn giao với quay đầu trong cùng test. Toàn bộ phim vẫn cần mở/kể chuyện/voice/claim/AI-label/final QC; cặp này không làm giảm forecast tự động.

## Prompt ảnh thực tế — START

```text
Use case: identity-preserve. Asset: single vertical 9:16 START reference for an EP01 reaction close-up, not a storyboard or collage. Image 1 is the character/wardrobe/lighting/set reference. Reframe the same small neat Vietnamese street eatery to a tighter eye-level frontal medium close-up of Dao, remaining on the same front side of the table, same left-right screen geography. Dao is the EXACT same adult anthropomorphic peach fruit woman: preserve her face proportions, peach skin texture, crease, brown stem, green leaf, large brown eyes, eyelashes, cream blouse and pink waist ribbon. Keep her head turned gently DOWN and SCREEN RIGHT looking towards the water glass at her right, as in the reference START. Lips softly closed, relaxed expression, not already looking at Khoai. Include a narrow out-of-focus edge of Khoai's navy jacket shoulder and golden potato cheek at far LEFT as an eyeline anchor; don't show his mouth, hands, chopsticks or food in this face-focused shot. Dao framed head to upper torso, complete leaf visible, hands below crop. The existing water glass may be partly visible at bottom right, but do not invent a new table arrangement or food. Match original warm amber light, street lanterns/background and stylized 3D materials, no studio/new costume/new characters. Only change camera framing; preserve the actual head orientation/expression and character identity. No text, no labels, no logos, no montage.
```

## Prompt ảnh thực tế — END

```text
Use case: precise-object-edit / identity-preserve. Image 1 is the exact edit target. Create the END frame for this same vertical 9:16 reaction shot. Change ONLY Dao's head orientation, eye direction and a tiny expression detail: she has just turned from looking down screen right at her glass to looking UP and SCREEN LEFT at Khoai's face, beyond the blurred potato cheek/shoulder at far left. A subtle knowing, gently amused expression, one brow lifted only a little, lips closed with a small restrained smile, not laughing or speaking. Keep her adult anthropomorphic peach identity, exact face/eye size and materials, crease, brown stem and green leaf attached correctly. Keep the cream blouse, pink ribbon, torso and forearms in the EXACT same pose and place, same camera/scale/framing, glass/table wood edges, lighting, street lanterns/background, and blurry Khoai foreground shape and position unchanged. Do not add or reveal hands, chopsticks, food, other characters or props. Single final still frame, no text, no panel layout.
```

## Gói video dự thảo — CHƯA SUBMIT

```text
Locked camera. Match the supplied frames. Dao slowly turns her head once from looking down at her glass on screen right to looking up at Khoai on screen left, then holds a gently amused knowing look. Her lips stay closed. Her torso and arms remain at their supplied positions. Keep the blurred potato cheek and navy shoulder still at the left edge. Preserve the same peach face, leaf, blouse, glass, light and background.
```

Dự thảo x3 Veo Lite/Frames/9:16, giá lịch sử30, dự kiến8s nếu UI vẫn như164; actual chưa đọc. Trước chạy phải kiểm model/giá/khung thật và Tác nhân tắt, không tự bật Quality. Gate: quay nhìn đúng một nhịp, giữ sau phản ứng, không miệng nói/gesture, cốc/thân/tiền cảnh không trượt, identity và lighting ổn; kiểm video toàn clip/đoạn dày và nối với shot Khoai, không chỉ ảnh. Audio và nhịp câu bắt gặp tích hợp sau khi owner nghiệm thu.

## Tổng hợp và quyền chi

Đã xác định: cặp khung phản ứng cận đã lưu, kiểm và truy nguồn/hash. Đã chốt trong phạm vi: tiếp tục chuẩn bị theo hướng chuyển động, chưa sinh video mới. Giả định: góc cận tách một nhiệm vụ có thể dễ kiểm hơn; chưa thử, không gọi là cải tiến đã chứng minh. Còn mở: chuyển động actual, nối trục, shot nâng-khựng/chuyển-nhận, audio R01 và quyền điều chuyển. Trial34/Quality100 vẫn riêng; chi Flow mới0, không đọc lại số dư tài khoản. Bước tiếp: chốt hai câu xác nhận ngân sách/audio, rồi khóa thứ tự các bộ trong trần được duyệt; không tiêu30 để còn4 mà chưa có kế hoạch hoàn thiện được chấp nhận.
