# EP01 — P6 static hand/prop diagnostics v0.1

Ngày 2026-09-30. Status: TWO_OUTPUTS_SAVED / ROOT_QC / CHOPSTICK_GRIP_REWORK_NEEDED / BOWL_PROVISIONAL. Authority như46–47: thử still P6 trong cap tổng200credit, không video/food/voice/publish. Identity source duy nhất approved duo45, không promote angle/expression chưa duyệt.

Hai phép thử độc lập: Khoai cầm đôi đũa trống; Đào đỡ bát trống. Không mô phỏng Nem Bùi suy đoán. Chỉ kiểm pose/grip tĩnh, không chứng minh gắp/chuyển/thả thức ăn hay consistency chuyển động. Không tự gán kích thước đạo cụ này là production lock.

## Prompt exact

COMMON + CHARACTER + POSE + END, ghép một dấu cách. CHARACTER = KHOAI/DAO nguyên chuỗi46, duy nhất thay câu `Both empty hands and feet visible.` bằng `Both hands and feet visible.`. Không còn yêu cầu tay trống mâu thuẫn grip.

COMMON:

Use the attached approved duo portrait as the ONLY character identity, proportions, clothing and material reference. Generate a single-character static hand-and-prop diagnostic, not a redesign or a scene from the episode. Preserve the selected character's face, fruit volume, adult proportions, colors, clothing details and fabric texture. Change only the arm and hand pose required to hold the one specified prop. Use a calm neutral reference expression. Do not invent accessories or blend in earlier designs.

H-K01 / POSE:

Straight-on front view, head and torso facing camera. Anh Khoai holds exactly two plain straight wooden chopsticks in his anatomical RIGHT hand, the hand on the LEFT SIDE of the image. Raise this hand to mid-chest, away from the torso so the grip is clearly visible. Show a plausible eating grip with a supported lower chopstick and movable upper chopstick, separated tips pointing toward screen right. Clear distinct fingers with no extra digits, fused fingers, floating sticks or intersections through the hand. His other hand hangs relaxed and empty. No food between the tips, no bowl, plate or table. This is a still pose, not a motion sequence.

H-D01 / POSE:

Straight-on front view, head and torso facing camera. Chi Dao holds one small plain ivory ceramic eating bowl at upper-waist level using both hands. One palm supports the underside and the other hand steadies the side, fingers visibly wrapping naturally without passing through the ceramic. The bowl is clearly empty, tilted only slightly toward the camera so its rim and empty interior can be inspected. Arms comfortably bent, elbows separated from the torso. Clear distinct fingers, no extra digits, fused hands, duplicate bowls or floating bowl. No food, chopsticks, plate or table. This is a still pose, not a motion sequence.

END:

One full-body character centered, generous clear margin on every side, full shoes and head or leaf visible. Plain warm ivory studio background, soft neutral-warm lighting consistent with the reference. Only the specified prop; no food, companion, text or logos. Portrait 9:16. Preserve platform watermark.

## QC / gate

Pro/image/9:16/x1, đọc giá trước mỗi lượt. Download actual file, root visual review, hash/bytes/dimensions. Kiểm identity/outfit rồi anatomy, số đạo cụ, điểm tiếp xúc và anatomical hand vs screen direction. Partial occlusion ghi NOT_VERIFIABLE, không bịa đủ số ngón. Không chứng minh grip biomechanical chính xác hay motion từ still. Không independent-agent PASS hoặc owner approval. Failed pose lưu riêng không xoá/sửa ảnh che lỗi.

## Actual run / root review

Hai Generate thành công, primary duo reference, Pro/image/9:16/x1, UI0credit trước từng lượt. H-K01 asset edit/c71c00a5-b48c-47e2-af56-5a4e8b28161f; H-D01 asset edit/14105867-a2a0-44c2-aae5-3c3879667063. Download và xem trực tiếp actual local images, không chỉnh/flip/upscale.

| File trong media/raw/ep01_p6_consistency/ | Dimensions | Bytes | SHA256 |
|---|---|---:|---|
| H-K01_v0.1.jpg | 768×1376 | 86783 | 990E89C5248F78BFDD032B4C4D327DDB25D18AB58C16506AEB5565122051CCD8 |
| H-D01_v0.1.jpg | 768×1376 | 71987 | 1A03F3B25B29CE5F9D59C7E789B766A234DAA0B04830C88D63985A4655B60431 |

Khoai: đúng hai đũa, anatomical RIGHT/screen LEFT, tips screen right, không food/table; identity/outfit nhìn tương đối giữ. Nhưng các ngón nắm cả đôi đũa cùng nhau, không đọc rõ lower support/upper movable như eating grip; FAIL functional-grip brief. Anatomy bị che, không chứng minh đủ số ngón hoặc gắp được. Không retry trong vòng này.

Đào: một bát trống, hai tay tiếp xúc và phần tay dưới bát nhìn thấy, không phát hiện xuyên tay rõ ở bản768px. Giữ blouse collar/buttons/skirt/bow; torso hơi chếch thay exact front, hand underside partly occluded. Root PROVISIONAL STILL USABLE, không strict pose/anatomy PASS. Grip chuyển động chưa kiểm; kích thước bát chưa owner-approved. Watermark cả hai giữ nguyên.

## Closeout vòng46–48

9 requests trong vòng hiện tại =4angle +1targeted rework +2expression +2hand; 9output generation thành công, không có backend failure trong vòng này. Quality failures/partials ghi trên, không gộp generation success thành QC PASS.

Flow hiển thị số dư1.050 sau vòng, bằng số dư kiểm ở44; từng request UI0. Observed balance delta0credit, không có itemized billing audit hoặc tuyên bố mọi lượt Flow đều miễn phí. Cumulative cap200credit vẫn áp dụng. Không video/voice/food/reference upload mới. Actual exports768×1376 không exact9:16 và không native1K verified; chưa phải final production delivery format.

Proof screenshot: media/raw/ep01_p6_consistency/Flow_P6_round_v0.1.jpg, account panel đóng trước capture để không lưu identity. Media nằm local/gitignored; commit/push chỉ docs và manifest/hash, không báo GitHub đã có binary outputs.

Đã xác định: source identity primary duo dùng được cho các diagnostic riêng, nhưng chưa chứng minh continuity. Chốt không thay baseline45 hoặc dựng P6complete. Giả định: collar/buttons theo primary, hình khối phần khuất do AI suy diễn. Còn mở: exact Khoai profile, Đào eyeline, sắc thái chột dạ, grip đũa, food visual, voice và motion. Bước kế: owner review hình khối/face variants; sửa lỗi direction/eyeline/grip theo lượt kiểm có tiêu chí trước khi shot tương tác. Không cần owner trả lời thêm7câu để duyệt những gì đã duyệt.
