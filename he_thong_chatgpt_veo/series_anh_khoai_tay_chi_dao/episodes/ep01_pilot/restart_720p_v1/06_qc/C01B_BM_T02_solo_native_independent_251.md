# REC251 — Review hình native độc lập BM solo T02

Kết luận: **HOLD / BLOCK BM→BR**. Native có chữ burn-in trái prompt; chưa chọn range BM và chưa có bằng chứng range sạch chữ chứa lời trọn. Không tự retry.
Nguồn: `05_native/EP01_720_C01B_BM_T02_SOLO_NATIVE.mp4`; SHA256 đã kiểm từ file khớp `780ab0b3fb29454f732d2f56ed30526a77f81ed98bbaf04ca04cdb5cf094b231`.
Đã đọc full `native_evidence.json`, prompt250 và report/lesson REC249; trực tiếp xem hai board 6fps (24 mẫu) và PNG gốc F22/F23/F57/F58. Không xem/nghe AV liên tục hoặc kiểm bằng mắt cả 96 frame.
Quy ước: F bắt đầu từ 0; file PNG là F+1. Evidence ở `C:/Users/PC/Downloads/du_an_nem_bui/251_BM_SOLO/BM_T02_native_qc/`.

## Blocker và biên chữ

- PNG F22 (`00023.png`), 0,916667s: chưa có chữ, miệng đã mở. F23 (`00024.png`), 0,958333s: chữ “Khoan” trắng viền đen xuất hiện trên ngực, phía trên bát.
- F57 (`00058.png`), 2,375s: còn chữ. F58 (`00059.png`), 2,416667s: hết chữ. Hai cặp frame liền nhau khóa biên vào/ra tại cửa sổ kiểm; các mẫu board F24–F56 đều có chữ, chưa kiểm từng frame ở giữa.
- Chữ nằm trong PNG trích từ native, không phải nhãn board; flag caption stream=0 không phủ định burn-in. Prompt đã yêu cầu spoken audio only và không visual transcription/caption/lettering.
- Board F24/F28/F32 cho thấy miệng mở/đổi hình trong đoạn có chữ; F36 đã khép và đuôi F60–F92 không chữ nhưng môi khép trong các mẫu.
- Cắt toàn đoạn chữ sẽ bỏ phần chuỗi khẩu hình mở. Đoạn sạch trước F23 chỉ có một phần bắt đầu mở miệng; đuôi sạch không chứng minh lời trọn. Không có cơ sở chọn range sạch đủ “Khoan” hoặc ghép tiếng lên môi khép.

## Phần hình quan sát được và giới hạn

- Trong mẫu: giữ chủ thể solo Khoai, không thấy Đào; toàn mặt/miệng rõ, hướng sang phải, hai tay nghỉ cạnh bát. Bát, đũa, chén chấm và mép món còn thấy; không thấy ăn/uống/reach/hơi nóng hoặc cut/pan/zoom rõ trong mẫu.
- Solo loại phần gaze/hover Đào nhìn thấy khỏi BM, không chứng minh Đào/contact ngoài khung đã giữ đúng. Continuity A→BM→BR→C02 và góc đầu/gaze qua cut chưa được kiểm.
- Evidence kỹ thuật ghi 720×1280, 24fps, 96 frame/video4s, audio AAC stereo48kHz/4,01s, full decode thành công. Đây không phải chứng nhận motion/audio/lip-sync.
- Không thực hiện nghe tiếng PCM/native: đúng từ, lời thừa, giọng K20, sắc thái ấm và đồng bộ tiếng–môi vẫn CHƯA KIỂM; không kế thừa approval take cũ.

REC249 đã có burn-in cùng loại và thêm lỗi gaze/hover Đào. T02 đổi solo và diễn đạt lời chỉ là audio nhưng vẫn sinh chữ: thay coverage không giải quyết blocker caption trong output này. Việc Đào khuất hình không chứng minh lỗi gaze/contact đã được sửa.
Chỉ kết luận output không thực hiện đầy đủ điều kiện không chữ; chưa xác định cơ chế provider hoặc một cụm prompt/voice/dấu câu là nguyên nhân duy nhất. Hai lần lỗi không chứng minh mọi lượt/model đều lỗi, cũng không tạo authority thử tiếp.
Giữ nguyên nguồn; BR HOLD dù tiếng sau này có đạt. Không crop chữ, freeze, che bằng món, ghép voice lên đuôi khép hoặc dùng lượt BR làm retry; cần owner chốt hướng tiếp sau root đọc đầy đủ report.
