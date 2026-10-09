# REC259 — Chốt C03A, sản xuất C03B và giữ cổng hành động

Ngày 09-10-2026. Owner trả lời “ok đấy” cho đúng bản mở đầu 15,5 giây ở REC258: câu hỏi Đào/D06, nhịp–khẩu hình và hai sai khác đã trình ở điểm nối 13,75 giây. Approval được lưu riêng, không duyệt native C03A đủ 4 giây hoặc các clip mới.

## Đã thực hiện

1. Trích nguyên khung cuối F41 của bản C03A được chọn, không quay lại master cũ. Nguồn là bản cắt đã mã hóa lại; không tuyên bố PNG giống tuyệt đối native.
2. DOP/ACT kiểm ảnh và prompt; sửa mâu thuẫn yêu cầu cười nhưng cấm mọi chuyển động môi. Phản biện độc lập đọc lại prompt/hash mới; root đọc đầy đủ trước gửi.
3. Dùng Computer Use đối soát Flow: đúng ảnh, chỉ K20 đúng ID, readback đúng, Omni 1.1 Flash/Ingredients/720p/9:16/4 giây/x1/Tác nhân tắt/tiếng bật. Gửi đúng một lượt giá 7 credit, tải gốc thành công.
4. Native 720×1280, 24 fps, 96 khung; video 4 giây, AAC 4,01 giây, giải mã đủ. Root xem toàn bộ ảnh rời, các khung đầy đủ và 56 khung quanh chỗ nối mới; đây không phải playback AV liên tục.
5. Nhận dạng ngoại tuyến không gợi ý trước ghi đúng “Chờ mẹ quay lưng.”, âm cuối đến khoảng 1,24 giây. Không lấy ASR làm chứng nhận K20 hoặc độ truyền cảm.

## Kết quả và giới hạn

- Trong 96 ảnh rời, miệng Khoai chuyển động ở lời đáp, miệng Đào khép; bốn tay nghỉ, đũa và món chưa được lấy, không thấy khói hoặc chữ mới ngoài watermark.
- **Chưa đạt toàn nhiệm vụ C03B:** Đào có phản ứng cười kín, sau đó quay ra trước thay vì hướng về cốc ngoài phải. Không được suy rằng Đào đã mất chú ý vào Khoai hoặc cho anh gắp khi cô vẫn đang nhìn.
- Root dựng một candidate 50 khung `[0,50)` / 2,083 giây, giữ lời và đầu phản ứng, bỏ đuôi quay ra trước. Ghép QC với bản mở đầu đã chốt thành 17,583 giây / 422 khung; hình–tiếng cùng gốc, không tăng tốc/đổi pitch. Điểm nối mới ở 15,5 giây không thấy nhảy tư thế lớn trong ảnh rời, nhưng còn phải nghe/xem thực.
- Candidate và bản nối **NOT_SELECTED**. C04 **HOLD**; không tự chạy lại hoặc dùng native đuôi làm reference tiếp.
- Phản biện độc lập kiểm đủ 96 native và 56 khung encoded quanh nối mới; root đọc toàn bộ báo cáo. Reviewer xác nhận thiếu hướng nhìn cốc và không thấy blocker seam hình mới. Candidate chỉ có đầu nụ cười rất nhẹ, không chứa phản ứng blink rõ hoặc động tác quay cốc. Không gọi full reaction hoặc full C03B PASS.

## Hai việc cần owner chốt

1. Nghe/xem đúng candidate: có đúng K20, trọn “Chờ mẹ quay lưng.”, nhịp–khẩu hình và chỗ nối mới chấp nhận được không?
2. Đề xuất A: giữ đoạn đáp–phản ứng này, chuyển toàn bộ động tác quay về cốc sang đầu C04; vẫn phải thấy Đào quay trước, rồi Khoai mới lấy đũa/gắp. Không bỏ hành động hoặc đổi câu chuyện. Phương án B: giữ ranh giới C03B ban đầu và làm lại C03B để có cả hướng nhìn cốc. A tránh tạo lại phần thoại hiện có, nhưng C04 vẫn chưa được tạo/kiểm và độ thành công chưa biết.

Nếu chọn A, còn khoảng 12,417 giây của mục tiêu 30 giây cho C04–C09; cần đo các action/thoại thực trước khi chốt EDL, không cắt âm cuối hay bỏ beat để ép thời lượng.

## Ngân sách và tài liệu

Thực chi 7 credit, số dư cùng tài khoản 1.008→1.001. Sổ dự án 129/500, còn 371: lượt đầu 119, tạo lại 97, bổ sung sau rough 45, dự phòng 110 vẫn đóng. Đây là hai số khác nhau: số dư tài khoản không mở rộng quyền chi của dự án.

- `restart_720p_v1/00_decisions/C03A-and-opening-approval-259.json`
- `restart_720p_v1/04_requests/C03B_T01_request_259.json`
- `restart_720p_v1/06_qc/run-registry-259.json`
- `restart_720p_v1/06_qc/C03B_review_derivatives_technical_259.json`
- Evidence/media tại `C:/Users/PC/Downloads/du_an_nem_bui/259_C03B`.

Không coi báo cáo giấy, preset ID, ASR hoặc chỉ ảnh rời là duyệt cả phim hay giọng thực. Giữ tất cả originals và trạng thái chưa đạt.
