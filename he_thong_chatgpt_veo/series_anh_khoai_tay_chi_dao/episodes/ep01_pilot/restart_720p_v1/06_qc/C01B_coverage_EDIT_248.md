# C01B — Thiết kế nối và thoại, EDIT/DLG-EDIT248

Ngày 08/10/2026. RUN_ID `REC248-C01B-EDIT-DLG-COVERAGE`. Vai maker EDIT + DLG-EDIT. **PAPER_PROPOSAL / STATIC_DRAFT_REFERENCE_VIEW / FOR_ROOT_INTEGRATION; không EDL khóa, media PASS, review độc lập hoặc quyền resume production.** Chỉ viết report này; không UI/browser, tạo ảnh/video, install/API, chi, Git, sửa script hoặc media.

## 1. Nguồn, quyền và giới hạn bằng chứng

Đã đọc đầy đủ 217, 236, `00_decisions/C01B-coverage-direction-248.json`, `00_decisions/C01B-stop-and-coverage-options-247.md`, và các đóng góp `C01B_coverage_DIR_248.md`, `C01B_coverage_ACT_248.md`, `C01B_coverage_DOP_248.md` hiện có trong `06_qc`. Đã đọc thêm hồ sơ exact selection/audio C01A 246, exact approval C02 246 và hai manifest trim để định danh nguồn/range. Hai lỗi MAJOR start liên tiếp và STOP được kế thừa từ hồ sơ 247; EDIT không xem/nghe lại các video hoặc tự xác nhận findings media trong run này.

Owner 217 chọn `1A/2A/3A` cho nhiệm vụ chuyên biệt có artifact và reviewer độc lập. Owner 248 chọn hướng A và yêu cầu tiếp tục: thiết kế riêng coverage C01B, giữ nguồn/lời/giọng/canon. Đây không là owner duyệt các shot/ref mới, request trả phí, media hoặc mở C03A. T01/T02 giữ trạng thái không selected; không kéo một phần thu đẹp của chúng vào proposal để tự đóng lỗi start hoặc chuyển tiếng đã duyệt T01 sang hình mới.

Run này đọc hồ sơ và trực tiếp xem một draft still BM mới khi root cung cấp; không trực tiếp nghe, continuous AV, đo native mới, probe/hash lại hoặc xem lại hai endpoint gốc. Mọi số đo nguồn dưới đây là **reported measured evidence trong hồ sơ hiện hành**, không phép đo mới của EDIT. Các khoảng/cut chưa có media được ghi UNKNOWN; đó là thiếu bằng chứng, chưa phải lỗi output quan sát được.

## 2. Source lock và range hiện biết

Đường file trong bảng là tương đối từ `restart_720p_v1`; giữ exact exports làm source chọn, không tự mở lại đuôi native hoặc thay selection.

