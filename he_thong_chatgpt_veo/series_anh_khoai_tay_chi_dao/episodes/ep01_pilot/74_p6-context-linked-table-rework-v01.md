# P6 — Sửa bàn ăn theo bối cảnh toàn tập

2026-10-01. Owner yêu cầu sửa tiếp, phản biện việc rau/lá bị tách xa và sản xuất từng phần không nối bối cảnh. Authority: sửa image trong Flow project hiện hành; không đổi script, primary, voice/video hoặc release. Không owner-approved output mới.

## Context preflight — actual root read trước generation

Đã đọc toàn bộ: script32; approvals/direction45,64; reference use68; serving71–72; PROD7 common contract02 và role prompts03; VE runtime02. Root mở actual C/F05/nembui bằng view_image. Giữ findings13–15 từ batch73.

Đối soát sửa lời: đĩa lá riêng có trong71 và bộ phục vụ72 đã được duyệt. Vị trí phía sau là functional draft, không bắt buộc giữ khi ảnh actual không phục vụ scene. Không có source/claim rằng lá phải được phục vụ riêng hoặc xa món. Owner phản biện vị trí; sửa placement trong cùng bộ phục vụ, không xóa lá/chấm.

| Script/context | Hệ quả thiết kế đầu vào và kiểm sau |
|---|---|
| Hai người bạn trưởng thành, Khoai trái/Đào phải, quán nhỏ ven phố chiều tối | Bàn cho hai vị trí cạnh nhau; không romance hoặc set nhà hàng sang; no people trong lượt bàn trống này |
| Đào định kéo đĩa nem | Đĩa nem có vùng trống tới vị trí phải; lá/chén không chắn đường; bàn trống chỉ kiểm bố trí dự kiến |
| Đào quay sang lấy cốc | Một cốc ngoài phải bộ phục vụ phải; không giữa hai người |
| Khoai gắp nem về miệng, đổi hướng trước contact, Đào đưa bát nhận | Không props/đĩa lá chắn hành lang giữa món và hai bát; không thêm cuốn lá/nhai/đút |
| Món/lá/chấm là cùng một bữa ăn | Đĩa lá sát đĩa nem ở vùng dùng chung, không xa sau như decor; hai chén chấm vẫn cạnh bát; leafy accompaniments cần reference morphology |
| Approval F05, refs68, findings13 | Giữ primary texture; sửa drift table output về dải/lát phẳng mỏng; broad leaves elongated non-lobed, không common-fig lobes; sprigs không gắn species PASS từ prompt |

## Request TABLE-CONTEXT-R01 — pre-execution

Edit target C_v0.1 Flow55cc8bc8-fecf-4183-a506-f05fc62c940c. Three supporting components selected in editor: F05, nembui.jpg, owner-authorized mẹt longfilename68. No new upload/research-only asset. Latest UI editor: Nano Banana Pro /9:16 /0credits, no output-count control exposed in editor. One edit submit intended; reconcile actual outputs, no blind resubmit. UI price không billing ledger.

Đây là combined context rework (placement+leaf+food), không L01/F01 one-factor experiment; không suy nhân quả từ kết quả. Hai proposed isolated tests15 giữ NOT_RUN, không gọi lượt này là đã hoàn tất chúng.

```text
Edit the current empty table image for a scene of two adult friends eating together at a tidy modest Vietnamese sidewalk eatery at dusk. Keep the wooden table, stools, right-side street opening, warm lamp, camera and platform watermark. This is a shared meal, not a display of disconnected props. The left place is for Khoai and the right place is for Dao, seated next to each other along the near edge. Keep exactly two empty receiving bowls, two separate small red chili dipping bowls, two pairs of wooden chopsticks and one unbranded water glass outside the right-hand place. Keep all serving items inside the image.
Move the small accompanying-leaf plate CLOSE beside the central Nem Bui plate, just beyond its left-back rim with a narrow gap, in the same shared reachable serving area, not isolated far behind. Leave clear space from the Nem plate toward the right bowl for Dao to pull the dish and later offer her bowl; keep the leaves and sauces out of that path. Do not add hands, people, wrapped portions or a new eating action.
Correct both the broad leaves and the food while retaining the meal context. The added plain Nem plate reference is the approved food texture: irregular THIN FLAT curved ribbons mixed with small flat pink-tan slices and fine golden-beige rice powder, not uniform round rope-like noodles or fried sticks. Use the added real nembui.jpg for the broad Vietnamese sung leaf silhouette: whole elongated oval/elliptic blades, pointed tips, continuous unlobed edges and visible central veins. No deep lobes, maple-like or common Mediterranean fig leaves. Use the added real woven-tray photo only for the few narrow branching serrated dinh lang sprigs accompanying those broad leaves, not its basket, other foods or rolled portions. Make the leaf shapes readable at this table scale. Keep the existing central plate, prop count, bowl positions, water-glass side and simple unbranded surroundings. No extra dishes, signs, menus, writing, branded bottles or alcohol. Preserve the platform watermark.
```

