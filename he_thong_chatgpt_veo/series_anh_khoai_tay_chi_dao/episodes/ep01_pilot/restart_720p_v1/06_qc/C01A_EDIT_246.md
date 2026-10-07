# C01A — Thiết kế điểm dựng và nối phần mở, REC246

**Run:** C01A-EDIT-246. **Ngày:** 07/10/2026. **Role:** EDIT v0.2, maker đóng góp. **Mode:** PAPER_EDIT_PLAN / STATIC_REFERENCE_VIEW. **Disposition:** PAPER_PLAN_COMPLETE / CONDITIONAL_PREPARATION. Không có EDL actual, generation-ready, audio/AV review hoặc whole-film PASS.

## 1. Đầu vào và khả năng kiểm thực

Đã đọc đầy đủ PROD7/02, DIRECT01, DIRECT05 EDIT v0.2, AEQ02 và SIA10; kế hoạch236; `00_decisions/scoped-autonomy-238.json`; `00_decisions/C02-export-approval-246.json`; `06_qc/run-registry-246.json`; `03_voices/bindings-238.json`. Lời bảy lượt và cách tách N02 dùng phiên bản hiện hành được ghi nguyên văn ở236, không dùng script chín lượt lịch sử trong hợp đồng.

Đã trực tiếp xem `02_refs/C01A_F0_from_C02_T02_v1.png`, tính lại SHA-256 `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`. Still cho thấy Khoai trái/Đào phải; môi cả hai khép, mắt hướng vùng bàn; tay nghỉ, đũa trên bàn, hai bát riêng trống, nem trên đĩa chung, rau trước trái/hai chấm/cốc ngoài phía Đào. Rau và cốc vẫn sát/cắt mép hình. Có watermark native; không đề xuất xóa. Đây là quan sát một ảnh, không xác nhận tay tiến/dừng/thu, giọng, motion hoặc lip-sync.

**Nguồn C02 được owner duyệt theo hồ sơ246:** `07_edits/C02_T02_FLOW_0_7p5S_FOR_APPROVAL.mp4`, SHA-256 `d151eb1d9f5f5b4486fed030579d9da3de0d23f434a65db2f6c4dca88b3228f3`. Approval chỉ cho export đã trình, không cho đuôi native10s hoặc toàn tập. Theo dữ liệu root giao: video181 frames/24fps =7,541667s; audio7,509333s. Tôi chưa probe hoặc nghe/xem file này, nên ghi đây là **reported measured evidence của root**, không phép đo trực tiếp của EDIT. Tên file0_7p5S không làm duration actual thành7,5s.

Chưa có C01A/C01B media/range/timing hoặc báo cáo DOP/ACT246 được giao vào context này. Capability của EDIT là đọc giấy/xem still; không nghe, không full playback. Thẩm quyền217 cho bounded specialist local work;238 quyền production có giới hạn thuộc root;246 đóng checkpoint C02 và mở chuẩn bị C01A. Tôi chỉ viết report này, không UI/API/Git/generation/credit, chỉnh nguồn, audio overlay, timewarp hoặc duyệt thay owner.

## 2. Câu–người nói–hình và state khóa

| Đơn vị | Expected speaker / exact text | Nhiệm vụ hình và điểm kết | State |
| --- | --- | --- | --- |
| C01A | Đào, D06/Aoede: “Anh nhìn mãi. Không hợp thì để em.” | Mặt/miệng Đào rõ; nói với Khoai thân mật. Tay ngoài, phía phải màn hình, tiến gần mép đĩa để biểu hiện ý định lấy; chưa chạm đĩa/món, chưa thu tay. Khoai nghe, không nói | F0→F0; endpoint tay còn ở pha định lấy |
| C01B | Khoai, K20/Orus: “Khoan.” | Thấy người nói và tay Đào cùng quan hệ. Sau cue này Đào dừng rồi thu tay, không tự làm xong trước anh ngắt | F0→F0; tay nghỉ trước ký ức |
| C02 selected export | Khoai: “Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.” | Nhận trạng thái hai người nghỉ tay để vào ký ức, không có thêm “Khoan” | F0→F0 theo nhiệm vụ; điểm nối mới chưa được nghiệm thu |

