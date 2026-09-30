# Định hướng quality-first và khung quy trình kế thừa

- **Ngày:** 2026-09-29
- **Trạng thái:** proposed — cần chốt decision nền tảng trước khi viết SOP chi tiết
- **Nguồn học:** các tài liệu kiến trúc, nghiệp vụ, dữ liệu, safety, eval, vận hành và roadmap của dự án mẹ `agentic_cinema`.

## 1. Diễn giải đúng yêu cầu

Mini-project không nhằm tạo video nhanh nhất và cũng không lấy tự động hóa làm thước đo thành công. Mục tiêu là xây một **production operating system đủ quy trình**, thực thi tuần tự, có con người kiểm soát, để owner:

- biết mỗi đầu ra được tạo từ input và quyết định nào;
- không chuyển bước khi artifact trước chưa đạt;
- so sánh phiên bản và quay lại điểm quyết định đúng;
- kiểm soát tính đúng, tính nhất quán, quyền sử dụng và credit;
- nghiệm thu được master cuối và bộ hồ sơ bàn giao;
- biến lỗi của tập trước thành checklist/eval cho tập sau.

**North-star đề xuất:** tỷ lệ tập được owner chấp nhận ở final QC mà không phát hiện lỗi đáng lẽ phải bị chặn ở stage trước.

## 2. Nguyên tắc kế thừa từ dự án lớn

### Giữ bắt buộc trong mini-system

| Năng lực | Cách áp dụng thủ công trước |
|---|---|
| Source of truth | Folder dự án + Markdown/JSON có cấu trúc |
| Versioning | Không ghi đè bản đã duyệt; mỗi revision có ID, ngày, lý do |
| Provenance | Liên kết idea → source → brief → script → shot → prompt → clip → master |
| Human approval | Gate có checklist, quyết định `approve/rework/reject` và người duyệt |
| Rights/consent | Asset manifest trước khi đưa reference/voice/music sang provider |
| Structured output | Mỗi stage có template, field bắt buộc và tiêu chí completeness |
| Fail-closed | Thiếu field/quyền/bằng chứng quan trọng thì dừng, không tự suy diễn để đi tiếp |
| Evaluation | Creative rubric, factual review, continuity review và technical QC riêng |
| Cost control | Generation manifest ghi mode, số candidate, credit dự kiến/thực tế |
| Audit/decision log | Ghi điều đã chọn, phương án bị loại và lý do |
| Change control | Thay đổi upstream phải chỉ ra downstream artifact cần tái duyệt |
| Delivery manifest | Danh mục file, version, trạng thái duyệt, thông số và hạn chế sử dụng |

### Đơn giản hóa nhưng không bỏ

| Thiết kế production | Bản mini quality-first |
|---|---|
| Database nghiệp vụ | File có schema + index/manifest dự án |
| Workflow engine/state machine | Stage status trong Markdown/JSON + checklist chuyển gate |
| Approval token | Approval record do owner ký/chốt trong tài liệu |
| Cloud audit/logging | Decision log + generation log + change log |
| Automated eval suite | Rubric và test cases chạy thủ công/có Codex hỗ trợ |
| Observability dashboard | Bảng theo dõi lỗi, rework, credit và acceptance theo tập |
| Queued media jobs | Người dùng thao tác Flow theo generation manifest đã duyệt |
| CI/CD release gate | Readiness checklist trước generation, edit, export và delivery |

### Chưa cần kế thừa ở giai đoạn hiện tại

- Google ADK/Agent Engine, Cloud Run, database, RAG/vector store.
- Multi-agent runtime, MCP/A2A và tự động gọi API.
- Multi-tenant IAM, SLO/on-call, canary production và load testing.
- Auto-publish hoặc automation tối ưu throughput.

Các mục trên chỉ trở lại backlog khi giải quyết một pain đã quan sát, không vì mong muốn “hệ thống trông đầy đủ”.

## 3. Khung lifecycle chất lượng đề xuất

Đây là **process map cấp cao**, chưa phải SOP cuối cùng.

