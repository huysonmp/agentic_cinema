# 09 — Lộ trình thực thi

Lộ trình được chia theo **kết quả kiểm chứng**, không theo số tuần cứng. Mỗi mốc chỉ mở rộng khi mốc trước có demo, test và tài liệu vận hành.

## M0 — Foundation (đã khởi tạo)

### Kết quả

- problem statement/MVP/out-of-scope;
- kiến trúc, dữ liệu, security, eval và deployment guide;
- repository, license, contribution rules và nguồn tài liệu.

### Done khi

- [x] Tài liệu liên kết được, không chứa secret/dữ liệu có bản quyền.
- [x] GitHub repository có lịch sử ban đầu.
- [ ] Owner xác nhận vertical slice và lựa chọn database/UI ở ADR tiếp theo.

## M1 — Local vertical slice

### Xây dựng

- scaffold Python/ADK và package domain;
- ingest TXT/PDF text-native cục bộ;
- scene/breakdown schema + validator;
- orchestrator `Uploaded → Parsed → BreakdownProposed`;
- review/approval qua CLI hoặc UI tối thiểu;
- JSON/CSV export;
- synthetic fixtures + unit/workflow eval.

### Done khi

- [ ] Một script mẫu chạy end-to-end, resume được.
- [ ] Mỗi breakdown field quan trọng có citation.
- [ ] Invalid output fail-closed; không ghi đè source.
- [ ] Chi phí/token/latency được đo.

## M2 — Grounded knowledge và continuity

### Xây dựng

- corpus/index theo project/version/ACL;
- retrieval tool có citation contract;
- continuity agent và diff giữa screenplay versions;
- injection/adversarial eval;
- review UI mở đúng page/source span.

### Done khi

- [ ] Citation correctness/coverage đạt release gate.
- [ ] Không cross-project retrieval trong test.
- [ ] Agent abstain đúng khi thiếu evidence.

## M3 — Shot planning và media preview

### Xây dựng

- shot-plan schema, constraint/assumption UI;
- prompt/brief generation;
- optional Imagen/Veo/Lyria/TTS adapter theo nhu cầu;
- R2 approval, cost estimate/budget và queued generation;
- provenance manifest và nhãn AI-generated.

### Done khi

- [ ] Không media job nào chạy thiếu approval hợp lệ.
- [ ] Partial failure/retry/idempotency test pass.
- [ ] Rights/consent gate và safety flow được kiểm thử.

## M4 — Staging productionization

### Xây dựng

- API/UI, auth, tenant/project ACL;
- private storage, database, Agent Engine/Cloud Run;
- IaC + CI/CD + federation;
- logs/traces/metrics/alerts và dashboard;
- backup/restore/delete + incident runbook;
- load, cost, security và human eval.

### Done khi

- [ ] Release/security gates pass.
- [ ] Canary/rollback/kill switch được thử.
- [ ] SLO/budget/on-call owner được chốt.

## M5 — Partner integration (tùy chọn)

Chỉ chọn sau khi có nhu cầu rõ:

- observability/analytics;
- research/enrichment;
- database/tooling;
- governance hoặc collaborative hosting.

### Done khi

- [ ] ADR so sánh build/buy và data terms.
- [ ] Adapter/MCP threat model + contract tests.
- [ ] Có feature flag, fallback và cách ngắt provider.

## Backlog ưu tiên

### Must

- schema/provenance/citation;
- approval và tool policy;
- evaluation fixtures;
- cost/observability;
- rights/consent metadata.

### Should

- screenplay version diff;
- OCR;
- bilingual Vietnamese/English normalization;
- export PDF/Fountain/FCPXML tùy use case;
- UI diff và bulk edit.

### Could

- Live voice rehearsal;
- database MCP;
- A2A agents qua service boundary;
- schedule/budget integrations;
- storyboard/video/audio preview.

### Won't yet

- autonomous publishing;
- real-person voice/face cloning;
- training on private scripts;
- unbounded web browsing/tool execution.

## Issue template cho mỗi feature

```markdown
Problem/user:
Acceptance criteria:
Input/output schema:
Data classification and rights:
Tools and risk level:
Human approval:
Eval cases/metrics:
Cost/latency budget:
Observability:
Failure/rollback:
Docs/ADR:
```
