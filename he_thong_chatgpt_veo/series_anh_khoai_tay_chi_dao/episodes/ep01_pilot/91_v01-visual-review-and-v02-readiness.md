# EP01 — Kiểm hình V01 và readiness V02

2026-10-01, Asia/Saigon. Owner yêu cầu tiếp tục. Chưa có xác nhận nghe V01 đạt; V02 vẫn chưa submit. Ngân sách riêng còn tối đa 10 credit theo 88, không retry/Quality.

## Đã kiểm trên media thật

Root trích grid 4×4 từ V01 gốc: chọn frame n=0,12,…180 ở 24fps, thứ tự trái→phải, trên→dưới ứng với 0;0,5;…7,5 giây. File `artifacts/voice-qc/v01-visual-r1/frames-2fps.png` đã được xem bằng view_image. Chỉ 16/192 frame, không full playback hoặc kiểm đồng bộ âm vị.

AV-CUT đã xem độc lập cùng grid, đọc request 85, raw metadata/ASR và ghi [report 05](../../agents/audio_edit_quality/reports/05_v01-visual-r1.md). Không nhận kết luận root trước review. Đây là follow-up cùng context đã kiểm concat, không cold context mới.

| Hạng mục | Quan sát | Kết luận và giới hạn |
|---|---|---|
| Bố cục | Khoai trái, Đào phải, cùng ngồi; bố cục bàn/camera không có đổi lớn trong mẫu | Đạt quan sát mẫu, không chứng nhận identity hoặc continuity toàn clip |
| Khẩu hình | Khoai có trạng thái mở/khép miệng; Đào chủ yếu nhìn, cười khép miệng và chớp mắt | Không đủ xác nhận đúng lượt toàn clip, Đào im lặng hoặc lip-sync |
| Gesture | Khoai nâng tay về ngực ở các mẫu khoảng 1–3,5 giây, thêm một mẫu 5 giây | Lệch giới hạn “only subtle natural facial movement and speech”; auditor ghi MAJOR trong scope visual của probe. Không tự suy giọng kém hoặc lỗi choreography production |
| Đạo cụ | Không thấy cầm đũa, ăn/uống hoặc chuyển món trong mẫu; đĩa/lá/bát/cốc giữ bố trí lớn | Không quan sát được mọi frame, không đủ đóng motion gate |
| Chữ phát sinh | Nhãn tên Khoai ở góc dưới trái | Unwanted text so với yêu cầu không thêm caption; khác platform watermark ở dưới phải |
| Người nền | Có người từ khung đầu, vị trí thay đổi giữa mẫu | Không có reference trực tiếp để xác nhận ai “được thêm”, không tự ghi added-person defect |

## Đóng nghi vấn nguồn chữ bằng frame native

Auditor giữ nguồn chữ UNKNOWN vì chưa tự xác minh overlay của montage. Root kiểm tiếp frame n=24 (1 giây) bằng FFmpeg select đơn thuần, không drawtext: `artifacts/voice-qc/v01-visual-r1/frame-001sec.png`. Đã xem ảnh native 720×1280: nhãn tên vẫn hiện ở dưới trái. Vì vậy chữ tồn tại trong file V01, không do thao tác tạo grid hoặc UI player.

Finding VIS-02 được xác minh **nguồn chữ**, chưa được sửa hoặc miễn yêu cầu. Nhãn có thể mang dấu không đúng tên chuẩn; chưa dùng OCR để khóa từng ký tự. VIS-01 gesture cũng giữ mở. SHA256 V01 gốc kiểm lại vẫn `a291bf77c9b913de43a006f4737dfcb5d27da2e9811ca6812bdc045c6e81bf76`.

Owner proof: `C:/Users/PC/Downloads/du_an_nem_bui/V01_visual_2fps.png` và `V01_native_1sec.png`. Không crop/erase caption, không thay media gốc hoặc generate retry.

## V02 — chuẩn bị được, chưa chạy

Giữ exact V02 prompt 85, reference bàn v0.8 và Lite/frames/9:16/720p/8 giây/x1 theo 88. Không tự đổi lời hoặc prompt để chữa caption. Chưa fresh UI preflight/giá đầu vòng V02, không ghi settings/balance hiện hành từ snapshot cũ.

Khi đủ listening gate, kiểm lại actual UI model/mode/reference/count/giá 10 credit trước đúng một lượt V02. Khác cấu hình hoặc terminal không rõ → HOLD. Không dùng 10 credit dành V02 để retry V01.

V01 không đạt yêu cầu visual sạch của probe, nhưng vẫn là bằng chứng có thể dùng để owner nghe đánh giá voice. Không yêu cầu tạo lại chỉ để nghe. Duyệt giọng để tiếp tục thử V02 không đồng nghĩa chấp nhận V01 làm production take hoặc miễn các lỗi visual.

## Handoff

- Đã xác định: root và auditor đã kiểm actual sample; gesture lệch yêu cầu, chữ phát sinh được xác nhận trong frame native.
- Quyết định: tiếp tục QC; giữ native audio/không rephrase/Gemini deferred; không credit mới.
- Giả định: sample mapping đúng phép trích frame; ASR timecode vẫn chỉ ước lượng.
- Còn mở: nghe hồi/hội, rang/răng và chất giọng; full playback/lip-sync; khắc phục hoặc owner quyết định phạm vi visual; V02 preflight.
- Bước tiếp: owner nghe **V01 gốc**, xác nhận đủ lời và giọng Khoai phù hợp; sau đó V02 Lite theo 88. Retry/chỉnh prompt để chữa visual cần request/approval riêng. Chưa chuyển sang master hoặc đóng P6.