| Source / vai trò | SHA256 trong hồ sơ | Range / thời lượng hiện biết | Phạm vi được giữ |
| --- | --- | --- | --- |
| A — `07_edits/C01A_T04_FLOW_0_3p333S_FOR_APPROVAL.mp4` | `e22c113204c404e928683c69465237921f601f2b33a3eb9a9187eb0648f4b803` | Export zero frames 0–80 inclusive; 81/24 = 3,375s video; 3,370667s audio | Exact prefix selected dưới ngoại lệ limited rim-touch/inner gesture; owner nghe D06/đủ N01/kể cả “em”/nhịp. Picture scope theo review mẫu, không full lip-sync certificate. Không whole native 6s |
| A80 — `02_refs/C01B_START_from_C01A_T04_FLOW_v1.png` | `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb` | Exact extracted export frame 80; PTS 3,333333s, hiển thị tới 3,375s trong A | START state nguồn: Khoai tay nghỉ, Đào outer contact vành phải; inner hover gần thân/bát. Không hai tay nắm đĩa |
| BM / B-K — nguồn nói mới, **CHƯA TỒN TẠI** | UNKNOWN | Native fps/frame count/duration/range/audio onset/offset: UNKNOWN | Một nguồn hình–tiếng mới với mặt/miệng Khoai nói nguyên “Khoan.”; không borrowing T01 audio |
| BR / B-D — nguồn phản ứng mới, **CHƯA TỒN TẠI** | UNKNOWN | Native fps/frame count/duration/range/release onset/rest: UNKNOWN | Mặt Đào và đường buông/thu thực; im lời. START/END refs dự kiến là hai exact ảnh nguồn sẵn có |
| C02 — `07_edits/C02_T02_FLOW_0_7p5S_FOR_APPROVAL.mp4` | `d151eb1d9f5f5b4486fed030579d9da3de0d23f434a65db2f6c4dca88b3228f3` | Export zero frames 0–180 inclusive; 181/24 = 7,541667s video; 7,509333s audio | Owner 246 chấp nhận đúng export hình/Khoai/lời/nhịp. Không whole native 10s hoặc whole film |
| C02F0 — `02_refs/C01A_F0_from_C02_T02_v1.png` | `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad` | Exact frame 0 của C02 selected | END state BR: hai tay Đào nghỉ hai bên bát, tay Khoai nghỉ, môi khép, bàn/món F0 |

UI A 0→00:03:08 đã cho 81 frames, UI C02 0→7,5s đã cho 181 frames. Tên file/điểm UI không thay duration đo. Range trong bảng là range **export selected**, không tuyên bố EDL native từng frame đã kiểm lại. Chênh audio/video khoảng 4,333ms ở A và 32,334ms ở C02 không tự chứng minh khoảng im có thể dùng, gap nghe được hoặc lỗi sync; kiểm trên assembled target thực.

## 3. Sequence đề xuất cụ thể

**A exact 3,375s → BM: Khoai nói nguyên “Khoan.” → BR: Đào tiếp nhận, buông contact ngoài, thu tay ngoài và settle tay trong về bát riêng, cả hai tay nghỉ → C02 exact 7,541667s.** Ba cuts có động cơ: đổi sang người ngắt, sang người nghe, trở về người kể ký ức. Không dissolve hoặc insert món làm trung gian.

Đồng ý khảo sát phương án root: **BM mới là asymmetric medium thiên Khoai, vẫn cùng trục và state A80; BR trở về khung chung gốc, START exact A80, END exact C02F0.** BR không cần sinh thêm hai still reaction riêng nếu giữ phương án này. Đây là đề xuất tích hợp thay cho BR medium thiên Đào của DOP ban đầu; root/DOP/reviewer cần đánh giá khả năng đọc mặt–tay trong khung chung gốc. Hai endpoint gốc không chứng minh route hỗ trợ cả hai với cấu hình đúng, không chứng minh output sẽ giữ start hoặc chuyển động giữa chúng. CTD/FLOW kiểm feature/request/quote, không EDIT tự đổi mode.

BM cần reference góc/cỡ mới có kiểm/duyệt riêng; không crop A/T01/T02 để giả coverage mới. Sau đọc đầy đủ DOP hiện hành và `00_decisions/C01B-coverage-production-brief-248.md`, EDIT cập nhật: BM chỉ cần coverage mắt/miệng Khoai rõ; contact/tay Đào có thể ngoài khung và giữ UNKNOWN, không buộc nhét toàn bàn vào shot nói. State scene vẫn kế thừa A80, không cho phép reset rồi giấu ngoài khung. BR original-wide phải thấy mặt Đào, contact và toàn release/return để chứng minh nhiệm vụ; nếu BR thiếu vùng đó thì REWORK design, không hứa crop sau để chữa.

