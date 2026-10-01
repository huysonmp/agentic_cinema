# EP01 — Context ledger cho bàn ăn và khung hai nhân vật

2026-10-01. `ACTIVE_ROOT_PREFLIGHT / SOURCE_CONTEXT_ONLY / NOT_ASSET_APPROVAL`.

Ledger này gom dữ liệu đã chốt để maker và reviewer đối chiếu toàn tập. Không chứa prompt tạo ảnh, maker rationale hay kết luận QC. Không thay runtime contract hoặc lập một agent mới. Quyền hiện hành: sửa/thử ảnh trong Flow theo yêu cầu owner tiếp tục; không voice/video/release. Media output mới vẫn cần review và owner selection.

## Hồ sơ nguồn và trạng thái

| Input | Trạng thái / phạm vi |
|---|---|
| `32_p5-script-c-v0.5-approved-content.md` + approval33 | Nội dung C-v0.5 đã được owner duyệt; không sửa thoại, ý nghĩa hoặc thêm động tác ăn |
| `36_p5-v0.5-final-paper-reviews-and-cue-decision.md` + approval38 | Hai paper reviews đã hoàn tất; Q0 đã duyệt: F01 cùng nhận diện món, F02 cùng mạch mùi/rang gạo, nhãn AI bắt buộc. Root đọc đối soát36/38 trong continuation này; hiệu quả đọc/nhớ/nhịp vẫn media dependency |
| `45_p6-owner-v03-visual-baseline-approval.md` | Primary duo đã duyệt, không demo outfit/pose/quan hệ |
| `64_p6-input-decisions-approved-2026-10-01.md` | Quán nhỏ ven phố chiều tối; mood không khóa camera/bàn chi tiết; Canva do owner ghép |
| `68_p6-food-local-intake-and-owner-use-approval-2026-10-01.md` | Hai ảnh thật owner-authorized reference use; không independent commercial-rights clearance |
| `71_p6-food-texture-approval-and-street-table-brief-2026-10-01.md` + `72_p6-serving-approval-and-table-trial-2026-10-01.md` | F05 texture và bộ phục vụ được duyệt; vị trí/khoảng cách là functional staging cần kiểm trên ảnh, không tập quán duy nhất |
| Owner phản hồi trong chat | Rau/lá, đồ chấm, món và người phải nằm trong cùng bối cảnh dùng bữa; yêu cầu sửa và kiểm dữ liệu toàn tập, không sản xuất lẻ tẻ |

### Exact media references

- Primary: `media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg`, SHA256 `ECFBE7A3C543730C268A77CA08D508147115CA804154F85EBDBB38C5C601E8C7`.
- Food visual reference: `media/raw/ep01_p6_food/F-NB-05_v0.1.jpg`, SHA256 `C562A77D4A79D6A01E1518191796283810B6E40ADEF814A299B85960099C7E28`. Generated design reference, không fact proof.
- Real reference: `C:/Users/PC/Downloads/du_an_nem_bui/nembui.jpg`, SHA256 `A51303F7100EDD0944DC00DAA19402FECFE24BB0E15A4143DA8F8EAE7B9E3A2D`.
- Real reference: `C:/Users/PC/Downloads/du_an_nem_bui/z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg`, SHA256 `1237956E99458385F95F1EDF18E0A98E1BDDB777030AC1D69FAB05FA7A51D741`.

## Invariants và phần được điều chỉnh

**Giữ:** hai người bạn trưởng thành, Khoai trái/Đào phải trong khung; mặt/outfit theo primary; Khoai chín chắn hài kín, Đào cởi mở tự chủ; quán bình dân gọn gàng chiều tối; món Nem Bùi và bộ phục vụ gồm một đĩa món, đĩa lá sung + ít đinh lăng, hai chén tương ớt, hai bát nhận, hai đôi đũa gỗ, một cốc ngoài bên Đào. Không brand, landmark, romance hoặc trẻ em. Giữ watermark nền tảng.

**Điều chỉnh ở P6/P7:** camera axis/góc cao, kích thước bàn trong khung, ghế và vị trí các đồ vật để hành động dễ đọc. Bố trí cạnh gần trong draft bàn trống không phải invariant nội dung. Có thể đặt camera đối diện cạnh hai người đang ngồi để cùng thấy gương mặt và mặt bàn; vẫn cùng một cạnh dài, không đối diện nhau. Không tự biến thay đổi này thành owner-approved final framing.

Lá bày riêng là lựa chọn phục vụ đã duyệt; không có claim phải bày xa món. Bản có lá lót quanh đĩa món là biến thể appearance chưa được owner chọn, không mặc định canon. Không thêm cuốn lá/chấm/nhai để hợp một output.

