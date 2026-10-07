# REC228 — DIR/EDIT/DLG maker: đường sản xuất R01

Ngày 2026-10-07. Local-only; không browser, generation, credit, Git hoặc đọc CONT228. Đã đọc đầy đủ storyboard214, runtime217, approval222, source-map223, hồ sơ227, tài liệu202/221 và manifest202/run-manifest221. Đối chiếu thêm203, approval222, results180/ASR-A03 và SIA221 để phân biệt tiếng đã duyệt với timing thực của B.

## Quyết định hiện hành

Owner: **“Không cần thử tay riêng nữa, làm sản xuất rồi check thôi, chứ k còn ngân sách để thử nữa”.** Đề nghị REC227 ba test tay im lặng bị hủy trước submit; không giữ gate “phải test tay riêng” để tiếp sản xuất. Không đề nghị batch x3 mới. M_v03 đã được duyệt về pose tĩnh. S là nguồn làm việc; E_v02 là candidate đã kiểm, chưa tự nâng thành fullG1.

Giữ C-v0.6, K20/D06, B làm chuẩn riêng EP01 và exact N02 B đã duyệt. Không tuyển giọng lại hoặc hỏi lại quyết định anchor/voice. Lượt này chuẩn bị đường sản xuất và chỉ ra điều kiện khả thi; không tự tuyên bố một route chưa kiểm UI đã giữ được tiếng/miệng hoặc tự dùng số dư làm quyền chi.

## Nguồn thật và kiểm trực tiếp

Đã rehash các file bên dưới, khớp hồ sơ. Đã FFprobe N01 excerpt và B trực tiếp; đã xem fullsize A03f24/1s, A03f48/2s, Bf0 và E_v02. S/M đã được xem và review trong nhiệm vụ225/226/227 của cùng reviewer; nhận xét dưới đây dùng đúng phiên bản/hash đó, không gọi là một lần xem media chuyển động mới.

| Nguồn | Provenance / trạng thái | SHA-256 kiểm trong lượt |
| --- | --- | --- |
| `180_c_v06_dialogue/A03.mp4` | Native nguồn N01/N03/N04; hình thiếu bộ phục vụ, khác món/nền và có caption ở nguồn theo223/180 | `3921e8f9d3a4475bcbd7677f3ca7a180e499adbf432702ccec08aa45dac1620b` |
| `180_c_v06_dialogue/A03_VOICE_REVIEW.wav` | PCM decode A03; toàn nguồn nhiều lượt, không dùng nguyên để đưa N02 cũ trở lại | `9b560b03a98e3d0cd722a0a2877d5395c08110ad2f361230f534d8a8736b3ae0` |
| `183_speaker_audit/N01_intended_Dao_UNVERIFIED.wav` | Trích A03 `[0;2,15)`; PCM16/48kHz/stereo,2,150s. Tên UNVERIFIED là lịch sử;203 đã duyệt người nói/chỗ nối của bản202 chứa toàn excerpt này | `366e95086c57dc1c5d2a2d366d6b24410ab85b0dcc7b2f2d4fbb61d3aa69cfe1` |
| `221_n02_pa_v_trial/N02_B_NATIVE.mp4` | Exact B được222 duyệt toàn frame `[0;240)`/24fps; video10,000s, audio10,005s/48kHz/stereo | `660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535` |
| `221_n02_pa_v_trial/inspection/N02_B_NATIVE/AUDIO_REVIEW.wav` | Decode của B thực; dùng đo timing B, không lấy WAV nguồn200 thay | `bafac31224a35eb80d2121dc05f0e6f5ae4839e6623895a1d51adeff21decb1f` |

Tất cả đường dẫn trên nằm dưới `C:/Users/PC/Downloads/du_an_nem_bui/`. Approval203 thuộc bản nối202; approval222 thuộc exact B mới có timing cục bộ khác nguồn200. Không suy hai approval làm tiếng N02 của WAV202 thành giống B.

Ảnh S/M/E:

