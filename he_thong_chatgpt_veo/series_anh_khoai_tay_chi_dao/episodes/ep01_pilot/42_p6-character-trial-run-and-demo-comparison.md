# EP01 — P6 character trials / demo comparison

Ngày: 2026-09-30. Status: FOUR_BASE_TRIALS_GENERATED_AND_SAVED / ROOT_VISUAL_QC_RECORDED / OWNER_ASSET_APPROVAL_PENDING.

## Authority và actual run

Tiếp nối request40 và authority41; owner yêu cầu “làm đi”, sau đó nhắc “nhớ tham khảo ảnh mẫu nhé”. Scope vẫn thử nhân vật P6 tối đa tổng200 credit, không video/publish. Project riêng: EP01_P6_Khoai_Dao_Pilot, trên in-app browser. Owner đăng nhập trực tiếp. Không ghi account identity, credentials, signed media URL hoặc telemetry vào Git.

R-K01 và R-D01 đã chạy đúng prompt text của request40: Image / Nano Banana Pro / 9:16 / x1 mỗi request. Hai output: Potato character design portrait; Peach character 3D design. Không upload demo hoặc ảnh báo, không giọng, món, pair hay video. UI trước Generate hiển thị giá0 credit; số dư trước và sau hai lượt đều1.050. Đây là quan sát phiên này, không tuyên bố mọi ảnh Pro luôn miễn phí hoặc billing itemized đã audit.

## Local outputs và export limits

Lưu ảnh đang hiển thị bằng browser media download, sau đó copy vào media/raw/ep01_p6_character_base/ (ignored Git):

| File | Actual size | Bytes | SHA256 |
|---|---|---|---|
| EP01_P6_KHOAI_BASE_v0.1.jpg | 768×1376 | 86998 | 1E0871003ECEB6ECBFABFCBD09F3EC8AE79437FBA956C4620330101C16035C58 |
| EP01_P6_DAO_BASE_v0.1.jpg | 768×1376 | 94248 | EC947A88EF59B15AFD94A9D60BE84269C82E76E441E351785D5C24A757BF5EEF |

Menu tải1K không trả download event; asset bundling cũng thất bại fetch. Đường lưu media hiển thị thành công. Không gọi các file này là verified native1K export. Tỷ lệ actual768/1376 không chính xác9/16; cần xử lý khung khi lên shot, giữ watermark. Không upscale/crop/chỉnh ảnh.

## Reference intake và QC root thực hiện

Đã xem trực tiếp demo f3035b95-3deb-4752-b473-9de3b563084a.jpg tại Downloads, và cả hai local output. Demo là tham chiếu nét mặt/material/độ duyên, không canon cặp đôi, nghề, trang phục hoặc props. Không upload demo; owner nhắc tham khảo không được dùng để suy mọi chi tiết đã approved.

- V01 có silhouette khoai/đào nhận diện được, toàn thân/chân nhìn rõ, outfit theo brief, nền sạch, không chữ/logo thừa; watermark còn nguyên. Phong cách/material tương đối tương thích. Chưa test tay cầm đũa, chuyển động, multi-view, identity hay originality/rights.
- Khoai v01: nụ cười/mắt khá hiền và đối xứng, chưa thể hiện rõ sự chín chắn, kén chọn và hài kín đáo. Texture khoai tốt; không cần đổi outfit hoặc nghề để sửa nét mặt.
- Đào v01: nhận diện quả đào tốt, nhưng đầu lớn và biểu cảm khá chung, dễ đọc thành búp bê. Cần ánh mắt chủ động, chân mày/nụ cười có ý, không làm vẻ trẻ con thành trẻ em.
- Nhận định độ duyên là phán đoán creative của root, không điểm số khán giả, không independent agent PASS, không owner rejection.

## V02 — lý do và prompt exact trước chạy

Thử text-only hai base mới để kiểm riêng face/attitude. Không dùng v01 làm final reference; không đổi script/canon, không thêm đồ ăn, props, set hoặc pose đôi. Giữ Pro/9:16/x1, kiểm giá trước mỗi Generate. Tối đa một variant mỗi nhân vật ở vòng này rồi so sánh, không tự lặp vô hạn vì giá0.

### R-K02

