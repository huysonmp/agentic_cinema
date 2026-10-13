# REC286 — Có video mới; chưa chọn vì thay đổi ngoài món

Ngày 13-10-2026. **ONE_APPROVED_REQUEST_COMPLETED / NATIVE_720_DOWNLOADED / VISUAL_REWORK_NOT_SELECTED / NO_RETRY.**

## Kết quả và phạm vi duyệt

Owner “duyệt” chấp thuận đúng một request qua composer dự án, cap20, trừ ngân sách tạo lại, không tự chạy lại. Đã kiểm lại nguồn/ảnh/prompt đúng hash, một video ingredient + START material-only, Omni1.1Flash/Ingredients/720p/9:16/x1/Agent OFF và giá20. Không đổi thoại/giọng/ảnh; không dùng END hoặc tái dựng lời.

Flow xử lý đến hoàn tất và trả file mới. Đã tải **720p kích thước gốc** bằng nút download/event, lưu bản gốc ở repo và folder owner, không ghi đè source. Số dư cùng tài khoản sau reload **1.013→993**, net debit20. Sổ dự án **237/500, còn263**: lượt đầu82, tạo lại26, hậu bản thô45, dự phòng110 vẫn đóng. Đây là actual debit, không chỉ reservation/giá public.

## Bản kiểm thực để xem

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/286_FOOD_EDIT_PROJECT_PROMPT/`.

- Video: `EP01_720_C05_C06_FOOD_EDIT_T01_NATIVE_286.mp4`.
- SHA-256: `4703fb9b34abbb63144364cb388aa4d9921e06d7b7c597f2da77d04a7299e583`; 960.215 bytes.
- Native: 720×1280/H.264/24fps/**124 khung**; video5,166667s, AAC stereo48k/audio5,184s, giải mã toàn bộ thành công.
- Nguồn đã duyệt: SHA `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`, 123 khung/video và audio5,125s. Output thêm một khung; không tự gọi đó là padding hoặc cắt bỏ để hợp thức hóa.
- Flow output: https://flow.google.com/project/bcb1f53c-13b6-4719-b866-01348dfcddd6/edit/195014ac-915d-4de1-8cd8-bde11a1006ae.

Native QC: `native_qc/native_evidence.json`, `all_native_frames/00001.png`…`00124.png`, tám board `full16_01.png`…`full16_08.png`, audio trích riêng và ASR offline ở `asr_qc/`. Root, maker và critic đã xem đủ124 khung qua board liên tiếp, cùng các khung full-resolution quan trọng để so nguồn. Đây là **toàn-frame ở độ lớn contact sheet + một số khung full-resolution**, không xem/nghe AV liên tục hoặc kiểm mọi pixel ở độ phân giải gốc. Bốn ô đen cuối board8 chỉ là padding board, không khung đen video.

## Lỗi đã có bằng chứng — không chuyển approval nguồn

| Scope | Quan sát | Kết luận |
| --- | --- | --- |
| Món | Đĩa và phần A trên đũa chuyển khỏi lát đặc sang hỗn hợp rời/thính. Không thấy khói, gắp lại, thả hoặc đút ăn trong board toàn124 khung | Cải thiện về hướng vật liệu; chưa nghiệm thu món/quantity tuyệt đối, không bù lỗi khác |
| Trang phục | Đào bị thêm **yếm/dây xanh trước ngực ngay F0**, trong khi nguồn và START là áo trắng, xanh ở váy dưới | **MAJOR ngoài phạm vi sửa món**; giữ lỗi mở, không đổi canon |
| Hậu cảnh/camera/cut | Output F71 còn phố cũ, **F72 tại3,000s chuyển sang hậu cảnh khác với đèn lồng lớn**, bàn/đĩa/bát theo khung đổi. Source giữ phố cũ; cut nguồn tạiF66/2,75s | **MAJOR không bảo toàn bối cảnh và sequence**. Không suy mọi motion/audio trễ sáu khung; cần mapping mới kết luận retiming |
| Thời lượng | Source123F→output124F, audio dài hơn | Timing/range mở; chưa tự trim/time-stretch hoặc áp EDL cũ |
| Tiếng/khẩu hình | Có audio, thứ tự hoạt động miệng khái quát Đào rồi Khoai trong ảnh | **Chưa actual listening/AV/sync PASS**. Approval tiếng/nhịp REC277 không chuyển qua output mới |

Root đã đọc đầy đủ `06_qc/C05_C06_food_edit_maker_actual_diagnosis_286.md` và `06_qc/C05_C06_food_edit_actual_independent_286.md`, đối soát hình thật và đồng ý **NOT_SELECTED**. Các báo cáo này ghi debit chờ root tại thời điểm viết; số dư actual cập nhật20 ở report/run hiện hành này. Không đưa output vào EDL hoặc finishing, không xin owner miễn lỗi rõ để gọi clip đạt.

## Tiếng: dữ liệu kỹ thuật không thay nghe thật

FFmpeg giải mã PCM s16le đầy đủ: nguồn SHA `cab92ff38ffa950d109e9ee7900f0165558ecb840200b140e12f4f0730b042bd`; output SHA `017afc3ef1a3bc8b93fa6570eaa30f725bac590c4ba67b337b9d163e3a8f6918`. PCM đầy đủ không giống byte-exact; điều này **không chứng minh giọng đã đổi**, vì duration/encode/padding có thể ảnh hưởng hash. Chưa cô lập nguyên nhân khác biệt audio.

ASR local `small`, CPU/int8, tiếng Việt, offline, không initial prompt, nhận “Chờ em quay lưng nữa à.” và “Anh gấp cho em mà.”. Biến thể gắp/gấp là transcript mismatch, không tự kết luận phát âm sai; không dùng ASR để nhận K20/D06 hoặc heard_text. Không cần yêu cầu owner nghe để bù MAJOR hình đã rõ. Video/audio được lưu để xem, chưa được duyệt lại.

## Nguyên nhân theo tầng và kinh nghiệm

Đã xác định: điểm vào project composer thực thi được gói và sinh file; kết quả đổi món nhưng cũng thay vùng ngoài món. Prompt có yêu cầu giữ trang phục/phố/camera/cut, vì vậy không thể nói lỗi chỉ do thiếu viết các yêu cầu đó. **Chỉ dẫn bằng chữ chưa tạo ra kiểm soát vùng sửa cứng.**

Chưa cô lập: drift do đặc tính tái dựng của model, toàn ảnh ingredient, clip có cut hay câu prompt nào. Yếm xanh không có trong approved START, nên không tự nói model đã sao chép yếm từ ảnh đó. Thành công thực thi REC286 cũng không giải thích lỗi request chung REC284. Không hứa crop ảnh/tách shot/thêm negative prompt sẽ chắc chắn khắc phục.

Kinh nghiệm: kiểm vùng ngoài đối tượng cần sửa và cả chuỗi, không chỉ món/poster/720p. Giữ ba tầng riêng: **request chạy được → output hợp lệ kỹ thuật → output đạt nghệ thuật/bảo toàn**. Lần này chỉ đóng hai tầng đầu; kiểm toàn khung đã chặn drift trước ghép.

## Chốt vòng và bước tiếp

Đã làm: một lượt đã duyệt, tải gốc, hash/decode/thông số, kiểm toàn124 khung bằng board và critical stills, maker/critic/root review, debit20 và lưu bài học. Quyết định: không chọn take này, không thay source/EDL, không tự retry/batch sửa toàn tập; giữ native/job/source.

Giả định cần kiểm còn lại: có thể có cơ chế giới hạn vùng/refs giúp giữ source tốt hơn. Chưa là giải pháp đã chứng minh. Food gate các cảnh cũ, cảnh nhận–bỏ mới và timing30/rough35 giây vẫn mở.

**Bước tiếp khuyến nghị:** đánh giá phương án sửa cục bộ có cơ chế bảo vệ vùng ngoài món, hoặc phương án tạo lại có kiểm soát continuity và ngân sách toàn tập. Không tiếp tục cùng route chỉ bằng siết câu chữ. Nếu cần crop/ref/script/tool mới hoặc request trả phí, phải trình scope/cap/checkpoint trước; không dùng một lượt286 làm quyền cho việc đó. Chưa có phương án mới được owner duyệt, chưa hứa hoàn tất phim bằng263 còn lại.
