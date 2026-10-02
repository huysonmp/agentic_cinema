# Thử tích hợp cặp giọng K20 / D06

Ngày: 2026-10-02. Owner cho phép: “thử đi xem nào”.

## Phạm vi và đầu vào

- Khoai: Orus tuỳ chỉnh K20, `fb1188da-e6c8-4156-9bba-0576c01a8da6`.
- Đào: Aoede tuỳ chỉnh D06, `0ce1551e-e74b-481c-bb9e-d31e04f8b352`.
- Ảnh: `T2-CODEX-OPEN_v0.7.png`, chọn trong tài nguyên Flow.
- Đoạn thoại lấy từ kịch bản C-v0.5 đã duyệt: Đào “Chờ em quay lưng nữa à?” → Khoai “Anh gắp cho em mà.” → Đào “Thế em quay lại đúng lúc rồi.”
- Để cô lập giọng, giữ máy cố định và tay trên bàn, không thực hiện gắp/ăn. Đây là probe kỹ thuật, không sửa blocking kịch bản chính.

## Route thử thực tế

Flow đang chọn Omni 1.1 Flash, Thành phần, 9:16, 360p, 8 giây, x3. UI báo 18 credit cho cả lượt. Đã thông báo route cho owner trong commentary; không gọi đây là Veo Lite và không coi là duyệt chuyển pipeline production. Ngân sách thử 200 credit gần nhất còn 170 trước lượt này, dự kiến còn 152 nếu trừ đúng 18; chờ kiểm chứng actual.

Trước submit đã đối chiếu detail ID từng preset rồi thêm vào compose. Âm thanh đơn lẻ bị cảnh báo cần thành phần khác; thêm ảnh làm ba thành phần hoạt động. Click chip thành phần sẽ gỡ chip, không mở detail; đã gỡ/khôi phục và kiểm lại đủ Orus + ảnh + Aoede trước gửi.

## Prompt actual

```text
Create an 8-second vertical 9:16 voice-pair integration test using the supplied image T2-CODEX-OPEN_v0.7.png. Preserve the adult potato man Khoai on the left and adult peach woman Dao on the right, their exact faces, clothes and small clean street-side eatery. Use the attached custom Orus voice for Khoai (warm grounded adult Northern Vietnamese male) and attached custom Aoede voice for Dao (breezy friendly adult Northern Vietnamese female). Do not invent substitute voices. One locked medium two-shot; both seated, hands resting on the table; no picking up food, no eating or feeding. The Nem Bui dish is served cool, matching the image. Focus only on facial performance and dialogue. Speak only these exact Vietnamese lines in order, with short natural pauses and no overlap: Dao, lightly teasing: "Chờ em quay lưng nữa à?" Khoai, warm, quietly embarrassed but trying to sound matter-of-fact: "Anh gắp cho em mà." Dao, smiling with a quick playful reply: "Thế em quay lại đúng lúc rồi." Only the assigned character moves their mouth during their own line; the other listens. Keep each assigned voice identity throughout. Clear close conversational audio, very quiet street ambience, no music, no narration, no subtitles, no written speaker names. This is a dialogue timing and voice identity probe, not the final episode.
```

## Gate và trạng thái

Đã tạo và tải đủ ba bản, không resubmit. Số dư live 652 so với mốc 670: ròng 18 credit, khoản thử mới còn 152/200; Quality 100 riêng chưa dùng.

| Bản | Asset ID | Kiểm hình từ tám khung, một khung mỗi giây |
|---|---|---|
| V01 | 3da9ceda-0ee5-4997-9ea8-d397f52928ef | Giữ hai nhân vật rau quả; món đổi sang các phần tròn có rau bên trên, không giữ đúng nem tham chiếu |
| V02 | 777da017-35c4-4de4-8013-c7b6c2a7c1b5 | Đào thành người, món/bố cục thay đổi; CHARACTER FAIL |
| V03 | fdd19c71-bbf1-45bf-8249-0d0f43f44fac | Đào thành người, bối cảnh thay đổi; CHARACTER/SETTING FAIL |

URL mỗi bản: `https://flow.google.com/u/1/project/9276788e-9781-44fb-ba5b-083006667374/edit/{asset-id}`.

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/153_voice_pair`, gồm V01/V02/V03.mp4, ba contact sheets, preflight.png và results-flow.png. Source download: V01 `Creating_voice_integration_test_20261002211443.mp4` (828439 bytes), V02 lúc 211730 (821581 bytes), V03 lúc 211815 (751136 bytes). Tải lặp V01 lúc 211615 giữ nguyên ngoài folder.

Cả ba 360×640, H.264, 24 fps, 8 giây, AAC 48 kHz stereo; full decode FFmpeg exit 0. Chạy script local_voice_qc.py offline bằng môi trường/model đã cài; báo cáo, SHA256, WAV và ASR ở `artifacts/voice-qc/153-v01` tới `153-v03`. Cả ba ASR trả: “Chờ em quay lưng nữa à? / Anh gấp cho em mà. / Thế em quay lại đúng lúc rồi.” Khác biệt gấp/gắp có thể từ phát âm hoặc ASR, cần nghe; transcript không xác nhận accent, voice identity, người nói hoặc lip-sync. Root chưa nghe xác nhận, không nói agent đã nghe.

## Bài học và bước tiếp

- Hai lần waitForEvent(download) timeout nhưng file thực đã có trong Downloads; cả tab cũ và mới. Không gọi tải thất bại từ event; kiểm file/size/decode trước retry. V02/V03 click UI và đối soát file thành công.
- Nhật ký output có đủ ba input, nhưng model vẫn lệch hình. Gắn preset không chứng minh giọng giữ đúng.
- “Adult peach woman” có thể mơ hồ giữa quả đào và người phụ nữ; đây là giả thuyết, chưa nguyên nhân đã xác nhận. Cũng cần kiểm khả năng giữ hình của route Thành phần. Không kết luận chắc do từ khóa/preset.
- V01 chỉ dùng nghe cặp giọng/nhịp, không chọn production. Owner nghe identity, accent và từ “gắp”. Sau đó thử khóa hình/món, giữ cặp giọng và route, thay một nhóm chỉ dẫn nhận diện 3D anthropomorphic peach/potato; giữ nguồn món actual. Chưa chạy lượt đó.
- Chưa winner, chưa production PASS, chưa đổi pipeline production hoặc Quality/release. P6/P7 thử tích hợp vẫn mở. Giả định: cặp preset được duyệt là baseline; hiệu lực trong video còn chờ kiểm.
