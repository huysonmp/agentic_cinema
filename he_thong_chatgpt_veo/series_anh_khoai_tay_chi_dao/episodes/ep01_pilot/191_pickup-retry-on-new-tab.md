# EP01 — Thử lại gắp trên tab Flow mới

## Cập nhật approval tại192

Owner đã duyệt **nhịp P02 đầu0–2,5s** tại[192](192_pickup-rhythm-approval-and-local-join.md). Trạng thái chờ chọn dưới đây là lịch sử. Chỉ nhịp/range được duyệt, không PASS native8s, FOOD toàn cảnh hoặc điểm nối; không tăng quyền chi.

Ngày 2026-10-05. Owner yêu cầu “mở tab mới rồi chạy đi”, cho phép thử lại batch190 đã lỗi không tính phí. Giữ một yêu cầu x3 Lite tối đa30 trong phần còn30, không thêm ngân sách hoặc mở hành động/Quality khác.

## Preflight và submit

- Tab mới cùng browser/account/project `9276788e-9781-44fb-ba5b-083006667374`; không đổi provider hoặc tắt bảo vệ.
- Account trước244; Frames, Veo3.1 Lite, 9:16, 720p, 8s, x3; quote live30. Silent fallback ON, Agent OFF.
- Chọn START/END188 đã upload ở190, kiểm trực quan hai thumbnail: từ đầu đũa chạm đĩa đến giữ một miếng trên bát riêng. Không dùng ảnh185.
- Prompt giữ nguyên [190](evidence/190/prompt-pickup-SUBMISSION.txt), đọc lại khớp; không sửa đa biến trong thử phục hồi phiên.
- Submit một lần **2026-10-05T14:33:10.466Z** (21:33:10 giờ Việt Nam). Ba thẻ yêu cầu xuất hiện; ở thời điểm ghi ban đầu chưa có native để QC.

## Đã hoàn tất và tải đủ

Cả ba video mới đã có trong Flow và tải 720p gốc. Account244→214 sau submit, đọc lại sau hoàn tất vẫn214; chi ròng30. Sổ dự án **262/262, còn0** trong quyền chi. Account214 không cấp quyền thử tiếp. Không lỗi/refund ở batch191; lỗi190 vẫn chi0.

| Mã local | ID Flow | SHA256 native |
| --- | --- | --- |
| P01 | 204dd5e6-0ee5-40e1-9f25-2c3bb6c58178 | 59bad62f23a00ea913d961b10ca9204c3f794da31805a82a04bc967baa6b9ae1 |
| P02 | c1abc9fa-56b8-4cd6-a1cd-3c4b964fbd34 | d45e28ae30d26109adf598984176c8ec44a4db2f52d0da9985fc27c2ba53efc6 |
| P03 | 5b4e1007-cc51-4e85-8082-d36d315a8943 | b4d3a610699083eb770d2f4025697b1d49fbf5d4abb80df42e1777afc49500fc |

Mã theo thứ tự tải, không thứ tự lưới: lưới trái→phải P02/P01/P03. Bản so sánh local trái→phải P01/P02/P03. [Manifest tải](evidence/191/download-manifest.json), [technical report](evidence/191/technical-report.json), [ảnh batch](evidence/191/completed-batch.png).

Ba native đều8s/720×1280/24fps/H.264, full decode sạch, **có AAC stream** dù silent fallback ON. Chưa nghe nội dung track; không suy audio im lặng từ cài đặt. Native giữ nguyên, hai bản xem dẫn xuất loại audio local. Chưa dùng audio này hoặc đổi giọng đã chốt.

Tải P01 ở tab tạo chưa về file; mở tab riêng đúng URL asset + menu720p nhận file. P02/P03 cũng nhận ở tab đó. Callback download đều hết thời gian chờ dù file đã đến trong ba lượt sau; kiểm đường file/bytes/hash/decode trước mọi retry. Không tái sinh video để chữa tải. Tab mới đã cho generation thành công ở vòng này, **không chứng minh nguyên nhân lỗi190 hoặc cam kết cách này luôn hiệu quả**.

