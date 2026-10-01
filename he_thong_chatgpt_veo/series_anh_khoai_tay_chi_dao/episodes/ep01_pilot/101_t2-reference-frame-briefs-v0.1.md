# EP01 T2 — Brief khung tham chiếu v0.1

2026-10-01. Root / PAPER_PREPARATION theo100. PROPOSAL_COMPLETE, chưa tạo ảnh hoặc reference approval mới. Root trực tiếp xem hai ảnh bên dưới và tính SHA256 trên bytes local trong vòng này; không chỉ dựa tên file.

## Manifest nguồn thực

Đường dẫn tương đối từ series root; mọi file giữ nguyên, không crop/overwrite.

| ID | File/version | SHA256 | Chức năng |
|---|---|---|---|
| TABLE08 | media/raw/ep01_p6_food/T-NB-03_v0.8.jpg | AEB6DFAEE1773109243F9F952235A44F2417C6FB7FB4FAF15BE61C34CA40D924 | Bàn/quán/ánh sáng/serving geography theo78 |
| PAIR03 | media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg | ECFBE7A3C543730C268A77CA08D508147115CA804154F85EBDBB38C5C601E8C7 | Mặt, thân hình và trang phục theo45; không nền studio hoặc tư thế đứng |

Quan sát TABLE08: Khoai trái, Đào phải, nem giữa bàn, đĩa lá phía trước trái; bát chấm nhỏ gần trái món và bát chấm phía trước phải; hai bát ăn, hai đôi đũa trên bàn, cốc ngoài phải Đào. Ánh sáng ấm, quán ven phố, người/xe nền, ghế tiền cảnh; watermark dưới phải. PAIR03: áo khoác tối/sơ mi sáng của Khoai; sơ mi sáng, váy xanh và nơ hồng của Đào; hai người trưởng thành. Không dùng ảnh demo cặp đôi làm identity lock.

Không thêm rau/chấm mới, không gỡ đồ chấm hiện có hoặc đổi chúng thành nước mắm theo suy đoán. Đây bảo toàn reference đã duyệt, không nghiên cứu lại recipe. Root đọc trực tiếp bằng System.Drawing trong vòng này: cả TABLE08 và PAIR03 đều 768×1376, không exact9:16. Target đầu ra mới 9:16; nếu công cụ cần crop/extend, trình cách xử lý và kiểm watermark trước, không tự cắt. Trước upload kiểm lại đúng bytes đã chọn.

## Hai ảnh dự kiến, một trạng thái kiểm soát

| Planned ID — chưa có file/hash | Bố cục | State kiểm soát |
|---|---|---|
| T2-R-OPEN-v0.1 | Trung rộng, hơi nhìn xuống; món giữa thấp là cửa chú ý; hai mặt ở phần trên. Giữ cả presentation nem, lá/chấm, hai bát/đũa và cốc trong khung. | Ngồi cùng phía bàn, Khoai trái/Đào phải; cả hai tay nghỉ như TABLE08; cốc/đũa trên bàn; không kéo đĩa, gắp, uống hoặc nhai. |
| T2-R-END-v0.1 | Cùng cảnh/trục/độ phóng đại chủ ý, nâng hướng máy nhẹ: mắt Khoai là trọng tâm trái trên, Đào vẫn rõ như người nghe; toàn đĩa nem và bộ phục vụ vẫn thấy phía thấp. Không chỉ giữ một mép đĩa. | Cùng state trên; không tự thêm cử chỉ/đạo cụ. Endpoint phải được dẫn từ OPEN đã chọn để giảm drift, không hai ảnh độc lập cùng prompt. |

END cũng là composition reference cho S02, **không** frame diễn xuất cuối B04 hoặc chứng nhận match S01/S02. Hai ảnh này là neutral diagnostic endpoints: chưa thay keyframes production S01 có tay Đào gần đĩa, chưa có S04/S05. Sau probe, tạo action-specific frames theo storyboard, không lấy neutral frames làm toàn bộ đầu vào tập.

Không tạo thêm ảnh ký ức mẹ/bếp. Nét nhớ được triển khai qua ACT/VOICE trong bước khác. Đây tránh mở thêm nhánh chưa duyệt, không giản lược story hoặc acting đã chốt.

## Prompt dự thảo — chỉ dùng sau execution approval

OPEN:

> Use TABLE08 as the approved meal, street-side eatery, lighting and spatial reference; use PAIR03 for the two adult original characters' facial identity and clothing only. Create a vertical 9:16 medium-wide composition, slightly looking down toward the complete shared meal. Potato character sits screen left; peach woman sits screen right. Keep their faces in the upper area and the whole Nem Bui presentation in the lower centre. Retain the same herbs plate front-left, both dipping dishes, two eating bowls, chopsticks resting on the table and water glass outside the woman's right side. Both characters' hands rest naturally, without touching or moving any food or utensils. Preserve the warm ordinary tidy street eatery and the original spatial relationships; no romantic pose, extra ingredients, steam, signage, captions or character names. Preserve source provenance/watermarks; do not erase them. No hand or food action. The still is a neutral camera-test reference, not a scene performance.

END (input OPEN được owner chọn + nguồn đã duyệt nếu route hỗ trợ):

> Reframe the approved OPEN image to the endpoint of a small, motivated upward camera tilt without crossing the axis or pushing in. Bring the potato character's eyes into the primary visual emphasis, while keeping the peach woman clearly visible as a listening companion. Keep the entire food presentation and every serving item visible in the lower foreground, not merely the plate edge. Preserve the exact same identity, clothing, resting hands, table layout, food quantity, lighting and provenance. No object movement, new expression performance, text or extra props. If this composition cannot fit, do not silently remove meal items or switch to a close-up; return it for review.

Prompt là ý đồ, không cam kết model sẽ báo không làm được. Operator phải reject output sai, không coi câu cuối là công cụ enforcement. Khả năng nhiều ref/chỉnh ảnh trên account chưa kiểm, không xác định model image từ tên dự án.

## Kiểm ảnh trước handoff

So sánh trực tiếp với TABLE08/PAIR03 và OPEN→END: mặt/váy/nơ; tuổi/quan hệ; toàn món và đúng đồ ăn kèm; đủ bát/đũa/cốc; tay nghỉ; bên trái/phải không đảo; không dời props để nhét khung; tông ấm và mắt rõ; nền không lấn mặt; crop không mất watermark. Không chấp nhận việc sửa một lỗi tạo thêm lỗi khác.

Ghi actual file ID/path/version/hash/dimensions/model/prompt/edit history; owner chọn từng ảnh sau visual review. Quyền upload/usage vẫn phải kiểm provenance theo hồ sơ45/78 trước request thực, không suy quyền sở hữu tuyệt đối từ approval sáng tạo.

Nếu END không giữ toàn bữa ăn: HOLD và báo framing feasibility; không tự đổi sang camera tĩnh, mất rau/chấm, zoom hoặc thêm insert. Ảnh tĩnh đẹp không chứng minh chuyển máy được.

Handoff: đã xác định nguồn và hai briefs; chốt hướng theo100, chưa asset selection; giả định endpoint tái khung khả thi; mở actual images/route/rights; tiếp theo reviewer giấy rồi execution gate cho ảnh.