C01A chỉ gắn **một D06** mới `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`, không K20, không câu audition/thoại C01B. Speaker map là expected, không proof âm thanh sinh đúng. C01B được chuẩn bị sau khi có state ra thực của C01A, không dùng ảnh F0 bàn nghỉ để giả tay còn định lấy ở điểm nối. Mode Ingredients không cam kết khóa START/END.

## 3. Nhịp phần mở và hai lựa chọn paper

### A — Cho ý định tay diễn cùng lời, khuyến nghị

Đào nhìn Khoai và nói câu đầu; câu sau vẫn đối thoại với bạn, tay ngoài bắt đầu tiến gần đĩa trong khi cô nói. Khi toàn âm cuối “em” đã đủ, tay vẫn ở pha định lấy nhưng chưa contact. Cắt tương thích sang C01B: Khoai nói “Khoan”, cô mới dừng/thu. Như vậy cảnh mở gồm **lời + động tác đồng thời → ngắt → phản ứng**, không phải lời xong rồi biểu diễn một chuỗi tay riêng dài để lấp source6s.

Tác dụng kể chuyện: người xem biết cô sẵn sàng thử món và đang định lấy; lời ngắt có nguyên nhân nhìn thấy. Giữ đời thường, không giành giật đĩa hoặc “giám sát” Khoai. Không yêu cầu tay phải đạt một mốc giây bịa; ACT/DOP cụ thể hóa đường đi và vùng bàn có thể đọc được.

### B — Thêm nhịp nhận ra ý định trước “Khoan”, có điều kiện actual coverage

Giữ một nhịp hình ngắn sau câu Đào để người xem nhận rõ tay đang tới đĩa rồi mới C01B. Ưu điểm: cue ngắt dễ hiểu nếu hình tay ở A quá nhanh/nhỏ. Đổi lại opening dài hơn; chỉ dùng nếu source thật có pose/ánh nhìn phù hợp và nhịp whole-film cho phép. Không freeze/repeat frame, không kéo im artificial hoặc thêm lượt sinh chỉ để có nhịp này. Nếu source đã thể hiện ý định rõ ngay trong lời, A hợp lý hơn.

Cả A/B vẫn giữ nguyên7 lượt và nhiệm vụ stop/retract. Không chosen cut trước media. Không J-cut “Khoan” lên hình Đào/món để che mặt Khoai; không phủ câu N01 bằng bát nem hoặc crop người nghe/speaker.

## 4. Timing: khả thi về cấu trúc, chưa chứng minh vừa4,5s

236 đặt C01A native6s, C01B native4s và opening slot TARGET khoảng4,5s. Hai duration sinh không phải10s bắt buộc đưa vào timeline. Slot4,5s có thể được thử bằng cách cho tay tiến **cùng lời** và chỉ bỏ các khoảng trống actual đã xác minh, nhưng hiện chưa có audio/action durations để kết luận chắc chắn vừa hoặc quy định mỗi clip phải cắt còn bao nhiêu giây.

Minimum retained interval cần đủ: toàn N01 và hơi thở/đuôi âm cần thiết; ý định tay còn đọc được; toàn “Khoan”; dừng và thu tay đọc được trước ký ức. Các thành phần có thể chồng nhau hợp nghĩa **trong cùng take**, nhưng không tự chồng tiếng của hai lượt hoặc xóa phản ứng bằng cut. Không lấy số từ, dấu câu hoặc ASR boundary làm timing/cut sample-accurate.

**Tác động C02 đã duyệt:** slot ký ức cũ8,5s so với video export7,541667s chênh0,958333s. Nếu giữ opening4,5s, khối opening+C02 là khoảng12,041667s trước các phần sau, thay vì mốc13s giấy. Đây là phép tính trên allocation236 và duration được root báo, không EDL actual hoặc proof toàn tập đã có0,958333s “dư”. Không tự khóa lại C02 tại7,5s, trim thêm export đã được duyệt hoặc đặt pad im/freeze để khớp mốc13s.

Nếu opening thực hơi dài, root/EDIT có thể trình phân bổ lại khoảng chênh cùng timing toàn tập; không sinh giọng gấp, tăng tốc/pitch, bỏ từ/reaction hoặc tự dài hơn30s. Nếu vượt lượng có thể tái phân bổ sau đo, báo xung đột với các nhiệm vụ hành động sau chứ không ép giữ4,5s bằng cách che lỗi. 30s là target khóa, chưa chứng minh toàn lời/hành động đã vừa.

