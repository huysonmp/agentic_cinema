# EP01 — Brief thay ụ nem trong frame tích hợp

2026-10-01 (Asia/Saigon). Run `EP01-P6-ART-TEXTURE-01`; role `AG-ART-01` hiện hành; stage `P6`; mode `PAPER_PROPOSAL`.

Disposition: `PROPOSAL_COMPLETE / FOOD_MOUND_ONLY`. Đề xuất dùng actual F-NB-05_v0.1 làm nguồn hỗ trợ để thay phần nem trong frame tích hợp. Không thay F05, không sửa recipe/canon, không final media review, không asset approval hoặc generation-ready.

## 1. Envelope và quyền

- Task được giao: so actual approved F05 với hai ảnh thật68 và T-NB-03_v0.2/v0.3; viết một exact Vietnamese edit prompt ngắn chỉ thay ụ nem, cùng một focused test và stop rule.
- Output duy nhất: `agents/production_team/10_integrated-food-repair-brief-v01.md` v0.1.
- Đã đọc toàn bộ common contract02 và section AG-ART-01 của role prompts03; không dùng role mới.
- Authority: root giao maker/adviser paper scope; source71:7–11 giữ approval F05; source68:3,20 cho hai ảnh thật owner-authorized reference use; ledger75 là context, không asset approval.
- Không Flow, upload, generation, media editing, Git hoặc release. Không đọc maker76, reports18/19. Source ledger75 có status summaries của run khác; các dòng status đó không dùng làm evidence đánh giá hình món trong brief này.
- Tools dùng: đọc file local; `view_image` actual ở detail original; hash/bytes/dimensions/decode local. Không account UI, không audio/video. Không cần botany research vì task không đổi hoặc xác định species lá.
- Root xử lý prop count riêng. Brief này bảo toàn số lượng đồ vật của exact edit target; không âm thầm sửa count/background qua food prompt.

## 2. Inputs thực đọc

Documents: `episodes/ep01_pilot/75_p6-episode-context-ledger-v01.md`, `71_p6-food-texture-approval-and-street-table-brief-2026-10-01.md`, `68_p6-food-local-intake-and-owner-use-approval-2026-10-01.md`. Source spans sử dụng ở phần3–4. Runtime documents02/03 chỉ là instructions.

| Actual media đã mở | Dimensions / bytes | SHA256 kiểm trên file trong run | Vai trò |
|---|---|---|---|
| `media/raw/ep01_p6_food/F-NB-05_v0.1.jpg` | 768×1376 / 159684 | `C562A77D4A79D6A01E1518191796283810B6E40ADEF814A299B85960099C7E28` | Approved generated design/texture reference; hash khớp source71:9 và ledger75:21 |
| `C:/Users/PC/Downloads/du_an_nem_bui/nembui.jpg` | 1920×1367 / 492138 | `A51303F7100EDD0944DC00DAA19402FECFE24BB0E15A4143DA8F8EAE7B9E3A2D` | Authorized real appearance reference; hash khớp source68:10 |
| `C:/Users/PC/Downloads/du_an_nem_bui/z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg` | 980×739 / 227642 | `1237956E99458385F95F1EDF18E0A98E1BDDB777030AC1D69FAB05FA7A51D741` | Authorized real appearance reference; hash khớp source68:16 |
| `media/raw/ep01_p6_food/T-NB-03_v0.2.jpg` | 768×1376 / 147495 | `EA82375A3B6261DF4A97D87A01D3346C96AFA194534D59F4D0C354E7B655175F` | Integrated comparison target, không approved food source |
| `media/raw/ep01_p6_food/T-NB-03_v0.3.jpg` | 768×1376 / 152648 | `1773E60ECEB06312F969734DFC4A2F2B5809964E698F2F2EFDE35C6356ADC102` | Latest target được giao quan sát, không final selection của adviser |

Model, actual supporting-component capacity, masking/edit behavior, account settings, current cost, available cap và exact operator request approval: `UNKNOWN / NOT_TESTED` trong paper run. Không suy từ trial cũ. Nếu root dùng target mới sau sửa props, phải ghi exact target version/hash và xem lại actual target đó trước edit; brief không tự xác nhận target chưa được giao.

## 3. Appearance ledger — observation vs fact