- S_v01: `224_g1_opening_refs_v01/REF01-S_v01_NATIVE.jpg`, hash `eba9a13c86f359df458022a5a54664264e5bb29fcca08d6181454cb1ee482422`.
- M_v03: `226_ref01_m_v03_from_s/REF01-M_v03_NATIVE.jpg`, hash `66defd18afc0845da8b34968446b98f547dcad951e6712e2e6a81ff2d5e2017c`.
- E_v02: `225_g1_repaired_refs_v02/REF01-E_v02_NATIVE.jpg`, hash `8df19973fa6595cd166cab67b08a2009256091fb05bf14be322b1371308dbc03`.

S/M Flow asset riêng đã tách tại227. Chưa có hồ sơ slot E trong route sản xuất mới. Không nhét ba ảnh vào hai slot start/end rồi cho rằng M đã được ràng buộc.

## Thiết kế request sản xuất cụ thể

**Ưu tiên một request sản xuất có tiếng nguồn N01 và mặt Đào nói, x1, thay hình A03 bằng chuẩn B.** Request phải làm đoạn có khả năng dùng trong phim, không quay lại test tay im lặng. Route ưu tiên để root kiểm là **video visual repair / audio-driven edit** với một nguồn N01-only; họ route video ingredient Omni1.1 Flash đã chạy tại221 là căn cứ cần khảo sát, không phải bảo đảm cấu hình2,15s hoặc audio+frame hiện hỗ trợ.

Gói nguồn local cần chuẩn bị trước preflight: một derivative N01-only từ A03, giữ đúng tiếng excerpt `[0;2,15)`, có manifest native/audio hash và thời gian; không tải full A03 làm ingredient rồi để model nói lại N02 cũ. N01 WAV đã có nên không cần thu tiếng mới. Nếu cần guide video với ảnh S/E, phải ghi rõ đó là guide chưa có lipsync; không gọi guide thành sản phẩm. Lượt maker này chưa tạo derivative hoặc guide.

Brief sản xuất để chuyển thành prompt/request:

| Thành phần | Chỉ đạo cụ thể |
| --- | --- |
| Lời/voice | Đào nói duy nhất “Anh nhìn mãi. Không hợp thì để em.” theo tiếng N01 đã có và D06 được giữ. Không prompt model thu giọng nữ “giống D06” từ mô tả rồi coi là khóa voice |
| Khung | Hai người, Khoai trái/Đào phải; đủ mặt/mắt/miệng và bàn tay di chuyển; máy khóa cùng phía trục, chuẩn mặt/đèn/nền/món của B |
| S | Mở ở tay nghỉ. Đào nhìn Khoai và nói nhẹ, trêu, không thuyết trình vào camera. Khoai nghe, không mấp máy lời Đào |
| S→M | Trong ý “Không hợp thì để em”, tay ngoài Đào ở phải hình đưa xuống và hơi vào trong quanh ngoài bát đến phía phải vành đĩa. M là pose giữa: ngón cong, gap rõ, thấp hơn đỉnh món, không sau mound. Không cầm/nhấc/chạm món hoặc kéo đĩa khỏi F0 |
| M→E | Cần thấy ngừng ý định và trở lại tay nghỉ để nối B. Timing của việc này phụ thuộc xử lý “Khoan” bên dưới; không khóa một mốc giây tùy ý hoặc làm trước cue rồi gọi là nghe/dừng |
| Môi | Đào vận động môi phù hợp đúng N01; Khoai im trong N01. Khi dùng lời Khoai, Khoai phải có miệng đúng lời và Đào nghe. Hai miệng khép chỉ tại các vùng im đúng nguồn, không throughout như prompt227 |
| Bộ bàn/F0 | Giữ đĩa nguội, rau trước-trái, hai bát trống, hai chén chấm, hai đôi đũa nghỉ, ly ngoài phải Đào; không hơi/khói, ăn/uống/gắp hoặc đồ vật mới |

Không giả route start/end Lite227 có khả năng nhận tiếng N01 và khóa D06. Nếu live route chỉ nhận S/E và tự sinh giọng, nó chưa đáp ứng request này. Không tiêu một lượt “production” thực chất là test im lặng rồi tính thêm lượt lipsync chưa dự toán.

## Điểm nối N01 → đầu N02 B: xung đột thực cần xử lý

