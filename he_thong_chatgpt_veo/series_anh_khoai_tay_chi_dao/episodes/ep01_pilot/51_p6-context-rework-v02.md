# P6 — Context rework v0.2

Ngày 2026-09-30. Owner: “làm lại đi, cho đến khi thật sự ok được, trường hợp nếu cần tách ra thành các thành phần thì nên tách”. Status: THREE_CANDIDATES_READY_FOR_OWNER_REVIEW, chưa owner-approved. Giữ cap 200 credit đã cho phép; không chạy video. Mỗi request đọc UI price, tải/xem/QC trước request tiếp theo. Không dùng ảnh fail50 làm identity reference.

## Thiết kế thử nghiệm

1. Tách biến: chỉ thay background từ approved duo v0.3; giữ nguyên pose/outfit/identity/spacing. Nếu identity chưa giữ được, tách nhân vật và nền; QC mỗi thành phần rồi thử composition.
2. Khi baseline đạt root QC, thử bối cảnh khác, luôn quay về approved duo thay vì tích lũy drift qua ảnh mới.
3. Không coi mood-frame đứng nguyên là storyboard diễn xuất. Pose ngồi/tương tác là phép thử riêng, không được waive lỗi để chuyển video.

Primary `Two characters standing in studio` = media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg, SHA256 ECFBE7A3C543730C268A77CA08D508147115CA804154F85EBDBB38C5C601E8C7. Flow Image / Nano Banana Pro / 9:16 / x1.

## R01 — chỉ đổi nền phố

UI price trước submit: 0 credit. Exact prompt:

Edit the attached image. Replace ONLY the plain studio background with a quiet Vietnamese neighborhood lane in soft daylight, rendered in the same warm tactile stylized 3D animation style as the characters. Keep BOTH existing characters exactly as they are: identical faces, fruit-shaped heads, eyes, brows, peach seam, stem and leaf, body proportions, clothing, waist bow, shoes, standing poses, spacing and relative size. Do not redesign, humanize, add hair, change expressions or change their clothing. Keep the characters large and fully visible in the same framing. Add believable ground contact shadows. Background has simple plaster facades, shutters and potted plants, no text, logos, food or extra people. Single portrait image. Preserve platform watermark.

Result: Flow asset d0ca59fa-b606-40ca-9dad-b18b8800f96f; local media/raw/ep01_p6_contexts/R01_street_v0.2.jpg. Root visual QC: giữ sát mặt, mắt/lông mày, silhouette đầu quả, cuống/lá, outfit và tỷ lệ duo; không còn humanization. Chấp nhận làm baseline đổi nền để owner xem, không phải đi dạo/diễn xuất, không claim pixel-identical.

## R02 — thử ngồi quán, reset nguồn primary

UI price trước submit: 0 credit. Không dùng R01 hay fail50 làm reference. Exact prompt:

Use the attached image as the exact character design. These are anthropomorphic VEGETABLE AND FRUIT characters, NOT human people. Keep their original faces and head-to-body proportions: the left character has the same tall golden potato body/head with thick dark brows; the right character has the same large pink-orange PEACH head with seam, woody stem and green leaf, NO hair. Keep their exact original clothes: potato navy overshirt with chest pocket and rolled sleeves, cream shirt, charcoal trousers; peach ivory collared puff-sleeve blouse, sage A-line skirt, pink bow AT HER WAIST, brown boots. Change their poses to sit on separate stools on opposite sides of a small plain empty table at a quiet Vietnamese sidewalk eating spot at dusk. Potato left, peach right, both facing three-quarter toward camera with a slight friendly glance toward one another. Their empty hands rest on their own laps. Keep faces large and clear; include boots and stools. Warm practical light, stylized 3D animated-film environment matching the characters, NOT a photograph. Adult friends, no touching or romantic pose. No food, cups, text, logos or extra people. Single portrait composition; preserve platform watermark.

Result: Flow asset b55b303c-edb9-4ee4-9376-83e9bb885763, saved media/raw/ep01_p6_contexts/R02_sidewalk_v0.2.jpg trước editor edit. Root QC: không humanization, head/body và outfit giữ khá sát trong seated view; nơ đúng eo, có cuống/lá, hands trên đùi. FAIL_BACKGROUND_TEXT: có biển chữ phía trên trái và poster trái dù prompt cấm text. Không owner-approved.

## R03 — sửa riêng nền của R02

Editor target R02, không thay primary. UI price 0 credit. Exact prompt:

Change ONLY the background signage: replace every signboard, lettering and wall poster, especially in the upper-left corner and left wall, with blank unmarked surfaces matching the existing wall and awning. Keep the two fruit characters, their faces, proportions, clothes, seated poses, hands, table, stools, lighting, framing and all other details unchanged. Do not add text, logos or food. Preserve platform watermark.

Result: cùng Flow asset b55b303c-edb9-4ee4-9376-83e9bb885763, local media/raw/ep01_p6_contexts/R03_sidewalk_v0.3.jpg. Root QC: biển và poster đã sạch chữ, identity/outfit/seated pose giữ sát R02, không thấy lỗi rõ cần sửa tiếp trong mood-frame này. READY_FOR_OWNER_REVIEW, không owner-approved, không kiểm chứng motion. Khung hình có khoảng nền phía trên; chưa coi là camera lock cho episode.

## R04 — nền bếp, reset nguồn primary

UI price 0 credit. Exact prompt:

Edit the attached approved duo image. Replace ONLY the studio background with a modest warm Vietnamese home kitchen: cream walls, simple tiled backsplash, wooden cabinets, a small wooden dining table behind the characters, potted herbs by a daylight window. Render the environment in the same tactile stylized 3D animated-film style, not a real photograph. Preserve BOTH existing characters exactly: original faces, eyes, brows, fruit-shaped head silhouettes and sizes, peach seam, stem and leaf, body proportions, clothing, waist bow, shoes, standing poses, spacing and relative size. Do not redesign or humanize either character. No human hair. Keep both characters large, fully visible and separate as adult friends, not a couple. Soft window daylight, coherent ground contact shadows. No food, text, packaging, logos, extra people or romantic props. Single portrait image; preserve platform watermark.

Result: Flow asset 6fb3a942-0b86-4df6-97b5-5d9b44841960; media/raw/ep01_p6_contexts/R04_kitchen_v0.2.jpg. Root QC: giữ sát bộ đôi gốc ở mặt/head/body/outfit; có cuống/lá, nơ eo, bàn chân đủ khung, không hair/humanization/signage; ánh sáng ấm hòa với nền. READY_FOR_OWNER_REVIEW. Là thử bối cảnh đứng, không phải cảnh nấu ăn hay tương tác đã duyệt.

## Manifest / closeout của vòng này

Tất cả 4 ảnh preview tải được 768×1376, không tự nhận native 1K hay chính xác 9:16. Chưa crop/upscale. UI chọn 9:16 không chứng minh kích thước xuất chuẩn bàn giao cuối.

| Raw file trong media/raw/ep01_p6_contexts | Bytes | SHA256 |
|---|---:|---|
| R01_street_v0.2.jpg | 160746 | EA774CC0F577D36167981306BEFBA811042BD36048E4186BFE6240CF017DD05F |
| R02_sidewalk_v0.2.jpg — superseded signage error | 132857 | 68CA28A444A6AA6C8B7A4A2746D1DBF1DE8FC1A62EB8D32C7DA8545027FEC835 |
| R03_sidewalk_v0.3.jpg | 136144 | DBB12B51A2A4E73E29560854E6B45EACF523CFAD28729A3517D3B0531850127A |
| R04_kitchen_v0.2.jpg | 138625 | BA8C65EF038307ABDEC63B20EC946840C1F0605FF6C1A5E44BF17D3AEAE52967 |

Proof screenshot R04_flow-review-proof.jpg, 559×646, SHA256 554A4D3D0BC526EDD548CBDF2294B4A425BB65CA1A7FA13FA4AEDC8A9519B506. Media lưu local/gitignored; chỉ manifest/prompt/QC push Git.

Đã xác định: background-only giữ identity sát hơn output50; một seated prompt sửa ràng buộc identity không còn humanization và signage có thể sửa riêng mà giữ nhân vật ở mức visual QC. Chưa có controlled benchmark hoặc kết luận tuyệt đối về prompt/provider.

Quyết định thực thi: reset nguồn gốc cho từng scene; tải/QC trước request kế; sửa riêng lỗi nền R02. Giả định: ba bối cảnh là mood exploration generic, không địa điểm/canonical scene. Chưa cần tách nhân vật riêng vì các kết quả R01/R03/R04 đủ sát để trình review; không tuyên bố đã tạo layered/cutout components.

Vấn đề mở: owner đánh giá độ sát mặt và hợp thế giới series; độ tự nhiên của tương tác/ngữ cảnh, camera/lighting lock theo shot thật; food visual, motion, xuất đúng chuẩn và các vấn đề P6 khác vẫn riêng. Bước kế: owner review R01/R03/R04; chỉ tách character/background riêng nếu còn drift cụ thể hoặc chuyển sang pose/shot khó. Không tự approve P6 hoặc chuyển video.
