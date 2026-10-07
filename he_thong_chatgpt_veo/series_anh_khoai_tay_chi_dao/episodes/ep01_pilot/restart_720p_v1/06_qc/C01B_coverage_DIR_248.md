# C01B — Thiết kế coverage DIR REC248

Ngày: 08/10/2026. RUN_ID: `REC248-C01B-DIR-COVERAGE`. Trạng thái: **DESIGN_ONLY / FOR_INTEGRATION**. Đây là đóng góp maker DIR, chưa là review độc lập, media PASS, prompt sẵn sàng submit hoặc approval chi. Owner đã chọn hướng A của247 và yêu cầu tiếp tục; quyền217 `1A/2A/3A` cho bounded local role run. Lượt này chỉ đọc hồ sơ, xem hai ảnh và viết đúng report được giao; không UI, generation, credit, API, Git hoặc sửa media.

**Cập nhật tích hợp 08/10/2026:** đề xuất ban đầu bên dưới được giữ làm lịch sử. Riêng composition B-K/B-D và cách đặt cue nghe qua cut đã được thay thế bởi phụ lục tích hợp cuối file: BM thiên Khoai cho phép contact ngoài khung UNKNOWN; BR về nguyên góc chung A80→C02F0; không eye-lift/release trong BM rồi reset ở BR. Khóa nguồn, mục tiêu kể chuyện, timing và các giới hạn chất lượng/quyền trong đề xuất ban đầu vẫn giữ. Khi có khác biệt về coverage/cue, dùng phụ lục cùng brief248 hiện hành, không dùng yêu cầu cũ buộc BM thấy toàn tay/hai mặt.

## Kết luận đạo diễn

Thiết kế C01B thành hai shot: **B-K — Khoai ngắt bằng “Khoan.”, thấy rõ mặt/miệng; B-D — Đào nhận lời ngắt rồi buông–thu tay, thấy rõ mặt và hai tay**. Cắt theo sự chuyển chú ý từ người ngắt sang người nghe. Sau B-D mới vào exact C02 đã chấp nhận. Không đổi chuyện/lời: vẫn là Đào định lấy món → Khoai yêu cầu chờ → cô dừng → anh chia sẻ ký ức. Hai người trưởng thành, bạn bè; Khoai trái, Đào phải.

Đổi coverage có lý do kể chuyện, nhưng không xóa yêu cầu nối trạng thái thật. Nếu B-K hoặc B-D tự đổi inner hand gần bát thành tay vươn tới vành trái đĩa, đó vẫn là lỗi continuation. Không gọi góc mới là quyền reset tay. Hai take B cũ giữ STOP; không dùng T01/T02 làm nguồn selected hoặc tự mở T03 cùng tuyến cũ.

## Nguồn đã đọc và khả năng kiểm thực

Đã đọc **toàn bộ**217,236, `00_decisions/C01B-stop-and-coverage-options-247.md`, `00_decisions/C01B-repeated-start-stop-247.json` và `06_qc/C01B_T02_native_independent_247.md`. Các trạng thái “chờ chọn” trong247 là lịch sử trước lựa chọn A được root giao ở REC248; không tự chỉnh hồ sơ247.

Đã trực tiếp xem hai ảnh đầy đủ bằng công cụ xem ảnh và tính lại SHA256:

| Nguồn | SHA256 | Điều quan sát được trong still |
| --- | --- | --- |
| `02_refs/C01B_START_from_C01A_T04_FLOW_v1.png` — exact A80 | `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb` | Khoai trái, hai tay nghỉ trên bàn, môi khép. Đào phải, mắt thấp về vùng món; tay ngoài từ screen-right đang tại vành phải đĩa, tay trong lơ lửng gần thân/bát riêng, chưa nằm phẳng. Không phải hai tay đang ôm hai phía đĩa. |
| `02_refs/C01A_F0_from_C02_T02_v1.png` — đích C02F0 | `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad` | Hai nhân vật cùng trục trái/phải; tay Khoai nghỉ, hai tay Đào nghỉ hai bên bát riêng; hai bát trống, đũa trên bàn, cốc ngoài bên Đào. |

Cả hai ảnh: phố mở, ánh ấm, rau/lá phía trước-trái, hai đồ chấm, đĩa nem giữa bàn, không thấy hơi nóng. Still cho biết bố trí nhìn thấy, không chứng minh plate stationary3D, đường chuyển động, nghe, giọng hoặc sync. Tôi không phát/nghe video và không tự review lại full T01/T02; việc lặp MAJOR là evidence của reviewer247/root, không claim quan sát AV mới của DIR248.