| Stage | Artifact chính | Quality gate | Nếu không đạt |
|---|---|---|---|
| P0. Project setup | project charter, folder/index, vai trò, definition of done | scope và authority rõ | làm rõ trước khi ideation |
| P1. Series foundation | audience, promise, content pillars, tone, format, series bible | series có khác biệt và lặp lại được | sửa định vị/format |
| P2. Research & evidence | source register, facts/claims, rights status | claim quan trọng có nguồn; asset dùng được | research thêm hoặc bỏ claim/asset |
| P3. Episode brief | mục tiêu tập, một thông điệp, hook, CTA/outcome | không mâu thuẫn series bible | revise brief |
| P4. Concept development | 2–3 concept, trade-off, concept decision record | concept phục vụ brief, khả thi với Veo | chọn lại hoặc thu hẹp |
| P5. Script & narrative | beat sheet, narration/dialogue, timing draft | logic, cảm xúc, clarity và factuality đạt | quay lại script/research |
| P6. Visual development | visual bible, character/location/prop refs, style frames | style và continuity đủ rõ; rights pass | sửa reference/style |
| P7. Shot design | shot list, continuity map, edit intent, audio plan | coverage đủ để dựng; không có gap logic | bổ sung/revise shot |
| P8. Generation planning | prompt package, input refs, model/mode, candidate plan, credit cap | G3: request cụ thể, hợp lệ, trong budget | không generate |
| P9. Veo generation | raw candidates + generation log | từng clip đạt creative, continuity và technical QC | regenerate có lý do hoặc sửa plan |
| P10. Selection & assembly | select log, rough cut, pickup list | sequence truyền đạt đúng và có nhịp | pickup/re-edit; không vá mù quáng |
| P11. Post-production | picture lock, voice, music/SFX, text/subtitle, grading | creative QC + factual QC + rights QC | trả đúng stage gây lỗi |
| P12. Master QC | export candidate + QC report | nội dung, hình, tiếng, chữ, thông số đều pass | rework và tạo master revision mới |
| P13. Delivery | master, thumbnail/caption nếu có, manifest, source package, rights note | owner acceptance | chưa bàn giao/publish |
| P14. Retrospective | issue log, credit report, lessons, regression checklist | bài học được chuyển thành thay đổi có owner | chưa đóng episode |

## 4. Luồng kiểm soát thay đổi

Mọi thay đổi phải xác định loại và phạm vi tái duyệt:

```text
Series bible thay đổi
  → kiểm tra lại mọi episode brief đang mở

Fact/source thay đổi
  → script → on-screen text/voice → shot liên quan → master QC

Character/style reference thay đổi
  → visual bible → shot/prompts liên quan → continuity QC → edit

Script/beat thay đổi
  → timing → shot list → audio plan → generation/pickup

Model/mode/prompt strategy thay đổi
  → generation test → so baseline → chỉ thay candidate liên quan
```

Nguyên tắc: không bắt đầu lại toàn bộ nếu thay đổi cục bộ, nhưng cũng không cho downstream artifact giữ trạng thái `approved` khi dependency đã đổi.

## 5. Mô hình chất lượng nhiều lớp

Không dùng một câu “video đẹp” làm tiêu chuẩn chung. Tách ít nhất sáu lớp:

1. **Content quality:** thông điệp, logic, insight, độ phù hợp audience.
2. **Factual quality:** claim, nguồn, mức chắc chắn, không bịa dữ kiện.
3. **Narrative quality:** hook, progression, payoff, nhịp và clarity.
4. **Visual quality:** composition, motion, style, artifact, character/object consistency.
5. **Audio/text quality:** voice, pronunciation, mix, subtitle, spelling và safe area.
6. **Delivery quality:** file đúng version/thông số, đủ quyền, manifest và khả năng truy vết.

Mỗi lớp cần rubric riêng và người phê duyệt rõ, dù trong pilot cùng một người có thể giữ nhiều vai trò.

## 6. Ranh giới agent, skill và con người — chưa thiết kế chi tiết

### Con người giữ quyền

- định vị, thông điệp, taste và creative intent;
- phê duyệt nguồn/quyền và risk exception;
- khóa brief/concept/script/style/shot/generation request;
- chọn clip, picture lock, master acceptance và quyết định publish.

### Codex có thể hỗ trợ

- điều phối stage/checklist và kiểm tra completeness;
- tạo phương án, phân tích trade-off, phát hiện mâu thuẫn;
- chuyển artifact upstream thành artifact downstream có cấu trúc;
- review theo rubric, lập danh sách lỗi và impact map;
- duy trì version/decision/change/generation/delivery log.

