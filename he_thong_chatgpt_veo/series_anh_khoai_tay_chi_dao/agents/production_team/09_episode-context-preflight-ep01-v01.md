# EP01 — Context preflight P6: bàn ăn và frame tích hợp

Ngày: 2026-10-01 (Asia/Saigon). Run: `EP01-P6-CONTEXT-CTD-01`. Role: `AG-CTD-01` hiện hành, stage `P6`, mode `PAPER_REVIEW`.

Disposition: `PASS_FOR_OWNER_REVIEW / PAPER_CONTEXT_ONLY`. Hướng camera đối diện cạnh hai người ngồi có cơ sở để lập bản request tiếp theo. Đây không phải `MEDIA_PASS`, không phải phê duyệt T-NB-02C_v0.4/T-NB-03_v0.1, không xác nhận generation-ready hoặc P6 complete.

## 1. Envelope, quyền và phạm vi kiểm

- Task: đối soát ledger75 với exact script/approval, visual baseline, direction, serving và reference authorization; đánh giá lựa chọn staging trước lượt sửa frame tích hợp.
- Target paper: hướng dựng frame tiếp theo, dựa trên `75_p6-episode-context-ledger-v01.md`; context media được xem là `T-NB-03_v0.1.jpg` và bàn trống `T-NB-02C_v0.4.jpg`.
- Envelope update từ root trong run: dựng **NEW style-frame từ composer thư viện**, không edit primary và không dùng T03/T02C hoặc secondary scene làm source. Input dự kiến: PRIMARY + F05 + `nembui.jpg` + ảnh mẹt68 hỗ trợ vài sprigs; scene theo text64/71/75. Đây là combined reconstruction, không one-factor experiment và không tạo causal claim về hiệu quả từng input.
- Authority thực có: nhiệm vụ paper adviser từ root; content approval33, primary visual approval45, direction64, food/reference/serving approvals68/71/72. Quyền tiếp tục sửa/thử ảnh của owner được ledger75 ghi nhận; run CTD này không được sử dụng quyền operator đó.
- Không được làm: Flow, generation, upload, Git, sửa script/approval/source ledger, tự duyệt asset, triển khai runtime role mới, voice/video/release. Không đọc file74 hoặc các reviewer reports13–19.
- Đã đọc toàn bộ common contract02 và section `AG-CTD-01` của role prompts03. Không dùng role đề xuất08 làm authority.
- Tools thực dùng: đọc file local, xem ba JPEG bằng `view_image` ở độ chi tiết original, kiểm decode/kích thước/hash local. Không browser, không account UI/model/cost read-back, không audio/video.
- Không là media auditor cuối. Quan sát still ở đây chỉ hỗ trợ phân tích viewpoint, dependencies và request; không chấm pass nhân vật/món/lá độc lập.

## 2. Inputs thực đọc và version/access

Các path ở bảng tài liệu dưới đây là `episodes/ep01_pilot/` tương đối từ series root.

| ID | Artifact thực đọc | Status / giới hạn dùng |
|---|---|---|
| S75 | `75_p6-episode-context-ledger-v01.md` | ACTIVE_ROOT_PREFLIGHT / SOURCE_CONTEXT_ONLY; ledger, không asset approval |
| S32 | `32_p5-script-c-v0.5-approved-content.md` | Exact C-v0.5 / OWNER_CONTENT_APPROVED; status final paper review pending tại hồ sơ này |
| S33 | `33_p5-c-v0.5-owner-content-approval.md` | Xác nhận đúng approval C-v0.5; không request/media approval |
| S45 | `45_p6-owner-v03-visual-baseline-approval.md` | Primary duo v0.3 được duyệt; consistency/performance còn pending |
| S64 | `64_p6-input-decisions-approved-2026-10-01.md` | Quán nhỏ ven phố chiều tối; không khóa final table/camera; không voice/video |
| S71 | `71_p6-food-texture-approval-and-street-table-brief-2026-10-01.md` | F05 texture được duyệt; vị trí tabletop là draft |
| S72 | `72_p6-serving-approval-and-table-trial-2026-10-01.md` | Bộ phục vụ được duyệt; prompt T01 là lịch sử một trial, không canon camera |
| S68 | `68_p6-food-local-intake-and-owner-use-approval-2026-10-01.md` | Hai ảnh thật owner-authorized use; research-only và commercial-rights clearance tách riêng |

