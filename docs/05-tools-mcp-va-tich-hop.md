# 05 — Tools, MCP và tích hợp

## Khi nào dùng function tool, MCP hoặc A2A

| Cơ chế | Dùng khi | Không dùng khi |
|---|---|---|
| Function tool | Logic nội bộ nhỏ, API ổn định, schema do ta quản lý | Muốn chia sẻ tool cho nhiều host/ngôn ngữ |
| MCP | Chuẩn hóa truy cập tool/resource bên ngoài | Chỉ cần một hàm nội bộ đơn giản |
| A2A | Agent độc lập cần giao tiếp qua ranh giới dịch vụ/tổ chức | Các module trong cùng process |

Nguồn: [ADK custom tools](https://adk.dev/tools/), [ADK MCP tools](https://adk.dev/tools/mcp-tools/), [MCP specification](https://modelcontextprotocol.io/) và [A2A protocol](https://a2a-protocol.org/latest/).

## Tool contract bắt buộc

Mỗi tool cần khai báo:

- tên theo động từ + đối tượng (`search_script`, `create_preview_job`);
- mô tả không mơ hồ, JSON input/output schema;
- auth scope và tenant/project scope;
- read/write/destructive/external-spend classification;
- timeout, retryable errors, rate limit;
- idempotency key cho mọi write;
- max payload và loại dữ liệu được phép;
- redaction/logging policy;
- approval policy và compensation/rollback nếu có.

Ví dụ result envelope:

```json
{
  "status": "success",
  "data": {},
  "error": null,
  "provenance": {
    "provider": "internal",
    "request_id": "req_...",
    "observed_at": "2026-08-10T00:00:00Z"
  }
}
```

Tool không trả exception stack/secret cho model. Lỗi được ánh xạ sang mã hữu hạn và thông điệp an toàn.

## Phân loại rủi ro và phê duyệt

| Cấp | Ví dụ | Chính sách |
|---|---|---|
| R0 | đọc metadata nội bộ | tự động trong ACL |
| R1 | search/RAG, phân tích model | tự động với budget/rate limit |
| R2 | tạo preview có phí, ghi draft | approval theo run/request hash |
| R3 | gửi email, publish, chia sẻ data, xóa | approval rõ ràng ngay trước hành động; audit đầy đủ |

Approval không phải câu “hãy cẩn thận” trong prompt. Đó là capability/token do application layer phát hành, có actor, expiry, action hash và single-use.

## MCP hardening

- Chỉ kết nối server/transport trong allowlist.
- Pin package/image digest; kiểm tra provenance và changelog.
- Dùng network egress policy, TLS và auth riêng cho mỗi server.
- Sanitize tool description/output; server MCP cũng là bên không đáng tin tuyệt đối.
- Không truyền toàn bộ conversation hoặc screenplay nếu tool chỉ cần ID/field nhỏ.
- Giới hạn danh sách tool được expose cho từng agent.
- Test schema drift, timeout, oversized output, prompt injection và compromised server.
- Database MCP dùng query/template đã kiểm soát, read-only mặc định; không để model tự nối SQL tùy ý với credential rộng.

## Tích hợp tham chiếu từ hackathon

Không bắt buộc chọn partner cho dự án riêng. Giữ adapter interface và đánh giá theo use case:

| Đối tác | Vai trò có thể phù hợp | Link tài nguyên gốc |
|---|---|---|
| IBM | governance/enterprise AI/data workflow | [IBM resources](https://agentic-cinema.devpost.com/details/ibm-resources) |
| Grafana | dashboard, metrics, traces, incident workflow | [Grafana resources](https://agentic-cinema.devpost.com/details/grafana-resources) |
| Parallel | web research/data enrichment theo chính sách | [Parallel resources](https://agentic-cinema.devpost.com/details/parallel-resources) |
| ClickHouse | event/analytics/observability khối lượng lớn | [ClickHouse resources](https://agentic-cinema.devpost.com/details/clickhouse-resources) |
| Replit | prototyping/hosting cộng tác | [Replit resources](https://agentic-cinema.devpost.com/details/replit-resources) |

Các trang Devpost là nguồn bối cảnh, có thể hết hạn sau cuộc thi. Trước khi tích hợp, phải đọc docs, pricing, data-processing terms và auth của chính nhà cung cấp.

## Adapter interface đề xuất

```python
class ToolAdapter(Protocol):
    name: str
    risk_level: str

    async def validate(self, request: ToolRequest) -> ValidationResult: ...
    async def execute(self, request: ToolRequest, context: ToolContext) -> ToolResult: ...
    async def compensate(self, receipt: ToolReceipt) -> CompensationResult: ...
```

Đây là thiết kế tham chiếu, chưa phải code đã triển khai. ToolContext không chứa credential thô; adapter lấy secret bằng service identity.

## Test bắt buộc cho tool

- happy path và schema validation;
- denied ACL/expired approval;
- timeout/429/5xx và retry;
- duplicate idempotency key;
- partial failure/compensation;
- output chứa prompt injection/secret-like string;
- provider đổi field hoặc trả payload quá lớn;
- budget exhausted và circuit breaker mở.
