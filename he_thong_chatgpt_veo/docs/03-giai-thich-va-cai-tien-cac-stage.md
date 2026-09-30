# Giải thích 15 stage và các giả thuyết chưa kiểm chứng

- **Ngày:** 2026-09-29
- **Trạng thái:** superseded as a design proposal — phần mô tả stage còn giá trị tham khảo; các thay đổi quy trình chưa được chấp nhận
- **Mục tiêu hiện tại:** lưu lại diễn giải stage và các giả thuyết từng được đề xuất để kiểm chứng, không coi chúng là cải tiến đã có bằng chứng.

> **Hiệu chỉnh 2026-09-29:** Tài liệu này đã đề xuất quá sớm việc gom phase và giảm formal gate từ 15 xuống 6 khi chưa có pilot, số liệu defect/rework, thử nghiệm agent chuyên biệt hoặc quan sát tải human review. Vì vậy không dùng cấu trúc 5 phase/6 gate làm baseline. Baseline hiện tại giữ đầy đủ P0–P14 và quyền kiểm soát tại từng stage. Xem `04-hieu-chinh-va-kham-pha-human-ai.md`.

## 1. Đánh giá khung 15 stage hiện tại

Khung hiện tại có đủ vòng đời từ foundation đến retrospective. Điểm mạnh là không coi generation là trung tâm duy nhất và có stage riêng cho research, visual design, generation planning, QC và delivery.

Tuy nhiên, nếu áp dụng máy móc sẽ có bốn rủi ro:

1. **Quá nhiều gate hình thức:** nếu stage nào cũng đòi owner duyệt như nhau, người duyệt sẽ mệt và approval mất ý nghĩa.
2. **Phát hiện tính bất khả thi quá muộn:** concept/script có thể rất hay nhưng khó tạo nhất quán bằng Veo; đến P9 mới biết sẽ gây rework lớn.
3. **Master QC trở thành nơi bắt mọi lỗi:** lỗi brief, fact, continuity hoặc shot coverage đáng lẽ phải bị chặn sớm.
4. **Retrospective không quay lại hệ thống:** nếu lesson không cập nhật template/rubric/test case, tập sau vẫn lặp lỗi.

### Các giả thuyết kiến trúc đã nêu nhưng chưa được kiểm chứng

- Gom 15 stage thành 5 phase để điều hướng tài liệu.
- Giảm số formal human gate và thay một số gate bằng exit check.
- Cho phép feasibility probe có kiểm soát trước production lock.
- Gắn lỗi downstream với `origin_stage`.
- Buộc retrospective cập nhật checklist, rubric, template hoặc test case.

Chỉ hai ý cuối có cơ sở trực tiếp từ yêu cầu truy vết và học qua vòng lặp, nhưng cách triển khai vẫn cần pilot. Việc gom phase, giảm gate và thêm probe hoàn toàn chưa đủ bằng chứng để gọi là cải tiến.

## 2. Phương án 5 phase và 6 formal gate đã bị rút khỏi baseline

| Phase | Stage | Formal gate |
|---|---|---|
| A. Foundation | P0–P2 | G0 — Series/project readiness |
| B. Editorial design | P3–P5 | G1 — Episode brief lock; G2 — Script lock |
| C. Production design | P6–P8 | G3 — Generation release |
| D. Production & finishing | P9–P11 | G4 — Picture lock |
| E. Assurance & delivery | P12–P14 | G5 — Master acceptance |

Đây chỉ là một configuration có thể đưa vào thử nghiệm sau khi baseline đầy đủ đã chạy. Nó không phải kiến trúc được khuyến nghị hiện tại.

## 3. Cấu trúc chung của một stage

Mỗi stage về sau nên có một `stage card` với các trường:

```text
stage_id / episode_id
status: not_started | drafting | review | approved | rework | blocked | superseded
input_versions
owner / reviewer
required_outputs
quality_checks
open_issues
decision + rationale
approved_version / approved_at
downstream_impact_if_changed
```

Không được dùng từ `approved` nếu chưa chỉ rõ version nào được duyệt.

## 4. Giải thích từng stage và thực hành ứng viên

Các dòng mang nhãn **“Cải tiến”** bên dưới phải được đọc là **thực hành ứng viên cần test**, không phải kết luận tốt hơn baseline. Nhãn cũ được giữ để thể hiện rõ phần nào của đề xuất trước đã vượt quá bằng chứng.

### P0 — Project setup

