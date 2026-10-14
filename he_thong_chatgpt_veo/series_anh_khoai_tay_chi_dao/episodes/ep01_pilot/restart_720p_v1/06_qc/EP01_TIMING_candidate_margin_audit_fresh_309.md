# EP01 — EDIT timing / candidate margins, fresh REC309

Ngày 14-10-2026. Reviewer `/root/timing_audit_309`, bounded read-only ngoài đúng report này. **Kết luận: số đếm root khớp; qua C08 candidate là 816F/34s, rough35 còn 24F/1s cho C09. Có vùng đệm để thử cắt, chưa có số khung tiết kiệm an toàn đã nghiệm thu.** Không nghe actual/continuous AV, không browser/credit, không sửa media/EDL/Git, không chọn range mới. C09/B bắt buộc giữ; chưa có actual C09 tại snapshot này.

## Authority và snapshot

Đọc plan236, storyboard214; approval rough35 REC264; EDL257/268/307/309 và quyết định246/256/258/259/261/263/269/300/308. Đọc REC245/255/256/258/262/298/300/307/308/309, SELECTED_BLOCK308 và các report timing263/C03B259. Không đọc/quét toàn repo. Memory chỉ nhắc phân biệt paper/frame/ASR với actual AV; mọi range và quyền hiện hành bên dưới đối soát lại từ artifact hiện tại.

- Plan236/214: final target30, giữ lời/voices/mặt người nói/causality, A vào bát Đào rồi B khác về Khoai. R09 không được bỏ để cứu bảng thời gian.
- `00_decisions/rough-cut-35s-approval-264.json`: rough tối đa35s, ưu tiên gần30 nếu cắt an toàn, bảo toàn lời và nhịp tự nhiên; không phải final35 đã duyệt. Không cần chứng minh final30 trước khi hoàn tất footage C09 và dựng rough có bằng chứng.
- `00_decisions/C06-KEEP-A-encoded-range-dialogue-sync-approval-300.json`: đúng source KEEP_A298 [0,48), không dùng C06 cũ redirect hoặc ACT_B293.
- `00_decisions/C06-C07-local-bundled-acceptance-308.json` + `07_edits/C06_C07_SELECTED_BLOCK_308.json`: chọn exact encoded block307 [0,120), SHA `e97dd894d5225d64953145008494854fa154c691373b243e16490fdf41269fef`. C07 standalone không được tự coi đã duyệt riêng toàn hình. Range thống kê C06/C07 ở bảng là mapping trong block đã duyệt.
- C08 [0,64) silent309 là **conditional candidate**, chưa owner production-selection/full-film acceptance. Native vẫn có audio; derivative bỏ riêng audio C08 phát sinh, không coi toggle là native-silence evidence.

**Không có conflict duration giữa các authority hiện hành.** EDL257/268/307 vẫn mang pending/NOT_SELECTED từ lúc dựng thử; acceptance258/269/308 và selectedblock308 cập nhật trạng thái theo exact hash/scope, không cần sửa hồi tố EDL lịch sử. C05→C06 food seam vẫn OPEN; approval300 lời/range và approval308 C06→C07 không đóng seam này. Chưa có global production EDL/full-film export được duyệt bằng tổng các approval rời.

## Inventory R01–R09 tại 24fps

Range half-open, zero-based. Timeline dưới đây chỉ là phép tính nối range hiện hành, không EDL mới được chọn.

| Beat / source | Range nguồn | F / giây | Timeline F | Thẩm quyền / giới hạn |
| --- | --- | --- | --- | --- |
| R01 C01A T04 Flow cut | [0,81) export |81 /3.375|[0,81)|prefix246; audio246; exact opening258/259 |
| R01 BM Khoan local-shirt-repair |[20,38) nguồn254 = [0,18) short255|18 /0.750|[81,99)|selection256; opening258/259 |
| R01 BR T01 silent |[28,78) native|50 /2.083333|[99,149)|exception/range258; opening259 |
| R02 C02 T02 Flow export |[0,181) export|181 /7.541667|[149,330)|export246; opening258/259; extra frame Flow đã đo |
| R03 C03A T01 |[0,42) native|42 /1.750|[330,372)|approval259, exact opening15.5s |
| R03 C03B T01 |[0,50) native|50 /2.083333|[372,422)|selection261; whole17.583s chưa explicit accepted |
| R04 C04 T02 |[0,144) native|144 /6.000|[422,566)|boundary A263; QC silent treatment269 |
| R05 C05 T02 |[0,66) native|66 /2.750|[566,632)|range/seam269; không T01 |
| R06 C06 KEEP_A298 |J[0,48) trong block307|48 /2.000|[632,680)|range300 + exact encoded block308 |
| R07 C07 TWOREF local-mouth307 |J[48,120), tương ứng local[0,72)|72 /3.000|[680,752)|block308; không substitute standalone |
| R08 C08 DEPOSIT_A309 silent |[0,64) native mapping|64 /2.666667|[752,816)|conditional trial309, actual reviewer gate còn mở |
| R09 C09/B |UNKNOWN|UNKNOWN|[816,816+N)|chưa generated tại snapshot; plan236/story214 phải giữ |

