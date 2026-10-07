# REC229 — DIR/EDIT/DLG maker preflight local

Ngày: 2026-10-07. Phạm vi: review gói chuẩn bị R01 production, không self-quality PASS. Không đọc CONT229; không browser/upload/generation/chi/API/Git, không sửa nguồn hoặc cài mới.

## Kết luận

**PREPARED / HOLD_BEFORE_PAID_SUBMISSION cho các điểm preflight còn mở.** Phạm vi thay picture quanh “Khoan” đã được owner duyệt; không hỏi lại quyết định này. Source package có tiếng nguồn đúng và một brief có đủ Đào nói → Khoai nói → Đào nghe/dừng/thu tay. Đây là đường sản xuất có khả năng dùng trong phim, không standalone test. Chưa có motion, voice, sync hoặc AV PASS.

Cần cụ thể hóa điểm nối thực và vai trò của E so với Bf24, timing phần picture dùng được trước đệm, cùng binding ingredients/quote sau upload. Boundary B1s chỉ provisional từ ASR/silence; chưa nghe nên chưa khóa cutpoint. Owner consent ở hộp quyền upload vẫn đang chờ theo preparation-notes; reviewer không giải quyết hoặc tự bấm đồng ý.

## Tài liệu và bằng chứng thực

Đã đọc đầy đủ `preparation-notes.md`, `source-manifest.json`, `R01-production-prompt-DRAFT.txt` và script `scripts/prepare_ep01_rec229_opening_source.py`.

Đã xem `GUIDE_DIAGNOSTIC_NOT_TARGET.jpg` toàn board, S_v01, M_v03, E_v02 và exact Bf24/1s bằng `view_image`, `detail: original`. Board không có nhãn nativeframe/time, nên chỉ dùng quan sát nội dung, không lấy vị trí thumbnail làm onset chính xác. Không xem liên tục AV hoặc nghe actual trong lượt này.

Đã rehash 4 sources và 2 artifacts: **6/6 khớp manifest**. Đã độc lập đọc WAV và so PCM theo ranges: N01 `[0;103200)` nối B_PCM `[0;48000)` khớp toàn sidecar151.200sample-frame,48kHz,2channel,16-bit,3,150s. FFprobe guide:360×640/24fps,96frames/4,000s; audio48kHz/stereo/4,000s. Đây là kiểm kỹ thuật, không chứng nhận nghe hoặc sync.

| Artifact | SHA-256 đã xác minh |
| --- | --- |
| A03 native | `3921e8f9d3a4475bcbd7677f3ca7a180e499adbf432702ccec08aa45dac1620b` |
| N01 excerpt | `366e95086c57dc1c5d2a2d366d6b24410ab85b0dcc7b2f2d4fbb61d3aa69cfe1` |
| Exact B native | `660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535` |
| B_PCM WAV | `bafac31224a35eb80d2121dc05f0e6f5ae4839e6623895a1d51adeff21decb1f` |
| Exact combined PCM sidecar | `594e815ec69ee0e10e5881bceb20470ec09e54fcda61704d80439a4c157adfb4` |
| Upload guide MP4 | `1ecc6b496291179ce1f5e82153883e2df826b8cf3d7bfdd64edca2a78530b82f` |

Sau thông tin root cập nhật, đã đọc đầy đủ prompt hiện hành và tính lại hash: `1085c89be58aee20340443a2a6ff42623ae0a085a81e29b9549c897515eed1ed`. Bản này bổ sung bỏ mouth motion sai của guide và xác định E chỉ là resting-hand reference. Bản đầu review có hash `44a4caba6a9c4d39a62555a45e4b7f1e01ab0d8257f9f6e92b44c3dcce1c27ff`; các kết luận dưới đây áp dụng bản cập nhật. Chưa submit.

## Findings trước submit

Mức MAJOR ở đây là blocker của thiết kế hoặc kiểm trước chi, không phải confirmed defect của output chưa được sinh.

