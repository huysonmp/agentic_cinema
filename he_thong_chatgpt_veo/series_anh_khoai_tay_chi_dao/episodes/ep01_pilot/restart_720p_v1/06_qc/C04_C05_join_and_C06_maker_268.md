# REC268 — Maker DIR / DOP / ACT / EDIT: nối C04→C05 và draft C06

Ngày 12-10-2026. RUN_ID `REC268_C04_C05_JOIN_C06_MAKER`. **Kết luận: hình tại seam không có MAJOR mất bát/reset cốc; range C05 và draft C06 phù hợp để trình gate tiếp. Shortened encoded join chưa được nghe/xem liên tục, chưa được owner chấp nhận; C05 range/endpoint và C06 vẫn HOLD.** Đây là maker actual seam + paper C06, không độc lập, không approval trả phí hay output C06.

## Authority, target và scope thực

- Đã đọc owner acceptance mới `00_decisions/C05-T02-owner-audio-AV-acceptance-268.json`: owner trả lời “Đạt toàn bộ tiếng và AV trên T02”, exact native C05 T02 SHA-256 `3df61217ddf6d09792fe1e5991c3668d115ce5648c00802f196d87abe57d23df`. Accepted scope là đầy đủ N05, Đào/D06, một lượt/no male/extra, âm cuối và AV nguồn. **HUMAN EVIDENCE**, không nhận maker/root đã nghe. Duyệt này không bao shortened range, encoded seam, C06, cả phim hay export.
- Giữ authority217 đã đọc FULL ở REC267; lần này đọc FULL plan236 (phần output bị cắt đã đọc bổ sung), C06 draft268, voice bindings238, boundaryA263 và scoped238. Plan236 là lịch sử kế hoạch; quyền238 thay separate-request policy trong scope, rough35 tại264 thay trần30 cho rough, không là duyệt cuối hoặc mở reserve. Owner audio/AV268 không thêm quyền generation.
- Actual encoded QC: `C:/Users/PC/Downloads/du_an_nem_bui/268_C04_C05_JOIN/C04_T02_C05_T02_8p75S_JOIN_QC_NOT_APPROVED.mp4`; **SHA-256 tự kiểm file hiện hành** `a788ff13cbd7279a11137f993ad2462381f48e041dc0d7e748c380a3d8e8bdc6`.
- Mapping được giao: C04 native `[0,144)` /6s + C05 native `[0,66)` /2.75s; C04 audio replaced6s silence, C05 first2.75s audio, không speed/gain/voice replacement. Maker đọc evidence encoded, không tự chạy dựng lại hoặc chứng minh nội dung audio bằng probe.
- Đã đọc FULL `encoded_qc/native_evidence.json` và `action_all/manifest.json`: 720×1280 H.264/24fps, 210 decoded/extracted frames, audioAAC48k stereo, video/audio/container8.75s; full_decode_success. Không đồng nhất technical evidence với cảm giác cắt/AV PASS.
- **Ảnh thực đã xem ở REC268:** action boards17/18/19/20, encoded F128–159 tất cả32 khung; PNG full F143/F144/F209 (`00144.png`/`00145.png`/`00210.png`). Không nhận đã xem all210 trong lượt này. REC267 maker đã xem toàn96 C05 native và full START, không dùng report native đó thay encoded-target review.
- Evidence scope `FRAME_STILLS_AROUND_ENCODED_SEAM_AND_ENDPOINT`; `ACTUAL_LISTENING=NOT_PERFORMED`, `CONTINUOUS_VISUAL=NOT_PERFORMED`, `FULL_AV=NOT_PERFORMED`. Không nghe, phát AV, browser/API/credit/git/cài mới/script mới/chỉnh media; không đọc report independent268. Chỉ ghi report này.

## Actual seam F143 → F144 / 5.958333 → 6.000000 giây

Encoded F128–143 là tail C04 actual đã chọn, F144–159 là native C05 F0–15. Trong tail C04, Đào đã nhìn Khoai; Khoai nhìn xuống A, cả hai môi kín, A còn trên own pair, cốc nâng. F144 C05 hai người nhìn nhau, cả hai môi kín; nữ bắt đầu môi hé ở encodedF153/nativeF9/t=6.375s. Không lặp head turn/discovery đã được boundaryA263 chuyển sang C04.