Acceptance: source-linked leaf/food fidelity + same shared reachable service area + script-linked prop paths/count; no approval by prompt. Need independent actual review; character reach/temporal action NOT_TESTED until composite/video.

## Agent/system đề xuất — chưa thêm role mới

CTD đã có trách nhiệm bảo toàn ý nghĩa; ART đã có script/style/shot needs; PROMPT đã có traceability. Lỗi hiện tại là orchestration thiếu context preflight và reviewers được scope nhỏ, không phải chưa có role name. Root chịu trách nhiệm check episode context trước dispatch/generation.

Đề xuất thêm mandatory context ledger vào envelope: exact script+approval, canon/refs+status, source/use constraints, prop→beat mapping, invariants versus adjustable staging, findings phụ thuộc, downstream impact. CTD/context paper review trước maker request; reviewers cold trước rồi nhận ledger để đối chiếu, không đọc maker rationale. Có thiếu/mâu thuẫn trọng yếu → HOLD prompt. Đây là đề xuất bổ sung vận hành, không claim agent mới implemented/tested; chưa thay contracts ngầm.

## Kết quả

R01 SUBMITTED_ONCE / ONE_HISTORY_OUTPUT / DOWNLOADED / ROOT_REWORK. File T-NB-02C_v0.2.jpg được tải cả từ big editor và trực tiếp history output, hai đường trả cùng filenamebase. Download a74d6ea5-bb82-4bab-99ea-2655b1e377dd.jpg; SHA2565C6EA8558FAD463874AE42F73F672F9743FE73F24E9B0D856459D9EC5DE19C3B. Bản owner Downloads/du_an_nem_bui và project media/raw/ep01_p6_food. Asset editor55cc8bc8 vẫn giữ cùng ID, có history mới với prompt và bốn components (target+three supports); không giả newassetID. Root actual view: lá vẫn có thùy, vị trí và texture gần như control; chưa sửa thành công. Không kết luận exact pixel identity từ hash khác. Proof T-NB-02C_v0.2_flow-proof.png. Hai agent16/17 đã nhận exact path trước review; maker74 forbidden cho họ.

### R02 preflight — sửa nhỏ có nối context

Một edit tiếp trên editor/current table, chỉ nembui.jpg component hỗ trợ; Nano Banana Pro/9:16, same UI0credit setting observed R01, no count control. Không retry unchangedprompt. Thay chiến lược: Vietnamese concise leaf/placement-only, không food retexture hoặc đổi scene. L01/F01 của15 vẫn không gọi executed exact protocol. Nếu còn không đổi, HOLD và kiểm edit/input binding, không submit mù.

```text
Chỉ sửa đĩa lá ăn kèm trong ảnh bàn ăn hiện tại. Đây là bữa ăn chung của Khoai và Đào tại quán nhỏ ven phố, không phải bàn trưng bày: kéo đĩa lá sát cạnh trái của đĩa nem, hai mép đĩa gần nhau, vẫn chừa đường kéo đĩa nem về bát bên phải và đường đưa bát nhận món. Thay toàn bộ lá to xẻ thùy bằng lá sung nguyên bản giống ảnh nembui.jpg được đính kèm: lá đơn dài hình bầu dục, đầu nhọn, mép liền không xẻ thùy, gân giữa rõ. Giữ một ít nhánh đinh lăng hiện có trên cùng đĩa lá. Không dùng lá sung phương Tây hình bàn tay, không lá phong. Giữ nguyên nem, hai bát, hai chén tương ớt, hai đôi đũa gỗ, cốc nước ngoài phải, bàn ghế, góc máy, ánh đèn và nền phố. Không thêm nhân vật, tay, món phụ, chữ hoặc động tác cuốn/chấm mới. Giữ watermark của nền tảng.
```

