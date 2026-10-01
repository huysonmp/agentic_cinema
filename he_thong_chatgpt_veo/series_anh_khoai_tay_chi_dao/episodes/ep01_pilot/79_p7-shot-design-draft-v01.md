# EP01 — Shot design P7 v0.1

2026-10-01. Run `EP01-P7-SHOT-01`; maker `AG-SHOT-01 / P7 / PAPER_PROPOSAL`.
Status: `PROPOSAL_COMPLETE / OWNER_REVIEW_DRAFT`; chưa independent review, shot approval, P6 PASS, motion/voice PASS hoặc generation-ready.

## Scope, envelope và actual access

- Đăng ký/envelope: `agents/production_team/12_p7-paper-run-log-v01.md`, section EP01-P7-SHOT-01 đã tồn tại trước maker; chỉ tạo file79, không sửa upstream/log.
- Thực đọc: common02 toàn bộ; Tier1 stage-map02 toàn bộ; role03; log12; exact episode32/35/38/45/62/71/75/78 và CTD `agents/production_team/11_p6-next-gate-readiness-v01.md`.
- Bổ sung sau dispatch, trước chốt: root mở allowlist source35 rồi `agents/production_team/13_flow-official-planning-evidence-2026-10-01.md`; đã đọc cả hai. Source13 là root ghi từ Google ngày này, không phải maker tự browse hoặc account UI proof.
- Access deviation: regex trích role03 bị greedy, output vô tình gồm CTD/CHAR/ART/VOICE trước AG-SHOT-01. Chỉ áp dụng AG-SHOT-01; đã báo root. Không đọc maker74/76, reviewer18/19, prompt/gói77 hoặc references khác.
- Thực xem bằng view_image: T-NB-03_v0.8, primary pair v0.3, F-NB-05_v0.1, H-K-I03_v0.1 và H-K-I05_v0.1 ở các đường dẫn media bên dưới. Không nghe tiếng, xem video, đo duration, kiểm lại hash hoặc live UI.
- Authority: 38 giữ C-v0.5/Q0 và hướng hình/giọng;45 primary;62 I03/I05;75 ghi serving approval;78 exact static v0.8 + P7 paper. 35 chốt owner tự dựng Canva/nhận clip pack có QC. Không tạo owner decision mới.
- Missing/NOT_TESTED: actual voice, shot-specific action/expressions, account-specific model/feature/cost/audio evidence và approved P8 request; source13 đã có general Google feature docs. Chỉ local read/view + apply_patch; không browser/network/generate/upload/credit/audio/Git/release/agent con.

## Reference ledger và staging

| ID | Exact path dưới series / trạng thái / quan sát thực |
|---|---|
| R-T08 | `media/raw/ep01_p6_food/T-NB-03_v0.8.jpg`; static owner-approved78. Khoai trái/Đào phải cùng cạnh; cốc ngoài phải; bát/đũa/chén riêng, đĩa nem giữa, đĩa lá gần trái; ánh sáng ấm. Không motion proof. |
| R-P03 | `media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg`; primary-approved45. Identity/outfit; portrait đứng không chứng minh mọi góc ngồi/biểu cảm. |
| R-F05 | `media/raw/ep01_p6_food/F-NB-05_v0.1.jpg`; texture-approved71. Mảnh phẳng xen dải cong/vụn beige; generated ref, không nguồn fact/công thức. |
| R-I03 / R-I05 | `media/raw/ep01_p6_consistency/H-K-I03_v0.1.jpg` / `H-K-I05_v0.1.jpg`; direction-selected62. Lưng tay/ngón cong, đũa chéo trước ngực; contact/grip động chưa kiểm. Không bắt ngón khuất lộ. |

FACT về authority khác FICTION câu chuyện: ký ức mẹ qua lời32, không flashback/mẹ xuất hiện hoặc fact Bắc Ninh. Camera/timing bên dưới là PROPOSAL; nhận xét trade-off là OPINION, feasibility là HYPOTHESIS cần media.

