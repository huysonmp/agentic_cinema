# C01B T01 — Chẩn đoán hình ảnh và khả năng cứu bằng điểm cắt

Run C01B-T01-DOP-DIAGNOSIS-246. Mode SAMPLED_FRAMES_DIAGNOSIS / TARGETED_PAPER_PROPOSAL. Vai DOP maker, không independent critic. **Disposition: REWORK_RECOMMENDED_FOR_START_AND_ACTION_CONTINUITY / ROOT_INTEGRATION_PENDING. Không mở C03A, không cấp retry hoặc owner waiver.**

## 1. Target và phạm vi kiểm thực

Đã đọc exact `04_requests/C01B_prompt_DRAFT_246.txt`, `06_qc/C01B_T01_ASR_raw_246.json` và các trường evidence native. Tính lại hash native `05_native/EP01_720_C01B_T01_NATIVE.mp4`: `f7321e72c952cf849f9b5febede7fb08951c997970de82e6f8d424f54415089b`, khớp handoff. Evidence root ghi24fps/96frames; không lấy decode hoặc metadata thành quality PASS.

Đã trực tiếp xem owner-QC tại `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/06_qc/C01B_T01_NATIVE_246/`: `overview_1fps_01.jpg`, hai board `mouth_hands_6fps_01.jpg`/`02.jpg` gồm24mẫu index0,4,…92; mở full PNG index0,16,24,48,56,72,95 (filename=index+1). Thời gian lần lượt0/0,666667/1/2/2,333333/3/3,958333s theo24fps. Đây là sampled still sequence, không xem hết96frame hoặc continuous AV; chưa nghe audio và không certify lip-sync.

Đã xem lại exact source `02_refs/C01B_START_from_C01A_T04_FLOW_v1.png` hash theo hồ sơ `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb` và C02 F0 `02_refs/C01A_F0_from_C02_T02_v1.png` hash `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`. Approval nguồn C01A cho phép limited rim-touch/inner gesture nhưng không platepull/take/eat; không bao gồm một reach mới của hai tay trong C01B hoặc miễn lỗi nối. Critic độc lập actual chưa đọc/đang pending. Task chỉ local read/view và ghi report này, không UI/API/Git/mediaedit/generation/credit.

## 2. Đối soát start — sai gì và lớn tới đâu

| Thành phần | Source C01A end | T01 index0 | Ý nghĩa / giới hạn |
| --- | --- | --- | --- |
| Tay trong Đào | Gesture cong gần bên trái bát cô, phía sau đĩa; chưa tới vành trái đĩa | Cẳng tay kéo dài chéo ra trước-trái, ngón ở gần mép trên-trái đĩa | Tư thế mới mở một hành động tới đĩa. Không phải rung nhỏ của cùng gesture, không thể giải thích chỉ bằng camera drift |
| Tay ngoài Đào | Ngón hơi cuộn/sát mép phải đĩa ở pose chạm nguồn | Ngón mở và tách khác hướng ở cạnh phải; tới index16/24 lại sát vành cùng tay trong | Match contact/grip không giữ đúng. Không suy lực nắm hoặc khoảng cách3D từ projection; sai silhouette/route quan sát được |
| Đĩa và nem | Pile có các dải/thịt lớn và silhouette đỉnh của source | Phân bố miếng/đỉnh pile khác; plate outline cũng lệch nhẹ | Food morphology/geography jump độc lập với tay; không được đổi/che món để cứu join. Không đếm gram hoặc kết luận thêm/bớt lượng thật từ ảnh |
| Camera/face/light | Khung hai người cùng axis, warmth và nền quán | Vẫn cùng kiểu khung, mặt đủ, palette gần | Không cần sửa camera toàn cảnh để chữa lỗi; camera/identity full-motion chưa PASS |