Các nguồn selected được giữ nguyên theo dispatch và hồ sơ hiện hành:

- C01A exact cut: SHA256 `e22c113204c404e928683c69465237921f601f2b33a3eb9a9187eb0648f4b803`, 81 khung/24fps, **3,375s**. A80 là khung cuối tại3,333333s, còn thời gian hiển thị tới3,375s; không lấy tên file3p333 làm duration.
- C02 exact accepted export: SHA256 `d151eb1d9f5f5b4486fed030579d9da3de0d23f434a65db2f6c4dca88b3228f3`, **7,541667s**. Không mở lại native tail hoặc thay cut để giải bài toán B.
- Hai actualB đã thất bại cùng start-pose blocker, T02 có release/rest sớm hơn trong mẫu nhưng không đóng mismatch. T02 audio chưa được chấp nhận; T01 audio acceptance không chuyển sang shot mới.

## Beat map và coverage đề nghị

| Beat | Shot / hình phải thấy | Hành vi và nguyên nhân | Điều kiện ra / lý do cắt |
| --- | --- | --- | --- |
| B0 — nối ý định từ A80 | B-K: cỡ vừa ưu tiên Khoai, giữ Đào phải và bàn trong khung đủ đọc trạng thái tay | Đào vẫn đang ở contact vành phải đã có; inner hand gần thân/bát, chỉ có thể tiếp tục thu vào. Khoai đang nghe, tay nghỉ, chưa có động tác lệnh tay. | Khán giả còn nhận được hành động Đào đang định lấy, trước khi bị lời ngắt làm đổi ý. Không mở B bằng hai tay tới đĩa. |
| B1 — ngắt nhẹ | B-K: mặt/miệng Khoai rõ suốt nguyên từ “Khoan.”, Đào có mặt để thấy nghe | Khoai đổi chú ý từ món sang Đào, gọi chờ bằng giọng K20 ấm chắc, thân mật, mức ngắt vừa đủ. Không quát, không giám sát, không giơ hai tay. Đào nhận cue trước khi buông. | Giữ hết âm “Khoan.” và diễn mặt người nói trên hình nói. Cut có động cơ sang phản ứng khi sự chú ý của Đào đã bắt đầu đổi. Exact cue/cut phải đo trên audio thật. |
| B2 — nghe và quyết định dừng | B-D: medium Đào bên phải, đủ mặt và cả hai tay; Khoai ở phía trái theo trục | Mắt Đào lên Khoai, ý lấy món dừng; outer fingers thôi contact vành phải. Inner hand chỉ về thân/bát, không ra trái tới đĩa. Không cần gật mạnh, giật mình hoặc thêm lời. | Chuyển từ ý định lấy sang chấp nhận chờ đọc được bằng mắt rồi tay. Nếu release bắt đầu cuối B-K, B-D phải tiếp đúng phần còn lại, không diễn release lần hai. |
| B3 — buông, thu, nghỉ | B-D giữ mặt Đào và đường tay đến bát, không insert món | Outer hand rời vành → thu về phía mình → nghỉ cạnh bát; inner hand thu nhẹ về vị trí nghỉ còn lại. Đĩa không bị kéo/nhấc; nem chưa bị gắp. Khoai tay nghỉ, không hành động cạnh tranh với phản ứng. | Có một điểm nghỉ tự nhiên đọc được, không freeze. Đào sau nhận lời dừng có thể chuyển ánh nhìn nhẹ về vùng món chung để chuẩn bị nghe ký ức; không tạo một nhịp diễn mới dài. |
| B4 — vào C02 | Cắt về exact C02F0 cùng trục và vật thể | Tay Đào đã nghỉ như đích C02F0, môi người nghe khép; bát vẫn trống, đũa nghỉ, F0→F0. Khoai bắt đầu phần “Mùi này…” trong C02 đã chọn. | Cut thay trọng tâm từ phản ứng trở về ký ức, không dùng C02 để giấu phần release chưa diễn xong. |

### Ý nghĩa và quyền hạn của hai shot