| Appearance | Phân loại | Evidence / giới hạn |
|---|---|---|
| F05 có dải mỏng cong và dẹt, nhiều mặt bản thấy được; xen lát/mảnh phẳng không đều, hồng-tan/nâu nhẹ; vụn beige bám nhám trên các bề mặt | VERIFIED_AS_PIXELS / approved FICTION_STYLE reference | Actual F05, ụ nem ở trung tâm. Source71:9 giữ exact texture; không yêu cầu mọi miếng có cùng shape/độ phủ |
| Hai ảnh thật cũng có mix dải cong/mảnh-lát không đều và bề mặt vụn bột; ảnh mẹt có nhiều phần cuộn cong và màu vàng hơn ảnh đĩa | VERIFIED_AS_PIXELS | Actual hai ảnh68. Đây là appearance support, không recipe/ingredient analysis hoặc duy nhất một cách trình bày |
| T03v02/v03 có nhiều đoạn vàng ngắn, khá tròn/que hoặc thẳng, xen một số lát hồng lớn có mặt trơn dễ nổi bật | VERIFIED_AS_PIXELS / target observation | Actual ụ nem trung tâm ở cả hai version. Mô tả local geometry; không suy món/đĩa thực là sai xuất xứ |
| Khi xuống kích thước integrated frame, powder/ribbon geometry có thể bị giản lược thành round sticks hoặc pink slabs | HYPOTHESIS / UNTESTED mechanism | Quan sát hiện tượng khác F05 không chứng minh nguyên nhân là scale/model/prompt/reference weighting; cần test output thực |
| Species lá, công thức, nguyên liệu cụ thể, hương vị và nguồn gốc đĩa | UNKNOWN / ngoài task | Ledger75:47–49 và ART EP01 boundary: ảnh không chứng minh các fact này |

F05 cũng có lát/mảnh hồng-tan; không ban mọi lát hồng hoặc bắt model biến toàn bộ ụ thành một loại ribbon. Repair là giữ exact mix, surfaces và variation của approved F05 khi đưa vào scene, không thiết kế shape/recipe mới. “Vụn bột” trong prompt là mô tả bề mặt thấy được; không dùng still làm bằng chứng fact thính nằm ngoài mọi phần món.

## 4. Sai lệch cần xử lý và phạm vi phải giữ

Food geometry ở T03v02/v03 chưa đọc giống approved F05 tại phần nem: target ưu thế đoạn vàng kiểu que/tròn/thẳng, còn F05 có nhiều dải dẹt cong, mặt phẳng của lát không đều và coating nhám. Đây là căn cứ lập repair proposal; không phải disposition final của integrated assets.

Source71:40 yêu cầu giữ F05, không biến thành sợi mì/nem chua/roll; ledger75:49 nêu mix lát/mảnh phẳng xen dải mỏng cong, hồng-tan và vụn beige. Target phải lấy **mound content** từ F05, áp vào plate hiện có với cùng footprint/volume projected và perspective. Không copy đĩa trắng full-frame, nền studio hoặc bố cục close-up của F05. Không thay lượng/portion để giải chi tiết bị nhỏ.

Invariants của edit này: plate/rim hiện có, vị trí món, hai nhân vật và hands, các lá, mọi props/số lượng hiện có, cốc, camera/crop, scene/background, ánh sáng và watermark. Không gộp xóa/thêm bát/chén/đũa, dọn background, đổi lá, sửa outfit hoặc action vào request food.

Giữ số lượng của exact target chỉ là edit boundary. Nó không xác nhận số lượng đó đã đạt serving ledger75:27; root vẫn phải xử lý/check count riêng trước final integrated selection.

## 5. Phương pháp và dependencies

| Input / lựa chọn | Vai trò | Trade-off / gate |
|---|---|---|
| Exact integrated image root chỉ định | **Edit target**: toàn frame giữ nguyên, chỉ vùng ụ nem thay | Target phải actual-preview đúng version; nếu props branch đổi version cần root re-read target, không trộn hashes |
| Actual F-NB-05_v0.1 | **Supporting composite source**, chỉ phần nem | Đề xuất chính: có approved geometry/texture thật để chuyển vào scene. Nguy cơ model copy đĩa/nền/camera của F05 hoặc thay portion; phải kiểm preservation |
| Hai ảnh thật68 | Comparison evidence trong brief/test | Đã owner-authorized nhưng không cần thêm làm ingredient trong focused request này. Không lấy arrangement lá/ớt/mẹt/món ngoài ảnh để thay source F05 |
| Text-only mô tả texture | Alternative paper, không thêm request/test | Ít dependency hơn nhưng model có thể tiếp tục render round sticks/pink slabs. Không chọn làm request đề xuất khi actual approved F05 sẵn có |

