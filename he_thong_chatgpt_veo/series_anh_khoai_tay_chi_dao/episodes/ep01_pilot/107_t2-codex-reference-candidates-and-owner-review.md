# T2 — Cặp ảnh Codex để kiểm, chưa chốt input video

2026-10-01. CANDIDATES_CREATED / INDEPENDENT_STATIC_REVIEW_COMPLETE / REWORK / GENERATION_REQUEST_NOT_READY. Authority106: ảnh tích hợp Codex, video vẫn Veo. Root đã tự tạo, không giao owner chuẩn bị.

## Hai candidates hiện hành

![OPEN v0.3](C:/Users/PC/Downloads/du_an_nem_bui/T2-CODEX-OPEN_v0.3.png)

![END v0.3](C:/Users/PC/Downloads/du_an_nem_bui/T2-CODEX-END_v0.3.png)

OPEN3 thấy đủ danh mục bộ phục vụ nhưng reviewer phát hiện một số đầu lá bị sát/cắt biên trái; sửa lại nhận định ban đầu của root về “trọn”. END3 tạo từ OPEN3, không owner-selected hoặc continuity pass. Cả hai941×1672 thực, không exact9:16. Chưa crop/resize để tránh sửa ảnh ngoài authority và mất vùng phục vụ. Target9:16 phải kiểm trước export/upload video.

## Manifest actual outputs

Tool built-in imagegen, không CLI/API key; actual model name/cost không được tool trả trong evidence đang có, ghi UNKNOWN. Không Flow video/generation hoặc credit mới trong vòng106. Tên exec sau là tên file do tool trả, không suy provider jobID.

File project dưới `media/raw/ep01_t2_references/`, owner dưới `C:/Users/PC/Downloads/du_an_nem_bui/`. Root đo941×1672 cho cả6PNG và so hash hai nơi: cả6True. Media gitignored theo convention, commit tài liệu/manifest, không nói ảnh được pushGit.

| Asset | SHA256 | Tool filename dưới C:/Users/PC/.codex/generated_images/01a0eb0e-6ec3-7121-a6a5-ea0ccdb77744/ | Disposition root |
|---|---|---|---|
| T2-CODEX-OPEN_v0.1.png | ABEC1E9D9174CD3083B70E9543396E9A3AB3D8BF935EC6BBD9EC4F2EE82D2F9F |exec-788cde2c-7701-48b2-a55d-3e47c17d9f32.png | Rework: wide/bench, crop leaf, mark missing |
| T2-CODEX-OPEN_v0.2.png |4CB014BE7F06EF18E490AC85DC4F65308814983AA5593EFA3F6A63C218F1C808 |exec-2918a506-0366-4575-8d83-78c4025f3ffb.png | Rework: cropped leaf/glass; mark redrawn by AI, not native provenance |
| T2-CODEX-OPEN_v0.3.png |AB492C8CC00C0834B37B732BA2B8EC0598F5AE0B95C4D8ADB2A58D7311CEDBF3 |exec-da9aff19-ad84-4817-97eb-2a4707c2caee.png | Candidate for static review; mark missing |
| T2-CODEX-END_v0.1.png |8079A8B53D1CB4BED97EA09715031FAB8ECF58E7D26E18DBB62D6599AC7DA0F3 |exec-28c26ce1-f7d4-40b8-adda-fe3c0820b146.png | Rework: too much tilt/new sky |
| T2-CODEX-END_v0.2.png |C804381D9EAA6BAAD0E61C4F1DD80BDAE61A6A82A0A1636F4B8A962FB325776C |exec-70f55cfc-284b-4598-a534-cf3f44230094.png | Rework: almost duplicate of OPEN |
| T2-CODEX-END_v0.3.png |7CA642984DC7A5A732DC796C30617E7360099CD46F1E431980290AA81220D91B |exec-b2178f7e-b1e9-467a-a0f7-20371038ef41.png | Candidate for static review; continuity/attention not certified |

## Dependencies / boundaries

TABLE08+PAIR03→OPEN1; OPEN1+TABLE08→OPEN2; OPEN2→OPEN3. OPEN3→END1; OPEN3+END1 anti-example→END2; OPEN3→END3. Revisions saved separately, originals untouched. Both source refs viewed before first call; intermediate images tool displayed and root directly inspected before subsequent edits. Six calls/six outputs, not all approved.

No original watermark restored in OPEN3/END3. AI-drawn symbol in OPEN2 is NOT genuine Google native watermark or proof of source; do not use it to close provenance. Existing source bytes/hash/history are preserved, but that does not satisfy the visible-mark invariant101 by itself. Need owner decision on cross-tool derivative disclosure/provenance handling, not silently waive/remove or imitate a native mark. AI content label still required at handoff/publication, distinct from watermark.

Attention food→eyes remains a design hypothesis, not established by stills. New refs may change food/face/background shape; compare TABLE08/PAIR03 before selection. No motion/audio/voice/timing/whole-episode PASS. Camera102 not submitted; V02/CR-01 scopes unchanged.

## Review / next gate

Existing CINE-LIGHT đã thực kiểm bốn ảnh và lưu [report R1](../../agents/directing_team/t2_reference_probe_r1/02_codex-reference-static-review-r1.md); root đọc FULL report và đối soát ngày2026-10-01. Đây không phải blind audience test. Reviewer không chứng nhận CONT/FOOD/RIGHTS ngoài phạm vi quan sát.

Verdict actual: **REWORK / KEEP_FOR_OWNER_CREATIVE_REVIEW / NOT_REQUEST_READY**. Ba MAJOR: rendition nem khác mound sợi nhỏ TABLE08; nét miệng/mắt Khoai đổi giữa OPEN/END trái yêu cầu neutral state; mất dấu nguồn và cách xử lý provenance chưa chốt. Ba MINOR: đầu lá sát/cắt biên; attention food→eyes chưa rõ hơn, thêm nền sáng phía trên; ratio không exact9:16. Hai mặt, main plate và danh mục serving items rõ là kết quả static có giới hạn, không whole-meal/continuity/motion PASS.

Đề xuất sửa có giới hạn: phục hồi rendition nem theo TABLE08, giữ một trạng thái nét mặt, thêm margin lá, điều chỉnh hierarchy theo direction100; sau đó review cặp mới. Không đổi baseline để hợp thức hóa lỗi. Các vai ART/CONT/RIGHTS được nêu là tuyến xử lý, chưa thực chạy trong vòng này.

**Một quyết định owner cần trả lời:** có duyệt xử lý derivative liên công cụ bằng cách giữ nguyên file nguồn, hash/lineage và attribution rõ ảnh tạo bằng AI, không vẽ lại dấu Google để gọi là native watermark? Watermark native trên đầu ra Veo phải giữ nguyên. Đây là đề nghị exception riêng cho yêu cầu visible source mark101 trên ảnh derivative Codex, CHƯA_APPROVED; không thay duyệt hình/món/cặp hoặc quyền chạy video. Nếu không duyệt, phải chọn route bảo toàn dấu nguồn đúng nghĩa thay vì giả chứng thực.

Đã xác định:6PNG và report kiểm thực, cặp3/3 chưa đạt. Chốt: công cụ ảnh Codex theo106, direction100 không đổi. Giả định: cặp khung có thể dẫn camera nhẹ; actual không chứng minh. Còn mở: sửa food/face/margin/hierarchy, owner provenance decision, chuyên môn continuity/format và request video riêng. Tiếp theo: chốt provenance→bounded rework→review mới; không chạy Veo từ cặp bị REWORK. [Exact prompts sáu lượt](108_t2-codex-reference-exact-prompts.md) đã lưu nguyên văn.
