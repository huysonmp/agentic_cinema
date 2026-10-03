# 164 — Thử phản ứng bằng prompt ngắn

## Phạm vi được duyệt — 2026-10-03

Owner trả lời “ok” cho đề xuất sau vòng 163: giữ hai khung nem thấp, chạy ba Lite cùng prompt ngắn, chỉ một nhịp Đào quay nhìn Khoai; kiểm trước khi ghép giọng. Không phải duyệt cảnh hoàn chỉnh hoặc Quality. Hạn mức bộ thử 30 từ khoản còn 54; Quality 100 riêng không sử dụng.

## Đầu vào và preflight

- START: `C:/Users/PC/Downloads/du_an_nem_bui/161_source_retest/START_short_tuft_v0.1.png`; SHA256 `E8A9AA146CB5CE0EE8596B0AE716951D6F68FEAA5FE3E5E007DA4615ABC0B4BD`.
- END: `C:/Users/PC/Downloads/du_an_nem_bui/163_low-hold-reaction/END_low_reaction_v0.1.png`; SHA256 `A85C816872CC794326F07066B90FC8F6A68F500FAC26DF20620E1A2760EFE5F7`.
- Flow dự án `9276788e-9781-44fb-ba5b-083006667374`; Veo 3.1 Lite, Khung hình, 9:16, 720p, 8 giây, x3; Tác nhân tắt. UI báo 30 credit, số dư trước 354.
- Media và ảnh bằng chứng: `C:/Users/PC/Downloads/du_an_nem_bui/164_short-reaction/`.
- Không sửa ảnh. Tính chuẩn món và continuity với C01 vẫn phải kiểm riêng; đầu vào được tái sử dụng cho so sánh kỹ thuật, không tự nâng thành canon mới.

## Prompt nguyên văn

```text
Locked tripod. Match the supplied frames. Dao makes one slow head turn from her glass to look at Khoai, then holds the knowing look. Khoai keeps his lips closed and glances at Dao. His hand, the two chopsticks and the small tuft of nem stay low above his bowl for the entire shot. Both characters keep their hands at the supplied positions. Preserve both identities, clothes, table items and lighting.
```

Không có đoạn mô tả âm thanh. Điều này không đồng nghĩa đã tắt âm thanh. Ba mẫu cùng cấu hình; seed không được kiểm soát, chưa đủ kết luận nhân quả so với 163.

## Gate review

Kiểm toàn clip và dày vùng nghi vấn: nem thấp trên bát, không đưa tới miệng; hai đũa và tuft ổn định; Khoai không tự nói; Đào quay nhìn một lần rồi giữ, không thêm động tác tay/cốc. Giữ danh tính, trang phục, bàn ăn, ánh sáng; không hơi nóng từ nem. Lỗi tạo âm thanh được phân loại là lỗi công cụ, không chấm fail hình khi không có video. Chỉ file tải thật và giải mã thành công mới được ghi đã nhận.

## Kết quả

Đã gửi x3: hai video, một lỗi âm thanh. Thay một lượt lỗi bằng x1 cùng prompt/khung/model; lượt thay cũng lỗi âm thanh, UI ghi không tính phí. Tổng bốn yêu cầu, hai media, hai lỗi công cụ. Chưa đủ ba video để so sánh; không đổi prompt trong vòng này và không tiếp tục retry vô hạn.

| Mẫu | Flow ID | Tệp native trong Downloads | Review hình |
| --- | --- | --- | --- |
| R01 | d4539c77-9f3d-4cf8-8f25-d2180db2f714 | Two_characters_having_dinner_20261003081015.mp4 | Khoai nâng nem tới vùng miệng, mở miệng khoảng 0,75–1,5s rồi hạ; Đào thêm cử chỉ tay và gaze qua lại. Không đạt |
| R02 | ed94ac20-e829-4735-8c32-329de2938f9e | Two_characters_having_dinner_20261003081038.mp4 | Khoai nâng nem/mở miệng khoảng 0,75–1,25s rồi hạ; Đào thêm cử chỉ và nhìn ra ngoài trước khi nhìn Khoai. Không đạt |

Đã tải native 720p, copy thành R01/R02 trong folder 164 và giải mã toàn file không lỗi. Cả hai H264, 720x1280, 24fps, 8s, AAC. Kiểm grid toàn clip 2fps và đoạn đầu 0–2s tại 8fps (`R01-grid.png`, `R02-grid.png`, `R01-dense.png`, `R02-dense.png`). Mẫu đủ bằng chứng loại tại gate động tác; chưa cần gọi là đã ăn/cắn, không suy luận mức độ đạt giọng từ stream AAC. Không thấy hơi nóng trong khung đã kiểm; chưa chứng nhận toàn bộ frame, hình chuẩn món hoặc continuity C01.

Credit trước 354, sau 334, chi ròng **20**; khoản thử còn **34**. Quality 100 riêng chưa dùng. `balance-before.png`, `balance-after.png`, `results-final.png` là bằng chứng UI. X1 chỉ dùng thay lỗi; đã khôi phục x3 cuối vòng, không gửi thêm.

## Tổng hợp sau vòng

- Đã xác định: prompt ngắn cùng hai khung thấp vẫn sinh nâng nem/mở miệng và cử chỉ ngoài yêu cầu ở cả hai video nhận được.
- Quyết định xử lý: loại cả hai khỏi ghép; chưa chuyển Quality hoặc voice; không nâng thành owner-approved cảnh. Owner chỉ duyệt bộ thử.
- Giả định đang dùng: bối cảnh cầm nem có thể gợi động tác ăn; đây chưa phải nguyên nhân được chứng minh. Không kết luận độ dài prompt là nguyên nhân hoặc đã được giải quyết.
- Còn mở: phản ứng một nhịp, ổn định tay/miệng, lỗi âm thanh, đủ ba mẫu, continuity với C01 và đoạn chuyển nem vào bát.
- Bước tiếp theo đề xuất, chưa gửi: thiết kế cận phản ứng Đào có Khoai ở tiền cảnh để tách diễn ánh nhìn khỏi chuyển động tay, nối với C01/shot giữ nem bằng continuity sheet. Mục đích là rõ nhịp bắt gặp, không che lỗi và gọi cảnh cũ đã sửa. Trình khung/góc nối trước một bộ x3 Lite mới; khoản còn 34 đủ giá bộ 30. Không đổi kịch bản hoặc giọng đã chốt.