Không tự hứa local edit/mask/composite capability. Root/Flow phải xác nhận actual editor hỗ trợ target + F05 component đúng scope; nếu không có input method đó, dừng và ghi thiếu capability thay vì gọi output tương đương F05 từ mô tả. Không sửa hoặc ghi đè file F05.

Rights/source mapping: F05 là generated design ref đã owner duyệt texture theo source71, không fact proof; hai ảnh68 có owner-authorized reference use, không independent commercial-rights clearance. Không research-only uploads. Task không đòi mở rộng authority hoặc xin lại approval texture F05; next tool request vẫn theo quyền root thực có.

## 6. Exact Vietnamese edit prompt v0.1

Prompt này đi cùng actual target + actual F05 supporting component, không đi cùng full-scene generation request.

```text
Chỉ thay ụ nem trên đĩa giữa bàn bằng phần nem từ ảnh tham chiếu F-NB-05_v0.1. Giữ đúng hỗn hợp dải mỏng dẹt cong xen lát/mảnh phẳng không đều, màu vàng-be và hồng-tan cùng lớp vụn bột nhám như F05, ở đúng kích thước và phối cảnh ụ nem hiện tại. Giữ nguyên đĩa, hai nhân vật, lá, mọi đạo cụ và số lượng, cốc, bối cảnh, camera, ánh sáng và watermark; không chép đĩa hoặc nền của F05.
```

Không có yêu cầu đổi recipe, slice shapes của F05, sửa count/background hoặc thêm eating action. Prompt là đề xuất paper, không quyền submit hoặc cam kết output giữ toàn bộ invariants.

## 7. Một focused test, acceptance và stop

**Câu hỏi:** một mound-only edit có giữ được approved F05 mix dải dẹt cong/lát không đều/coating nhám ở kích thước integrated frame, đồng thời giữ các vùng còn lại của target không?

**Test đề xuất:** một edit request với exact target root chọn và F05 supporting source; một candidate nếu count/credit/settings đã được root xác minh và quyền hiện có bao phủ. Request/model/count/cap không do adviser cấp: `PENDING_ROOT_VERIFICATION`. Không one-factor causal claim về model/prompt/reference weighting; đây là kiểm kết quả đạt brief hay không.

**Acceptance cho riêng repair: all required, không bù bằng điểm đẹp.**

1. Trong full-frame ở kích thước xem integrated hiện hành, ụ nem còn đọc được mix dải có mặt dẹt/cong xen lát không đều như F05; không ưu thế round straight sticks hoặc pink slabs trơn. Kiểm local region ở độ phân giải actual để xác định mặt bản/coating, rồi trở lại full-frame; zoom lớn một mình không đủ chứng minh readable ở scale scene.
2. Mix màu và powder-like surface giữ direction F05; không biến thành glossy/smooth food hoặc uniformly powder-only mass. Có lát hồng-tan hợp F05 là đúng hướng, không loại bỏ để đạt một texture đơn nhất.
3. Mound giữ vị trí, projected footprint/portion và perspective trên plate hiện có; plate/rim không bị thay bằng plate F05; không chuyển camera/crop hoặc lighting của toàn ảnh sang F05.
4. Frame ngoài mound bảo toàn nhân vật/hands, leaves, props/số lượng, cup, background, ánh sáng và watermark so exact target trước edit. Food succeeded nhưng region khác đổi vẫn fail bounded repair; chưa whole-asset pass.

**Stop:** không submit thêm tự động. Nếu candidate vẫn dominant sticks/smooth slices, không đủ đọc ở integrated scale, thay portion/plate hoặc drift ngoài mound: lưu exact output/version/hash, stop, route root/PROMPT/ART phân tích; không “sửa thêm vài lần”, regenerate full scene hoặc đổi F05 shape để cứu target. Nếu đạt riêng repair: chuyển independent food/CONT review và owner selection; adviser không tự asset-pass. Prop-count/background branches và các gates khác còn riêng.

## 8. Coverage / findings / closure

