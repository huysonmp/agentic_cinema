# REC218 — Đối soát mã chốt chặn local

Ngày 2026-10-06. Đây là kiểm phần mềm và phạm vi quyền, **không phải QC đạt cho EP01**. Không tạo media, dùng credit, cài công cụ, commit/push hoặc phát hành.

## Đã triển khai

`scripts/ep01_recovery_gate.py` phân biệt PLANNING, FINISHING và DELIVERY. PLANNING luôn là `UNVERIFIED_PLANNING_NOT_RELEASE`; không trả media PASS. Hai mode sau yêu cầu:

- Bốn contribution DIR/DOP/ACT/EDIT thực tồn tại, có checksum, actor riêng và snapshot đầu vào hiện hành.
- Năm scope review: diễn ý/diễn xuất; hình ảnh–ánh sáng; continuity–món; người nói–giọng–khẩu hình; dựng–AV. Reviewer không trùng maker; báo cáo giấy, ảnh mẫu, ASR hoặc HOLD không thay kiểm media.
- Scope người nói phải đi qua `ep01_speaker_gate.evaluate`, gắn request/review có checksum với đúng target/package/current AV và cùng reviewer: các nguồn, mẫu giọng và hồ sơ duyệt mẫu, đủ bảy lượt, nghe/so mẫu, within-turn/overlap, người nói thấy mặt và người nghe không nói ké. AUDIO_SELECTION không thay AV_ASSEMBLY/FINAL_AV; DELIVERY cần FINAL_AV. Gate recovery không nhận `PASS_APPROVED_OFFSCREEN` toàn lượt để tránh kế thừa phương án cũ203. Điều này không cấm hình người nghe/insert có nhiệm vụ trong một lượt vẫn có speaking-face; đổi coverage vẫn phải duyệt đúng phạm vi.
- Đúng target, script, storyboard, timeline, audio và toàn bộ source trong EDL. Đổi bytes nguồn hoặc range/timeline làm bằng chứng cũ không còn hợp lệ. Hook finishing còn gắn picture, dữ liệu timing phụ đề và approval lịch sử; delivery gắn export, manifest, SRT và clean export.
- Không còn CRITICAL/MAJOR mở. Hồ sơ đóng lỗi cần kiểm media độc lập đúng scope/capability/checks trên đúng target/snapshot, nhật ký quan sát và checksum, không chỉ câu maker “đã sửa”. Chỉ MINOR có thể nhận ngoại lệ owner có hồ sơ riêng.
- Approval toàn tập cho **đúng hành động và đúng file**. Duyệt phản ứng ngắn, giọng nguồn, storyboard hoặc tầng 4 không thay duyệt finishing/export.

`release_authorized=false` xuyên suốt: kiểm này không cấp quyền đăng TikTok.

## Các đường đã hook và giới hạn

| Đường local | Chốt chặn |
|---|---|
| `build_ep01_frame_bound_review.py` | Render thử chỉ PLANNING, đầu ra NOT_FINAL; giữ trạng thái chưa kiểm |
| `finish_ep01_approved_cut.py` | Thiếu FINISHING gate dừng trước đo mix/tạo thư mục/copy/render; decoded picture của AV được duyệt phải đúng picture định render |
| `verify_ep01_finished_export.py` | Bắt buộc chọn technical diagnostic hoặc DELIVERY gate; diagnostic không là nghiệm thu |
| CLI `ep01_recovery_gate.py` | Đối soát bằng chứng; tự đọc/hash sources khai trong timeline, không tin checksum viết trong EDL |

Hai helper finishing/verifying hiện vẫn gắn nguồn 209/210 và lịch caption cũ. Chúng được khóa để không lặp đường bàn giao thiếu QC; **chưa phải finisher tổng quát cho recovery EDL mới**. Khi có EDL mới được chọn, phải cập nhật adapter/mốc caption, test và đối soát dependencies trước chạy. Không dùng adapter cũ với tên file mới để giả đã sẵn sàng.

Các planner/probe lịch sử khác không được đổi thành master hoặc kế thừa media PASS. Hook trên không khóa nút Flow, Canva hay mọi thao tác ngoài repo. File từ ngoài phải intake, hash và review như target mới. Gate không xác minh được bằng mã rằng người khai capability thực sự đã nghe/xem; root phải đọc báo cáo và giữ checkpoint người thật khi AI thiếu capability. Hash của một báo cáo giấy cũng không biến nó thành kiểm media.

## Kiểm thử đã chạy thực

Các lệnh chạy với `.venv/Scripts/python.exe` trong repo:

1. `-m unittest discover -s scripts -p 'test_ep01*.py'`: **91 tests, OK**. Trong đó gate recovery có 42 fixture tests; còn lại là 39 test SIA hiện hữu và 10 test frame-bound/N02.
2. `-m unittest discover -s scripts -p 'test_finish*.py'`: **5 tests, OK**.
3. `git diff --check`: exit 0, không báo lỗi whitespace. Đây là read-only check, không commit/push.

Tổng hiện hành **96/96 tests**. Các vòng trước lần lượt đạt90,93 và94 tests trước bổ sung bridge/closure/offscreen/picture-binding; không xóa lịch sử kiểm. Fixture hư cấu có nhãn SYNTHETIC, nằm trong TemporaryDirectory của test; không đưa approval/report PASS fixture vào hồ sơ phim thật. Trong fixture recovery, evaluator SIA được mock để cô lập bridge; evaluator thật được kiểm riêng bằng39 tests và không mock trong runtime.

SIA độc lập đã chỉ ra schema ban đầu chưa đủ binding reference/từng lượt và closure capability, rồi phát hiện route offscreen cũ có thể lọt. Root bổ sung bridge, closure scope/cap/checks và reject offscreen toàn lượt, thêm regression tests. Đây là sửa mã theo phản biện cụ thể, không phải SIA xác nhận đã nghe phim hoặc mọi finding media đã đóng. Xem lịch snapshot/đối soát tại `08_sia-review.md`.

Lệnh negative thực với dữ liệu local hiện có:

```powershell
.venv/Scripts/python.exe scripts/finish_ep01_approved_cut.py --out C:/Users/PC/Downloads/du_an_nem_bui/218_BLOCKED_FINISHING_DO_NOT_CREATE
```

Kết quả: `FINISHING blocked: mandatory recovery gate evidence missing`. `Test-Path` thư mục trên trả **False**. Không có render/đo mix/copy hoặc media đầu ra từ lệnh này. Không tạo bằng chứng PASS giả để vượt chốt chặn.

## Cách vận hành tiếp

Root tập hợp báo cáo thực, xác định target recovery và snapshot khi có EDL/bản dựng mới. Reviewer thực kiểm đúng target, ghi JSON có scope/capability/checks/findings và nhật ký quan sát. Owner duyệt đúng mốc đã chốt; sau đó mới có thể lập manifest FINISHING hoặc DELIVERY tương ứng. Có report thiếu, UNKNOWN hoặc lỗi trọng yếu chưa đóng thì giữ HOLD/REWORK, không điền MET để vừa schema.

Mã + tests bảo vệ cấu trúc hồ sơ, không chấm độ hấp dẫn hoặc tự đồng bộ miệng. Trạng thái hiện tại của phim vẫn chưa đủ điều kiện finishing.