**Mục đích:** tạo điều kiện để mọi quyết định sau có cùng phạm vi, người chịu trách nhiệm và định nghĩa hoàn thành.

**Đầu vào:** ý định xây series, tài khoản/công cụ có thể sử dụng, nguồn lực và ràng buộc ban đầu.

**Công việc chính:**

- xác định owner, reviewer và người thao tác công cụ;
- lập cấu trúc folder, naming và version convention;
- xác định loại nội dung, mức factual risk và dữ liệu nhạy cảm;
- định nghĩa “done”, “bàn giao” và trường hợp phải dừng;
- đặt nguyên tắc credit, quyền asset, retention và publish.

**Đầu ra:** project charter, responsibility map, definition of done, risk class, folder/index và register rỗng.

**Exit check:** không còn mơ hồ về ai được quyết định điều gì và output cuối dùng cho ai.

**Lỗi thường gặp:** bắt đầu chọn tool/agent khi chưa biết deliverable; coi mọi video có cùng mức rủi ro.

**Cải tiến:** thêm `content risk class` ngay P0. Fiction, knowledge và high-stakes dùng mức evidence/reviewer khác nhau; tránh áp quy trình nặng như nhau cho mọi tập.

**Đường trả lỗi:** nếu mục tiêu hoặc đối tượng bàn giao đổi, quay lại P0 và đánh dấu các decision downstream cần review.

### P1 — Series foundation

**Mục đích:** tạo “hiến pháp sáng tạo” để các tập cùng thuộc một series, không phải tập nào cũng nghĩ lại từ đầu.

**Đầu vào:** project charter, vùng chủ đề và định hướng của owner.

**Công việc chính:**

- xác định audience, need/tension và viewing context;
- viết series promise và reason-to-follow;
- chọn content pillars, engine lặp lại và phạm vi không làm;
- xác định tone, narrator/persona, format và nguyên tắc hình ảnh;
- lập tiêu chí nhận diện “đúng series” và “không đúng series”.

**Đầu ra:** series bible phiên bản đầu.

**Exit check:** có thể dùng bible để đánh giá một ý tưởng là fit, near-fit hay out-of-scope.

**Lỗi thường gặp:** bible chỉ chứa mỹ từ; audience quá rộng; visual style không liên hệ với giá trị nội dung.

**Cải tiến:** thêm 3–5 `negative rules`, ví dụ không giật gân sai fact, không đổi narrator giữa tập, không dùng visual đẹp nhưng làm sai nghĩa. Negative rules thường kiểm soát consistency tốt hơn mô tả phong cách dài.

**Đường trả lỗi:** feedback nhiều tập cho thấy promise/engine sai thì mở revision mới của series bible; không sửa âm thầm.

### P2 — Research & evidence

**Mục đích:** xây nền sự thật và quyền sử dụng trước khi creative biến giả định thành lời khẳng định hoặc asset thành footage.

**Đầu vào:** series bible, đề tài hoặc hypothesis của tập.

**Công việc chính:**

- lập câu hỏi nghiên cứu và claim dự kiến;
- thu nguồn, đánh giá độ tin cậy, ngày và phạm vi hỗ trợ;
- phân biệt fact, inference, creative interpretation và unknown;
- lập asset/rights register;
- xác định claim cần expert review.

**Đầu ra:** evidence pack, claim register, source register và rights status.

**Exit check:** claim quan trọng có evidence hoặc được loại/viết lại; asset có quyền chưa rõ bị quarantine.

**Lỗi thường gặp:** thu quá nhiều nguồn nhưng không biết nguồn hỗ trợ câu nào; citation tồn tại nhưng không entail claim; dùng nguồn cũ cho thông tin dễ thay đổi.

**Cải tiến:** dùng `claim-first research`: lập claim inventory trước, rồi gắn evidence trực tiếp cho từng claim. Research vẫn mở xuyên suốt P3–P5; P2 chỉ tạo baseline chứ không giả vờ mọi câu hỏi đã đóng.

**Đường trả lỗi:** factual QC phát hiện lỗi phải quay lại claim register và mọi script/text/audio phụ thuộc claim đó.

### P3 — Episode brief

**Mục đích:** khóa điều tập này cần đạt trước khi tranh luận concept hoặc hình ảnh.

**Đầu vào:** series bible, evidence baseline và ý tưởng tập.

**Công việc chính:**

