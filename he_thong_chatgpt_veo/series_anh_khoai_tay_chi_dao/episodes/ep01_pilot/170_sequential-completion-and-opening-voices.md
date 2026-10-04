# 170 — Quyền xử lý tuần tự và hoàn thiện thoại đầu

**Cập nhật sau phản hồi owner ngày2026-10-04:** giọng nam khác mẫu đã chọn; A03/B01 trình nghe có trạng thái `OWNER_REPORTED_IDENTITY_MISMATCH`, chưa dùng master. [RCA171](171_k20-voice-identity-root-cause-audit.md) loại trừ extraction, kiểm K20 live nhưng chưa chứng minh exact historical server binding; không coi chọn theo performance là kết luận nguồn chắc chắn. B02/B03 chưa verdict nghe riêng. Giữ phần dưới làm nhật ký thời điểm thực hiện; không ghi audio approval từ lệnh tiếp tục chung.

Ngày 2026-10-03. Chủ dự án giao xử lý tuần tự đến video cuối để duyệt; nếu cần xác nhận phải trình ngay. Đây là quyền tiếp tục sản xuất trong phạm vi đã chốt, không tự đăng TikTok, mở ngân sách mới, đổi kịch bản hoặc hạ tiêu chuẩn hình/giọng.

## Phạm vi và thứ tự

1. Hoàn thiện audio sáu câu đầu bằng K20 Orus và D06 Aoede, giữ lời tại bản 32. Audio ba câu cuối R01 được phép tái dùng theo 168.
2. Đo nhịp audio, chọn coverage có nguồn/timecode; xử lý cảnh quay đi, nâng-khựng, phản ứng, chuyển-nhận và kết còn thiếu.
3. Ráp bản 30 giây, kiểm âm lượng/đồng bộ/chuyển cảnh, đặt F01/F02 và nhãn AI, xuất bản cuối để chủ dự án duyệt. Không biến ảnh tạm trong animatic 166 thành video đạt.
4. Mỗi nhóm công việc ghi input, prompt, ID, kết quả kiểm, chi thực tế và quyết định dùng/loại. Commit/push theo yêu cầu hiện hành.

Ngân sách đầu vòng được phép chi 94, số dư Flow đọc lại 294. Không coi toàn bộ số dư là quyền chi. Không chi thêm cùng cách phản ứng fail ở 169; Quality không còn một khoản 100 riêng.

## Bộ thoại A — hai câu mở

Đầu vào: OPEN7, Orus tùy chỉnh K20 và Aoede tùy chỉnh D06. Đã tìm preset qua danh mục Giọng nói và đối chiếu performance, không chọn giọng nền. Picker thêm ngay khi chọn option; nút Thêm vào câu lệnh có thể không còn, phải đọc trạng thái thay vì bấm lặp. Reuse trong màn edit chỉ điền ô sửa video; về project không giữ compose, nên gắn lại ba thành phần và kiểm route generation.

Omni 1.1 Flash / Thành phần / 360p / 9:16 / 8 giây / x3, giá actual 18. Không gọi đây là bộ Lite hoặc duyệt hình production. Tạo hình cùng thoại chỉ có thể sử dụng sau kiểm hình riêng; mục tiêu chính là audio.

Lời giữ nguyên: Đào “Anh nhìn mãi. Không hợp thì để em.” → Khoai “Khoan. Mùi này làm anh nhớ cái chảo.” Diễn: Đào nhẹ và tinh nghịch, Khoai đáp kịp rồi hạ giọng kể thân mật; không đọc đều, không quát hoặc tán tỉnh.

Folder: `C:/Users/PC/Downloads/du_an_nem_bui/170_opening_voice_blocks/`. Prompt A/B nguyên văn sẽ lưu ở folder này trước submit; kết quả, file nhận và ngân sách cập nhật theo thao tác thực.

## Bộ thoại B — bốn câu tiếp

Đào “Nem thì đây. Chảo ở đâu?” → Khoai “Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ.” → Đào “Chờ ăn?” → Khoai “Chờ mẹ quay lưng.”

Dự kiến cùng route/preset, x3, 10 giây để câu ký ức không bị ép vội. Kiểm giá actual trước gửi, không dùng quote 18 cho mọi thời lượng. Giữ khoảng nghỉ nhỏ sau hồi bé và trước câu cuối; không tự thêm câu giải thích.

