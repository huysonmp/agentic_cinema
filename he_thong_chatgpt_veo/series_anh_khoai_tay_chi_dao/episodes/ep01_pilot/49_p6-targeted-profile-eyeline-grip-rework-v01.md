# EP01 — P6 targeted rework v0.1

Ngày 2026-09-30. Status: SIX_OUTPUTS_SAVED / ROOT_EYELINE_PROVISIONAL_PASS / PROFILE_AND_GRIP_FAIL / P6_STILL_OPEN. Owner “ok làm tiếp đi nào” sau46–48. Sửa ba lỗi cụ thể, không tự promote asset hay chuyển video. Giữ cap tổng200credit theo41; số dư ở48 là1.050, kiểm actual cuối vòng.

## Control / reference / gates

Primary reference duy nhất: approved duo45, Flow `Two characters standing in studio`, SHA256 ECFBE7A3C543730C268A77CA08D508147115CA804154F85EBDBB38C5C601E8C7. Dùng asset có sẵn, không upload reference mới. Không dùng output sai làm mẫu identity. Pro/image/9:16/x1, đọc giá trước mỗi Generate, giữ watermark. Native preview export có thể không exact9:16/native1K; kiểm actual metadata trước báo giao.

Chạy một lượt mỗi lỗi; nếu còn lỗi, chỉ retry khi có chẩn đoán và prompt delta cụ thể. Không chạy lặp vô hạn để tạo PASS. Root visual QC không giả independent-agent hoặc owner approval. Các phần geometry khuất vẫn generated inference.

## Prompt exact

Mỗi prompt = COMMON + CHARACTER + TARGET + END, ghép một dấu cách. CHARACTER là KHOAI/DAO nguyên chuỗi46; với H-K02 chỉ thay `Both empty hands and feet visible.` bằng `Both hands and feet visible.`. END tách cho H-K02 như dưới để không mâu thuẫn no props. Chỉ các text dưới đây được gửi, không ID/nhãn.

COMMON:

Use the attached approved duo image as the only source of character identity, face, fruit shape, adult proportions, materials and clothing. Show only the specified character and preserve all visible design details; do not redesign or blend in earlier versions. This is a diagnostic studio still, not a scene from the episode.

C-K-P03 / TARGET:

Orthographic right-facing side elevation of Anh Khoai, like a model-sheet silhouette. Camera exactly perpendicular to his right-facing body: a true ninety-degree side view, not three-quarter. Nose, mouth and shoe toes point toward the right edge; back of head and jacket toward the left edge. Show only ONE eye and ONE eyebrow. The far eye and far eyebrow are fully hidden. The front shirt buttons and belt buckle are hidden behind the body's near-side contour, not presented to camera. Head, shoulders, hips and feet face the same rightward direction, with no head turn toward camera. Arms relaxed and empty. Keep his gentle neutral closed-mouth smile.

E-D02 / TARGET:

Exact front view of Chi Dao: head, shoulders and torso square to camera. Change only the eye gaze while preserving her subtle knowing closed-mouth smile. Both pupils and irises move toward the LEFT EDGE of the IMAGE, toward an unseen friend outside frame. The pupils sit visibly closer to the left side of each eye opening; more white of each eye is visible on its RIGHT side. Do not look at the camera or toward the right edge. Keep her original eye shape, lashes and brows, without crossed eyes or changing head orientation. Arms relaxed and empty.

H-K02 / TARGET:

Front-facing Anh Khoai with exactly two plain wooden chopsticks in his anatomical RIGHT hand, on the LEFT SIDE of the image, raised to mid-chest away from his torso. Render a readable eating grip, not a closed fist around both sticks. The LOWER chopstick rests in the thumb web and on the ring finger, which supports it without squeezing it in a fist. The UPPER chopstick is held separately between the thumb, index finger and middle finger, like a pencil. Index and middle fingers are visibly bent around the upper stick, with a small gap separating it from the lower stick. Both sticks extend toward screen right with separated empty tips. Natural compact cartoon hand anatomy consistent with the character, no extra digits, no fused fingers and no stick passing through skin. Other hand relaxed and empty. Keep the calm reference face. No food, bowl, plate or table.

END C-K-P03 / E-D02:

One full-body character centered with generous margin, full shoes and head or leaf visible. Plain warm ivory studio background and soft neutral-warm light matching the reference. No companion, food, props, text or logos. Portrait 9:16. Preserve platform watermark.

END H-K02:

One full-body character centered with generous margin, full shoes and head visible. Plain warm ivory studio background and soft neutral-warm light matching the reference. Only the specified two chopsticks; no companion, food, other props, text or logos. Portrait 9:16. Preserve platform watermark.