- xác định một audience moment cụ thể;
- khóa một thông điệp chính và tối đa 2–3 supporting points;
- xác định hook promise, desired viewer response và CTA nếu có;
- đặt duration band, format, factual/rights risks và success criteria;
- ghi rõ những điều tập này không cố giải quyết.

**Đầu ra:** episode brief.

**Formal gate G1:** owner khóa brief trước khi concept development.

**Lỗi thường gặp:** nhiều thông điệp cạnh tranh; hook hứa khác payoff; brief mô tả giải pháp thay vì vấn đề.

**Cải tiến:** thêm `one-sentence comprehension test`: sau khi xem, khán giả cần nói lại được điều gì trong một câu? Nếu không viết được câu này thì brief chưa sẵn sàng.

**Đường trả lỗi:** concept hoặc script không cứu được brief mơ hồ; phải quay lại P3.

### P4 — Concept development

**Mục đích:** tạo và so sánh các cách kể khác nhau trước khi đầu tư vào script/visual chi tiết.

**Đầu vào:** episode brief đã khóa.

**Công việc chính:**

- phát triển 2–3 concept thực sự khác nhau;
- với mỗi concept: logline, viewer journey, hook, payoff, visual metaphor, audio mode;
- đánh giá brief fit, originality, clarity, Veo feasibility, continuity risk và credit risk;
- ghi phương án bị loại và lý do.

**Đầu ra:** concept cards và concept decision record.

**Exit check:** chọn được concept thắng bằng cùng rubric; không chọn chỉ vì một ảnh đẹp.

**Lỗi thường gặp:** các concept chỉ khác wording; chọn theo taste tức thời; bỏ qua khả năng dựng thành sequence.

**Cải tiến:** thêm `pre-mortem`: giả sử concept thất bại, ba nguyên nhân khả dĩ nhất là gì? Nếu rủi ro nằm ở khả năng Veo, cho phép một feasibility probe nhỏ có cap và ghi rõ `non-final`.

**Đường trả lỗi:** nếu probe chứng minh concept không khả thi, quay lại so sánh concept; không cố generate vô hạn.

### P5 — Script & narrative

**Mục đích:** biến concept thành dòng thời gian có thể nghe, hiểu, nhìn và dựng được.

**Đầu vào:** concept được chọn, episode brief, claim/evidence.

**Công việc chính:**

- tạo beat sheet theo thời gian;
- viết voice-over/dialogue/on-screen text;
- gắn claim ID vào câu factual;
- kiểm tra hook, progression, payoff, CTA và nhịp;
- table read hoặc timed read;
- lập assumption/open-question list.

**Đầu ra:** beat sheet, timed script và factual trace.

**Formal gate G2:** khóa script/narrative trước production design.

**Lỗi thường gặp:** script đúng chữ nhưng quá dài; hình và lời nói trùng nhau; visual không có nhiệm vụ kể chuyện; sửa câu factual nhưng quên subtitle/shot liên quan.

**Cải tiến:** viết ba cột `time | audio/text | visual function`; mỗi visual phải có chức năng như establish, explain, contrast, reveal hoặc emotional beat. Chạy `silent test` và `audio-only test` để phát hiện sự phụ thuộc không chủ ý.

**Đường trả lỗi:** lỗi fact → P2; lỗi message → P3; lỗi concept → P4; lỗi wording/timing → sửa trong P5.

### P6 — Visual development

**Mục đích:** định nghĩa ngôn ngữ hình ảnh và các invariant phải giữ xuyên clip.

**Đầu vào:** script lock, series bible, approved assets/rights.

**Công việc chính:**

- tạo visual bible cho palette, lighting, texture, composition và camera language;
- định nghĩa character/location/prop identity cards;
- phân biệt canonical reference, style reference và inspiration only;
- tạo style frames/keyframes;
- lập continuity invariants và forbidden variations.

**Đầu ra:** visual bible, reference manifest, identity cards, style frames và continuity rules.

**Exit check:** reviewer có thể chỉ ra cụ thể điều gì phải giống và điều gì được phép biến đổi giữa shot.

**Lỗi thường gặp:** moodboard đẹp nhưng mâu thuẫn; reference chứa nhiều chủ thể thừa; không phân biệt style và identity; quyền asset không rõ.

**Cải tiến:** quản lý reference như dữ liệu: mỗi reference có ID, role, rights, source, crop/background note và shot áp dụng. Chọn một `hero frame` làm chuẩn thẩm mỹ, nhưng không biến một frame thành tiêu chuẩn duy nhất cho mọi góc máy.