Bf0 đã xem: Khoai miệng mở, Đào miệng khép, **tay Đào đã nghỉ cạnh bát**. M khác trạng thái bàn tay đó. E gần bố trí tay nghỉ, nhưng gaze/biểu cảm không trùng tuyệt đối Bf0. Một cut có thể hợp lệ về máy/khung; chưa chứng minh Đào dừng sau nghe “Khoan”.

Storyboard214/223 cần ý định lấy → Khoai “Khoan” → Đào dừng. Exact B từ frame0 đã ở tay nghỉ. Nếu toàn B `[0;240)` phải được dùng nguyên cả hình lẫn tiếng, không thể đồng thời thể hiện pha tay M→E trên cùng những frame đầu ấy bằng một clip mới. Chỉ để S→M cuối N01 rồi hard cut sang B tay nghỉ là thiếu pha phản ứng nhìn thấy; không ghi causal stop PASS. Cho Đào thu tay trước tiếng “Khoan” cũng không được mô tả như đã phản ứng nghe.

Hai cách dựng có hệ quả khác nhau, không phải hai câu hỏi xin chọn lại quyết định đã chốt:

1. **Giữ toàn B nguyên vẹn** — request mới chỉ sản xuất N01. N01 có ý định đưa tay nhưng kết trước cut vào Khoai; việc thu tay có thể bị ellipsis qua cut. Đây là coverage giới hạn, không giữ đầy đủ yêu cầu “thấy nghe rồi dừng” của214/223. Chỉ được nhận dùng nếu root ghi cụ thể trade-off ấy và giải quyết phạm vi nghệ thuật; không âm thầm gọi là đã đạt toàn beat. Không tách/thu lại “Khoan”.
2. **Giữ B làm nguồn audio exact và phần hình còn lại, thay một prefix hình để thấy phản ứng** — đo prefix chứa trọn “Khoan” từ đúng B, dùng một source sản xuất ghép N01 + prefix B với âm thanh liên tục; generate/repair R01 có đủ Đào nói → Khoai nói → Đào dừng/thu về E. Sau đó nối suffix B gốc ở boundary đã đo. Không retime, không lặp/cắt chữ, không dùng WAV200. Cách này giữ nguồn B và phần còn lại, **nhưng thay coverage đầu B nên không còn toàn native B nguyên vẹn đã duyệt222**. Trong scope hiện giao “giữ N02 B exact”, đây là phương án có blocker về phạm vi, không tự triển khai hoặc gọi approval222 bao phủ AV mới.

**Khuyến nghị maker:** root làm cụ thể timing prefix và source package trước khi chi để biết phương án2 cần thay bao nhiêu hình; chưa trình một con số đoán. Nếu giữ whole-B là ràng buộc tuyệt đối, ghi rõ phép giản lược của phương án1 và giải quyết conflict này trước submit. Owner bỏ test riêng là quyết định về quy trình/budget; không tự cho phép cắt B hoặc thay cơ chế kể chuyện. Không tái hỏi voice/anchor/N02 acceptance.

## Audio timing: việc có thể làm ngay tại local

N01 excerpt dài2,15s, tương đương103.200 sample-frame ở48kHz. Biên này không nằm trên lưới video24fps: frame51 tại2,125s; frame52 tại2,166667s. Khi làm derivative phải giữ nguyên samples lời, tách audio boundary và picture frame boundary trong manifest/EDL; không cắt tiếng theo việc làm tròn frame cho tiện.

ASR-A03 ước lượng N01 cuối ở2,0s và “Khoan” nguồn A03 ở2,2–2,58s. Đây là locator cho nguồn A03 cũ; **không phải cutpoint của B**. A03f48/2s có Khoai bắt đầu mở miệng, chỉ là trạng thái hình lấy mẫu, không xác nhận chữ đang nói. Đoạn0–2,15 đã được owner chấp nhận trong202/203; không bắt owner duyệt lại source ấy vì tên fileUNVERIFIED hoặc vì ASR.

B có timing cục bộ khác nguồn200 theo221; không dùng word-times200 hoặc mốc202 để lấy “Khoan”. Local task cần thực hiện: decode B nguyên vẹn; định vị lời bằng waveform/ASR nếu có rồi kiểm nghe đúng B để khóa onset/offset “Khoan” và pause trước “Mùi”; ghi uncertainty nếu chưa có actual hearing. Đối chiếu hình quanh boundary bằng nativeframe/PTS. Chưa nghe không dùng một boundary giả để tạo R01 prefix hoặc J-cut. Không tự áp crossfade speech, tăng tốc, đổi pitch hoặc thu lại tiếng để ép vừa.

