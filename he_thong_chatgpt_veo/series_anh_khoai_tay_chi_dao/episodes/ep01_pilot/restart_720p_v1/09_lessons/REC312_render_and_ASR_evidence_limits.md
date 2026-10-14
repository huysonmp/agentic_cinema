# REC312 — Ghi chú dựng và kiểm bằng chứng

- FFmpeg9.0.2 đang dùng không nhận `-filter_complex_script`; lần gọi đầu dừng trước dựng, không có output hoặc chi Flow. Đã đọc filter artifact bằng PowerShell và truyền nội dung vào `-filter_complex`, dựng được840khung. Giữ filter artifact riêng để truy vết; không cần cài công cụ mới hoặc sửa script.
- ASR unprompted trên rough nhận N01–N07 nhưng sai chính tả “rang”/“gắp”; cuối còn sinh câu subscribe không thuộc kịch bản. Không thêm câu ASR này vào caption/claim register hoặc gọi đó là giọng lạ thật. C08/C09 trong filter là silence; phải kiểm PCM thực của vùng đó và phân biệt nhận dạng máy với nghe thật.
- No-audio UI không chứng minh native không tiếng. Native C09 vẫn có AAC/PCM khác0, được giữ nguyên; bản xem im tiếng copy video bitstream và framemd5 toàn96khung khớp. Chỉ bỏ âm phát sinh của cảnh không thoại, không sửa tiếng K20/D06.
- Ngoại lệ Đào đặt cốc/đỡ bát do owner duyệt riêng REC312. Không đổi finding thành đúng prompt cũ; không chuyển approval đó sang range/nhịp/whole-film/final approval.
- Dựng đúng840khung chỉ chứng minh35s, không chứng minh ending8khung đủ hấp dẫn hoặc final30. Cần kiểm exact export và owner xem/nghe toàn bản; không cộng khoảng nghỉ ASR thành thời gian có thể cắt an toàn.