**Đường trả lỗi:** reference không thể đạt continuity → quay P4/P5 để đổi cách kể hoặc giảm phụ thuộc nhân vật phức tạp.

### P7 — Shot design

**Mục đích:** chuyển narrative và visual system thành coverage đủ để dựng sequence hoàn chỉnh.

**Đầu vào:** timed script, visual bible, continuity rules.

**Công việc chính:**

- tách shot theo chức năng kể chuyện, không chỉ theo câu prompt;
- xác định duration intent, framing, action, camera, transition và audio relationship;
- lập shot dependency/continuity map;
- đánh dấu must-have, alternative và optional beauty shot;
- tạo edit map/animatic thô nếu có thể.

**Đầu ra:** shot list, continuity map, edit intent, coverage matrix và pickup strategy.

**Exit check:** nếu mọi must-have shot đạt, editor có thể dựng được câu chuyện không có gap.

**Lỗi thường gặp:** shot list là danh sách hình đẹp; thiếu establishing/reaction/transition; nhiều shot phụ thuộc một chi tiết khó giữ; không có phương án B.

**Cải tiến:** thêm `coverage matrix`: mỗi beat/script line được cover bởi shot nào, audio nào và fallback nào. Giảm single point of failure bằng alternative shot cho điểm kể chuyện quan trọng.

**Đường trả lỗi:** coverage gap → sửa P7; narrative gap → P5; style/identity gap → P6.

### P8 — Generation planning

**Mục đích:** biến shot design thành request Veo có thể kiểm tra trước khi tiêu credit.

**Đầu vào:** approved shot package và reference manifest.

**Công việc chính:**

- lập prompt package cho từng shot;
- ghi model/mode, duration, aspect, inputs, first/last frame hoặc ingredients;
- tách required constraints, creative latitude và negative constraints;
- dự kiến số candidate, thứ tự batch, stop rule và credit cap;
- kiểm tra rights, safety, continuity dependency và filename/output ID.

**Đầu ra:** generation manifest và generation-ready packet.

**Formal gate G3:** owner thấy chính xác request, asset và credit trước khi generate.

**Lỗi thường gặp:** prompt cố nhồi toàn bộ screenplay; không có version; đổi nhiều biến cùng lúc; generate shot khó trước khi khóa identity/style.

**Cải tiến:** dùng `one-variable experiment` khi test prompt; chạy theo dependency order—identity/style anchor trước, shot phụ thuộc sau. Mỗi shot có stop rule: đạt, đổi chiến lược, hoặc quay upstream; không chỉ “thử thêm lần nữa”.

**Đường trả lỗi:** request sai → P8; shot không khả thi → P7/P6; concept không phù hợp model → P4.

### P9 — Veo generation

**Mục đích:** thực thi request đã duyệt và thu candidate có provenance đầy đủ.

**Đầu vào:** generation manifest approved.

**Công việc chính:**

- thao tác đúng request/version trong Flow;
- ghi actual model/mode/settings, credit, thời điểm và output ID;
- lưu raw output không ghi đè;
- chấm nhanh technical defect, creative fit và continuity;
- mọi deviation khỏi manifest phải ghi lý do.

**Đầu ra:** raw candidates, generation log và exception record.

**Exit check:** candidate có thể truy về shot/request; reject có reason code; không có output “không biết tạo từ prompt nào”.

**Lỗi thường gặp:** prompt drift không ghi lại; chỉ lưu clip tốt; xóa evidence thất bại; regenerate vì cảm giác không rõ nguyên nhân.

**Cải tiến:** tạo taxonomy lý do reject: identity, motion, composition, continuity, artifact, audio, factual mismatch, safety hoặc brief mismatch. Taxonomy giúp biết nên sửa prompt, reference, shot hay concept.

**Đường trả lỗi:** theo reason code; không mặc định quay lại P8 cho mọi lỗi.

### P10 — Selection & assembly

**Mục đích:** đánh giá clip trong sequence thật, không chọn từng clip độc lập.

**Đầu vào:** candidates, shot/coverage matrix và timed script.

**Công việc chính:**

- shortlist bằng rubric, không chỉ taste;
- dựng rough cut sớm;
- kiểm narrative clarity, rhythm, continuity và audio/visual relationship;
- lập pickup list có mức độ critical;
- ghi selected/rejected/alternate và lý do.

**Đầu ra:** select log, rough cut, coverage report và pickup list.

**Exit check:** sequence đủ nghĩa và đủ coverage; mọi pickup đều gắn với defect/gap cụ thể.