B-K cho khán giả thấy ai đã ngắt, thái độ ngắt và khẩu hình của từ quan trọng. B-D cho khán giả thấy người nghe chủ động chấp nhận chờ, nên đoạn ký ức sau đó có người đang lắng nghe. Nhịp này làm rõ hai ý khác nhau; nó không thay lời bằng hình tay hoặc biến Đào thành người bị ra lệnh.

Khuyến nghị DOP dùng thay đổi cỡ/góc có ý nghĩa rõ giữa A→B-K và B-K→B-D, cùng phía trục; không chỉ lệch raster chút ít mà giả match-cut cùng góc. Đây là **camera intent**, chưa là góc/khung đã tạo. B-K vẫn phải cho phép kiểm vị trí hai tay Đào; B-D phải đủ mặt, vành phải đĩa, bát riêng và toàn đường thu. Không crop để giấu tay trong sai, che mặt bằng foreground, hoặc cho cảnh cận nem đứng vào từ “Khoan”. DOP xác định composition cụ thể và khả năng đọc đồng thời mặt–tay trong dọc9:16 trước đóng brief.

Hai shot là hai nhiệm vụ coverage trong bản dựng, **chưa quyết định số request/tính năng multishot**. Không giả định một output tự dựng hai camera tốt hoặc một tuyến mới đã sẵn có. CTD phải đề xuất cách tạo từng nguồn bằng công cụ hiện được phép và kiểm feature/input/quote trước production; đổi tool/mode/voice ngoài quyền hiện hành cần nêu riêng.

## Liên tục hành động: đổi coverage phải giải được gì

1. **A→B-K:** giữ chức năng tay theo A80. Một tay contact vành phải, tay kia gần thân/bát; đầu B không tự vươn thêm, plate/food không tự reset. Chấp nhận perspective mới về thiết kế không đồng nghĩa cho phép đổi trạng thái physical action.
2. **B-K→B-D:** cut tại chuyển chú ý/tiếp nhận. Khoai đã nói rõ trên hình; B-D là phản ứng với lời vừa nghe. Không đặt Khoan lên môi khép của B-D hoặc cho Đào buông trước nguyên nhân. EDIT chọn điểm cut có tail âm đầy đủ trên B-K, không chèn overlay để sửa speaker. Nếu output buộc causal cue vào vùng không nhìn rõ, report là coverage chưa đạt.
3. **B-D→C02:** động tác đã hoàn tất trước cut, tay/bát/đũa/đĩa/cốc/rau/chấm khớp chức năng và bố trí C02F0; góc mới vẫn là cùng bàn. Không nhảy từ tay ở vành sang tay nghỉ mà thiếu đường thu. Food arrangement drift còn phải kiểm, không đóng vì đã gọi đúng tên món.

Không đồng nhất hành động này với đường miếng A ở cảnh sau: C01B vẫn F0, không gắp/ăn/thả nem, không dời rau hoặc đổi hai đồ chấm. Giữ cold/no-steam, hai bát riêng trống, hai đôi đũa đúng vị trí và cốc ngoài Đào. Giọng K20/D06, tuổi, tình bạn và canon không mở lại.

## Timing: có conflict phải đo, chưa có EDL mới

Hai selected nguồn đã chiếm **3,375 +7,541667 =10,916667s** trước khi thêm bất kỳ C01B mới. Vì thế full30s chỉ còn **19,083333s − thời lượng B selected** cho các phần C03A trở đi, nếu không đổi A/C02 và không dùng overlap để chữa lỗi. Không coi slot1,125s từ opening4,5s giấy là bắt buộc cho “Khoan + nghe + buông + thu”.

Giả định làm việc để khảo sát nhịp: B-K+B-D có thể cần khoảng **2–3s selected**, chưa nghe/đo/thử và không phải duration sinh hoặc cam kết output. Với2s, mở+kỷ niệm thành12,916667s; với3s thành13,916667s. Phần sau còn17,083333–16,083333s, trong khi236 phân bổ giấy khoảng17s sau R02. Ví dụ này cho thấy2s có thể sát phân bổ cũ,3s có thể gây thiếu nhịp; không chứng minh toàn phim vừa30s hoặc cấp quyền rút những cảnh sau.