## Đạo cụ → beat → tiêu chí kiểm

| Beat đã duyệt | Đầu vào chức năng / điều cần nhìn thấy |
|---|---|
| Khoai nhìn món, Đào định kéo đĩa | Đĩa món rõ, mép đĩa có vùng tay tới; không lá/chén chắn đường kéo về Đào |
| Khoai liên tưởng chảo mẹ rang gạo | Chỉ là ký ức hư cấu qua lời thoại; không thêm bếp/flashback, không nói mẹ làm Nem Bùi |
| Đào quay sang lấy cốc | Cốc ở ngoài phía Đào, không giữa hai người; không bị người/props che |
| Khoai đưa nem về miệng rồi khựng | Có vùng trống từ đĩa tới miệng Khoai; motion và grip phải probe bằng media riêng, still chưa chứng minh |
| Khoai đổi hướng, Đào đưa bát nhận | Hai vị trí cạnh nhau, bát Đào có thể cầm đưa ra; không đút, không thức ăn đã chạm miệng |
| Khoai đặt nem vào bát Đào, gắp miếng khác | Không thay đổi nguyên liệu/portion bằng prompt; object state và transfer cần kiểm video sau |
| Dùng bữa có món/lá/chấm | Đĩa lá sát vùng dùng chung, chén chấm là phần bữa ăn, không đồ trang trí xa tầm; không khẳng định một cách ăn là duy nhất |

## Fact và giới hạn hình ảnh

F01: Nem Bùi gắn với Bùi Xá, Bắc Ninh. F02: thính gạo rang góp một phần vào mùi vị. Ký ức/hài là fiction; không gán tập quán cả vùng. Không dùng một still để chứng minh nguyên liệu, công thức, vị ngon, xuất xứ đĩa hoặc species thật. Nhãn AI và fact text sẽ kiểm trên surface tương ứng, không thêm chữ vào style-frame này.

Food fidelity cần so actual F05 và ảnh thật: lát/mảnh phẳng xen dải mỏng cong, màu hồng-tan và vụn thính beige, không đĩa sợi tròn đồng đều. Lá rộng phải so silhouette với ảnh thật, không chốt species từ tên trong prompt; sprigs cần kiểm hình thái đủ đọc. Research-only references không được tự upload.

## Context check trước request — root/CTD hiện hành

1. Exact script, approvals và primary đúng phiên bản; input bị thiếu ghi rõ.
2. Mỗi đạo cụ có vai trò trong cùng scene; không tối ưu một vật làm hỏng beat khác.
3. Tách invariant với staging adjustable; thay meaning/canon/claim phải route owner.
4. Input Flow xác nhận bằng preview actual, không chỉ title. Phân biệt target, support và generated candidate.
5. Sau generation kiểm integrated image lại tất cả nhân vật/món/lá/chấm/bát/đũa/cốc/đường hành động. Cold reviewer trước, ledger sau.

Context ledger kiểm sự sẵn sàng của request, không bảo đảm output đạt. New-role proposal `agents/production_team/08_episode-context-gate-proposal-v01.md` vẫn PROPOSAL_ONLY.

## Run registration trước dispatch

| Run | Role / scope | Target | Output | Status trước dispatch |
|---|---|---|---|---|
| EP01-P6-R03R04-CONT-02 | AG-CONT-01 + AP / cold then context media review | T-NB-02C_v0.4 và T-NB-03_v0.1 | agents/visual_experiments/18_integrated-table-staging-review-v01.md | COMPLETED; outcome xem riêng run-log04 sau cold |
| EP01-P6-R03R04-FOOD-02 | independent food/leaf fidelity reviewer / cold then reference | Hai target như trên | agents/visual_experiments/19_integrated-table-food-review-v01.md | COMPLETED; outcome xem riêng run-log04 sau cold |
| EP01-P6-CONTEXT-CTD-01 | AG-CTD-01 / paper preflight, camera/table alternatives | Exact source ledger75 + script32/primary45/serving71–72 | agents/production_team/09_episode-context-preflight-ep01-v01.md | COMPLETED; paper scope, không output approval |

Report18/19 cold records đã lưu trước source comparison. Sau cold, full72 vô tình lộ prompt/root QC lịch sử T01; hai reviewer đã disclosure và loại khỏi evidence, không gọi toàn run pristine independent. Các lượt sau cấp ledger/approval-only, không full72. Ledger75 là source-only briefing; báo cáo outcome đọc sau cold, không gửi maker QC cho reviewer.

Không ghi run completed khi chưa có actual report. Reviewer không có quyền Flow/upload/generation/Git/asset approval. Same model contexts không là audience thực.