- Giữ địa lý R-T08: máy đối diện cạnh hai người, Khoai screen-left và Đào screen-right ở mọi shot. Trục nối hai người; mọi vị trí máy ở cùng phía trước bàn, không vượt trục/đảo trái phải. Máy khóa, không orbit hoặc dựng360°.
- Eye-line: Khoai nhìn xuống đĩa rồi sang phải tới Đào; Đào nhìn xuống món rồi sang trái tới Khoai. Quay lấy cốc nhìn ngoài screen-right; quay lại phải bắt được cả đũa/miếng nem và mặt Khoai. Không nhìn thẳng lens.
- `WORKING_ASSUMPTION W-HAND`: Khoai dùng tay phải cầm đũa theo hướng I03/I05; tay trái nghỉ cạnh bát. Đào dùng tay trái định kéo đĩa và đưa bát; tay phải lấy cốc ngoài phải; đôi đũa Đào nằm trên bàn. Đây là choreography đề xuất, không canon tay thuận.
- `WORKING_ASSUMPTION W-PROP`: đĩa chỉ có ý định kéo, dừng khi Khoai nói “Khoan”, vẫn vùng giữa; Đào nhấc cốc rồi đặt lại đúng chỗ trước đưa bát, không uống. Bát Đào đầu cảnh chưa có phần nem nhận; không thêm thức ăn khác. Không thêm cuốn/chấm/nhai/ăn.
- P0 = ụ nem ban đầu, A = phần gắp đầu, B = phần khác ở kết; không lượng gram/count miếng suy từ still. Lá/chấm/bát Khoai/cốc và đôi đũa Đào không tự dịch/nhân đôi. Từ S04 có P0−A; cuối S05 P0−A−B, A ở bát Đào, B trên đũa Khoai, chưa chạm miệng.
- Framing đề xuất crop bớt nền/ghế của R-T08 để thấy mặt và đường đũa/bát/cốc, giữ layout/ánh sáng; đây chưa owner-approved crop. Native 768×1376 theo78 chưa exact 9:16; P8/P11 kiểm transform không cắt tay/cốc/watermark. Không coi kích thước ref là delivery.

## Hai coverage options cho ăn vụng → bị thấy → chữa cháy

| Option | Coverage / lợi ích | Trade-off / điều kiện |
|---|---|---|
| A — causal two-shot liên tục | S04 giữ từ Đào quay lấy cốc, Khoai gắp về miệng, Đào quay lại, khựng, đổi hướng tới nhận bát. Hai mặt và toàn đường A luôn trong cùng khung; ít nguy cơ cắt mất nguyên nhân. | TARGET10–14s vượt native4/6/8s trong source13; **không một native request10–14s**. Chỉ giữ liên tục nếu P8 chứng minh route-supported extension/assembly nối usable; extend trong bảng chỉ Lite, chưa account proof. Nhiều tay/props/thoại có risk drift. |
| B — chia coverage có bridge | B1 two-shot từ lấy cốc tới A đang về miệng, Đào quay lại, khựng và câu “Chờ em quay lưng nữa à?”; TARGET4–6s. B2 cùng phía trục, match A dừng ngoài miệng rồi đổi hướng, hai câu còn lại và nhận bát; TARGET6–8s. | Giảm tải một đoạn nhưng thêm join rất nhạy về A/grip/mặt/cốc, dễ biến thành gắp cho cô từ đầu. Đầu B2 phải match state B1, không khởi động từ neutral v0.8. Không cut chỉ tay/reaction, không lặp gắp/thoại. Ranges vẫn chưa audio-tested; không coi chắc fit4/6/8s. |

Khuyến nghị sơ bộ A cho paper plan vì ý định ăn và đổi hướng cùng bằng chứng hình; owner chưa chọn. Nếu actual visibility/native workflow không đủ, trình B với join evidence, không âm thầm cắt mất nguyên nhân hoặc đổi lời. S01–S05 là đơn vị coverage logic, **không phải** năm native requests hoặc số clip khóa; P8 xác định request units/feature/duration/count/cap bằng bằng chứng hiện hành.

Feature evidence bổ sung13: text/frames-to-video4/6/8s; Ingredients Lite/Fast8s, Quality unsupported; extend chỉ Lite theo bảng. Đây Google docs do root kiểm, account UI/cost/audio vẫn UNKNOWN; không đổi sang Omni. A là ưu tiên ngữ nghĩa có dependency kỹ thuật, chưa route thực thi thắng B. P8 phải đối soát mode/refs/keyframes, không gom tính năng khác nhau vào một request. R-T08 **neutral pre-action** chỉ phù hợp baseline S01; S04/S05 hoặc B2 đã có đũa/miếng nem/bát/cốc hoạt động cần start-state riêng, không gọi neutral v0.8 là action keyframe.

## Shot table — option A khuyến nghị, chưa duyệt