EDIT/DLG-EDIT cần đo nguyên từ Khoan thực, cue nghe, toàn đường release/retract, điểm nghỉ và joins; tính bảng thời lượng thực cùng mọi câu/hành động còn lại. Chỉ trim idle dư sau khi thấy động tác đủ. Không tăng speed/pitch, cắt âm/cuối câu, bỏ phản ứng, freeze, chèn im lặng, lấy food cover hoặc sửa A/C02 để ép số. Nếu bảng thực vượt30s, root trình conflict và lựa chọn phân bố trước mở sản xuất phụ thuộc; DIR không tự cấp ngoại lệ30s hay thay chuyện.

## Đầu vào và cổng cần đóng tiếp

- **DOP:** thiết kế hai composition B-K/B-D cùng trục, rõ mắt–miệng Khoai và mặt–tay Đào; xác định refs cần chuẩn bị. Hai ảnh đã xem là nguồn trạng thái, không tự là ref góc mới ready. Lượt DIR này không tạo/sửa thêm ảnh.
- **ACT:** đặc tả observable cue nghe→dừng→release→retract, động tác tiếp qua cut, sắc ngắt thân mật và nghe không lời. Khóa Khoai tay nghỉ; xác định end rest về C02F0.
- **EDIT/DLG-EDIT:** dựng shot/line/state map, ghi timing conflict bằng actual sources. Chưa có new native nên ranges/cut chính xác là UNKNOWN.
- **CTD/PROMPT:** kiểm cách thực thi coverage dưới quyền hiện hành; prompt/input/config/quote và thử có tiêu chí khác route cũ. Không dùng chữ “exact” làm bằng chứng frame-lock; không hứa tỷ lệ thành công.
- **CONT/FOOD + reviewer độc lập:** kiểm states cả ba joins, vị trí hai tay, food/table drift; SIA/AV/owner checkpoint kiểm đúng Khoan/K20/mouth/cue nghe trên media mới. Source acceptance cũ không thay AV gate mới.

Không cần owner trả lời lại lựa chọn A/B đã chốt. Sau root đọc và tích hợp các vai, review thiết kế/ref đúng scope, xác định được request cụ thể có quote và authority thì mới trình phần production tương ứng. Duyệt hướng A hoặc nhận report này không tự duyệt media, retry cũ, reserve110, C03A hoặc release.

## Tổng hợp vòng DIR

**Đã xác định:** hai lỗi start-pose thật đã khiến route cũ STOP; A80/đíchC02F0 được xem trực tiếp, hashes khớp; B phải giữ mặt người ngắt và causal hearing/release/retract trước ký ức. **Quyết định đã chốt:** owner chọn khám phá coverage A, A/C02 selected giữ nguyên. **Giả định làm việc:** hai shot mới, cùng trục; khoảng2–3s để khảo sát selectedB, chưa được đo. **Còn mở:** composition/ref khả thi, route/quote, actual words/cue/ranges/joins và khả năng vừa30s. **Bước tiếp:** root tích hợp DOP/ACT/EDIT và kiểm độc lập gói thiết kế; chỉ chuyển production khi request/media gates có đủ bằng chứng và quyền tương ứng.

## Phụ lục tích hợp DIR — 08/10/2026, sau đọc brief/DOP/EDIT248 hiện hành

Phạm vi cập nhật: **PAPER_INTEGRATION_AMENDMENT / COMPOSITION_AND_CUE_ONLY**. Đã đọc đầy đủ `00_decisions/C01B-coverage-production-brief-248.md`, `06_qc/C01B_coverage_DOP_248.md` và `06_qc/C01B_coverage_EDIT_248.md` hiện hành. Không xem/nghe lại media cũ, không xem thêm ảnh BM mới trong lượt phụ lục này, không tự chứng nhận draft image hoặc output. Chỉ sửa report DIR được giao. Root cần cập nhật bản report đã sao chép vào archive owner trước phụ lục nếu dùng bản đó để review.

### Coverage đang được tích hợp

**C01A exact → BM asymmetric medium thiên Khoai → BR nguyên góc chung → C02 exact.** DIR đồng ý phương án này có cùng động cơ kể chuyện với đề xuất ban đầu: nhìn người ngắt, nhận phản ứng người nghe, trở về người kể ký ức. BR dùng khung chung và hai still nguồn sẵn có giúp giảm thêm nguồn tái lập bàn/props; đây là lợi ích thiết kế, không bằng chứng model sẽ đạt.

