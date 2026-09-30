# Khám phá vòng 1 — mini-system ChatGPT/Codex → Veo

- **Ngày:** 2026-09-29
- **Trạng thái:** completed — các quyết định vòng 1 đã được khóa trong `01-chot-vong-1-va-kham-pha-noi-dung.md`
- **Mục đích vòng này:** chốt use case pilot, ranh giới Codex–Veo và các điểm con người phê duyệt trước khi thiết kế agent/skill.

## 1. Bài toán lõi đang được hiểu

Xây một hệ thống vận hành tối giản giúp một người hoặc nhóm sáng tạo đi từ ý tưởng/brief đến video tạo bởi Veo. Codex/ChatGPT đảm nhiệm phần công việc nhận thức và tài liệu; con người duyệt các quyết định quan trọng; Veo đảm nhiệm generation.

Đây chưa phải một ứng dụng production hay một hệ thống tự động chạy không giám sát. Giá trị cần kiểm chứng trước là: **quy trình có tạo ra một video đúng ý hơn, ít vòng sửa hơn và vẫn cho người dùng kiểm soát được quyết định/chi phí hay không**.

### Đối tượng liên quan tạm xác định

| Vai trò | Trách nhiệm dự kiến |
|---|---|
| Chủ ý tưởng/đạo diễn | Chốt mục tiêu, thông điệp, thẩm mỹ và chọn phương án |
| Operator Codex/ChatGPT | Cung cấp input, duyệt tài liệu và giữ project context |
| Codex/ChatGPT | Khám phá brief, tạo concept/shot/prompt package, kiểm tra tính nhất quán |
| Operator Veo | Kiểm tra request, tạo video, ghi nhận kết quả và chi phí |
| Người duyệt quyền nội dung | Xác nhận quyền dùng hình ảnh, nhân vật, nhãn hiệu, giọng và tài liệu nguồn |

Một người có thể giữ nhiều vai trò trong pilot.

### Outcome mong muốn tạm thời

Một pilot hoàn tất khi ta có:

1. một creative brief đã duyệt;
2. một shot/generation package đã duyệt;
3. các video candidate từ Veo và nhật ký prompt/thiết lập;
4. quyết định chọn hoặc loại từng candidate kèm lý do;
5. một retrospective đủ rõ để quyết định skill/tool nào đáng xây tiếp.

## 2. Hiện trạng liên quan trong repository

Dự án mẹ đã có thiết kế production-first cho ingest kịch bản, breakdown, shot planning, approval, media generation, provenance và audit. Tuy nhiên chưa có vertical slice triển khai. Mini-project này nên tái sử dụng các nguyên tắc có ích (approval, version, rights, provenance), nhưng không kéo theo ngay Google ADK, database, RAG, cloud deployment hay nhiều agent.

## 3. Sáu câu hỏi/quyết định ưu tiên vòng 1

### Q1 — Video pilot đầu tiên giải quyết việc gì? — **Cần bạn trả lời**

Các phương án khởi đầu:

| Phương án | Hệ quả |
|---|---|
| A. Quảng cáo/social cho một sản phẩm thật | Outcome và tiêu chí đánh giá rõ; cần asset/quyền thương hiệu chính xác |
| B. Cảnh phim ngắn hư cấu | Hợp với định hướng `agentic_cinema`; khó đánh giá hiệu quả ngoài chất lượng sáng tạo |
| C. Video kể chuyện/giải thích | Dễ kiểm soát cấu trúc và thông điệp; có thể cần voice, chữ hoặc hậu kỳ |
| D. Music/fashion/visual mood piece | Dễ thử thẩm mỹ; tiêu chí “đúng” thường chủ quan hơn |

**Khuyến nghị sơ bộ:** chọn một sản phẩm đầu ra thật mà bạn sẵn sàng sử dụng hoặc chia sẻ nội bộ. Không dùng demo vô thưởng vô phạt vì nó không bộc lộ pain vận hành.

### Q2 — Đơn vị outcome đầu tiên lớn đến đâu? — **Cần bạn trả lời**

| Phương án | Hệ quả |
|---|---|
| A. Một clip/shot ngắn | Học nhanh về prompt và reference; chưa kiểm chứng continuity hay quy trình nhiều cảnh |
| B. Một sequence ngắn gồm vài clip | Kiểm chứng được storyboard, continuity, selection và assembly; effort vẫn có thể giới hạn |
| C. Một video hoàn chỉnh dài | Gần nhu cầu thật nhưng đưa quá nhiều biến số vào vòng đầu |

**Khuyến nghị sơ bộ:** B — một sequence 20–30 giây từ khoảng 3–4 clip candidate/shot. Con số này là giả định làm việc, cần điều chỉnh theo use case ở Q1.

