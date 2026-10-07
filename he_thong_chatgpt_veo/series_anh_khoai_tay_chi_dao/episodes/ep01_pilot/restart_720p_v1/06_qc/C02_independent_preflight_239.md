# C02 — Phản biện độc lập trước sản xuất, REC239

Run **C02-CRITIC-239**, ngày 07/10/2026. Vai reviewer độc lập, không làm maker của prompt hoặc bốn báo cáo đạo diễn. Mode **COLD_PAPER_AND_STATIC_REFERENCE_REVIEW_THEN_INTEGRATION_CHECK**.

**Verdict: PAPER_PASS_CONDITIONAL cho logic của draft239 trên input v2 đã đọc; SUBMIT_HOLD.** Đây không phải approval dùng v2, không generate-ready và không PASS hình–tiếng. Owner đã chọn **“Sửa khung ảnh master trước khi chạy C02”**: v2 phải thay phiên bản, rồi kiểm lại phần phụ thuộc; không mang verdict này sang v3 tự động.

## 1. Input, thứ tự đọc và giới hạn

Đã đọc đầy đủ PROD7/02 common runtime, DIRECT01 operating model, hồ sơ217/236/238, quyết định scoped-autonomy238, thoại178 C-v0.6 và storyboard214. Trước khi đọc rationale makers, đã đọc exact `04_requests/C02_prompt_239.txt`, request preparation239 và voice-approval239, trực tiếp xem toàn ảnh native MASTER01 v2, tính lại hash bằng PowerShell. Sau cold review mới đọc đầy đủ gói tích hợp239 và bốn báo cáo DIR/DOP/ACT/EDIT239. Đã đọc bindings238 cập nhật239, static reviewer238, lesson239 và quyết định mới `00_decisions/master-reframe-239.json`.

| Target thực kiểm | SHA256 thực tính |
| --- | --- |
| `02_refs/MASTER01_v2_NATIVE.jpg` | `239e91f53e00de3caeb7d9153c473b6ae4aadcb70945dfe5462a6b8a2d52115f` |
| `04_requests/C02_prompt_239.txt` | `d60cd53a64e9284f0fc5e4c9faca3ecb5a0e18e7d570aa1bfcf320100f2c54ca` |

Quyền217 cho bounded local reviewer task;238 cấp quyền giới hạn cho root, không chuyển quyền chi sang reviewer. Run này chỉ đọc tài liệu, xem ảnh tĩnh và viết report được giao. Không browser/API/Git/generation, không sửa inputs hoặc approval. Tôi không kiểm UI trực tiếp, không nghe preview/audio, không có native C02, waveform, continuous video, AV, source ranges hoặc EDL thực. Metadata768×1376 lấy từ hồ sơ static238, không coi là metadata video mới. Chưa tự đối chiếu ảnh nem thật trong run này; closure chất liệu món kế thừa report238 đúng hash, không nhận là kiểm độc lập mới về food authenticity.

## 2. Cold interpretation — trước rationale

Prompt cho thấy một lượt Khoai kể ký ức với Đào tại bàn hiện tại. Khung cận vừa hai người cố định, không minh họa bếp/mẹ hoặc cận món. Ánh nhìn từ món sang bạn là chuyển chú ý chính; Đào nghe, không nói. Hành động tay bị giữ ở F0, chưa có cú gắp hoặc vẻ ăn vụng. Draft không biến ký ức thành claim vùng miền.

Ảnh actual v2: Khoai trái, Đào phải; đủ hai gương mặt, mắt và miệng; bốn tay nghỉ, bát riêng trống, hai đôi đũa trên bàn, nem ở đĩa giữa. Không thấy khói quanh món. Rau trước trái bị cắt biên; cốc ngoài phải sát biên. Ảnh này không chứng minh framing cận vừa, chuyển mắt, giọng hoặc khẩu hình của output chưa tồn tại.

Lời duy nhất trong prompt khớp phần N02 được tách tại236:

> Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.