| Vùng kiểm tại cut | Expected → observed | Finding / hệ quả |
|---|---|---|
| Hai bát cá nhân | Tách/rỗng, bát Đào còn đọc được → full F143 và144 đều có vành/lòng bát riêng ở bên phải plate, bát Khoai bên trái. | Không major mất/reset bát. Bát nhận không phải cốc hay chấm. |
| Cốc Đào | Nâng inherited tay ngoài → vẫn nâng từ F143 qua144–159. Đáy cốc F144 thấp hơn F143 khoảng10–20px theo ảnh full720×1280; không đo tracking phần mềm. | **MINOR continuity drift** đã biết; không gọi exact lock, cũng không phải reset sát bàn T01. Cần owner xem tốc độ thực để xác nhận mức chấp nhận. |
| Gaze Khoai | Bị bắt→nhìn người bắt → F143 mắt về A, F144 mắt đã sang Đào. | **MINOR/PERF seam**: eye shift xảy ra qua cut, không có motion nối bên trong source. Có logic reaction, chưa chứng nhận cảm giác liền ở real time. |
| A/own pair | Giữ A xa miệng → F143/144 vẫn một A giữa tips pair trong tay ngoài màn hình-trái, ở vùng dưới ngực trên bát Khoai. Góc/pose tái dựng nhẹ, không thấy ăn/trao/thả. | Tính liên tục vật thể đọc được; không pixel-identity proof. Không có flip trục hoặc destination mới. |
| Tay/người nghe | Inner hands nghỉ, pair nữ trên bàn → còn nghỉ; nữ môi kín đến nativeF8, nam kín toàn window. | Không thêm lời nam từ hình; âm thật cần owner checkpoint encoded. |
| Món/ánh sáng/bố cục | Rau front-left, hai chấm, plate nguội, hai faces/two-shot → giữ bố cục qua cut, không thấy khói hoặc prop biến mất. | Không phải mask/crop workaround; native watermark còn. Không certify toàn phim từ window32frames. |

DIR/ACT: seam giữ nguyên causal chain khán giả đã thấy anh tranh thủ ở C04 → cô nhìn lại trước cut → cô nói ở C05 → anh khựng. Gaze jump nhỏ không làm A trở thành cho Đào từ đầu. Không thiếu nguyên nhân bị bắt ở seam này theo ảnh và boundary đã duyệt. DOP: camera/trục/mắt/bàn tương thích, không mất mặt người nói hoặc tay mang A. Chưa gọi “smooth join” bằng stills.

## Range `[0,66)` và endpoint actual encoded F209

EncodedF209/t=8.708333 là native C05F65/t=2.708333, ranh giới hết clip ở8.750. Full endpoint cho thấy hai môi kín, hai mắt đọc được, A còn held ở own side, hai bát empty rõ, cốc Đào lifted tay ngoài, tay trong resting, own pair Đào còn tabletop. **Thị giác endpoint phù hợp F2 để chuẩn bị C06**, chưa là approved START asset.

Lý do giữ range conditional REC267 còn đúng: entry0.375s trước female mouth movement; giữ hình biến đổi môi nativeF9–45; giữ closure từF46, blink/reopen namF49–55 và caught stillness F56–65. Đề nghị ending sau mắt mở, không cắt tại blink. Đây là contribution EDIT; voice source đã accepted bởi owner268, nhưng trọn âm cuối của shortened2.75s, encoded sync và rhythm thực vẫn cần nghe/xem target mới. Không suy từ source lip-sync approval ra export/range PASS, không suy mouth closure ra waveform đã hết.

Do C04 có6s silence trong QC, điểm6.0s chuyển sang C05 source ambience có thể tạo bước tiếng. Đây là **rủi ro phải nghe**, chưa phải defect đã nghe. C04 nguồn AAC chưa được accepted; silence là cách targetQC hiện hành xử lý theo mapping được giao, không là final sound design/mix approval. Không tự thêm fade/ambience/nhạc để giả đóng gate.

Root cần owner kiểm exact8.75s target: câu/âm cuối còn đủ sau shorten, miệng–tiếng và phản ứng, seam gaze/cup/A thấy tự nhiên, nhịp caught đủ trước excuse. Kết quả cần artifact/hash/range riêng; nếu endpoint thay thì C06 ref/draft dependency phải kiểm lại.

## Paper C06 T01: thiết kế chuyên môn theo plan236

Đã đọc FULL `04_requests/C06_T01_prompt_DRAFT_268.txt`. Draft rõ PAPER REVIEW ONLY, sẽ dùng approved exit của C05 sau range/join gate; **chưa có actual C06 ref**, cloud upload/config/quote/output. Không GO input final hay submit từ paper này.