| Rule ID | Status / severity | Artifact / evidence | Impact và action / route | Owner gate / closure evidence |
|---|---|---|---|---|
| ART-1 — food evidence | MET trong proposal | Actual F05 và hai ảnh68; hashes phần2; source71:9 | Đủ appearance evidence để viết brief; dùng F05 làm primary design source | Không mở lại approval F05; closure output vẫn cần actual comparison |
| ART-2 — geometry fidelity | DEFECT target observation / MAJOR | T03v02/v03 actual mound vs F05 actual; ledger75:49 | Local geometry khác primary; đề xuất mound replacement / P6 ART + PROMPT | Exact new candidate + actual F05 comparison ở local và full-frame; owner chọn asset riêng |
| ART-2 — integrated readability | UNKNOWN / MAJOR | Chưa có output của prompt phần6 | Không biết geometry/powder còn đọc sau edit hay không | Một focused output có version/hash và evidence cả full-frame/local; không quyết từ prompt |
| ART-3 — prop/screen geography | MET về edit boundary; output UNKNOWN | Prompt giữ target ngoài mound; source71:28 và ledger75:27 | Không lẫn count/background repair; CONT kiểm drift ngoài vùng / P6 | Closure exact before/after preservation; không nhận xét serving count đạt |
| ART-4 — rights | MET authorization classification; clearance UNKNOWN | Source68:3,20,29–30; source71:50 | Không dùng research-only; không biến authorization thành commercial clearance / RIGHTS | Tool request theo authority root; release/clearance riêng, không phát sinh approval mới ở adviser |
| ART-5 — không claim mới | MET trên paper | Appearance ledger và prompt mô tả pixels; ledger75:47 | Không bịa recipe/ingredient/place/health hoặc cách dùng duy nhất | Giữ dialogue/fact/canon; nếu muốn đổi chúng route P2/P5/owner |
| ART-TOOL — actual method/readiness | UNKNOWN / MAJOR | Không account/settings/cost/cap read-back trong run | Không gọi prompt này generate-ready / FLOW + PROMPT | Actual input preview + request/settings/count/cap/authority đúng scope trước submit |
| ART-MOTION/AUDIO | N/A | Task still geometry only | Không grip, eating transfer, timing hoặc audio verdict | Các media gates tương ứng kiểm riêng khi có quyền |

## 9. Handoff và run record

- Đã xác định: actual F05 có approved varied flat/curved geometry và powder-like surface; T03v02/v03 vẫn ưu thế sticks/pink smooth slices ở phần món.
- Quyết định đã có: giữ exact F05; sửa mound thôi; root xử lý props riêng. Brief không tạo asset approval.
- Giả định làm việc: editor có thể nhận exact target + F05 supporting source; portion và projected mound boundary giữ nguyên. Feature/method chưa được adviser kiểm account.
- Còn mở: actual next target nếu root sửa props trước, input method, settings/cost/count/cap, outcome repair và independent output checks.
- Next: root tạo reviewable exact edit request với prompt phần6, xác minh actual target/support và quyền trước submit; thử một focused candidate; stop/read-back theo phần7; independent review + owner selection sau đó.

| Run | Role / stage / mode | Access thực | Output / disposition | Owner decision mới | Next route |
|---|---|---|---|---|---|
| EP01-P6-ART-TEXTURE-01 | AG-ART-01 / P6 / PAPER_PROPOSAL | Common02 + role03; source75/71/68; F05/two real refs/T03v02/v03 actual | `10_integrated-food-repair-brief-v01.md` / PROPOSAL_COMPLETE — mound-only | None | Root/PROMPT/FLOW request verification; focused edit nếu authorized; ART/CONT independent review; owner selection |

Change log v0.1: tạo bounded repair brief, exact Vietnamese prompt, source/target role mapping và một focused test/stop. Không chỉnh input/media, không Flow/upload/generation/Git, không final media hoặc asset pass.

## 10. Addendum — EP01-P6-ART-TEXTURE-02: R09 analysis và next-test alternatives

Ngày 2026-10-01. Existing role `AG-ART-01`, stage P6; dispatch label `PAPER_ANALYSIS`, thực hiện bounded paper maker analysis/next proposal theo common02. Không lập runtime role/mode implementation mới. Prior proposal phần1–9 được giữ nguyên làm lịch sử; addendum này không sửa approval F05 hoặc tự đóng findings bằng prompt.

**Latest disposition:** `PROPOSAL_COMPLETE / R09_FOOD_GEOMETRY_UNRESOLVED / NO_NEW_TEST_RUN_BY_ADVISER`. Root đã chạy một focused edit theo phần6 và dừng test đó. Phân tích này đề xuất tối đa hai đường thử khác nhau, không cấp quyền retry hoặc tự chọn final asset.

### 10.1 Inputs/access và actual request record