## Acceptance trước run

- Profile: screen RIGHT, chỉ một mắt/mày, không thấy mặt trước áo/buckle do xoay về camera; root nhận định hình học, không đo góc3D.
- Eyeline: iris/pupil LEFT trong hai mắt, không cross-eye; giữ đầu front và nét tinh ý.
- Grip: hai đũa độc lập, lower được đỡ/upper pencil-like; ngón bị che đánh NOT_VERIFIABLE, không suy chứng minh gắp từ still.
- Mọi ảnh: identity/outfit so primary, không redesign; actual dimensions/hash, không xoá output sai.

Next: xem và log từng actual file, ghi pass/partial/fail. Food/voice/motion và owner geometry approval vẫn pending. Không phải kết luận P6complete.

## Actual first three / chẩn đoán đổi approach

Ba request thành công về generation, selected primary duo, Pro/image/9:16/x1, UI0credit từng preflight; download/xem trực tiếp actual file. Files media/raw/ep01_p6_consistency/: C-K-P03_v0.1.jpg (edit/a89052fa-7e6c-4a17-aba0-b6bf6e53d59c), E-D02_v0.1.jpg (edit/38ecd277-8521-4249-b6d7-063189581371), H-K02_v0.1.jpg (edit/e8625983-54a4-4d2a-80e6-b600cfb847df).

- Profile còn mày xa, mặt trước áo và buckle: EXACT_PROFILE_FAIL; không đo exact degree.
- Đào mắt screen-left của ảnh nhìn vào trong/screen right, mắt screen-right nhìn screen left: CROSSED_GAZE_FAIL, không đồng bộ left gaze. Không gọi chuyển động mắt thành công.
- Khoai vẫn closed-fist-like around both sticks, lower/upper support không đọc rõ: GRIP_FAIL. Tương tựH-K01; không có chứng cứ prompt dài cải thiện grip.

Hình nhìn tương đối giữ identity/outfit, nhưng ba biến điều khiển không đạt. Giả thuyết: prompt regeneration dài từ duo không đủ để kiểm điều khiển cục bộ; chưa kết luận nguyên nhân model hay Flow dựa ba ảnh. Kiểm phương pháp edit cục bộ là thử nghiệm, không cải tiến đã được chứng minh.

## Targeted edit diagnostic — một lượt mỗi target

Dùng editor của chính generated image làm EDIT TARGET, không promote làm approved identity source/canon. Không upload dữ liệu mới; primary45 vẫn chuẩn đối chiếu. Giữ các phần không chỉnh; review drift so primary và target. Editor canvas target là đầu vào chỉnh; không khẳng định request này chỉ reference duo. Kiểm Image/Pro/9:16/x1/price trước từng Generate. Tối đa3edit ở vòng này, không lặp thêm nếu fail.

C-K-P04 edit target C-K-P03, prompt exact:

Rotate this same character and his whole body about fifteen degrees farther away from the camera into a strict right-facing side elevation. Hide the far eyebrow and far eye completely. Show the side of the jacket, not its front; hide the shirt button row and belt buckle behind the near-side contour. Keep only the near eye visible. Keep the same potato facial identity, clothing, colors, materials, scale, ivory background and full-body framing. Change only the viewing orientation. No redesign, props, text or companion. Preserve watermark.

E-D03 edit target E-D02, prompt exact:

Fix only the gaze. She looks toward the LEFT EDGE of this picture with both eyes together, not cross-eyed. Move the pupil in the eye on the LEFT SIDE OF THE PICTURE leftward toward its outer corner; the pupil in the eye on the RIGHT SIDE OF THE PICTURE also looks left. Keep a natural relaxed gaze and normal eye alignment. Preserve the same eye openings, lashes, brows, smile, face, peach shape, leaf, clothes, pose, background and framing. No other changes. Preserve watermark.

H-K03 edit target H-K02, prompt exact:

Change only the raised hand's grip on the two wooden chopsticks. Open the fist into a natural eating grip: lower stick supported by the ring finger and thumb web; upper stick held like a pencil by thumb, index and middle fingers. The thumb lies across the two supports, not hidden behind a fist. Make the two sticks diverge slightly, with separated empty tips pointing right. Keep exactly two straight sticks and natural compact fingers, no extra digits or skin intersections. Preserve the same face, outfit, other hand, full-body pose, background and framing. No food or other props. Preserve watermark.

## Actual edit results / manifest