| ID / mức | Expected → observed | Sửa trong scope / điều kiện đóng |
| --- | --- | --- |
| EDIT229-01 / MAJOR / timing-boundary OPEN | Prefix B phải chứa trọn “Khoan” và đủ phản ứng trước trở lại memory. Package dùng1s vì ASR0–0,34 và next word1,10; silence dưới ngưỡng0,364292–1,209979. Chưa hearing; silence threshold có thể bao gồm âm nhỏ. Mốc1s không được xem là boundary đã nghiệm thu | Giữ1s là candidate có uncertainty, không tự khóa. Trước khi khóa range/master, kiểm actual audio đúng B quanh cue/pause/next word và AV output. Nếu chưa có hearing trước submit, root phải ghi rõ đang sản xuất với candidate1s có rủi ro; không trình “đã khóa cutpoint”. Không kéo/thu lại tiếng hoặc cắt theo ASR một cách tự động |
| EDIT229-02 / MAJOR / usable-tail OPEN | Beat stop-return phải hoàn tất trong phần hình dùng trước nối B, không ở frame cuối4s. Prompt nói complete “approximately3.150” rồi hold0,85. Một lần hoàn tất sát3,15 hoặc trong đệm không cung cấp biên dựng an toàn | Làm rõ return/settle phải hoàn tất **trước đoạn picture dự định cắt**, có ít nhất một nhịp nghỉ đọc được trước join. Chỉ phần0–khoảng3,15 được dùng nếu join B1s; không tận dụng đệm để đẩy action muộn rồi lặp/retime tiếng. QC ghi first frame hand-rest, stop cue và last usable frame; nếu chỉ đạt ởđuôi4s, chưa đạt range đề nghị |
| EDIT229-03 / MINOR / specification FIXED, media join UNKNOWN | Final posture phải nối Bf24 thực. E có gaze hướng nhau và Đào trung tính. Bf24: Khoai gần khép mắt/nhìn thấp, Đào hướng thấp-trái và cười nhẹ; tỷ lệ khung native 360×640 so refs 768×1376 khác nhau | Prompt cập nhật đã ghi E **ONLY resting-hand reference**, không khóa eye expression/camera scale: đã sửa nhầm vai trò reference ở brief. Chưa có output để khẳng định gaze/framing match. Bf24 chỉ là candidate join; root kiểm exact output trước/sau cut, không hứa match từ hai ảnh tĩnh. Chưa cần ép biểu cảm E thành blink của B hoặc đổi memory tiếp sau |
| EDIT229-04 / MINOR / compressed acting risk | Reach phải là động tác đọc được, không snap/teleport. Prompt chỉ bắt đầu “as she offers để em”; locatorA03 cũ đặt cụm này ở khoảng1,62–2,0, cue B đặt2,15, nên reach và stop có thể rất ngắn. Stop-return có khoảng1s sau Bstart | Cho ý định/khởi đầu chuyển tay xuất hiện trong vế “Không hợp thì để em”, rồi tới M khi offer kết; không cần đợi riêng âm “em” mới bắt đầu. Đây là chỉ đạo diễn trong cùng lời, không sửa text/timing. Dừng theo **supplied male cue thực**, không bắt động tác vào timestamp mô tả nếu onsetaudio khác |
| EDIT229-05 / MINOR / brief strengthened, output UNKNOWN | Guide là audio/timing source; đầu ra phải đồng nhất B/S. Board có A03 thiếu bộ bàn, ụ món/nền khác, mouth motion nguồn gần boundary có nguy cơ sai speaker; sau đó hard cut sang B tay nghỉ. Script không chứa motion S→M→E | Prompt cập nhật đã yêu cầu không copy mouth motion nguồn, dựng mouth từ actual audio và speaker map. Đây là sửa brief đúng phạm vi, chưa chứng minh output làm được. Cần actual S/M/E attached và mapping verified trước submit; M là midpoint, E là hand-rest. Nếu route không nhận đủ refs, không dùng riêng tên trong prompt để giả ingredients hiện hữu |
| EDIT229-06 / MINOR / audio preservation risk | Voice/timing giữ đúng nguồn và masterBPCMcontinuousonce. Upload guide AAC lossy, sidecarPCMexact; script encode192k và pad4s | Không gọi upload AAC là exactPCM. Sau output decode/audio nghe+alignment; nếu master dùng nguồnPCMoriginal, kiểm sync actual với hình mới, không coi overlay là closure. Guide suffix0,85 chỉ padding, không thànhpause mới trướcmemory |
| EDIT229-07 / MAJOR / live gates OPEN | Route/ingredients/quote phải verified và consent upload giải quyết trước chi. Notes chỉ ghi Ingredients → Omni 1.1 Flash → 360p/4s/x1; video upload chưa qua hộp quyền sử dụng, giá chưa xác minh | Root tiếp upload sau owner consent đúng gate hiện hữu, kiểm preview/chips UUID/names/prompt hash/route/cost/output x1. Không suy giá Lite227 sang Omni229 hoặc số dư77 thành quote/quyền chi. Không batch x3, retry hoặc test riêng |

## Mốc picture và audio phải tách trong EDL

Audio đổi từ N01 sang B tại2,150s, tức103.200samples. Mốc dùng prefix1s đưa theoretical join tới3,150s. Hai mốc không nằm trên grid24fps:2,15×24=51,6;3,15×24=75,6. Script `fps=24` làm tròn picture, không dịch PCM. Không gọi guide hardcut picture/audio là cùng boundary tuyệt đối.

Nếu output cũng24fps, frame75 tại3,125s và frame76 tại3,166667s. Root cần EDL ghi picture boundary đã chọn và audio offset độc lập, giữBPCMcontinuousonce; không cắt/thêm một sample lời để khớpframegrid. Nếu bắt đầu Bf24 sau frameboundary3,166667 thay vì3,15, khoảng chênh16,667ms cần ghi và kiểmAV, không gọi đã sample-frameperfect. Chưa chọn một giải pháp grid bắt buộc trong report này vì FPS/output thực chưa có.

