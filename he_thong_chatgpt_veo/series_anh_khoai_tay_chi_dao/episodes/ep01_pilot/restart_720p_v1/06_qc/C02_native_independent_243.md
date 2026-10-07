# C02 T01 — Review native độc lập, REC243

Run **C02-NATIVE-CRITIC-243**, ngày07/10/2026. Mode **SAMPLED_NATIVE_FRAMES_AND_REFERENCE_COMPARISON**, không continuous playback/AV hoặc actual listening. **Disposition: REWORK_VISUAL_SCOPE / HOLD mở các cảnh phụ thuộc.** Không tự chọn take, không cấp quyền retry.

## Nguồn và phạm vi thực kiểm

Target `05_native/EP01_720_C02_T01_NATIVE.mp4`; SHA256 tính lại bằng PowerShell khớp **`5ba2878f2e59bbe03a49345217a0bccbf00b5d8c7864dac64d22cf26ceb6d4d4`**. Native evidence do root lập:720×1280,24fps,240frames, video10s, audio10,005s, full decode success. Tôi đọc evidence nhưng không tự chạy lại probe/decode. Hash/source xác định được, technical decode không chứng minh nghệ thuật hoặc đồng bộ môi.

Cold phase đã xem toàn `overview_1fps_01.jpg` (10 samples0–9s), **cả bốn** `mouth_hands_6fps_01–04.jpg` (60 samples, zero-based frames0,4,…236), và full-resolution native `00001.png`/frame0/0s, `00021.png`/frame20/0,833333s, `00049.png`/frame48/2s, `00240.png`/frame239/9,958333s. Sau đó đối chiếu actual approved `MASTER01_v5_CHATGPT_NATIVE.png` đã xem, exact prompt242 và authority242/243, mới đọc request242 hiện hành. Các boards có nhãn frame/time khớp native_evidence mapping. Tổng là61 unique frame samples đã nhìn ở cấp board/fullframe, không xem toàn240frame; riêng49.png là frame48 zero-based, không frame49.

Đọc record human master242, preview voice239 trong run trước; lần này đọc assembly-sequence243, registry243 và current request242. Quyền217/236 cho bounded reviewer actualQC, chỉ đọc local/xem evidence/viết report này. Không UI/API/Git/credit/media edits. Tôi không nghe audio, không đánh giá tiếng K20/lời/speaker thực hoặc lip-sync. Chưa có transcript/ASR trong folder ở lúc tìm; không suy heard_text từ prompt. Công cụ dựng account do root kiểm riêng, report này không xác nhận đã dùng được từ catalog.

## Cold interpretation

Hai nhân vật được giữ trái/phải; cả hai gương mặt luôn hiện trong61 samples, không cận món phủ lượt. Khoai bắt đầu nhìn xuống món, sau đó hướng sang Đào với các poses miệng mở/khép và nét cười. Đào chủ yếu nghe, nhìn anh/chớp mắt, không thấy chuỗi speech-like mouth poses rõ trong samples. Điều này chưa chứng minh ai nói bằng tiếng hoặc đồng bộ môi.

Ngay đầu clip Đào chắp hai tay trước ngực, rồi hạ xuống. Bàn giữ nem/rau/chấm/bát/đũa/cốc; không thấy gắp, ăn hoặc hơi nóng trong samples. Tuy nhiên nền đã thành một mặt tiền/tường quán có cửa cuốn, quạt và bảng “NEM BÙI”, khác rõ quán ven phố mở/đèn lồng/mái bạt của v5. Camera vẫn rộng thấy toàn thân/chân và nhiều vùng nền, không cận vừa hai mặt như packet.

## Findings expected–observed và route sửa

