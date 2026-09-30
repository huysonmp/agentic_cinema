# P6 — Diagnostic cận tay cầm đũa v0.1

Ngày 2026-09-30. Owner yêu cầu “h bước tiếp theo đi” sau51. Cho tiếp tục công việc, không tự suy approval toàn P6/scene/voice/video. P6 vẫn OPEN. Các cảnh51 vẫn candidate, v0.3 duo45 vẫn primary identity.

## Mục tiêu và controls

Tách tay thành diagnostic component để kiểm lỗi grip còn fail49, trước khi đặt lại trong scene. Không cắt lỗi khỏi ảnh để coi shot đạt. Cận tay không chứng minh full-character consistency, motion gắp hoặc chuyển miếng nem. Không thêm food appearance chưa kiểm chứng.

Primary Flow `Two characters standing in studio`; chỉ dùng texture/anatomy/sleeve của Khoai làm reference, không dùng failed grip. Image / Nano Banana Pro / 9:16 / x1. UI trước submit 0 credit; cap200 vẫn nguyên. Không upload reference mới. Kiểm ảnh trước retry; không lặp prompt tương tự vô hạn.

Acceptance: hai đũa liên tục/tách được; lower đỡ bởi thumb web/ring, upper pencil-like; không closed fist, không stick xuyên da, không ngón thừa/fused nhìn thấy. Phần bị khuất ghi NOT_VERIFIABLE, không tự PASS.

## H-K-C01 exact prompt

Create a diagnostic CLOSE-UP of ONLY Anh Khoai’s anatomical right hand and forearm holding exactly two wooden chopsticks in a conventional relaxed eating grip. Use the left potato character in the attached image solely for golden potato skin texture, rounded adult cartoon hand anatomy, cream cuff and navy rolled overshirt sleeve. Crop out the face and all other characters. Camera sees the thumb and finger supports clearly; hand fills most of the frame against a plain warm ivory background. Lower chopstick rests in the thumb web and against the ring finger, staying still. Upper chopstick is held like a pencil between thumb, index and middle fingers. Show the index and middle fingers curved separately over the upper stick, not all fingers curled into a fist. Both long chopsticks extend toward screen right with a small gap between the empty tips. Exactly two continuous sticks, no skin intersection or fused fingers. Warm tactile stylized 3D animated-film render matching the reference. No food, bowls, table, text, labels or arrows. Single portrait diagnostic image; preserve platform watermark.

Result: Flow asset ef5c30f0-736b-4d59-999f-6ddca114e77b; local media/raw/ep01_p6_consistency/H-K-C01_v0.1.jpg. Root QC: rõ hai đũa liên tục/tách tips, thumb ép upper, ngón curved riêng, lower có điểm đỡ khác upper; không còn closed-fist đồng thời giữ hai que như49. STATIC_GRIP_PROVISIONAL_PASS ở mức quan sát, chưa chứng minh đủ khớp bị khuất, đúng anatomical handedness chắc chắn hoặc motion. Chất liệu vàng/cuff/sleeve sát primary; đây là component diagnostic không approved identity/canon asset.

## H-K-I01 — tích hợp có phân vai input

Hai Flow components: approved duo45 là ONLY identity/outfit; H-K-C01 là grip-only candidate. Không upload mới. Image / Pro /9:16/x1; UI0credit trước submit. Exact prompt:

Two input roles: the image showing two full-body fruit characters is the ONLY identity, face, proportions and clothing reference for Anh Khoai, the potato on the left. The separate close-up hand image is ONLY a chopstick grip reference. Show only Anh Khoai in a waist-up studio portrait, original golden potato silhouette, thick dark brows, brown eyes and gentle neutral smile; original cream shirt and navy rolled overshirt with chest pocket. His anatomical RIGHT hand, on the LEFT side of the picture, is raised at chest height clear of his face and torso, holding exactly two wooden chopsticks in the same relaxed eating grip as the close-up: thumb and curved index/middle control upper stick, ring supports lower stick, fingers not curled in a fist. Chopsticks extend toward screen right with empty separated tips. Preserve the hand material and arm scale from the character, do not enlarge hand to dominate his body. Left arm relaxed. Plain warm ivory backdrop, matching soft studio light, tactile stylized 3D render. No peach character, food, bowl, table, text or logos. Single portrait image; preserve platform watermark.