| Media thực mở | Kích thước / bytes | SHA256 kiểm trên bytes trong run này | Status được phép suy |
|---|---|---|---|
| `media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg` | 768×1376 / 94739 | `ECFBE7A3C543730C268A77CA08D508147115CA804154F85EBDBB38C5C601E8C7` | Hash khớp S45:11 và S75:20; primary baseline, không mọi pose/action |
| `media/raw/ep01_p6_food/T-NB-03_v0.1.jpg` | 768×1376 / 140686 | `51B6806F839A216F818DAC192839EBCACAD5935C89CBA2E1C1628AA20479D45B` | Current integrated candidate; chưa owner-approved theo dispatch |
| `media/raw/ep01_p6_food/T-NB-02C_v0.4.jpg` | 768×1376 / 132997 | `87CAF331A65AEE0FECFAF6C540E8C743B4C7F8922915FA6A0144A131FF4B11DD` | Empty-table candidate; chưa owner-approved theo dispatch |

**Không truy cập trong run:** actual F-NB-05 và hai ảnh thật ở Downloads không nằm trong ba actual media được giao; chỉ đọc approval/intake metadata. Không kiểm leaf species/food fidelity bằng so ảnh thật. Không đọc source38 được S64:10 nhắc tới; không xác nhận P5 final-review closure mới hơn S32/S33. Model/ref capacity/account settings/cost/spent credit/approved exact next request đều `UNKNOWN / NOT_TESTED` trong phạm vi này. Không suy các giá trị đó từ hồ sơ trial cũ.

Root reported account read-back trong dispatch update: đã mở primary Flow “Two characters standing in studio”, editor `9a03ed42-2b78-445b-a1a3-5901311a4c4a`; native download có hash khớp primary45. Preview component R04 là secondary scene, không primary. Đây là evidence **ROOT_REPORTED**, không account read-back độc lập của CTD; không xác nhận settings/price/count của request mới. CTD trực tiếp xác minh hash primary local ở bảng trên.

## 3. Đối soát ledger với quyết định gốc

| Context rule | Kết quả paper | Source span / ý nghĩa |
|---|---|---|
| Exact setup/payoff C-v0.5 | MET | S32:9–39,43–46 và S33:10–16 khớp S75:35–42. Nem hướng về miệng Khoai, đổi hướng trước contact, Đào hiểu và đưa bát, nem vào bát; không đút |
| Hai agency và quan hệ bạn | MET ở ý định | S32:35–45: Đào chủ động trêu/đưa bát, Khoai bình thản chữa cháy; S45:14 giữ bạn bè. Frame đẹp không xác nhận performance này |
| Primary identity/outfit | MET về dependency | S45:11–20 và S75:20,27. Outfit theo primary, gồm blouse Đào có cổ/nút; portrait pose/nụ cười không phải trạng thái cố định scene |
| Food, serving, quán | MET về quyết định | S71:7–11,22–24 và S72:3–5 khớp S75:27. Texture F05, đĩa lá riêng, hai chén tương đỏ, hai bát, hai đôi đũa, một cốc bên Đào |
| Camera/table geography | MET là adjustable | S64:5, S71:26–30, S75:29. Prompt T01 tại S72:16 chọn near-side/overhead cho một trial; không có approval khóa cạnh gần hoặc góc đó vĩnh viễn |
| Lá sát món | MET là lựa chọn staging | S71:28 đặt phía sau là draft; S75:31,43 cho lá riêng trong vùng dùng chung, không yêu cầu bày xa. Dời đĩa lá sát trái-món không sửa serving set |
| Fact/fiction và quyền | MET trong ledger | S32:52–56, S68:3,20,29–30 và S75:45–49: không suy công thức/species từ ảnh, không upload research-only, không biến authorization thành independent commercial clearance |

Không phát hiện lệch lời thoại hoặc payoff giữa ledger và exact script trong allowlist. “Khoai trái/Đào phải” là ràng buộc screen geography của ledger/request này, không kết luận canon camera cho mọi tập. “Cùng một cạnh dài” là lựa chọn staging hiện hành mà CTD đánh giá; script không khóa kích thước bàn hoặc ghế.

## 4. Quan sát still liên quan đến preflight — không media verdict

