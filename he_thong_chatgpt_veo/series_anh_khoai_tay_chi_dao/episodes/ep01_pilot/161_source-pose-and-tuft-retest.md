# EP01 — sửa nguồn pose và phần nem, thử lại theo nhóm biến

## Quyền thử và scope

Owner trả lời “ok” với kết quả/hướng sửa 160. Trial đầu lượt còn **184 credit**, số dư Flow lần kiểm trước 484. Quality riêng chưa dùng. Không đổi lời thoại/story hoặc duyệt tập hoàn chỉnh; C01 vẫn được chấp nhận riêng cơ học gắp.

## Chuỗi sửa có truy vết

1. Từ END_hold_v0.1 của 158, đổi riêng đầu/gaze Đào quay rõ sang cốc screen right; giữ tay, Khoai và bàn.
2. Sau kiểm ảnh, đổi riêng phần nem đang cầm: nhỏ/sợi ngắn tương ứng C01, không dây dài chạm bát.
3. Từ START đó dựng END nâng tay dừng bên cằm, môi đóng, không tiếp xúc. Kiểm cả inventory, diễn và continuity.
4. X3 Lite với cùng cấu trúc prompt 160, chỉ thay mô tả hướng nhìn cho đúng nguồn. Nếu đổi cả pose và tuft trước video thì chỉ là thử sửa nhóm nguồn, không đủ xác nhận nguyên nhân riêng của từng biến.

Người điều phối kiểm actual, chưa gọi agent độc lập đã chạy. Dùng imagegen built-in để sửa ảnh, computer-use cho UI Flow; chưa ghép thoại hoặc chuyển Quality.

## Kết quả hiện tại

### Prompt pose thực tế

```text
Use case: identity-preserve. Image 1 is the exact edit target. Change ONLY the adult peach woman's head orientation and eye direction: she turns her head clearly toward SCREEN RIGHT and looks down at her existing water glass beside her own right side, away from the potato man seated on screen left. Show a believable three-quarter side/profile view with her nose facing the glass; do not leave a front-facing face with just shifted pupils. Preserve the same peach facial identity, eyelashes, stem and leaf, adult proportions, gentle expression, outfit, body and BOTH hands in their exact original positions. Keep potato man, his face, grip, chopsticks, held nem, left hand completely unchanged. Keep camera, crop, lighting, street background, TWO bowls, TWO dipping saucers, leaf plate, nem plate/mound, spare chopsticks and water glass exactly unchanged. No missing/extra props, no steam/text/diagram. One portrait still.
```

Đã gửi x3 Veo 3.1 - Lite Frames, 9:16, 720p/8s. Giá hiển thị 30 credit, proof `C:/Users/PC/Downloads/du_an_nem_bui/161_source_retest/preflight.png`. Giữ cấu trúc video prompt 160, chỉ đổi câu Dao sang head turned screen right cho khớp nguồn; vì sửa nhiều nhóm ảnh không dùng so sánh này để chứng minh nguyên nhân từng biến.

### Đối soát và QC sau chạy

Đủ ba thành công/tải native. Số dư actual **454** (`balance-after.png`), trước 484 => ròng **30 credit**, trial còn **154**; Quality riêng chưa dùng. Cả ba giải mã toàn bộ sạch, H264 720x1280/24fps/8s, AAC. Chưa nghe ambience, không voice/lip-sync PASS.

| Mã | Flow ID | Native filename trong Downloads | Hình / quyết định |
| --- | --- | --- | --- |
| R01 | 18a0c712-30bd-4c6d-be48-faa062d4111f | Man_eating_nem_at_street_20261002231147.mp4 | Đào giữ hướng cốc tốt hơn; tay vượt endpoint đến vùng mũi/mắt rồi hạ; phát sinh sợi dài. Loại |
| R02 | 4862c452-af3d-4ce7-86b6-bf502d30474b | Man_eating_nem_at_street_20261002231238.mp4 | Đào giữ hướng cốc; nem/đũa vượt vị trí dừng vào vùng môi-mũi, sợi dài tái xuất hiện. Loại |
| R03 | 0c0d0dd8-c519-4bf1-ac06-8952bb26bdae | Man_eating_nem_at_street_20261002231330.mp4 | Đào quay lại sớm, Khoai mở miệng/nâng-hạ-nâng thay vì giữ. Loại |

Bản lưu `R01.mp4/R02.mp4/R03.mp4`; grid mỗi 0,5s toàn clip; R02 kiểm thêm 6fps đoạn 1–3,5s (`R02-dense.png`). Không chứng nhận đã cắn ở tất cả mẫu từ ảnh; việc vượt endpoint/không giữ và không đủ rõ chưa tiếp xúc đã đủ fail. Đạo cụ chính vẫn còn trong khung kiểm nhưng không thay gate diễn. Không trình owner bản lỗi để duyệt ghép.

### Kết luận có giới hạn / bước tiếp

Đổi nguồn pose đi kèm hướng nhìn đầu ra tốt hơn ở R01/R02, chưa chứng minh quan hệ nhân quả riêng vì nhiều biến đổi. Chuẩn hóa tuft ngắn không ngăn model tái sinh sợi dài; sửa nhóm nguồn **chưa đủ** giải quyết quỹ đạo đưa nem lên. Không tuyên bố lỗi do một keyword, hoặc END đúng thì video đúng. Scene/mound có drift từ bước ảnh, chưa qua continuity với C01/canon.

