# REC221-PICTURE-R1 — Coverage hình N02 A/B/C

Ngày: 2026-10-06, Asia/Saigon. Scope: SAMPLED_FRAMES + native boundary inspection + read-only hash/PTS. **REVIEW_COMPLETE trong scope ảnh; HOLD speech-linked coverage, meaningful performance, lipsync, actual listening và full AV.** Không chọn final take, không production PASS. Đây là review ba output thực batch221, không là tiếp tục tự duyệt proposal218.

## Inputs, quyền và cách kiểm thực tế

Authority workflow217/220/221 và dispatch bounded picture review sau batch owner duyệt. Chỉ viết report này bằng apply_patch; không generation/browser/spend/delegation/install/git, không sửa native, không dựng hoặc đổi audio. Không đọc CONT/SIA review221 trước viết. Root có gửi factual hints về B cut7s và C chữ/A dish; kết luận bên dưới được đối chiếu trực tiếp bằng boards/native frames, không dùng hints làm evidence duy nhất. Đã đọc main220/221, report218/04 và criteria214 R02 (criteria214 đã đọc toàn bộ trong lượt218 cùng context).

Targets dưới `C:/Users/PC/Downloads/du_an_nem_bui/221_n02_pa_v_trial/`. Đã đọc `inspection/inspection.json` đầy đủ; xem thực ba `inspection/N02_{A,B,C}_NATIVE/contact-0.5s.png` (20 samples/board). Root trích240 frame/take; reviewer **không xem hết240**. Đã xem riêng native JPG trong `inspection/N02_{A,B,C}_NATIVE/all_frames/frame-NNNN.jpg`:

- A:68/69/70,143,156,163/164/165/166/167/168/169,175/176,191,200/201/202 (18 ảnh riêng).
- B:71/72,143,156,163/164/165/166/167/168/169,175/176/177,191 (15 ảnh riêng).
- C:48–72 liên tiếp;95–108 liên tiếp;143,156;163–169 liên tiếp;174–177 liên tiếp;191 (53 ảnh riêng).

Boards và ảnh riêng có mẫu trùng; không cộng60 board samples+86 JPG thành146 frames duy nhất hoặc video playback. Dải6–8s có các cụm consecutive frames quanh cut168 và176, không kiểm từng frame toàn khoảng này. Sampling không loại trừ một-frame artifact ngoài mẫu, chuyển gaze/mouth ngắn, listener speech/motion sai giữa mẫu hoặc lỗi voice. Dùng PowerShell đọc JSON/Get-FileHash, FFprobe read-only show_frames PTS; FFmpeg `select=gt(scene,0.25),showinfo -an -f null -` cho cut hints, không tạo media mới. Threshold không là semantic detector; boundary thực xác minh bằng cặp JPG trước/sau.

| Target | SHA-256 trực tiếp, khớp inspection | Probe/PTS scope |
|---|---|---|
|N02_A_NATIVE.mp4 |`35c1a0e527bf4171d8d92ed530f2058d5f7c0c005f372ff6d2f68dacbf524537` |240 frames,24fps; video10,000s/audio10,005s theo inspection; FFprobe trả240 PTS |
|N02_B_NATIVE.mp4 |`660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535` |Như A; PTS native xác nhận f168=7,000000s |
|N02_C_NATIVE.mp4 |`9bd637ed26b953d8ea87019c1fa93c1d09228551240f3b85be98815fbd2a494d` |Như A; PTS native xác nhận f176=7,333333s |

Time convention0-based, t=n/24, range in-inclusive/out-exclusive. Cut time dùng native PTS, không timestamp board. Một ví dụ cần tránh: C board nhãn4,000s đã hiện chữ nhưng native f96=4,000s không chữ; f97=4,041667s có chữ. Timestamp0,5s trên board là guide sampling, không exact EDL/onset.