**Primary v0.3 actual:** Khoai bên trái, Đào bên phải; silhouette và màu khác nhau rõ; áo khoác xanh than/áo kem/quần tối của Khoai, blouse kem có cổ/nút/váy sage/nơ hồng đất của Đào. Dùng ảnh này làm nguồn identity/outfit. Không dùng tư thế đứng cạnh nhau, nụ cười hoặc khoảng cách portrait làm blocking buộc phải giữ trong bữa ăn.

**T-NB-02C_v0.4 actual:** bàn trống chiếm khung, hai bát và hai đôi đũa có thể thấy; bàn có đĩa lá riêng bên trái phía sau món và thêm vòng lá dưới/quanh món. Góc nhìn cao làm rõ tabletop; nó không chứng minh khi thêm thân/người vẫn thấy đủ bát, mặt và đường với tay. Vòng lá quanh main dish là biến thể chưa owner chọn theo S75:31; không tự thừa kế approval serving.

**T-NB-03_v0.1 actual:** Khoai lớn ở tiền cảnh trái, Đào nhỏ/lùi ở phía phải; đây là projected composition thấy trên still, không đo tọa độ/chiều cao thật. Bàn nằm giữa hai vùng nhân vật; chưa có cơ sở dùng still này chứng nhận cùng một cạnh dài. Chỉ một bát nhận trống hiện rõ ở vùng dưới giữa; vị trí bát còn lại từ bản bàn trống không có visibility đủ để duyệt. Đào đặt tay sát miệng cốc bên phải; Khoai chưa cầm đũa. Main dish có vòng lá lớn; đĩa lá riêng lùi về phía sau trái, một phần bị Khoai che.

Các quan sát này giải thích vì sao nên dựng lại quan hệ camera–hai người–props, thay vì coi layout candidate hiện tại là bàn/asset đã khóa. Không kết luận identity drift, nem đúng/sai hay species lá đạt từ preflight này; đó là nhiệm vụ CHAR/ART và reviewer chuyên môn trên exact media/reference.

## 5. Invariants, phần được điều chỉnh và prop → beat

**Giữ trong request tiếp theo:** exact script32/approval33; primary identity/outfit45; Khoai screen-left/Đào screen-right; bạn trưởng thành; quán ven phố bình dân gọn gàng chiều tối; nhóm phục vụ đã duyệt; texture lineage F05; no brand/landmark/romance mới; giữ watermark. Still là neutral style-frame: chưa cầm đũa/miếng món, chưa ăn/cuốn/chấm, chưa đóng vai đoạn payoff.

**Được điều chỉnh bằng staging proposal:** camera ở phía đối diện cạnh hai người ngồi, góc cao vừa đủ, crop và tỷ lệ tabletop trong khung, chỗ ghế, vị trí/khoảng cách props. Screen order và cùng cạnh dài phải được viết đồng thời trong request. Chỉ “đổi camera sang đối diện” có thể làm model đảo thứ tự hoặc giữ người ngồi hai phía; không thay thế được mô tả blocking rõ.

| Prop / vùng chức năng | Beat / hiểu biết phải bảo toàn | Yêu cầu ở neutral still | Evidence phải có về sau |
|---|---|---|---|
| Một đĩa nem giữa hai người | S32:9–15: Khoai chú ý món, Đào định kéo đĩa | Đĩa/viền rõ trong tầm tay cả hai, có phần mép để Đào tiếp cận; không props chặn giữa tay Đào và plate | P7 coverage Đào định kéo; video kiểm tay/đĩa thực |
| Vùng plate → miệng Khoai | S32:25–31: ý định ăn rồi chuyển hướng | Khoảng không quanh mặt/ngực/tay Khoai, không cốc/chén/lá lớn chắn hành lang | Motion thực phải thấy hướng về miệng và đổi trước contact; still không chứng minh |
| Hai bát nhận riêng, trước mỗi người | S32:35–39: Đào đưa bát, nem vào bát | Hai bát thấy rõ miệng/viền, bát Đào có vùng cầm/đưa ra; không bát ẩn sau torso hoặc leaf plate | Grip, transfer, object state và không đút phải kiểm media |
| Cốc nước ngoài Đào | S32:25–29: turn lấy cốc giúp setup bị phát hiện | Cốc bên ngoài phía Đào, đầy đủ trong khung và có vùng tay tới; không nằm giữa hai người hoặc trước bát nhận | Video kiểm lượt quay đi/quay lại, không tự suy timing từ vị trí |
| Đĩa lá riêng sát trái món | S71:22,36: lựa chọn ăn kèm hiện diện | Cùng cụm dùng bữa, trong tầm với; đặt lệch khỏi đường Khoai gắp và đường Đào kéo/nhận; không làm decor rải bàn | ART so morphology với actual approved refs; không auto-identify species |
| Hai chén tương đỏ | S71:22–24: serving set hai bạn | Chén cạnh vùng bát nhưng ngoài đường chuyển đũa/bát; thấy rõ và phân biệt với bát nhận | CONT số lượng; ART appearance. Không thêm action chấm |
| Hai đôi đũa gỗ nằm bàn | Có công cụ cho gắp ở các beat sau | Mỗi đôi gần vị trí người tương ứng, đủ thấy; hands neutral, không food-on-chopsticks ở style-frame | Probe grip riêng và action theo script khi có quyền media |