| Input mới thực mở | Dimensions / bytes | SHA256 kiểm lại trên bytes | Vai trò |
|---|---|---|---|
| F-NB-05_v0.1.jpg | 768×1376 / 159684 | `C562A77D4A79D6A01E1518191796283810B6E40ADEF814A299B85960099C7E28` | Actual approved geometry/texture reference, vẫn giữ nguyên |
| R08 — T-NB-03_v0.5.jpg | 768×1376 / 153196 | `4F98035619D5453A6BC737657F4468A29D280B417F5DB916C55ED2371C7ED360` | Before của focused edit |
| R09 — T-NB-03_v0.6.jpg | 768×1376 / 147160 | `F631378EE97B74027A69FA900D9F1FC31B194F2E946E712809275507C5B68FFF` | After; current native full frame theo root |

Đã đọc own proposal10; source75 context; source71/68 vẫn là approval/intake inputs đã đọc ở run trước. Maker được mở **exact R09 input/prompt record** tại source76:116–128, không đọc reviewer18/19. Đây là maker analysis có intent/request context, không cold independent media review. Không lấy root QC heading hoặc các report khác làm căn cứ cho quan sát geometry dưới đây.

Source76:118–120 ghi R08 làm target editor, đúng **một** supporting F05 component đã actual-preview; không thêm primary hoặc hai ảnh thật. Nano Banana Pro / portrait9:16 / UI estimate0 là recorded settings của R09, không xác nhận billing, model reference weighting hoặc settings của lượt sau. Source76:125 khớp exact prompt phần6; source76:128 khớp focused test/stop brief. Dispatch ghi một submit/output, không mask drawn.

Root capability update (`ROOT_REPORTED`, adviser không vào UI): history hiển thị hai components gồm implicit target + F05 support; crop control chỉ thấy aspect presets16:9/9:16/1:1/free và Apply/Cancel; root Cancel, không apply. Không mask/inpaint/region-selection control nào được quan sát. Vì vậy các phương án dưới dùng full-frame natural-language edit hoặc new image composition, **không đòi mask, crop ra ingredient, cutout hoặc Python/local manipulation**. Không biết provider hidden arguments/weighting; crop UI không là bằng chứng local replacement capability.

### 10.2 Quan sát và giới hạn kết luận

Ở central mound, cả R08 và R09 vẫn có nhiều đoạn vàng ngắn dạng que/khá tròn hoặc thẳng; các lát hồng lớn với mặt tương đối trơn tiếp tục nổi rõ. Bố cục và mix projected của ụ nem rất gần nhau trong hai actual still. F05 vẫn có nhiều mặt dải dẹt cong/lát không đều và bề mặt vụn beige nhám đọc được. R09 chưa cung cấp evidence đủ để đóng target geometry difference trong proposal phần4/7.

Đây là so sánh thị giác, không kết luận pixel-identical; hashes khác nhau. Không khẳng định không có bất kỳ thay đổi nhỏ nào, và không quy nguyên nhân cho “model bỏ qua source”, reference weighting, thiếu mask, prompt dài, scale hoặc preservation constraints. Một accessible output của một request không phân biệt các cơ chế đó. Cũng không kết luận model/Flow không thể làm việc này.

Các vùng khác trông gần current scene ở mức quan sát chung; addendum không chấm identity/leaf/count/lighting final PASS. Trước mọi next-test, root giữ R09 exact làm baseline before để kiểm vùng ngoài mound, portion/plate và serving count. Approved final serving theo ledger75:27 vẫn là một plate món, một plate lá, hai bát nhận, hai chén tương, hai đôi đũa, một cốc; không sửa count trong food request.

### 10.3 A — Empty-plate intermediate rồi thêm F05 (khuyến nghị)

**Điều mới được thử:** tách thao tác thành (A1) bỏ nội dung món khỏi target mà giữ plate/scene, rồi (A2) đặt món F05 lên target đã được xác nhận trống. Khác R09 là A2 không yêu cầu thay một ụ sai đang có trong **edit target**. Hai intermediate/output phải qua gate; không phải gửi lại prompt R09 cho cùng target. Test chứng minh hoặc bác bỏ tính khả dụng của đường thao tác này trên các outputs cụ thể; không chứng minh cơ chế vì sao R09 thất bại.