Để cụ thể hóa độ lệch **ước lượng bằng mắt trên ảnh720×1280, không registration/pixel segmentation**: đầu ngón tay trong source ở khoảngx400,y890–900, B0 xuống/trái về khoảngx325–335,y910–920 — lệch cỡ65–75px ngang và15–30px dọc. Tức khoảng9–10% bề rộng khung, đủ tạo khác biệt hành động nhìn thấy; không là thông số vật lý hoặc threshold automated. Tay ngoài B0 mở ra phải so nguồn khoảng vài chục pixel, nhưng dấu khác chính là shape ngón/contact chứ không coordinate. Plate outline B0 dường như lệch phải/lên cỡ10–20px ở một số biên; food silhouette thay nhiều hơn. Không có phép đo registered nên các số này **không dùng như tọa độ sửa hoặc proof plate displacement trajectory**.

## 3. Chuỗi quan sát actual

- Index0/16/24: tay trong đã ra trước và tới mép bên trái đĩa; tay ngoài ở mép phải. Khoai có môi mở mạnh tại16/0,667s, khớp vùng root báo có “Khoan” khoảng0,5–0,9s về mặt hình, nhưng tôi không nghe hoặc xác minh đúng âm/giọng. ASR “Khuán!”0–0,84s là detector không chính xác đã ghi, không owner approval hoặc heard text.
- Board indices4–48 và full24/48: hình đọc như hai tay còn tới/ở hai phía đĩa trong thời gian sau lời ngắt, không một outer-release ngay sau cue trong khi inner settle về bát. Đào chuyển nhìn Khoai về khoảng1,5–2s trên mẫu; tiếp đó mới thu.
- Full56/2,333s: cả hai tay đã rời vùng rim về phía bát, còn đang thu. Full72/3s và95/3,958s: hai tay về vùng nghỉ cạnh bát, hướng nhìn Đào sang Khoai. Đúng state nghỉ ở cuối không xóa start/extra-reach ở trước.
- So end với C02 F0: quan hệ tay/bát gần state mục tiêu, nhưng nét nhìn hai người và pile nem không match tuyệt đối. Phải kiểm actual join, không gán PASS vì đều tênF0. Không kết luận plate đứng yên toànpath hoặc release clean từ số mẫu này.

## 4. Có cứu bằng offset đầu được không?

**Không tìm được cơ sở cho một bounded offset trung thực từ mẫu đã xem.** Bỏ vài frame đầu vẫn còn inner-reach/two-hand rim và food jump ở vùng cần giữ lời. Cắt vào index16 đang Khoai nói không sửa pose đầu, còn có nguy cơ mất onset. Bắt đầu sau khoảng1s làm Khoan có nguy cơ mất hoàn toàn; vào2,333–3s lấy trạng thái thu/nghỉ sẽ bỏ nguyên nhân ngắt và phần buông khỏi vành. Không nối audio Khoan từ đầu lên phần hình sau, không tăng tốc, freeze, crop bát nem hoặc đổi plate để hợp thức hóa.

Một offset chỉ được xem xét nếu EDIT/SIA chứng minh simultaneously: toàn Khoan thật còn nguyên, pose nguồn→range đầu có match đúng action, outerrelease sau nghe và inner không reach mới, món/geography không jump. Các điều kiện này hiện chưa có evidence. DOP không tuyên bố mọi frame chưa xem đều không thể, nhưng **không khuyến nghị đi tiếp bằng cut khi đã có lỗi start xuyên vùng lời**. Needs native dense/playback/audio checks nếu root muốn khảo sát thêm; không scope paper này cấp cut approval.

## 5. Giả thuyết request và sửa tối thiểu

