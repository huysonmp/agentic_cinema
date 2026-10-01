# P6 — Grip: gói ảnh để owner xem

**SUPERSEDED recommendation:** owner phản hồi “cầm đũa ngược” với I09. [Record61](61_p6-owner-grip-rejection-2026-10-01.md) ưu tiên: I09 OWNER_REJECTED/REWORK, rút đề nghị chọn ref; I07 HOLD chờ kiểm lại cùng họ grip. Nội dung packet bên dưới là lịch sử trình duyệt, không recommendation hiện hành.

Ngày2026-10-01. Đây là packet lựa chọn, không approval. Kế thừa authority và exact prompts/results ở59. Nhân vật/body/outfit baseline45 không đổi, scriptC-v0.5 không đổi. P6 OPEN.

## Hai ảnh chính

| Candidate | Vai trò | Điều đã kiểm | Không xác nhận |
|---|---|---|---|
| [I07 cận tay](../../media/raw/ep01_p6_consistency/H-K-I07_v0.1.jpg) | Ref đọc cấu trúc cầm đũa | CONT AP-MEDIA-03 bounded static-readability PASS_FOR_NEXT_GATE: upper-control/lower-support nhận diện được, hai que, tipsphải, không impossible visible contact | Không motion, không full-character identity, không chứng minh phần khuất I06 |
| [I09 tích hợp](../../media/raw/ep01_p6_consistency/H-K-I09_v0.1.jpg) | Ref nửa người có mặt/tay | Root actualview rõ hơn fullbody; CONT AP-MEDIA-04 report12 PASS_FOR_NEXT_GATE trong bounded static identity+grip-readability; đủ mặt/tay/two sticks, tỷ lệ tự nhiên | Không owner approval, không motion/food, không final9:16 delivery |

[I08](../../media/raw/ep01_p6_consistency/H-K-I08_v0.1.jpg) giữ làm lịch sử thử: còn toàn thân, không đạt waist-up/readability target. Không loại/xóa raw; không trình như ảnh tích hợp đã pass.

## Cách dùng approval nếu owner chấp nhận

Đề nghị chọn **I07 làm hand-detail reference và I09 làm integrated static-grip reference** dựa trên actual reports11/12 (root đã đọc). Headroom I09 rộng hơn prompt intent; không ảnh hưởng vùng kiểm nhưng chưa bố cục final. Không duyệt cả P6 hoặc bảo đảm gắp/đổi hướng/chuyển nem. Không thay primaryduo45. Dùng refs này ở bước sau phải gắn đúng version, không dựa vào tên card mutable.

Điều owner trực tiếp xem: gương mặt Khoai có còn đúng chất; tay/đũa có tự nhiên và hợp style; cặp ref này có đủ làm baseline tĩnh cho thử action sau không. Không bắt owner xác minh contact khuất hoặc “diễn” thử. Agent/root vẫn chịu việc QC và ghi unknown.

## Còn mở và next

- Functional motion: pickup → đưa gần miệng → khựng → chuyển sang bát Đào; chỉ kiểm qua video khi P7/P8/request được duyệt, chưa chạy.
- Food F-NB-02 chưa terminal evidence; không submit duplicate. Food reference/fidelity approval riêng.
- Other P6 gaps (profile/eyeline/voice…) không được hai ảnh tay tự đóng.
- Diagnostic3:4 không là sửa video format. Mọi request video vẫn phải kiểm/đặt9:16 và đọc feature/cost hiện hành.

Giả định: grip tĩnh đủ nhận diện vai trò upper/lower, không đòi nhìn xuyên các ngón che que; scope này không chứng nhận mọi cơ học khuất. Các ảnh generation là separate versions, không pixel-proof của ảnh trước.
