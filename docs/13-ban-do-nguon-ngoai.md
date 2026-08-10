# 13 — Bản đồ nguồn ngoài

Các repository trong `ext/` là **nguồn tham khảo được ghim commit**, không phải mã runtime được import trực tiếp. Dependency Python vẫn phải được khai báo và khóa phiên bản trong `pyproject.toml`/lockfile khi bắt đầu M1.

| Đường dẫn | Upstream | Vai trò trong dự án | Mốc sử dụng chính |
|---|---|---|---|
| `ext/generative-ai` | Google Cloud generative-ai | Notebook chính thức cho Gemini, Agent Engine, RAG, media và eval | M1–M4 |
| `ext/agent-starter-pack` | Google Cloud Agent Starter Pack | Cấu trúc ứng dụng, deployment và observability tham chiếu | M1, M4 |
| `ext/adk-samples` | Google ADK samples | Mẫu agent, workflow, tool và deployment | M1–M5 |
| `ext/adk-python` | Google ADK Python | Tra cứu API và hành vi implementation của ADK | M1–M4 |
| `ext/python-genai` | Google Gen AI Python SDK | Tra cứu client Gemini, cấu hình model và typed responses | M1–M3 |
| `ext/mcp-toolbox` | MCP Toolbox for Databases | Mẫu MCP/database, auth và tool boundary | M2, M5 |
| `ext/modelcontextprotocol` | Model Context Protocol | Specification, schema và ví dụ interoperability MCP | M2, M5 |
| `ext/a2a` | Agent2Agent Protocol | Giao tiếp agent qua service boundary khi thực sự cần | M5 |

## Quy tắc sử dụng

- Không thêm `ext/` vào `PYTHONPATH` và không import trực tiếp từ submodule trong production.
- Chỉ chuyển thể phần cần thiết sau khi kiểm tra giấy phép, NOTICE và attribution.
- Mọi ví dụ đưa vào mã dự án phải có test, phù hợp threat model và không mang secret/dữ liệu mẫu không rõ quyền.
- Khi tài liệu local khác tài liệu chính thức hiện hành, ưu tiên kiểm tra upstream và ghi lại quyết định trong ADR.
- Gitlink trong repository cha là nguồn sự thật về phiên bản đã duyệt.

## Bản đồ theo milestone

### M1 — Local vertical slice

- `agent-starter-pack`: cấu trúc package, cấu hình môi trường và entrypoint.
- `adk-samples`: orchestrator/workflow agent, function tools và session state.
- `adk-python`: API contract của ADK khi sample và package phát hành khác nhau.
- `python-genai`: structured output, upload/input đa phương thức và model config.
- `generative-ai`: document processing và Agent Engine notebooks.

### M2 — RAG và continuity

- `generative-ai`: retrieval, BigQuery/vector search và citation patterns.
- `mcp-toolbox`: database tool boundary và xác thực.
- `modelcontextprotocol`: protocol contract, capability negotiation và security considerations.

### M3 — Shot planning và media preview

- `generative-ai`: Imagen/Veo/Lyria/TTS và multimodal evaluation.
- `python-genai`: request/response API cho media adapters.

### M4–M5 — Production và tích hợp

- `agent-starter-pack` và `adk-samples`: deployment, tracing, eval và CI/CD.
- `a2a`: chỉ dùng nếu agent nằm ở service/owner boundary khác nhau.
- `mcp-toolbox`/`modelcontextprotocol`: chỉ dùng khi MCP giải quyết ranh giới dữ liệu hoặc công cụ cụ thể.

## Khởi tạo

Mặc định lấy đầy đủ lịch sử:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./scripts/bootstrap.ps1
```

Máy CI dùng một lần có thể chọn snapshot nông:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./scripts/bootstrap.ps1 -Shallow
```
