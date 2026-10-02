# Thử riêng giọng nam miền Bắc — R1

**Owner review mới nhất:** cả ba bị loại vì tiếp tục sai vùng giọng. OWNER_REJECTED / ACCENT_FAIL; các trạng thái chờ nghe bên dưới là lịch sử. [RCA chuỗi nguồn/điều khiển/QC — 146](146_voice-accent-root-cause-audit.md). Không tiếp tục chọn mẫu từ bộ này.

Ngày 2026-10-02. Owner cấp thêm 200 credit và yêu cầu thử tiếp. Đây là trần thử bổ sung, không mua credit, không thay ngân sách Quality riêng. Số dư Flow trước thử đọc actual 650. Bộ 142/143 vẫn bị loại theo 144.

## Thiết kế và giả định

Một request Lite x3, UI 30 credit; khung đầu T-NB-03_v0.8.jpg chọn lại từ picker, không khung cuối; Frames, 9:16, 720p, 8 giây. Không thử nhiều sắc thái cùng lúc. Chỉ dùng câu Khoai trong kịch bản đã duyệt; một câu để giảm áp lực ba trích đoạn trong 8 giây. Giọng Hà Nội là giả định thử cụ thể hóa nam miền Bắc, chưa khóa canon. Prompt tiếng Việt là một can thiệp mới; đồng thời rút lời và giản lược mô tả, nên không kết luận riêng ngôn ngữ prompt gây cải thiện nếu đạt.

## Prompt actual

```text
Máy quay cố định trong tám giây, giữ bố cục và bàn ăn của ảnh đầu. Anh Khoai, nhân vật khoai tây nam trưởng thành ở bên trái, nói một câu với chị Đào ở bên phải. Đào lắng nghe, hai người để tay trên bàn. Âm thanh chính là giọng nam trưởng thành nói tiếng Việt bằng giọng Hà Nội tự nhiên, miền Bắc Việt Nam. Phát âm và ngữ điệu hội thoại của người Hà Nội, âm sắc nam trung trầm, nói bình thản và thân mật. Anh Khoai nói đúng một lần, đầy đủ câu: "Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ." Chỉ miệng Khoai chuyển động theo lời nói, tiếng phố nền nhỏ. Đây là mẫu kiểm giọng vùng miền, ưu tiên nghe rõ giọng Hà Nội và từng tiếng, không cần diễn cảm phức tạp.
```

## Gate và ngân sách

Trước submit: Lite/x3/30 credit và ảnh đầu đã kiểm UI. Cần kiểm fallback audio, lưu native và WAV không xử lý. Gate file độc lập gate nghe: root chưa có khả năng nghe xác nhận accent trong thao tác này, owner nghe quyết định. Không tự gọi mẫu mới là giọng Bắc đạt dựa vào prompt. Dừng sau ba mẫu để trình nghe trước khi phát triển chất diễn. Không nhất thiết tiêu hết 200; giữ phần còn lại cho vòng có thông tin mới.

Trạng thái đăng ký: PREFLIGHT / NOT_SUBMITTED. Kết quả actual bổ sung sau chạy.

## Nhật ký actual

Đã chọn lại T-NB-03_v0.8.jpg (picker hiển thị tên/preview), START có ảnh, END trống. UI hiển thị Veo 3.1 Lite, Frames, 9:16, 720p, 8 giây, x3, giá 30. Đã đọc lại prompt nguyên văn sau nhập; tác nhân OFF, return-without-audio OFF, hover-audio OFF. Gửi đúng một request; ba ô mới “Khoai speaks to Dao at table…” đang tiến hành, chưa có kết quả nghe.

Ảnh proof `D:/Workspace/agentic_cinema/artifacts/voice145-r1/submitted.png`. Khoản 30 là giá submit, phí ròng và số dư sau chạy sẽ đối soát; chưa gọi 170 còn lại là đã xác nhận actual trước đối soát. Không request thứ hai hoặc Quality.

## Kết quả actual / gói nghe

Đủ ba video, tải 720p gốc thành công. Số dư UI sau thử 620, so với 650 trước: ròng 30, ngân sách bổ sung 200 đã dùng 30 còn 170. Tổng các khoản thử liên tục 430/600. Quality riêng chưa dùng. Không retry hoặc video câm.

Tất cả: 8 giây, H.264 720×1280, AAC 48 kHz stereo; full decode FFmpeg exit 0. WAV PCM s16le được trích từ audio native, không chỉnh âm sắc/âm lượng/cắt lời. Trạng thái hiện hành GENERATED / DOWNLOADED / TECHNICAL_DECODE_PASS / ACCENT_REVIEW_PENDING. Root chưa nghe xác nhận accent, đúng lời hoặc lip sync; không chọn winner hoặc production PASS.

| Mẫu | Asset Flow | Tên tải gốc trong Downloads | Byte |
|---|---|---|---:|
| B-R1-01 | fd98f82a-4463-49a3-9f35-16ef5b7d03fb | Khoai_speaks_to_Dao_at_20261002164647.mp4 | 2110913 |
| B-R1-02 | d4cf0ff7-d349-4f74-adbc-d32401a41e34 | Khoai_speaks_to_Dao_at_20261002164706.mp4 | 1969540 |
| B-R1-03 | 055fc5a7-e415-4c0e-a261-21900c83a894 | Khoai_speaks_to_Dao_at_20261002164724.mp4 | 1935055 |

Đã kiểm prompt tiếng Việt trong từng asset. Helper tải cũ tìm chuỗi tiếng Anh nên trường prompt của helper rỗng; không dùng trường rỗng làm bằng chứng prompt. Root đã đọc actual UI tiếng Việt riêng trước/giữa tải.

MP4 SHA-256:

```text
B-R1-01 38767E80AE5383CB82C10D0D194974C0DCFB7F836F360638BFA255EFE6E759E8
B-R1-02 E74D2B9D9A71A419EB348315CDBB981941CBD719FCC6E5497D0D5FEC15676212
B-R1-03 3A07332CF2F256FDA7447877492C88D438A5355E7CEBADB963761FB5EE299B5E
```

Bản làm việc tại `D:/Workspace/agentic_cinema/artifacts/voice145-r1`; bản owner tại `C:/Users/PC/Downloads/du_an_nem_bui/145_giong_Bac_R1`. Mỗi mã có MP4/WAV. Proof results.png hiển thị asset mới trong editor.

![B-R1-01](C:/Users/PC/Downloads/du_an_nem_bui/145_giong_Bac_R1/B-R1-01.wav)

![B-R1-02](C:/Users/PC/Downloads/du_an_nem_bui/145_giong_Bac_R1/B-R1-02.wav)

![B-R1-03](C:/Users/PC/Downloads/du_an_nem_bui/145_giong_Bac_R1/B-R1-03.wav)

Owner chỉ cần xác nhận mẫu nào đúng giọng nam Bắc (hoặc cả ba vẫn sai) trước. Chưa cần chọn diễn xuất hay nhất. Bước sau dựa trên kết quả nghe; không chạy sắc thái hoặc tiêu tiếp 170 một cách mù. Approval 200 đã có, không hỏi lại ngân sách trong trần.

Ghi chú vận hành: ô mới xuất hiện cuối accessibility tree nhưng lưới screenshot còn cũ, click title không mở được. Reload một lần sau khi hết progress đưa ba ô mới lên đầu, mở và tải được. Đây là workaround hiển thị, không lỗi âm thanh hoặc lý do tái sinh video.
