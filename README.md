# Agentic Cinema

Agentic Cinema là dự án cá nhân xây dựng một **hệ điều hành tiền kỳ điện ảnh có tác nhân** trên Gemini, Google Cloud và Agent Development Kit (ADK). Hệ thống tiếp nhận kịch bản và tư liệu sản xuất, tạo breakdown có cấu trúc, hỗ trợ lập shot list/storyboard, tìm kiếm tri thức có dẫn nguồn và chỉ thực hiện các hành động nhạy cảm sau khi con người phê duyệt.

> Dự án được gợi cảm hứng từ bộ tài liệu Agentic Cinema Hackathon, nhưng **không phải bài dự thi** và không phụ thuộc vào một partner track. Phần hackathon chỉ được lưu lại để truy xuất nguồn gốc.

## Mục tiêu sản phẩm

Phiên bản đầu tiên giải quyết một luồng hoàn chỉnh:

1. Nạp kịch bản PDF/TXT và tài liệu tham chiếu vào vùng lưu trữ riêng.
2. Trích xuất cảnh, nhân vật, đạo cụ, bối cảnh, thời gian, yêu cầu âm thanh/VFX thành JSON có schema.
3. Cho người dùng duyệt và sửa breakdown trước khi đi tiếp.
4. Sinh shot list, prompt storyboard và gói bàn giao cho các bộ phận.
5. Hỏi đáp trên kịch bản/tài liệu bằng RAG, luôn kèm nguồn và vị trí trích dẫn.
6. Ghi lại tool call, quyết định phê duyệt, chi phí, độ trễ và lỗi để có thể kiểm toán.

## Nguyên tắc thiết kế

- Một **orchestrator** điều phối các agent chuyên môn; workflow xác định được dùng cho nghiệp vụ, LLM chỉ dùng tại điểm cần suy luận.
- Mọi đầu ra nghiệp vụ quan trọng phải có schema, nguồn gốc và phiên bản.
- Hành động ghi/xóa/xuất bản/gửi ra ngoài cần xác nhận của con người.
- Dữ liệu dự án, prompt, log và media được phân quyền theo nguyên tắc tối thiểu.
- Model ID, giá và vùng triển khai là cấu hình, không hard-code; luôn kiểm tra tài liệu trước mỗi bản phát hành.
- MVP ưu tiên phân tích và lập kế hoạch. Không tự động phát hành nội dung, mô phỏng danh tính hay dùng tư liệu không rõ quyền.

## Bản đồ tài liệu

| Tệp | Nội dung |
|---|---|
| [00 — Tổng quan và phạm vi](docs/00-tong-quan-va-pham-vi.md) | Người dùng, vấn đề, MVP, tiêu chí thành công |
| [01 — Kiến trúc](docs/01-kien-truc-he-thong.md) | Thành phần, agent, luồng dữ liệu, cấu trúc mã dự kiến |
| [02 — Thiết lập Google Cloud và ADK](docs/02-thiet-lap-google-cloud-adk.md) | Môi trường, API, xác thực, chạy local |
| [03 — Quy trình điện ảnh](docs/03-quy-trinh-nghiep-vu-dien-anh.md) | Luồng ingest → breakdown → planning → export |
| [04 — Dữ liệu, RAG và đa phương thức](docs/04-du-lieu-rag-da-phuong-thuc.md) | Schema, ingest, retrieval, media |
| [05 — Tools, MCP và tích hợp](docs/05-tools-mcp-va-tich-hop.md) | Hợp đồng công cụ, phê duyệt, partner adapters |
| [06 — An toàn, bảo mật và bản quyền](docs/06-an-toan-bao-mat-va-ban-quyen.md) | Threat controls, quyền riêng tư, IP, AI safety |
| [07 — Kiểm thử, đánh giá và quan sát](docs/07-kiem-thu-danh-gia-va-quan-sat.md) | Evals, metrics, tracing, release gates |
| [08 — Triển khai, vận hành và chi phí](docs/08-trien-khai-van-hanh-va-chi-phi.md) | Dev/staging/prod, CI/CD, SLO, FinOps |
| [09 — Lộ trình thực thi](docs/09-lo-trinh-thuc-thi.md) | Các mốc và Definition of Done |
| [10 — Nguồn tài liệu](docs/10-nguon-tai-lieu.md) | Toàn bộ link gốc và nguồn bổ sung |
| [11 — Bối cảnh hackathon](docs/11-hackathon-tham-khao.md) | Yêu cầu/tiêu chí cuộc thi để tham khảo |
| [12 — Nhật ký quyết định](docs/12-nhat-ky-quyet-dinh.md) | ADR và các quyết định ban đầu |
| [13 — Bản đồ nguồn ngoài](docs/13-ban-do-nguon-ngoai.md) | Tám upstream được ghim và cách dùng theo milestone |
| [14 — Chính sách cập nhật upstream](docs/14-chinh-sach-cap-nhat-upstream.md) | Bootstrap, update, release gate và rollback submodule |

## Bắt đầu nhanh

Hiện repository là **documentation-first**: kiến trúc và quy tắc đã được chốt trước khi sinh code. Khi bắt đầu milestone M1:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install --upgrade google-adk google-genai "google-cloud-aiplatform[agent_engines,adk]"
gcloud auth application-default login
```

Sao chép `.env.example` thành `.env`, điền project/location và **không commit secret**. Xem đầy đủ tại [hướng dẫn thiết lập](docs/02-thiet-lap-google-cloud-adk.md).

Để lấy đầy đủ tám repository nguồn tham khảo đã ghim, kể cả submodule lồng:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./scripts/bootstrap.ps1
```

Checkout mặc định lấy đầy đủ lịch sử và tự bật Windows long paths cho các lệnh Git. CI hoặc máy tạm có thể dùng `-Shallow`; xem [bản đồ nguồn ngoài](docs/13-ban-do-nguon-ngoai.md) và [third-party notices](THIRD_PARTY_NOTICES.md).

## Trạng thái

- [x] Chốt phạm vi, kiến trúc tham chiếu và nguồn tài liệu.
- [x] Ghim source upstream chính thức và bổ sung quy trình bootstrap/kiểm tra.
- [ ] Scaffold ứng dụng ADK và schema miền nghiệp vụ.
- [ ] Xây dựng vertical slice ingest → breakdown → approval → export.
- [ ] Thêm RAG có citation và bộ eval.
- [ ] Triển khai staging trên Google Cloud.

## Giấy phép

Mã nguồn của repository được cấp phép theo [Apache License 2.0](LICENSE). Tư liệu người dùng tải lên, kịch bản, hình ảnh, âm thanh và đầu ra tạo sinh không tự động mang giấy phép Apache; quyền của chúng phải được quản lý riêng trong metadata dự án.
