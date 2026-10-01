# EP01 — Codex reference static review R1

2026-10-01. `EP01-T2-CODEX-CINE-R1` / CINE-LIGHT / P6–P7 / bounded STATIC_MEDIA_REVIEW. **REWORK for the controlled OPEN→END pair / KEEP_FOR_OWNER_CREATIVE_REVIEW as unselected candidates / NOT_REQUEST_READY**.

## Actual inputs, authority, independence

FIRST trực tiếp xem bốn ảnh qua `view_image`: `media/raw/ep01_t2_references/T2-CODEX-OPEN_v0.3.png`, `T2-CODEX-END_v0.3.png`, approved baseline `media/raw/ep01_p6_food/T-NB-03_v0.8.jpg` (TABLE08) và `media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg` (PAIR03). Mô tả quan sát ở mục dưới được hình thành trước đọc lại brief/approval trong vòng này. Đây cùng context từng paper-review, còn nhớ intent và baseline; không phải blind audience hoặc fresh-context critic.

Đọc FULL trong vòng này: production_team02 common runtime, directing_team01 operating model, audio_edit_quality02 shared contract và09 CINE-LIGHT; sau quan sát ảnh đọc FULL episode101 v0.1 và100.106 đọc phần mở đầu lines1–8 để lấy authority; trong vùng này có maker mô tả route/dependency và run-status, không sử dụng các lời đó làm evidence compliance. Không đọc section actual execution hoặc maker/root findings của106, không đọc105/107 hoặc verdict mới của root. Không kiểm prompt/model/edit history ngoài allowlist.

Authority106: owner “ok” đổi riêng khâu ảnh sang công cụ Codex, cho ảnh/review/chọn; video vẫn Veo, không quyền video/voice/Flow spend/API/CLI mới.100 duyệt shot direction, không chọn các candidate này. Chỉ local view/read/hash/dimension và viết report này; không sửa ảnh, generation, browser, upload, git hoặc credit.

Tự đo bằng System.Drawing và Get-FileHash, không suy metadata từ tên file:

| Actual candidate | Width×height | SHA256 |
|---|---|---|
| OPEN_v0.3.png | 941×1672 | AB492C8CC00C0834B37B732BA2B8EC0598F5AE0B95C4D8ADB2A58D7311CEDBF3 |
| END_v0.3.png | 941×1672 | 7CA642984DC7A5A732DC796C30617E7360099CD46F1E431980290AA81220D91B |

941×1672 gần9:16, không exact9:16 (941×16=15056;1672×9=15048). Không tự crop hoặc gọi exact. Baseline hashes/dimensions đã tự kiểm ở paperreviewR1; vòng này trực tiếp xem lại baseline, không tính lại hash baseline.

## Cold observations trước đối chiếu101/100

**OPEN:** hai người ngồi cùng phía bàn, Khoai trái/Đào phải; nhìn xuống vùng bàn, nét cười nhẹ. Mặt lớn, mắt rõ và texture da nổi; reviewer nhìn mặt trước, rồi món. Hai bát, hai đôi đũa, hai chấm, cốc phải và đĩa lá trái đều có; đĩa món chính thấy toàn và sáng rõ. Lá ngoài cùng sát/tràn biên trái; không có nhiều khoảng thở cho foliage. Nem nhìn như các mảnh/miếng dẹt sáng và hạt bao bên ngoài, khác mound sợi nhỏ ở TABLE08. Nền phố nhiều đèn cam sáng, xe/người blur. Bàn đầy tiền cảnh, không ghế tiền cảnh như TABLE08. Không thấy dấu sao trắng dưới phải của baseline.

**END:** cùng trái/phải và danh mục serving items; tay vẫn nghỉ cạnh bát. Nhân vật/bát/món nằm thấp hơn trong khung, thêm nền/đèn phía trên, giảm phần mặt đứng của bàn ở đáy. Món vẫn thấy toàn đĩa; lá ngoài trái vẫn sát/cắt biên. Khoai đổi hình nét cười/lips và vùng mắt so OPEN; không chỉ một bản dịch pixel. Đào còn rõ, mặt và phần áo/váy nhìn tương tự về tổng thể. Đĩa món vẫn rất nổi; mắt Khoai chưa thành điểm nhấn riêng rõ hơn OPEN đối với reviewer. Không thấy dấu nguồn dưới phải. Không có video để quan sát đường máy.