Master audio đúng: N01 whole → B whole; prefix B trong guide chỉ là input sản xuất, không append thêm vào B whole để lặp “Khoan”. Audio output4s không tự được dùng nguyên: có padding và có thể đổi tiếng. Picture sau candidate join là B gốc với native range thực; không thay/mix toàn memory hoặc đổi playback speed B để cứu action.

## Thứ tự acting và QC production

Prompt có logic một tay ngoài, gap với plate, không prop drift: Đào nói N01/Khoai nghe; Khoai nói “Khoan”/Đào nghe kín miệng; dừng rồi return. Đào vốn nhìn Khoai trong S/M nên “glances at Khoai” không tự là cue rõ; quan hệ nghe nên đọc qua stop sau onset male, phản ứng mắt/tay ngắn và return, không quay đầu lớn hoặc phản ứng thắng/thua.

Tay ở M che một phần bát. QC cần xem liên tục toàn quỹ đạo và frame vùng che, tách occlusion hợp lý với nhập hình/xuyên gốm. Không cho PASS3D từ hai ảnh đầu-cuối; không đoán collision khi ngón/tay bị che. Kiểm không chạm plate/food, không cầm đũa/ly và bát trống F0.

Đây là một candidate production x1. Sau khi có media, DIR/EDIT/DLG và reviewer độc lập kiểm native/hash/range, thực nghe/AV đúng speakers/voices/wording/sync, hành động causal, final rest và join new picture → B memory. Native frame đẹp ở cuối4s không đóng lỗi diễn ra đầu clip hoặc trước join. Không thừa acceptance whole-native222 cho join mới; không hỏi lại acceptance B đã chốt.

## Tổng hợp

Đã xác định: source/artifact hash6/6, PCM sidecar khớp samples, guide4s đúng metadata; phạm vi visual prefix đã được cấp, production-only. Prompt cập nhật đã xử lý nhầm vai trò E và cảnh báo mouth motion sai của guide. Đã chốt: exact B audio và memory picture sau nối giữ; K20/D06/text/B baseline giữ; không test/x3.

Giả định:1s là candidate prefix, output4s chỉ cung cấp khoảng3,15s useful coverage và tail đệm; route có thể repair picture theo audio/ref nhưng chưa verified. Còn mở: actual cue boundary, readable stop-return trước join, gaze/framing tại exact join, rights consent, ingredients/quote actual, output AV. Bước tiếp: root ghi rõ timing/EDL candidate; giải quyết gate upload/live price; một production x1 nếu có quyền chi phù hợp rồi review media actual. Không self-quality PASS.

## Delta read-back — prompt cuối

Đã đọc đầy đủ prompt cuối và tính lại SHA-256, khớp giá trị root gửi: `98ee8c606585da5e8e07bb66199f85a368c25d4b9b80d131d972e0363fde8b29`. Đây là bản hiện hành thay các prompt hash ở phần lịch sử trên; không mở rộng task hoặc kiểm media mới.

| Finding / thay đổi | Disposition tại brief cuối | Giới hạn còn giữ |
| --- | --- | --- |
| EDIT229-02 — usable tail | **FIXED_AT_BRIEF**: hoàn tất stop-return và settle BEFORE3,000s, có nhịp tay nghỉ trước join candidate khoảng3,150s; không hoàn tất trong padding | Output acting/timing UNKNOWN. Chỉ đóng lỗi diễn thực khi native output có đủ stop, return và rest trước range dựng đã chọn |
| EDIT229-04 — reach bị dồn cuối lời | **FIXED_AT_BRIEF**: bắt đầu reach trong vế “Không hợp thì để em”, không đợi âm cuối hoặc snap tay vào M | Quỹ đạo và diễn thực UNKNOWN; không retime tiếng hoặc tự nhận khoảng0,85s sau cue đủ vì prompt đã viết |
| Padding vào master | **CLARIFIED**:0,85s cuối chỉ tool-input padding, không đưa vào master | Giữ source B PCM liên tục đúng một lần. Không dùng đệm để lấp thời gian hoặc kéo dài pha return |
| Native watermark | **CLARIFIED**: cấm chữ/logo/subtitle thêm, giữ mandatory native provenance/watermark | Không coi watermark native là vi phạm yêu cầu “không added text”, không xóa hoặc sửa nguồn |
| E / mouth nguồn guide | Giữ các sửa trước: E chỉ hand-rest pose; bỏ mouth motion sai của guide, theo actual audio và speaker map | AV/speaker mouth/sync và join gaze/framing UNKNOWN; không tự quality PASS |

Disposition hiện hành: các sửa thiết kế EDIT229-02/04 đã được đọc lại và đóng **ở phạm vi brief**. Boundary B1s vẫn **PROVISIONAL**; actual hearing chưa có. EDIT229-01 và EDIT229-07 cùng các unknown output/join vẫn giữ theo trạng thái đã ghi, không tự nâng thành READY_TO_SUBMIT hoặc motion/AV PASS. Scope owner đã duyệt thay picture quanh “Khoan” giữ nguyên, không cần xin lại scope này từ delta brief.