**Draft BM root mới cung cấp:** `02_refs/C01B_BM_START_v1_CHATGPT_FOR_REVIEW_248.png`, SHA256 theo root `8ecb1105de2b8a0b786c05ad38e4965206d62a7629741a7863e8fcb77f7bad03`, 941×1672, gần 9:16 nhưng chưa đúng raster 720×1280. EDIT đã trực tiếp xem full still: mặt/miệng Khoai lớn, rõ, tay anh nghỉ; Đào hiện một phần bên phải, mắt thấp, tay trong gần bát thấy được. Tay ngoài/contact vành phải ngoài khung nên **UNKNOWN**, không chứng minh vẫn contact hoặc được phép đổi tay. Có thể giữ draft làm candidate review đúng phạm vi framing người nói theo DOP/brief hiện hành; việc ngoài khung không tự là blocker buộc đổi cỡ BM. Candidate vẫn chưa owner-approved hoặc request READY; actual reset nếu lộ ở BM/BR hoặc join vẫn phải REWORK. BR là nơi proof contact→release→rest, không nơi hợp thức hóa nguồn BM sai. Still không có voice/motion/AV hoặc owner media approval.

| Order / nhiệm vụ | Line-to-picture / người nói–nghe | State vào→ra và sự kiện phải thấy | Range/cut status |
| --- | --- | --- | --- |
| A selected | N01: Đào nói “Anh nhìn mãi. Không hợp thì để em.”; Khoai nghe | Giữ exact prefix kết A80; chưa pull/take/eat trong selected scope | Giữ nguyên export 0–80; không cắt cuối “em” hoặc lấy thêm native tail |
| BM / B-K | N02a: **Khoai nói chỉ “Khoan.”**, K20 mới; Đào nghe im | Đầu tiếp A80. Khoai tay nghỉ, phát âm thân mật; Đào outer contact/inner hover. Khuyến nghị không hoàn tất phản ứng tay hoặc quay mắt rõ trong BM nếu BR sẽ START exact A80 | Native/range UNKNOWN. Giữ từ onset đến hết waveform giọng và động tác phát âm; điểm cut theo actual, không timestamp mẫu |
| BR / B-D1 | Không lời mới; Đào nghe lời vừa nói, Khoai không diễn nói thêm | START contact/inner hover như A80; mắt Đào chuyển chú ý lên Khoai ngay nhịp kế tiếp, không pause hoặc reach mới | Cue onset UNKNOWN; không lặp Khoan để cô “nghe lại” |
| BR / B-D2–3 | Hai người im lời; Đào là chủ thể reaction | Outer ngón nới→tách khỏi vành→cẳng tay thu về thân/ngoài bát→nghỉ. Inner chỉ thu/settle về cạnh trong bát, không tới plate-left. Đĩa đứng yên, hai bát trống, đũa nghỉ. Cuối hai tay nghỉ như C02F0 | Toàn path/rest UNKNOWN; không cut từ contact thẳng sang rest |
| C02 selected | N02b: Khoai nói “Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.”; Đào nghe | Giữ exact C02F0 và source selected; F0→F0, không gắp | Giữ export 0–180; không sinh/lặp Khoan trong C02 hoặc mở tail đã loại |

Việc BR trở về A80 sau BM là trở lại **một contact vẫn đang được giữ**, không phát lại reach của A. Giữ BM không thay physical state là điều kiện của phương án ref này. A80 có mắt Đào thấp; **BM không cho Đào bắt đầu release hoặc nâng mắt rõ rồi BR reset về A80**. Nếu actual BM làm vậy, HOLD/dependency rework, không quay ngược action để giữ ref tiện lợi. Root/DIR quyết định ref/coverage phù hợp từ actual hợp lệ, không tự cho phép sửa A/C02.

## 4. DLG-EDIT: nguyên âm thanh và checkpoint mới

Giữ **trọn waveform tiếng nói của “Khoan.” từ nguồn BM mới**, gồm onset/âm cuối và phần diễn miệng tương ứng; không gate/chop âm, cắt tail, đổi pitch/speed, ADR, crossfade qua từ hoặc chuyển placement để sửa sync. Không hiểu “giữ waveform” là bắt đưa mọi idle/ambience của toàn native vào phim. Khoảng dư chỉ được trim sau khi xác định actual whole word, causal reaction và handles cần thiết.

