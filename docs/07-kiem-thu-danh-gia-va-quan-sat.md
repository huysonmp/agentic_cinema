# 07 — Kiểm thử, đánh giá và quan sát

## Kim tự tháp chất lượng

1. **Unit test:** parser, schema, business rule, policy, idempotency.
2. **Contract test:** model structured output, tool/MCP adapter, provider error mapping.
3. **Workflow test:** state transition, approval, resume, partial failure.
4. **Agent eval:** response quality, grounding, trajectory/tool selection.
5. **Security/adversarial:** injection, exfiltration, permission bypass, oversized media.
6. **Load/cost:** concurrency, quota, latency, token/media spend.
7. **Human evaluation:** producer/filmmaker rubric trên use case thật được phép.

## Eval dataset

Mỗi case có:

```text
case_id
input_assets + rights metadata
initial_state
expected_structured_output / allowed variants
expected_citations
expected_tool_trajectory / forbidden tools
rubric and severity
cost/latency envelope
```

Tách:

- `dev`: dùng để phát triển prompt;
- `regression`: ổn định, chạy mỗi PR;
- `holdout`: không dùng chỉnh prompt;
- `adversarial`: injection/safety/security;
- `production-sampled`: đã redaction và có chính sách/consent.

## Nhóm metric

### Structured extraction

- schema validity;
- precision/recall/F1 theo entity/field;
- scene boundary accuracy;
- normalized value vs original text preservation;
- unsupported field rate.

### Grounding và citation

- citation completeness;
- citation correctness/entailment;
- grounded claim rate;
- abstention đúng khi thiếu bằng chứng;
- cross-version/source leakage rate.

### Agent trajectory

- đúng tool và thứ tự hợp lệ;
- forbidden/unnecessary tool calls;
- số bước, retry và loop;
- approval compliance;
- idempotent behavior khi resume.

### Product/operations

- completion/success rate;
- p50/p95 end-to-end và tool latency;
- token/input media volume, cost per run/project;
- human acceptance/edit distance/time saved;
- safety block và false-positive review rate.

Tham khảo [ADK evaluation](https://adk.dev/evaluate/) và [Vertex AI Gen AI evaluation](https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview).

## Release gates

Không phát hành chỉ vì demo trông tốt. Một thay đổi model/prompt/tool cần:

- regression không giảm metric quan trọng quá ngưỡng;
- 100% schema validity hoặc fail-closed;
- 0 approval bypass/forbidden side effect;
- citation correctness đạt ngưỡng đã chốt;
- p95/cost nằm trong envelope;
- human reviewer ký nếu thay đổi policy/media behavior.

Canary model upgrade theo tỷ lệ nhỏ, so sánh với baseline và có rollback alias/config.

## Observability model

Mỗi run liên kết bằng `trace_id`, `run_id`, `project_id` (pseudonymous nếu cần), `agent_name`, `workflow_version`.

### Logs

Structured fields:

```json
{
  "event": "tool_call_completed",
  "run_id": "run_...",
  "tool": "search_script",
  "risk": "R1",
  "duration_ms": 183,
  "status": "success",
  "retry_count": 0,
  "input_bytes": 312,
  "output_bytes": 1840,
  "content_logged": false
}
```

### Traces

Span cho API request, workflow step, model call, retrieval, tool/MCP call, approval wait và export. Không đặt prompt, script hoặc credential vào span attribute.

### Metrics và alerts

- request/run success và latency;
- model/tool error theo code/provider;
- invalid structured output;
- approval wait/denied;
- token/cost/quota usage;
- queue depth/age;
- cross-tenant deny, policy block và anomalous egress.

Tham khảo [Cloud Logging](https://cloud.google.com/logging/docs), [Cloud Trace](https://cloud.google.com/trace/docs/overview) và [Cloud Monitoring](https://cloud.google.com/monitoring/docs).

## Dashboard tối thiểu

- Product funnel: upload → parsed → approved → exported.
- Quality: extraction/citation/acceptance trend theo version.
- Reliability: error, p95, queue, retry, provider health.
- Cost: project/run/model/modality, budget burn rate.
- Safety: blocked requests, approval events, suspicious tool attempts.

## Incident playbook

1. Xác định scope theo run/model/tool/version, không tải nội dung nhạy cảm về máy cá nhân.
2. Bật kill switch cho tool/provider hoặc route về bản ổn định.
3. Thu hồi credential/token nếu có khả năng lộ.
4. Giữ evidence/audit theo chính sách; tránh log thêm dữ liệu.
5. Thông báo owner phù hợp; đánh giá nghĩa vụ người dùng/pháp lý.
6. Sửa, thêm regression/adversarial test và hoàn thành postmortem.

## Kiểm thử thủ công trước demo/staging

- [ ] Script bình thường và script scan.
- [ ] Người dùng sửa breakdown rồi resume.
- [ ] Source đổi version giữa run.
- [ ] Tool timeout và provider 429.
- [ ] Approval từ chối/hết hạn/replay.
- [ ] Prompt injection trong dialogue/metadata/MCP result.
- [ ] Budget/quota hết giữa workflow.
- [ ] Xóa project và xác minh dữ liệu phụ trợ.
