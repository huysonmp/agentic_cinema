# P6 — Duyệt bộ phục vụ và thử bàn ăn

Ngày 2026-10-01. Owner “duyệt” bộ phục vụ71 và đề nghị dựng bàn ăn. Chốt lá sung + ít đinh lăng, hai chén tương ớt, hai bát, hai đôi đũa gỗ, cốc nước bên Đào; quán ven phố bình dân chiều tối. Một food-table still trước ghép nhân vật; chưa mở voice/video hoặc đóng P6.

Texture F05 được giữ làm reference thiết kế, ảnh thật68 hỗ trợ appearance/lá. Không dùng F05 để tự chứng minh fact món đúng. Không thay script32: Khoai đưa phần chưa chạm miệng vào bát Đào. Chưa thêm cảnh cuốn/chấm.

Trạng thái: T-NB-01 / GENERATED / DOWNLOADED / REWORK_REQUIRED / OWNER_OUTPUT_APPROVAL_PENDING.

## Preflight và input

Flow project9276788e-9781-44fb-ba5b-083006667374. Lỗi kết nối reCAPTCHA service xuất hiện trước run; reload một lần, không giải challenge hoặc vượt kiểm tra. Sau reload UI sử dụng được, không challenge xuất hiện. Chọn hai thành phần đã có: F05 “Creating reference image of Nem …” (asset56d529b7-b789-4988-b83d-95b2a00ec347), rồi ảnh mẹt filename đã duyệt68. Không upload mới, không chọn F04. UI Hình ảnh / Nano Banana Pro / 9:16 / x1 / 0 tín dụng trước submit. Hai component hiện trong composer; nhấn tạo một lần, UI0% và đúng prompt. Giá UI không phải xác nhận billing ledger.

## Prompt thực chạy

```text
Create a vertical food-table concept image for two friends at a modest tidy Vietnamese sidewalk eatery at dusk, without showing the friends yet. Reference image 1, the plain plate of Nem Bui, is the approved dish texture: preserve its irregular curved strips, small thin slices and fine golden-beige toasted rice powder coating. Reference image 2, the real dish on a woven tray, supports the accompanying leaves only; do not copy its surrounding foods or woven tray. On a simple rectangular wooden table, place one off-white ceramic plate of Nem Bui in the center, fully visible with space around it. Behind it place one separate small plate of fresh la sung (Vietnamese fig leaves) and a small amount of la dinh lang (Polyscias fruticosa leafy sprigs); use recognizable broad oval fig leaves and slender serrated compound foliage, not generic mint or lettuce. Arrange two empty small ceramic receiving bowls at adjacent left and right near-side seating positions, each with one small separate bowl of red chili dipping sauce and one pair of wooden chopsticks lying neatly beside it. A single unbranded clear glass of water sits at the outer right edge for the right-side friend to reach, not blocking the central dish. Keep a clear path between the central plate and both receiving bowls. Show all essential tabletop objects within the frame, camera three-quarter overhead but wide enough to reveal the table and simple low stools, a softly blurred sidewalk and warm small-shop lighting behind. Believable natural food materials compatible with tactile stylized 3D characters later. No people, characters, hands, additional dishes, alcohol, branded bottles, signs, lettering or landmarks. Preserve the platform watermark.
```

Không dùng tên loài trong prompt làm bằng chứng leaf correctness; actual output cần riêng kiểm hình thái so tư liệu.

## Output và root QC

Asset: https://flow.google.com/u/1/project/9276788e-9781-44fb-ba5b-083006667374/edit/a40ef5d8-4465-47a5-a45e-6bd9444ca760 . Editor hiển thị đúng prompt/hai thành phần. Một lần submit, không chạy thêm.

- Download: `C:\Users\PC\Downloads\675d217d-87cc-4e2f-9462-8f73eb4fa66c.jpg`.
- Owner: `C:\Users\PC\Downloads\du_an_nem_bui\T-NB-01_v0.1.jpg`.
- Project: `media/raw/ep01_p6_food/T-NB-01_v0.1.jpg`.
- JPEG 768×1376, không tỉ lệ toán học9:16 dù UI chọn9:16. SHA256 `A259AF1B863F7DFD48B83DE5B78174FB0A31E812C892064555325E483DFAB830`.
- Proof `media/raw/ep01_p6_food/T-NB-01_flow-proof.png`, SHA256 `E0A2141BFFA1B63DC2602DB03EFD303CDA2D6B8DFE2D43FE9011275A0DC4BE6A`.

Đã mở file thật: có một đĩa nem trọn khung, đĩa lá riêng phía sau, hai bát nhận món, hai chén tương đỏ, hai đôi đũa và một cốc nước phải; bàn gỗ/quán vỉa hè ánh sáng ấm, chưa người/nhân vật. Nem giữ dạng sợi và lát phủ thính ở mức quan sát, không chủ động thay texture F05 đã chốt; continuity texture vẫn phải so kỹ khi dựng integrated frame.

Lỗi: bát trái crop, chén tương phải crop, cốc sát/crop mép phải; đũa phải chạy ra mép dưới. Background tự thêm menu có ảnh/chữ mặc dù yêu cầu không signs/lettering. Không xác định được brand, nhưng vẫn vi phạm brief nền sạch. Hai chỗ đặt bát nằm chéo gần/xa, chưa thể kết luận bố trí khớp hai bạn cạnh nhau khi chưa có thân/ghế. Lá rộng và tán hẹp có mặt nhưng leaf correctness chưa được xác minh độc lập; không ghi PASS chỉ vì có tên trong prompt. Chưa kiểm thao tác gắp/đưa bát/lấy cốc với nhân vật.

## Tổng hợp vòng và đề xuất

Đã xác định: bộ phục vụ71 được owner duyệt, T01 đã tạo và tải được; đủ nhóm props nhưng bố cục/nền chưa đạt. Chốt: giữ texture F05, script32, set quán nhỏ, không auto-approve output. Giả định: hai chén riêng và nước là thiết kế phục vụ project. Còn mở: framing đủ đồ, nền không chữ, xác minh lá và staging hai người, phần gắp, voice/motion. Tiếp theo đề xuất: sửa một lượt T02 với camera rộng hơn, mặt bàn đầy đủ và nền trơn không menu; kiểm lá riêng trước chốt food-table baseline. Chưa thực hiện T02, chưa ghép nhân vật/video hoặc đóng P6. Binary local; commit chỉ docs/metadata.