**TABLE08:** face/meal nhỏ hơn tương đối, nhiều ghế/phần dưới bàn hơn; warm nhưng ít bóng/chi tiết sắc như cặp mới. Đĩa nem dạng mound nhiều sợi/texture nhỏ; đồ chấm và cốc nhỏ hơn tương đối. Người/phố/xe phía sau khác cấu trúc, đèn ít nổi hơn cặp mới. Có dấu trắng hình sao dưới phải. Không lấy quan sát đó để xác nhận recipe hay native provenance pháp lý.

**PAIR03:** mặt, silhouette và trang phục đứng toàn thân trên nền kem; Khoai dark jacket/light shirt, Đào light blouse/green skirt/pink bow. Cặp mới bảo toàn motif này về thị giác; khuôn mặt/texture được render khác. PAIR03 có dấu trắng dưới phải, cặp mới không thấy. Tư thế/nền đứng không phải constraint cho cảnh bàn.

## Capability và coverage sau đối chiếu

| Check | Status / giới hạn |
|---|---|
| Cả hai mặt, full main plate, số serving items | MET ở hai still: đủ hai mặt, main plate, herbs dish, hai chấm/hai bát/hai đôi đũa/cốc. Foliage biên trái cần sửa/kiểm riêng; không blanket full-meal pass |
| Warm light / eyes / food legibility | MET static legibility; tông ấm, chi tiết mắt/món rõ. Cặp mới sáng/bóng và nền đèn nổi hơn TABLE08 là aesthetic difference, không measured exposure defect |
| Attention meal→Khoai eyes | NEED_MORE_EVIDENCE / concern static: OPEN face-first với reviewer, END thêm headroom/background; không đo gaze hoặc audience attention |
| Camera vs scene change | DEFECT ở control nét mặt; geometry changes do camera có thể hợp lý nhưng không chứng minh pure tilt. Không khẳng định mọi dịch chuyển màn hình là object drift |
| Source food preservation | DEFECT visible rendition mismatch so TABLE08; route ART/CONT. Không tự chứng nhận identity/food quantity/exact props continuity |
| Marks / provenance | DEFECT so requirement101 giữ mark; provenance chain/usage UNKNOWN, không suy mark thật/giả từ tên file |
| Motion, flicker, warping, joins, acting, audio, price | UNKNOWN hoặc N/A static scope; không playback/audio/cost evidence, không CONT/PERF/AV pass |
| Production S01/S02/S04/S05 readiness | UNKNOWN: neutral still pair không action keyframes, J23 hoặc full production coverage |

## Findings — actual stills, không timecode video

| ID / severity / kind | Expected / observed / source | Evidence / uncertainty / action, route, closure |
|---|---|---|
| STATIC-01 / MAJOR / confirmed visual constraint mismatch |101 bảo toàn cùng food/source TABLE08. Hai v0.3 render nem thành các mảnh dẹt và hạt lớn rõ, khác mound sợi nhỏ ở TABLE08 | So trực tiếp full plates; chắc cao về khác rendition, không kết luận thành phần/recipe hoặc gram. ART/CONT + owner kiểm lại texture/presentation của exact reference; sửa có giới hạn hoặc owner chốt reference change trước dùng. Closure: actual revision được so baseline, ART/CONT report nếu được giao, owner selection; không bằng prompt “same meal”. |
| STATIC-02 / MAJOR / controlled-pair defect |101 END “No… new expression performance” và giữ state. OPEN→END Khoai có nét miệng/cười và mắt khác, nhất là đường lips sáng/mở hơn END | So vùng mặt trực tiếp; chắc cao rằng hình mặt khác, mức diễn xuất không được PERF certify. Camera projection có thể đổi shape nhưng cặp này chưa chứng minh chỉ do camera. DOP/CHAR/CONT kiểm same face/state, PERF nếu cần ý nghĩa; review revised pair trước video. Closure: matched static pair với thay đổi camera được mô tả, không dựa video chữa. |
| STATIC-03 / MAJOR / mark constraint + provenance unresolved |101 “Preserve source provenance/watermarks; do not erase them”. Baseline có dấu sao dưới phải; cả v0.3 không thấy dấu đó | Quan sát chắc cao về absence, không chứng minh engine cố ý xóa, quyền dùng hoặc native watermark status. Root/RIGHTS làm rõ lineage/usage và owner quyết định cách tuân thủ101 hoặc exception trước request. **Không yêu cầu AI vẽ lại logo/sao rồi gọi native provenance.** Closure: hồ sơ derivative/source minh bạch và cách preservation được phép hoặc change approval thực; mới drawn symbol không đóng finding. |
| STATIC-04 / MINOR / edge framing defect |101 giữ full herbs/serving presentation; v0.3 leaf tips ngoài trái bị biên ảnh cắt/sát biên dù plate vẫn thấy | Direct still view, chắc cao với tips, không coi missing entire herbs dish. DOP/ART giữ thêm margin foliage trong revision, không dời món/đạo cụ để nhét khung. Closure: actual full foliage + plate visible ở cả frames; không tự crop source hoặc add foliage. |
| STATIC-05 / MINOR / aesthetic concern, intent unresolved |101 OPEN meal-entry→END mắt Khoai trọng tâm. OPEN mặt lớn nổi; END thêm vùng đèn/nền phía trên trong khi mắt Khoai thấp hơn khung và món vẫn nổi | Interpretation trực tiếp, không audience fact; dịch xuống có thể là upward tilt hợp lệ nên không gọi camera direction sai chỉ vì tọa độ. DOP trình hierarchy revision vẫn đúng approved direction; owner so hai frames với description attention trước đọc intent. Closure: owner creative choice và sau quyền riêng full-motion review; static approval không motion pass. |
| STATIC-06 / MINOR / format precision |101 target9:16; bytes941×1672 gần nhưng không exact | System.Drawing + integer check; defect chỉ nếu route/request yêu cầu exact, hiện support UNKNOWN. FLOW/root ghi exact dims, trình permitted padding/crop nếu cần và kiểm không mất food/marks; không tự chỉnh. Closure: route acceptance hoặc approved processed file+dimensions. |

