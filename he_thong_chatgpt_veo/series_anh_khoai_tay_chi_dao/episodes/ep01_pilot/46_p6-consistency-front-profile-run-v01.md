# EP01 — P6 consistency front/profile v0.1

Ngày: 2026-09-30. Status: FIVE_OUTPUTS_SAVED / ROOT_QC / EXACT_PROFILE_NOT_PASSED / OWNER_GEOMETRY_REVIEW_PENDING.

Owner nói “ok chạy đi” sau approval45 và next consistency/expression/hands. Vòng đầu4ảnh chẩn đoán: front và profile riêng mỗi nhân vật. Không nhảy sang expression/props nếu identity/outfit còn lệch cần xử lý. Không video/mua credit/publish; total cap200credit theo41, cumulative spend kiểm actual. Không hiểu200là mỗi turn. Số dư cuối vòng44 là1.050 và giá UI0; phải kiểm lại actual cho lượt mới.

Reference chính duy nhất: asset Flow Two characters standing in studio, local EP01_P6_PAIR_CONCEPT_v0.3.jpg, SHA256 ECFBE7A3C543730C268A77CA08D508147115CA804154F85EBDBB38C5C601E8C7. Chọn asset có sẵn trong project, không upload file khác. Demo gốc và base riêng không trộn vào request này.

## Prompt exact — cách ghép

Mỗi prompt = COMMON + một dấu cách + CHARACTER + một dấu cách + VIEW + một dấu cách + END. Không gửi ID/nhãn Markdown. Các chuỗi dưới đây là toàn bộ text thực, không paraphrase ngầm.

COMMON:

Use the attached approved duo portrait as the ONLY identity, proportions, outfit and material reference. Generate a diagnostic single-character turnaround image, not a new design. Preserve the selected character exactly as seen in that reference; change only the viewing angle. Match the reference facial construction, fruit silhouette, color, mature adult charm, fabric texture and clothing details. Do not blend in any earlier design or invent accessories.

KHOAI:

Show ONLY Anh Khoai Tay, the male golden potato on the left of the reference. Preserve his elongated irregular potato shape, dark thick brows, warm brown eyes and restrained friendly smile. Preserve the cream collared open-neck button shirt, dark navy casual overshirt with chest pocket and rolled sleeves, charcoal trousers, brown belt with buckle and brown leather lace-up shoes. Both empty hands and feet visible. Remove the peach character.

DAO:

Show ONLY Chi Dao, the female pink-orange peach on the right of the reference. Preserve her peach seam, woody stem, green leaf, warm brown almond-shaped eyes, graceful lashes, curved eyebrows and welcoming gentle smile. Preserve her ivory collared button-front blouse with softly puffed elbow-length sleeves, sage-olive A-line midi skirt, dusty-rose waist bow and brown lace-up ankle boots. Do not replace the blouse with a round-neck top, an apron or trousers. Both empty hands and feet visible. Remove the potato character.

FRONT:

Exact straight-on front view: camera at the character's eye level, face and body facing directly toward the camera, shoulders and hips square, no three-quarter rotation, head upright. Relaxed symmetrical stance, arms slightly away from the body. Keep the reference expression subtle and natural.

PROFILE:

Exact ninety-degree side profile facing screen right: camera at the character's eye level, head, torso and feet all turned together into true side view. Do not turn the face back to the camera or show a three-quarter view. Preserve the same character's facial depth and fruit volume, not a generic human profile. Arms relaxed, empty hands readable.

END:

One full-body character centered, generous clear margin on every side, full shoes and leaf or head visible. Plain warm ivory studio background, soft neutral-warm lighting consistent with the reference. No food, props, companion, text or logos. Portrait 9:16. Preserve platform watermark.

| Request | CHARACTER | VIEW |
|---|---|---|
| C-K-F01 | KHOAI | FRONT |
| C-K-P01 | KHOAI | PROFILE |
| C-D-F01 | DAO | FRONT |
| C-D-P01 | DAO | PROFILE |

## Run controls / QC

Flow image / Nano Banana Pro /9:16 /x1 mỗi request; reference chip xác nhận trước Generate, giá phải đọc được trong cap. Tải actual image hiển thị vào media/raw/ep01_p6_consistency/ với file versioned; metadata/dimensions/hash ghi sau. Không gọi preview export là native1K. Nếu failed, ghi lỗi/credit và chỉ retry có lý do; không lặp không giới hạn. Vòng này chưa đo consistency bằng pixel hay audience score.

