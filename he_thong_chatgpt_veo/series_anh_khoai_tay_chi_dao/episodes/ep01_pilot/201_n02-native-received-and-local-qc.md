# EP01 — Đã nhận native N02 mới, kiểm local và trình nghe

Ngày 2026-10-06. Owner yêu cầu tiếp tục sau lượt 200. Không sinh thêm hoặc dùng lại N02 cũ trong A03.

## File thực đã nhận

Kiểm Downloads thấy `Character_recording_audio_direction_20261006120100.mp4`, 1.197.956 byte, thời gian sửa 12:01:01 ngày 06/10. File chưa có tại các lần kiểm ở lượt 200, nay đã có; chưa biết thao tác tải nào hoàn tất. Không kết luận timeout luôn đồng nghĩa tải thất bại hoặc owner đã phải tải lại.

Giữ file gốc; sao lưu vào `C:/Users/PC/Downloads/du_an_nem_bui/200_n02_replacement/N02_NATIVE.mp4`. SHA256 cả hai: `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153`.

Đối chiếu với clip 200, ID `3b312ed6-ac2b-4798-b965-cffe5f738893`: tên native phù hợp tên UI, metadata 10 giây/360p, khung hình tại 2,29 giây phù hợp screenshot 200 và nội dung lời là N02. Đây là đối soát nội dung/thuộc tính; không tuyên bố media ID được nhúng trong MP4 hoặc có checksum từ Flow để so độc lập.

## Kết quả kiểm kỹ thuật

- FFprobe: Google encoder, H264 360×640/24 fps, AAC 48 kHz/stereo, dài 10,005 giây.
- Giải mã toàn video và audio bằng FFmpeg: exit 0, không báo lỗi.
- Tách `N02_EXPECTED_K20_REVIEW.wav`, PCM 16-bit/48 kHz/stereo. **Toàn bộ 1.920.960 byte PCM khớp giải mã native**; không đổi âm lượng/cao độ/tốc độ, không cắt khoảng nghỉ hoặc đuôi âm.
- SHA256 WAV `52c7a027f55c6e354b0c5ac1d697bd8789682bfbc9ac99907a45e741f129b062`; dài 10,005 giây. Tên EXPECTED_K20 ghi vai/giọng dự kiến, không tự là kết luận kiểm nghe.
- Đo âm lượng trung bình −19,2 dBFS, đỉnh −1,5 dBFS. Đây là số đo, không nghiệm thu độ ấm, diễn xuất, méo tiếng hoặc identity.

[Kết quả và hash](evidence/201/results.json), [metadata](evidence/201/media.json), [ASR](evidence/201/asr.json), [khung đối chiếu](evidence/201/native-frame.png). Video/WAV giữ trong folder owner, không commit file lớn vào repo.

## Nội dung, giọng và giới hạn

Đã đọc skill transcribe: tuyến mặc định cần OpenAI API. Vòng này không được mở API mới; tiếp tục bộ local `scripts/local_voice_qc.py` đã duyệt ở lượt 89, không cài hoặc gọi dịch vụ mới. Faster-whisper small/CPU/int8/offline/vi, không initial prompt. Tuyến API của skill không được triển khai; không xin key để đổi tuyến trong lượt này.

ASR nhận hai phần:

> Khoan, mùi này làm anh nhớ đến bếp nhà anh.
> Hồi bé, mẹ gian gạo, anh đứng chờ.

“gian” là kết quả nhận dạng thay “rang” đã duyệt; không coi đây là kết luận phát âm sai và không mở bộ thử chữ này. ASR không nhận thêm lượt Đào trong transcript; **điều đó không chứng minh toàn lượt là giọng nam K20**. Root chưa có phương tiện nghe/so reference thực, không tự điền observed=Khoai.

Đã trình **WAV nguồn mới duy nhất** trực tiếp trong chat. Owner sau đó trả lời **“Đúng Khoai/K20 xuyên suốt, nhịp chấp nhận được”**. Ghi [approval](evidence/201/owner-approval.json) theo đúng hash WAV: **N02 mới APPROVED bởi owner** về người nói/giọng xuyên suốt và nhịp. Đây là nghe nghiệm thu phần sửa, không tuyển giọng lại. Root không tự nhận đã nghe. N02 cũ/A03 vẫn REWORK; approval N02 không là formal SIA report hoặc toàn bộ bảy lượt AUDIO_SELECTION PASS.

## Không ghép nhầm hoặc ép slot cũ

ASR ước tính lời từ 0 đến 7,34 giây, native/WAV dài 10,005 giây. Không tự coi toàn đuôi sau 7,34 giây là im lặng để cắt. Khoảng nghỉ kỹ thuật giữa hai phần khoảng 1,19 giây là số đo; nhịp toàn nguồn đã được owner chấp nhận ở trên.

N02 cũ có slot dự kiến khoảng 5,46 giây trong audit 183. Nguồn mới cần cập nhật timing; không ép vào slot cũ bằng tăng tốc hoặc cắt lời. **Không thay cả nguồn mở A03 mười giây bằng N02 mới mười giây**: A03 chứa N01–N04, còn nguồn mới chỉ chứa N02. Phải lập bảng nguồn từng lượt, giữ N01/N03/N04 và phần kết theo đúng script, rồi nghe kiểm bản nối hiện hành trước khi chọn tiếng final. Các range ASR chỉ giúp tìm chỗ nghe, không tự là điểm cắt đã duyệt. Bản nghe nối được ghi riêng tại [202](202_seven-turn-review-with-approved-n02.md).

Sáu lượt khác chưa có xác minh đủ theo SIA; việc duyệt N02 riêng không tự thành bảy lượt PASS. Chưa dispatch reviewer độc lập hoặc tích hợp nhận dạng speaker tự động; không báo agent đã nghe khi thực tế chỉ chạy script local.

## Tổng hợp

- Đã xác định: có native mới thật; bảo toàn file/hash, decode sạch, WAV không chỉnh và transcript N02.
- Đã chốt: owner duyệt toàn N02 mới đúng Khoai/K20 và nhịp; giữ C-v0.6/K20/D06, không dùng N02 cũ, không sinh thêm hoặc chi credit.
- Giả định: file mới tương ứng clip200 dựa trên tên, metadata, khung và nội dung; không có Flow checksum độc lập.
- Còn mở: source map bảy lượt, điểm cắt các lượt giữ lại và QC bản nối cuối.
- Tiếp: dựng bản nghe bảy lượt từ N02 mới nguyên vẹn và các lượt còn lại; bản nối có nhãn review, không tự nghiệm thu tiếng final. Không tái đưa N02 sai vào; không retry sinh vì quyền200 chỉ một lần.

Chi vòng này 0; trần 422/đã chi 329/còn 93 credit được phép sử dụng. Chưa Quality/master/phát hành. Trạng thái chưa có native tại 200 giữ như lịch sử, được cập nhật tại 201. Folder owner vẫn `C:/Users/PC/Downloads/du_an_nem_bui/200_n02_replacement/`.