Create one original full-body cinematic 3D character design of Anh Khoai Tay, an adult anthropomorphic potato friend. Give him a broad, slightly irregular golden-brown potato silhouette with gently asymmetric contours and richly tactile natural potato skin, small clean speckles, subtle sculpted cheeks and warm shading. He is mature, composed, discerning and quietly funny, not stern or unfriendly. Design a memorable face with expressive warm brown eyes, strong thick dark eyebrows, slightly lowered relaxed upper eyelids, one eyebrow subtly raised, and a small asymmetric closed-mouth smile that suggests he has noticed something amusing but will not say it yet. His gaze is attentive rather than blank or startled. Keep an appealing adult animated-feature sensibility, not a baby, toy doll, plush toy or glossy plastic figurine. No hair or beard. The potato form is his actual head and upper body, not a mask on a human. Relaxed three-quarter standing pose with natural weight on one leg, shoulders at ease, both hands visible, empty and anatomically coherent. Wear an open-collar cream shirt with neatly rolled sleeves, charcoal trousers and simple brown leather shoes. One character only, full body and feet visible, clear silhouette margins, plain warm ivory studio background. Soft warm directional key light, gentle fill, subtle rim light, detailed fabric and fruit materials. No companion, romantic pose, blazer, apron, flowers, rolled plans, food, professional props, logos, captions or decorative lettering. Do not imitate a branded character or real person. Portrait 9:16. Preserve any platform watermark.

### R-D02

Create one original full-body cinematic 3D character design of Chi Dao, an independent adult anthropomorphic peach friend. Her rounded pink-orange peach head has a gentle natural seam, small woody stem, one green leaf, delicate restrained peach fuzz and warm coral blush. Make a memorable lively face: expressive warm brown almond-shaped eyes with beautifully sculpted upper eyelids, restrained natural eyelashes, expressive curved eyebrows, subtly lifted cheek and an asymmetric knowing closed-mouth smile. Her gaze shows curiosity and quick understanding, as if she has just caught a friend being playfully evasive. Warm, approachable and mischievous, not smug, passive or childish. Balance cute animated-feature charm with clearly adult bearing; reduce the oversized bobblehead impression, avoid infant cheeks, toddler proportions, toy-doll simplicity, heavy makeup, exaggerated body curves or glossy plastic. The peach is her actual character head, not a mask. Relaxed three-quarter standing pose with a slight natural head tilt, confident easy posture, both hands empty and visible. Wear an ivory top, light sage-green casual jacket, light-brown trousers and simple brown shoes. One character only, full body and feet visible with silhouette margins, plain warm ivory studio background. Soft warm directional key light, gentle fill and subtle rim light, detailed fabric and fruit materials, visually compatible with an adult potato character. No companion, couple pose, apron, flowers, food, professional props, logos, captions or decorative lettering. Do not imitate a branded character or real person. Portrait 9:16. Preserve any platform watermark.

## Stage / next gate

P6 đang thử tạo hình, chưa approved asset; P5 nội dung không đổi. Còn mở: owner chọn base sau comparison, hands/multi-view/pair/motion, voice và food visual reference. Sau chọn base mới được xây sheets/shot reference theo gate, không tự chuyển production video.

## V02 — kết quả actual

R-K02 và R-D02 đã chạy đúng hai prompt exact ở trên, cùng Pro / image / 9:16 / x1. Trước mỗi request đã kiểm settings với giá0credit. Cả hai hoàn tất, lưu media hiển thị như v01, không verified native1K export. Tổng4 requests thành công, không generation failed/retry, không reference upload. Sau4lượt số dư vẫn1.050credit, giảm quan sát0; chưa audit billing itemized. 200credit authority chưa bị tiêu theo quan sát này; không tự tăng scope vì ảnh đang giá0.

| File trong media/raw/ep01_p6_character_base/ | Actual size | Bytes | SHA256 |
|---|---|---|---|
| EP01_P6_KHOAI_BASE_v0.2.jpg | 768×1376 | 92881 | FDE0B47D3D0BE5C73F37A255F75152B32BFDB320C23321E8F1CAE24F89A9C6A3 |
| EP01_P6_DAO_BASE_v0.2.jpg | 768×1376 | 102013 | A4207CBDD64450207906F5466D5E3CD857928B9FD645EF903973C7A7A29F37F4 |

Đã xem local image v02, không chỉ thumbnail. Khoai v02 có silhouette chắc hơn, texture/eyebrow/nụ cười gần chất demo hơn v01; nhưng mắt còn tròn và mở rộng, chưa đạt yêu cầu upper eyelid relaxed rõ ràng. Đào v02 có dáng trưởng thành, mắt/mày/miệng có ý hơn; mắt híp cùng cười lệch có thể đọc thành hơi đắc ý, chưa hẳn sự cởi mở dễ gần. Jacket v02 chuyển thành casual zip khác v01: design variant chưa canon lock, cần chọn rồi khóa outfit chi tiết. Đây là root creative judgment, không khảo sát hay independent media review.

Disposition: giữ cả4mẫu, trình v02 như hướng đáng cân nhắc, KHÔNG AUTO_APPROVE. Owner có thể chọn từng nhân vật khác version hoặc yêu cầu chỉnh tiếp. Nếu chọn v02, nên làm expression-neutral/curious/skeptical/embarrassed samples sau để tránh dùng biểu cảm knowing-smile như trạng thái mọi cảnh. Các gate tay/ngón khi cầm đũa, pair compatibility, multi-view, motion/voice vẫn NOT_RUN.