Toàn từ nói cần thấy trên mặt/miệng Khoai ở BM. Cut trực tiếp sang BR ngay sau nguyên âm thanh/diễn phát âm hoàn tất là lựa chọn đầu tiên để khảo sát; không bắt Khoai giữ môi nghỉ lâu rồi Đào mới phản ứng. BR tiếp nhận ngay, không tạo một im lặng mới để lấp thời gian. **Không mặc định overlap hoặc audio lead vào BR:** BR im là phản ứng với từ vừa nghe. Nếu actual assembled đọc thành phản ứng chậm, trình DIR/ACT/EDIT sự kiện/cut/range thực để xét nhịp khác; không tự chồng Khoan lên môi nghỉ hoặc dịch speech khỏi nguồn đồng bộ.

Mọi voice ID/performance chỉ là binding input. K20/Orus mới trong ACT 248 là `b447b35c-b35e-4140-af72-ecd277282b1a`, cần đối soát request/binding hiện hành trước production; không thêm D06 vào BM/BR, không lời “Mùi này…” vào BM. T01 đã được owner nghe không là approval cho waveform BM mới. BR nếu có lời/tiếng cười ngoài brief hoặc miệng diễn người nói sai phải được ghi finding; không mute để biến lỗi thành nguồn im đạt.

Checkpoint cụ thể trước nhận BM selected: SIA/AV hoặc owner có capability **nghe đúng native/take và exact range/export/hash mới**, xác nhận Khoan chỉ một lần, đúng Khoai/K20, đủ âm cuối/nhịp và môi Khoai diễn speech ở hình tương ứng; Đào không bị gán giọng hoặc phát âm thay. AI không nghe thì giữ `ACTUAL_LISTENING/VOICE UNKNOWN`, làm phần kiểm source/range/hình có capability và trình exact artifact để owner nghe. Không gọi ASR, waveform plot, tên preset hoặc decode là heard_text/voice PASS.

Sau assembly kiểm A/N01→Khoan→C02/N02b không lặp/bỏ/chồng lời; giữ source waveform A/C02 đã chọn. Source approval vẫn đúng scope nguồn, nhưng cut mới và tổng AV cần review trên target mới. Report source cũ không tự PASS joins.

## 5. Ba điểm nối và điều kiện cắt

| Join | Cut có lý do / state cần khớp | Rủi ro lặp hoặc giấu lỗi | Bằng chứng còn cần |
| --- | --- | --- | --- |
| J1 A→BM | Sau hết N01 của exact A; chuyển trọng tâm tới Khoai ngắt. BM đầu outer contact vành phải, inner hover gần bát; Khoai tay nghỉ; không reach/two-grip | BM tự reset tay/món; cắt mất “em”; góc/raster đổi rất nhỏ gây jump không có nhiệm vụ | Actual đầu BM, A80, dense frames quanh cut và audio onset; source/range/hash. Native cut indices UNKNOWN |
| J2 BM→BR | Giữ toàn Khoan trên mặt Khoai rồi chuyển người nghe. BM chưa buông/thu; BR vẫn contact trước release, tiếp nhận ngay | BR bắt lại Khoan; BM đã eye-lift/release rồi BR quay về A80 thấp mắt/contact; hai lần buông; thêm pause; lip-tail trên người nghe | Actual mouth/word offset, BM exit và BR entry/cue/release. Indices/timecodes UNKNOWN |
| J3 BR→C02 | Sau trọn release/retract và rest tự nhiên; hai tay nghỉ, F0, nhìn/môi/props hợp đích C02F0; quay lại lời ký ức | C02 thay đoạn thu thiếu; END C02F0 xuất hiện ở BR rồi lặp nhiều frames tạo hold; food/table jump dù tay hợp | Actual BR endpoint/path, C02F0 và assembled start of memory; rest/cut indices UNKNOWN |