R02 SUBMITTED_ONCE / ONE_HISTORY_OUTPUT / DOWNLOADED. T-NB-02C_v0.3.jpg owner/project folders như R01; download1af7f98f-073c-4907-99f2-73a7fd3a38ac.jpg, SHA256D6DFC4FA16F88950706F4BB7B73112EEE487B2B86ECBB1A263A88398A779C774. Same asset editor history, no newassetID claimed. Actual root view: rear broad leaves đã đổi sang không thùy; model thêm vòng lá quanh đĩa nem, không kéo đĩa lá phía sau sát theo yêu cầu. Texture nem vẫn rope-like như control (R02 chủ ý không sửa nem). Props count/background/watermark giữ ở scope still. Không auto-approve, không gọi movement/whole-meal gate PASS. Hai reviewers nhận exact v0.3 để append review sau cold; không generation tiếp khi chưa đối soát. Proof T-NB-02C_v0.3_flow-proof.png và T-NB-02C_v0.3_editor-proof.png.

Agent context đề xuất chi tiết: agents/production_team/08_episode-context-gate-proposal-v01.md. Root đã thực hiện context preflight ở vòng này; chưa claim runtime agent mới đã xây/test/approved.

## R03 — scoped food-texture edit

R03 dùng current table revision sau R02 và thêm F05 texture reference; prompt chỉ đổi món trung tâm, giữ lá/bối cảnh/props/action context. Flow history output `fe588365-c66b-42d8-ab05-dc6906474f74`; downloaded `fe588365-c66b-42d8-ab05-dc6906474f74.jpg`; owner/project `T-NB-02C_v0.4.jpg`; SHA256 `87CAF331A65AEE0FECFAF6C540E8C743B4C7F8922915FA6A0144A131FF4B11DD`. JPEG768×1376. Proof `T-NB-02C_v0.4_flow-proof.png` đã lưu.

Root visual QC only (independent agent quota unavailable at this point): central mound reads more heterogeneous than v0.3, with visible pink-tan flat pieces and fine curls, but some thick curls remain. This is a bounded improvement, not proof of documentary recipe or final texture fidelity. Leaf ring/plate, two bowls, two red sauces, two chopstick pairs, water outside right, stools/background and watermark remain visible. The leaf-lined central plate makes the serving appearance a deliberate variation; its rim and a separate rear leaf plate remain readable enough for integrated blocking, but owner gate stays open. R03 status: `KEEP_AS_PROVISIONAL_INTEGRATION_BASE / FOOD_REVIEW_PENDING / P6_NOT_CLOSED`.

No independent R03 reviewer report was completed because delegated contexts hit the Codex usage limit after R02. This root QC is explicitly not independent review; rerun specialist review when quota is available before final asset approval. Do not represent R03 as P6 PASS.

### R03 exact prompt — bổ sung từ history UI đã đối soát

```text
Chỉ chỉnh món Nem Bùi trên đĩa trung tâm trong ảnh bàn ăn hiện tại. Giữ nguyên bối cảnh quán nhỏ ven phố, góc máy, bàn ghế, đĩa lá ăn kèm, hai bát nhận món, hai chén tương ớt, hai đôi đũa, cốc nước ngoài bên phải, ánh đèn và watermark. Không thêm người, tay, món phụ, chữ hay động tác mới. Dùng ảnh texture Nem Bùi được đính kèm làm chuẩn: món phải là hỗn hợp không đều của các lát thịt màu hồng nâu nhạt và các dải/sợi mỏng dẹt cong, phủ vụn thính gạo vàng-beige mịn. Giảm mạnh các sợi tròn giống mì hoặc dây; không để cả đĩa thành các que tròn cùng độ dày. Giữ vài dải cong mảnh xen kẽ lát phẳng, bề mặt vụn thính tự nhiên, không chiên giòn, không biến thành mì hoặc đồ chiên. Giữ món nằm gọn trong đĩa, không làm lá lót quanh món biến mất và không che kín hoàn toàn mép đĩa. Đây là chỉnh texture món để dùng cho cảnh Khoai gắp một miếng rời về phía miệng rồi đổi hướng vào bát Đào; không tạo tay hay miếng đang gắp ở lượt này.
```

