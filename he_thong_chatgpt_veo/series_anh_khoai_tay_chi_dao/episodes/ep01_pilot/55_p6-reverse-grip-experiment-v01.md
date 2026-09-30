# P6 — Reverse integration v0.1

Ngày 2026-09-30. Owner “cứ làm đi” sau53/54: tiếp tục still trials, không video/voice. P6 OPEN. Hai request editor Nano Banana Pro,9:16,mỗi request một output; UI0credit trước từng submit. Không kiểm billing tổng. QC là root operator, chưa reviewer độc lập/owner acceptance. Primary identity vẫn duo45 v0.3 (đã mở ảnh local đối chiếu lượt này).

## H-K-I04 — canvas tay, identity phụ trợ

Canvas H-K-C01, Flow asset `ef5c30f0-736b-4d59-999f-6ddca114e77b`; explicit composer component `Two characters standing in studio` primary45. Raw C01 đã có bản local trước editor, không ghi đè. Editor có thể giữ nhiều phiên bản trong cùng asset; tên `Hand holding wooden chopsticks` không còn mô tả đầy đủ current canvas.

Exact prompt:

```text
Expand the CLOSE-UP HAND canvas into a waist-up portrait of Anh Khoai, the adult golden potato on the LEFT in the attached duo reference. Keep the canvas hand, finger arrangement and both wooden chopsticks unchanged in shape and camera orientation; zoom out to make this hand proportional to his body and connect its existing navy sleeve naturally to his right shoulder. Use the duo ONLY for Khoai face, potato silhouette, cream collared shirt and navy rolled overshirt with chest pocket. The raised hand stays on screen left, held clear of his torso; the thumb and separate curved fingers remain visible as in the canvas, with two empty chopstick tips pointing screen right. His other arm rests naturally. Plain warm ivory studio background, soft warm light, tactile stylized 3D render. No peach character, food, text, additional hands or additional sticks. Preserve platform watermark.
```

Actual: full-body thay waist-up; mặt/outfit khá sát primary, thân nhỏ hơn trong framing. Thumb và curved fingers đọc rõ hơn I03, không closed fist; hai đũa liên tục. Tuy nhiên long tips hướng screen LEFT, không RIGHT như prompt, canvas orientation không bảo toàn. Grip cơ học hoàn chỉnh/hidden supports và handedness chưa chứng minh. **PARTIAL_DIAGNOSTIC / ORIENTATION_REWORK**, không production pass.

Local `media/raw/ep01_p6_consistency/H-K-I04_v0.1.jpg`; SHA256 `412367B419CD3EEADD65390BD853A790776FFC7E354B6ACFB1F1970A74C93557`. Proof `H-K-I04_flow-proof.png` cùng folder.

## H-K-I05 — sửa riêng hướng

Canvas I04; không reference thêm. Exact prompt:

```text
Change ONLY the pose of the raised right forearm and hand: rotate the wrist so the two long empty chopstick tips point to SCREEN RIGHT, toward the space in front of his chest, with short handles to screen left. Preserve the visible thumb and separate curved fingers in this same relaxed eating grip; do not turn the hand into a fist. Keep this exact potato face, silhouette, body proportions, cream shirt, navy overshirt, other arm, framing and background unchanged. Exactly two continuous chopsticks. No food or text. Preserve platform watermark.
```

Actual: hướng screen-right đạt, mặt/outfit/frame phần lớn giữ, nhưng thumb không đọc rõ, các ngón lại gần song song nắm que. **GRIP_REGRESSION / REWORK**; không lựa bản sau chỉ vì mới hơn. Không flip toàn ảnh bằng code để che lỗi hoặc đổi handedness.

Local `media/raw/ep01_p6_consistency/H-K-I05_v0.1.jpg`; SHA256 `8BC1621C64E728FBFA45BA0526B923274D546D82A6A1AB08EA1A17E5983AB500`. Proof `H-K-I05_flow-proof.png` cùng folder. Media gitignored; docs chỉ manifest.

## Tổng hợp vòng

Đã xác định reverse integration cho visible fingers tốt hơn nhưng không giữ direction; direction repair gây regression. Quyết định giữ cả hai, không promote và không lặp lại cùng kiểu repair trong vòng này. Giả định: grip cận chỉ diagnostic, không model sheet approved. Còn mở: đạt grip + direction + identity đồng thời; motion chưa test. Tiếp theo: thiết kế close-up grip ngay trong orientation cuối rồi kiểm trước expand, hoặc phương án staging khác nhưng giữ story và route owner nếu đổi ý nghĩa. Mẫu food-only làm riêng56, không để lỗi tay cản nghiên cứu món. Đề xuất bổ sung năng lực agent tại agents/10, chưa duyệt/dispatch.
