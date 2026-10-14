# REC309 — C08 actual review độc lập

**CONDITIONAL_GO_C09_FROM_EXACT_ENCODED_PREFIX_F63 / STILL_EVIDENCE_ONLY.** Candidate có thể dùng là `07_edits/C08_DEPOSIT_F0_F63_SILENT_REVIEW_309.mp4`, range `[0,64)`, 64F/24fps/2,666667s. Không phát hiện MAJOR nhìn thấy trong range này. Không nhận toàn native4s, không owner approval, không AV PASS hoặc full-film/release PASS.

## Phạm vi thực kiểm và provenance

- Đã đọc đủ scoped-autonomy238, run309, acceptance308, selectedblock308, independentpreflight308, FINALprompt309, hai native_evidence và audio_measurement309. Chỉ local read/view/hash, viết riêng report này; không browser/paid/retry/Git/media/EDL.
- Trực tiếp xem START308, native F0, tất cả sáu `C08_DEPOSIT_native_309/full16_01..06.png` (mọi F0–95), tất cả bốn `C08_PREFIX_SILENT_encoded_309/full16_01..04.png` (mọi F0–63); mở riêng **từng full720 native F32–64**, nativeF68/F72, và **encoded prefixF63** (`all_native_frames/00064.png`). File PNG đánh số1-based, F trong report là0-based. Tự đếm đủ96/64 PNG.
- Tự SHA256 native: `32542320b20b2c6dc2dd9673c0a6bec46c904e3e23917e0620d0baecf61efc0e`; encoded prefix: `a152f5bf1b4070df58aede9c55d45226d8b5cd1ef91833e0807bd7a3d2f9a724`; START: `f68ded8001d4a93b3076921e87785d25b803c0b450a8f0fa4c3b0709a6fdc6ee`. Đều khớp hồ sơ.
- Metadata/decode theo evidence đã đọc: native720x1280/24fps/96F/4s, full_decode=true, cóAAC; prefix720x1280/24fps/64F/2,666667s, full_decode=true, **một stream video, không stream audio**. Reviewer không chạy lại decoder; hash và hình được kiểm độc lập, decode/probe là evidence của pipeline.

## Findings theo frame

| Frame | Trực tiếp thấy và kết luận |
| --- | --- |
| START/F0–15 | Khoai trái đầu khoai lốm đốm, Đào phải đầu đào/cuống/lá; bát rỗng ở tay trong Đào và cốc nâng tay ngoài. Blink Đào đầu clip mở dần khoảngF8–11; không pose/face reset rõ. A ở tips trên đúng bát đang cầm, bát riêng Khoai trên bàn. |
| F16–33 | Cùng cụm A đi xuống một đoạn ngắn; không hướng vào miệng, không trả đĩa hoặc lấy B. F32 vẫn thấy cụm trên tips ngay trên lòng bát Đào. |
| F34–39 | Cụm A hạ qua vùng rim vào lòng đúng held bowl. ĐếnF38–39 thấy A trong bát cùng tips đang ở trong bát; không có bản sao thứ hai ở tips và nơi khác. Tiếp xúc và thời điểm tips mở chính xác bị che một phần bởi food/rim, nên chỉ xác nhận một episode placement/release nhìn thấy, không chứng nhận cơ học hidden-contact. |
| F40–55 | A vẫn trong lòng bát; tips không kéo lại một cụm A, không có release lặp hoặc pickup mới. Đào vẫn cầm bát và cốc, không đổi tay. Khoai chuyển sang nụ cười nhỏ khép miệng. |
| F56–60 | Hai tips rời cụm, nâng lên trống và tách khỏi lòng/rim trong chiếu2D. A ở lại bát. Không thấy cụm food mắc theo tips. |
| F61–63 | Tips trống đã clear phía trên/trái bát, rút về Khoai; A thấy trong bát tay Đào. EncodedF63 tự xem giữ đúng state này, hai miệng khép/nụ cười, cốc còn nâng. F63 là exit phù hợp để chuẩn C09 từ exact encoded source. Đũa còn đang rút, chưa có hold dài hoàn toàn đứng yên. |
| F64–68 và F69–95 | Retract tiếp rồi bát/cốc hạ rõ từ khoảngF68 trở đi; F72 bát ở thấp hơn gần bàn, F80–95 bát/cốc rất thấp/gần bàn. Ngoài choreography giữ bowl/glass nâng của C08: **không dùng toàn4s hoặc nativeF95 làm C09START**. |

Trong tất cả boards không thấy cloneA/spare personal bowl, đổi đích nhận, ăn/đút miệng, lấyB, camera cut, identity/props reset, miệng mở thành phát âm hoặc steam. Đúng hai **bát cá nhân**, ngoài hai chén chấm: một bát Khoai trên bàn và một bát Đào cầm. Rau, đĩa nem nguội, hai chén chấm, đũa nghỉ phải và watermark được giữ. Hình nem vẫn đọc được dạng sợi/mảnh; ảnh không xác thực nguyên liệu hay nhiệt độ thực tế.

Không thấy interpenetration rõ tại phần hiển thị. Tuy nhiên underside bát/tay đỡ Đào chồng vùng resting hand Khoai ở một số frame; depth/clearance và tiếp xúc sau bát vẫn **CLEARANCE_UNKNOWN**, không dùng acceptance308 để miễn kiểm này.

## Giới hạn và cổng tiếp theo

- Đây là xem mọi still qua board cộng full critical frames, **không phát liên tục video, không nghe**. Không chứng nhận perceived rhythm/continuous motion, tiếng nói/âm nhạc/AV/lip-sync, vật lý3D khuất hoặc bảo toàn từng sợi food. ASR nếu có không phải bằng chứng reviewer đã nghe hoặc native không có thoại.
- Audio measurement309 ghi PCM khác0, max_abs0,192046/RMS0,041690; no-audioUI=true không chứng minh native im. Prefix không có audio track theo probe nên phù hợp derivative im tiếng cho nhiệm vụ no-dialogue; native được bảo toàn. Việc bỏ track không tự chứng nhận native voiceless hay final soundtrack.
- Không có blocker still MAJOR buộc retake trong prefix. Có thể chuẩn C09 **có điều kiện** từ exitF63 trích nguyên trạng của đúng encoded prefix đã hash, xác minh PNG/provenance sau trích; không redraw, không thế native tail, không coi report là duyệt unseenC09. C09 phải giữ A ở bát Đào, same hands/glass/two bowls/identity, rồi thực hiện B theo scope riêng và QC actual.
- C06–C07 được owner nhận exact bundled5s theo308; C08 prefix chưa có owner acceptance. Authority238 cho scoped work không thay owner checkpoints full rough/final. Report không chuyển ngân sách, không cấp quyền retry hoặc release.
- Theo run309: balance1015→1008/debit7; spent272/rem228, first73/retake0/post45/reserve110CLOSED. Đây là ledger được đọc, không live refresh balance độc lập.
- Timing còn OPEN: throughC07=752F; thêm prefix64F→816F/34s, còn24F/1s trong rough35s cho C09. Không hứa đủ C09B trong1s, không bỏB/tăng tốc hoặc chốt final30. Food seamC05→C06, dựng nhịp/AV toàn chuỗi và owner rough/final checkpoint còn giữ nguyên.

**Disposition:** giữ native nguyên vẹn; candidate local `[0,64)` là source/range hợp lệ có điều kiện cho C09 preparation từ encodedF63. Full native4s không đạt choreography tail; continuous AV và hidden clearance chưa được chứng nhận. Không cần paid retry chỉ từ bằng chứng still hiện có.
