# MASTER01 v3/v4 — Kiểm khung thực và dừng lặp

Ngày07/10/2026. Reviewer root/maker tích hợp, **không độc lập**. Capability: xem toàn native ảnh tĩnh, tính SHA256 và đọc size/verifyJPEG bằngPillow. Không video/audio/motion.

| Bản | Target/hash | Quan sát | Kết quả |
| --- | --- | --- | --- |
| v3 |02_refs/MASTER01_v3_NATIVE.jpg /49f672ca0fd63ab0539b9dde90f7a181aa5acc1b0d88a632c91ecb40b04e1aa4|Rau vẫn vượt mép trái, cốc sát phải; bố cục gần v2; mặt và F0 nhìn thấy|REWORK_FRAMING |
| v4 |02_refs/MASTER01_v4_NATIVE.jpg /f5f5b9e767dab5007d6de2b1cca8671f07e25c5adeaba56cea01ede8a5da65b0|Camera composition mới vẫn gần khung cũ; không có margin hai bên như request; hai mặt/F0/món vẫn thấy|REWORK_FRAMING / STOP |

Cả hai768×1376, chưa đúng tuyệt đối9:16. Không tạo derivative resize/crop, không đổi watermark. Hai mặt/miệng khép, tay nghỉ, bát trống, chopsticks bàn; nem không thấy khói. Đây là hồi quy tĩnh trong scope nhìn thấy, không chứng nhận mọi claim món hoặc footage đã đạt.

Nguyên nhân đã biết: output không thực hiện điều chỉnh framing yêu cầu. Promptv3/v4 đã phân biệt không moveprops; v4 đúngsourceupload/picker/chipv2, fullinputquote0. Không thấy bằng chứng dùng nhầm nguồn hoặc đổi model. Giả thuyết source image vẫn neo framing mạnh: chưa chứng minh cơ chế; không quy lỗi cho account/credit hoặc gọi model không làm được.

Khắc phục đề xuất chưa chạy: tách nguồn character identity và food material khỏi whole-scene v2; thiết kế scene mới có serving margin bằng nguồn riêng, kiểm mặt/geography/F0/food lại. Hệ quả là drift cần được phát hiện, không coi source split là chắc chắn chữa. Tooloutpaint khác chỉ là lựa chọn cần owner, không tự đổi.

Run reviewer độc lập chỉ gửi interimfeedback trước khi lỗi usage, không có report. Registry ghi thất bại; không kế thừa report238 làm reviewv4. Giữ humancheckpoint và productionHOLD. Hai lần framingfailure liên tiếp đủ dừng theo238; đây không phải bằng chứng một video C02 đã hỏng.
