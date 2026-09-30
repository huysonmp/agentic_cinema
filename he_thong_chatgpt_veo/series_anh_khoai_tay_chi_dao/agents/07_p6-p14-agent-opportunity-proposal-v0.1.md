# P6–P14 — Đề xuất vị trí agent theo đầu ra và khoảng trống

Ngày: 2026-09-30. Version: v0.1. Status: PROPOSAL_FOR_OWNER_REVIEW / NOT_IMPLEMENTED / NOT_AUTHORIZED_TO_GENERATE.

## 1. Bài toán và bằng chứng hiện trạng

EP01 đã được owner chấp nhận nội dung [C-v0.5](../episodes/ep01_pilot/32_p5-script-c-v0.5-approved-content.md), có [approval record](../episodes/ep01_pilot/33_p5-c-v0.5-owner-content-approval.md). Cần biến ký ức và cú chữa cháy thành hình/tiếng/video AI mà không mất câu chuyện, sai món hay rối tay–đũa–bát. Owner trực tiếp thao tác Flow, duyệt từng đầu ra trọng yếu; không mục tiêu tối ưu tự động hóa/tốc độ.

Đã kiểm local: bộ [runtime/stage map](quality_system/02_runtime-contract-and-stage-map-v0.1.md), [sáu role](quality_system/03_tier1-role-prompts-v0.1.md), [readiness](quality_system/06_flow-fixture-retest-and-runtime-readiness-v0.1.md), folder script_workroom và p2_fact_source_auditor. Có Fact/Dialogue/Creative agents đã chạy trên bản trước; Tier1 có prompt/rubric và fixture text, runtime owner review vẫn pending, production media chưa kiểm. Chưa tìm thấy contract chuyên biệt cho các maker visual/voice/storyboard/prompt/edit. Director cầu nối vẫn là đề xuất được ghi ở [25](../episodes/ep01_pilot/25_owner-creative-correction-and-a-v0.3-retention.md), chưa implement.

Không coi “chưa tìm thấy contract” là khẳng định không ai có thể làm việc đó. Khoảng trống là nhiệm vụ/đầu vào/đầu ra/tiêu chí/phân quyền chưa đóng gói để chạy và đánh giá nhất quán.

## 2. Cơ sở nghiên cứu công nghệ — không thay bằng chứng tài khoản