Không có “Khoan”, N03 hoặc mẫu audition trong block lời. Tên custom voice trong prompt khớp bindings; ID K20 mới trong request preparation là `b447b35c-b35e-4140-af72-ecd277282b1a`, khác ID D06 `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`. Request ghi một voice chip, không Đào. Đó là tính nhất quán hồ sơ, chưa là readback UI hoặc tiếng thực do tôi kiểm.

## 3. Coverage, findings và cách đóng

| Rule / status | Expected → observed | Mức / hành động và closure |
| --- | --- | --- |
| PF-TEXT-01 / MET trong paper | Chỉ phần N02 của Khoai, không lặp “Khoan” → exact prompt đúng178/236, không thêm lời audition/câu Đào. | Không thấy defect paper. SIA/owner vẫn phải nghe trọn native mới, đặc biệt boundary “Hồi bé” và âm cuối “chờ”. |
| PF-BIND-01 / PAPER_MET; LIVE_UNKNOWN | Một K20 mới → tên/ID khớp voice approval239/bindings, hồ sơ ghi chỉ một chip. | MAJOR nếu binding/output sai. Root đọc lại picker/chip/prompt cuối; actual listening và attribution kiểm sau sinh. Cùng ID không bảo đảm identity giọng trên output. |
| PF-FACE-01 / DESIGN_MET; MEDIA_UNKNOWN | Mặt/miệng Khoai xuyên lời, Đào nghe → prompt yêu cầu đủ hai mặt, không cutaway/turn che miệng; still có hai mặt rõ. | MAJOR nếu output mất mặt hoặc Đào diễn nói. Kiểm toàn lượt trên native, phạm vi xem/nghe thực và mẫu miệng dày; không coi board tĩnh là FULL_AV. |
| PF-STATE-01 / STILL_MET; MOTION_UNKNOWN | F0→F0, không gắp/khói → still phù hợp và prompt khóa tay/đũa/bát/món. | MAJOR nếu take gắp sớm/reset/khói. CONT/FOOD kiểm state đầu–giữa–cuối và chuyển động, không lấy negative prompt làm closure. |
| PF-COVERAGE-01 / PAPER_MET | Cận vừa hai người không dời serving → prompt cho ngoại vi ngoài coverage nhưng giữ geography. Phù hợp236 và DOP; không xung đột với yêu cầu master đầy đủ serving. | C02 không chứng minh count/position của props không nhìn thấy. CONT phải ghi giới hạn và so khung chung tiếp theo; không miễn QC bằng việc crop. |
| PF-TIME-01 / UNKNOWN, không là lỗi take | Sinh10s và slot8,5s chỉ target → makers/integration không bịa EDL hoặc ép speed/pitch. | Native chưa có; đo thoại/handles/ranges và joins thật. Nếu không vừa, trình conflict, không cắt lời hoặc phủ món để lấp. |
| PF-OWNER-01 / BLOCKER hiện hành | Master phải accepted trước C02 → owner chọn sửa khung, `master-reframe-239.json` xác nhận v2 không accepted và submit hiện không allowed. | **SUBMIT_HOLD**. Giữ v2 lịch sử; tạo/sửa v3 chỉ khi quote ảnh0 đúng scope, review actual/hash/geography/F0/food/margins, owner chốt input mới. |
| PF-VERSION-01 / STALE_DEPENDENCY | Packet/prompt phải bám master được chọn → draft239 và phần pending trong các báo cáo vẫn chỉ v2; decision mới supersedes “chờ chấp nhận minor”. | Rework binding/phiên bản trước submit. Cập nhật request/prompt/packet và registry theo quyết định, tính hash mới, kiểm lại phần bị ảnh hưởng. Không tự sửa báo cáo lịch sử thành đã review v3. |
| PF-QUOTE-01 / UNKNOWN_FINAL | Đủ inputs/config/quote live≤15 → hồ sơ có quote15 khi prompt trống, explicitly không final. | **SUBMIT_HOLD** tới screenshot/readback đầy đủ sau mọi chỉnh prompt/chip: đúng model/mode/720p/9:16/10s/x1/Agent OFF, giá và trần còn hợp lệ. Quote cũ không cấp quyền request mới. |
| PF-ASSEMBLY-01 / UNKNOWN_ACCOUNT_CAPABILITY |236§13 yêu cầu kiểm đường dựng trước chi clip → chỉ có catalog Stringout Creator; mở template tạo remix; chưa trim/arrange/linked-audio/export thực. | **HOLD readiness sản xuất theo plan**. Root kiểm chức năng thật trên account, nêu chính xác phần thiếu/route cần owner quyết định. Không gọi catalog là Scenebuilder đã dùng được hoặc ghép miễn phí. Không tự chạy tool giá UNKNOWN hay đổi route local. |
| PF-SIDE-EFFECT-01 / OBSERVED_IN_ROOT_LOG, không trực tiếp UI | Điều tra công cụ không nên bị gọi hoàn toàn read-only → lesson239 ghi UI đã tự tạo remix, không chạy/xóa. | Root giữ tên/ID và log side effect nếu lấy được; không xóa hoặc coi đó là clip/export. Việc ghi rõ giới hạn là đúng; chưa có bằng chứng phát sinh chi. |
| PF-FACT-01 / N/A generation-only | Không claim/caption mới → prompt chỉ fiction ký ức, không có fact text. | Không thay final Fact/disclosure/readability gate. Claims F01/F02 và nhãn AI vẫn kiểm khi finishing/export. |