2026-10-01 re-observation correction: vài mảnh phẳng có mặt nhưng vẫn nhiều sợi/cuộn dày. Nhận xét “bounded improvement” phía trên là root qualitative impression, không finding closure; không promote texture chỉ từ khác biệt nhỏ.

## R04 — integrated still / kết quả đối soát hồi cứu

Một submit đã diễn ra sau R03, cùng editor55cc8bc8, target current table + component title `Editing 3D animated duo image`. Title riêng không chứng minh primary45; preview/component identity phải đối chiếu trước run tiếp. Nano Banana Pro/9:16/0 credit UI quan sát khi submit; không billing inference. Chưa đăng ký R04 đầy đủ trước submit là thiếu sót log; phần này ghi hồi cứu từ UI history, không giả pre-registration.

```text
Ghép hai nhân vật adult friends vào chính bối cảnh bàn ăn hiện tại, giữ nguyên toàn bộ quán ven phố, bàn, lá, đĩa Nem Bùi, hai bát, hai chén tương ớt, hai đôi đũa, cốc nước và watermark. Dùng ảnh bộ đôi được đính kèm chỉ để giữ đúng gương mặt, tạo hình và trang phục đã duyệt: Khoai bên trái, Đào bên phải, ngồi cạnh nhau cùng một cạnh gần của bàn, không phải người yêu và không tạo dáng chụp ảnh. Giữ tỷ lệ nhân vật stylized 3D trưởng thành, không trẻ em, không thay trang phục. Khoai hơi nghiêng chú ý về đĩa nem với vẻ kén chọn nhưng hài hước kín đáo; Đào cởi mở, tự nhiên, tay gần cốc nước bên ngoài phải như chuẩn bị quay sang lấy cốc. Hai nhân vật nhìn và ngồi đúng phối cảnh bàn, không che đĩa nem, bát phải, chén chấm hoặc khoảng trống gắp món. Không cầm đũa, không gắp thức ăn, không thêm thoại hay hành động mới ở lượt style-frame này. Không đổi món, không thêm món phụ, không chữ/biển hiệu/logo.
```

Lịch sử editor có 5 output images đúng thứ tự control/R01/R02/R03/R04; R04 terminal image, không pending. Click history mới rồi download big editor: `00730938-ab12-4ed5-b9b3-9a6af5fb2fee.jpg`; native displayed media 768×1376, saved `T-NB-03_v0.1.jpg`, SHA256 `51B6806F839A216F818DAC192839EBCACAD5935C89CBA2E1C1628AA20479D45B`. Cả owner Downloads và project raw đã copy; proof `T-NB-03_v0.1_flow-proof.png`. Thumbnail download trả webp, không được nhầm là native media; native JPG là target review.

Root actual observation: Khoai ở cạnh trái/gần, Đào ở cạnh xa/phải, không cùng một cạnh dài; một bát rõ ở tiền cảnh, hai chén thấy với chén trái một phần, một đôi đũa rõ và phần đũa trái bị che. Đĩa lá vẫn ở sau món, texture còn sợi dày; giữ watermark. Không gọi bị che là đồ vật đã biến mất. `ROOT_REWORK / INDEPENDENT_REVIEW_REGISTERED / NOT_OWNER_APPROVED`. Không dùng still để chứng minh grip, reach hay motion payoff.

Context ledger cho run tiếp: `75_p6-episode-context-ledger-v01.md`. Camera/cạnh gần draft cần đổi để cùng thấy mặt và bàn nhưng giữ hai người ngồi cạnh nhau; không thay script. Reviewer cold chỉ nhận exact media; ledger/ref sau cold, không file74.