Prompt hiện hành có cả `Begin in the exact pose` và `She keeps her intention to take the plate until she hears "Khoan"`; cue sau có thể mơ hồ giữa “giữ pose hiện có” và “tiếp tục tiến lấy”. Cùng text còn nói inner-hover settle nhưng chưa chặn rõ **inner chỉ đi về thân/bát, không đi ra rim**. Actual thấy extra-reach tương thích với giả thuyết mơ hồ này; một output không causal proof. Food jump có thể là regeneration/reference adherence chưa đủ, không chứng minh do một câu prompt gây ra. Input ID/config thực phải root/FLOW kiểm riêng trước diagnosis cuối.

Giữ samecamera/scene/source/voices/lời; tách một transition, không thêm action:

> Ngay đầu, tay ngoài của Đào đã ở đúng pose chạm vành phải trong ảnh; tay trong vẫn ở đúng gesture gần bát cô. Không có động tác tiến tới đĩa mới. Khoai nói duy nhất “Khoan.” nhẹ và rõ. Nghe lời ngắt, Đào chỉ nới ngón tay ngoài khỏi vị trí chạm hiện có, nhấc tách và thu về cạnh ngoài bát. Đồng thời tay trong chỉ rút ngắn về thân và settle cạnh trong bát, không tới vành đĩa. Đĩa và từng bố cục miếng nem giữ nguyên trong khung; không kéo/trả đĩa. Hai mặt, tay và mép đĩa cùng thấy, camera cố định.

Đây là cue đề xuất để root/ACT/CTD tích hợp, **không prompt final hoặc permission retake**. Bỏ/reword `keeps intention to take` thành hold existing contact, không khuyên đưa nhiều câu negative mâu thuẫn. Không dùng tuyên bố “exact start” làm chứng nhận Ingredients có STARTlock. Nếu tuyến thực vẫn redraw scene/pile/start, cần root nêu giới hạn và lựa chọn technique hợp lệ sau preflight, không lặp chữ “exact” rồi hứa chắc đạt. Không tự đổi Frames+voice hoặc model/canon.

## 6. Findings và handoff

| Rule | DOP finding | Severity / route |
| --- | --- | --- |
| DOP-B01-START | DEFECT observed pose tay trong và tay ngoài so exact source | MAJOR cho causal join; root/ACT/CTD sửa tại request/take, critic actual độc lập |
| DOP-B01-REACH | Sampledsequence two-hand rim rồi mới retract, không chỉ release đã chạm | MAJOR cho nhiệm vụ; không giải bằng C02 endstate đẹp |
| DOP-B01-FOOD | Food contour/distribution thay ở B0 và end | Continuity DEFECT cần FOOD/CONT severity xác nhận trên join; không tự waive/crop/sửa món |
| DOP-B01-OFFSET | Không có evidence offset giữ đồng thời lời/start/ý nghĩa | HOLD selection; EDIT/SIA không dùng nghe/ASR riêng để bỏ hình chặn |
| DOP-B01-END | State nghỉ gần F0 ở72/95 | Partial observed, join/wholepath UNKNOWN; không MEDIA PASS |
| DOP-B01-VOICE | Chưa nghe, chưa verify pronunciation/K20/sync | UNKNOWN; SIA/owner đúng scope, ASR không quyết định |

Root đọc critic actual rồi tích hợp targeted correction và authority/stop rule238. Không mở C03A từ report này. Sau lượt được phép, kiểm start thật trước mở phần phụ thuộc, rồi wholepath/AV/join; prompt/screenshot/trạng thái cuối không thay chứng cứ actual. Không paidretry từ DOP.

Đã xác định: exactsource và T01 khác pose đầu/món, two-hand approach tồn tại qua vùng lời rồi mới thu; cuối tay nghỉ chỉ đạt bộ phận. Quyết định mới: none. Giả thuyết: câu “giữ ý định lấy” có thể kéo action tiếp tục; source adherence chưa đủ, không causal proof. Còn mở: critic/root, wholepath/voice/cut actual và tuyến sửa. Bước tiếp: chẩn đoán request/input/take, giữ samecamera và sửa chỉ transition release; không hide bằng cắt hoặc tiếp sản xuất.
