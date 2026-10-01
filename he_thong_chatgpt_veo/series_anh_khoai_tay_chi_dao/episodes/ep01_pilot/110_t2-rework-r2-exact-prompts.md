# T2 R2 — Exact prompts

2026-10-02. Built-in imagegen, transparent_background=false cho cả năm lượt. Không API/CLI. Reference order: lượt1 OPEN3+TABLE08; lượt2 OPEN4+TABLE08; lượt3 OPEN5+nembui.jpg owner-approved real photo; lượt4 OPEN6 only; lượt5 OPEN7 only. Percentages là intent, không actual measurement.

## Lượt 1

```text
Use case: precise-object-edit.
Asset type: OPEN neutral camera-test reference for an adult AI food series.
Input images: Image 1 is the edit target OPEN3; Image 2 is TABLE08, the approved FOOD RENDITION reference only, not a framing or face replacement.
Primary request: Change ONLY the food mound within the central main plate in Image 1 to closely match the Nem Bui mound in Image 2. It must be a compact tangled mound of many fine short pale beige strands, lightly dusted with very fine roasted-rice powder, with occasional thin flat translucent strips integrated among the strands. Match the visible texture and compact presentation of Image 2, not noodles, fusilli, thick curls, crunchy flakes, chunky pieces or coarse round sesame-like grains. Keep the main plate at the same position, size and perspective, with the same approximate mound footprint.
Invariants: preserve exactly both adult characters' faces, closed mouths, gentle resting expressions, gaze, clothing, resting hands, two eating bowls, two dipping dishes, two pairs of resting chopsticks, herbs plate, water glass, table, background, warm light and camera composition of Image 1. Do not move or add any object. Do not change faces or beautify them. No action, captions, logos or imitated provider watermark. This is a newly AI-generated derivative with provenance recorded separately; do not copy a source mark from Image 2. One portrait image, no collage.
```

## Lượt 2

```text
Use case: precise-object-edit.
Input images: Image 1 edit target, Image 2 approved visual reference for the food on the central plate ONLY.
Change ONLY the central food mound. Faithfully recreate the fine, densely intertwined julienned texture of the food mound in Image 2. Reduce the thickness and width of every pale strand greatly. Most pieces should look like slender short matchsticks or narrow translucent julienned strips rather than wide flat chunks, curls or pasta. Use a light dusty beige fine powder coating, not visible round grains. Reproduce the compact low mound from Image 2; preserve the dish footprint and plate position from Image 1. Closely inspect the mound in Image 2 rather than keeping Image 1's chunky representation.
Keep absolutely unchanged the characters, their facial expressions and eyes, hands, garments, all bowls and dipping dishes, resting chopsticks, herb plate, glass, background, light, table, framing and canvas. No new props or ingredients. No captions or drawn provider marks. One portrait image, no collage.
```

## Lượt 3

```text
Use case: precise-object-edit.
Input images: Image 1 is edit target OPEN5. Image 2 is the owner-approved real Nem Bui photograph, authoritative for visible food texture only.
Replace ONLY the food mound inside Image 1's central plate with a faithful stylized-3D rendition of the mound in Image 2: irregular thin pale yellow-beige skin ribbons interspersed with thin brownish meat slices, all with a fine matte dusty toasted-rice coating. Match the actual visible appearance, irregular ribbon thickness, flatter meat slices and powdery texture in Image 2. Not shiny pasta, thick crunchy curls, sesame seeds or round granular coating. Preserve the plate and mound footprint/height from Image 1. Do not transfer the leaves, red chili garnish, plate, packaging or background from Image 2.
Everything else in Image 1 must stay unchanged: both adult characters' exact faces and resting expressions, eyes, clothes, hands, bowls, two pairs chopsticks, sauces, herb plate, glass, table, warm light, background and framing. No action, text, logos, synthetic provider watermark. Single portrait image.
```

## Lượt 4

```text
Use case: identity-preserve.
Input Image 1: edit target OPEN6.
Primary request: Reframe the SAME stationary scene slightly wider, reducing its image scale by about 8 percent and extending the view naturally, while retaining a single vertical portrait canvas. The sole purpose is to show every tip of the herbs at left with a clear small margin, and keep the right water glass comfortably inside the frame. Do NOT move the herbs plate or other objects on the table to accomplish this. Preserve the same viewpoint and downward angle; no extra sky or foreground bench.
Invariants: exact faces, closed-mouth expressions, gaze, hands at rest, clothing, fine powder-coated ribbon-and-slice food texture and quantity, all plate/bowl/chopstick/glass positions in the scene, warm light and existing background. No relighting, new expressions, new food, decorations, signage, text or synthetic watermark. Fill only the necessary peripheral scene extension. No collage.
```

## Lượt 5

```text
Use case: identity-preserve.
Asset type: END of a small upward camera tilt, neutral diagnostic, paired to supplied OPEN7.
Input Image 1 is the sole scene and identity anchor. Reframe this identical frozen moment by a VERY SMALL upward camera tilt, no dolly or zoom. Move the scene a little lower within the portrait frame, roughly 3 percent of image height, reveal only a little more of the existing street at top and lose an equivalent amount of bare wooden table facade at bottom. Preserve every herb leaf tip, both dipping dishes, entire main food plate, both eating bowls, both resting chopstick pairs and water glass, all with margins. Keep both complete faces clearly visible. Do not add sky, new buildings or brighter lamps. Emphasize Khoai's eyes without changing the lighting or scene geometry.
CRITICAL: Both characters are motionless, not acting. Copy EXACTLY the original closed mouth shapes, eye openings and gaze, eyelids, eyebrows, smiles, head angle, clothes, hands resting. No change of expression, no new teeth or parted mouth, no new squint. Keep identical food strands/slices/powder/quantity and all object relationships. Same warm light and background detail. Do not redraw food or rearrange props. No captions, logos or imitated provider watermark. One portrait image, no collage.
```