### Q3 — Điểm xuất phát của hệ thống là gì? — **Cần bạn trả lời**

| Phương án | Hệ quả |
|---|---|
| A. Ý tưởng vài dòng | Codex phải hỗ trợ discovery và creative development nhiều nhất |
| B. Creative brief có sẵn | Dễ chuẩn hóa đầu ra và đo chất lượng chuyển đổi brief → video |
| C. Kịch bản/treatment có sẵn | Cần breakdown, chọn đoạn và quản lý continuity |
| D. Asset tham chiếu có sẵn | Cần manifest quyền sử dụng và chiến lược frames/ingredients |

**Khuyến nghị sơ bộ:** cho phép phối hợp A + D trong pilot nếu asset có quyền sử dụng rõ; không mở mọi loại input ngay từ đầu.

### Q4 — Giai đoạn đầu dùng Veo theo cách nào? — **Quyết định nền tảng cần chốt**

| Phương án | Hệ quả |
|---|---|
| A. Con người thao tác Google Flow | Nhanh nhất, quan sát được hành vi thật, không cần code/API key; thao tác và log cần ghi tay |
| B. Codex chạy script gọi Gemini API | Lặp lại và lưu provenance tốt hơn; phát sinh key, credit/cost, async polling, tải/lưu file và xử lý lỗi |
| C. Vertex AI/API production | Kiểm soát cloud/IAM tốt hơn; quá nặng cho discovery nếu chưa chứng minh workflow |

**Khuyến nghị sơ bộ:** A cho pilot đầu; chuẩn hóa `generation_request` và `generation_result` ngay từ đầu để sau này chuyển sang B mà không đổi logic nghiệp vụ.

### Q5 — Con người bắt buộc duyệt ở đâu? — **Quyết định nền tảng cần chốt**

Đề xuất bốn gate tối thiểu:

1. `G1 — Brief lock`: mục tiêu, audience, thông điệp, format và ràng buộc.
2. `G2 — Creative/shot lock`: concept, shot sequence, reference và điều cấm.
3. `G3 — Generation approval`: prompt + input asset + model/mode + số candidate/credit dự kiến.
4. `G4 — Selection/export`: chọn clip, cho phép chỉnh/extend/export hoặc loại bỏ.

**Khuyến nghị sơ bộ:** dùng đủ bốn gate trong pilot đầu; sau retrospective mới gộp những gate không tạo giá trị.

### Q6 — Điều kiện truy cập và dữ liệu thật hiện có là gì? — **Cần bạn trả lời/kiểm tra thực tế**

Cần biết:

- bạn đang có gói Google AI/Flow nào và Veo model/mode nào thực sự hiển thị tại tài khoản/khu vực;
- có sẵn API key/GCP project hay chỉ dùng giao diện Flow;
- asset nào sẽ dùng cho pilot và quyền sử dụng/likeness/voice của chúng;
- ai là người duyệt và ai trực tiếp thao tác Veo;
- giới hạn credit/ngân sách tối đa cho pilot.

Không đưa credential hoặc secret vào repository hay hội thoại.

## 4. Pain và ràng buộc cần quan sát trong pilot

Chưa nên coi đây là sự thật; cần ghi nhận bằng nhật ký thực tế:

- brief mơ hồ làm prompt thay đổi liên tục;
- prompt tốt cho từng clip nhưng sequence thiếu continuity;
- reference asset không đủ sạch hoặc dùng sai vai trò;
- không nhớ prompt/model/settings nào tạo ra candidate nào;
- tốn credit do generate trước khi chốt creative direction;
- lựa chọn candidate dựa trên cảm tính nhưng không lưu lý do;
- việc chuyển dữ liệu thủ công Codex → Flow có thể là nút thắt hoặc lại là approval gate hữu ích.

## 5. Giả định làm việc và rủi ro

### Có thể tạm giả định để tiếp tục

- Một operator chính dùng Codex và Flow trên máy cá nhân.
- Tài liệu là Markdown/JSON trong folder dự án; media lớn không commit vào Git.
- Vòng đầu manual-first; chưa cần web app, database, MCP, RAG hay multi-agent runtime.
- Một orchestrator conversational trong Codex là đủ; skill chỉ được thêm khi workflow lặp lại đã rõ.

### Bắt buộc kiểm chứng trước khi kết luận

- Model, feature, độ dài, resolution, aspect ratio, reference/frames và credit thực tế trong tài khoản Veo/Flow của bạn.
- Mức độ giữ nhất quán nhân vật/sản phẩm qua nhiều generation.
- Chất lượng audio/voice và việc có nên tách audio khỏi video workflow.
- Khả năng tái lập kết quả khi dùng cùng generation package.
- Chính sách/quyền đối với asset thật, likeness, voice, nhãn hiệu và đầu ra.
- Việc thao tác Flow có thể/được phép tự động hóa hay nên giữ hoàn toàn thủ công.

