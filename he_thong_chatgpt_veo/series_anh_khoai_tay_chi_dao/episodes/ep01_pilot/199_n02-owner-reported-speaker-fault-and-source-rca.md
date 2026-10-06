# EP01 — Lỗi người nói N02 và truy nguyên nguồn

Ngày 2026-10-06. Owner báo: **“sai đoạn `Hồi bé mẹ rang gạo, a đứng chờ`, đoạn đó là nam nói mà sao vẫn sai đi sai lại vậy”**, sau đó yêu cầu tiếp tục kiểm tra.

## Kết luận hiện hành

Toàn bộ N02 là lời Khoai, giọng nam **K20 / Orus tùy chỉnh**:

> Khoan. Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.

Ghi **N02 REWORK — OWNER_REPORTED_WRONG_SPEAKER**, không tiếp tục dùng N02 của A03 cho tiếng final. Sáu lượt còn lại chưa được xác minh đầy đủ; phản hồi này không nghiệm thu cả bộ tiếng. Không thay lời hoặc tuyển lại giọng.

Đây là bằng chứng nghe của owner, không phải root tự nghe hay máy nhận diện. Owner chưa chỉ rõ giọng thực tế là Đào/D06 hay giọng khác; không tự điền kết luận đó. Báo cáo 180/183/198 giữ như lịch sử; trạng thái hiện hành theo199.

## Truy nguyên đã kiểm tại vòng này

1. Prompt thực tế180 giao **cả N02** cho Khoai/Orus, còn ghi hai câu hồi tưởng thuộc cùng một lượt và Đào nghe. Không có chỉ dẫn giao “Hồi bé…” cho Đào. Prompt đúng không bảo đảm output đúng.
2. Giải mã audio native `180_c_v06_dialogue/A03.mp4` bằng FFmpeg ra PCM16-bit/48kHz/stereo: **trùng từng byte** với `A03_VOICE_REVIEW.wav` (1.920.960 byte PCM).
3. Toàn bộ PCM A03 là phần đầu **không đổi** của bản nghe bảy lượt198. File nghe198 và bản nối180 có cùng SHA256. Không có lượt tạo lại tiếng tại198.
4. Do đó lỗi owner nghe nằm trong nguồn A03 được tái sử dụng, không phát sinh do đổi nhãn speaker, chuyển WAV hoặc nối bảy lượt. Chưa đủ bằng chứng giải thích cơ chế bên trong dịch vụ sinh giọng.

File/hash và phép đối chiếu tại [bằng chứng](evidence/199/source-fault.json). Khoảng N02 theo excerpt183 là 2,08–7,81 giây nguồn A03, có đệm nghe; **không phải điểm cắt stem đã nghiệm thu**.

## Vì sao lỗi vẫn quay lại

- A03 được chọn kỹ thuật vì peak −0,4dBFS, trong khi A01/A02 đạt0dBFS; đây không phải lựa chọn theo kiểm từng người nói.
- ASR không xác nhận câu nào thực sự do K20/D06 nói. Speaker trong script/caption chỉ là vai dự kiến.
- Approval tạm181 không thay kiểm từng lượt. Audit183/SIA184 đã nêu thiếu kiểm nghe; tôi vẫn trình lại **cùng A03 chưa sửa** tại198.
- SIA có contract và validator hồ sơ, chưa có nhận dạng người nói tự động đã xác thực. Có agent/gate không đồng nghĩa đã nghe kiểm.

Nguyên nhân quy trình: **nguồn chưa đạt kiểm người nói vẫn được giữ làm working source, và lỗi chưa được xử lý nguồn trước khi trình lại**. Trách nhiệm thuộc khâu chọn nguồn/điều phối, không phải owner phải nhắc lại vai. Chưa kết luận khoảng nghỉ, dấu câu, preset hoặc server binding là nguyên nhân âm học.

## Đề xuất sửa có mục tiêu

Đã ghi loại N02/A03 khỏi lựa chọn tiếng final. Giữ native/bản nối nguyên trạng để truy vết; không xóa, đổi pitch hoặc sửa phụ đề để che lỗi. **AUDIO_SELECTION chưa đạt**, chưa chi sản xuất theo điều kiện nguồn tiếng tại197. Đây là ghi nhận disposition, chưa triển khai bộ chặn tự động toàn repo.

Đề xuất thay **toàn bộ N02** bằng một nguồn chỉ-Khoai/only-K20, không gắn D06 hoặc lời Đào trong request. Giữ C-v0.6 và chất giọng đã chọn. Kiểm đúng người xuyên suốt N02, so mẫu K20, rồi kiểm nhịp N01→N02→N03. Tách vai giảm độ phức tạp, không bảo đảm tuyệt đối không lỗi.

[Prompt sửa dự thảo](evidence/199/N02-single-speaker-DRAFT.txt) chưa gửi. Trước gửi phải kiểm model hỗ trợ voice reference, preset ID/token thực, ảnh đi kèm, cảnh báo input, x1 và giá trực tiếp. Không dùng quote Lite/Frames10 tại198 như giá đã xác minh cho tuyến giọng. Sau thao tác nguồn phải đọc lại compose cuối; không bấm chip mở preview vì có thể gỡ input theo lỗi172.

Gói100 tại198 **không gồm sinh lại giọng**. Đề nghị owner cho phép đổi phạm vi: dành **tối đa10 trong100 còn lại** cho đúng một lần sửa N02/x1, không mở bộ ba mẫu. Nếu duyệt, tối đa90 còn lại cho hình: dự toán cơ sở80, dự phòng tối thiểu10 thay vì20. Giá thực vượt10 hoặc cần retry phải trình lại. Đề xuất chưa được duyệt, chưa kiểm giá hoặc gửi.

## Tổng hợp

- Đã xác định: đúng vai N02; nguồn A03 giữ nguyên từ native đến bản nghe; lỗi lặp là nguồn cũ chưa sửa.
- Đã chốt: N02/A03 REWORK theo owner, không dùng tiếng final; giữ K20/D06/C-v0.6.
- Giả định: nguồn chỉ-Khoai phù hợp để thay trọn lượt, cần kiểm nghe sau tạo.
- Còn mở: cơ chế dịch vụ sinh sai, identity nguồn thay, sáu lượt khác và gate hình–tiếng cuối.
- Tiếp: duyệt chuyển tối đa10 cho một lần sửa N02; kiểm input/giá trước tạo, rồi trình đúng đoạn sửa. Không tuyển giọng lại.

Chi vòng này **0**, cap **422**, spent **322**, còn **100**. Chưa tạo/sửa audio/video, chưa Quality/master/phát hành. Owner folder: `C:/Users/PC/Downloads/du_an_nem_bui/199_n02_source_rca/`.
