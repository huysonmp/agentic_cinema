# REC296 — Prompt ảnh tư thế nhận–cho

13-10-2026. Owner duyệt chuẩn bị hai ảnh nháp P1/P2. Built-in imagegen, không CLI/API, không Flow video. Prompt là yêu cầu bảo toàn, không bằng chứng giữ nguyên pixel hoặc chuyển động đạt. P2 sẽ edit từ P1 đủ phù hợp, không sinh độc lập từ END cũ.

## P1 v1 — Bát riêng rỗng gần A, chưa thả

Edit target: `02_refs/C06_ENTRY_LOCAL_v3_FOR_REVIEW_291.png`, SHA256 `7c8023cbe655745b941e1a47dd1df3614ba66fcef512a41c5c4c4048bb33f8cc`.

```text
Use case: identity-preserve.
Asset type: single vertical storyboard pose reference P1, not a collage.
Input image 1 is the EDIT TARGET and authority for faces, clothing, camera framing, table and background.
Primary request: edit only the receiving pose in this image. The adult peach woman on screen-right now lifts her existing EMPTY personal beige bowl with her INNER hand (the hand currently resting on the table near the middle of the image), bringing that same bowl leftward toward the small pinch of nem held by the potato man. Her bowl is held upright, opening clearly visible, just below and close to the held pinch so it clearly becomes the recipient. Arrange a physically natural short handover: keep her bowl distinct from his bowl and the serving plate, with visible air between the pinch and the empty bowl. The food has NOT been released.
Preserve the potato man's mature face, calm slightly caught expression and gaze toward her. He still holds the SAME small pinch in the SAME wooden chopstick tips on his own side, not a long extended offering pose. His inner hand remains resting on the table, separate from her bowl and visible. Both characters remain seated, same scale and position.
The peach woman's OUTER screen-right hand continues to hold exactly the same water glass, raised outside and well away from her bowl. No glass inside a bowl, no drinking, no switching hands. Her inner forearm naturally reaches to support her own bowl; no extra hand, fused fingers or impossible crossing.
Preserve both original faces and eye shapes, the peach stem and leaf, white blouse and green skirt with waist bow (NO bib or apron), his charcoal jacket and white shirt, warm street-eatery background, lanterns, camera and lighting. Preserve his empty personal bowl on the table, her resting chopsticks on screen-right, the front-left herbs, both dipping bowls and the shared nem plate. Her original bowl location becomes empty because she lifted that same bowl; do NOT create a third bowl. Keep the whole receiving interaction and both faces within the existing 9:16 framing.
Preserve cold nem texture: irregular thin skin ribbons and meat slivers with fine toasted-rice powder. Same small held pinch, no steam, no noodles, no large uniform chunks. No new words, captions, graphic labels or decorative marks. Retain the small existing source mark; do not invent a new watermark.
Make ONE image of the before-release state. Do not redesign, beautify or restyle the faces, table, background or costumes.
```

## P1 v2 — Sửa riêng mặt và hướng nhìn sau kiểm v1

Edit target: P1 v1 đã sinh; supporting identity reference: entry v3 REC291. V1 có bát rỗng đúng vai nhưng mắt Khoai chưa chú ý Đào và toàn khung được redraw. Chỉ dẫn sửa không là cam kết pixel lock.

```text
Use case: identity-preserve.
Input image 1 is the EDIT TARGET: P1 empty-bowl receiving pose. Input image 2 is the facial-identity and eye-direction authority from C06 v3, NOT a pose or framing target.
Primary request: correct ONLY the potato man's face and eyes in image 1 to closely match image 2: same mature potato facial shape, eyebrows, eyelids, eyes, mouth and subtle caught-but-composed expression. His gaze must be toward the peach woman's eyes on screen-right, not toward the camera, downward at his bowl, or a disappointed stare. Preserve the peach woman's identity, face and knowing gentle expression as closely as possible.
Keep image 1's camera framing, scale, lighting, background and complete table unchanged. Keep its receiving pose exactly: she holds her own empty beige bowl in her INNER hand under the still-held small pinch; her OUTER screen-right hand holds the glass outside the bowl. He holds that same pinch in the same chopsticks on his own side; his inner hand rests separately on the table. Keep the air gap above the empty bowl, both faces visible, and all herbs, two dipping bowls, his personal bowl, her resting chopsticks and cold nem plate.
Do not reposition hands, bowl, glass, chopsticks or food. Do not put food into the empty bowl yet. No costume change, bib, apron, new props, captions or extra watermark. One vertical image, same before-release state and same framing as image 1.
```

## P2 v1 — Chuyển cùng A vào bát, đũa trống rút ngắn

Edit target: P1 v2. Root thấy hướng nhìn Khoai đã chuyển về Đào và tư thế bát/cốc giữ phù hợp cho ảnh nháp; chưa owner duyệt và không coi là endpoint nối C06.

```text
Use case: precise-object-edit.
Asset type: single vertical storyboard pose reference P2, just after receiving the same food.
Input image 1 is the EDIT TARGET and sole authority for the composition, both faces and gazes, hands, bowl, glass, clothing, table, background and lighting.
Primary request: change only the potato man's chopstick tips and the location of the SAME SMALL PINCH of nem. That small pinch has now been deposited into the peach woman's personal bowl that she is already holding in her INNER hand near the center. Put only that small bite-sized pinch inside the bottom of her bowl; her bowl is NOT full. Remove the pinch completely from the chopstick tips. The same pair of wooden chopsticks is now empty and retracted a short distance toward the potato man, visibly clear of her bowl, held in the SAME OUTER screen-left hand. Do not pick up anything new or move the food toward the shared serving plate.
Keep the peach woman's held bowl and hand in exactly the same pose and location, without growing or moving the bowl; keep her OUTER screen-right hand holding the same glass above and outside the bowl. Preserve the potato man's other hand resting separately on the table. Keep both faces, expressions and eyes exactly as in input image 1: his understated caught-but-composed look toward her, her gentle knowing look toward him. No face redesign or change of gaze.
Preserve image 1's complete 9:16 framing and camera scale, original faces, clothes (white blouse and green skirt with waist bow, no bib/apron; charcoal jacket and white shirt), warm street-eatery background, lanterns and lighting, his empty personal bowl, her resting chopsticks, front-left herbs, two dipping bowls, and the shared cold nem plate. No extra hand or extra bowl, no glass in a bowl, no duplicate pinch, no steam. The received pinch has the same delicate irregular skin ribbons, meat slivers and toasted-rice powder as the held pinch. Keep its small amount; do not import pieces from the large plate.
ONE after-release still, not a montage, no added text, captions or watermark; retain the existing small source mark. Keep all regions outside the small changed food/chopstick-tip area unchanged as closely as possible.
```