**A1 input roles:** current native R09 full frame là edit target; không supporting component. Tạo E01 empty-plate diagnostic intermediate, version/path do root đăng ký. E01 không episode asset, không sửa source R09/F05, không final phục vụ thiếu món. Chỉ nhấn submit một lần nếu quyền/count/cap/settings thực cho phép.

Exact prompt A1:

```text
Chỉ xóa toàn bộ ụ nem khỏi đĩa giữa bàn để tạo một đĩa trống dùng làm ảnh trung gian. Giữ nguyên đĩa và mép đĩa, vị trí, phối cảnh, hai nhân vật và tay, lá, mọi đạo cụ và số lượng, cốc, bối cảnh, camera, ánh sáng và watermark. Không thêm vật mới hoặc thay phần khác.
```

**A1 before/after gate:** so E01 với R09. Mound được bỏ hết; một plate trống còn cùng vị trí/rim/shape/perspective; không xóa plate cùng món, không thay lá/props/count/people/hands/cup/background/crop/lights. Chỉ khi E01 đạt mục đích diagnostic và preservation này mới xem xét A2. Nếu không đạt, stop A, lưu actual/version/hash; không chạy A2 lên plate/scene đã drift hoặc retry xóa món tự động.

**A2 input roles:** E01 đã qua A1 gate làm edit target; actual F05 làm **một supporting food source**. R09 chỉ là local before/after comparison cho root, không thêm lại làm ingredient mang geometry sai. Không dùng tên file làm bằng chứng composer đã có F05: actual preview phải đúng.

Exact prompt A2:

```text
Chỉ đặt phần nem từ ảnh tham chiếu F-NB-05_v0.1 lên đĩa trống giữa bàn. Giữ nguyên hỗn hợp dải mỏng dẹt cong xen lát/mảnh phẳng không đều, màu và bề mặt vụn bột nhám của F05. Đặt một ụ vừa trong lòng đĩa hiện có, để viền đĩa còn rõ, không phóng to món hoặc đĩa. Giữ nguyên đĩa, hai nhân vật và tay, lá, mọi đạo cụ và số lượng, cốc, bối cảnh, camera, ánh sáng và watermark; không chép nền hay đĩa từ F05.
```

**A2 before/after gate:** food identity/geometry so actual F05; scene preservation so E01; final projected portion/footprint/plate so **original R09**. Empty E01 không còn visual evidence về portion cũ, nên prompt không bảo đảm khôi phục exact lượng món. Portion là acceptance bắt buộc: nếu ụ to/nhỏ hoặc shape/height projected lệch đáng kể R09, fail đường A dù texture đẹp. Không chữa bằng một retry resize ngoài cap/test đã chốt. Không đổi F05 recipe/slice shape để fit.

**A outcome/stop:** nếu E01 đạt nhưng A2 vẫn sticks/smooth slabs, không giữ portion hoặc drift vùng khác, stop sau output A2. Root ghi “empty-plate route failed acceptance”, không “F05 không được model dùng”. Nếu A2 đạt riêng repair/preservation, route independent food + CONT review và owner selection; không tự đóng asset/P6. Hai edits có thể tích lũy drift ngoài food; kiểm cả hai stage thay vì chỉ nhìn mound cuối.

**Trade-off:** dùng editor workflow root đã thực dùng và có checkpoint trước thêm món; cần hai bounded submits, E01 chỉ là diagnostic. Tốn hơn một edit trực tiếp, có rủi ro scene/portion drift; allowance/cost thực phải root kiểm cho từng stage, không suy UI estimate0 thành miễn phí/infinite retry.

### 10.4 B — Food-detail component theo scene trước khi reintegrate (alternative, không chạy cùng A)

**Điều mới được thử:** xem có tạo được geometry F05 ở một food-detail composition theo perspective/lighting scene khi không mang burden hai nhân vật/serving, rồi xem một component đã qua gate có giữ fidelity khi đưa về full-frame hay không. Component pass + reintegration fail sẽ xác định thất bại nằm ở **đầu ra bước reintegration trong đường thử này**, không chứng minh nguyên nhân là scale, weighting hoặc preservation. Component fail thì chưa có căn cứ thử reintegration.

**B1 input roles:** new image composer, actual F05 là primary food geometry/texture source; R09 là supporting context cho **plate perspective/light/relative portion**, không nguồn food texture. Vì R09 còn geometry sai, role separation chỉ là instruction, không được giả định model thực ưu tiên đúng. Root kiểm khả năng chọn exact hai images trước submit. Tạo D01 food-detail diagnostic component, không sửa approved F05 và không dùng D01 tự động làm new approved food baseline.