Không nghe targets hoặc AUDIO_REVIEW.wav, không xem continuous visual/full AV. Audio measurements trong inspection đã đọc nhưng không dùng Pearson/hash PCM khác nhau để xác nhận thoại/giọng hoặc áp timing ASR cũ lên tiếng output mới. Actual speech-end từng output **UNKNOWN** trong scope này. Không gắn “Hồi bé”, “chờ” vào frame chỉ vì script/subtitle hoặc source ASR.

## Kết quả coverage và cut logic theo output

Criteria214 R02: “Cận vừa Khoai thấy đầy đủ mặt/miệng; ánh nhìn đi từ món lên Đào khi chia sẻ ký ức, nét cười kín”; F0→F0; cắt theo chuyển chú ý/kết ý. Khóa221 yêu cầu Khoai hiện mặt/miệng qua hết lời, Đào nghe im lặng, tay nghỉ/không gắp. PA cận qua hết final word và broader visible-face coverage là hai tiêu chí khác nhau: two-shot còn mặt Khoai không được gọi offscreen; nhưng vẫn cần kiểm xem cut có đúng diễn/ý và phù hợp direction214.

| Target / measured segmentation hoặc observations | Coverage sampled / gaze / listener / outfit | Cut logic và disposition |
|---|---|---|
|**A:** [0,69) two-shot, [69,168) cận Khoai, [168,201) dish, [201,240) two-shot; cuts f68→69=2,875s, f167→168=7,000s, f200→201=8,375s |Khoai full mặt/miệng ở cận qua f167; f168/f169/f175/f176/f191/f200 không có mặt. Dish có nhánh lá đỉnh. Samples two-shot có Khoai trái/Đào phải, áo khoác xanh sẫm/áo sáng và Đào áo sáng/nơ hồng; tay nghỉ. Không thấy Đào nói trong samples two-shot nhưng chưa xác minh silent toàn take |Vùng offscreen33frames=1,375s vẫn tồn tại; source cũ offscreen37frames bắt đầu6,833333s. A chỉ dịch cut muộn4frames (1/6s), chưa giải quyết PA mặt qua hết ký ức. Coverage structure **REWORK**; overlap với speech/output “chờ” cần actual AV, không xác nhận từ ASR cũ. Cận món vẫn không có motive đã được duyệt để phủ đuôi ký ức |
|**B:** [0,72) two-shot, [72,168) cận Khoai, [168,240) two-shot; cuts f71→72=3s và f167→168=7s |Full mặt/miệng Khoai trước/sau cut7s. f163–167 cận thấy miệng; f168/f169 two-shot anh miệng mở, f175/f176/f177 môi khép, f191 tay nghỉ/hai người nhìn nhau. Đào ở mép khung trước, đủ mặt sau; samples môi cô khép. Trang phục/vị trí giữ trong samples |Không có dish/offscreen trong samples toàn take và cụm native inspected. Sửa được **mất mặt do cut món** ở mức sampled structure, nhưng chưa đủ xác nhận giữ cận PA qua final word hoặc lời/khoảng nói đúng. Cut7s có thể đưa tương tác nghe trở lại; actual meaning/transition cần nghe-xem. **HOLD / candidate đưa checkpoint**, deviation cận→two-shot cần DIR/owner disposition khi tích hợp coverage. Không reject vì “early cut” từ source ASR7,34 |
|**C:** f48–52 clean two-shot, f53–63 blend/ghost overlay, f64 clean cận; cận tới f175, f175→176 hardcut7,333333s trở lại two-shot. Chữ xuất hiện f97 (4,041667s), còn ở f175 (7,291667s), mất ở f176 |Giữ full mặt/miệng Khoai ở samples6–7,291667s; không dish trong samples. f53–63 chồng two-shot với cận: hai vị trí mặt/mắt/miệng và bàn cùng hiện, giảm khả năng đọc người nói. Cận chủ yếu mắt gần camera; two-shot sau176 hướng sang cô. Outfits/vị trí/tay nghỉ nhất quán trong inspected samples |Broader face coverage cải thiện; **REWORK** bởi burned-in chữ ngoài nhiệm vụ và blend mặt. Exact observed blend [53,64) có11frames=0,458333s ở mức visual noticeable boundary; không xem playback để kết luận transition mượt. Cut7,333333s chưa được nhận là đúng sau từ “chờ”. Không dùng chữ làm chứng minh âm thanh đúng |