Duration dưới là khoảng `TARGET`, không MEASURED hoặc giới hạn native. Tổng mục tiêu 25–35s hướng tới khoảng 30s; khả năng vừa 30s `UNKNOWN` trước tiếng/diễn thực. Không nén thoại để đạt bảng.

| Shot / source32 / intent | Frame, camera, eye-line / action và exact lời | TARGET | Start → end states | Audio/cue / join / deps |
|---|---|---|---|---|
| S01 /9–15 / món + Khoai bị mùi giữ lại | Two-shot rộng đủ bàn và cốc, phía trước như R-T08. Khoai hơi nghiêng nhìn/ngửi món, chưa cầm phần nem; Đào chuẩn bị ăn, nhìn Khoai. Đào: “Anh nhìn mãi. Không hợp thì để em.” Tay trái định kéo đĩa; Khoai: “Khoan. Mùi này làm anh nhớ cái chảo.” | 4–6s | R-T08 neutral, P0, đũa trên bàn, cốc ngoài phải, bát ở chỗ → đĩa dừng vùng giữa, tay Đào gần mép đĩa; Khoai nhìn sang Đào, không food-contact. | F01 ở món mở cảnh; nhãn AI theo cue dưới. Ambience quán thấp, không nhạc riêng. J12 cắt sau “chảo” đủ đuôi âm, đúng đĩa/tay; D1/D2/D5. |
| S02 /17–19 / hỏi và kể ký ức qua lời | Two-shot trung cùng phía trục; hai mặt + bàn, không đổi set. Đào nhìn trái: “Nem thì đây. Chảo ở đâu?” Khoai nhìn cô: “Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ.” Không chèn chảo/bếp/mẹ. | 6–8s | Kế S01, Đào thu tay trái về cạnh bát, đĩa/P0 không đổi, tay Khoai không cầm nem → hai người đối thoại, tất cả props giữ. | F02 cùng mạch liên tưởng, không minh họa nguyên liệu như proof. J23 cùng eye-line/tư thế; không cắt trong câu; D1/D2/D5. |
| S03 /21–23 / setup ăn vụng | Two-shot trung, cùng máy; Đào trêu tò mò: “Chờ ăn?” Khoai tỉnh: “Chờ mẹ quay lưng.” Giữ reaction vừa đủ, không wink/hoảng/romance. | 3–4s | Như S02, P0 và đũa trên bàn, cốc nguyên chỗ → Khoai kết câu, Đào chuẩn bị quay ngoài phải; chưa gắp nem. | Không nhạc gag, không SFX thay ý. J34 vào frame rộng **trước** quay lấy cốc; khớp tay/cốc/P0 và không lặp câu; D1/D2. |
| S04 /25–37 / chứng kiến toàn causal payoff và Đào hiểu | Two-shot trung rộng khóa, đủ miệng Khoai/đũa/A, mắt Đào, cốc ngoài phải và bát. Đào quay lấy cốc tay phải; Khoai nhanh nhấc đũa tay phải, gắp A về miệng. Đào quay lại, Khoai khựng nhẹ khi A vẫn tách miệng. Đào: “Chờ em quay lưng nữa à?” Khoai đổi hướng **trước contact**, bình thản đưa A về phía cô, theo vùng bát; Khoai: “Anh gắp cho em mà.” Đào nhìn A rồi anh, đặt cốc lại, đưa bát tay trái ra nhận; Đào: “Thế em quay lại đúng lúc rồi.” | 10–14s | P0, đũa Khoai trên bàn, cốc ngoài phải/bát Đào tại chỗ → P0−A, A vẫn kẹp đũa Khoai phía trên bát Đào đang đưa ra; cốc trở lại vị trí; Đào hiểu/trêu, không mở miệng chờ đút. | Không F01/F02 mới che payoff; giữ AI nhỏ theo cue. Thoại không chồng/nhai. J45 giữ A chưa thả, match bát/tay/hướng đũa và hai eye-lines, không duplicate transfer; D1/D3/D4/D5. |
| S05 /39 / nhận món và kết | Cùng góc/crop S04 để nối; Khoai đặt A vào bát cô, Đào cười nhẹ. Khoai rút đũa, tự gắp B từ đĩa. Kết ngay sau gắp, không đưa B vào miệng/ăn thêm. | 2–3s | A còn trên đũa trên bát đưa ra, P0−A → A trong bát Đào, B trên đũa Khoai/P0−A−B; Đào giữ bát, cốc nguyên chỗ, props còn lại không đổi. | Không thoại thêm; tiếng đặt món/đũa nếu có phải tự nhiên, không che đuôi câu trước. Đủ giữ kết sau B để cut sạch; D3/D4/D5. |

