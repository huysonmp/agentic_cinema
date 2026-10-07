# C01B T01 — Review actual độc lập REC246

Ngày 07/10/2026. Run C01B-T01-NATIVE-CRITIC-246. **PARTIAL_TASK_OBSERVED / HOLD_AUDIO_AND_ACTUAL_JOINS**, không native/AV/EDL APPROVED. Có diễn hướng nhìn→rời vành→thu tay trong mẫu đã kiểm; không thấy kéo/nhấc đĩa/lấy/ăn kiểu tail T04. Tuy nhiên **actual start không giữ exact pose nguồn**. Không tự retake, release hoặc chi credit.

## Exact target, nguồn và năng lực

Hash PowerShell thực:

- Native `05_native/EP01_720_C01B_T01_NATIVE.mp4`: `f7321e72c952cf849f9b5febede7fb08951c997970de82e6f8d424f54415089b`.
- Start ref `02_refs/C01B_START_from_C01A_T04_FLOW_v1.png`: `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb`, byte-identical với PNG frame80 của selected C01A cut theo preflight đã kiểm.
- C02 F0 `02_refs/C01A_F0_from_C02_T02_v1.png`: `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`.

Đọc full request T01/preflight và actual owner QC `C01B_T01_NATIVE_246/native_evidence.json`, ASR/diagnostics `C01B_T01_ASR_246`; canon236/scoped238 và limited contact exception kế thừa đã đọc. Prompt T01 là exact draft c9487… đã review; không paper PASS thành actual PASS. Technical evidence root:720×1280/24fps/96frames/video4s/audio4,032s/full decode good; reviewer tính hash, không tự probe/decode lại.

**Phạm vi trực tiếp xem:** whole overview1fps (0/24/48/72); cả2boards6fps (0,4,…92); fullframes **0–4,8–11,36,44–72 liên tiếp,95**. Tổng **52 unique native frames**, gồm dense44–72 /1,833333–3s. Zero-index; file name=index+1, last95=`00096.png`. Đã thử nhầm `00097.png`, nhận missing-file và sửa đúng95; không xem/ghi một frame96 không tồn tại. Xem toàn start ref và C02 F0. Không xem mọi96frame/continuous AV, không actual nghe; không chứng nhận khẩu hình/âm “Khoan”/voice bằng still hoặc ASR.

## Findings actual

| Finding / severity | Expected / observed và time/frame | Closure / giới hạn |
| --- | --- | --- |
| **B-START-POSE / JOIN_HOLD** | Nguồn C01A frame80: inner hand Đào hover gần cạnh trong bát, outer fingers sát/chồng vành phải. Actual B0: inner hand đã vươn trái-xuống sát phía trái đĩa hơn; outer fingers mở cong và rời/ít ôm vành hơn. Đầu clip không reset về tay nghỉ, nhưng cũng **không exact source pose**. Early0–4/0–0,166667s và8–12/0,333333–0,5s hai tay còn hướng về hai bên đĩa; mẫu36/1,5s inner fingers ở vành trái. | Mismatch actual quan sát được, không suy input hash=video start. Nguy cơ jump/new reach ở A→B cần xem actual joint. **Không selected/release join trước disposition**, không tự gắn whole-native REWORK chỉ vì không pixel-identical. Limited inner gesture ở nguồn không tự waive mọi động tác mới. |
| B-PLATE / GEOMETRY_DRIFT | B0 upper outline/food mass khác source0cf4; qua early→36/1,5s outline đĩa/khối món dịch/biến hình nhẹ, không giữ pixel-stationary. So44–72 từngframe, đĩa không đi cùng tay khi thu; đuôi72–95 không thấy nhấc/kéo về Đào như T04 tail. | **No visible gross pull/lift/take/eat observed**, không “plate absolutely stationary PASS”. Drift hình/món có thể gây pop qua cuts; layer source→take/join, phải root/DOP/CONT đánh giá trên đoạn nối. Không khẳng định có lực kéo thật hoặc first physical motion từ still. |
| B-RELEASE / OBSERVED_SEQUENCE | Mẫu36–44/1,5–1,833333s tay còn gần vành;45–47/1,875–1,958333s outer fingers bắt đầu nới/lùi;48–52/2–2,166667s khoảng rời vành rõ hơn.53–67/2,208333–2,791667s hai tay về phía bát;68–72/2,833333–3s settle/rest, giữ tới95/3,958333s. | Release→retract đọc được trên chuỗi still dày. Không teleport trong44–72, không extra hand/crossing bowl/glass thấy được. Route nâng qua vùng đũa không chứng minh clearance3D mọi frame hoặc fluidity khi chạy. |
| B-CAUSE / AUDIO_UNKNOWN | Khoai mouth mở trongboards8–20/0,333333–0,833333s, về nghỉ24/1s. Đào nhìn xuống rồi chuyển mắt lên Khoai khoảng32–36/1,333333–1,5s; release sau đó. Không cả tay đã rest ngay đầu, không thu trước các mẫu mouth event. | Thứ tự visual phù hợp mục đích; **không chứng nhận cô nghe đúng cue** hoặc causal timing audio từ still. Khoảng chờ giữa từ và release khá dài; cần actual playback/rough, không gọi chắc nhạt hoặc đạt từ timestamp. |
| B-FACE / SPEAKER | Hai mặt/miệng nhìn rõ, Khoai giữ hai tay nghỉ; Đào môi khép trong toànsamples kể cả dense44–72. Khoai mở miệng/cười ở early rồi khép ở remainder được xem. | Coverage quan sát phù hợp. Mouth event không đủ xác nhận K20/nam/only Khoai/lời chính xác, lipsync hoặc không có tiếng Đào. |
| B-SET / SERVING / TEXT | Phố mở/đèn lồng/mái bạt/phía trục giữ; bát trống, hai đôi đũa nghỉ, rau trước-trái, hai chấm và cốc ngoài phải còn. Symbol bốn điểm dưới-phải giữ; không new lettering/steam/food take trongsamples. | Không thấy repeat text/presenting kiểu C01A T02; không whole96frame guarantee. Nem/outline drift vẫn tách khỏi no-steam finding, không dùng món che lỗi nối. |
| **B-END→C02 / JOIN_UNKNOWN** | B72 và95: cả tay Đào nghỉ quanh bát trống, Khoai tay nghỉ, bát/đĩa/đũa cònF0; gaze Đào hướng Khoai. C02 F0: tay nghỉ nhưng Đào nhìn thấp hơn, mặt/pose/bát/food mass có khác nhẹ. Không swap/reset mónA vì chưa gắp. | State-compatible **không exact geometry/gaze/light match PASS**. Phải kiểm actual cut và nguyên nhân tiếp lời N02, không dissolve/cận nem/audio overlay để giấu. |

