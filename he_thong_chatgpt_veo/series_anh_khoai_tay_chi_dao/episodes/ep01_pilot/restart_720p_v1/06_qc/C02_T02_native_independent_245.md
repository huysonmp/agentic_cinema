# C02 T02 — Review native độc lập, REC245

Run **C02-T02-NATIVE-CRITIC-245**, ngày 07/10/2026. Mode **SAMPLED_NATIVE_FRAMES + REFERENCE + OFFLINE_TEXT_EVIDENCE**. **Disposition: RETAIN_CANDIDATE_WITH_TAIL_EDIT; HOLD_ACTUAL_AV_AND_OWNER_CHECKPOINT.** Không duyệt nguyên clip 10 giây, không tự khóa EDL, không cấp quyền T03.

## Nguồn và phạm vi thực kiểm

Target owner `05_native/EP01_720_C02_T02_NATIVE.mp4`, tương ứng native repo cùng tên. SHA256 tính lại bằng PowerShell: `2f20ec53b20cf3dea2eb48ee0c3f76913ce8a4da45f05ebf24dc33587a9ed297`, khớp dispatch/request. Reference actual `02_refs/C02_MEDIUM_v1_CHATGPT_NATIVE.png` đã xem lại; hash thực `c0ec77283233b4b4f49c172697f8c7b42fd2a7cc4bf3960670723b1a871fd0a7` khớp.

Evidence owner ở `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/06_qc/C02_T02_245/`: đã đọc đầy đủ `native_evidence.json`; đọc full prompt/request245, report243/244 và audioapproval244 sau cold visual phase. Contracts PROD7/DIRECT/217/236/238 và canon178/storyboard214 đã đọc đầy đủ trong các run trước của reviewer này. Không UI/API/Git/credit/media edit.

- Xem toàn overview 1fps: 10 samples, zero-based frames 0,24,…216.
- Xem cả bốn boards mouth/hands 6fps: 60 samples, frames 0,4,…236.
- Xem full-resolution PNG tương ứng zero-based frames **0,48,172,176,179,180,181,182,183,184,186,188,192,196,200,204,208,212,239**. Filename = frame + 1, ví dụ `00183.png` = frame 182 / 7,583333 giây.
- Tổng **66 unique frame samples**, không continuous playback hoặc xem đủ 240 frames. Đặc biệt đã kiểm fullframe quanh 7,167–7,750 giây và các mốc 7,833–8,833 giây; không khẳng định từng frame trong cả đoạn đều đã nhìn.
- Native evidence của root: 720×1280, 24fps, 240 frames, video 10,000 giây, audio/container 10,005 giây; decode thành công. Reviewer đọc evidence, không tự probe/decode lại.

**Không actual listening; không voice identity, speaker attribution hoặc lip-sync PASS.** ASR/silence dưới đây chỉ là dữ liệu offline bằng văn bản, không thay owner nghe native.

## Findings và lớp xử lý

| ID / mức | Expected → actual evidence | Closure / lớp xử lý |
| --- | --- | --- |
| C245-GEO / SAMPLED_MET | Giữ phố mở của medium244 → overview, fullframes 0/48/239 và boards giữ chiều sâu con phố, đèn lồng, mái bạt đỏ-cam bên phải. Không thấy tường/cửa cuốn/quạt/bảng quán mới của T01. | **GEO-01 MAJOR của T01 không lặp trong samples.** Không cam kết mọi background pixel hoặc frame chưa xem. Kiểm continuity các shot sau theo master/reference, không lấy tên “quán phố” làm đủ bằng chứng. |
| C245-FRAME / SAMPLED_MET_WITH_MINOR_VARIATION | Cận vừa hai mặt/tay/bát → cả hai mặt và miệng rõ; không legs/shoes/table legs như T01, không cận món che lượt thoại. Native có hơi nhiều bàn/phần dưới hơn reference, không phải khung pixel-identical. | **FRAME-01 MAJOR của T01 không lặp.** Sai biệt nhỏ cỡ khung cần đạo diễn/root xem cùng assembly; không gọi “exact framing” đã chứng minh. Không cần tự tái sinh chỉ vì sai biệt này. |
| C245-HAND / SAMPLED_MET | Bốn tay nghỉ riêng từ đầu → fullframe0 và mọi board sample giữ tay trên bàn; không chắp tay trước ngực/thu tay đầu shot như T01. | **ACT-01 head-state MAJOR của T01 không lặp trong samples.** Không chứng nhận toàn 240 frames hay joins với C01B chưa dựng. |
| C245-ID-FACE / SAMPLED_MET | Khoai trái, Đào phải, cùng identity/wardrobe, mắt/miệng đọc được → giữ trong samples; head/eyes Khoai chuyển về Đào, cuối môi khép/cười nhẹ; mặt Đào không bị món hoặc props che. | Không pixel-identical hoặc actual acting/AV approval. Không mất mặt người nói như lỗi bản phim cũ. |
| C245-LISTENER-TAIL / VISUAL_DEFECT, MINOR_LOCALIZED + AV_UNKNOWN | Prompt245 yêu cầu Đào khép môi toàn shot → frame181 / 7,541667s còn khép; frame182 / 7,583333s bắt đầu hé, frame184 / 7,666667s mở rõ; frames188–204 / 7,833333–8,500000s có miệng dạng O, frame208 / 8,666667s còn hơi hé; frame212 / 8,833333s đã khép. | Đây là **vi phạm lips-closed nhìn thấy**, không bằng chứng Đào nói hoặc bị gán giọng. Mức hiện tại khu trú ở tail; chưa đủ bằng chứng nâng thành MAJOR speaker lỗi. Ưu tiên EDIT bỏ tail sau khi nghe/kiểm range giữ trọn lời và nhịp. Nếu actualAV cho thấy chồng tiếng/sai speaker thì phân loại lại. Không tự T03, không freeze/mute hay phủ món để che lỗi. |
| C245-F0-FOOD / SAMPLED_MET | Nem nguội; bát trống, đũa nghỉ; rau/chấm/cốc đúng geography → samples giữ hai bát trống, hai đôi đũa trên bàn, nem giữa, rau trước-trái, hai chấm, cốc ngoài-phải. Không gắp/ăn/di chuyển serving hoặc visible steam. | Không chứng minh công thức/claim, không kiểm ngoài coverage; không phát hiện tái diễn lỗi khói trong samples. Joins cần kiểm lượng món/state thực. |
| C245-LIGHT / SAMPLED_READABLE | Warm soft light, mặt rõ → sampled eyes/mouths đủ sáng, không che miệng. | Không continuous flicker/exposure PASS. Dấu biểu tượng tạo sinh ở dưới-phải thấy trong native; không tự xóa, không coi nó thay disclosure đã chốt. |