“Trước mỗi người” là theo tọa độ người ngồi, không cố định “cạnh gần camera”. Khi camera sang phía đối diện, bát phải theo người ở cạnh xa; không giữ bát ở vị trí cũ rồi thêm người phía đối diện bát.

## 6. Hai staging alternatives — chưa chọn final frame

### A — Camera đối diện trung điểm cạnh hai người ngồi (khuyến nghị)

Khoai ở screen-left, Đào ở screen-right, cả hai ngồi cùng cạnh dài phía xa camera. Camera nhìn từ cạnh đối diện, nâng nhẹ đủ thấy hai mặt và tabletop. Framing ưu tiên đầu, thân trên và đầy đủ nhóm props; không cần chứng minh ghế/chân bằng full-body nếu làm mất bát/cốc. Hai bát nằm trước từng người; nem giữa vùng chung; đĩa lá sát bên trái nem nhưng lệch ra phía camera nếu cần tránh đường với của Khoai; chén chấm đặt ngoài các hành lang; cốc ngoài bên Đào. Không đặt đĩa lá vào giữa bát Đào và plate.

- Lợi ích: khoảng cách projected hai mặt cân hơn, hai agency rõ, vùng plate → miệng Khoai → bát Đào có thể đọc trong cùng hemisphere camera; phù hợp ý root mà không sửa payoff.
- Trade-off: crop dọc dễ ép cả hai vai và đồ bàn; góc quá thấp làm plate che bát, quá cao làm mặt/biểu cảm mất ưu tiên. Không có góc/độ cao thắng được xác nhận trước trial.
- Điều kiện: phối hợp camera và actor geography; không reuse bố trí vật từ T02C như invariant. Hai bát/cốc phải thấy đầy đủ, leaf plate không che reach lane. Neutral hands, không lấy cốc/đũa/ăn trong still.
- Technical hypothesis: góc nâng vừa phải và bớt floor/ghế có thể giữ mặt + serving; `UNTESTED`, không cam kết model thực hiện đúng.

### B — Camera cùng phía đối diện, lệch nhẹ về phía Đào

Giữ screen-left/right và cùng cạnh xa; camera chỉ lệch nhẹ trong cùng phía bàn, chưa đổi sang nhìn sau lưng/qua vai. Bát Đào và cốc ngoài Đào rõ hơn, Khoai vẫn đủ mặt và tay; plate/lá giữ cùng cụm. Không chọn mức lệch làm mặt Khoai lùi nhỏ như current candidate.

- Lợi ích: có thể tách silhouette tay Đào, miệng bát và cốc nếu option A bị overlap; hữu ích cho bài toán Đào quay sang cốc và đưa bát sau này.
- Trade-off: Đào có thể projected lớn hơn và che bát/plate; Khoai có nguy cơ nhỏ/lùi hoặc tay bị thân che. Requires kiểm scale/framing lại, không sửa chiều cao canon từ perspective.
- Use gate: fallback paper nếu A không giữ đủ visibility; không mặc định generate cả hai. Không tự đổi sang ngồi đối diện để giải crop.

## 7. Coverage và findings