Đối soát: 81+18+50+181=330; +42+50=422; +144=566; +66=632; +120=752; +64=816. Root632/752/816 đều khớp. So plan236, R01 hiện6.208333s so4.5s giấy; R03 hiện3.833333s so3s; R04 hiện6s so3s. R02 hiện7.541667s so8.5s giấy. Chênh kế hoạch không đồng nghĩa có thể cắt lại đúng số đó.

## Kiểm mới đã thực hiện

Fresh SHA256 và `ffprobe -count_frames` trên bảy file: opening257 `dd8a24…`330F13.75s; opening+C03A259 `47b779…`372F15.5s; C03B short `87a5d8…`50F2.083333s; C04 T02 `8ad98f…`144F6s; C05 T02 native `3df612…`96F4s; selected block307 `e97dd8…`120F5s; C08 silent309 `a152f5…`64F2.666667s. Tất cả720×1280/24fps, hash khớp authority tương ứng. Count đọc frame không thay full AV playback.

Tự xem existing boards: C04 T02 `262_C04/action_all_frames/action_all_01.jpg`, `_03.jpg`, `_16.jpg`, `_18.jpg` (F0–7/16–23/120–127/136–143); C02 Flow export `ep01_restart_720p_v1/06_qc/C02_T02_FLOW_245/mouth_hands_6fps_01.jpg`, `_03.jpg` (mẫu4F, không full181). C04 đầu những frame này mutual gaze/tay nghỉ; đuôi A đã kẹp, cốc nâng/Đào hướng Khoai, hai bát còn. C02 đầu0–16 ở mẫu môi khép/tay nghỉ; F20–24 có blink, F28+ bắt đầu khẩu hình. Cuối C02 sample F168/172 môi Khoai khép, F176 Đào blink. Không nhận đã nghe hoặc chứng nhận chỗ cắt từ các still.

## Vùng đệm và candidate cuts — phải actual AV review

Các timestamp ASR là **machine estimates đã có**, không phonetic boundaries mới đo/nghe. Khoảng ASR-gap không phải speech-free guarantee. `Measured` = range/count hoặc máy ước lượng có artifact; `candidate` = số khung giả định để thử, chưa tiết kiệm được phê duyệt.

| Ưu tiên / vùng | Evidence measured hoặc đã ghi | Candidate cụ thể, chưa selected | Hệ quả phải kiểm |
| --- | --- | --- | --- |
| 1. C02 lead |ASR245 N02 phần ký ức start0.96s; mẫu ảnh0–16 môi khép; F20–24 blink|Thử bỏ [0,16), tiết kiệm16F/0.666667s; giữ speech timing tương đối bằng cắt hình+audio đồng gốc|Còn khoảng0.293s theo ASR trước lời, không bảo đảm onset. BR→C02 đổi từ sourceF0 sangF16, phải seam/gaze/nhịp sau thu tay và âm đầu Mùi trên encoded candidate |
| 2. C04 lead |Ảnh tự xem F0–7/F16–23 đều mutual gaze/tay nghỉ; report263 ghi idle đầu~1s|Thử [12,144) thay[0,144), tiết kiệm12F/0.5s; **giữ endpointF143**|Không lấy chưa nói làm dư vô nghĩa. C03B→C04 entryF12 mới; phải giữ Đào đổi chú ý/nâng cốc trước Khoai pickup. Không cắt mid-action |
| 3. C02 tail |ASR245 end6.94s; silence diagnostic245~6.969s; export end181/24=7.541667s. Gap máy~0.602s; mẫu F168/172 khép, F176 blink|Thử end173, bỏ[173,181), tiết kiệm8F/0.333333s; nếu ghép với lead16 thì range[16,173)=157F|End7.208333s còn~0.268s sau ASR. C02→C03A đổi endpoint từF180 sangF172; giữ âm cuối chờ, closure, reaction/hand/scale exception259 và nhịp nhớ→hỏi |
| 4. C04 tail — chỉ dự phòng |Report262: A rời đĩaF105–107, Đào nhìn lạiF113–114. Tự xemF120–127/136–143 là hold/caught-state; nominal audit-zone[120,144)=24F|Không chọn số tiết kiệm mới. Có thể khảo sát cắt sau caught/khựng nếu3 vùng trên không đủ|C04 endpointF143 là nguồnC05 hiện hành; trim tail đổi A/tips/cốc/gaze vào C05F0, tái kiểm seam269 và khoảng đọc phát hiện. Không cắt hết24F rồi gọi approved |
| R03A/C03B — ít ưu tiên |ASR258 N03 end1.36s vs selected1.75s; closure C03A chỉ ổnF38+. ASR/report259 N04 end1.24s vs selected2.083333s; miệng khépF30+, blinkF36–40|Không nhận0.39/0.843s là savings. C03A chỉ2–4F nằm sau closure, quá nhỏ; C03B reaction/cười là beat hài|Trim tail thay sourceF41/F49 và điểm nối sang C03B/C04; không xóa reaction để khớp số học |
| C01A / BM / BR |ASR C01A N01 end3.20s so81F3.375s; BM đã18F0.75s; BR50F bao nhìn lênF30+/buôngF44+/thuF64+/nhìn mónF71+|Giữ hiện hành ở lượt audit này|C01A chỉ~0.175s máy-gap; BM đã sát từKhoan; BR thực hiện release/retract, không có saving lớn được chứng minh |
| C05 T02 |range66 đã owner nghe/cut269; visual closure/responseF56–65 ở report268|Giữ66; không áp end2.44s ASR T01 sangT02|Hai frame64↔66 từng là breathing choice; source/timing không được hoán đổi |
| C06+C07 block308 |ASR exactjoin307 N06~0–1.64s, N07~2.38–4.10s; block5s. Native298 ASR N06~0.46–1.60s khác estimate join|Giữ120F. Không cộng0.36+0.90s máy-gap thành tiết kiệm|N07 tail chứa nâng bát/giữ khoảng nhận tớiJ119. Cắt C07 đổi endpoint C08 đã sinh từJ119; trimming block cần exact encoded AV/cut/miệng sửa recheck |
| C08 |64F/2.666667s là candidate actual309; root đã kiểm emptytips/A-in-bowl tớiF63|Giữ64 để chờ reviewer actual; không tự thay bằng1.5s giấy236|Không cắt trước khi release/retract đọc đủ; C09 entry theo exit actual được chọn |