Exact prompt B1:

```text
Tạo một ảnh cận riêng đĩa nem để làm thành phần trung gian. Dùng F-NB-05_v0.1 làm nguồn duy nhất cho hỗn hợp dải, lát, màu và bề mặt phần nem; giữ đúng hình dạng của F05. Dùng ảnh bàn ăn T-NB-03_v0.6 chỉ để theo góc nhìn đĩa, ánh sáng và tỷ lệ phần nem trên đĩa. Hiển thị một đĩa nem trên bàn gỗ, đủ thấy toàn bộ viền đĩa và rõ chi tiết món; không nhân vật, lá, chén, bát, đũa hoặc cốc. Không sao chép phần nem của ảnh bàn ăn.
```

**B1 before/after gate:** so D01 actual với F05 về mix flat/curved strips, irregular slices, colors, powder-like surface; so R09 về plate perspective/relative mound-to-plate size/light direction. Không thêm shape/recipe mới; không dùng ảnh cận chỉ che mismatch hoặc đổi portion. Nếu vẫn sticks/smooth slabs, plate angle/portion sai hoặc surfaces mất, stop B; không thử reintegration bằng component chưa đúng.

**B2 input roles:** original native R09 làm edit target; D01 **đã kiểm** làm một supporting mound source. Không thêm ingredient count/identity/leaf/background khác. D01 chưa owner-approved asset; chỉ dùng diagnostic input nếu trial authority root thực bao phủ.

Exact prompt B2:

```text
Chỉ thay ụ nem trên đĩa giữa bàn bằng phần nem từ ảnh cận trung gian đã chọn. Giữ nguyên hình dạng dải/lát, màu và bề mặt nhám của phần nem trong ảnh cận, thu về đúng kích thước, vị trí và phối cảnh ụ nem của ảnh bàn ăn hiện tại. Giữ nguyên đĩa, hai nhân vật và tay, lá, mọi đạo cụ và số lượng, cốc, bối cảnh, camera, ánh sáng và watermark; không chép đĩa hoặc nền của ảnh cận.
```

**B2 before/after/stop:** geometry so D01 và approved F05; full-frame food readability và portion/plate/vùng ngoài mound so R09. Một actual output rồi stop nếu bất kỳ gate không đạt. Không asset-pass từ component pass. Trade-off B có diagnostic về chuyển góc/light và component fidelity, nhưng cần hai submits và vẫn reintegrate vào target có ụ cũ; role separation của B1 cũng chưa proven. Vì vậy ưu tiên A để thử một target đã bỏ ụ sai, giữ B là alternative có câu hỏi khác, không blind fallback chạy ngay khi A fail.

### 10.5 Before-submit gates chung và findings mới

- Chỉ chọn **một** đường A hoặc B; mỗi stage tối đa một submit đề xuất, stage2 có điều kiện stage1. Không dispatch cả hai đồng thời. Counts/credit allowance/settings/authority do root xác minh, không được adviser gia hạn200credit hoặc tự cho quyền tool.
- Root đăng ký exact request/target/support/version, actual previews, UI settings/estimate/count semantics và stop trước từng stage. Nếu UI không hỗ trợ input roles thực cần dùng, dừng tại readiness, không giả mask/crop/feature hoặc dùng Python/local manipulation.
- Working diagnostic intermediate không là asset approval hoặc replacement của F05. Final vẫn bảo toàn approved count/people/leaf/portion/plate và canon; chỉ kết quả có actual evidence mới chuyển tiếp independent review/owner selection.