## 6. Research và thử nghiệm cụ thể sau khi trả lời Q1–Q6

| Task | Bằng chứng cần thu | Quyết định được hỗ trợ |
|---|---|---|
| R1. Account capability check | ảnh/chú thích các model, mode, duration, resolution, credit thấy trong Flow; không chụp thông tin nhạy cảm | chọn Flow hay API và khóa phạm vi pilot |
| R2. Chọn một brief thật | brief, audience, CTA/thông điệp, format, tiêu chí đạt | xác định outcome và rubric |
| R3. Reference test nhỏ | cùng một shot chạy text-only, first-frame và ingredients/reference nếu có | chọn input strategy |
| R4. Prompt repeatability test | 2–3 candidate cùng package, log setting và lỗi | thiết kế prompt schema và QA checklist |
| R5. Human-gate observation | thời gian, số lần sửa, lý do reject tại G1–G4 | giữ/gộp/thay gate |
| R6. Rights/data check | manifest nguồn và quyền cho mọi asset dùng trong pilot | cho phép generation/export |

## 7. Các vấn đề mở rộng — chưa giải quyết ở vòng này

- Tự động gọi Veo API, polling và download.
- Agent chuyên môn riêng cho script, visual continuity, prompt hoặc QA.
- MCP/plugin, database, RAG, UI review, cloud deployment.
- Tự động dựng timeline, nhạc, voice-over, subtitle và publish.
- Multi-user, phân quyền, audit production và cost dashboard.

Chỉ mở các nhánh này sau khi pilot cho thấy pain thật và điểm nào đáng tự động hóa.

## 8. Tổng hợp cuối vòng 1

### Đã xác định

- Có một mini-project riêng trong repository.
- Codex/ChatGPT tạo tài liệu/gói generation; Veo tạo video; con người kiểm soát điểm quan trọng.
- Dự án mẹ là nguồn nguyên tắc tham khảo, không phải blueprint bắt buộc.

### Quyết định đã chốt

- Pilot là video TikTok dạng kể chuyện/giải thích và hướng đến xây dựng một series.
- Mỗi outcome thử nghiệm là một sequence gồm nhiều clip, không chỉ một shot đơn lẻ.
- Điểm xuất phát là ý tưởng được người dùng và Codex cùng phát triển, đánh giá và chốt.
- Giai đoạn đầu người dùng thao tác Google Flow thủ công; sau khi workflow ổn định mới đánh giá tích hợp Gemini API.
- Giữ bốn human gate G1–G4.
- Người dùng là operator Veo và người phê duyệt chính.
- Điều kiện tài khoản do người dùng cung cấp: Google AI Pro, khoảng 100 credit và có quyền truy cập các mode Veo cần dùng; cần kiểm tra trực tiếp trong Flow trước generation.

### Giả định đang dùng

- Manual-first qua Google Flow cho pilot đầu.
- Một conversational orchestrator trước; chưa tách nhiều agent/skill.
- Tài liệu Markdown/JSON là source of truth ban đầu.
- Tạm dùng format dọc `9:16` cho TikTok; thông số xuất bản cuối cùng cần kiểm tra trước production.

### Vấn đề còn mở

- Chủ đề, audience, giá trị cốt lõi và lời hứa của series.
- Độ dài, cấu trúc tập, phong cách hình ảnh và chiến lược audio/voice.
- Asset/quyền sử dụng và giới hạn credit cụ thể cho một tập hoặc một vòng thử.
- Tiêu chí đánh giá chất lượng nội dung và hiệu quả TikTok.
- Gate nào thực sự cần giữ hoặc có thể gộp sau pilot.

### Bước tiếp theo đề xuất

Hoàn tất discovery vòng 2 trong `01-chot-vong-1-va-kham-pha-noi-dung.md`, sau đó chọn một tập pilot và thiết kế **một** vertical slice tối thiểu; chưa cần dựng toàn bộ hệ thống.


## 9. Nguồn chính thức đã kiểm tra

- OpenAI — Skills: <https://developers.openai.com/api/docs/guides/tools-skills>
- OpenAI — Guardrails and human review: <https://developers.openai.com/api/docs/guides/agents/guardrails-approvals>
- OpenAI — Rethinking skills and prompts: <https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra>
- Google — Create videos in Flow: <https://support.google.com/flow/answer/16353334>
- Google — Flow models and supported features: <https://support.google.com/flow/answer/16352836>
- Google AI for Developers — Generate videos with Veo: <https://ai.google.dev/gemini-api/docs/veo>
