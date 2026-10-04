# 175 — Thử cụm ký ức với K20 và D06

Ngày: 2026-10-04. Owner trả lời “ok” sau đề xuất chạy ba mẫu cụm B, tối đa 21 credit từ 25 credit còn lại tại [174](174_owner-provisional-acceptance-k20-controls.md). Đây là duyệt thực thi phép thử, không phải nghiệm thu đầu ra.

## Phạm vi và đầu vào

- Kịch bản 32 giữ nguyên. Chỉ thử bốn câu: Đào “Nem thì đây. Chảo ở đâu?”; Khoai “Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ.”; Đào “Chờ ăn?”; Khoai “Chờ mẹ quay lưng.”
- K20 Orus tùy chỉnh: `fb1188da-e6c8-4156-9bba-0576c01a8da6`; D06 Aoede tùy chỉnh: `0ce1551e-e74b-481c-bb9e-d31e04f8b352`.
- Ảnh OPEN7 chỉ dùng đối chứng: `43057def-574c-4ca7-916c-d55083f9b670`. Không mặc định nghiệm thu hình hoặc dùng thay bộ cảnh sản xuất.
- Omni 1.1 Flash / Thành phần / 360p / 9:16 / 10 giây / x3. Không phải Veo Lite hoặc Quality.
- Kiểm tích hợp lời thật và hai người nói; không phải phép thử nhân quả đơn biến. Nhịp diễn được chuyển sang bốn câu thực, giữ hướng âm sắc đã chọn, không sửa preset thư viện.

## Kiểm trước khi tạo

Phiên trình duyệt cũ không còn; mở lại đúng dự án Flow trong trình duyệt tích hợp. Số dư tài khoản trực tiếp là 317 credit, khác snapshot 275 tại 173; chưa rõ nguyên nhân chênh lệch và không tự coi là cấp thêm quyền chi. Quyền chi dự án trước lượt vẫn là 25 credit, trần phép thử này 21.

Đã đọc ID và đặc điểm D06 trong thư viện; chọn K20 theo đặc điểm phân biệt với K12, sau đó đối chiếu token trực tiếp trong lời. Token K20 và D06 đều có `data-reference-type=audio` và đúng ID. Ô nhập có ba thành phần: một ảnh đúng OPEN7 và hai giọng, không biểu tượng lỗi. Chỉ đọc chip, không bấm chip để xem chi tiết vì có thể làm mất nguồn.

Cài đặt trực tiếp báo Omni 1.1 Flash, Thành phần, dọc 9:16, 360p, 10 giây, x3; báo giá 21 credit. Prompt nguyên văn tại `evidence/175/prompt-B.txt`; token và cấu hình tại `evidence/175/preflight.json`. Cần xem screenshot cuối rồi mới bấm tạo, không thay đầu vào sau lần kiểm đó.

## Trạng thái

THREE_NATIVE_DECODED / OWNER_PAIR_LISTENING_PENDING — đã xem screenshot cấu hình và screenshot đầu vào cuối: ảnh + hai giọng, đúng token, không biểu tượng lỗi. Sau kiểm không thay đầu vào; bấm tạo đúng một lần. Nhận đủ ba kết quả, tải đủ file gốc qua menu 360p trong tab tải riêng. Không gửi lại, không nâng Quality hoặc tạo thêm.