## 5. Endpoint và điểm dựng semantic

| Điểm | Sự kiện đề xuất, không timecode actual | State/hình cần nối | Lỗi cần chặn |
| --- | --- | --- | --- |
| Vào C01A | Trước onset “Anh”; có mặt Đào và bối cảnh hai người đủ hiểu lời. Không đòi một lead-in im dài | Hai tay Đào nghỉ từ ảnh F0, Khoai quan sát món; bàn giữ geography | Mất âm đầu, xuất hiện ngay tay đã chạm/đang lấy hoặc nền mới |
| Giữa N01 | Giữ mạch hai câu và khoảng nghỉ tự nhiên giữa “mãi” và “Không” | Tay có thể bắt đầu tiến cùng câu sau theo ACT; Khoai vẫn nghe | Cắt/chắp từ thành câu khác, hand jump/reset, Khoai nói miệng lời cô |
| C01A→C01B | Chỉ sau đuôi “em” hoàn chỉnh và ở pose tay đang định tới mép, chưa contact; không mặc định native finalframe là range ra | C01B kế thừa cùng tay/vị trí/hướng tiến, hai bát trống/đũa nghỉ/món chưa động | Cắt trước “em”, tay C01B về bàn trước “Khoan”, đã chạm món/đĩa trượt hoặc đổi tay |
| Trong C01B | Giữ trọn “Khoan” và tín hiệu Đào nghe→dừng→thu, không chỉ lấy frame đầu/cuối đẹp | Tay thu một lần về tư thế nghỉ; Khoai ngắt nhẹ rồi chuyển chú ý ký ức | Đào thu trước cue, tự nói thêm, tay teleport; nam nói offscreen không có chủ ý đã duyệt |
| C01B→C02 | Sau đuôi “Khoan” và sau thu tay đọc được; vào đầu export C02 đã duyệt theo actual onset/state | So actual C02 opening, mắt/đầu/hai tay/bát/đũa/nem/rau/chấm/cốc/ánh sáng/cỡ khung | Reset/hướng mắt giật, Khoan lặp, pop/đứt breath, thay export đã duyệt mà không tái review |

Đề xuất hard cut có động cơ đối thoại/hành động, không dissolve che contact/state. Không prescribe source in/out trước có footage. Word boundary chỉ đề nghị khoảng lân cận cần **nghe** (“Anh”, “mãi”, “Không”, “em”, “Khoan”, “Mùi”), không timestamp. Native image được rút từ C02 giúp đối chiếu identity/geography nhưng không bằng chứng C01B→C02 đã match chuyển động.

## 6. Kế hoạch kiểm actual và dependency

- **C01A toàn lượt:** native/hash/probe; source interval đủ N01, mouth Đào thực và Khoai im; SIA/AV-VOICE cùng owner nghe actual D06 trước mở thêm lời Đào. Preview239 hoặc tên/ID preset không thay checkpoint246.
- **Tay và endpoint:** xem chuyển động toàn đoạn; trích dày theo FPS probe thật quanh lúc tay rời bàn/tiến gần mép và range ra. So từng frame cần thiết ở vùng bàn–tay–đũa–bát, không dùng vài thumbnail để chứng nhận đường đi liên tục. Không contact/không món dịch chuyển, không đổi tay hoặc đũa nhân đôi.
- **C01A→C01B:** khi có hai nguồn, kiểm các frame ngay trước/sau cut và liên tục quanh điểm nối. Nghe âm cuối “em”→“Khoan”, không overlap/mất/lặp. Đối chiếu hướng tay chưa contact và phản ứng dừng sau cue; speaker/miệng đúng cả hai.
- **C01B→C02:** cùng target rough mới kiểm nghe-xem; approval C02 giữ scope nguồn đã chọn, không thừa kế full-join PASS. So cỡ cảnh/trục, tay nghỉ, eyeline, props, ánh sáng; không dùng C02 tail ngoài selected export để vá.
- **Đo rồi mới EDL:** source ID/version/hash/FPS/duration; source ranges measured; timeline order/in-out; line-to-picture map; trạng thái đầu/cuối range; review evidence đúng cut/export fingerprint. Không dựng thêm source giả hoặc đổi audio route vì chưa có timing.

