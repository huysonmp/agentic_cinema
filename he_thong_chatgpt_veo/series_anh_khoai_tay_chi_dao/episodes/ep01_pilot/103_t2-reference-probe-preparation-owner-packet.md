# EP01 T2 — Gói chuẩn bị khung và thử chuyển điểm nhìn

2026-10-01. SHOT_DIRECTION_APPROVED / PREPARATION_COMPLETE / PAPER_READY_FOR_OWNER / MEDIA_NOT_CREATED.

[Approval100](100_t2-shot-approval-and-reference-preparation.md) đã ghi đúng quyết định owner. Không cần chọn lại T2 hoặc duyệt lại J23. P6 vẫn mở cho refs/voice; P7 cách quay đã duyệt, chưa actual motion pass.

## Đầu ra để chuẩn bị

- [Brief101](101_t2-reference-frame-briefs-v0.1.md): hai khung dự kiến OPEN/END, hash nguồn đã kiểm, composition và prompt. END được dẫn từ OPEN đã chọn, không hai ảnh tạo độc lập. END dùng làm bố cục S02, không thay frame diễn xuất.
- [Request102](102_t2-camera-attention-probe-request-draft-v0.1.md): một thử camera món→mắt Khoai, không thoại hoặc động tác món; Lite/9:16/x1/4s là cấu hình đề xuất chưa kiểm account. Không retry/Extend tự động.
- [Run log11](../../agents/directing_team/11_t2-reference-probe-preparation-run-log.md): root chuẩn bị; đăng ký một reviewer CINE-LIGHT độc lập. Không nói CHAR/ART/PROMPT đã chạy riêng.

Hai ảnh baseline được root xem trực tiếp; SHA256 và kích thước actual768×1376 đã kiểm. Chưa có ảnh OPEN/END mới hoặc clip thử. Không gọi hai baseline hiện có là inputs hoàn chỉnh cho request102.

## Review độc lập đã thực chạy

[CINE-LIGHT R1](../../agents/directing_team/t2_reference_probe_r1/01_independent-preparation-review-r1.md) được context riêng, đọc101/102 trước approval và không đọc các report reviewer cũ. Có đọc99 chứa summary cũ nên không gọi đây blind review; không dùng summary đó làm closure. Reviewer trực tiếp xem hai baseline, tự kiểm hash/dimensions; root đọc toàn bộ report sau khi lưu.

Kết luận: PAPER_READY_FOR_OWNER, chưa có confirmed paper defect cần rework. Concern PREP-01: baseline hút mắt vào hai mặt trước món; đây cách đọc của reviewer AI, không audience evidence. Khi chuẩn bị OPEN phải kiểm liệu món thực sự mở đường chú ý, không chỉ viết “food-led” trong prompt. Giữ framing/ánh sáng đã duyệt; nếu cần đổi đáng kể phải trình revision.

PREP-02–04 vẫn UNKNOWN/MAJOR: đủ món/Đào/watermark suốt tilt; processing/provenance/rights; account route/giá/request approval. Không đóng chúng bằng bản giấy. PREP-05 nhắc motion/identity/audio cần reports trên output thực; không có CONT/PERF/AV media runs mới. Root đồng ý giới hạn scope này, không tuyên bố generation-ready.

## Ranh giới thử với kịch bản thật

Tay nghỉ/cốc ở bàn là control của camera diagnostic, không sửa S01 có Đào định kéo đĩa hoặc xóa hành động cả tập. Sau thử camera vẫn cần action-specific frames/acting/voice và mạch A. Chín câu, rau/chấm cùng bữa, warm baseline và geography giữ. CR-01 quay liền qua trao nem chưa duyệt. V02 và request voice95 giữ HOLD; thử camera không lấy ngân sách của giọng.

## Quyết định tiếp theo — đúng dependency

Owner có thể chuẩn bị hai khung theo101 rồi đưa file/ID để kiểm. Nếu muốn Codex tạo thay, cần giao quyền execution cho ảnh cụ thể; gói này chưa có quyền đó. Sau actual image review/selection mới kiểm UI start/end/Lite/duration/giá và trình exact camera request trước submit. Không yêu cầu owner đoán tính năng hoặc giá chưa biết.

Đã xác định: baseline thực và controls. Đã chốt: cách quay T2 theo100. Giả định: small tilt giữ toàn bữa ăn khả thi. Còn mở: ảnh actual, khả dụng/giá trên account, âm/motion/readability. Bước tiếp: reviewer giấy→owner chuẩn bị/chọn ảnh→account preflight→request approval riêng→một thử→review thực. Không tiêu credit trong vòng này.