BR Frames nếu route khả thi có thể giữ cả exact endpoint ảnh trong output. Không mặc định frame 0 generated byte-identical ref hoặc END nằm ở native frame cuối; cần xem actual. Ở J3, BR endpoint và C02 frame 0 giống pose không tự là lỗi: nối resting pose có thể hợp nghĩa. Tuy nhiên phải kiểm số frame lặp/hold và nhịp; không xóa C02 frame 0/đổi A range theo suy đoán hoặc dùng freeze. Chỉ chọn range BR sau khi chứng minh trọn action/rest còn giữ; source A/C02 giữ nguyên.

Kiểm đồng thời geography Khoai trái/Đào phải, identity/clothes/light/eyeline, nem nguội/no steam, đĩa/pile chưa lấy, rau trước-trái, hai chấm, hai bát trống, hai đôi đũa nghỉ, cốc ngoài Đào. Cut khác cỡ không miễn reset/count/shape. Không dùng crop/món che tay, đổi tốc, overlay giọng lên môi khép, reverse, freeze hoặc dissolve để đóng findings.

Ngoài duplicate action còn cần kiểm duplicate **timeline instance**: hồ sơ trim A 246 từng ghi tự có hai instance cùng native trước sửa. Khi có scene/assembly mới, read-back đúng một A, một BM, một BR, một C02 theo source IDs/ranges; native giữ nguyên. Đây là check đề xuất, chưa thao tác hoặc khẳng định lần này có duplicate.

## 6. Sổ thời gian 30s — phép tính khả thi, chưa EDL

Đặt `bK` và `bD` là thời lượng **selected thực** BM/BR sau đo, `B=bK+bD`. Hiện cả hai UNKNOWN. Không lấy duration sinh hoặc snapshot timestamp làm duration dựng; không coi sound overlap là cách tự lấy thêm giây.

`A+C02 = 3,375 + 7,541667 = 10,916667s`.

`Tổng mở + ký ức = 10,916667 + B`.

`Thời gian còn cho C03A…C09 = 30 − 10,916667 − B = 19,083333 − B`.

| B giả định để khảo sát, không đo/khóa | A+B+C02 tính toán | C03A…C09 còn theo target 30s | So với 17s phân bổ giấy của 236 sau R02 |
| --- | --- | --- | --- |
| 2s |12,916667s|17,083333s|Chênh +0,083333s trên giấy; chưa proof đủ toàn thoại/hành động |
| 3s |13,916667s|16,083333s|Chênh −0,916667s trên giấy; cần kiểm actual nhiệm vụ sau trước kết luận |

**2–3s là giả định làm việc của DIR để khảo sát**, không số đo, duration sinh, clip range, budget/cost hoặc lời hứa thành công. Mốc mở 4,5s của 236 trừ A 3,375s cho 1,125s chỉ là phép tính slot cũ; không buộc B mới vừa 1,125s. Slot C02 giấy 8,5s trừ source 7,541667s cho 0,958333s không tự thành slack được cấp; cần tính actual toàn sequence. Nếu các phần sau thực cần 17s thì B chỉ có 2,083333s theo số học, **chưa phải giới hạn nghệ thuật đã duyệt hoặc lý do cắt mất diễn**.

Phần sau phải giữ các nhiệm vụ sau, nhưng source/hash/range/duration thật hiện UNKNOWN trong run này; không lập whole-film EDL giả:

| Khối sau | Lời / hành động cần bảo toàn | Allocation giấy 236, không timing đo |
| --- | --- | --- |
| C03A+B / R03 | Đào “Anh chờ ăn à?” → Khoai “Chờ mẹ quay lưng.”; cô nhận ý đùa/chuyển chú ý |3s|
| C04 / R04 | Đào quay lấy cốc trước; Khoai tranh thủ gắp A về mình, chưa tới miệng |3s|
| C05 / R05 | Đào thấy A→nhìn anh; Khoai biết bị thấy/khựng; Đào “Chờ em quay lưng nữa à?” |2,5s|
| C06 / R06 | Khoai “Anh gắp cho em mà.” và đổi hướng cùng A |2s|
| C07 / R07 | Đào hiểu/trêu “Thế em quay lại đúng lúc rồi.”, đưa bát riêng trống nhận |2,5s|
| C08 / R08 | Thả cùng A vào bát Đào một lần, đũa rời; không speech cover |1,5s|
| C09 / R09 | A vẫn trong bát Đào, B khác về Khoai, hai mặt hiểu nhau |2,5s|
| Tổng giấy |Đủ N03–N07 và quan hệ A/B, chưa source EDL|17s|

