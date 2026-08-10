# 02 — Thiết lập Google Cloud và ADK

## 1. Điều kiện cần

- Python 3.10+ theo ADK Python quickstart; dự án nên chuẩn hóa một phiên bản và khóa trong CI.
- Git và GitHub CLI.
- Google Cloud CLI (`gcloud`).
- Một Google Cloud project có billing; kiểm tra [Free Program](https://cloud.google.com/free) và [giá Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/pricing) trước khi chạy media generation.
- Quyền tổ chức phù hợp để bật API, tạo service account, bucket và runtime.

## 2. Tách môi trường

Tối thiểu dùng ba project hoặc ba ranh giới tương đương:

| Môi trường | Dữ liệu | Mục đích |
|---|---|---|
| dev | chỉ synthetic/public/licensed fixtures | phát triển nhanh |
| staging | dữ liệu kiểm thử được kiểm soát | integration/eval/load/security |
| prod | dữ liệu thực đã phân loại | người dùng thật |

Không dùng project cá nhân chung cho production. Thiết lập budget, quota và log retention riêng ngay từ đầu.

## 3. Cấu hình CLI

```powershell
gcloud auth login
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
gcloud config set ai/region YOUR_SUPPORTED_LOCATION
```

Kiểm tra project và identity trước mỗi lệnh tạo tài nguyên:

```powershell
gcloud config list
gcloud auth list
```

## 4. Bật API tối thiểu

Danh sách thực tế tùy kiến trúc; bắt đầu với:

```powershell
gcloud services enable `
  aiplatform.googleapis.com `
  run.googleapis.com `
  artifactregistry.googleapis.com `
  cloudbuild.googleapis.com `
  secretmanager.googleapis.com `
  storage.googleapis.com `
  logging.googleapis.com `
  cloudtrace.googleapis.com
```

Không bật hàng loạt API không dùng. Ghi danh sách thành Infrastructure as Code ở milestone triển khai.

## 5. Môi trường Python

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install --upgrade google-adk google-genai "google-cloud-aiplatform[agent_engines,adk]"
```

Giải thích:

- `google-adk`: xây và chạy agent cục bộ.
- `google-genai`: client thống nhất cho Gemini/GenMedia API.
- `google-cloud-aiplatform[agent_engines,adk]`: tích hợp deployment/runtime quản lý trên Vertex AI Agent Engine.

Không sao chép vô thời hạn mốc phiên bản `>=1.101.0` trong tài liệu hackathon. Sau khi proof-of-concept chạy ổn, tạo lockfile và pin phiên bản đã test; dùng bot/PR để nâng cấp có eval.

## 6. Chọn backend Gemini

Development có thể dùng Gemini Developer API, nhưng dự án này chọn **Vertex AI** cho đường production vì IAM, project boundary, audit và tích hợp Google Cloud.

`.env` cục bộ dựa trên `.env.example`:

```dotenv
GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
GOOGLE_CLOUD_LOCATION=YOUR_SUPPORTED_LOCATION
GOOGLE_GENAI_USE_VERTEXAI=true
```

Model ID không được mặc định trong tài liệu kiến trúc. Chọn model qua [model catalog](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models), kiểm tra lifecycle, region, quota, modality và giá tại thời điểm triển khai.

## 7. Tạo agent thử nghiệm

Theo [ADK Python quickstart](https://adk.dev/get-started/python/):

```powershell
adk create agents\hello_agent
adk run agents\hello_agent
```

Hoặc giao diện dev:

```powershell
adk web --port 8000
```

`adk web` chỉ dùng phát triển/debug, không đặt trực tiếp làm UI production.

## 8. IAM và secret

- Dùng service account riêng cho runtime, deployer và CI.
- Cấp quyền ở resource nhỏ nhất; không dùng Owner/Editor cho service account chạy app.
- Dùng Workload Identity Federation/OIDC cho CI thay cho service-account key dài hạn.
- Secret nằm trong Secret Manager; agent chỉ nhận giá trị cần dùng tại runtime.
- Không đưa API key, signed URL, access token hoặc nội dung script vào `.env.example`, log hay prompt.

## 9. Checklist xác nhận local

- [ ] `gcloud auth application-default print-access-token` hoạt động nhưng token không bị ghi log.
- [ ] Một lời gọi Gemini qua Vertex AI thành công trong đúng project/location.
- [ ] `adk run` chạy agent mẫu.
- [ ] Tool giả lập trả structured result và timeout đúng.
- [ ] `.env` bị Git ignore.
- [ ] Budget alert và quota protection đã bật trước khi thử Imagen/Veo/Lyria/TTS.

## 10. Nguồn chính thức

- [ADK Python quickstart](https://adk.dev/get-started/python/)
- [Google Gen AI Python SDK](https://googleapis.github.io/python-genai/)
- [Vertex AI Agent Engine overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- [Set up Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/set-up)
- [Deploy an agent](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy)
- [Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc)
