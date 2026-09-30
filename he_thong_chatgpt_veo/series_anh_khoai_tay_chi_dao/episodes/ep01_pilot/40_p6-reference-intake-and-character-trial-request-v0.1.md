# EP01 — P6 reference intake và request thử base nhân vật v0.1

Ngày: 2026-09-30. Status: OWNER_RUN_APPROVAL_PENDING / NOT_RUN.

Upstream: [approval38](38_p5-content-handoff-and-p6-direction-approval.md), [spec39](39_p6-character-voice-design-and-sample-plan-v0.1.md). Root research/request draft, không PROD7 runtime run, không mẫu đã kiểm.

## 1. Research intake thực hiện

| Nguồn | Truy cập lượt này và giới hạn |
|---|---|
| [VietnamPlus/TTXVN, 03/12/2014](https://www.vietnamplus.vn/hoc-trom-nghe-lam-nem-thinh-bui-xa-dung-chat-o-bac-ninh-post294563.amp) | Full text, đoạn91–99 mô tả thịt cắt nhỏ/trộn thính/gói lá và dùng với lá sung. Ảnh credit Thanh Thương/TTXVN; footer269 yêu cầu chấp thuận bằng văn bản khi sao chép. |
| [Trang Bộ Công Thương, 08/02/2023](https://thuongmaibiengioimiennui.gov.vn/dac-san-vung-mien/2023/2/nem-bui) | Full text, đoạn16–18 mô tả phần thịt/bì dạng sợi, trộn thính, nắm/gói. Dòng23 ghi nguồn Hà Nội Mới: repost, không nguồn điều tra độc lập. |
| VOV5/R2 ở pack P2 | Trả 503 lượt này; không phủ nhận evidence cũ, không giả đã đọc lại. |

Appearance ledger: cấu trúc cắt nhỏ/trộn thính và nắm/gói là TEXT_SUPPORTED_IN_REPORTED_METHODS, không một công thức duy nhất. Màu, độ phủ, độ ẩm, kích cỡ và texture phần gắp vẫn VISUAL_UNVERIFIED: đã đọc text/caption, chưa xem trực tiếp ảnh món. Chưa food board hoàn tất. Không thêm ingredient/process claim vào thoại/caption từ mô tả hình này.

R4/S5 là RESEARCH_ONLY / UPLOAD_NOT_AUTHORIZED; ghi nguồn không tự cấp quyền ảnh. Không tải ảnh, không upload báo hoặc demo. Tiếp theo cần xem ảnh món có provenance; nếu muốn đưa vào Flow phải kiểm quyền riêng. Chưa bắt owner cung cấp ảnh vì còn đường desk research.

## 2. Official Flow docs và UI preflight

[Image help](https://support.google.com/flow/answer/16729550) mô tả tạo ảnh từ text với model/tỷ lệ/count và reference tùy chọn. [Get started](https://support.google.com/flow/answer/16353333) yêu cầu kiểm giá hiện hành trong settings; ghi SynthID và watermark hiển thị tự động tại Việt Nam. Giữ watermark, không crop/bỏ; nhãn AI của dự án vẫn cần. Docs feature đã mở được một phần, lần tái mở timeout; không lấy phần chưa đọc để hứa tiếng/video.

UI read-only bằng computer-use: mở một project hiện có, settings/menu/screenshot rồi quay lại ô tác nhân; không tạo project, nhập prompt, đổi/save settings, upload hoặc Generate. Không lưu identity/account/project ID vào Git.

Screenshot xác nhận default image Nano Banana 2 Lite, 16:9, x2; default video Omni 1.1 Flash, 16:9, x1. Luôn luôn xác nhận trước tạo vẫn bật. Menu có Nano Banana Pro/2/2 Lite. Đây là default project mở, không selected settings cho EP01. Menu không cho thấy chi phí request/balance; CHƯA QUAN SÁT GIÁ, không suy từ gói3000 credit hoặc tên model.

## 3. Request xin duyệt EP01-P6-CHAR-BASE-v0.1

- Tạo project riêng tên EP01_P6_Khoai_Dao_Pilot; không sửa project cũ.
- Hai request text-only: Khoai một output và Đào một output, x1 mỗi lượt, 9:16. Không món/set/pair/sheet/voice/video ở lượt này; chúng vẫn nằm trong các bước QC/mẫu sau.
- Model đề xuất Nano Banana Pro trên Flow, để thử chứ chưa chứng minh tốt hơn model khác. Dừng nếu không khả dụng/tự chuyển model, không thay ngầm.
- Giữ Luôn luôn xác nhận. Chọn per-request nếu có; nếu cần save default thì chỉ project pilot được duyệt. Không đổi setting tài khoản/bảo vệ.
- Cap đề xuất tối đa 40 credit tổng, KHÔNG phải giá dự báo. Đọc giá actual trước xác nhận mỗi lượt; không nhìn được giá hoặc vượt phần cap còn lại thì dừng hỏi. Không mua/upgrade.
- Không retry tự động kể cả failed/refunded. Dừng sau tối đa hai request và trình output/QC. Không dùng cap dư để sinh thêm.
- Không upload ảnh báo/demo/giọng người thật. Chỉ gửi prompt text bên dưới. Cho tải output về folder media dự án, không publish/share hoặc commit media.

## 4. Prompt exact đề nghị

### R-K01 — Khoai

Create one original full-body 3D character design image of Anh Khoai Tay, an anthropomorphic potato who behaves like a mature adult friend, calm, thoughtful, quietly witty and approachable. His elongated slightly asymmetric golden-brown potato form is his actual character body and head, not a human wearing a potato mask. Subtle clean potato skin texture and small natural marks, soft tactile materials, expressive medium-sized brown eyes, defined eyebrows, a restrained slight smile. No hair or beard. Balanced adult body language, relaxed upright posture, both hands visible and empty. Wear an open-collar cream shirt with sleeves neatly rolled below the elbows, charcoal trousers and simple brown shoes. A single character in a three-quarter front view, entire body and feet visible with clear space around the silhouette. Warm neutral studio lighting and a plain light neutral background. Charming cinematic 3D stylization without baby proportions, oversized eyes, glossy plastic or plush-toy fur. No food, scene, companion, professional props, flowers, logos, captions or lettering. Do not imitate an existing branded character or a real person. Portrait composition, 9:16. Do not add decorative text; preserve any platform-applied watermark.

### R-D01 — Đào

Create one original full-body 3D character design image of Chi Dao, an anthropomorphic peach who behaves like an independent adult friend, curious, open-minded, lively and subtly playful. Her soft pink-orange peach form is her actual character body and head, not a human wearing a fruit mask. A subtle peach seam, a small stem and a modest green leaf make her recognizably a peach rather than an apple. Very fine restrained peach fuzz, soft tactile materials, medium-sized expressive brown eyes, restrained eyelashes and a knowing gentle smile. Balanced adult body language and relaxed upright posture, both hands visible and empty. Wear an ivory top, a light sage-green jacket, light-brown trousers and simple shoes. A single character in a three-quarter front view, entire body and feet visible with clear space around the silhouette. Warm neutral studio lighting and a plain light neutral background, visually compatible with the Anh Khoai Tay design brief. Charming cinematic 3D stylization without baby proportions, oversized eyes, heavy makeup, exaggerated body curves or plush-toy fur. No apron, flowers, food, scene, companion, couple pose, logos, captions or lettering. Do not imitate an existing branded character or a real person. Portrait composition, 9:16. Do not add decorative text; preserve any platform-applied watermark.

Hai prompt độc lập từ text không bảo đảm compatibility/identity; kiểm bằng output. Base 3/4 không chứng minh multi-view consistency. Không hứa resolution từ tỷ lệ9:16. Prompt/spec không tự cấp generation permission.

## 5. QC/log và điểm dừng

Hiện mọi kiểm media đều NOT_RUN: đúng silhouette khoai/đào (không táo), khí chất trưởng thành, outfit, texture/mặt, tay/ngón/chân, crop, chữ thừa, watermark và style giữa hai base. Originality/rights không tự PASS vì prompt nói original. Owner cần chọn từng asset/version trước sheet/pair/motion.

Log cần request ID/version, prompt/settings observed, output ID/file, dimensions/format actual, credit actual hoặc bằng chứng số dư với giới hạn attribution, lỗi/disposition/QC và approval. Destination dự kiến media/raw/ep01_p6_character_base/; chưa tạo folder/output. Media ignored Git; metadata được commit/push.

## 6. Tổng hợp và owner gate

- Đã chốt: hướng Q0/V1A/V2A/V3A, không thay script.
- Đã kiểm: text nguồn mô tả món, official image docs, default UI và bảo vệ trước tạo.
- Giả định: model Pro và cap40 là đề xuất thử; không dự báo chất lượng/giá.
- Còn mở: visual food/rights, actual giá, output nhân vật, giọng và runtime PROD7 review riêng.
- Next: owner duyệt request v0.1 và lệnh chạy hai ảnh theo cap40. Preflight actual giá/model/count phải đạt mới Generate; voice/food/video cần request sau. Duyệt hướng trước không được xem là duyệt chạy request này.