Không gán các khối sau vào timestamp tuyệt đối mới khi chưa có media; thời gian vào C03A hiện chỉ biểu thức `10,916667+B`. Cần đo từng line/path/cut thực trước production phụ thuộc và full rough gate. Nếu tổng vượt 30s, root trình conflict và phân bố có source evidence; không tự đổi lời/cắt action/rút exact A/C02/tăng speed/pitch hoặc bỏ end beat. Không gọi feasibility tính toán là đã chứng minh phim vừa 30s.

## 7. Handoff và tiêu chí đóng phần EDIT

| Task cụ thể | Người/scope | Output cần để thay UNKNOWN |
| --- | --- | --- |
| Tích hợp BM medium + BR original-wide với hai source refs | Root/DIR/DOP/ACT; reviewer độc lập design | Versionlock composition, causal cue, vùng mặt/tay, xung đột ref/pose; ghi rõ BR gốc thay đề xuất BR medium trước |
| Kiểm route/inputs/config/live quote | CTD/PROMPT/FLOW theo authority hiện hành | Request cụ thể/phạm vi/gates; không claim voice+exact endpoints cùng route nếu chưa kiểm. Proposal giấy không mở submit |
| Định danh BM/BR thật, giữ natives | Root/EDIT | Hash, fps/frame count/duration, native→selected ranges zero-based, start/end inclusivity, event landmarks; chưa có new take thì vẫn UNKNOWN |
| Đo Khoan/cue/release/rest | EDIT + ACT + SIA/AV/owner theo capability | Full word waveform on source face; onset/cut/offset, one release/retract, rest, tiếng mới nghe được theo exact target |
| Kiểm J1/J2/J3 và duplicate | CONT/FOOD/PERF/CINE + AV-CUT độc lập | Findings theo actual frames/ranges/hash; nếu sample-only ghi đúng giới hạn. Không tự closure từ ảnh endpoint |
| Đối soát 30s/full rough | Root/EDIT + DIR và reviewer | Measured line/state/timing ledger đủ N01–N07/A–B; assembled export/hash/gates, conflict trước mở rộng |

EDIT maker không tự duyệt output này hoặc media về sau. Ranges mới cần source evidence trước khóa; root đọc đầy đủ report và giải bất đồng, reviewer độc lập kiểm đúng target/capability. Endpoint, đúng input/voice ID và report tồn tại không đủ đóng MAJOR start. Duyệt source audio cũ không thay nghe/AV/nhịp của media mới hoặc whole film.

**Đã xác định:** exact A 3,375s / C02 7,541667s và A80/C02F0 có định danh; STOP tuyến cũ vẫn áp dụng; B phải nối nguyên từ Khoan trên mặt Khoai tới reaction/release/rest thấy được. Draft BM đã xem có mặt Khoai rõ, tay ngoài Đào ngoài khung UNKNOWN. **Đã chốt:** owner cho khám phá coverage A, giữ source cuts/canon/voice direction; chưa media/request approval. **Giả định đang dùng:** BM medium bất đối xứng, BR khung chung gốc A80→C02F0; B 2–3s chỉ khảo sát; chưa proof route/path/nhịp. **Còn mở:** draft BM framing/contact/preflight, route/quote, natives/ranges/cue/voice mới, cả ba joins và actual 30s. **Bước tiếp:** root tích hợp/ref/review trong scope 248; chỉ trình production cụ thể sau feasibility và approval cần thiết, không tự T03/C03A từ file này.