## Review hình — root, chưa nghiệm thu độc lập

Kiểm16 khung mỗi clip cách0,5s từ0–7,5s. Với P02/P03, xem thêm toàn72 frame native của0–3s trong bảng180×320/frame; mở native frame P02 tại2,75s và P03 tại2,708s để xác nhận vệt hơi mờ. Chưa xem mọi frame3–8s ở native resolution, chưa review nghe hoặc agent độc lập; không gọi PASS toàn take.

| Mẫu | Quan sát | Kết luận |
| --- | --- | --- |
| P01 | Gắp khỏi đĩa và kéo về bát, nhưng nâng/giữ cao hơn điểm END, vệt hơi rõ quanh ngực từ khoảng2s. | REWORK toàn clip. |
| P02 | Một lượt gắp/kéo về bát, phần đầu0–2,5s có thể làm insert; sau khoảng2,7s thấy vệt hơi quanh áo, cuối clip hạ tay về END. | REWORK toàn8s; đề xuất đoạn hẹp để owner xem. |
| P03 | Một lượt gắp/kéo về bát, có nâng thêm rồi hạ; vệt hơi mờ quanh áo khoảng2,7s. | REWORK toàn8s; phương án đối chiếu, không chọn mặc định. |

Không thấy quay về đĩa gắp lần hai/thả món hoặc miệng trong các frame đã xem. Đó là quan sát trong phạm vi kiểm, không chứng nhận conservation từng sợi hoặc hành động ngoài khung. Các vệt hơi quanh áo không cho biết chính xác nguồn phát; vẫn không phù hợp phép thử món nguội.

## Gói owner xem

Folder: `C:/Users/PC/Downloads/du_an_nem_bui/191_pickup_new_tab/`.

- `P01.mp4`, `P02.mp4`, `P03.mp4`: native nguyên8s, giữ audio stream.
- `P01-P02-P03_FULL8s_SILENT_COMPARISON.mp4`: ba native đủ8s, thu mỗi ảnh về360×640 và ghép ngang, không tăng tốc/cắt bỏ lỗi; chỉ bỏ audio. SHA256 `05bf157c96231217e79a52163e03ff1972a715018207dd76329b6ee698c18c78`.
- `P02_0.00-2.50_SILENT_CANDIDATE.mp4`:60 frame/2,5s,720×1280/24fps, bỏ audio, không crop/đổi tốc độ; decode sạch. SHA256 `9dde08e3bef922ee8b1456b10d2bb6552ff40d6406eea6d9ae73cddc34b5045b`.

Đoạn P02 đề xuất giữ đúng hành động gắp chưa ăn và kết thúc trước vệt hơi đã phát hiện. Không dùng bản cắt để che lỗi hoặc gọi native8s đã đạt; giữ native/bản so sánh để owner thấy toàn bộ. Trong60 frame đầu đã xem không thấy vệt hơi rõ; vẫn cần owner xem nhịp liên tục và kiểm nối. Chưa đưa vào182/186; chưa END tiếp nối khớp pixel, FOOD toàn cảnh hoặc continuity PASS.

## Tổng kết vòng

- Đã xác định: tab mới nhận batch và có đủ ba native; lỗi tải được xử lý ở tab asset, kỹ thuật decode đạt, toàn take hình còn lỗi.
- Quyết định đã chốt: thử lại đúng batch x3 trong30, không mở Quality hoặc hành động tiếp.
- Giả định làm việc: insert P02 đầu2,5s có thể nối sang phản ứng Đào; chưa kiểm chứng mạch/nối.
- Còn mở: owner chọn/duyệt nhịp gắp, vệt hơi/điểm giữ ở phần sau, join native→khung nâng/Đào, hình thiếu, SIA HOLD.
- Tiếp: owner xem P02 đoạn đầu/bộ so sánh; nếu chấp nhận cơ chế thì kiểm nối local không chi thêm. Generation tiếp cần quyền chi mới. C-v0.6/K20/D06 giữ nguyên; chưa master/publish.