**Lỗi thường gặp:** chọn clip đẹp nhất nhưng sequence rời rạc; regenerate khi edit có thể giải quyết; dùng hậu kỳ để che lỗi premise.

**Cải tiến:** đánh giá ở hai mức: `clip score` và `sequence contribution`. Một clip trung bình có thể là lựa chọn đúng nếu nối cảnh tốt hơn. Ưu tiên pickup theo critical path của câu chuyện.

**Đường trả lỗi:** thiếu coverage → P7/P8/P9; sai story → P5; mismatch style → P6; edit issue thuần túy → P10.

### P11 — Post-production

**Mục đích:** hoàn thiện hình, tiếng và chữ sau khi nội dung/coverage đã đủ.

**Đầu vào:** approved rough cut, audio/text assets và pickup đã xử lý.

**Công việc chính:**

- khóa picture trước các bước finishing khó đảo ngược;
- voice-over/dialogue edit, music/SFX và mix;
- subtitle/on-screen text, spelling và timing;
- color/visual consistency, transitions và cleanup;
- rights/credit check cho mọi asset mới.

**Đầu ra:** picture lock, audio mix, text track, project file và master candidate.

**Formal gate G4:** picture lock—sau gate này, thay narrative/shot phải mở change request.

**Lỗi thường gặp:** mix/color khi edit còn đổi lớn; text che subject/UI; dùng music/font/voice không rõ quyền; nhiều version tên mơ hồ.

**Cải tiến:** khóa theo thứ tự `content lock → picture lock → audio lock → text lock → finishing`. Dùng naming chứa episode, cut, revision và status; không dùng `final_final2`.

**Đường trả lỗi:** lỗi finishing sửa P11; lỗi coverage P10/P7; lỗi fact P2/P5; thay message phải mở lại G1/G2.

### P12 — Master QC

**Mục đích:** xác nhận master đáp ứng độc lập từng lớp chất lượng và không chứa defect nghiêm trọng.

**Đầu vào:** master candidate, brief/script/rights và delivery spec.

**Công việc chính:** thực hiện các pass tách biệt:

1. content/narrative;
2. factual/claim;
3. visual/continuity;
4. audio/loudness/pronunciation;
5. text/spelling/safe area;
6. technical/export;
7. rights/delivery completeness.

**Đầu ra:** QC report, defect list có severity/origin stage và master status.

**Exit check:** không còn blocker/critical; major defect chỉ được waive bằng exception của owner.

**Lỗi thường gặp:** xem một lượt và đánh giá mọi thứ; reviewer đã quá quen nội dung; lỗi được ghi nhưng không có severity hoặc owner.

**Cải tiến:** dùng pass độc lập và ít nhất một `fresh-eyes review` cho tập quan trọng. QC không tự sửa file; QC phát hiện, phân loại và route lỗi về owner/stage phù hợp.

**Đường trả lỗi:** theo `origin_stage`, sau sửa phải re-test phần ảnh hưởng và regression checks liên quan.

### P13 — Delivery

**Mục đích:** bàn giao đúng master cùng đủ context để sử dụng, sửa, chứng minh quyền và tránh nhầm version.

**Đầu vào:** master đã pass QC và delivery requirements.

**Công việc chính:**

- đóng gói master, thumbnail/caption nếu cần và project/source theo mức retention;
- tạo delivery manifest với checksum/version/status;
- kèm rights/usage notes, known limitations và exception;
- thực hiện read-back: mở file, kiểm duration, audio, text và danh mục;
- ghi acceptance hoặc rejection.

**Đầu ra:** delivery package, manifest, QC certificate và acceptance record.

**Formal gate G5:** master acceptance; publish là hành động riêng nếu sau này có.

**Lỗi thường gặp:** gửi đúng nội dung nhưng sai version; thiếu font/audio/source; không nói limitation; coi upload thành công là bàn giao thành công.

**Cải tiến:** dùng `delivery read-back` bắt buộc và checksum cho master. Tách `ready_for_delivery`, `delivered`, `accepted` và `published`; không gộp thành “done”.

**Đường trả lỗi:** package lỗi sửa P13; master lỗi quay P12/P11; content lỗi quay stage nguồn.

### P14 — Retrospective

**Mục đích:** biến kinh nghiệm của một tập thành năng lực hệ thống, không chỉ thành nhận xét.

**Đầu vào:** toàn bộ issue, decision, generation, QC, credit và acceptance log.