### Skill chỉ nên xuất hiện khi

- một stage đã có SOP ổn định;
- input/output contract và stop condition đã rõ;
- có template/rubric/test case để kiểm chứng;
- skill không tự vượt human gate.

Agent specialization chỉ xem xét sau khi có ranh giới trách nhiệm, dữ liệu và tiêu chí đánh giá độc lập.

## 7. Năm quyết định nền tảng cần chốt tiếp

### Q1 — “Bàn giao” nghĩa là bàn giao cho ai và để làm gì? — **Cần bạn trả lời**

| Phương án | Hệ quả |
|---|---|
| A. Chính bạn lưu và đăng TikTok | Package có thể gọn nhưng vẫn cần master, caption/thumbnail và hồ sơ nguồn |
| B. Bàn giao cho editor/đội content khác | Cần source package, naming, edit notes và pickup/change protocol rõ |
| C. Bàn giao cho khách hàng/brand | Cần acceptance criteria, quyền sử dụng, version sign-off và exception log chặt hơn |

### Q2 — Loại nội dung giải thích có mức yêu cầu sự thật nào? — **Cần bạn trả lời**

| Mức | Chính sách gợi ý |
|---|---|
| Creative/fiction | kiểm continuity và rights; không gắn nhãn claim thật |
| Knowledge phổ thông | claim quan trọng có nguồn; phân biệt fact và diễn giải |
| Chuyên môn/high-stakes | bắt buộc reviewer đủ năng lực; Codex không tự phê duyệt factuality |

### Q3 — Ai có quyền phê duyệt ở từng lớp chất lượng? — **Cần bạn xác nhận**

Giả định hiện tại: bạn là final approver cho toàn bộ. Cần biết có stage nào phải có reviewer khác, ví dụ chuyên gia nội dung, brand owner, editor hoặc người nắm quyền asset.

### Q4 — Bạn muốn lưu đến mức nào để có thể tái dựng và sửa? — **Quyết định nền tảng**

| Mức | Thành phần |
|---|---|
| Basic | master + prompt chính + selected clips |
| Reproducible | thêm mọi input ref, raw candidate, model/mode/settings, logs và project edit |
| Audit-ready | thêm source/rights, approval, rejected options, QC và change history đầy đủ |

**Khuyến nghị:** `Reproducible` cho mọi tập và `Audit-ready` cho artifact có claim, brand hoặc bên thứ ba.

### Q5 — Quan hệ giữa chất lượng và giới hạn 100 credit? — **Cần bạn chốt nguyên tắc**

Các lựa chọn:

- hard cap theo tập; hết cap thì dừng và review;
- owner có thể duyệt vượt cap nếu lỗi là critical;
- không đặt cap cứng, nhưng mọi generation vẫn cần justification và log.

**Khuyến nghị:** cap kế hoạch + exception do bạn duyệt. Chất lượng không bị hy sinh âm thầm, nhưng cũng không dùng “quality-first” để generate không giới hạn.

## 8. Điều đã xác định

- Chất lượng đầu ra bàn giao và quyền kiểm soát của owner cao hơn tốc độ/tự động hóa.
- Workflow cần đầy đủ stage, tuần tự và có gate; execution có thể thủ công.
- Mini-system sẽ kế thừa governance/eval/version/provenance từ dự án lớn, không kéo theo hạ tầng production chưa cần thiết.

## 9. Quyết định đã chốt

- D8: quality-first, human-controlled, sequential.
- Không chọn agent/skill/tool trước khi process, contract và quality gate được chốt.

## 10. Giả định đang sử dụng

- Bạn là owner/final approver.
- Source of truth trước mắt là file trong project folder.
- Flow thủ công và hậu kỳ ngoài Veo được phép.

## 11. Vấn đề còn mở

- Delivery consumer, factual-risk class, approval roles, retention/reproducibility và credit exception policy.
- Định vị/format cụ thể của series vẫn cần khám phá sau khi governance nền tảng đủ rõ.

## 12. Bước tiếp theo

Chốt Q1–Q5. Sau đó tạo process architecture phiên bản 1 gồm stage contract, artifact template, quality rubric, gate checklist và change-control matrix; chỉ khi đó mới ánh xạ agent/skill/tool.