### Range khả dụng — đề xuất, chưa EDL

Đã đọc full `C02_T02_245_ASR/asr.json` và `audio-diagnostics.log`: ASR ghi một segment **0,96–6,94 giây**; chữ “găng” thay “rang” có word probability thấp 0,328, chỉ là flag để nghe, không sửa thoại theo ASR. Silence detection ở -40dB ghi tail **6,968604–10,005 giây**. Hai nguồn offline hỗ trợ giả thuyết có handle sau âm cuối, không chứng minh giọng K20 hoặc lời nghe đúng.

**Candidate EDIT: [0, 7,500 giây), zero frames 0–179 / filename 00001–00180**, giữ nguyên đầu và theo ASR giữ đủ lời, có khoảng hơn 0,5 giây sau speech-end ước lượng; frame179 / 7,458333s và frame180 / 7,500000s đều còn môi Đào khép, Khoai cười nhẹ/môi khép. Candidate này bỏ trước mốc hé môi được quan sát 7,583333s. Cần actual listening xác nhận không cắt âm “chờ”, AV trong lượt nói và xem cut/join thực trước dùng; không mặc định chọn endpoint sát frame181 chỉ vì còn khép.

Không gọi 7,5 giây là timing đã duyệt hoặc tự đổi video 30 giây. EDIT/root phải cân timeline, chuyển sang N03 đúng người/lời; không bù bằng cận nem dài. Tool trim/export/assembly account là kiểm riêng của root, report không chứng nhận công cụ từ catalog.

## Request, authority và stop gate

Request245 hiện đã ghi native downloaded, một submit, quote15, medium UUID `4e9d7a4c-bf16-4aec-8212-d6e2990425e9`, một K20 ID `b447b35c-b35e-4140-af72-ecd277282b1a`, full prompt readback true, Omni 1.1 Flash / Ingredients / 720p / 9:16 / 10s / x1 / Agent OFF. Đây là root live record, reviewer không kiểm UI lại; bindings không tự chứng minh output voice. Exact dialogue vẫn chỉ Khoai N02, không “Khoan” hoặc audition/lời Đào.

Owner audioapproval244 chỉ áp dụng **T01 hash5ba2878f…**, không chuyển sang T02. Ba MAJOR T01 về set/khung/head-hands **không thấy lặp trong sampled T02**, nên chưa có căn cứ kích hoạt same-MAJOR-twice STOP từ chúng. Listener-tail là finding mới khác lớp; cũng không được gọi clip hoàn toàn sạch. Nếu kiểm actualAV tìm cùng MAJOR lặp lại phải dừng chẩn đoán theo238, không tự sinh T03.

## Handoff tuần tự

1. Giữ T02 làm candidate hình; chưa mở full gate C02 hoặc chọn final take thay owner.
2. Cho owner nghe exact T02, nhất là “Hồi bé, mẹ rang gạo, anh đứng chờ”; kiểm actualAV/sync và absence giọng khác trong range đề xuất.
3. Nếu đạt, EDIT thử range 0–7,5 giây và transition thực; trình checkpoint C02 + assembly test trước cảnh phụ thuộc theo243. Không tốn lượt sinh mới để sửa tail khi có thể cắt sạch và giữ lời.
4. Còn mở: actual voice/lời/nhịp/sync, cut/joins/timeline 30s, công cụ assembly thực và approval owner. Không release/whole-film PASS.
