# Google media API — Khám phá khả năng tự động hóa có cấp quyền

Ngày kiểm: 2026-09-30. Status: RESEARCH_COMPLETE_FOR_ROUTE_SELECTION / ACCOUNT_ACCESS_UNVERIFIED / IMPLEMENTATION_AND_PAID_RUN_NOT_AUTHORIZED.

## 1. Yêu cầu mới và giới hạn

Owner yêu cầu kiểm khả năng đấu nối API Veo/Flow và tạo ảnh qua cấp quyền, muốn tự động hóa sau duyệt và lệnh chạy thử. Đây là thay đổi định hướng so với baseline Flow thao tác thủ công, không phải quyền gọi API/tạo media/chi phí ngay hoặc blanket approval mọi lần thử. Lượt này chỉ đọc code/docs, không kiểm credential, đăng nhập tài khoản, enable billing/API, upload ảnh hoặc generate.

## 2. Kết quả đã xác minh

| Đường tích hợp | Evidence | Kết luận và giới hạn |
|---|---|---|
| Veo qua Gemini API | [Veo API docs](https://ai.google.dev/gemini-api/docs/veo) có SDK generate_videos, operation polling và download; có ví dụ video dọc | API chính thức có thật. Chưa chứng minh account owner truy cập được model/quota; API feature không đồng nhất mặc định với Flow |
| Ảnh qua Gemini API | [Image generation](https://ai.google.dev/gemini-api/docs/image-generation) có tạo/sửa ảnh, text/reference input, model-specific formats | Có thể dùng làm adapter tạo character/reference/style frames sau approval request. Chưa gọi; fidelity/consistency vẫn cần QC, không được coi ảnh output đã approved |
| Google Cloud route | [Cloud video generation docs](https://cloud.google.com/vertex-ai/generative-ai/docs/video/generate-videos-from-text) (hiện redirect sang Gemini Enterprise Agent Platform) có authentication/project/API flow | Có route Cloud chính thức; phải kiểm project/IAM/region và billing. Không cần chọn route này nếu Gemini API đáp ứng pilot |
| API của ứng dụng Google Flow | Đã đọc Flow Help, docs tạo clip/models/credits; search Google domains và developer blog cho public API | Chưa tìm thấy tài liệu developer API công khai chính thức cho Flow app. Không khẳng định tuyệt đối không tồn tại; không coi endpoint web nội bộ/reverse engineering là API được hỗ trợ |
| Flow UI automation | Chưa đăng nhập, chưa thử browser, chưa kiểm điều kiện tài khoản/terms | Khả năng khảo sát riêng, không API route đã ready. Có thể lỗi do UI/session/model changes; không lấy cookie/token từ browser hoặc bypass CAPTCHA |

Veo không phải Flow: Veo là model có API; Flow là app/workspace với features/credit/UI. API-generated media không tự xuất hiện trong project Flow và không mặc định đồng bộ toàn bộ editing state; import/quyền phải kiểm riêng.

## 3. Billing và cấp quyền cần phân biệt

Theo [Google AI plans](https://ai.google.dev/gemini-api/docs/google-ai-plans), lợi ích Pro/Ultra trong AI Studio UI khác direct API; direct API quản lý/billing riêng, Google One AI credits không là cùng hệ Cloud credit. Có khả năng subscription đủ điều kiện nhận Cloud credit qua Developer Program, phải kiểm account; không hứa dùng 3000 credit Flow để trả API. [Flow credits](https://support.google.com/flow/answer/16526234?hl=en) mô tả credit dùng trong app và cost theo generation. Số 3000 là thông tin owner cung cấp, chưa account read-back.

[Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing) có Veo paid-tier per-second và image model pricing; không chốt model/budget ở bước nghiên cứu. [Billing](https://ai.google.dev/gemini-api/docs/billing) có project spend caps/prepay nhưng nêu billing latency và long-running overage. Vì vậy budget UI/Cloud alone không thay application-side cap/request reservation; cũng không hứa hard dollar cap tuyệt đối trước evidence.

Với Gemini route: owner tạo/chọn project và billing theo nhu cầu, tạo restricted API key theo [API key docs](https://ai.google.dev/gemini-api/docs/api-key), cung cấp cho tiến trình cục bộ qua environment/secret storage; không gửi key trong chat, không viết vào repo hoặc log. GOOGLE_API_KEY có thể ưu tiên hơn GEMINI_API_KEY trong SDK; phải chỉ định nguồn credential để tránh dùng nhầm project. Không cấp toàn quyền Google account hay cần quyền owner Cloud cho runtime chỉ để generate. Cloud route dùng authentication/IAM phù hợp sau kiểm, ưu tiên tránh service-account key dài hạn nếu workflow hỗ trợ.

Khóa cho phép gọi dịch vụ không thay approval nội dung/chạy/chi phí. Phân biệt (a) quyền credential và project; (b) request approved đúng version; (c) lệnh RUN_TEST đúng request/cap; (d) permission upload refs; (e) output acceptance/release.

## 4. Code hiện có trong repo — evidence read-only

Đã đọc SDK vendor tại `ext/python-genai/google/genai/models.py` phần generate_videos và `operations.py` phần get: có request video, source/config, long-running operation status. SDK local dùng source và đánh dấu prompt/image/video positional inputs cũ deprecated; ví dụ docs một số chỗ còn dùng các field cũ. Cần pin SDK/API version và contract test trước implementation, không chép ví dụ rồi báo đã đấu nối.

Các notebook/external sample tồn tại nhưng không phải adapter production đã chạy của mini project. Không import/run code vendor trong lượt khảo sát. Adapter nếu được duyệt nên là Python modules + CLI + tests bình thường, không phụ thuộc notebook hay web API nội bộ.

## 5. Phương án để owner chọn

| Option | Hệ quả / trade-off | Khuyến nghị sơ bộ |
|---|---|---|
| A — Official Gemini API cho cả ảnh và video | Có request/job/output log rõ, dễ replay có kiểm soát; billing/quota API riêng, có thể phát sinh chi phí ngoài Flow | Phù hợp nhất nếu owner chấp nhận ngân sách API riêng và muốn automation ổn định |
| B — Hybrid: ảnh API, video Flow thủ công trước | Tự động được P6 references, giữ video route/credit hiện có; chưa tự động toàn bộ khâu generate video | Hợp nếu chưa muốn thêm ngân sách Veo API; không coi là đạt yêu cầu auto cả hai |
| C — Khảo sát UI-assisted Flow | Có thể sử dụng app account credit; cần kiểm browser access, điều kiện sử dụng và độ bền UI; chưa ready | Chỉ nghiên cứu nếu owner ưu tiên dùng Flow credit, không thay bằng reverse-engineered endpoints |

Cloud official route là lựa chọn kỹ thuật thêm nếu owner đã có GCP hoặc cần IAM/region controls; không mặc định thêm hạ tầng cho pilot. Các option mới là proposal, không thay policy P0 đã duyệt.

## 6. Control flow đề xuất — chưa implement

`DRAFT manifest → REVIEWED → OWNER_APPROVED → OWNER_RUN_TEST → SUBMITTED → POLLING → OUTPUT_SAVED → QC → OWNER_ACCEPTED hoặc REWORK`

Trước submit, executor kiểm request ID/version/content hash, approved script/ref/rights/model/settings, expiry, count/cap và permission upload. Lệnh có thể là “chạy thử request IMG-001 đã duyệt, tối đa một lần” thay vì cấp quyền không giới hạn. Hash/checksum là đề xuất cơ chế để tránh artifact đổi sau approval, chưa có số hash giả hoặc signature system implemented.

- Maker/Director/Prompt role lập manifest; review team phản biện; executor duy nhất gọi API trong scope. Không cấp credential cho mọi maker để tự chạy.
- Request ảnh P6 khác video P8/P9: ảnh là input mới cần owner duyệt trước khi được dùng làm video reference. Phê duyệt video không suy thành quyền tạo/thay character refs.
- Reserve worst-case estimated count/cost trước submit nếu đủ pricing evidence; record USD/API credits tách khỏi Flow credits, actual cost UNKNOWN nếu response không cung cấp và chưa billing read-back.
- Ghi operation ID ngay sau submit; resume polling existing job không submit lại. Timeout/connection loss sau submit: HOLD và reconcile, không retry generation mù có thể double spend. Application dedup ledger không đồng nghĩa provider idempotency được bảo đảm; concurrency khóa/reservation cần tests.
- Poll có backoff/deadline; save raw outputs/metadata vào owner-managed local media, không Git. Theo Veo docs, server giữ output ngắn hạn (hiện 2 ngày); ưu tiên download sớm, không chỉ lưu URL. Không log key/signed URL nhạy cảm.
- QC đánh giá media thật; fail dừng, đề xuất revision/request mới hoặc giữ retry budget chỉ nếu approval explicitly cho phép. Không auto publish hoặc đổi nội dung để vừa tool.

Đề xuất thử kỹ thuật đầu tiên sau implementation/credentials/approval: dry-run hoàn toàn offline; kiểm quyền từ chối; một image request có cap; owner chọn ref; rồi một video probe có cap riêng. Chưa quyết model/resolution/duration/chi phí và chưa cấp quyền submit; không bỏ quality gates episode chỉ để “test kỹ thuật”.

## 7. Điều cần owner trả lời (3 câu)

1. Chọn A/B/C ở trên? Khuyến nghị A nếu chấp nhận chi phí API riêng; nếu bắt buộc dùng 3000 Flow credit, chọn B hoặc khảo sát C và chấp nhận video API chưa nối.
2. Đã có project/API key/billing Google AI Studio hoặc GCP chưa? Chỉ trả trạng thái, không gửi secret. Chưa có thì chuẩn bị checklist tự cấp quyền, không tự enable billing.
3. Ngân sách tối đa cho đợt thử API đầu tiên là bao nhiêu USD, và duyệt theo từng request hay một batch có count/cap? Khuyến nghị từng request khi pilot chưa có cost/quality baseline. Không tự lấy “chưa lo credit” làm cap vô hạn.

## 8. Kết quả vòng khám phá

Đã xác định: official Veo/image API tồn tại, SDK repo có nền tích hợp; Flow public app API chưa xác nhận. Đã chốt: chỉ nghiên cứu và ghi hồ sơ/commit/push, chưa kết nối account/chi phí hoặc implementation. Giả định: approval trước từng experiment và giữ P0–P14, không auto acceptance. Còn mở: route/account/budget/tool/version/feature restrictions và data handling khi upload refs. Tiếp theo sau owner chọn: lập bounded implementation plan + permission amendment/executor contract, tests offline; trình request cụ thể trước paid run. Không đổi runtime agents/policy approved ngầm.
