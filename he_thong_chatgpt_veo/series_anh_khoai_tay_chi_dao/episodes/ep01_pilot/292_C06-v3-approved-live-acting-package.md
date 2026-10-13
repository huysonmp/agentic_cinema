# REC292 — Ảnh v3 được duyệt, gói C06 diễn B chuẩn bị trên Flow

13-10-2026. Owner nói “duyệt”, rồi “tiếp tục đi, duyệt” cho đúng ảnh v3 đã trình tại REC291. **Chốt ảnh tham chiếu, không tự chuyển thành duyệt video hoặc lượt trả phí.**

## Quyết định và đầu vào

Biên bản `restart_720p_v1/00_decisions/C06-entry-v3-owner-approval-292.json` khóa v3 SHA `7c8023cbe655745b941e1a47dd1df3614ba66fcef512a41c5c4c4048bb33f8cc`, 720×1280, cùng caveat nhỏ mép A đã công bố. Sắc thái B giữ theo REC290. Không chỉnh ảnh lần nữa hoặc sửa source C05/EDL.

Đã dùng trình duyệt tích hợp, kiểm đúng project `bcb1f53c-13b6-4719-b866-01348dfcddd6`, tài khoản `cutebabyshop2026@gmail.com`, Pro. Upload đúng PNG đã duyệt, chọn tên chính xác trong bộ thành phần và thêm vào composer. Không dùng ảnh START ở cuối C06/END sau nhận hoặc footage REC286 bị bác.

Prompt [C06_ACT_B_T01](restart_720p_v1/04_requests/C06_ACT_B_T01_prompt_292.txt), SHA `c16d79f396529a043973dba90b24cd0823279ac7c32766bac405fb7488c434da`, đã đặt và đọc lại khớp khi chuẩn hóa khoảng trắng. Nội dung: Khoai biết bị bắt tỏng, giữ thể diện; chỉ nói **“Anh gắp cho em mà.”**, nói trọn âm cuối rồi chuyển cùng A nhưng chưa thả. Không bắt gật/hạ cằm/nhún vai, không thêm tiếng Đào, không ép endpoint dừng–giữ cũ. Giữ cốc Đào trên không ngoài bát, hai bát rỗng, tay trong nghỉ, món lạnh không khói.

## Voice và cấu hình live đã kiểm

Đã chọn đúng option **EP01_Khoai_K20_Orus_720p_v1**, đọc đủ tên, performance nam Bắc/ấm chắc và sample 109 ký tự trước khi thêm. Không chọn D06/Aoede, Orus nền hoặc K12; không preview/save/sửa preset. Có đúng **hai chip: một ảnh, một giọng**. Câu audition trong UI chỉ là bằng chứng preset, không được đọc trong C06.

ID `b447b35c-b35e-4140-af72-ecd277282b1a` là mapping lịch sử. Current option DOM không lộ ID; **không tuyên bố xác minh ID live/backend**. Tên và toàn chỉ dẫn đã kiểm qua UI rồi thêm đúng option; tiếng output mới vẫn cần nghe/owner kiểm. Khi mở lại bộ giọng sau khi gắn, option K20 không hiện trong danh sách đó; locator báo không có match. Root đọc trạng thái mới thấy D06 chỉ ở panel xem, đóng panel và **không thêm D06**; không dùng lỗi locator để suy chip K20 mất hoặc đã đổi giọng. Không giả có screenshot preset khi thao tác chụp chưa chạy do locator lỗi.

| Thuộc tính | Đã đọc trên UI |
| --- | --- |
| Tuyến | Video → Thành phần |
| Mô hình | Omni 1.1 Flash |
| Khung / độ phân giải | 9:16 / 720p |
| Thời lượng / số đầu ra | 4 giây / x1 |
| Tác nhân | `aria-pressed=false` |
| Trả về video không tiếng | `aria-checked=false`, tiếng bật |
| Quote sau khi gắn tài nguyên | **7 credit** |
| Số dư tài khoản | **993 credit**, không thay so cuối REC286 |

**Giới hạn:** Ingredients là ảnh tham chiếu, chưa chứng minh khóa đúng F0 hoặc giữ pixel vùng ngoài món khi sinh video. Không đổi sang Frames và tự giả có saved voice tương thích. Không hứa model đạt acting B hoặc giữ giọng chỉ vì preset đúng.

## Bằng chứng và kiểm trước trả phí

`C:/Users/PC/Downloads/du_an_nem_bui/292_C06_ACT_B_PREFLIGHT/` chứa `CONFIG_QUOTE_292.png` và `LIVE_CONFIG_DOM_292.txt`. Screenshot có gói ảnh/voice, cấu hình và quote; SHA `2020fc06de325d6a8f4688c678a83262a686607cb3c716b2dbc21da1871a1b24`. Hồ sơ cấu hình: `restart_720p_v1/04_requests/C06_ACT_B_T01_preparation_292.json`.

Phản biện local độc lập đã hoàn tất, root đọc đầy đủ [báo cáo preflight](restart_720p_v1/06_qc/C06_ACT_B_independent_preflight_292.md): không có mâu thuẫn PAPER nghiêm trọng, đủ trình một request cap7; không cấp quyền tự submit. Reviewer xem screenshot/đọc DOM, ghi rõ các mục voice/performance/Agent/audio là root báo khi proof không hiện đủ. Đây là preflight, không actual video/acting/voice/AV PASS. Root không bấm Bắt đầu tạo; tab giữ để tiếp tục, phải recheck cấu hình/tài nguyên/quote sau khi nhận quyền trước gửi.

## Đề nghị lượt mới — chưa được cấp

Đề xuất **một** output C06 ACT B, quote/cap **7 credit**, bucket tạo lại; không tự retry. Nếu quote tăng hoặc tài nguyên/giọng/cấu hình không khớp thì không gửi, báo owner. Cap20 REC286 đã dùng, không tự tái sử dụng. Dự phòng110 vẫn đóng.

Nếu actual debit đúng7: sổ237→244/500, còn263→256, phần tạo lại26→19. Đây là dự tính, **chưa chi**. Sau output: tải native720/hash/decode/toàn-frame, kiểm diễn mặt–thân liên tục và speaker/lời/giọng/khẩu hình, A/props/món và điểm vào/ra; chỉ chọn range đủ lời + A chưa thả. Không dùng ASR/hash thay nghe, không che mặt bằng cận món hoặc revoice tự động.

Food C05/các cảnh trước vẫn dependency; timing30s còn mở theo REC289 (`632+N` qua C06, `88−N` cho kết nếu trước C06 giữ nguyên). Ảnh được duyệt không tự sửa các footage cũ hoặc đảm bảo phim cuối đủ30 giây.

**Đã chốt:** ảnh v3 và sắc thái B. **Đã xác minh:** gói ảnh+K20, prompt read-back, cấu hình live/quote7. **Giả định cần kiểm:** ảnh làm tham chiếu đủ giữ entry, diễn và food; giọng output thực. **Còn mở:** quyền một lượt mới, kết quả/AV/continuity/timing toàn tập. Flow chi mới0; sổ237/500 còn263, dự phòng110 đóng; chưa output/source replacement/EDL/release.
