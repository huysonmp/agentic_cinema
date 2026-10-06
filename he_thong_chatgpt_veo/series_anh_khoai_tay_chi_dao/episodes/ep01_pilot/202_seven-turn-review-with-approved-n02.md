# EP01 — Bản nghe bảy lượt, thay bằng N02 đã duyệt

Ngày 2026-10-06. Owner đã duyệt toàn N02 mới: **“Đúng Khoai/K20 xuyên suốt, nhịp chấp nhận được”** tại [201](201_n02-native-received-and-local-qc.md). Lượt này chỉ ráp bản nghe đối chiếu, không sinh media hoặc dùng credit.

**Cập nhật [203](203_audio-join-approved-and-picture-production.md):** owner “ok r đấy” đã duyệt người nói/chỗ nối của bản nghe này đúng hash. Các nhãn chờ duyệt dưới đây mô tả thời điểm trình 202, không còn là trạng thái hiện hành. Chưa nghiệm thu bản ghép hình–tiếng hoặc master.

## Đầu ra

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/202_dialogue_join_review/`.

File: `EP01_7_LUOT_N02_MOI_REVIEW_NOT_FINAL.wav`, PCM 16-bit/48 kHz/stereo, dài **22,055 giây**. SHA256: `3c83b7d6188f5b973b0ef5c77ebc1fc16afde7c11827764c5302145741b736d4`.

Đây là bản nghe đầy đủ, **không phải tiếng final, video 30 giây hoặc bản phát hành**. [Manifest](evidence/202/manifest.json) ghi nguồn, hash, thứ tự và đoạn sử dụng; [ASR](evidence/202/asr.json) ghi nhận dạng không có prompt mồi.

## Bảng nguồn và thứ tự

Mốc dưới đây thuộc bản nghe 22,055 giây, không phải timeline dựng đã chốt.

| Lượt | Người nói theo script | Nguồn sử dụng | Mốc bản nghe (giây) |
| --- | --- | --- | --- |
| N01 | Đào | Trích 183, từ A03: 0–2,15 | 0–2,15 |
| N02 | Khoai | Toàn WAV mới đã duyệt 201; không cắt | 2,15–12,155 |
| N03 | Đào | Trích 183, từ A03: 7,92–8,79 | 12,155–13,025 |
| N04 | Khoai | Trích 183, từ A03: 8,90–9,93 | 13,025–14,055 |
| N05 → N06 → N07 | Đào → Khoai → Đào | Toàn tiếng native R01; giữ chỗ nối trong nguồn | 14,055–22,055 |

Không đưa đoạn N02 cũ 2,08–7,81 của A03 hoặc file trích N02 cũ vào bản mới. A03 chỉ được giữ làm nguồn của N01/N03/N04; không sử dụng nguyên tiếng A03. Các file gốc vẫn được giữ để truy nguyên.

## Đã kiểm và chưa thể kết luận

Đã chạy `scripts/build_ep01_n02_replacement_review.py`: kiểm hash cố định của các đoạn giữ lại, nguồn kết và WAV N02; bắt buộc approval toàn N02 đúng hash; từ chối ghi đè folder có sẵn. Script không gọi API hoặc tạo tiếng mới.

Kiểm đầu ra PCM khớp từng byte với các khối nguồn đã xếp đúng N01–N07. Khối N02 giữ nguyên toàn bộ PCM; hash nguồn không đổi sau dựng. Không thêm gain, pitch, tăng tốc, fade hoặc mix. Bốn bài kiểm thử đều đạt, gồm từ chối approval sai, hash sai và định dạng WAV sai. Đây là kiểm nguồn/kỹ thuật, **không phải kiểm nghe tự động**.

Local ASR offline nhận đủ lời theo thứ tự:

1. Đào: “Anh nhìn mãi. Không hợp thì để em.”
2. Khoai: “Khoan. Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.”
3. Đào: “Anh chờ ăn à?”
4. Khoai: “Chờ mẹ quay lưng.”
5. Đào: “Chờ em quay lưng nữa à?”
6. Khoai: “Anh gắp cho em mà.”
7. Đào: “Thế em quay lại đúng lúc rồi.”

Danh sách trên là script duyệt để đối chiếu, không phải transcript nguyên văn. ASR vẫn nhận “gian” thay “rang”; giữ nguyên bằng chứng, không mở vòng sửa vì chưa có lỗi nghe xác nhận. ASR không xác minh người nói. Âm lượng trung bình −17,1 dBFS, đỉnh −0,4 dBFS; chưa chuẩn hóa tiếng final.

Root chưa nghe âm thanh. Chưa có formal SIA report toàn bảy lượt; không gắn PASS từ script/ASR. Owner duyệt N02 riêng không tự duyệt bản nối. Các đoạn trích 183 dùng lại đúng file nhưng chỗ cắt chưa được nghe nghiệm thu; bản này cho phép kiểm trực tiếp trước khi chọn nguồn dựng.

## Trình nghe và bước kế tiếp

Đã trình file mới trực tiếp trong chat, hỏi duy nhất: **từng lượt có đúng người nói và chỗ nối chấp nhận được để sang dựng hình không?** Không tuyển giọng lại hoặc mở thêm thử nghiệm.

Trạng thái lúc lưu: **chờ owner duyệt bản nối**. Có thể chỉ rõ lượt/mốc nếu cần sửa; không tự sinh lại tiếng.

Nguồn N02 vẫn chứa toàn đuôi 10,005 giây. Chưa thêm nhịp hành động sau N04 (Đào nhìn sang, Khoai lấy nem, bị phát hiện) hoặc intro/outro. Không lấy 22,055 giây rồi tuyên bố đã đủ cấu trúc phim; mục tiêu vẫn 30 giây. Sau duyệt cần cập nhật timing dựng theo tiếng hiện hành, đặt nhịp hành động đúng chỗ, rồi thực thi gói hình đã duyệt trong phạm vi ngân sách. Không kéo dài bằng thoại mới hoặc tăng tốc lời để cứu slot cũ.

## Kinh nghiệm lưu vào quy trình

Khi sửa một lượt trong nguồn nhiều người nói, phải tách bảng nguồn theo line ID. Chỉ thay đúng lượt lỗi, kiểm hash/phạm vi rồi ráp bản nghe hiện hành; không dùng lại bản nghe cũ như thể đã sửa. Approval cần gắn với file/hash cụ thể, không chỉ tên giọng hoặc tên nhân vật. Mỗi lớp kiểm phải ghi rõ: nguồn/PCM, nội dung nhận dạng, nghe nghiệm thu và hình–tiếng là các kiểm khác nhau.

## Tổng hợp

- Đã xác định: đủ bảy lượt trong bản mới; N02 mới nguyên vẹn, N02 cũ không được đưa lại vào.
- Đã chốt: N02 riêng đã duyệt; không thay C-v0.6, K20/D06 hoặc tạo thêm tiếng.
- Giả định làm việc: các đoạn giữ lại phù hợp để nghe đối chiếu, chưa mặc nhiên là điểm cắt final.
- Còn mở: owner duyệt bản nối; timing 30 giây và kiểm hình–tiếng.
- Tiếp: chốt bản nối, cập nhật dựng hình theo nguồn hiện hành và dùng gói hình đã duyệt; chưa master/phát hành.

Chi lượt này **0 credit**. Trần 422, đã chi 329, còn 93. Không xin thêm ngân sách hoặc mở lượt thử mới.