Background và serving-item screen coordinates dịch xuống giữa OPEN/END có thể do camera; không có phép registration/calibration nên không khẳng định object relocation chỉ từ chênh màn hình. Nền cặp mới khác TABLE08 và nhiều đèn cam hơn là observed re-render; warmth còn cùng hướng. Không tự kết luận mất geography toàn cảnh hoặc relight technical failure. Identity/quantity giữ UNKNOWN cho chuyên môn CONT dù CINE thấy motif/đếm danh mục vẫn còn.

## Alternatives và disposition

1. Khuyến nghị **bounded REWORK** cặp camera diagnostic: giữ các version này để owner xem; xử lý source-food rendition, same resting expression, foliage margin và source-mark/provenance disposition trước khi gọi paired refs usable. Hệ quả: có version mới và review riêng; không tự retry/generate trong scope này.
2. Owner có thể giữ v0.3 như **creative candidates** để chốt aesthetic warm/gloss/headroom, rồi đặt request reference revision. Hệ quả: vẫn NOT_REQUEST_READY và không sửa baseline approval lịch sử bằng lời “đẹp hơn”.
3. Nếu muốn chấp nhận food/look hoặc mark handling khác101, root trình change rõ và dependencies cho owner/ART/RIGHTS. Hệ quả: đổi reference specification, cần review lại; không âm thầm biến exception thành compliance. Không tự đổi tilt thành zoom/static/cut.

Verdict từng scope: full main plate/two faces + warm legibility **KEEP_FOR_OWNER_CREATIVE_REVIEW**; source preservation và paired resting state **REWORK**; hierarchy **REFRAME proposal / owner decision**; technical light **KEEP static legibility**, không đề xuất RELIGHT như lỗi exposure; camera motion/cut/audio **NEED_MORE_EVIDENCE**. Cặp này **NOT_REQUEST_READY**, kể cả owner thích visual; request/route/rights/count/cost/video authority vẫn gate riêng. Không generation permission hoặc production pass.

## Handoff năm mục

- Đã xác định: actual pair có đủ principal meal items/two faces, cùng left/right và warm clear look; concrete source-food/face-state/mark differences và foliage-edge issue.
- Quyết định đã chốt: authority106 cho image route/review,100 giữ approved shot direction. Reviewer chưa chọn thay owner; báo REWORK cho controlled pair.
- Giả định: một phần screen displacement thuộc camera reframing; chưa camera-only chứng minh và không tự suy object positions drift.
- Còn mở: owner aesthetic/change choices, food/identity/props specialist review, provenance handling, revised refs, route/video request và actual motion/audio/cost.
- Bước tiếp: root đọc findings, trình owner creative candidates + bounded revision choices; chỉ khi cặp usable và request được duyệt riêng mới sang video. Không ghi CONT/PERF/AV/RIGHTS đã chạy vì được route trong bảng.