| Rule ID | Coverage | Artifact / evidence | Giới hạn |
|---|---|---|---|
| CTD-1 — setup/payoff | MET trên paper | S32:9–39,43–46; phần5 map tất cả causal props | Performance/motion chưa test |
| CTD-2 — hai agency/relationship | MET trên paper | S32:29–45; S45:14; alternative A/B giữ chủ động Đào | Một neutral still không xác nhận khán giả hiểu joke |
| CTD-3 — alternatives | MET | Hai phương án phần6, trade-off và use gate cụ thể | Chưa owner chọn final output |
| CTD-4 — feature uncertainty | UNKNOWN | Không được giao model/account evidence/cap actual hoặc video | Không xác nhận feasibility/generation-ready |
| CTD-5 — handoff | MET | Dependencies và gates phần8–9 | Các role nhận handoff còn phải thực kiểm |
| C-IDENTITY | MET về provenance | Actual primary hash khớp S45:11 | Integrated identity consistency UNKNOWN |
| C-FOOD/LEAF | UNKNOWN | Intake/approval metadata S68/S71; không actual F05/real refs trong run | Không species/food fidelity verdict |
| C-RIGHTS | MET về phân loại / UNKNOWN clearance | S68:3,20,29–30; S71:50 | Owner use authorization không independent commercial-rights clearance |
| C-AUDIO/MOTION | N/A cho neutral still | Task chỉ paper/style-frame | Không audio/motion pass, thời lượng thực UNKNOWN |

Findings bên dưới là các chặn để nâng candidate/request thành approved production input, không phủ định quyền root tiếp tục lượt sửa ảnh đã được owner giao.

| Finding / rule | Status; severity | Source / impact | Action + route | Owner decision needed / closure evidence |
|---|---|---|---|---|
| F-CTX-01 / C-GEOGRAPHY | DEFECT ở dependency; MAJOR | T03 actual: left foreground Khoai, right background Đào; cùng cạnh dài không xác nhận được; S75:29 cho phép đổi camera. Giữ target layout như baseline có thể giữ nhầm quan hệ ghế–bát | Root/CTD/P6 chọn A làm working request; SHOT/P7 khóa screen geography và hemisphere | Không hỏi lại script; owner selection trên new candidate. Closure: exact new still thấy hai người cùng cạnh, hai bát trước đúng người; P7 ghi actor/camera positions |
| F-CTX-02 / C-PROP-BEAT | DEFECT ở visibility; MAJOR | T03 actual chỉ một receiving bowl rõ; không chứng minh bát Đào/đường nhận. S32:35–39 buộc Đào đưa bát | ART/P6 + CONT: rebuild bát theo người, clear transfer corridor; giữ cốc ngoài Đào | Closure still: cả hai bát/viền đủ thấy. Motion closure riêng: bát Đào nhận nem; không đóng bằng still |
| F-CTX-03 / C-SERVING | DEFECT ở unselected dependency; MAJOR | T02C/T03 actual có vòng lá quanh món, S75:31 ghi biến thể chưa owner chọn; dễ copy sang bản mới như canon | ART/P6 giữ đĩa lá riêng và texture lineage; không copy vòng lá để mặc định baseline | Nếu muốn giữ vòng lá: owner chọn variant riêng. Nếu theo serving đã duyệt: new still không kế thừa vòng lá unselected, review actual lại |
| F-CTX-04 / C-IDENTITY | UNKNOWN; MAJOR | Primary hash xác minh; T03 là pose/perspective khác chưa có approval. Không transfer approval45 sang candidate | CHAR/P6 + CONT đối chiếu actual primary về face/outfit/silhouette, không sửa canon để vừa bàn | Closure: exact candidate + independent review + owner selection; không gọi report CTD này là identity pass |
| F-CTX-05 / C-FOOD/LEAF | UNKNOWN; MAJOR | S68/S71 metadata đủ biết nguồn/approval; actual F05/ảnh thật chưa xem trong run. Nhãn tên lá/prompt không chứng minh fidelity | ART/P6 và food/leaf reviewer nhận exact approved actual refs/hashes để so candidate | Không hỏi lại authorization68. Closure: reviewer actual comparison, leaf morphology evidence và disposition version cụ thể; species vẫn unknown nếu ảnh không đủ |
| F-CTX-06 / C-REQUEST | UNKNOWN; MAJOR | Root đã chỉ định new reconstruction và bốn input roles; chưa có exact next request/settings/count/cost/cap read-back trong run CTD | PROMPT/P8 + FLOW/RIGHTS kiểm manifest, actual preview, count/cap/authority đúng phạm vi | Root dùng authority đã có; authority thiếu cho thao tác mới mới route owner. Closure: exact request/version và UI read-back/approval records; không dùng billing inference |
| F-CTX-07 / CTD-1/2 | UNKNOWN; MAJOR cho performance gate | S32:25–39 và common contract6–7: still không chứng minh ý định ăn/khựng/đổi hướng/Đào hiểu/timing | SHOT/P7 coverage, PROMPT/P8 probe khi có video authority riêng; PERF/CONT/AV review output thật | Chưa được video run này. Closure: exact playable media, time/frame evidence; không sửa thoại để khớp model |
| F-CTX-08 / C-P5-STATUS | UNKNOWN; MINOR cho paper preflight, không suy whole-production ready | S32:3 và S33:22 nêu final paper pending; S64:10 nhắc source38 nhưng ngoài allowlist | Root đối soát hồ sơ final P5 khi chuẩn bị production handoff; adviser không đọc thêm hoặc tuyên bố pending đã được đóng | Không yêu cầu owner approve C-v0.5 lại. Closure: exact final-review evidence/version được root đăng ký; không lấy approval33 làm final gate pass |

