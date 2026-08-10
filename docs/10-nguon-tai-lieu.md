# 10 — Nguồn tài liệu

**Ngày đối chiếu:** 2026-08-10. Ưu tiên tài liệu chính thức của Google/ADK và repository `GoogleCloudPlatform/generative-ai`. Các notebook gốc bên dưới đã được đối chiếu với cây `main` tại ngày ghi trên; tài liệu cloud/model/pricing có thể thay đổi nên phải kiểm tra lại trước khi triển khai.

## Cách dùng danh mục

- **Docs sản phẩm** là nguồn chính cho API, model, region, lifecycle, quota và security.
- **Notebook** là mẫu học tập; không copy credential, dependency không pin hoặc quyền IAM rộng vào production.
- **Devpost/form** là nguồn bối cảnh hackathon, có thể hết hạn; không dùng làm tài liệu vận hành.
- Khi link/tên cũ mâu thuẫn với docs hiện hành, docs chính thức và release notes hiện hành được ưu tiên.

## A. Nguồn gốc do người dùng cung cấp

### Giai đoạn 1 — Nền tảng và môi trường

| Chủ đề | Link gốc | Ghi chú cho dự án riêng |
|---|---|---|
| Vertex AI / managed setup | [Vertex AI documentation](https://cloud.google.com/vertex-ai/docs) | Trang tổng; với agent dùng mục Agent Engine bên dưới |
| Low-code agent | [Dialogflow CX agent concepts](https://cloud.google.com/dialogflow/cx/docs/concept/agent) | Chỉ chọn nếu use case phù hợp Dialogflow; không phải core hiện tại |
| Python SDK | [googleapis/python-genai](https://github.com/googleapis/python-genai) | SDK model/media client; không thay ADK orchestration |
| Agent Engine starter | [intro_agent_engine.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/intro_agent_engine.ipynb) | Notebook còn tồn tại trên `main` khi đối chiếu |
| Free program | [Google Cloud Free Program](https://cloud.google.com/free) | Đọc điều kiện và billing hiện hành |
| Hackathon credit | [Biểu mẫu credit](https://forms.gle/XPe837tzogh8L5sX6) | Không cần cho dự án riêng; form có thể đóng |

### Giai đoạn 2 — Document, RAG và media

| Chủ đề | Link gốc | Ghi chú |
|---|---|---|
| Document/PDF processing | [document_processing.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/document_processing.ipynb) | Dùng để học parse; thêm rights, schema, validation |
| RAG BigQuery/PDF | [rag_qna_with_bq_and_featurestore.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/retrieval-augmented-generation/rag_qna_with_bq_and_featurestore.ipynb) | Benchmark với lựa chọn managed hiện hành |
| Grounding/data store | [Grounding overview](https://cloud.google.com/vertex-ai/docs/generative-ai/grounding/overview) | Tên sản phẩm/đường dẫn có thể redirect; xem Vertex AI Search/RAG hiện hành |
| Multimodal introduction | [intro_multimodal_use_cases.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/intro_multimodal_use_cases.ipynb) | Text/image/video/audio patterns |
| Video transcription | [multimodal_video_transcription.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/multimodal_video_transcription.ipynb) | Thêm timecode/speaker QA và privacy |
| Video captioning | [captioning.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/multimodal-data-curation/captioning.ipynb) | Metadata search/index use case |
| Image/VFX concepts | [intro_gemini_3_image_gen.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_image_gen.ipynb) | Preview/storyboard; model lifecycle phải kiểm tra lại |
| Music/SFX | [lyria3_music_generation.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/music/getting-started/lyria3_music_generation.ipynb) | Kiểm tra access, region, pricing và rights |
| Gemini TTS | [gemini_3_1_flash_tts.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/getting-started/gemini_3_1_flash_tts.ipynb) | Không mô phỏng voice người thật thiếu consent |
| Multi-speaker podcast | [multi-speaker-podcast.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/use-cases/podcast/multi-speaker-podcast.ipynb) | Có thể dùng table read/rehearsal synthetic |
| Multimodal sentiment | [intro_to_multimodal_sentiment_analysis.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/multimodal-sentiment-analysis/intro_to_multimodal_sentiment_analysis.ipynb) | Không coi sentiment inference là ground truth về con người |

### Giai đoạn 3 — Đối tác hackathon

- [IBM resources](https://agentic-cinema.devpost.com/details/ibm-resources)
- [Grafana resources](https://agentic-cinema.devpost.com/details/grafana-resources)
- [Parallel resources](https://agentic-cinema.devpost.com/details/parallel-resources)
- [ClickHouse resources](https://agentic-cinema.devpost.com/details/clickhouse-resources)
- [Replit resources](https://agentic-cinema.devpost.com/details/replit-resources)
- [Full hackathon resources](https://agentic-cinema.devpost.com/resources)

### Giai đoạn 4 — ADK, Agent Engine, tools và MCP

| Chủ đề | Link gốc | Ghi chú |
|---|---|---|
| Agent Engine intro | [intro_agent_engine.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/intro_agent_engine.ipynb) | Local → managed runtime example |
| Deploy ADK | [tutorial_deploy_your_first_adk_agent_on_agent_engine.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_deploy_your_first_adk_agent_on_agent_engine.ipynb) | Đối chiếu deploy docs hiện hành |
| Live API on Agent Engine | [tutorial_get_started_with_live_api_on_agent_engine.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_live_api_on_agent_engine.ipynb) | Milestone tùy chọn cho rehearsal |
| External API/tool pattern | [tutorial_google_maps_agent.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/tutorial_google_maps_agent.ipynb) | Học adapter/auth/tool patterns; Maps không bắt buộc |
| Database MCP Toolbox | [tutorial_mcp_toolbox_for_databases.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/tutorial_mcp_toolbox_for_databases.ipynb) | Read-only/template query mặc định |
| Function calling | [intro_function_calling.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb) | Schema + tool result envelope |
| Forced function calling | [forced_function_calling.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/forced_function_calling.ipynb) | Không thay thế authorization/approval ở application layer |
| Multimodal function calling | [multimodal_function_calling.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/multimodal_function_calling.ipynb) | Visual signal vẫn là untrusted input |

### Giai đoạn 5 — Triển khai và an toàn

| Chủ đề | Link gốc | Ghi chú |
|---|---|---|
| Dialogflow version/environment | [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version) | Chỉ áp dụng nếu chọn Dialogflow CX |
| Serverless hosting | [Cloud Run quickstarts](https://cloud.google.com/run/docs/quickstarts) | Tốt cho API/tool worker |
| Secret | [Secret Manager](https://cloud.google.com/secret-manager/docs) | Dùng service identity, rotation và audit |
| Safety notebook section | [Gemini image safety settings](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_image_gen.ipynb#Safety-Settings) | Bổ sung application policy và human review |

### Bối cảnh/luật cuộc thi

- [Agentic Cinema overview](https://agentic-cinema.devpost.com/)
- [Official rules](https://agentic-cinema.devpost.com/rules)
- [Resources](https://agentic-cinema.devpost.com/resources)

## B. Nguồn chính thức bổ sung và hiện hành

### ADK và agent runtime

- [ADK documentation](https://adk.dev/)
- [ADK Python quickstart](https://adk.dev/get-started/python/)
- [ADK agent teams](https://adk.dev/tutorials/agent-team/)
- [ADK graph workflows](https://adk.dev/graphs/)
- [ADK template workflows](https://adk.dev/agents/workflow-agents/)
- [ADK custom tools](https://adk.dev/tools/)
- [ADK MCP tools](https://adk.dev/tools/mcp-tools/)
- [ADK sessions](https://adk.dev/sessions/)
- [ADK evaluation](https://adk.dev/evaluate/)
- [ADK deployment](https://adk.dev/deploy/)
- [Vertex AI Agent Engine overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- [Agent Engine setup](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/set-up)
- [Agent Engine deployment](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy)
- [Google Cloud Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)

> Lưu ý cập nhật: tài liệu ADK cũ tại `google.github.io/adk-docs` hiện chuyển hướng tới `adk.dev`. ADK 2.0 giới thiệu graph/dynamic workflow linh hoạt hơn; template sequential/parallel/loop vẫn hữu ích nhưng không còn là lựa chọn mặc định cho mọi luồng mới.

### Gemini SDK, model và tool use

- [Google Gen AI Python SDK docs](https://googleapis.github.io/python-genai/)
- [Google Gen AI SDK GitHub](https://github.com/googleapis/python-genai)
- [Vertex AI Gemini model catalog](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models)
- [Vertex AI generative AI release notes](https://cloud.google.com/vertex-ai/generative-ai/docs/release-notes)
- [Function calling](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)
- [Controlled/structured generation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output)
- [Context caching](https://cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview)
- [Gemini Live API](https://cloud.google.com/vertex-ai/generative-ai/docs/live-api)

### Document, retrieval và data

- [Document understanding](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/document-understanding)
- [Video understanding](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding)
- [Audio understanding](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding)
- [Document AI](https://cloud.google.com/document-ai/docs)
- [Vertex AI RAG Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview)
- [Vertex AI Search introduction](https://cloud.google.com/generative-ai-app-builder/docs/introduction)
- [BigQuery vector search](https://cloud.google.com/bigquery/docs/vector-search-intro)
- [MCP Toolbox for Databases documentation](https://mcp-toolbox.dev/)
- [MCP Toolbox for Databases source](https://github.com/googleapis/mcp-toolbox)

### GenMedia

- [Generate images with Imagen](https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images)
- [Veo video generation overview](https://cloud.google.com/vertex-ai/generative-ai/docs/video/overview)
- [Veo prompt guide](https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)
- [Vertex AI Media Studio](https://console.cloud.google.com/vertex-ai/studio/media)
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs)

Model/media availability, allowlist, safety, region và pricing thay đổi nhanh; luôn bắt đầu từ model catalog/release notes thay vì dựa vào model ID trong notebook.

### Security, reliability, evaluation và cost

- [Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc)
- [IAM overview](https://cloud.google.com/iam/docs/overview)
- [Secret Manager](https://cloud.google.com/secret-manager/docs)
- [VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/overview)
- [Cloud Audit Logs](https://cloud.google.com/logging/docs/audit)
- [Secure AI Framework](https://saif.google/)
- [Gemini safety filters](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters)
- [Vertex AI Gen AI evaluation](https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview)
- [Cloud Logging](https://cloud.google.com/logging/docs)
- [Cloud Trace](https://cloud.google.com/trace/docs/overview)
- [Cloud Monitoring](https://cloud.google.com/monitoring/docs)
- [Vertex AI generative AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)
- [Vertex AI quotas](https://cloud.google.com/vertex-ai/generative-ai/docs/quotas)
- [Cloud Billing budgets](https://cloud.google.com/billing/docs/how-to/budgets)

### Protocols

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Agent2Agent Protocol](https://a2a-protocol.org/latest/)

## C. Quy trình duy trì liên kết

Mỗi tháng hoặc trước release:

1. Kiểm tra redirect/404 và thay link cũ bằng canonical link.
2. Đọc model lifecycle/release notes, region, quota và pricing.
3. Đối chiếu dependency đang pin với ADK/Agent Engine compatibility.
4. Re-run regression/security eval trước khi đổi model/SDK.
5. Cập nhật ngày đối chiếu ở đầu tệp và ghi ADR nếu thay đổi kiến trúc.