Tiếp theo ưu tiên probe dựng cắt: insert C01 → pose đang giữ nem dưới môi → Đào quay lại, Khoai khựng nhẹ. Thử chuyển gaze/phản ứng, giữ tay/miếng nem ổn định, không ép model diễn đủ đường lên miệng trong một clip. Đây là thử kỹ thuật phù hợp story trước chạm miệng, chưa duyệt phương án đạo diễn cuối. Nếu đạt thì kiểm riêng chuyển vào bát, ghép rough-cut toàn nhịp và owner nghiệm thu; nếu vẫn tự ăn thì kiểm pose hold-only trước. Không lấy phần sau một lần ăn rồi chuyển miếng đó sang Đào.

### Prompt video thực tế

```text
Locked tripod two-shot at the supplied street eatery. Match the supplied start and end frames. Khoai gently raises the same small tuft of cool nem from above his own bowl to the final-frame position beside his chin, then holds it there with his lips closed and a clear space between food and face. One small continuous arm movement only. Keep the same two wooden chopsticks, handle grip and pinched tuft throughout. Dao remains with her head turned screen right looking down toward her water glass with her hand resting at it; she does not look back yet. Keep their exact potato and peach faces, outfits, both personal bowls, plate of nem, leaves, two dipping saucers, spare chopsticks and glass unchanged. Preserve light, table layout and camera. The held tuft stays outside the face throughout. Silent performance, no speech or music, subtle street ambience only. Preserve native watermark.
```

POSE_away_v0.1: `C:/Users/PC/Downloads/du_an_nem_bui/161_source_retest/POSE_away_v0.1.png`. Đã xem actual, đầu/mũi Đào hướng screen right và nhìn xuống cốc rõ hơn nguồn 158; chưa profile hoàn toàn. Khoai/tay và inventory chính còn nguyên trong hình. Chấp nhận làm bước trung gian kỹ thuật, chưa duyệt canon.

START_short_tuft_v0.1: cùng folder 161. Held tuft ngắn hơn, không dây dài về bát; grip và pose Đào còn. **Sai lệch ngoài ý định:** texture/tỷ lệ thịt trên ụ nem cũng thay đổi nhẹ dù prompt chỉ định không sửa mound. Vì vậy không coi đây là thử kiểm soát chỉ đổi đúng một biến hay ảnh canon sản xuất; chấp nhận riêng đầu vào probe động tác, phải hồi quy món/continuity sau.

END_short_pause_v0.1: cùng folder 161. Đã xem: tay nâng, nem nhỏ phía dưới môi đóng; hướng Đào giữ. Có chồng hình nem trước vùng cằm nên không chứng nhận khoảng cách chiều sâu từ một ảnh; video phải loại nếu có tiếp xúc/ăn. Inventory hai bát/hai chấm/rau/cốc còn.

SHA256 POSE: `FF25765B2007263567BB512DEABC765DDE388B8CECB741C9FC73E60E54AE8F6E`.
SHA256 START: `E8A9AA146CB5CE0EE8596B0AE716951D6F68FEAA5FE3E5E007DA4615ABC0B4BD`.
SHA256 END: `A97A444D14B74572E36FCF6B1402F725FEF455B15659124FAE95F24EC735CD36`.

### Prompt END thực tế

```text
Use case: precise-object-edit. Supplied image is the EXACT START frame and edit target. Produce one END frame by moving ONLY Khoai's right forearm, hand, his same two wooden chopsticks and SAME small short nem tuft. Raise his hand gently so the tuft pauses beside his chin, BELOW the level of his CLOSED lips, with clearly visible air separation from ALL food and chopstick tips to his face. Keep same correct handle grip, continuous sticks and tuft pinched at narrow tips. Not touching lips/chin, not eating. Maintain EXACT expression, identity, left hand and clothes. Dao stays in EXACT turned head pose looking down screen right at the glass, hands/body/clothes unchanged. Do not change nem mound texture/quantity, plate, BOTH bowls, TWO dipping dishes, leaves, glass, spare chopsticks, wood, light, camera, crop, background. No long noodle strands, smoke/text/overlays. One portrait still.
```

### Prompt tuft thực tế

```text
Use case: precise-object-edit. Image 1 is the EXACT edit target; Image 2 is ONLY a reference for the small held nem tuft's size and short irregular texture, not a camera/scene/hand reference. Change ONLY the loose food held between Khoai's existing chopstick tips in Image 1. Replace that held food with a very small loose tuft of short irregular rice-powder-coated pork/pork-skin strips similar to the held tuft in Image 2. Remove the long dangling threads extending toward his bowl: every food strip stays close to the pinching tips, a clear air gap below, no noodle cords. Not a roll or dumpling. Preserve exact hand grip, chopsticks angle and geometry, potato face and outfit, BOTH hands, Dao's already turned head/gaze toward the glass, her identity/body/outfit, all table items, TWO bowls/TWO chấm/leaf plate/glass/spare sticks/mound, camera, lighting, background unchanged. Do NOT modify the entire food mound. No text/steam. Single portrait still.
```