Result: Flow asset dba187f0-f6c0-4ef0-8cc1-7efe8a176e53; media/raw/ep01_p6_consistency/H-K-I01_v0.1.jpg. Face/outfit khá sát primary, tay right screen-left, hai đũa tách nhưng bốn ngón xếp gần song song ôm que, thumb không thấy/điểm đỡ không đọc rõ: GRIP_INTEGRATION_FAIL. Không suy hai đầu vào luôn kiểm soát được grip.

## H-K-I02 — editor repair

Edit target H-K-I01 đã lưu raw trước sửa; UI0credit. Không gắn thêm component trong composer editor; target tự động là input. Cụm “attached close-up” trong prompt tham chiếu nguồn của request trước nhưng không xác nhận editor gửi lại original refs; ghi rõ giới hạn thay vì nhận đây là three-input run. Exact prompt:

Fix ONLY the raised hand. Turn its palm slightly toward the camera so the thumb is clearly visible. Match the open eating grip in the attached close-up: thumb lies diagonally across the sticks, index and middle fingers curl separately over the upper stick, ring finger supports the lower stick, pinky relaxed. Do not show four parallel fingers enclosing both sticks in a closed fist. Keep exactly two sticks with separated empty tips pointing right. Preserve the same face, head shape, clothes, other hand, body, framing, background and light. No additional props or text. Preserve platform watermark.

Result: editor giữ cùng asset dba187f0-f6c0-4ef0-8cc1-7efe8a176e53; local media/raw/ep01_p6_consistency/H-K-I02_v0.1.jpg. Thumb nhú thêm nhưng palm chưa xoay rõ, bốn ngón vẫn nắm gần song song, upper/lower support không đọc được: GRIP_INTEGRATION_STILL_FAIL. Giữ lỗi, không promote candidate. Không chứng minh sửa cục bộ đã thành công.

## Manifest và tổng hợp

Ba request, từng UI0credit, không video/audio/food/upload mới. Ba raw preview đều768×1376, watermark nguyên, không exact9:16/native1K. Đã tải và xem từng output; hai asset cards, I02 là editor history của I01. Media gitignored; Git lưu prompt/manifest/QC.

| File trong media/raw/ep01_p6_consistency | Bytes | SHA256 |
|---|---:|---|
| H-K-C01_v0.1.jpg | 76624 | CCA4BE13F511E6FEEC50EF1E369A7117EFF44497112A1353187BA533C61B71E1 |
| H-K-I01_v0.1.jpg | 104004 | BCBBCFB064F5192544B9C4C5FB2F464AEA3724303B39F34303EADF6895EA165E |
| H-K-I02_v0.1.jpg | 102201 | CD669066BCDE379D194CC0FDDAF006612F83B913DB0E25AAFB96C6B90B7077F2 |

Proof Flow_H-K-I02_proof.jpg trong cùng thư mục. Root static review, không independent-agent PASS và không owner approval.

Đã xác định: cận tay giúp đọc grip rõ hơn; chuyển grip vào waist-up chưa đạt với generation hai components và một edit. Quyết định: không đóng lỗi grip, không hạ tiêu chí/chuyển video. Giả định: cận tay là prototype riêng, không production shot. Còn mở: handedness/khớp khuất, giữ grip khi tích hợp và motion; các mục food/voice/profile/asset gate còn nguyên.

Bước tiếp theo: chuẩn bị phép thử editor với close-up gắn trực tiếp và phân vai rõ, hoặc pose component bố cục gần đúng shot; không tiếp tục cùng prompt mơ hồ về ref trong history. Đồng thời hoàn tất food appearance intake theo P2 để chuẩn bị scene thật, không dùng món tự đoán. Nếu thay workflow audio/video cần request riêng trước chạy. P6 OPEN, chưa mở P7 chính thức.

## Các bước kế sau diagnostic

Food intake: đối chiếu nguồn P2 và ảnh Nem Bùi, ghi appearance/biến thể/provenance; quyền đọc nghiên cứu không tự cấp quyền upload. Voice: chuẩn bị mẫu đối đáp exact, cần quyết định workflow và quyền thử audio/video riêng; không suy quyền ảnh thành quyền video. Geometry profile, expression, owner asset review còn mở. Chỉ handoff P7 sau gate P6, không thay script để né khó kỹ thuật.
