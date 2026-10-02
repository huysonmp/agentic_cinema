# Gói nghe chọn giọng Khoai — Bắc, K2/K3/K4

**Kết quả owner mới nhất:** cả chín mẫu bị loại vì owner nghe là giọng nam miền Nam, không đạt yêu cầu nam miền Bắc. Trạng thái OWNER_REJECTED / ACCENT_FAIL; không còn ứng viên để chọn. [Quyết định, lỗi phép thử và hướng sửa — 144](144_owner-rejects-southern-accent-voice-auditions.md). Các mục chờ nghe bên dưới là lịch sử trước phản hồi.

Ngày 2026-10-02. Phạm vi thực hiện theo [142](142_northern-khoai-voice-auditions.md): chín mẫu, cùng TABLE08 và ba trích đoạn thoại, chỉ thay hướng diễn. Đây không phải cảnh hoàn chỉnh và không thay kịch bản 32.

## Đã xác định / quyết định / giới hạn

- Đã tạo và tải đủ chín video native; ròng 90 credit, Flow 740 → 650. Tổng thử 400/400, còn 0. Không dùng Quality 100 riêng, không mua thêm.
- Tất cả MP4: H.264, 720×1280, 8 giây; audio AAC, 48 kHz stereo. Giải mã toàn file bằng FFmpeg exit 0; trích PCM s16le WAV giữ sample rate/channels, không normalize, chỉnh cao độ, cắt hoặc ghép lời.
- Technical PASS chỉ chứng minh file đọc được và có audio, không chứng minh phát âm/giọng Bắc/độ trầm ấm hoặc diễn xuất đạt. Chưa nghe đánh giá thực, chưa ASR, chưa kiểm môi miệng/chuyển động liên tục; các gate này OPEN.
- K2/K3/K4 là hướng yêu cầu trong prompt, không phải chứng nhận âm sắc đã nghe. Veo chưa được chứng minh giữ một voice identity cố định qua lượt. Không chọn winner tự động.
- K1/K5 và giọng Đào chưa chạy. P6/P7 chưa đóng, chưa production PASS hoặc chuyển Quality.

## Manifest tải gốc

Các tên dưới nằm trong `C:/Users/PC/Downloads/`. Asset có thể mở trong dự án Flow `9276788e-9781-44fb-ba5b-083006667374`, đường dẫn `/edit/{asset}`. Đã đối chiếu prompt trong từng màn hình asset trước tải, không gán mã chỉ dựa vào tiêu đề.

| Mẫu | Asset | Tên tải gốc | Byte |
|---|---|---|---:|
| K2-01 | 7ef0bf50-a186-49e4-ac44-2d3973663e5a | Potato_man_speaks_to_peach_20261002162425.mp4 | 2341494 |
| K2-02 | 5c80cb58-5f6c-40aa-8601-765755c5c536 | Potato_man_speaks_to_peach_20261002162443.mp4 | 2274461 |
| K2-03 | a6e1b1e7-7e0b-4388-b799-390c9c3e8988 | Potato_man_speaks_to_peach_20261002162500.mp4 | 2331151 |
| K3-01 | fd31923b-fd1c-46ae-bf97-9abf76ef4d66 | Potato_man_speaking_to_peach_20261002162043.mp4 | 1901153 |
| K3-02 | ffc6b379-5a95-4205-8917-1bb02cb3ab35 | Potato_man_speaking_to_peach_20261002162346.mp4 | 2477207 |
| K3-03 | 7f3a4286-4273-4305-8bbc-448667329a52 | Potato_man_speaking_to_peach_20261002162406.mp4 | 2338266 |
| K4-01 | 6ba2d5a3-e32e-42af-b979-8254febc751c | Potato_man_speaking_to_peach_20261002161911.mp4 | 2326491 |
| K4-02 | 6d119874-f7d0-4768-8bf7-5e2fd2959ee7 | Potato_man_speaking_to_peach_20261002161942.mp4 | 1944530 |
| K4-03 | 0cd4c60b-0aa4-468d-a14b-66d2d9d5838c | Potato_man_speaking_to_peach_20261002162011.mp4 | 2321022 |