Không thấy xung đột cần thay lời, tuyển giọng lại hoặc bỏ mặt để prompt khả thi hơn. Không có bằng chứng dự báo xác suất thành công, sức hút khán giả, timing, voice identity, lip-sync hoặc đủ30s. Các lỗi MAJOR có điều kiện ở bảng là tác động nếu output mắc lỗi, không cáo buộc một video chưa được tạo.

## 4. Kiểm integration sau cold phase

DIR ba beat ký ức→chi tiết→câu hỏi; DOP camera cố định hai mặt; ACT mức R; EDIT paper A liên tục được prompt giữ đúng ý. Không chồng lựa chọn R/E hoặc A/B; không giả cả bốn makers đã nghe/xem actual. Các số giây chỉ target. Serving ngoài coverage là phân biệt scene geography với vùng nhìn, không mệnh lệnh dời rau khỏi bàn.

Điểm cần chỉnh duy nhất từ quyết định mới là **không tiếp tục coi v2 là candidate có thể được miễn minor để submit**. Packet hiện ghi “owner duyệt exact v2” là trạng thái lúc viết; decision reframe đã supersede. Logic thoại/diễn/framing có thể tái dùng sau revalidation, nhưng artifact/hash/binding và scope actual reference phải đổi đúng v3. Bốn báo cáo v2 không tự trở thành phản biện v3.

## 5. Handoff và tổng hợp

1. Đã xác định: draft239 nhất quán câu–speaker–voice hồ sơ, hai mặt/F0 trong still v2 và camera/performance/edit trên giấy; chưa có C02.
2. Đã chốt: owner giữ hai preview voice; owner yêu cầu sửa khung master trước C02. Reviewer không tự duyệt input hoặc output.
3. Giả định: Ingredients có thể chuyển framing và diễn từ master mới; chưa chứng minh, không gán xác suất.
4. Còn mở: v3/hash/owner acceptance; impacted paper review; full-input UI/config/quote; năng lực dựng account; mọi actual timing/giọng/miệng/chuyển động/joins.
5. Bước tiếp: root sửa master đúng scope0credit, kiểm hồi quy và trình owner; rebind/review packet phiên bản mới; đóng tool/quote gates. Chỉ sau đó một C02 theo238, rồi QC native và human checkpoint C02 trước mở C01A.

**Không MEDIA PASS, không AUDIO_SELECTION/ACTUAL_LISTENING, không FULL_AV, không generation-ready hoặc release approval trong report này.**
