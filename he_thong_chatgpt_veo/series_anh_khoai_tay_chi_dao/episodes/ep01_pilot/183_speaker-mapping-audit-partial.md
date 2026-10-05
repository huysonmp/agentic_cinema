# EP01 — Đối soát người nói: kết quả kỹ thuật, chưa xác minh identity

Ngày: 2026-10-05. Owner báo “nhầm voice người này nói người kia” và yêu cầu kiểm tra. Đây là chẩn đoán, không phải phép thử sinh giọng hoặc sửa nguồn.

## Kết luận có bằng chứng

1. Script178/package179 gán đúng vai dự kiến. Prompt180 ghi Khoai/K20/Orus và Đào/D06/Aoede, bốn lượt đầu đúng thứ tự. Chưa chứng minh công cụ sinh đã thực hiện đúng liên kết mỗi câu.
2. Kiểm lại trực tiếp WAV bản ráp182 với A03 nguyên nguồn và PCM giải mã mới từ R01: đoạn tại2s và20s khớp. Builder không cắt rồi đảo từng câu, không đổi tốc độ/âm lượng. Nếu audio có lỗi người nói, builder đã mang nguyên lỗi nguồn vào. Không dùng kiểm này xác nhận môi trong video hoặc speaker identity.
3. `speaker` trong captions/manifest182 là vai **dự kiến từ script**, không là người nói nhận diện từ audio. `local_voice_qc.py` chỉ chạy faster-whisper small, không có diarization/known-speaker verification. `speaker_verdict: NOT_PROVEN_BY_ASR` ở results180 còn hiệu lực về phương pháp.
4. A03 được chọn theo peak−0,4dBFS, không phải so từng lượt với K20/D06. Đây là thiếu gate đúng người nói tại chọn nguồn. Owner tạm chấp nhận giọng không chứng minh mọi lượt được gán đúng vai.

Lỗi quy trình đã xác định: đem kiểm text/PCM/mức âm thay cho kiểm người nói. Cơ chế sinh lẫn vai và các câu cụ thể đang sai **chưa được xác minh độc lập**; phản ánh của owner được ghi nhận, không biến thành kết luận máy đã nghe từng câu.

## Bảy lượt đã tách để kiểm

| Lượt | Vai dự kiến | Khoảng trong bản ráp30s | Lời | Identity thực tế |
| --- | --- | --- | --- | --- |
| N01 | Đào/D06 | 2,00–4,00 | Anh nhìn mãi. Không hợp thì để em. | Chưa xác minh |
| N02 | Khoai/K20 | 4,20–9,66 | Khoan. Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ. | Chưa xác minh |
| N03 | Đào/D06 | 10,04–10,64 | Anh chờ ăn à? | Chưa xác minh |
| N04 | Khoai/K20 | 11,02–11,78 | Chờ mẹ quay lưng. | Chưa xác minh |
| N05 | Đào/D06 | 20,00–21,90 | Chờ em quay lưng nữa à? | Chưa xác minh |
| N06 | Khoai/K20 | 22,62–23,84 | Anh gắp cho em mà. | Chưa xác minh |
| N07 | Đào/D06 | 24,74–26,34 | Thế em quay lại đúng lúc rồi. | Chưa xác minh |

Script `scripts/audit_ep01_speaker_mapping.py` chạy thực tế, tạo bảy đoạn WAV nguyên PCM có đệm ngắn trước/sau, không sửa nguồn hoặc bản ráp. Timing dựa trên ASR chỉ hỗ trợ tìm chỗ nghe, không phải final stems/forced alignment. Tên có `intended` và `UNVERIFIED` để không hiểu thành role PASS.

Folder local: `C:/Users/PC/Downloads/du_an_nem_bui/183_speaker_audit/`. Bằng chứng [speaker-audit.json](evidence/183/speaker-audit.json) lưu từng lượt, giọng dự kiến, nguồn, timecode, hash và observed_speaker=null.

## Giới hạn thực tế và việc cần để hoàn tất

- Các gói audition149/151 có ảnh và preset UI, chưa có WAV gốc K20/D06 local. Không lấy một câu đang nghi sai rồi gọi nó là mẫu chuẩn để kiểm chính nó.
- Không có công cụ nghe/nhận diện speaker đã chạy thành công. Skill transcribe đã đọc cùng reference/CLI; route known-speaker diarization cần `OPENAI_API_KEY`, biến này thiếu trong phiên hiện tại. Không tìm/đọc khóa bí mật ở file khác, không gọi API, cài thêm hoặc upload audio.
- Không kết luận nam/nữ hoặc identity chỉ từ cao độ, ASR, ảnh miệng, tên file hay token đã gắn vào prompt. Hai vấn đề voice identity và người đang mở miệng phải kiểm riêng rồi đối soát chung.
- Để tự kiểm bằng máy theo mẫu, cần lấy đúng hai audio reference K20/D06 và có công cụ nhận diện chạy được. Nếu dùng route của skill transcribe, owner phải cấu hình key cục bộ (không gửi key trong chat); kết quả vẫn là bằng chứng máy cần kiểm độ tin cậy, không chứng nhận tuyệt đối chất giọng/diễn.
- Phương án không dùng API: kiểm nghe thủ công bảy excerpt với preset chuẩn trong Flow, ghi người thực tế và kết luận từng câu. Chưa thực hiện bằng người nghe trong lượt này.

Ngân sách: **chi0**, sổ vẫn202/255, còn53 được phép thử; số dư224 là snapshot182, không đọc live lại trong lượt183. Không sinh lại audio, không chuyển Quality, không coi bản182 đạt đúng người nói. Chưa sửa builder/gate production hoặc chọn nguồn thay thế.

## Tổng kết vòng

- Đã xác định: gán vai dự kiến đúng; không đảo câu lúc dựng; thiếu kiểm identity thực tế tại chọn nguồn.
- Quyết định giữ nguyên: C-v0.6, K20/D06 và quyền chi; chưa chọn lại giọng.
- Giả định: không dùng broad approval làm nghiệm thu vai từng câu; lỗi nguồn còn phải xác minh.
- Còn mở: các lượt thực tế sai, identity với mẫu chuẩn, khớp môi và route nhận diện khả dụng.
- Bước tiếp: có mẫu reference/công cụ hoặc người nghe để điền observed_speaker; chỉ khi đó chọn đoạn thay và sửa nguồn. Không đổi nhãn để che lỗi hoặc gửi batch thử mù.