## Gate

Nhận file và xác định có audio, giải mã sạch, kiểm transcript/đo khoảng lời bằng công cụ đã có. ASR chỉ là bằng chứng: không chứng nhận giọng Bắc, đúng người nói, truyền cảm hoặc lip-sync từ transcript. Nếu chưa nghe được bằng năng lực thực tế thì ghi chưa kiểm nghe; không tuyên bố agent đã nghe. Chủ dự án vẫn duyệt bản cuối về cảm nhận giọng.

Nếu thiếu quyền chi, cần đổi câu chuyện/hình thức hoặc không có coverage đạt, trình đúng quyết định còn thiếu thay vì giả định được phép. Chưa cam kết hoàn thành đủ chất lượng trong 94 credit.

## Kết quả thực tế — nhận file và QC

A gửi x3: hai lượt Flow chặn với cảnh báo chính sách liên quan đến trẻ vị thành niên và thông báo không tính phí; một lượt có video A03. Đây là đối thoại ẩm thực giữa hai nhân vật trưởng thành, không yêu cầu nội dung gây hại. Không gửi lại hai lượt bị chặn hoặc tìm cách vượt bộ lọc. Nguyên nhân chưa xác định; một lượt cùng prompt thành công không chứng minh từ nào gây chặn. B diễn đạt tích cực, rõ hai nhân vật trưởng thành và mục tiêu ghi thoại; cả ba thành công, không suy đây là nguyên nhân khắc phục đã xác nhận.

| File | Flow media ID | File tải gốc | Bytes |
| --- | --- | --- | ---: |
| A03.mp4 | af9d27c5-0c10-425e-b83a-95b23f83761d | Create_dialogue_recording_for_ch…_20261003121933.mp4 | 799599 |
| B01.mp4 | c4b4f8ba-9078-4c7b-8c2e-c058d6fe3b15 | Create_vertical_dialogue_recording_20261003122342.mp4 | 895808 |
| B02.mp4 | a81fc2a9-a5c8-4791-acad-9b9c7e8cc904 | Create_vertical_dialogue_recording_20261003122407.mp4 | 987425 |
| B03.mp4 | 7bfe7636-f621-4fbd-adc8-291290cfa4f7 | Create_vertical_dialogue_recording_20261003122744.mp4 | 876054 |

Native download360p ở tab tải mới hoạt động cả bốn file; đối chiếu file hiện hữu/bytes và giải mã toàn file, không dùng toast làm bằng chứng duy nhất. H264360x640/24fps, AAC48kHz stereo; A8s, B10s. WAV `*_VOICE_PENDING.wav` là PCM48kHz stereo tách từ AAC gốc, không đổi tốc độ/giọng hoặc phục hồi chất lượng đã mất do AAC. Grid2fps cho kiểm sơ bộ hình, không chứng nhận từng frame/lip-sync.

Hình bốn lượt chưa đủ dùng production: mặt/tỷ lệ/framing thay đổi so với OPEN7; món thành ụ sợi có xu hướng giống mì, không giữ texture Nem Bùi đã duyệt; B03 đổi bố cục đạo cụ nhiều hơn. Chỉ xét audio, không dùng hình thoại để lấp khoảng thiếu coverage. Miệng chuyển động không đủ xác nhận đúng người nói hoặc đồng bộ tiếng–miệng.

Offline QC dùng `scripts/local_voice_qc.py`, faster-whisper small/CPU/int8, tiếng Việt, không initial prompt, không gọi API. Báo cáo tại `artifacts/voice-qc/170-A03`, `170-B01`, `170-B02`, `170-B03`; sao lưu folder owner `qc/`. Mỗi bộ có media.json/asr.json/transcript.txt/audio-diagnostics.log. Audio16k mono cho ASR không phải bản nghe gốc gửi owner.

| Mẫu | Khoảng lời ASR | Khác biệt cần nghe | Mean/max dBFS | Mẫu PCM chạm biên |
| --- | --- | --- | --- | ---: |
| A03 | 0–2,62; 3,50–6,70 | “đề em”, “cái chào” thay vì để em/cái chảo | -17,2 / -0,2 | 0 |
| B01 | 0,82–2,46; 2,88–7,24; 7,66–8,14; 8,56–9,44 | Nèm/chào/dăng gạo thay vì Nem/chảo/rang gạo | -17,4 / 0,0 | 4 |
| B02 | 0–1,64; 1,92–5,30; 5,70–6,20; 7,54–8,68 | chào/gian gạo/chờ anh | -17,2 / -0,1 | 0 |
| B03 | 0–1,88; 2,36–5,74; 6,18–6,76; 8,46–9,54 | chào/găng gạo; khoảng trước câu cuối cần nghe | -16,9 / -0,2 | 0 |

