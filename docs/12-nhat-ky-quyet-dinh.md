# 12 — Nhật ký quyết định kiến trúc (ADR)

## Cách dùng

Mỗi quyết định có trạng thái `proposed`, `accepted`, `superseded` hoặc `rejected`. Khi thay đổi, không xóa lịch sử; thêm ADR mới và liên kết ADR bị thay thế.

## ADR-0001 — Documentation-first

- **Trạng thái:** accepted
- **Ngày:** 2026-08-10
- **Bối cảnh:** Dự án bắt nguồn từ tài liệu hackathon nhưng sẽ phát triển độc lập, chưa có use case/code cụ thể.
- **Quyết định:** Chốt phạm vi, dữ liệu, safety, eval và deployment guide trước khi scaffold code.
- **Hệ quả:** Chậm có demo hơn một chút nhưng giảm rewrite và tạo tiêu chí kiểm chứng rõ.

## ADR-0002 — Google ADK + Vertex AI là đường production chính

- **Trạng thái:** accepted
- **Ngày:** 2026-08-10
- **Bối cảnh:** Cần orchestration, tool integration và managed runtime gắn Gemini/Google Cloud.
- **Quyết định:** Dùng ADK Python cho agent/workflow, Google Gen AI SDK cho model/media calls và Vertex AI/Agent Engine cho đường production. Local development có thể dùng mock hoặc backend được phép.
- **Hệ quả:** Tận dụng IAM/audit/managed runtime; domain schema/tool interfaces phải giữ portable để giảm lock-in.

## ADR-0003 — Graph/dynamic workflow cho orchestration mới

- **Trạng thái:** accepted
- **Ngày:** 2026-08-10
- **Bối cảnh:** ADK 2.0 ưu tiên graph/dynamic workflow; quy trình có approval/resume/branch.
- **Quyết định:** Orchestrator là state machine/graph; sequential/parallel/loop dùng cục bộ khi phù hợp. Không để LLM tự quyết định control flow đã biết.
- **Hệ quả:** Cần thiết kế state/event/idempotency rõ; đổi lại dễ kiểm thử và audit.

## ADR-0004 — Một orchestrator, agent chuyên môn có ranh giới rõ

- **Trạng thái:** accepted
- **Ngày:** 2026-08-10
- **Bối cảnh:** Multi-agent dễ tăng latency, chi phí và failure modes.
- **Quyết định:** Chỉ tách intake, breakdown, continuity, shot planning và media brief theo trách nhiệm/schema/quyền. MVP có thể chạy trong modular monolith.
- **Hệ quả:** Không có “agent cho mọi việc”; mỗi agent có tool allowlist và eval riêng.

## ADR-0005 — Human approval là capability ngoài prompt

- **Trạng thái:** accepted
- **Ngày:** 2026-08-10
- **Bối cảnh:** Prompt instruction không đủ bảo vệ write/delete/publish/spend.
- **Quyết định:** Hành động R2/R3 cần approval object/token single-use, expiry và request hash do application layer kiểm tra.
- **Hệ quả:** Workflow phải pause/resume và side effects phải idempotent.

## ADR-0006 — Apache-2.0 cho code; content rights quản lý riêng

- **Trạng thái:** accepted
- **Ngày:** 2026-08-10
- **Bối cảnh:** Repository có thể mở công khai, nhưng media/kịch bản có quyền riêng.
- **Quyết định:** Code/docs của repository theo Apache-2.0; user content/generated artifacts có rights metadata riêng và không được commit.
- **Hệ quả:** Cần asset manifest, consent/provenance và fixtures có quyền rõ.

## ADR-0007 — Upstream chính thức được ghim bằng Git submodule

- **Trạng thái:** accepted
- **Ngày:** 2026-08-10
- **Bối cảnh:** Dự án cần tra cứu implementation, notebook và protocol gốc; chỉ lưu link dễ bị drift, còn sao chép file làm mất lịch sử và attribution.
- **Quyết định:** Ghim tám repository chính thức trong `ext/` bằng Git submodule, mặc định checkout full history và hỗ trợ `-Shallow` riêng cho CI. Runtime dependency vẫn được khóa bằng package manager; production không import từ `ext/`.
- **Hệ quả tích cực:** Nguồn tái tạo được, commit review rõ, giữ nguyên license/NOTICE và có thể rollback bằng gitlink.
- **Đánh đổi/rủi ro:** Clone tốn thêm dung lượng/thời gian, nested submodule và Windows long paths cần bootstrap riêng, upstream có thể chứa nội dung ngoài phạm vi dự án.
- **Cách kiểm chứng/rollback:** `scripts/verify-submodules.ps1` kiểm tra đủ đường dẫn, SHA, dirty/shallow state; rollback bằng cách hoàn nguyên gitlink hoặc loại bỏ submodule trong một ADR thay thế.

## ADR cần quyết định trước M1

- ADR-0008: Operational database (PostgreSQL/managed alternative).
- ADR-0009: UI stack và auth provider.
- ADR-0010: RAG Engine vs Vertex AI Search vs BigQuery/vector store.
- ADR-0011: Agent Engine vs Cloud Run boundary.
- ADR-0012: IaC/CI runner và region/data residency.

## Mẫu ADR

```markdown
## ADR-NNNN — Tên quyết định

- **Trạng thái:** proposed
- **Ngày:** YYYY-MM-DD
- **Bối cảnh:**
- **Các lựa chọn:**
- **Quyết định:**
- **Hệ quả tích cực:**
- **Đánh đổi/rủi ro:**
- **Cách kiểm chứng/rollback:**
```