## Audio thực và boundary

Unprompted offline ASR nhận **“Khuán!”0–0,84s**, word probability0,6186; detector silence tail từ0,926583→4,032s. Đây là dấu hiệu cần nghe một từ ngắn, **không kết luận sai lời hoặc đúng K20**. ASR interval bắt đầu0 không chứng minh phonetic onset tại0; loudness threshold không chứng minh im tuyệt đối, không cấp trim/voice certificate. Gate owner nghe exact T01 root đang xử lý; chưa có acceptance artifact trong task này. Không chuyển C02/K20 hoặc C01A/D06 approval sang clipB.

Nếu audio được chấp nhận và A→B mismatch có disposition sau actual joint: **candidate rough** từ frame0 đến khoảng frame72 (tay đã rest rõ), không quyết định EDL. Inclusive0..72 sẽ là73frames/3,041667s ở24fps trước đo export, không3s duration; không cắt đầu để né jump vì có thể mất cue/lời. End-range phụ thuộc actual fullword/đường tay/join C02. Native4s và target opening4,5s không ép được: C01A3,375 + candidate khoảng3,04≈6,42s, cần phân bổ nhịp toàn phim sau media; không speed/pitch hoặc cắt phản ứng để giữ1,125s giấy.

## Disposition và bước tiếp

1. Giữ native nguyên. **Không mở paid retry từ report này.** Chưa thấy literal gross platepull T04-tail lặp ở Bsamples; đây là unit mới, start geometry/pose drift phải phân loại riêng, không tự gọi same MAJOR để stop hoặc miễn stop.
2. Root nghe qua owner đúng capability/target, lưu answer/hash; không ASR-certify “Khoan”.
3. Trước mở rộng phụ thuộc: root/DOP/ACT/EDIT kiểm **actual A→B joint** với exactC01A cut, nhất là inner-hand jump và plate/food pop. Có thể chuẩn bị rough cắt/nối miễn phí để quan sát, **không** coi đã source-closure picture final. Nếu jump phá causal action, REWORK layer source/staging/take có chẩn đoán; nếu nhỏ/chấp nhận trong quyền thì ghi disposition cụ thể, không hidden waiver.
4. Sau rangeB đạt lời/release/rest: kiểm B→C02 actual, EDL measured và rough owner AV. Không chọn lower-face/food insert hoặc audio overlay để hợp thức clip.

**Đã xác định:** native/hash;52samples, release/retract/face/serving quan sát phù hợp một phần; actual start mismatch và slight geometry drift. **Quyết định review:** HOLD audio + actual joins, không yêu cầu retake tự động hay thêm owner picture checkpoint cho từng clip. **Giả định:** đoạn0→rest có thể dùng nếu joins/âm thực đạt; chưa selected. **Còn mở:** đúngKhoan/K20, AV/phonetics/fluidity, root disposition mismatch và nhịp30s. **Bước tiếp:** exact listening + actual short rough audit rồi quyết định range/closure, không giấy hoặc still PASS thay video.