## 8. Identity / food / leaf / rights dependency map cho request tiếp theo

| Dependency | Vai trò đúng | Gate sử dụng |
|---|---|---|
| Primary pair v0.3, hash đã kiểm ở phần2 | Identity/outfit source | Không thay bằng demo/secondary outfit; preview actual đúng primary. Approval45 không auto-approve ngồi/tay mới |
| F-NB-05_v0.1, hash hồ sơ `C562A77D4A79D6A01E1518191796283810B6E40ADEF814A299B85960099C7E28` | Approved generated texture/design ref | Root verify actual đúng version/lineage; CTD không đã so actual F05. Không dùng nó làm food fact proof |
| `nembui.jpg`, hash hồ sơ `A51303F7100EDD0944DC00DAA19402FECFE24BB0E15A4143DA8F8EAE7B9E3A2D` | Authorized real appearance reference | Theo đúng phạm vi68; không tự copy lá/ớt như arrangement bắt buộc |
| `z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg`, hash hồ sơ `1237956E99458385F95F1EDF18E0A98E1BDDB777030AC1D69FAB05FA7A51D741` | Authorized loose food/leaf appearance support | Không copy các món ngoài mẹt/mẹt nguyên bố cục; morphology cần actual review |
| T-NB-03_v0.1 / T-NB-02C_v0.4, hashes phần2 | Unapproved context candidates | Theo root update: không chọn ingredient/source/edit target cho lượt mới; chỉ dùng các quan sát preflight. Không thừa kế geography/unselected serving cũ |
| FV04a/FV04b và reference research-only | Research evidence only | S68:29–30 chưa duyệt dùng; không tự upload/chọn làm generation ingredient |

Không có evidence về số reference tối đa hoặc công cụ kiểm từng loại trong run này. Root phải chọn input set khả dụng và ghi vai trò thực; không hứa model chấp hành đủ dependencies chỉ vì prompt nêu tên chúng. Những quyền tham chiếu owner đã cấp không cần được xin lại; independent commercial-rights clearance và release gate vẫn là status riêng.

Input set root dự kiến vì vậy là: primary actual giữ identity/outfit; F05 giữ approved dish texture; `nembui.jpg` hỗ trợ cấu trúc food/appearance; ảnh mẹt68 hỗ trợ ít foliage/sprigs, không chuyển các món khác/mẹt/arrangement nguyên ảnh vào scene. Bốn vai trò phải được actual composer preview xác nhận trước submit; primary giữ nguyên baseline. So sánh candidate sau combined reconstruction chỉ cho biết candidate đạt/không đạt các tiêu chí, không chứng minh riêng camera, số refs hay leaf source gây ra thay đổi.

## 9. Next-request gates và handoff