| Shot | Yêu cầu hiện hành thay phần composition cũ | Scope quan sát và điểm nối |
| --- | --- | --- |
| **BM, tương ứng B-K** | Cận vừa bất đối xứng thiên Khoai; mắt/miệng anh rõ suốt trọn “Khoan.”, cùng trục trái/phải, tay anh nghỉ. Không buộc toàn mặt Đào hoặc toàn bàn/hai tay Đào cùng vào khung. | Outer contact ở vành phải có thể ngoài khung: **UNKNOWN, không PASS và không bằng chứng giữ nguyên contact**. State scene vẫn kế thừa A80; phần tay/mặt/props nào lộ phải phù hợp. Ngoài khung không cấp quyền reset hoặc extra action. |
| **BR, tương ứng B-D** | Trở về **nguyên góc chung** có hai mặt, tay và bàn; START exact A80 `02_refs/C01B_START_from_C01A_T04_FLOW_v1.png` (`0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb`), END exact C02F0 `02_refs/C01A_F0_from_C02_T02_v1.png` (`c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`). Không cần BR medium mới để nhấn Đào. | BR phải hiện đúng contact đang có, inner hover gần bát, mắt còn thấp ở entry; sau đó thấy mắt nhận lời→outer release→retract→rest, inner settle inward. Hai refs chỉ là state nguồn/đích; actual start/path/end và ba joins chưa PASS. |

### Cue và cut: điều kiện tránh quay ngược phản ứng

BM giữ trọn từ nói trên hình Khoai rồi cut sang BR ngay nhịp kế tiếp, không thêm hold dài để Đào chờ phản ứng. **BM không được cho Đào nâng mắt rõ về Khoai hoặc bắt đầu buông/thu tay, rồi BR reset về A80 mắt thấp/contact cũ.** Điều này thay đoạn B1/B2 lịch sử cho phép Đào bắt đầu chuyển chú ý/release cuối B-K. Với BR_START exact A80 hiện hành, reaction có thể nhìn thấy phải bắt đầu ở BR, sau lời ngắt đã được nói trọn trên BM.

BR trở lại một contact còn đang được giữ, không phát lại lượt reach của C01A. Đào nâng mắt nhận lời ngay sau cut, nới ngón/rời vành rồi thu tay về bát, không thêm lời hoặc cần nghe “Khoan” lần hai. Nếu actual BM cho thấy eye-lift/release đã xảy ra trong phần Đào còn nhìn thấy, **HOLD dependency/rework trước chạy BR**; không lấy still A80 để hợp thức hóa quay ngược mắt/tay. Nếu BM không cho thấy outer hand, giữ UNKNOWN cho scope đó và bắt buộc kiểm contact/path cùng bản ghép thực ở BR; không tự suy đã diễn sai hay đã giữ đúng.

Không mặc định audio lead/overlap Khoan sang BR, overlay lời lên môi khép hoặc trim speech tail để làm cue sớm. DLG-EDIT đo nguyên âm/diễn phát âm thực rồi chọn cut; nếu full word→reaction đọc thành chậm trong actual join, DIR/ACT/EDIT xử lý từ sự kiện/range thật và trình conflict, không sửa bằng che lỗi. BR giữ im lời và mặt/đường tay rõ; C02 bắt đầu sau release/retract/rest hoàn tất.

### Những phần không đổi và trạng thái bàn giao

A exact3,375s/C02 exact7,541667s cùng hashes trước giữ nguyên; tổng10,916667s trước B. Khoai trái/Đào phải, tuổi/tình bạn, thoại/giọng, cold Nem Bùi/no-steam, bàn/props, F0 và các cấm che lỗi không đổi. B2–3s vẫn chỉ giả định khảo sát, không native range/quote/EDL; không ép1,125s hoặc tự rút nhịp phần sau để đủ30s. STOP T01/T02 không tự được gỡ.

**Disposition:** DIR thống nhất composition và cue với brief248/DOP248/EDIT248 hiện hành; đề xuất BM đầy đủ tay/hai mặt và BR medium trước được giữ làm lịch sử, không dùng làm spec hiện hành. Đây không là approval ảnh BM, quyền chi hai output/trần30, feature Frames, media PASS hoặc nghiệm thu actual joins. Draft BM, feature/input/quote, BM/BR natives, causal timing/voice/mouth và cả ba joins còn phải đóng bằng evidence và checkpoint đúng scope. Root cập nhật archive đã sao chép rồi đọc phụ lục, tích hợp review thiết kế/ref trước production tương ứng.