Ba edit thành công, Nano Banana Pro/9:16, từng edit preflight UI0credit, editor xuất một kết quả (editor không có x1 selector như generator). Thứ tự thực tế H-K03, E-D03, C-K-P04. Flow edit giữ cùng asset URL với target và thêm history; local raw originals đã download TRƯỚC edit và không ghi đè. Không báo có6asset cards mới; có6request/output versions, ba card có edit history. Target reference tự động của editor, không đính thêm duo vào editor prompt.

Một download E-D03 gặp no_matches khi canvas chưa hiển thị; refresh AX thấy image rồi download thành công. Không generate lại, không tính lỗi download thành backend generation failure.

| File trong media/raw/ep01_p6_consistency/ | Bytes | SHA256 |
|---|---:|---|
| C-K-P03_v0.1.jpg | 69981 | E7B78ECB3DA27DB112DE5A7DAEDC983A609DFDC23F01623C2B537B22D64306E3 |
| E-D02_v0.1.jpg | 71802 | 5E8ED263600353D2C7324E6698E25854D21D90C6A22D49640B3F6D29515772CA |
| H-K02_v0.1.jpg | 83773 | 06D3320DD2B637FEC81A46A7583D9C00D8D60C97F44CF4E64FB2DAA790F762D5 |
| C-K-P04_v0.1.jpg | 68148 | 301993D2291E747A30F3940A5436494B57417875E94574178706C35ED45F0610 |
| E-D03_v0.1.jpg | 73331 | D8C78CB321C6E050D98A56F2F1E485D27C9D64B65398ED7C54AD70EA55EC3B52 |
| H-K03_v0.1.jpg | 84480 | 9DBD55A2A405651B73895D96E5BF1C83F3187A295AB860ECE6E26D3443900EA6 |

Cả6actual768×1376, watermark nguyên, không exact9:16/native1K verified. Đã xem trực tiếp toàn bộ6localfiles, không flip/crop/upscale. Media gitignored, manifest/prompt/QC commit; không có binary trên GitHub.

E-D03: cả hai iris/pupils nhìn screen LEFT, không còn crossed gaze củaE-D02 ở mức root quan sát; giữ nụ cười kín, outfit và pose gần target. EYELINE_PROVISIONAL_PASS cho biến direction, không toàn expression sheet hoặc owner approval; cực trái hơi mạnh cần đặt vào shot thật để xem tự nhiên. Không chứng minh gaze animation.

H-K03: sticks tách đầu rõ hơn, nhưng tay vẫn gần closed fist, upper-pencil/lower-ring support không đọc được. GRIP_FAIL; chỉ cải thiện tip separation, chưa functional grip. Không gọi anatomy PASS.

C-K-P04: xoay đổi rõ nhưng thành screen LEFT; chỉ thấy một mắt/mày, không còn front belt buckle rõ, tuy nhiên còn slight back/torso three-quarter. DIRECTION_FAIL / EXACT_ORTHOGRAPHIC_NOT_PROVEN. Asset name vẫn `right side profile` không là chứng cứ hướng thực. Giữ fail, không flip che lỗi và không promote geometry.

## Credit và tổng hợp vòng

Số dư Flow sau6request là1.050, bằng lần kiểm48; preflight từng lượt0. Observed balance delta0credit, không có itemized billing audit; không suy mọi Flow generation free. Không video/voice/food/upload mới/mua credit/publish. Tổng15request từ46–49 (9 +6), local15output versions; generation success khác quality acceptance.

Proof media/raw/ep01_p6_consistency/Flow_P6_rework_v0.1.jpg, account panel đóng trước capture. Primary duo45 giữ nguyên. Chưa dùng candidate mới làm production reference.

- Đã xác định: edit cục bộ sửa gaze ở1case; regeneration prompt dài không sửa được3biến ở lượt này. Không tổng quát thành phương pháp tối ưu đã được chứng minh.
- Quyết định đã chốt: owner cho tiếp tục trial; không có approval mới cho E-D03/geometry/production. Không bỏ hoặc hạ tiêu chí profile/grip để đủPASS.
- Giả định: primary duo làm identity/outfit; phần khuất từ AI vẫn inference; root static-eye QC là tạm thời.
- Còn mở: profile screenRIGHT chuẩn, grip đũa, expressive depth, geometry owner gate, food/voice/motion, independent media review.
- Next đề xuất: một diagnostic cận tay để đọc grip rõ trước khi quay lại full body; kiểm góc nghiêng bằng input pose/reference định hướng rõ thay vì tiếp tục kéo dài prompt. Chưa thiết kế/upload pose reference mới, chưa có kết luận route sẽ thành công. Dừng bounded round6lượt, không lặp thêm cùng approach trong vòng này; vẫn ởP6, không chuyểnvideo.
