# P0 — Project Foundation working draft

- **Ngày:** 2026-09-29
- **Trạng thái:** ready_for_owner_approval
- **Owner:** người dùng
- **Điều kiện đóng P0:** các quyết định D0.1–D0.6 được chốt, các task kiểm chứng có owner/gate, và không còn blocker về authority, quyền hoặc nguồn lực.

## 1. Project identity đã xác định

| Hạng mục | Baseline hiện tại | Trạng thái |
|---|---|---|
| Sản phẩm | Series TikTok gồm hai nhân vật AI: Anh Khoai Tây và Chị Đào | confirmed |
| Phương thức sản xuất | Toàn bộ nội dung/hình ảnh nhân vật được tạo bằng AI | confirmed |
| Chủ đề | Giới thiệu món ăn vùng miền | confirmed ở cấp category |
| Initial release scope | 10 video | confirmed |
| Thời lượng | Khoảng 30 giây/video | confirmed |
| Định dạng | Video dọc cho TikTok | confirmed; thông số export cần kiểm tra |
| Owner/final authority | Người dùng | confirmed |
| Nền tảng dự kiến | Codex/ChatGPT và Google Flow/Veo | confirmed ở cấp định hướng |
| Nguồn lực Veo | Khoảng 3.000 credit/tháng theo thông tin owner cung cấp | declared; cần read-back trong Flow |
| Cách vận hành Veo ban đầu | Owner thao tác Flow thủ công | confirmed từ vòng trước |
| Ưu tiên | Chất lượng, quyền kiểm soát và bàn giao; không tối ưu trước cho tốc độ/tự động hóa | confirmed |

## 2. Cấu trúc project đề xuất

```text
he_thong_chatgpt_veo                       # hệ thống/quy trình
└── series_anh_khoai_tay_chi_dao           # một series project
    ├── series foundation và shared assets
    ├── character canon: Anh Khoai Tây
    ├── character canon: Chị Đào
    ├── episode 01 … episode 10
    └── shared registers / QC / delivery / retrospective
```

Mỗi episode là một workflow P2–P14 riêng nhưng dùng chung P0, series bible và character canon đã duyệt. Nếu foundation thay đổi, impact analysis phải chỉ ra episode nào cần review lại.

## 3. Sáu quyết định P0

### D0.1 — Audience và project promise — **confirmed**

Cần xác định:

- audience chính: độ tuổi, khu vực/ngôn ngữ và mức hiểu biết về ẩm thực;
- ưu tiên `giải trí`, `khám phá kiến thức`, `gợi ý trải nghiệm`, hay kết hợp;
- sau 30 giây, người xem cần nhớ/cảm thấy/làm gì;
- phạm vi địa lý của 10 tập đầu: toàn Việt Nam, theo miền, hay một danh sách địa phương cụ thể.

**Decision:** Khán giả chính là người trẻ yêu thích món ăn và văn hóa vùng miền, muốn tiếp cận chủ đề theo cách mới, chill, thú vị và giàu tính giải trí qua tạo hình AI đáng yêu. Sau mỗi tập, người xem cần nhớ được địa phương và món ăn cùng ít nhất một nét đặc trưng đúng. Phạm vi mở đầu là Bắc Bộ, trước mắt gồm Hà Nội, Hải Phòng và Bắc Ninh. Cách gọi tiểu vùng chính xác sẽ được research ở P1/P2, không khóa nhầm toàn bộ thành “Đông Bắc”.

### D0.2 — Character/IP foundation — **confirmed**

P0 chưa cần thiết kế ngoại hình chi tiết, nhưng phải chốt:

- Anh Khoai Tây và Chị Đào là nhân vật nguyên bản hoàn toàn, không dựa trên người thật hoặc nhân vật có bản quyền;
- ai sở hữu và được phép sử dụng character design, voice, tên và catchphrase;
- có cho phép nhân vật nhắc đến nhà hàng/nhãn hiệu/người thật không;
- giới hạn nội dung: ngôn ngữ, bạo lực, tình dục, định kiến vùng miền, trẻ em và quảng cáo;
- nguyên tắc disclosure nội dung AI trên video/caption nếu áp dụng.