QC: đúng front/profile, identity/material so primary, outfit (đặc biệt cổ/nút/nơ/váy), leaf/head volume, adult proportions, hands/feet/clear margin và watermark. Góc mới làm lộ phần chưa thấy ở primary là GENERATED_INFERENCE, không owner-established geometry. Media review root không giả independent auditor PASS. Owner approval primary không tự duyệt mọi angle output.

Next sau QC: xử lý drift nghiêm trọng trước, rồi expression/hands. Food/voice/motion vẫn pending; P6 chưa complete.

## Actual run / root QC

C-K-F01, C-K-P01, C-D-F01, C-D-P01 đều thành công, đúng prompt ghép trên; mỗi lượt Pro/image/9:16/x1, UI giá0credit và selected approved duo reference. Không upload reference mới. Browser media download, copy versioned và xem trực tiếp4local ảnh. Preview export actual768×1376, giữ watermark, không native1K verified.

| File tại media/raw/ep01_p6_consistency/ | Bytes | SHA256 | Disposition |
|---|---:|---|---|
| C-K-F01_v0.1.jpg | 75356 | EB39AECA3F00DA60212CDA96737342AD53CDE3323E7E0059B488B02B7DC0D7D6 | Front đúng; outfit/mặt gần primary, root provisional usable for diagnostics |
| C-K-P01_v0.1.jpg | 70546 | CFE2996A8A018CC2AB52D813A3D9090663A2E1F1AB0686A2DF0420A114123515 | FAIL requested direction: quay trái thay phải; giữ file, không flip ảnh để che lỗi |
| C-D-F01_v0.1.jpg | 76750 | 3D14115B1F7BE7C5F8D95674E2299B269E918F6676345AD9C466DB2289D2C0AB | Front đúng, collar/buttons/skirt/bow/boots giữ được ở mức quan sát |
| C-D-P01_v0.1.jpg | 62066 | 5AA538D8B8A860D4B3957CFD41D48FCF9821403B6AA7A2F976B35F09E5EB0212 | Side đúng hướng, hình khối ngang/độ nhô mặt/lá là generated inference cần owner review |

Cả4full body/feet và margin nhìn thấy được, không companion/text/food/props, giữ watermark. Khoai front mí/mày đối xứng hơn pair; không identical face landmarks, texture variation còn. Đào side head volume rộng, phần seam/back/leaf orientation không thể chứng minh từ primary front. Không đo pixel similarity, không độc lập auditor, không owner-approved four-angle sheet. Không dùng góc mới để ghi đè primary.

## C-K-P02 targeted rework — prompt exact

COMMON + KHOAI + VIEW_KP02 + END, ghép một dấu cách như trên. Reference vẫn primary duo, không dùng output quay sai làm identity source. Chỉ sửa hướng/góc, không redesign.

VIEW_KP02:

Exact ninety-degree side profile facing SCREEN RIGHT. The character's nose, mouth and both shoe toes must point toward the RIGHT EDGE of the image. The back of his head and back of his jacket must face the LEFT EDGE. Only the right-facing profile is visible; do not face left and do not turn toward the camera. Head, chest, hips and feet all rotate together into the same true side view. Preserve the approved fruit volume and relaxed adult posture, with arms hanging naturally and empty hands readable.

Chạy tối đa1rework ở vòng này, preflight giá lại; nếu vẫn sai ghi fail, không tự lặp để đủPASS.

### C-K-P02 actual

Generate thành công, reference primary duo, Pro/image/9:16/x1, UI0credit. Asset edit/2f6983e7-97c2-47c8-9650-0ba65608d03b. File media/raw/ep01_p6_consistency/C-K-P02_v0.1.jpg đã tải và xem trực tiếp. Đúng hướng SCREEN RIGHT; tuy nhiên thấy phần ngực áo và mày xa, còn góc chếch, chưa đạt exact90°. Disposition: DIRECTION_FIXED / EXACT_PROFILE_FAIL. Không retry thêm vòng này; không gọi profile sheet PASS. Không biến output này thành canonical geometry.

Export actual768×1376, 70.107bytes, SHA256 BE73C2BB44729DF82A2D9F865C9F9A54376DD3159CEFB5C52280DF736A34AD02; không native1K verified.

Có thể thử expression độc lập từ PRIMARY DUO để kiểm thêm khả năng giữ mặt; đây không phải promotion của angle outputs. Identity/outfit drift nghiêm trọng chưa quan sát thấy ở front; góc nghiêng vẫn unresolved. Food/voice/motion và grip động chưa kiểm.