Segmentation A/B được boundary frames và scene hints xác minh. C dissolve không được scene threshold phát hiện như hardcut; tôi xem từng f48–72 để xác định vùng hai hình chồng nhau có thể thấy. Không tuyên bố toàn pixel trước53/sau63 hoàn toàn không có blend ở ngưỡng nào; range[53,64) là vùng visually noticeable đã quan sát. Chữ C đọc được: “Hồi bé, mẹ rang gạo, anh đứng chờ.” ở f97–108 và các mẫu143/156/163–169/174/175; **chưa xem từng frame109–142 hoặc144–155**, nên onset97 và removal176 là boundary confirmed, không claim tất cả79frame luôn có cùng chữ không đổi. Chữ không che miệng trong inspected samples, nhưng là thay đổi output ngoài nhiệm vụ picture repair và không sửa khả năng nghe.

### Gaze, lips visible và meaningful performance

Trong cả ba, cận Khoai có full mouth visibility và nhiều mẫu miệng mở/khép. Eyes ở board3/3,5/4/4,5s và native cận gần cuối thường hướng gần camera; two-shot đầu/đuôi hướng qua Đào. B f167→168 đổi từ cận gần camera sang hai người nhìn nhau; C tương tự f175→176. Đây là mẫu cho **risk địa lý gaze**, chưa chứng minh ánh nhìn liên tục từ món lên cô đúng lúc anh nhớ. Không lấy mở miệng, một nụ cười, hoặc nhìn nhau ở tail làm bằng chứng kể ấm/nhớ mẹ/tò mò có ý nghĩa liên tục. Đào bị crop khỏi cận là giới hạn bố cục chứ không là lỗi biến mất/đổi outfit; listener silent toàn câu chưa kiểm khi cô ngoài frame.

Không có gắp A/đưa bát sớm trong inspected samples; tay hai người nghỉ ở two-shot/cận. Điều này hỗ trợ F0 ở các mẫu, không kiểm continuity toàn take hoặc thực tế không một hành động ngắn xen vào giữa mẫu. Mặt đã được giữ trong B/C không tự chứng nhận lipsync phù hợp K20 hoặc đúng người thật sự nói. Batch cùng prompt/source không là thử đa biến; chưa có bằng chứng “B diễn tốt hơn C” hoặc rating cảm xúc/retention.

So source216 theo exact old ranges [0,72),[72,164),[164,201),[201,240): A giữ cơ chế món nhưng dịch cut; B bỏ đoạn món, mở rộng two-shot; C bỏ đoạn món, kéo cận tới176 nhưng thêm blend/chữ. Không áp old ASR timestamp6,76/6,94/7,34 vào output221. Speech alignment mới và hearing phải quyết định overlap/safety; broader face coverage B/C có thể có thật dù PA cận cuối chưa được chứng minh.

## Findings và đường đóng