Mẫu chạm biên: PCM stereo16bit, trị tuyệt đối>=32767. B01 có4 mẫu không đủ kết luận nghe thấy clipping; giảm gain không phục hồi tín hiệu đã clipping nếu có. Không tự gọi B01 sạch hoặc B02/B03 có diễn tốt hơn từ thống kê. ASR lệch có thể do nhận dạng hoặc phát âm, chưa xác nhận. A03/B01 trình nghe như ứng viên, chưa là winner; chỉ một file A, không ghi ba mẫu A đạt.

SHA256 MP4:

- A03: `9be7ee58780a435a24f51ca7fbb4d24c73d04f0b59169f210e103eed4bdad866`.
- B01: `4481bd1b898c00a036a3392aa1a930f580c8349aedf1647926fd09bc44a8c1e2`.
- B02: `2f39236352a8e6ff9a65907bdbb8f8fadc9345446112ad5d241e1463ec3580e6`.
- B03: `7184ad3beac767147f60c61803c2964556d6a8567a4aa89280b46e9b51a2cece`.

## Đối soát và hai quyết định đang chờ

Đã đọc lại Flow267: 294→267, chi ròng27 (A6, B21), còn **67** được phép chi. Trần hợp nhất134 theo168, chi lũy kế67, còn67. Account267 không tự thành quyền chi267. A18 là quote x3, không phải chi actual sau hai lượt bị chặn; B10s quote21 kiểm trước submit, không ghi18.

Ba cụm coverage chưa đạt theo166/169: mở/kể chuyện/quay đi; nâng-khựng/phản ứng; chuyển-nhận/kết. Tối thiểu một bộ x3 Lite/cụm dự toán90 theo giá30 đã quan sát, thiếu23 so với67. Một cụm có thể cần hơn một shot/bộ: video8s không tự đủ lời14s hoặc coverage. Chưa bảo đảm90 là hoàn thành; audio sửa và hình thất bại chưa nằm trong tối thiểu.

Đã hỏi owner ngay:

1. Cấp thêm **tối đa90** cho full-motion/script đã duyệt hay giữ67 và trình lại phương án? Nếu duyệt:67+90=157, dự toán năm bộ hình x3 giá30+7, gồm ba cụm tối thiểu và tối đa hai bộ bổ sung/dự phòng. Chưa approved; không bảo đảm đủ nếu phải sửa audio hoặc tách thêm shot. Không tự đổi sang ảnh tĩnh, bỏ nhịp hoặc tiêu toàn account.
2. Nghe A03/B01 xác nhận đúng accent/identity/câu và cảm nhận diễn. Root chưa có năng lực nghe thực tế, không giả lập agent đã nghe. Nếu lỗi ghi rõ mẫu/câu để sửa có đối chứng, giữ preset đang chốt.

Chưa generation hình mới hoặc render bản lỗi thành master. Đã hoàn tất phần hiện tại không cần quyết định mới: tải/full decode/WAV/grid/QC/bằng chứng/hồ sơ. Dừng tại quyết định ảnh hưởng ngân sách/gate nghe, không phải coi nhóm thoại xong là nhiệm vụ cuối hoàn thành.

## Tổng hợp vòng

- Đã xác định: bốn file audio ứng viên; ba B, một A; hình chưa đạt; chi27, còn67.
- Đã chốt: xử lý tuần tự đến bản cuối; script32/cặp giọng/tiêu chuẩn giữ nguyên, không tự đăng/mở ngân sách.
- Giả định: audio có thể tái dùng sau nghe, hình mới có thể nối hợp lệ; chưa coi đủ coverage.
- Còn mở: nghe A03/B01, quyền thêm90 hoặc tái lập phương án67, timecode/source từng shot và đồng bộ miệng.
- Tiếp: nhận hai xác nhận, khóa timing; refs từng hành động, giá UI, x3 mỗi nhóm rồi review; ráp30s/claim/AI/âm lượng/continuity, trình owner master cuối.