1. **Lock working staging, chưa final selection:** dùng option A của phần6; viết rõ cùng cạnh dài phía xa camera, Khoai screen-left/Đào screen-right, bát theo người, plate trong vùng tay, leaf plate sát trái-món nhưng ngoài reach lane, cốc ngoài Đào. Owner đã duyệt script/serving; không mở lại cùng quyết định. B chỉ fallback nếu visibility của A thất bại.
2. **Build reviewable exact request:** Root/PROMPT tạo NEW request từ composer thư viện với bốn input roles ở phần8, không edit primary hoặc chọn T03/T02C/secondary scene làm source. Ghi target version mới, actual previews/hashes, neutral hands và no eating actions; cấm biến style-frame thành beat ăn/đưa bát/gắp. Reuse quyền đã có đúng scope; account features/settings/ref capacity/count/cost/cap/authority cần kiểm trước submit. Adviser không tự đặt count/spend allowance: `PENDING_ROOT_VERIFICATION`.
3. **Still acceptance, câu hỏi thử:** có đồng thời thấy hai mặt đúng primary, hai bát và đủ serving không? Cùng một cạnh dài có đọc được không? Món/lá/chấm là cùng bữa trong tầm dùng không? Cốc có chỗ lấy, bát Đào có chỗ đưa, plate có mép tiếp cận không? Fail nếu vật bị che/crop, screen order sai, người vẫn projected như hai phía bàn, lá chắn đường, vòng lá unselected trở thành default, hoặc frame thêm eating/payoff action. Không suy grip/reach động đã đạt chỉ vì các vật thấy trong still.
4. **Independent output checks:** exact downloaded candidate → cold media interpretation trước → actual primary/food/leaf refs và ledger sau theo reviewer scope. Root tổng hợp; owner chọn candidate. Current T02C/T03 chưa approved không là closure evidence cho lượt mới. Không đánh dấu MEDIA PASS từ report09.
5. **Production handoff riêng:** CHAR/ART xử lý refs và serving; SHOT/P7 đặt start/end states, axis/joins và payoff coverage; PROMPT/P8 lập request theo feature evidence, FLOW/RIGHTS phản biện; owner approval đúng request/video scope; sau đó PERF/CONT/AV kiểm media thật. Không dùng P6 still thay AI performance proof hoặc tự mở voice/video.

## 10. Tổng hợp và run record

- Đã xác định: ledger bảo toàn C-v0.5, primary v0.3, set/texture/serving đã duyệt và ranh giới quyền. Camera/prop distances của trial không là canon. Proposal camera đối diện cùng cạnh là hợp lý cho next frame.
- Quyết định đã có: nội dung, primary, F05 texture, quán ven phố chiều tối, bộ phục vụ và hai ảnh thật authorized use. Report này không tạo quyết định owner mới.
- Giả định làm việc: option A; neutral style-frame trước hành động, các vùng tay để trống; đĩa lá lệch trái nhưng gần main dish. Khoảng cách vật lý/góc camera chính xác chưa đo hoặc khóa.
- Còn mở: candidate mới, visibility/character consistency/food-leaf fidelity, exact request readiness/approval, performance/motion/audio và final owner selection. Independent commercial-rights status chưa xác minh trong run.
- Bước tiếp theo: root hoàn thiện exact request với staging A và dependency roles; kiểm readiness trong scope đã có; review actual output độc lập, rồi owner chọn. Không lấy paper-ready thành output-pass.

| Run ID | Role / stage / mode | Context / access thực | Report / disposition | Owner decision | Next route |
|---|---|---|---|---|---|
| EP01-P6-CONTEXT-CTD-01 | AG-CTD-01 / P6 / PAPER_REVIEW | S75/S32/S33/S45/S64/S71/S72/S68; primary/T03/T02C actual; local read-only | `09_episode-context-preflight-ep01-v01.md` / PASS_FOR_OWNER_REVIEW — paper only | None created; new media selection pending | Root + CHAR/ART/PROMPT for next still; independent reviewers; owner selection; P7/P8 separately |

Change log v0.1: tạo preflight theo role AG-CTD-01 hiện hành, tối đa hai staging alternatives; ghi rõ observed/proposed, source spans, dependencies, unknowns và closure evidence. Cập nhật envelope root: new combined reconstruction, bốn input roles, giữ nguyên primary, loại secondary/current table candidates khỏi ingredient set. Không sửa input, không run tools tạo media hoặc asset approval.