## Kết quả thực và đường dẫn bàn giao

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/175_k20_d06_dialogue/`. B01/B02/B03 đặt theo ba ô mới từ trái sang phải; không trùng các mẫu B của bộ 170. Manifest riêng tại `evidence/175/results.json`.

| Mẫu | Media ID | Native filename | Bytes |
| --- | --- | --- | ---: |
| B01 | bc58ddf3-d3d2-49c4-9c35-08de5ec304f4 | Characters_performing_dialogue_d…_20261004210337.mp4 | 982924 |
| B02 | d2c0b8fe-2cb1-42ba-abb2-f039a8aee1c9 | Characters_performing_dialogue_d…_20261004210404.mp4 | 966995 |
| B03 | 98635e9b-a597-439c-a889-6f33e0c58ce3 | Characters_performing_dialogue_d…_20261004210427.mp4 | 854515 |

Ba MP4 full decode sạch bằng FFmpeg 9.0.2: H264, 360×640, 24 fps, khoảng 10,01 giây; AAC 48 kHz stereo. WAV `B01_VOICE_PENDING.wav` tới B03 giữ 48 kHz stereo PCM16bit, mỗi file 1921038 bytes; không chỉnh gain, tốc độ hoặc âm sắc. Hash PCM MP4/WAV tương ứng bằng nhau ở cả ba mẫu. File QC ASR 16 kHz mono chỉ dành cho kiểm lời, không dùng làm bản nghe.

QC cục bộ chạy `scripts/local_voice_qc.py`, faster-whisper small / CPU / int8 / offline / tiếng Việt, không initial prompt, không API. Báo cáo tại `artifacts/voice-qc/175-B01` tới B03 và bản sao `qc/` trong folder owner.

| Mẫu | Những chỗ ASR cần nghe lại | Mean / max dBFS |
| --- | --- | --- |
| B01 | “Nèm”, “chào ở đâu”, “mẹ gian gạo”; các cụm lời còn lại có trong transcript | -16,6 / -0,5 |
| B02 | “Nèm”, “chào ở đâu”, “mẹ dăng gạo”; các cụm lời còn lại có trong transcript | -16,9 / -0,1 |
| B03 | “Nèm”, “chào ở đâu”, “Mẹ Giang Gạo”; các cụm lời còn lại có trong transcript | -17,0 / -0,2 |

Không dùng transcript để chứng nhận phát âm sai, giọng vùng miền hoặc đúng người nói. ASR gộp “Chờ ăn?” và “Chờ mẹ quay lưng” thành một đoạn ở cả ba, không chứng minh hai câu do một người nói. Cần owner nghe thực. Peak không thay kiểm nghe tiếng méo; chưa chấm chất giọng, diễn xuất hoặc độ hấp dẫn bằng tai.

## Kiểm hình giới hạn — không nghiệm thu cảnh

Đã xem contact sheet mỗi mẫu lấy một khung/giây, không phải kiểm toàn bộ chuyển động hoặc đồng bộ môi. B01 gần bố cục và trang phục OPEN7 hơn; B02 đổi đĩa và phần món; B03 làm mất trang phục Khoai và đổi bố cục bàn. Vì vậy B02/B03 **VISUAL_REWORK**, không dùng làm hình bàn giao. B01 chỉ ưu tiên xem trước vì hình ít lệch hơn, không là winner giọng hoặc visual PASS. Các khung quanh giữa đoạn có Đào mở miệng khi ASR còn ghi lời của Khoai; cần kiểm audio–hình đồng thời, chưa kết luận từ khung thưa/ASR ai đang nói.

Mục đích lượt này vẫn là nghe cặp giọng và lời thật. Không sửa hình lẻ tẻ trong lúc nghe duyệt, không dùng ảnh đối chứng để mặc định lấp phần cảnh chưa hoàn tất của EP01.

## Đối soát ngân sách và quyết định tiếp

Account trực tiếp 317 → 296, giảm 21 credit đúng báo giá và trần đã duyệt. Theo sổ quyền chi dự án: 109 + 21 = **130/134**, còn **4 credit**. Chênh lệch +42 so snapshot tài khoản cuối 173 chưa rõ nguyên nhân, không ghi thành cấp thêm ngân sách hoặc hoàn phí đã xác nhận. Không mở khoản thêm 90 credit chưa được duyệt.

Tab tải tạm đã đóng; tab dự án để sẵn B01 cho owner bấm Phát. Đã lưu screenshot đầu vào, cài đặt, submit, ba kết quả, lịch sử B01 và số dư sau tạo. Browser phiên này mở lại thành công; menu tải bản gốc ở tab riêng tải được cả ba file thực, không chỉ có thông báo tải.

Owner chỉ cần đánh giá bộ 175: (1) Khoai và Đào có giữ được chất K20/D06 đã chọn, đúng vai và nhịp đối đáp không; (2) nghe rõ các chữ “nem”, “chảo”, “rang” chưa. Không yêu cầu tuyển lại giọng hoặc chọn winner nếu cả ba đều tạm đạt. Nếu có mẫu đạt, mới chọn nguồn tích hợp và rà coverage; nếu chưa đạt, ghi lỗi theo mẫu rồi trình hướng xử lý, không tự chạy thêm với 4 credit còn lại.

## Tổng kết vòng

- Đã xác định: đầu vào UI đúng ảnh + hai token; nhận, tải và giải mã đủ ba MP4; WAV khớp PCM gốc; chi thực 21 credit.
- Đã chốt: thực hiện bộ thử cụm B x3 theo duyệt owner, giữ K20/D06 và lời kịch bản 32; chưa đổi Quality hoặc mở ngân sách mới.
- Giả định làm việc: hướng diễn chuyển sang lời thật vẫn phù hợp hai preset, nhưng chất giọng và nhịp thực phải nghe kiểm.
- Còn mở: nghe cặp giọng và phát âm, đúng người nói, đồng bộ môi, bộ cảnh sản xuất, cơ chế lỗi 170 và bản cuối.
- Tiếp: owner nghe ba mẫu; ghi quyết định theo phạm vi, sau đó chọn bước tích hợp hoặc xử lý lỗi. Không tạo thêm trong lượt này.

## Tiêu chí bàn giao

Tải đủ ba file gốc, kiểm giải mã và nội dung lời bằng công cụ cục bộ. Giữ bản nghe nguyên tốc độ, không thay âm sắc hoặc tăng giảm gain. ASR chỉ hỗ trợ kiểm lời, không xác nhận accent, danh tính giọng, cảm xúc hoặc đúng người nói. Owner nghe so với K20/D06 đã chọn; không ghi agent đã nghe độc lập nếu chỉ chạy kiểm kỹ thuật. Nếu phát hiện lỗi, ghi rõ từng mẫu, không tự tiêu thêm hoặc nâng Quality.
