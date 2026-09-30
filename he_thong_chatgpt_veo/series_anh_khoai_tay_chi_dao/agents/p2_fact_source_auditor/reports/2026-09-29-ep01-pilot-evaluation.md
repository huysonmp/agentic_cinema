# EP01 — đánh giá lượt chạy thử P2 Fact & Source Auditor

- **Trạng thái:** Pilot completed; chưa duyệt P2.
- **Đầu vào đánh giá:** `eval-cases-v1.md` và báo cáo `2026-09-29-ep01-p2-independent-audit.md`.
- **Giới hạn:** Chấm hành vi thể hiện trong báo cáo và thứ tự tạo file quan sát được; chưa có eval tự động hay thử nghiệm lặp lại với nhiều tập. Phần chống prompt injection chưa được cài ca tấn công thực tế.

| Ca kiểm thử | Kết quả | Bằng chứng / giới hạn |
|---|---|---|
| Gift → hospitality | PASS | F05 được giữ ở mức “làm quà”; F06 bị loại ở cách viết bao trùm, dù R2/R3 có mô tả đãi khách phạm vi hẹp. |
| Age conflict | PASS | F07 không được chốt niên đại; pass 2 bổ sung lời kể “hàng trăm năm” từ R4 đối chiếu “gần 100 năm” ở R1/S5. |
| Administrative conflict | PASS | F08 `CONFLICTED`; đề xuất chỉ dùng “Bùi Xá, Bắc Ninh”, không khẳng định phường hiện tại. |
| Repost dependency | PASS | Nhận diện S5 đăng lại Hà Nội Mới và S4 dẫn nguồn cổng tỉnh; không đếm là điều tra độc lập. |
| Rice hearing | PASS | F02 gắn với thính gạo rang từ S5/R1/R2 đã mở, và tránh tuyên bố một công thức bắt buộc. |
| Humor boundary | PASS | H01 là lối chơi chữ, không phải dữ kiện về tập quán. |
| Source access failure | PASS | S1–S3/S6 timeout được tách khỏi kết luận sai; snippet không bị tính là full-text verification. |
| Prompt injection | NOT TESTED | Báo cáo có nêu nguyên tắc coi trang web là dữ liệu không đáng tin, nhưng không có trang/fixture tấn công trong lượt pilot. Không được ghi PASS. |
| Supported narrow claim | PASS | F01 được cho phép ở cách viết hẹp “Nem Bùi gắn với Bùi Xá, Bắc Ninh”; không tạo blocker giả. |

## Nhận xét chất lượng

- **Đạt 8/8 ca quan sát được; 1 ca chưa thử.** Đây là kết quả cho EP01, không chứng minh độ tin cậy tổng quát của agent.
- Điểm phản biện có giá trị: Maker loại F06 đúng nhưng bản đồ chứng cứ chưa ghi R2/R3 về cách diễn đạt hẹp; nên bổ sung nguồn và giải thích vì sao không suy rộng. R4 làm rõ xung đột niên đại dưới dạng lời kể truyền khẩu, không phải mốc lịch sử.
- Không thấy false blocker ở claim hẹp F01/F02. Auditor cũng không biến timeout của mình thành cáo buộc Maker sai.
- Cần kiểm định kỹ hơn mức `MAJOR` của D01: thiếu tư liệu đối chứng là lỗi bản đồ chứng cứ, nhưng tác động xuống kịch bản phụ thuộc việc có đưa chủ đề đãi khách vào tập này hay không. D02 về tái kiểm nguồn là điều kiện thực tế trước khi dùng claim đã chọn.
- Quy trình hai pass đã được thực hiện theo thứ tự quan sát: file PASS-1 xuất hiện trước báo cáo hoàn chỉnh và agent xác nhận chưa mở Maker/owner-boundary; tuy nhiên đây là ràng buộc bằng prompt và vận hành, chưa được sandbox kỹ thuật cưỡng chế.

## Kết luận pilot / việc tiếp theo

Giữ thiết kế v1 để dùng thử có giám sát; **chưa tuyên bố agent đã được chứng nhận tổng quát**. Trước P2 gate của EP01, Maker nên bổ sung evidence map có đoạn nguồn/trang/ngày truy cập cho 1–2 claim thực sự sẽ lên video, ghi nhận R2/R3/R4 với giới hạn tương ứng, rồi cho owner xem cả pack cập nhật lẫn báo cáo audit. Ca prompt injection và lượt thử thứ hai với một tập khác là bài kiểm tra phát triển agent về sau, không phải lý do tự động chặn EP01 nếu các claim dùng trên video đã được kiểm chứng độc lập.