## Cue chữ, audio và hướng dẫn nối cho Canva

- C-F01 exact: “Nem Bùi — gắn với Bùi Xá, Bắc Ninh.” TARGET hiển thị lúc S01 món rõ; không ngụ ý đĩa fiction có xuất xứ thật. Chưa có in/out measured hoặc reading pass.
- C-F02 exact: “Thính gạo rang góp một phần vào mùi vị của Nem Bùi.” TARGET bắt đầu ở “Mùi này…” S01 và qua mạch rang gạo S02; F01 kết trước F02 để giảm cạnh tranh. Không bỏ “góp một phần”; nếu đọc thiếu, điều chỉnh cue/timeline hoặc trình owner, không rút câu tự ý.
- C-AI exact: “Video được tạo bằng AI.” PROPOSAL hiện từ S01 và xuyên pack ở vùng trống cùng vị trí; watermark giữ. Setting disclosure nền tảng và fiction boundary riêng, không coi nhãn AI đã giải thích ký ức là fact.
- Layout các cue là hậu kỳ theo35, clips sạch không burn text sinh máy; owner ghép Canva. Chọn vùng trống sau kiểm frame/crop/UI thực, không bịa safe-zone pixels. Subtitles nếu owner dùng không che mặt/đũa/món/bát/cốc; chữ F02 có nguy cơ quá tải cần AV/Fact/P11/P12 đọc thử trên export.
- Audio continuity: cùng hai giọng hướng38, ambience thấp ổn định; không ép một nhạc nền riêng mỗi clip. Không crossfade/chồng thoại tạo sai người hoặc cắt âm cuối. Có thể giữ ambience qua cut nếu actual audio cho phép, chưa có file rời/SRT/nhạc/rights.
- Clip-pack về sau theo35: order S01→S05, tên take `EP01_Sxx_Txx_vN`, selected/rejected/needs_fix + QC; in/out và duration sử dụng đo trên take thật, matching start/end theo bảng, cue theo timeline dựng thực. Logical shots có thể dùng nhiều hoặc ít source clips; không tự chọn take thay owner, không tự dựng master.
- J12/J23/J34/J45: lưu actual boundary frames + câu/âm đầu cuối và proposed edit handles sau media. Cắt ở trạng thái giữ có thể đối soát; không timecode hoặc số frame tưởng tượng. S04→S05 không được nối A đã trong bát sang A còn trên đũa; nếu không match, hold/rework hoặc trình coverage B.

## Dependency nhỏ nhất theo shot, keyframe briefs và acceptance

| ID / shots | Input còn thiếu / task nhỏ nhất / closure và route |
|---|---|
| D1 / S01–S04 | VOICE map9 exact câu rồi actual samples/đối đáp qua request đúng quyền; AV nghe “cái chảo”, setup, chữa cháy/trêu và đo actual timing. Không mẫu người diễn/clone; tiếng đúng người/tự nhiên/không nhai; timeline thực quyết định≈30s. |
| D2 / S01–S03 | CHAR/CONT chỉ đối soát identity/outfit và biểu cảm chú ý/đối đáp ở góc ngồi đã chọn. R-P03/R-T08 đủ baseline; nếu chưa cover expression cụ thể, xin đúng still/keyframe liên quan, không bộ360° mặc định. |
| D3 / S04–S05 | Keyframe brief K4a: Đào ngoài phải với cốc, A đang về miệng Khoai chưa contact; K4b: Đào đã quay hiểu, A đổi hướng vẫn ngoài miệng, chưa đút; K4c: A trên bát Đào đưa ra; K5: A trong bát, Khoai gắp B. Đây chỉ briefs, chưa prompts approved/media. Dùng R-T08/P03/I03/I05; CHAR/ART/CONT kiểm angle/occlusion cụ thể. |
| D4 / S04–S05 | Bounded actual motion probe khi P8 approved: plate→miệng chưa chạm→đổi hướng→bát, giữ A/grip/bát/cốc; sau đó B riêng. PERF kiểm ý định ăn/Đào hiểu; CONT kiểm chuyển vật, không hai A/biến mất/contact rồi trao. Không cần motion PASS trước draft/probe planning. |
| D5 / all | P8 PROMPT/FLOW/RIGHTS kiểm actual feature/model/audio/cost và ref input rights/roles; lập exact request/count/cap/stop, owner duyệt trước chạy. P11/P12 kiểm kỹ thuật/crop/cue/watermark/nhịp actual. R-T08 chưa exact9:16, serving/reference authorization không independent commercial clearance. |