Khuyến nghị thử một candidate nhỏ **sau có C09 actual**, không sửa ngay approved source: C02[16,173) và C04[12,144) tiết kiệm giả định16+8+12=36F/1.5s, giữ toàn lời/voices/tốc độ, giữC04 exitF143 và giữblock308120F/C0864F. Candidate này chưa được dựng trong audit. AV review cần tập trung hai biênC02 và C03B→C04; whole rough review vẫn bắt buộc. Nếu muốn giữ C02 exitF180 trước, chỉ lead16+C04lead12=28F/1.166667s là vòng thử ít đổi endpoint hơn; không tự tăng lead để bù thiếu.

## Fit35 và tiếp cận30 theo actual C09

Gọi N là selected actual C09 frames, S là savings **sau** có candidate AV/seam acceptance. Tổng =816+N−S. Fitrough35/840F cần **S≥max(0,N−24)**. Fitfinal30/720F cần **S≥96+N**. Hiện S đã được chứng minh an toàn trong audit này =0, N chưa biết.

| N C09, chỉ scenario | Tổng hiện hành | Saving cần rough35 | Saving cần final30 |
| --- | --- | --- | --- |
|24F/1s|840F/35s|0F|120F/5s |
|48F/2s|864F/36s|24F/1s|144F/6s |
|60F/2.5s, giấy236|876F/36.5s|36F/1.5s|156F/6.5s |
|72F/3s|888F/37s|48F/2s|168F/7s |

Candidate36F nếu AV đạt và C09 thực đúng60F thì rough35 vừa đúng840F, **không còn slack**; đó là scenario, không lời hứa. Vùng3 ưu tiên không chứng minh đủ156F để final30. Không cộng các khoảng nghỉ ASR, bỏC09/B, cut từ/âm cuối, tăngspeed/pitch, revoice, đóng băng hoặc tái sinh accepted clip để tạo ra lời hứa30.

Đã xác định: inventory/count khớp và các vùng thử cụ thể có evidence. Đã chốt: giữ quyền rough35, lời/canon/B và block308; không có selection mới từ report. Giả định: C08candidate64F chỉ dùng để tính có điều kiện; C09 actual chưa có. Còn mở: C09range/readability, C08selection/seam, C05→C06food seam, savings sau exact encoded AV review và whole-film rough/final. Bước tiếp: kiểm C09 thật → thay N trong công thức → dựng một candidate cùng EDL thử/hash → bounded actual frame review + actual AV/rhythm trên đúng candidate → owner rough checkpoint. Finishing F01/F02/AI label cần kiểm readability trong nhịp còn lại, không tự chèn hold mới rồi bỏ qua thời lượng.
