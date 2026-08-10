# 06 — An toàn, bảo mật và bản quyền

> Đây là checklist kỹ thuật, không phải tư vấn pháp lý. Với kịch bản, likeness, voice, hợp đồng hoặc dữ liệu cá nhân thực, cần người phụ trách pháp lý/quyền nội dung duyệt chính sách.

## Tài sản cần bảo vệ

- kịch bản chưa phát hành, treatment, storyboard và media;
- PII, thông tin cast/crew, lịch trình và location;
- quyền/consent, hợp đồng và metadata provenance;
- prompt, system policy, source code, model/tool credentials;
- approval, audit log và output tạo sinh.

## Mối đe dọa chính

- lộ dữ liệu giữa project/tenant;
- prompt injection từ PDF, subtitle, webpage hoặc MCP output;
- tool confused-deputy thực hiện hành động vượt quyền;
- SSRF, file bomb, malware, path traversal qua ingest;
- supply-chain compromise của package/container/MCP server;
- tạo deepfake/impersonation hoặc nội dung vi phạm quyền;
- log/trace vô tình chứa script, PII, token hoặc signed URL;
- chi phí tăng đột biến do loop/retry/media generation;
- output sai được coi là fact và đi vào kế hoạch sản xuất.

## Kiểm soát theo lớp

### Identity và access

- IAM least privilege, service account theo workload/môi trường.
- Tách deployer và runtime; production deployment cần review.
- ACL kiểm tra ở API, query/filter và object storage; không chỉ trong UI/prompt.
- CI dùng federation, không dùng JSON key dài hạn.

### Data protection

- Encryption mặc định; cân nhắc CMEK theo phân loại/khách hàng.
- Bucket public access prevention, uniform access, versioning/lifecycle phù hợp.
- Signed URL ngắn hạn, bound với object/action.
- Data minimization khi gửi model/tool; redaction PII nếu không cần.
- Retention/deletion workflow có thể kiểm thử.

### Agent/tool safety

- System policy tách khỏi untrusted content.
- Structured output + validator + business invariant.
- Tool allowlist, risk level, approval capability và idempotency.
- Max steps, max tool calls, token/cost/time budget cho mỗi run.
- Không cho model đọc Secret Manager hoặc credential trực tiếp.

### Network và supply chain

- Hạn chế egress; deny private/link-local metadata targets.
- Pin dependency, scan image/SBOM, dependency review và signed artifact nếu có.
- MCP/server ngoài qua gateway/adapter được quan sát.
- Staging test trước khi nâng model/SDK/server version.

Tham khảo [Google Cloud IAM](https://cloud.google.com/iam/docs/overview), [Secret Manager](https://cloud.google.com/secret-manager/docs), [VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/overview), [Cloud Audit Logs](https://cloud.google.com/logging/docs/audit) và [Secure AI Framework](https://saif.google/).

## Copyright, likeness và voice

Mỗi `SourceAsset` phải có tối thiểu:

- owner/uploader và source URI;
- declared rights basis: owned, licensed, public-domain, consented, unknown;
- allowed purposes/modalities/territories/expiry nếu có;
- likeness/voice consent cho người có thể nhận diện;
- restrictions và reviewer;
- hash + timestamp.

Nếu `rights_basis=unknown`, chỉ quarantine/metadata review; không index, train, generate derivative hoặc chia sẻ ra provider ngoài theo mặc định.

Không dùng tên người thật để yêu cầu mô phỏng khuôn mặt/giọng nếu không có consent phù hợp. TTS nhiều người nói dùng voice được dịch vụ cho phép và gắn nhãn synthetic.

## Provenance đầu ra

Mỗi generated artifact lưu:

- parent asset/version/shot IDs;
- prompt template version và user edits;
- model/provider/version/config;
- generation timestamp/request ID;
- safety decision và human approvals;
- content hash, watermark/provenance metadata nếu được hỗ trợ;
- license/usage note riêng, không kế thừa tự động từ code license.

Tham khảo [SynthID](https://deepmind.google/science/synthid/) như một lớp nhận diện; watermark không thay thế hồ sơ quyền và consent.

## Content safety

- Áp [Gemini safety/content filters](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters) theo use case.
- Thêm policy cấp ứng dụng cho sexual content, minors, graphic violence, hate, harassment, illegal activity và impersonation.
- Phân biệt nội dung mô tả trong kịch bản với yêu cầu tạo media; generation có gate riêng.
- Ghi reason code, không log toàn bộ nội dung nhạy cảm nếu không cần.
- Có quy trình appeal/manual review và không tự động “repair” nội dung bị chặn theo cách lách policy.

## Privacy và logging

- Mặc định log ID/hash/latency/status/token count, không log prompt/output nguyên văn.
- Content logging chỉ bật có chủ đích ở dev với fixtures an toàn hoặc môi trường kiểm soát.
- Trước khi dùng provider/partner, đọc data use, retention, residency và training terms hiện hành.
- Người dùng thấy rõ dữ liệu được gửi đến dịch vụ nào trước hành động R2/R3.

## Security release gate

- [ ] Threat model được cập nhật cho vertical slice.
- [ ] Không có public bucket/database/unauthenticated production endpoint ngoài thiết kế.
- [ ] Secret scanning và dependency scanning pass.
- [ ] Cross-tenant tests pass ở API, DB, RAG và object storage.
- [ ] Injection/SSRF/file bomb/tool abuse tests pass.
- [ ] Approval bypass test pass; R3 không thể chạy bằng prompt.
- [ ] Data deletion drill và restore drill đã được thực hiện.
- [ ] Incident owner, contact và kill switch được xác định.