**Công việc chính:**

- so plan với actual: rework, credit, defect và decision;
- tìm defect leakage: lỗi sinh ở đâu, đáng lẽ chặn ở gate nào;
- phân biệt lỗi hệ thống, lỗi thực thi và creative experiment hợp lệ;
- chọn thay đổi cụ thể cho quy trình;
- cập nhật regression checklist/test case.

**Đầu ra:** retrospective, corrective actions và process change proposal.

**Exit check:** mỗi lesson quan trọng đã trở thành owner + thay đổi + cách kiểm chứng, hoặc được ghi rõ không hành động.

**Lỗi thường gặp:** chỉ ghi “prompt cần tốt hơn”; tối ưu theo một trường hợp hiếm; sửa process nhưng không version.

**Cải tiến:** giới hạn mỗi tập 1–3 cải tiến hệ thống quan trọng để tránh process phình vô hạn. Đo `first-pass acceptance`, `rework by origin stage`, `credit per accepted second` và `escaped defects`—không dùng tốc độ làm north-star.

**Đường trả lỗi:** process change ảnh hưởng series-wide phải tạo proposal và áp dụng từ version/tập xác định, không hồi tố âm thầm.

## 5. Sáu register xuyên suốt

| Register | Chức năng |
|---|---|
| Decision log | quyết định, phương án, rationale, approver, version |
| Claim/evidence register | claim, loại, nguồn, confidence, reviewer, nơi sử dụng |
| Asset/rights register | asset, owner/source, quyền, hạn chế, expiry, nơi sử dụng |
| Change/impact register | thay đổi upstream và artifact downstream phải review lại |
| Generation register | request, setting, input ref, output, credit, result/reason code |
| Defect/QC register | defect, severity, origin stage, detected stage, correction, regression |

Các register có thể là Markdown/CSV/JSON trước; chưa cần database.

## 6. Severity và quy tắc dừng

| Severity | Ý nghĩa | Quy tắc |
|---|---|---|
| Blocker | vi phạm quyền/safety, sai master/source, không thể bàn giao | dừng ngay |
| Critical | sai thông điệp/fact trọng yếu, lỗi phá trải nghiệm hoặc continuity chính | bắt buộc sửa và re-review |
| Major | ảnh hưởng rõ đến chất lượng nhưng có thể waiver có lý do | owner quyết định |
| Minor | polish, không làm sai nghĩa hoặc điều kiện bàn giao | ghi backlog hoặc sửa |

Không dùng “quality-first” để biến mọi minor thành blocker. Chất lượng được làm chủ bằng phân loại và quyết định minh bạch, không phải sửa vô hạn.

## 7. Các giả thuyết thay đổi cần có dữ liệu trước khi đánh giá

1. **Từ 15 approval xuống 6 formal gate:** chưa được chấp nhận; chỉ có thể xem xét khi dữ liệu cho thấy gate nào không bắt được lỗi hoặc không tạo quyết định hữu ích.
2. **Thêm feasibility probe:** phát hiện sớm giới hạn Veo mà không biến discovery thành generation vô hạn.
3. **Thêm origin-stage routing:** lỗi được sửa tận nguồn, không dồn sang hậu kỳ.
4. **Tách clip quality khỏi sequence quality:** chọn clip dựa trên đóng góp cho câu chuyện.
5. **QC nhiều pass độc lập:** tránh một lượt xem cảm tính.
6. **Delivery read-back:** bàn giao chỉ hoàn tất khi package mở/đọc lại đúng.
7. **Retrospective phải cập nhật hệ thống:** lesson trở thành checklist/rubric/template/test.
8. **Risk-based rigor:** fiction, knowledge và high-stakes không dùng cùng một mức kiểm soát.

## 8. Điều kiện nghiên cứu trước khi đề xuất thay đổi SOP

1. Chạy ít nhất một episode qua đầy đủ P0–P14 với agent support được ghi nhận.
2. Đo loại lỗi, stage sinh lỗi, stage phát hiện, số vòng rework và quyết định human override.
3. Test agent chuyên biệt ở từng stage thay vì giả định human tự thực hiện phần lớn công việc.
4. Chỉ đề xuất thêm/bớt/gộp gate khi biết gate nào bắt được lỗi gì.
5. Phân biệt cải tiến chất lượng với tối ưu tốc độ hoặc giảm công sức.

Thiết kế nghiên cứu thay thế được ghi trong `04-hieu-chinh-va-kham-pha-human-ai.md`.