Acceptance paper: mọi dòng32:9–39 có shot, chín câu nguyên văn/đúng speaker; cơ chế joke32:25–37 hiện cùng causal coverage A; bát/cốc/tay/portion có start/end và join; không thay meaning/count/claim; timeline TARGET. Acceptance media tách riêng: xem/nghe actual clip và nối pack; owner chấp nhận; master cuối cần export thực theo35.

## Findings, limits và disposition

| Finding / rule / status / severity | Evidence, impact, action, route / owner need / closure |
|---|---|
| P7-01 / SHOT-1/2 / MET paper | Bảng map32:9–39 + boundaries43–46 giữ all lời/beat/cause; đây maker self-check, không reviewer PASS. Route independent FLOW/CONT paper review; owner chọn coverage sau report; closure79 exact + reviewer report + owner decision. |
| P7-02 / SHOT-3/4 / UNKNOWN / MAJOR | S04 nhiều hand/prop events; stills đã xem không chứng minh reach/transfer/expression. Route D3/D4; owner shot/ref/request selection; closure actual version-specific keyframes/probe và PERF/CONT. Không đòi lộ mọi ngón. |
| P7-03 / SHOT-5 + AV / UNKNOWN / MAJOR |32:56/38 media limits; chưa audio/video, target25–35s không≈30s measured. Route D1; owner workflow/timeline nếu cần; closure actual nghe/đo + edit timeline, không đổi thoại âm thầm. |
| P7-04 / Boundary + input / UNKNOWN / MAJOR |78 chỉ static/P7 paper;35 clip pack; frame chưa exact9:16. Source13 có docs4/6/8s nhưng S04 TARGET10–14s chưa route-supported continuous output; account/audio/cost/request/rights chưa verified. Route D5/P8 và alternative B, owner exact packet; closure exact mode/start-state/refs/rights/read-back/approval và actual join/technical media. |
| P7-05 / Cue readability / UNKNOWN / MAJOR |38 Q0; C-F01/F02/AI giữ exact nhưng layout/dwell chưa kiểm. Route P11 AV/Fact/P12; owner chấp nhận cue/export; closure chữ đọc đủ/không che hành động trên actual export. |
| P7-06 / Input discipline / DEFECT / MINOR | Role03 extraction vô tình lộ sections ngoài SHOT, đã disclosure/root biết; không dùng làm source verdict. Next dispatch trích đúng heading không greedy; closure root ghi actual access và reviewer độc lập đúng allowlist. |

Disposition: file79 KEEP_FOR_INDEPENDENT_PAPER_REVIEW; coverage A RECOMMENDATION_ONLY; W-HAND/W-PROP PROPOSED; all generation/voice/clip-pack/master claims HOLD. Không đóng P6 hoặc tự duyệt shot.
Change log v0.1: tạo mới từ exact source/approved refs; không thay upstream, không media mới, không timestamp/duration/hash giả.

## Handoff năm phần

1. **Đã xác định:** coverage toàn script/Q0; R-T08 quan sát thật là geographic baseline; causal payoff có A và B alternative; owner nhận clip pack có QC/order/state/audio/cue rồi tự dựng Canva35.
2. **Quyết định owner đã có:** C-v0.5/Q0, hướng giọng/hình38, primary45, grip62, food/serving theo71/75, static78 + quyền P7 paper. Chưa shot/coverage/request/voice approval.
3. **Giả định đang dùng:** W-HAND/W-PROP, máy cùng phía trục, crop chức năng, range TARGET và AI cue xuyên pack. Đây proposal cần review, không canon/feature promise.
4. **Còn mở:** independent shot review; visible path và reaction S04; audio thực/timing; clip joins/portion; crop/cue/rights/features/request. P6 chưa toàn bộ PASS; không media pack đã bàn giao/master PASS.
5. **Bước tiếp:** root kiểm completeness/read-back79 → reviewer paper độc lập coverage/action/join → trình owner coverage/choreography khi reviewable; đóng đúng D1–D5 và bounded P8 packet theo quyền. Sau actual media mới ghi selected takes/in-out/QC/join/cue cho Canva; master QC chỉ khi owner gửi export.