| Finding / rule | Status; severity | Evidence / impact | Action / route | Closure evidence |
|---|---|---|---|---|
| ART-T02-01 / ART-2 | DEFECT target geometry; MAJOR | Actual R08/R09 central mound vẫn gần nhau, không đọc mix F05 đủ; không có pixel identity claim | Không chạy lại cùng R09 request; root chọn một decomposed test | Actual E01+A2 hoặc D01+B2 với hashes và all acceptance gates; independent output review riêng |
| ART-T02-02 / ART-TOOL | MET recorded target/support use; UNKNOWN weighting | Source76:118–125 + root history update: implicit target + one previewed F05 component | Không gọi failure là “không có F05” hoặc khẳng định weighting; giữ technical hypotheses / FLOW | Actual request/input record xác minh role sử dụng; model hidden weighting vẫn unknown nếu không evidence |
| ART-T02-03 / ART-TOOL | UNKNOWN region control; MAJOR nếu dựa vào mask | Root chỉ thấy aspect crop và đã Cancel; không mask observed | A/B chỉ dùng observed whole-frame edit/new composer workflows; feature check root | UI read-back đúng workflow thật trước submit; không tự invent local selection |
| ART-T02-04 / ART-3 | UNKNOWN preservation/portion của next tests; MAJOR | E01 bỏ mound nên mất portion cue; D01 là new composition; hai-stage có thể drift | Before/after against original R09 bắt buộc; preserve approved serving/people/leaf/plate / CONT | Exact intermediates và final output, readable full-frame/local comparison; fail nếu portion/count/scene drift |
| ART-T02-05 / ART-5 | MET paper boundary | Chỉ đổi workflow/test, giữ approved F05 recipe/shape/canon | Không cure output bằng đổi F05, thêm action hoặc fact claim / ART+root | Prompt/manifest traceability và actual media, owner selection riêng |

### 10.6 Handoff / run record append

Đã xác định: đúng supporting F05 được recorded preview; R09 actual chưa đóng food geometry target. Root đã dừng focused R09 test; crop/region capability không được suy. Chưa xác định causal mechanism, khả năng A/B đạt, cost/billing hoặc next allowance.

Khuyến nghị làm việc: **A**, với empty-plate intermediate qua preservation gate trước, rồi F05 insertion. Root chỉ cần chọn route/verify concrete requests và quyền hiện có; không xin lại approval texture/canon F05. Nếu chọn B, giữ hai checkpoint như trên. Không tự chạy fallback hoặc reapproval asset.

| Run | Role / stage / dispatch mode | Access thực | Artifact / disposition | Owner decision mới | Next route |
|---|---|---|---|---|---|
| EP01-P6-ART-TEXTURE-02 | AG-ART-01 / P6 / PAPER_ANALYSIS, bounded paper maker scope | F05/R08/R09 actual; own10; source75/71/68; exact R09 record76:116–128; root capability update | report10 addendum / PROPOSAL_COMPLETE_NEXT_TESTS; R09 food unresolved | None | Root choose A or B; readiness per stage; actual outputs + independent review + owner selection |

Change log addendum v0.2: giữ prior proposal v0.1, thêm R08/R09/F05 actual comparison và recorded R09 request; hai alternatives tối đa với input roles/exact prompts/stage gates/stop; ưu tiên A. Không Flow/generation/upload/media edit/Git, không final media hoặc asset approval, không causal mechanism claim.

### 10.7 Dispatch update — root đã chọn A và chạy A1, actual còn pending

Root thông báo trong cùng run đã **chọn A, không B** và submit một A1 root-authored request, không supporting references: xóa toàn bộ phần món trong central ivory plate, giữ actual plate/frame. Final adviser addendum chưa hiện diện tại pre-submit; root đã log đúng provenance, không gọi A1 request đó là exact prompt A1 của adviser ở phần10.3. Root không apply mask/crop. Đây là `ROOT_REPORTED` dispatch/status update; adviser không thao tác UI hoặc mở actual A1 vì chưa được giao output.

Latest next route vì vậy là: đợi actual A1 → kiểm empty-plate/preservation gate của10.3 so original R09 → root đọc exact A2 prompt/input roles ở10.3 trước submit. B vẫn alternative paper được lưu, không fallback tự động.

**A2 thực dụng:** target là actual A1 **chỉ khi** đã giữ đúng plate, scene/people/leaf/count/cup/lights; supporting component đúng một actual F05, kiểm preview. Original T-NB-03_v0.6/hash `F631378EE97B74027A69FA900D9F1FC31B194F2E946E712809275507C5B68FFF` giữ làm before cho portion/plate, không tự thêm làm input ingredient. Không có vùng mask hoặc pixel-copy guarantee. Prompt10.3 yêu cầu mound nằm trong lòng plate và không phóng to; **root vẫn phải đối soát footprint/portion/height projected với original v0.6**, vì empty target không còn cue lượng món cũ. Nếu sai portion hoặc drift plate/vùng khác, stop, không repair tiếp để cứu test.

Status A2: `PENDING_ACTUAL_A1_GATE_AND_ROOT_REQUEST_READINESS`. Không có A1 media pass, A2 submit authority/cap hoặc asset approval được adviser tạo. Root có thể dùng quyền đã có đúng scope sau actual gate/readiness; không xin lại approval F05/canon đã chốt.