| Vai | Contribution / đối soát draft | Điều kiện và rủi ro |
|---|---|---|
| DIR | Giữ C06/N06 chữa cháy: caught stillness → nói bình thản “Anh gắp cho em mà.” → đổi hướng cùng A về bát riêng Đào. Hành động bắt đầu lúc lời sắp xong/sau lời, không cho từ trước khi bị bắt. | Đúng F2→F3 plan236. Không thêm N07, không release/ăn A, không sửa câu để ép thời gian. Phải thấy cause→excuse→redirect trong actual. |
| DOP | Two-shot ổn định giữ cả faces, mặt Khoai khi nói, listener nữ và A/tips/bát đích. Giữ trục Khoai-left/Đào-right và raised glass. | Cross-table reach từ outer-left hand Khoai sang bowl-right có thể che torso/face hoặc bị model đổi hand. Actual phải giữ mặt và đường A, không crop làm insert suốt N06. |
| ACT | Nam mature/K20, calm understated, ngượng nhỏ, no loud joke/MC/broad grin. Nữ silent listener nhìn face→piece, kín môi, không phát hiện lặp hoặc nói trước C07. | Preset không đảm bảo performance output. Eye/hand cue cần đủ rõ, không chỉ ghi “embarrassed”. Nếu lời/động tác chồng khó đọc, kiểm real time trước range. |
| EDIT / DLG-EDIT | Sinh6s cho room diễn; không mặc định dùng6s. End giữ A trên approach tới bát Đào, vẫn held; lips đóng/response beat ngắn. | Không chọn chỉ frame đẹp nếu mất motion/âm cuối. Chưa source/timing/range C06, không gọi fit35. |
| CONT / FOOD | SAME A, own outer-left pair không đổi tay/thêm piece; inner hands resting; both empty bowls; nữ glass inherited, own pair tabletop; rau/hai chấm/coldfood. | Bát RIGHT của nữ là destination, không male bowl/sauce. A không touch shared plate, không vào mouth, không drop. C07 mới đưa/lift bát; C08 mới release. |

Single voice binding đúng paper: `EP01_Khoai_K20_Orus_720p_v1`, saved new ID `b447b35c-b35e-4140-af72-ecd277282b1a`, baseOrus, K20 performance. Chỉ preset này cho C06 Ingredients; không attach D06 dù Đào vẫn trong hình. bindings238 ghi owner preview accepted239; không chứng minh actual C06 mới đúng voice hoặc UI/backendID đã verify trong live run. N06 nguyên văn **“Anh gắp cho em mà.”** chỉ Khoai nói một lần, female/no extra forbidden. Không chuyển audio268 của Đào sang C06 Khoai.

Draft không có mâu thuẫn canon/nhân vật/vật đích thiết yếu. Từ “across the tabletop” cùng “above the table/no touching shared plate” đủ định hướng trên giấy nhưng không khóa quỹ đạo: actual cần đi bên trên bàn, tránh chạm/đổi A với pile shared food và không nhầm chấm trước-phải thành bowl Đào. “End holding A in the approach” chưa khóa cự ly cuối; hợp lý vì C07 đưa bát nhận, nhưng readiness C07 phải dựa endpoint actual C06 và khả năng bát reach dưới A. Không tự yêu cầu drop trong C06 cho đủ F3, không để bát di chuyển sớm nhằm vá reach.

Nếu làm rõ phrasing trước final, đề nghị hẹp: chỉ định A/tips còn ở phía trước/trên vùng tiếp cận bát riêng Đào với clearance và không vào chấm; mọi point phải bám approved ref thật, không bịa coordinate/path khi chưa có. Đây là gợi ý, không blocker bắt buộc hoặc file prompt đã sửa. Nhiều anchor không bảo đảm Ingredients pixel lock hay all-frame motion; phải kiểm actual full nguồn.

## Timing35 và cổng còn mở

Conditional C05 `[0,66)` làm selected-before count từ566 lên632frames =26.333333s; tới rough35 còn208frames =**8.666667s cho C06–09**. Đây là giới hạn tổng thực về số học, không timing ước lượng N06/N07 hoặc motion. Plan236 chia R06≈2s/R07≈2.5/R08≈1.5/R09≈2.5 vốn tổng8.5s cho bốn nhịp; so margin8.666667 chỉ dư≈0.166667s nếu các ước lượng cũ đúng, **chưa được đo trên source mới**. Rủi ro nhịp chật cao hơn việc nhìn duration sinh6s.

Nếu phải dùng cả6s C06, còn2.666667s cho C07–09; chưa có bằng chứng đủ N07/đưa bát/thảA/gắpB/kết trong khoảng đó. Không khẳng định không thể tuyệt đối, nhưng không commit full6s hoặc mở shot sau từ giả định fit. Root cần actual lời/redirect C06 + timing C07–09, giữ nhịp tự nhiên và lời đầy đủ; nếu không vừa, trình conflict/tái phân bố trong authority hiện hành. Không speed/pitch/omit/dialogue-over-still workaround.

**Đã xác định:** owner accepted full native C05 tiếng/AV; encoded seam ảnh giữ hai bát/cốc/A, minor gaze/cup còn nhỏ; endpointF65 phù hợp chuẩn bị F2. **Chưa chốt:** shortened range/encoded AV/rhythm/actual C06 START. **Giả định:** range66 vẫn giữ nguyên lời/âm cuối; chỉ human check mới xác nhận. **Còn mở:** target8.75s owner checkpoint, root đọc independent report, approved native-frame asset/provenance/hash, final prompt/liveconfig/quote/budget permission và timingactual. **Bước tiếp:** checkpoint exact shortened join → khóa range/START → final paper/live gates C06 theo quyền thật; không generation hoặc chi trong task bounded này.