MP4 SHA-256 theo thứ tự manifest:

```text
K2-01 5A2308FE73C83B6ACAFCED600DC0BA1D6020680CC1C3EF6967808BDF77F888B9
K2-02 836B3B8F13A9B41970BC066C37B389E0848DE1FA24CEF54CC16A463306B7061A
K2-03 3FC2CDB153C731A0EFD3B02B1AD7E582513DFCCBDF7F9B409B979D077116EB2E
K3-01 EA7D11B7ECD99BABFB463DD0081331482AFE3D0FA5442370FAADEB11A44EC745
K3-02 1143B5E400360028542E47A9220323B57401559734FCDA2ADF501EB798BA1129
K3-03 B53CEA9D2A67D5BB605937A10A50C1A64539A3B453EBC923AAF881C24C2D3966
K4-01 612700AFDE92AA7984243E37D5A26E38840E715B9952941A8F4D96FE99FA1F4C
K4-02 7B8B8C5E4C044FBE0CAA5892FAAAFECC27913987834427A208F88E8B41569320
K4-03 3CF1DC9444DCB106B927E84C4C486D48354AEEF3226FAA128FB4C2240A5A89DA
```

## Nơi lưu và cách duyệt

Bản làm việc: `D:/Workspace/agentic_cinema/artifacts/voice142-r1`. Bản owner: `C:/Users/PC/Downloads/du_an_nem_bui/142_giong_Khoai_Bac`. Mỗi mã có `.mp4` và `.wav`; media không commit Git. Ảnh proof UI và settings giữ ở thư mục artifact.

### K2 — ấm, có nụ cười kín

![K2-01](C:/Users/PC/Downloads/du_an_nem_bui/142_giong_Khoai_Bac/K2-01.wav)

![K2-02](C:/Users/PC/Downloads/du_an_nem_bui/142_giong_Khoai_Bac/K2-02.wav)

![K2-03](C:/Users/PC/Downloads/du_an_nem_bui/142_giong_Khoai_Bac/K2-03.wav)

### K3 — ký ức trở về, ấm dần

![K3-01](C:/Users/PC/Downloads/du_an_nem_bui/142_giong_Khoai_Bac/K3-01.wav)

![K3-02](C:/Users/PC/Downloads/du_an_nem_bui/142_giong_Khoai_Bac/K3-02.wav)

![K3-03](C:/Users/PC/Downloads/du_an_nem_bui/142_giong_Khoai_Bac/K3-03.wav)

### K4 — điềm tĩnh, hài tỉnh bơ

![K4-01](C:/Users/PC/Downloads/du_an_nem_bui/142_giong_Khoai_Bac/K4-01.wav)

![K4-02](C:/Users/PC/Downloads/du_an_nem_bui/142_giong_Khoai_Bac/K4-02.wav)

![K4-03](C:/Users/PC/Downloads/du_an_nem_bui/142_giong_Khoai_Bac/K4-03.wav)

Owner cần trả lời: mã mẫu thích nhất (hoặc chưa mẫu nào đạt); độ Bắc/trầm/ấm có tự nhiên không; chỗ nào đọc đều, quá diễn, sai hoặc thiếu lời. Giả định làm việc: tiếp tục giữ hướng Khoai kể thân mật, ký ức có nét cười kín đã duyệt ở 93, chưa khóa giọng.

Bước tiếp theo: ghi quyết định nghe của owner; kiểm sâu lời, diễn và tính nhất quán trên mẫu được chọn. Nếu cần generation thêm phải có ngân sách mới, không mượn khoản Quality. Đánh giá khả năng giữ giọng trước áp dụng vào cảnh sản xuất; không coi chọn một audition là bảo đảm cả tập đồng giọng.