- Google Flow xác nhận mỗi model hỗ trợ feature khác nhau và yêu cầu kiểm model/resolution/credit trước generate: [Models & supported features](https://support.google.com/flow/answer/16352836?hl=en), kiểm ngày 2026-09-30. Không suy “full mode” hay 3000 credit thành tên model/tính năng hỗ trợ trong tài khoản owner.
- Flow có hướng dẫn tạo clip qua text/frames/reference và mô tả thao tác đầu vào: [Create videos in Flow](https://support.google.com/flow/answer/16353334?co=GENIE.Platform%3DDesktop&hl=en), kiểm cùng ngày. Chọn được workflow nào cho EP01 vẫn phải kiểm đúng model và UI account.
- Hướng dẫn Veo tổ chức ý định theo chủ thể/hành động, khung hình/chuyển động và audio: [DeepMind prompt guide](https://deepmind.google/models/veo/prompt-guide/), kiểm cùng ngày. Đây là hướng dẫn, không bảo đảm chuỗi gắp–đổi hướng–đặt vào bát thực hiện đúng.

Suy luận thiết kế của chúng ta: cần tách ý định sáng tạo, phương án shot, prompt thực thi và kiểm đầu ra. Đây không phải mô hình tổ chức bắt buộc do Google quy định, cũng chưa có bằng chứng tăng chất lượng pilot.

## 3. Bảy vị trí ưu tiên chuẩn bị cho P6–P9

Ưu tiên theo dependency, không cắt bớt quy trình. Đây là bảy contract đề xuất; role IDs chưa là agent đã triển khai. Các vai trò có thể dùng cùng nền mô hình nhưng context reviewer phải riêng, không giả độc lập hoàn toàn về thiên kiến.

### 1 — AG-CTD-01: Veo Creative–Technical Director

- Stage: nối P5 → P6/P7/P8; giải thích sai lệch khi P9/P10 có đầu ra.
- Input: exact approved script + brief/canon + model/feature evidence + refs/voice đã duyệt hoặc trạng thái thiếu.
- Output: beat-to-screen treatment; ý nghĩa phải giữ; rủi ro/chỗ cần thử; 2–3 phương án thể hiện có trade-off; decision memo cho owner.
- EP01: người xem phải thấy Khoai định ăn, rồi đổi hướng trước khi nem chạm miệng; Đào hiểu và nhận món, không mang vai mẹ/quản anh.
- Chất lượng: mỗi phương án giữ setup/payoff và quan hệ, phân biệt fact/hypothesis/probe; không bóp ý tưởng chỉ vì dự đoán model yếu.
- Ranh giới: maker/adviser, không final approver, không override P5/P6. Không tự chọn model/chi phí khi thiếu authority.
- Phối hợp AG-FLOW-01: CTD giữ ý định và trade-off; FLOW kiểm tải action, refs, join, feature/request. FLOW hiện có cả planning; không nhân đôi shot table. CTD cung cấp yêu cầu sáng tạo, một shot table do role shot chịu trách nhiệm, FLOW phản biện trên cùng version.

### 2 — AG-CHAR-01: Character Visual Designer

- Stage: P6, cập nhật có change-control khi cần.
- Input: approved character foundation, cấm romance/child targeting, style intent; ảnh demo chỉ là reference chưa canon.
- Output: phương án nguyên bản, character sheets nhiều góc, biểu cảm, tay/tỷ lệ/trang phục, nhận diện khác nhau, prompt tạo reference và asset IDs.
- EP01: mặt Khoai khựng rất nhẹ vẫn chín chắn; tay có cấu trúc ổn định để dùng đũa; Đào đáng yêu nhưng tự chủ và không bị làm thành trẻ nhỏ.
- Chất lượng: người xem nhận ra cùng nhân vật ở các góc và nét diễn; không dùng ảnh đẹp đơn lẻ thay consistency proof.
- Reviewer: CONT đối chiếu identity; RIGHTS kiểm provenance; owner khóa refs. Role không tự công bố thiết kế đã được bảo hộ/độc quyền.

### 3 — AG-ART-01: Food & Environment Art Director

- Stage: P6, hỗ trợ P7/P9 khi món/bối cảnh sai.
- Input: nguồn món cho phép, claim/source span, rights register, location/prop intent.
- Output: food appearance brief tách verified/uncertain, reference board dùng đúng quyền, set/prop layout, food/style frames và asset register. Mảng món và mảng set có checklist riêng; có thể dispatch context chuyên môn riêng nếu owner duyệt workflow.
- EP01: Nem Bùi phải nhận diện được; đũa, bát, cốc, đĩa có vị trí giúp thấy hành động chữa cháy. Không đưa landmark/nhãn hàng tùy tiện để “trông Bắc Ninh”.
- Chất lượng: không suy thứ nhìn thấy/texture/ingredients từ F02. Thiếu evidence hình món thì research intake trước khi khóa, không vẽ món theo tưởng tượng như fact.
- Reviewer: Fact/food fidelity, CONT và RIGHTS; owner duyệt. Nguồn đọc được không tự cho quyền upload ảnh làm ingredient.

### 4 — AG-VOICE-01: Vietnamese Voice & Performance Director

- Stage: P6 thiết kế/sample; P7 audio intent; P9/P11 sửa performance.
- Input: exact dialogue, character intent, pronunciation notes, audio workflow/account constraints.
- Output: voice briefs, performance notes từng câu, cách phát âm tên món/nơi, mẫu AI khi được phép, voice comparison và phương án native audio/post voice có trade-off.
- EP01: Khoai nói “Anh gắp cho em mà” bình thản nhưng lộ chữa cháy; Đào “Thế em quay lại đúng lúc rồi” trêu biết chuyện, không ngây thơ tin lời anh.
- Chất lượng: tự nhiên tiếng Việt, ổn định danh tính giọng, không nhấn như quảng cáo; đo nhịp trên audio/video thật, không kết luận từ đếm từ.
- Reviewer: Dialogue editor kiểm khẩu ngữ; AV kiểm audio thật/đồng bộ/caption; owner duyệt giọng. Role không tự đổi lời thoại hoặc hứa model giữ hai giọng hoàn hảo.

### 5 — AG-SHOT-01: Storyboard & Shot Director

- Stage: P7.
- Input: approved script, refs P6, CTD treatment, voice policy; thiếu gì phải ghi.
- Output: storyboard/keyframe briefs, shot list, screen geography, eye-line/action map, start/end states, edit intent và audio coverage. Không generate storyboard trước permission nếu cần công cụ media.
- EP01: ai nhìn đâu, tay nào cầm đũa, nem ở đâu trước/sau; đủ khung hình để thấy động cơ “định ăn” và cú đổi hướng, không cắt giấu mất trò đùa.
- Chất lượng: mọi beat có coverage, shot nối được; target duration tách native clip limit và thời lượng đã đo. Không mặc định long take hoặc montage tốt hơn trước test.
- Reviewer: FLOW kiểm feasibility; CONT kiểm state/ref dependencies; owner duyệt shot plan. Không tự sửa payoff để dễ quay.

### 6 — AG-PROMPT-01: Generation Package Engineer

- Stage: P8; revision request có lý do ở P9.
- Input: approved shot/ref/voice, verified active model/mode/features, approved count/cap, source/rights status.
- Output: request riêng từng shot với exact prompt, input asset/version IDs, start/end frame nếu workflow hỗ trợ, speaker/audio mapping, settings, candidate plan, fallback và generation log template.
- EP01: chỉ rõ nem chưa chạm miệng; đổi hướng sang bát Đào; không đút; không nhai khi nói. Đây là prompt intent, cần output test, không cam kết model tuân thủ.
- Chất lượng: prompt đối chiếu ngược script/shot, không đổi qualifier fact; request có provenance/version/cap. Nếu chưa biết feature/cost: UNKNOWN và không ready.
- Reviewer: FLOW + RIGHTS trước owner request approval; owner là Flow operator. Role không tự upload, gọi provider hay retry tiêu credit.

### 7 — AG-PERF-01: Narrative Readability & Performance Critic

- Stage: P9 candidate; P10 rough cut; re-check P11/P12 nếu timing thay.
- Input: media thực xem/nghe được + exact script/shot/refs. Lượt đọc lạnh có thể xem media trước maker rationale; sau đó đối chiếu script để giải thích lệch.
- Output: beat đọc được/không, diễn ý gì so với mục tiêu, frame/time evidence, candidate keep/rework/hold, finding route. Không dựng timecode khi không có media.
- EP01: người xem có hiểu miếng nem vốn dành cho Khoai? Có đọc câu chữa cháy như chữa cháy? Có hiểu Đào biết nhưng cho anh giữ thể diện? Có nhớ món/nơi/thính hay chỉ nhớ joke?
- Chất lượng: phân biệt “đẹp/ít lỗi” với “câu chuyện rõ/có duyên”; không dùng điểm tự chấm làm retention thật.
- Ranh giới với CONT/AV: PERF kiểm nghĩa và nhịp; CONT kiểm identity/object/time continuity; AV kiểm tiếng/đồng bộ/chữ. Không cho pass thay nhau. Không tạo lại candidate mình vừa review; owner chọn take.

## 4. Những vị trí tiếp theo — chuẩn bị trước khi đến stage, không bỏ

| Role đề xuất | Stage | Output maker phải bàn giao | Reviewer / quyền owner |
|---|---|---|---|
| AG-EDIT-01 — Assembly & Editorial Designer | P10 | take comparison, edit decision list, rough-cut plan, pickup list có lý do; dựng thật chỉ khi có media/tool và được giao | PERF/CONT/AV kiểm sequence, owner chọn và duyệt rough cut |
| AG-POST-01 — Sound, Caption & Finishing Designer | P11 | voice/SFX/music plan với rights, subtitle/caption timing, graphic/disclosure layout, finishing/export recipe; output thật khi có tool/input | AV/RIGHTS/Fact kiểm exact surface; owner duyệt thay đổi sáng tạo |
| AG-DELIVERY-01 — Delivery Package Coordinator | P13 | manifest, đúng master/version, source package, rights/disclosure notes, file inventory/checksum từ bytes thật | MASTER kiểm độc lập; owner nghiệm thu; không auto publish |
| AG-LEARN-01 — Pilot Experiment & Learning Analyst | P14 (định nghĩa phép đo trước P8) | thử nghiệm log, defect taxonomy, credit actual khi có log, lesson có evidence và revision đề xuất | owner duyệt thay đổi; không bật tự tối ưu/Tier2 hoặc đổi canon từ một candidate |

P12 không thêm một “QC tổng” trùng AG-MASTER-01: dùng MASTER/CONT/AV/RIGHTS và Fact/CULT đúng trigger. Delivery maker khác người kiểm bàn giao; POST maker khác AV reviewer. EDIT không thay quyết định owner về take/cut. Có contract không tự đồng nghĩa có công cụ dựng/đọc mọi định dạng media.

## 5. Lựa chọn tổ chức để owner chốt

### Quyết định A — Đội chuẩn bị đầu tiên

- A1: duyệt chuẩn bị cả bảy vị trí P6–P9, viết contract/prompt/fixture, mở run tuần tự khi đủ input. Hệ quả: phủ các khoảng trống tạo đầu ra và kiểm ý nghĩa từ đầu; nhiều role nhưng không chạy đồng loạt thiếu dependency. **Khuyến nghị sơ bộ** theo mục tiêu chất lượng của owner.
- A2: trước hết chuẩn bị CTD + CHAR + ART + VOICE; thiết kế SHOT/PROMPT/PERF khi sang P7/P8. Hệ quả: chia gói duyệt theo stage, nhưng phải hoàn tất các role còn lại trước video thử; không giảm chức năng/gate.

### Quyết định B — Ranh giới cầu nối với FLOW

- B1: CTD là creative maker/adviser riêng; FLOW giữ feasibility/planning kiểm tra kỹ thuật, phản biện artifact version do SHOT/PROMPT lập. Có nguy cơ thiên kiến model chung, cần context riêng và evidence. **Khuyến nghị sơ bộ**.
- B2: mở rộng FLOW thành cả director và planner. Ít handoff hơn nhưng dễ cùng context vừa đề xuất vừa tự đánh giá; cần một technical reviewer riêng nếu chọn. Không gọi đây là cải tiến đã chứng minh.

### Quyết định C — Lượt thử video đầu tiên (chỉ lập kế hoạch)

- C1: test đoạn payoff rủi ro tay–đũa–nem trước, rồi test toàn tập. Dễ khoanh nguyên nhân nhưng không đo được hiệu quả cả chuyện từ đoạn rời. **Khuyến nghị sơ bộ**; request/cap vẫn owner duyệt riêng.
- C2: rough cut cả tập trước. Có ngữ cảnh để đánh giá humor, nhưng lỗi nhiều shot có thể làm khó chẩn đoán. Không giả định chi phí/candidate count khi chưa có P8 evidence.

## 6. Giả định / điều phải kiểm trước kết luận

Giả định làm việc: sản xuất thủ công trên Flow, agent tạo tài liệu và kiểm bằng công cụ có thật; không tích hợp API. Bảy role mới và bốn role downstream mới là đề xuất, chưa owner approve/runtime test. Không gọi cải thiện chất lượng là kết quả đã đạt.

| Cần research / test | Task cụ thể | Đầu ra / gate |
|---|---|---|
| Model/mode/account feature thật | Owner cung cấp screenshot/read-back setting; đối chiếu docs Google ngày thực dùng | feature evidence register trước P8, không truy cập tài khoản khi chưa được giao |
| Food fidelity | ART đối chiếu nguồn hình/claim, ghi quyền từng asset | food reference pack P6 có fact/uncertain/rights |
| Hai giọng và sắc thái | VOICE đề xuất workflow; sample AI khi đủ permission | voice comparison P6, AV đọc/nghe thật; nếu tool không nghe được ghi NOT_TESTED |
| Cú đổi hướng nem có làm được và đọc được | CTD/SHOT/PROMPT lập probe hai cách quay giữ nghĩa; owner duyệt request, thao tác Flow | P9 candidate evidence + PERF/CONT/AV findings, không proof từ prompt |
| Nhịp 30s và nhớ chi tiết thính | rough cut/audio AI thật, kiểm timing; cold interpretation và owner judgement, tách khỏi số liệu người xem thật | finding P10/P12; nếu cần sửa script/text quay đúng stage |
| Chi phí/thất bại | Log từng request/candidate/credit thực, phân biệt plan/actual | P14 report; không ước lượng giả từ gói 3000 |

## 7. Chốt vòng đề xuất

- Đã xác định: nội dung C-v0.5 accepted; thiếu các maker downstream và critic chuyên đọc diễn ý trên media; reviewer Tier1 đã có nhưng chưa episode/media run.
- Đã chốt: chỉ approval nội dung và quyền lưu/commit/push; chưa approval triển khai các role đề xuất hay generation.
- Giả định: giữ P0–P14 và owner-operated Flow; một role có thể có nhiều lần run theo stage, không nghĩa tự chạy liên tục.
- Còn mở: A/B/C ở trên; runtime version Tier1; account features; media review tool coverage.
- Tiếp theo nếu owner chấp thuận: chuẩn bị contract/prompt/input-output/rubric/fixtures cho nhóm được chọn, trình version; đóng review P5, rồi mở P6 đúng dependency. Mỗi artifact/run/decision lưu ngay, commit/push theo nhóm việc; không gom hậu kiểm sau khi đã generate.