Tool trim/export đơn C02 đã tạo một export được owner chấp nhận theo246, nhưng report này chưa trực tiếp kiểm khả năng multi-clip assembly/audio control; root đối soát UI/evidence mới theo scope. Không tự thay sang local cutting hoặc hứa stem/J-L controls. DOP/ACT246 cần được root đọc/tích hợp trước final request và independent critic; thiếu báo cáo không biến thành lỗi media đã quan sát.

## 7. Findings và disposition

| Rule / trạng thái | Expected / evidence hiện có | Severity nếu mismatch / route / closure |
| --- | --- | --- |
| EDIT246-SOURCE / MET ở scope hồ sơ | Exact C02 export được owner246 chọn, không toàn native; stillF0 được xem/hash lại | MAJOR nếu dùng sai nguồn; root manifest/selected hash và actual join |
| EDIT246-TIME / UNKNOWN | Opening≈4,5s TARGET; source C01A/B chưa có; C02 report duration7,541667s | Không coi thiếu timing là defect; EDIT đo media và whole-film allocation trước khóa EDL |
| EDIT246-FACE / DESIGN_SPECIFIED, MEDIA_UNKNOWN | Đào nói thấy mặt/miệng; Khoai nghe; Khoan thấy Khoai | MAJOR nếu sai; DOP/ACT/SIA/AV-CUT trên actual full interval |
| EDIT246-HAND / STILL_F0_OBSERVED, MOTION_UNKNOWN | Tay ngoài tiến→chưa contact; ngắt→dừng→thu; món vẫn F0 | MAJOR nếu thiếu cause/reset/contact; CONT/PERF/ACT kiểm path và actual cut |
| EDIT246-VOICE / OWNER_PREVIEW_ACCEPTED, C01A_UNKNOWN | OneD06 binding; actual female Northern voice checkpoint chưa chạy | HOLD thêm lời Đào; SIA/AV-VOICE + owner nghe đúng C01A/hash với reference/provenance |
| EDIT246-JOIN / UNKNOWN | C01B phải ra nghỉ tay khớp C02 selected đầu | MAJOR nếu state/speaker/âm cắt sai; actual rough hash/full AV + frame evidence |
| EDIT246-FINAL / NOT_TESTED | Giữ7lượt/30s/ý nghĩa hành động; chưa full rough | Không có whole-film PASS; DIR/EDIT và reviewer theo capability, owner rough rồi final |

Report chỉ hoàn tất proposal paper; các mức MAJOR là tác động **nếu** quan sát mismatch, không kết luận clip chưa tồn tại đã hỏng. Tôi chưa nghe/xem AV, không fake human acceptance, không nâng approval C02 thành approval take sau hoặc cảnh ghép.

## 8. Handoff năm mục

1. **Đã xác định:** exact N01/C01B/N02split, một D06 mới, F0 still hiện hành và C02 selected export owner246; reported durationC02 video7,541667s/audio7,509333s, không7,5s chính xác.
2. **Quyết định đã chốt:** chỉ kế thừa236/238/246, không chosen range/approval mới. Khuyến nghị paperA cho tay tiến cùng câu sau, giữ toàn lời và cue stop/retract.
3. **Giả định:** native6s/4s tạo được khoảng lời/action có thể chọn; opening4,5s có thể đạt hoặc cần phân bổ lại. Đây không forecast xác suất và chưa actual timing.
4. **Còn mở:** DOP/ACT integration/final request, media/timing/endpoint, voice Đào actual, two joins, multi-clip Flow capability và tổng30s.
5. **Bước tiếp:** root tích hợp và independent preflight, chạy một C01A trong quyền238 sau readback; QC và owner nghe giọng actual trước thêm lời Đào. Lấy state ra range C01A thật chuẩn bị C01B, rồi kiểm điểm nối vào exact C02 accepted; đo opening trước cập nhật EDL/nhịp toàn tập.

**Change log:** tạo mới C01A_EDIT_246; chỉ report paper, không đổi canon/source/media/approval hay tiêu credit. Không tự dùng reportC02_EDIT239 hoặc các mốc236 như QC media của lượt mới.