Khi có B audio decode và giữ N01/N03/N04/cụmN05–N07, tổng thời lượng các khối vẫn xấp xỉ22,055s theo metadata, nhưng không còn là PCM bản202 vì N02 đã thay bằngB. Con số này chỉ giúp forecast; không khóa các joins hoặc chứng minh30s vừa acting. Giữ toànB audio10,005s không phải rútB về7s vì có return7s.

## Khả thi, blocker và ngân sách forecast77

Khả thi hiện có: tiếng N01 source, exactB, S/M/E pose, asset S/M riêng và route video visual repair từng chạy. Blocker trước một request production có thể review: route thực nhận được sourceN01-only + reference/hướng hình, duration và giá; quyết định cách giữ wholeB hay thayprefix có phạm vi rõ; actual boundary của “Khoan” nếu dùngprefix; timing tổng và media/package hash. Các blocker này không yêu cầu trả tiền cho test tay mới.

Forecast thấp nhất để thấy mức căng ngân sách, **không phải quote hoặc approval**:

| Đơn vị mới giả định | Số lượt x1 |
| --- | ---: |
| R01 nói + tay trong một output sản xuất |1|
| R03 hỏi/đáp |1|
| R04, R05, R06, R07 |4|
| R09 kết |1|
| Tổng |7|

Nếu mọi lượt thật đều10credit thì7lượt=70, còn7 trên snapshot77, chưa đủ thêm một lượt10credit. R08 giả định tái dùng207/gộpR07, nhưng223 vẫn chưa đóng match/continuity của207; không nhận giả định ấy là footage đã dùng được. Nếu R01 cần riêng motion và lipsync thành hai lượt, hoặc R08 cần lượt riêng:8×10=80, vượt77. Route Omni/audio-driven có thể khác giáLite10; phải kiểm live. Không dự toán hoàn tất bằng giá test227 hoặc lấy77 làm ngân sách chi đã được cấp. Không có x3, không Quality, không retry dự phòng được tự mở.

## Gate sau khi làm sản xuất

Từng output sản xuất phải giữ native/hash, decode và kiểm mặt/acting/đường tay liên tục, FOOD/F0, tiếng actual K20/D06, đúng text/speaker, listener mouth và sync tại đúng phiên bản. Overlay đúng tiếng nguồn lên mặt mới **không đủ xác nhận lipsync**. Nếu output giữ audio sai hoặc timing đổi, không tự chồng N01 gốc lên rồi gọi preservation đạt; cần kiểm AV mới và đóng finding tại nguồn phát sinh. N02 B gốc luôn giữ nguyên file để truy nguyên; derivative/cut không thừa hưởng whole-native acceptance về joins.

Maker này chưa nghe actual audio hoặc xem continuous AV; không motion/voice/lipsync PASS. Runtime217 maker/reviewer độc lập và gates local vẫn áp dụng cho production; không cần một paid test riêng để thực thi review sau production.

## Tổng hợp vòng

Đã xác định: test227 bị hủy; N01 excerpt/hash/source hiện hữu và có approval203; exactB/hash/probe còn đúng; A03 hình chưa match; S/M/E đủ chỉ đạo pose nhưng không phải diễn có tiếng. Đã chốt: production rồi check, giữ kịch bản/voice/anchor/B, x1 theo nhu cầu, không batch thử.

Giả định làm việc: ưu tiên một audio-driven/video-repair request cho R01, giá chưa biết;7đơn vị mới là forecast optimistic. Còn mở: wholeB versus causal M→E coverage conflict, exact“Khoan” timing, live capability/quote của production và budget thực. Bước tiếp theo: root/SIA làm timing và package local, root xác minh route production bằng UI read-only, hoàn thiện request cụ thể với scope/quote rồi xử lý approval chi theo quyền hiện hành; không hỏi lại những quyết định đã chốt, không tiêu cho test tay riêng.