| Rule / disposition | Expected → observed và vị trí evidence | Mức / correction layer / closure |
| --- | --- | --- |
| C243-GEO-01 / DEFECT | Giữ cùng quán/scene v5 → fullframe0,48,239 và toàn overview: thay phố mở với mái bạt/đèn lồng bằng tường vàng/cửa cuốn, quạt hai bên, xe máy giữa sau và bảng chữ mới. Không thể giải thích chỉ bằng crop gần hơn của cùng ảnh; table relative geography còn nhưng set/background đã được dựng lại. | **MAJOR** continuity/approved visual identity. Giữ native; truy source binding→prompt→take. Request ghi cloudv5 đã verified, nhưng reviewer không kiểm UI trực tiếp. Chỉ có bằng chứng output lệch; chưa chứng minh model mechanism. Root/CTD/DOP sửa tại reference/request hoặc trình owner quyết định đổi set; không lấy C02 này làm chuẩn các cảnh sau im lặng. Closure: actual revision khớp set đã chốt hoặc owner change approval rõ scope rồi recheck dependencies. |
| C243-FRAME-01 / DEFECT | Stable medium two-shot ở face level, tay/bát/vùng đĩa dưới khung → frames0,48,239 vẫn full seated bodies/shoes/table legs, nền chiếm phần lớn trên; gương mặt đọc được nhưng attention chưa cận như thiết kế. | **MAJOR so với direction cụ thể**, không cáo buộc mất mặt. Route DOP/CTD/reference camera framing. Không crop hậu kỳ chỉ để đổi nhãn mà chưa kiểm chất lượng/đạo diễn, và không phủ món. Closure actual framing đủ nhiệm vụ; nếu owner chấp nhận rộng phải ghi thay đổi có lý do/ảnh hưởng thay vì báo prompt complied. |
| C243-ACT-01 / DEFECT | Cả hai hands rest/F0 xuyên shot, nối sau C01B đã thu tay → frame0–16/0–0,666667s Đào chắp tay trước ngực; frame20/0,833333s đang hạ, tới frame24/1s tay nghỉ. Full00001/00021 xác nhận. | **MAJOR ở head-state matching; đoạn lỗi khu trú**. ACT/EDIT kiểm tiếng onset actual trước xét range bỏ phần đầu. Chưa nghe nên không xác nhận có handle đủ để trim. Không bỏ âm “Mùi” hoặc ép timing để sửa. Closure measured selected range/audio/state khớp hoặc source revision; C01B không bị viết lại để hợp thức cử chỉ này. |
| C243-TEXT-01 / NEW_BACKGROUND_TEXT | Masterv5 không có bảng món, generation prompt không yêu cầu caption → bảng “NEM BÙI” và các dòng mờ xuất hiện nền tại0/2/9,958s. | **MINOR riêng chữ; thuộc MAJOR set change ở GEO-01**. Không đọc/diễn giải các dòng mờ thành claim. Không thấy brand cụ thể đã xác định; đừng gán tên nhà hàng. Root/Fact/ART kiểm nếu giữ; không tự xóa watermark/text hoặc coi đây là chữ F01/F02/disclosure đã hoàn tất. |
| C243-FACE-ID-01 / MET trong samples | Khoai trái/Đào phải, mặt/miệng không bị che → tất cả samples giữ; hình khoai vàng/mày dày và đào/cuống/lá/wardrobe phù hợp. | Không thấy MAJOR identity regression trong vùng nhìn. Không pixel-identical hoặc full240frame guarantee; vẫn cần actualAV/mouth attribution và chọn range đúng. |
| C243-LISTENER-01 / SAMPLED_MET; AV_UNKNOWN | Đào nghe không nói → samples mặt chủ yếu môi khép/nhìn anh/chớp mắt; không thấy miệng phát âm thay rõ. | Chưa nghe nên không voice/speaker/lip-sync PASS. SIA/owner nghe toàn lượt, kiểm sync và boundary “Hồi bé” trên exact native. |
| C243-F0-FOOD-01 / SAMPLED_MET ngoài head-hands finding | Không gắp/đũa nghỉ/bát trống/nem nguội → samples giữ hai bát trống, hai đôi đũa bàn, một đĩa nem và rau/chấm/cốc; không miếng trên tay, no visible steam. | Không xác nhận mọi frame hoặc đũa grip action chưa xảy ra. Food identity visible tương thích material miếng/dải áo bột, không chứng minh công thức. State/camera/amount cần so joins thực. |
| C243-LIGHT-01 / SAMPLED_READABLE | Warm light đọc mặt/miệng → sampled faces đều rõ, bóng không che miệng. Nền đổi loại ánh sáng quán. | Không thấy blocker exposure trong samples; không kết luận không flicker continuous. Warm tone không tự đóng set mismatch. |
| C243-END-01 / CANDIDATE_STATE_ONLY | Đuôi đủ lời→môi khép/F0/listener curious → frame192–239/8–9,958s Khoai môi khép/cười nhẹ và tay nghỉ, Đào chú ý. | Không đo audio tail thực, chưa selected range/EDL. Không gọi finalmouth rest là lời đã hết hoặc đã đúng nhịp. EDIT chọn range sau actual listening, giữ âm cuối “chờ”. |
| C243-TECH-01 / EVIDENCE_MET | Native720p9:16/24fps10s đúng request → evidence240frames720×1280, hash thực khớp. | Technical evidence không bù GEO/FRAMING/ACT defects; AV identity/timing vẫn UNKNOWN. |

## Đối soát request sau cold phase

Request242 ghi ảnhv5 cloud `737ec0aa-d1a2-45e5-8f94-b2694c1d1ac3`, một K20 `b447b35c-b35e-4140-af72-ecd277282b1a`, không D06; prompt hash242; Ingredients/Omni1.1Flash/720p/9:16/10s/x1/AgentOFF, full quote15 và một submit theo243. Tôi không mở UI để chứng thực lại fields. Trạng thái JSON lúc đọc còn `AWAITING_OUTPUT`; native hiện đã có bằng chứng riêng nên root cần đồng bộ trạng thái, không coi field cũ là không tồn tại file.

Không có maker winner rationale được dùng để khởi đầu review. Lỗi tại take không có bằng chứng buộc tuyển giọng lại, thay lời hoặc dùng Quality. Giả thuyết model tái dựng set từ diễn giải scene/Ingredients chưa được chứng minh; phải lưu exactinputs/config trước sửa. Scene drift có thể liên quan ngữ nghĩa prompt, khả năng reframe hoặc conditioning, nhưng chỉ output quan sát không đủ xác định nguyên nhân duy nhất.

## Handoff

- Đã xác định: native thật/hashes, mặt có coverage, F0 món giữ trong samples, có set/framing/head-hand defects cụ thể.
- Đã chốt trong review: **REWORK_VISUAL_SCOPE**; không retain-as-approved hoặc mở C01A mặc định. Owner/root quyết định lựa chọn và request tiếp theo riêng.
- Giả định: head gesture có thể trim nếu âm chưa bắt đầu; **chưa được xác minh**, không giải quyết nền/khung rộng.
- Còn mở: tiếng/lời/giọng/AV actual, selectedrange/timing, cause chain và Flow trim/export thực.
- Bước tiếp: root trình gọn ba lỗi hình và phạm vi chưa nghe; đóng nghe/assembly để phân biệt khả năng tool với chất lượng take; sửa đúng source/request/direction được chốt rồi kiểm lại exactnative. Không autorun từ report; sameMAJORtwice thì dừng chẩn đoán theo238.

**Không ACTUAL_LISTENING, FULL_AV, voice identity/lip-sync PASS, full-film/30s hoặc release approval.**