| ID / rule / status / severity | Evidence thực / impact / uncertainty | Action / closure |
|---|---|---|
|PIC221-F01 / A face coverage / DEFECT / MAJOR |A f167→168 và200→201: dish offscreen7–8,375s, vẫn thiếu mặt trong range structure. Speech overlap chưa xác minh |Không chọn nguyên A cho PA; nếu đề xuất cut/coverage khác cần artifact/ranges/hash mới và actual AV. Closure phải hiện mặt qua actual lời và có narrative reason, không sửa chữ/che audio |
|PIC221-F02 / B return to two-shot / MET sampled visible-face; UNKNOWN final-word/coverage intent / MAJOR gate |B cut7s vẫn full mặt/miệng Khoai, Đào nghe trong inspected samples. Chưa biết output speech-end hoặc đúng mouth sync |DIR/EDIT tích hợp cận→two-shot diff, actual listening/AV kiểm toàn “Hồi bé…chờ” và cut; owner checkpoint nếu giữ variation. Không tự bác B vì cut trước7,34 cũ; không tự approve B |
|PIC221-F03 / C unrequested typography / DEFECT / MAJOR |Native96→97 xuất hiện chữ;175→176 biến mất. Source visual repair không yêu cầu burned captions; word text không chứng minh voice |REWORK current C; không crop/mask tự làm master. Closure source/version sạch chữ hoặc exact owner exception sau review, recheck phụ thuộc toàn target |
|PIC221-F04 / C transition face readability / DEFECT sampled / MAJOR |C f53–63 chồng vị trí mặt/mắt/miệng giữa hai scale; f52/f64 clean. Thiếu reason kể để blend hiện tại→hiện tại; meaningful playback chưa kiểm |ACT/PERF/EDIT xem continuous transition và paper rationale; artifact mới sửa readable transition hoặc owner exception đúng scope. Không coi detector không ra cut là không lỗi |
|PIC221-F05 / gaze/remembering/listener / UNKNOWN / MAJOR gate |Cận mẫu hướng gần camera, tail hướng nhau; listener ngoài crop/khép môi ở samples không xác minh silent. Môi visible≠lipsync |Continuous silent+fullAV trên từng candidate/hash; ACT/PERF/SIA đúng capability. Closure có timecodes actual gaze/listener/mouth/diễn, không report vẫn |
|PIC221-F06 / output text/voice/timing preservation / UNKNOWN / MAJOR gate |Chưa nghe trong review; inspection có PCM không equal nhưng không là diagnosis. Old ASR không current evidence |SIA/AV review actual outputs so approved source, whole turn và actual word endpoint. Không chồng audio cũ/retime để giả giữ. Closure heard/reference/fullAV logs+owner checkpoint |

Hash/PTS MET chỉ là integrity, không bù MAJOR. A và C có defects quan sát trong scope; B là candidate có lợi thế coverage sampled, chưa winner. N02 chưa formal G2 PASS, R01/N03/narrative joins và whole30s chưa được kiểm bằng report này.

## Handoff năm mục

1. **Đã xác định:** rehash ba targets khớp inspection; A dish7–8,375s, B two-shot từ7s vẫn có mặt, C two-shot từ7,333333s và có chữ/blend đã xác minh native. Đã phân biệt offscreen coverage với nhiệm vụ giữ cận/diễn ý nghĩa.
2. **Quyết định đã chốt:** kế thừa217/220/221 và214; không chọn final output. Không thêm quyền generation/retake hoặc tự sửa native. Không đổi lời hay dùng source ASR làm output timing.
3. **Giả định đang dùng:** n/24 khớp FFprobe PTS; board chỉ sampling guide; exact audio preservation/word-end/acting chưa xác minh. Full-mouth samples là visible criterion, không âm/AV đạt.
4. **Còn mở:** actual speech-end từng take; lipsync/giọng/speaker/listener thật; gaze/nhịp có nghĩa; B coverage deviation disposition và C clean source; continuity source/whole film thuộc scope khác. Không đọc trước CONT/SIA để làm đáp án.
5. **Bước tiếp:** root tích hợp reviews độc lập; ưu tiên actual hearing/AV B để phân biệt sửa offscreen với đáp ứng PA/ý đồ, trình findings đúng hash tại checkpoint G2. A/C current defects giữ mở, không tự retry hoặc bỏ shot/mặt để né lỗi. Nếu cần thay/sinh tiếp, scope/quote/output/criteria và owner approval riêng.