**Decision:** Anh Khoai Tây và Chị Đào là nhân vật nguyên bản, không dựa trên người thật hoặc IP bên thứ ba. Toàn bộ thiết kế, giọng, tên và catchphrase thuộc project. Hai nhân vật chưa được xác định là một cặp đôi; quan hệ/dynamic sẽ được xây tại P1. Không nhắc hoặc mô phỏng nhãn hiệu/nhà hàng cụ thể. Không hướng nội dung tới trẻ em, không dùng định kiến hoặc miệt thị vùng miền, và phải disclosure nội dung do AI tạo. Cụm “không cần có bản quyền” được chuẩn hóa thành “không sử dụng IP bên thứ ba”; project không từ bỏ quyền đối với tài sản nguyên bản của mình.

### D0.3 — Factual và cultural quality policy — **confirmed**

Vì series giới thiệu món ăn vùng miền, cần quy định:

- claim nào bắt buộc có nguồn: nguồn gốc, địa phương, nguyên liệu, cách ăn, lịch sử, danh xưng “đặc sản”, giá trị dinh dưỡng;
- khi các vùng/nguồn có cách giải thích khác nhau thì trình bày thế nào;
- có cần reviewer hiểu văn hóa/ẩm thực cho từng tập hay chỉ dùng source audit;
- phân biệt fact, giai thoại, ý kiến và lời thoại hài hước;
- câu nào không đủ bằng chứng phải bỏ, làm mềm hoặc gắn uncertainty.

**Decision:** `knowledge phổ thông có yếu tố văn hóa`. Research và tư liệu phải đầy đủ, có thể truy xuất nguồn. Không đưa dinh dưỡng vào phạm vi mặc định. Claim trọng yếu phải có nguồn; tách fact, giai thoại, ý kiến và lời thoại hài hước. Khi có nhiều cách diễn giải, không tuyên bố một phiên bản là duy nhất nếu evidence không hỗ trợ. Thêm reviewer khi chủ đề nhạy cảm hoặc nguồn mâu thuẫn. Checklist chi tiết được tạo theo từng episode.

### D0.4 — Delivery package và Definition of Done — **confirmed**

Đề xuất baseline `Audit-ready` cho 10 tập thử nghiệm:

- master video đã QC;
- project/edit source và asset dùng trong bản cuối;
- caption, cover/thumbnail brief và metadata đăng nếu có;
- series/episode brief, script, visual/shot/generation package;
- raw candidate và select/reject log;
- prompt/reference/model-mode-setting/credit log;
- source/evidence/rights manifest;
- QC report, approval/change/exception record;
- delivery manifest và retrospective.

Một episode chỉ `DONE` khi master được owner `ACCEPTED`, package đã read-back và retrospective hoàn tất. `DONE` không đồng nghĩa `PUBLISHED`.

### D0.5 — Credit, lịch và exception policy — **confirmed cho pilot 01; batch policy deferred**

Với 3.000 credit/tháng và scope 10 video, chưa nên chia đều ngay khi chưa biết cost thực tế của mode. Cần chốt:

- 10 video phải hoàn thành trong một tháng hay có thể trải qua nhiều tháng;
- planned credit envelope cho toàn bộ batch;
- tỷ lệ reserve cho character/style tests, failed generations và critical rework;
- ai được phép duyệt vượt planned budget (mặc định: owner);
- điều kiện dừng generation để quay lại script/visual/shot plan.

**Decision:** trước mắt sản xuất một video pilot cho chuẩn, không đặt cap credit làm điều kiện tối ưu. Mọi generation vẫn phải được log để tạo baseline. Sau retrospective pilot 01 mới lập policy credit cho batch còn lại; không mặc định chia đều 3.000 credit cho 10 tập.

### D0.6 — Operating model và source of truth — **confirmed**

Baseline đề xuất:

- Codex Orchestrator duy trì workflow state, dependency và register;
- mỗi stage dùng Maker Agent chuyên biệt + Critic Agent độc lập;
- owner duyệt mọi stage trong pilot đầu; chưa gộp/bỏ gate;
- Flow chỉ được thao tác từ generation package đã duyệt;
- mọi agent output là proposal;
- Markdown/JSON/CSV trong project folder là source of truth;
- artifact được version, bản approved không ghi đè;
- raw media lưu ngoài Git nhưng có manifest, ID và checksum/path;
- mọi override/exception của owner được ghi rationale.

**Decision:** áp dụng toàn bộ baseline trên. Owner tự lưu trữ và xử lý project trong folder `series_anh_khoai_tay_chi_dao` do Codex tạo. Giữ toàn bộ raw candidate của pilot; retention cho batch sẽ được chốt sau retrospective pilot.

## 4. Task bắt buộc kiểm tra thực tế — không yêu cầu owner trả lời bằng phỏng đoán

| ID | Task | Khi nào phải hoàn tất | Bằng chứng |
|---|---|---|---|
| R0.1 | Read-back tài khoản Google Flow | trước khi khóa credit policy/P8 | model, mode, duration, resolution, feature và credit cost hiển thị thực tế |
| R0.2 | Kiểm tra yêu cầu TikTok hiện hành | trước khi khóa delivery/export specification | aspect ratio, resolution, codec, duration, safe area, disclosure/upload requirement liên quan |
| R0.3 | Kiểm tra data/usage terms của công cụ | trước khi đưa asset thật vào provider | điều khoản hiện hành và hạn chế sử dụng phù hợp |
| R0.4 | Chọn nơi lưu raw media/project edit | trước Pilot 1 | path, dung lượng, backup, naming, checksum/read-back test |
| R0.5 | Chọn tool hậu kỳ | trước P10/P11 | khả năng dựng dọc, audio, subtitle, export và lưu project source |

## 5. Artifact P0 cần hoàn thiện sau khi D0.1–D0.6 được chốt

1. Project charter.
2. Scope và hierarchy system/series/episode.
3. Roles, agent responsibility và approval matrix.
4. Quality/risk policy.
5. Character/IP/rights policy ở cấp project.
6. Source-of-truth, naming, version và retention policy.
7. Credit/generation/exception policy.
8. Delivery package và Definition of Done.
9. Research/verification task register.
10. P0 review của Critic và approval record của owner.

## 6. Điều kiện P0 được clear

- D0.1–D0.6 có decision và rationale.
- Không còn blocker về authority, ownership, risk policy hoặc source of truth.
- R0.1–R0.5 có owner và gate phải hoàn tất; những task chưa đến hạn không chặn P0.
- Governance Agent tạo đủ Project Foundation Pack.
- Risk/Quality Critic review và mọi blocker/critical finding được xử lý.
- Owner phê duyệt đúng version của P0 pack.

## 7. Trạng thái cuối vòng hiện tại

### Đã xác định

- Identity, owner, tool direction, nguồn lực dự kiến và batch 10 video.

### Chưa chốt

- Tên thương hiệu chính thức của series; hiện dùng working title “Anh Khoai Tây & Chị Đào”.
- Phân loại tiểu vùng văn hóa chính xác và danh sách món/tỉnh cho 10 tập; xử lý tại P1/P2.
- Credit policy cho batch sau pilot 01.

### Có thể tạm giả định

- Character nguyên bản, family-friendly, không mô phỏng người thật, không dùng brand chưa duyệt.
- Knowledge phổ thông có evidence và cultural sensitivity.
- Audit-ready trong batch thử nghiệm.

### Phải kiểm tra thực tế

- R0.1–R0.5.

### Bước tiếp theo

Owner review `series_anh_khoai_tay_chi_dao/00_governance/07_p0-review-and-approval.md`. Nếu đồng ý, ghi quyết định `APPROVED` để đóng P0 và chuyển sang P1.
