# REC283 — Phản biện độc lập phương án sửa riêng hình món C05→C06

Ngày 13-10-2026. Reviewer: `food_repair_critic_283`, bounded local role theo REC217. **LOCAL_DOCUMENT_AND_SAMPLED_STILL_PREFLIGHT / CONDITIONAL_PROPOSAL_ONLY / NOT_PAID_GO.** Không tạo ảnh, sửa media, browser/API, chi credit, git hoặc công cụ mới. Không nghe thực, không xem AV liên tục; không cấp audio, lip-sync hoặc toàn phim PASS.

## Kết luận trước

Nguồn joined C05→C06 là lựa chọn hợp lý hơn full C06 native đã có tail không được chọn: target này đúng range và điểm nối owner đã duyệt. Thử sửa vật liệu đĩa + phần A trên đũa có mục đích rõ, nhưng **chưa có bằng chứng Flow sửa được hai vật thể mà giữ nguyên diễn, miệng, tiếng và cut**. Chỉ đủ chuẩn bị một đề nghị có ranh giới và xin quyền riêng; không đủ tự chạy hoặc dự báo xác suất đạt cao bằng số.

Hai điều kiện bắt buộc trước paid request: root xác nhận đúng source/segment và quote live; owner cấp một lượt edit tối đa 40 credit ngoài trần 15/clip REC238. Approval ảnh REC283 không bao gồm quyền này. Không dùng 40 credit như thử riêng món rồi tự chạy tiếp cả phim.

## 1. Tài liệu đã đọc và phạm vi quyền

Đọc đầy đủ REC217, REC281, REC282, `00_decisions/receive-still-owner-approval-283.json`, `06_qc/receive_stills_root_review_282.md`, `06_qc/food_dependency_screening_282.md`, REC232/253/254, `00_decisions/scoped-autonomy-238.json`, acceptance277 và EDL276. Các file tương đối tính từ folder `restart_720p_v1`, trừ báo cáo REC ở folder episode.

REC281 khóa nhịp mới Đào đưa bát và nói N07, Khoai bỏ phần đã giữ vào bát. Đây là thiết kế **cảnh nhận mới**, không chỉ thị bắt video C05→C06 cũ diễn thêm hành động đó. Repair C05→C06 phải kết thúc vẫn đang giữ A; không gửi END v2 làm đích cho nguồn cũ.

REC277 duyệt tiếng/nhịp/điểm nối C05→C06, không toàn phim hay tail C06. REC283 chỉ duyệt ngoại hình món và tư thế ảnh START v1/END v2; không master/canon/movement/voice/seam, paid request hoặc reserve.

## 2. Bằng chứng kiểm thực trong run này

Đã kiểm SHA-256 trực tiếp các file dưới đây và trực tiếp xem hai ảnh thật, START v1, END v2, bốn ảnh encoded join F32/F65/F66/F122, cùng opening F239. Không tự trích ảnh mới; dùng evidence đã có. Metadata 123F/24fps/5,125s/720×1280 đọc từ evidence276 và EDL; **run này không decode lại video**.

| Input | Đường dẫn và SHA-256 đã kiểm |
| --- | --- |
| Target joined đã duyệt | `C:/Users/PC/Downloads/du_an_nem_bui/276_C05_C06_JOIN/C05_C06_5p125S_JOIN_QC_NOT_FINAL.mp4` — `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf` |
| START v1, ingredient dự kiến | `02_refs/RECEIVE_START_food_v1_CHATGPT_FOR_REVIEW_282.png` — `491575988bbbea26e16fda3a7f02401b874f9abcc24eda7cdef340764ab232d8` |
| END v2, chỉ cho thiết kế nhận mới | `02_refs/RECEIVE_END_v2_CHATGPT_FOR_REVIEW_282.png` — `82057aba35ffd8182f4624696d209750767452b842413013bd9d94f87b1a596d` |
| Nem thật 1 | `C:/Users/PC/Downloads/du_an_nem_bui/nembui.jpg` — `a51303f7100edd0944dc00daa19402fecfe24bb0e15a4143da8f8eae7b9e3a2d` |
| Nem thật 2 | `C:/Users/PC/Downloads/du_an_nem_bui/z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg` — `1237956e99458385f95f1edf18e0a98e1bddb777030ac1d69fab05fa7a51d741` |

Encoded sample folder: `C:/Users/PC/Downloads/du_an_nem_bui/276_C05_C06_JOIN/encoded_qc/all_native_frames/`. F là zero-based, tên PNG là F+1:

- F32 `00033.png`: `f1abd8fcc4cd3663d13772a155a739863fd3519ae7d323dedcd1ed9e6bed2dbb`.
- F65 `00066.png`: `6b5ddc28eb8230d8d9eba8b86287d4930859c3f48ff081cc26e63a3610291499`.
- F66 `00067.png`: `56b34ff184d6ca3fab9d70ab0b77f24b98c9b2a3f498b821d8600ad41048f4fa`.
- F122 `00123.png`: `e91ca242818689d617bce9416766e331bb7211a305bc0660238bf3ce4ba34578`.
- Opening F239 `C:/Users/PC/Downloads/du_an_nem_bui/257_BR_PRODUCTION/join_qc/all_native_frames/00240.png`: `53edc80a388555bb90718a2cf27c480a540dc8b0a01735fdc54fdbcd2b28e8bb`.

## 3. Quan sát riêng, không lấy lời prompt làm kết quả

Ảnh thật có thịt/bì rời, dải mỏng cong và mép không đều, lớp thính; ảnh 1 vẫn có miếng thịt khá rộng. Không cần ép tất cả thành sợi siêu nhỏ hoặc viện ảnh 2 để kết luận mọi Nem Bùi chỉ có một cấu trúc duy nhất. Các món khác trong ảnh 2 không thuộc vật liệu cần thêm vào bàn phim.

START được duyệt gần hướng món thật hơn nguồn: đĩa có phần rời và thính, phần trên tips là một nhúm gồm dải thay cho lát đặc. Tuy nhiên nhúm treo trong START trông lớn/dài hơn lát A nguồn, và cả ảnh có thay đổi mặt, chất liệu/ánh sáng, tầm với của tay. **Chuyển vật liệu không có nghĩa sao chép toàn pose hoặc phóng lớn lượng A theo START.** END v2 thể hiện phần nhỏ trong bát và tips trống; không chứng minh bảo toàn lượng liên tục. Owner approval ảnh giữ nguyên, reviewer không mở lại lựa chọn thẩm mỹ chỉ vì những giới hạn kỹ thuật này.

Nguồn C05 F32, F65 và C06 F66/F122 đều còn lát A đặc, cùng đĩa phiến lớn. Ở F122 đũa đã di chuyển về phía bát Đào nhưng A chưa thả. Cốc vẫn nâng tay ngoài, bát còn trên bàn. Prompt repair không được làm Đào đưa bát, thả A, đổi cốc hoặc kéo trạng thái END vào đoạn này.

F65→F66 tại 2,75s là cut thực dù cùng góc rộng, độ đổi hình nhỏ. Gộp nguồn dưới 10s tránh hai request/80 credit, nhưng model có thể làm mượt cut, kéo giãn thoại hoặc tái diễn chuyển lượt. Không suy cut vốn mượt sẽ được edit giữ nguyên.

Opening F239 cũng có đĩa phiến đặc; phù hợp dependency screening282. Repair này thành công chỉ đóng món cho 123F riêng, không chốt hình món toàn 689F đang giữ.

## 4. Rủi ro và điều kiện chặn

| Rủi ro | Tiêu chí kiểm / STOP |
| --- | --- |
| Whole-image ingredient kéo mặt, ánh sáng, pose mới vào nguồn | Video source là authority cho người/camera/tay/bát/cốc. START chỉ authority vật liệu món; không yêu cầu dùng như first/last frame. Drift mặt/miệng/camera hoặc diễn mới → NOT_SELECTED. |
| A trở thành nhiều miếng, dài/phình hoặc bị thả | Chỉ một phần nhỏ trên cùng tips, giữ đường di chuyển và trạng thái chưa thả; không đổi số lượt gắp. Kiểm mọi khung có A, không chỉ F0/Fend. |
| Đĩa đổi nhưng A giữ lát đặc, hoặc A thành mì/giò/đồ nóng | Cả đĩa và A cần cùng vật liệu thịt/bì/thính theo refs; không khói, không món khác. Không dùng mỗi màu vàng làm FOOD PASS. |
| Smooth/re-time cut 2,75s, mouth hoặc speaker bị tái tạo | Đối chiếu toàn target mới với nguồn quanh seam và từng lượt. Đủ N05 rồi N06, đúng Đào/D06 rồi Khoai/K20, âm cuối và sync phải có nghe/xem thực. Transcript/PCM correlation không thay review này. |
| Speech-edit route từ chối | REC232 chỉ chứng minh request có mouth/speaker rebuild đã bị từ chối. Prompt này không sửa speech, không viết lại thoại hoặc rebuild mouth. Nếu từ chối: log exact error/charge; không tự rút clause rồi submit lại. |
| Thành công edit bị suy thành sửa toàn phim khả thi | REC253 edit nhận nhưng không xóa chữ và PCM không bit-exact. REC254 giữ audio tuyệt đối bằng patch áo tĩnh không chứng minh dynamic food patch. Không dùng hai lịch sử làm tỷ lệ thành công. |

Khuyến nghị preflight prompt: nêu rõ **chỉ thay cấu trúc vật liệu món trong đĩa và A đã giữ; giữ vị trí/độ chiếm khung hợp lý của phần nhỏ và số lượt; mọi diễn, timing, miệng, camera, audio và cut theo source; ảnh ingredient không là pose**. Không nhắc hoạt động nhận–bỏ hoặc N07 trong repair cũ. Không hứa prompt bảo toàn được bằng chữ.

### Có cần crop riêng món trước không?

Một crop món sạch, truy được từ START, có thể giảm tín hiệu mặt/pose dư. Nhưng run này **không có thử nghiệm hay live evidence cho thấy crop là bắt buộc hoặc input masks được route hỗ trợ**. Không tự sinh/crop ảnh hoặc chuyển approval sang file khác. Có thể trình whole START với material-only scope trước, root kiểm input/quote/UI; nếu route ép lấy ảnh làm khung đầu/cuối hoặc không dùng được reference riêng khi edit thì HOLD, không đánh tráo thành Frames generation. Nếu chọn crop/asset mới, phải lưu lineage/hash/scope phù hợp trước dùng; crop không tự giải quyết cả phim hay đảm bảo giữ audio.

## 5. Ngân sách và giới hạn quyết định

Sổ REC283: đã chi 217/500; còn 283 = first-pass 82 + retake 46 + post-rough 45 + reserve 110 đóng. **173 credit đã phân bổ không phải quyền tiêu tùy ý ngoài từng bucket/trần.** Giá edit 40 và segment tối đa 10s do root cung cấp từ Google hiện hành; reviewer này không kiểm browser hoặc quote trực tiếp. 5,125s phù hợp độ dài tài liệu, chưa chứng minh route nhận exact file.

Nếu owner duyệt đúng một edit 40 và cho trừ retake: retake còn 6, project spent 257, còn 243 gồm usable allocated 133 = 82 + 6 + 45 và reserve 110. Không mở reserve hoặc đổi bucket ngầm. 173 chỉ đủ tối đa bốn edit 40 về phép cộng, nhưng không đủ để cam kết sửa toàn bộ các cảnh và tạo kết; riêng retake46 chỉ chứa được một edit. Chín nhóm sampled shot sửa riêng 9×40 = 360 không nằm trong 173. Gộp nhiều shot ≤10s là giả thuyết giảm request, đổi lại rủi ro qua nhiều cut và phải có kế hoạch/phê duyệt, chưa là cách đủ ngân sách đã chứng minh.

## 6. Cổng đề nghị và kết luận vận hành

1. **GO local preparation:** đúng hash/range 123F; START v1 material-only, không END; root read-back prompt cùng binding/provenance. Nguồn gốc giữ nguyên.
2. **HOLD paid action:** cần live route/segment/quote/settings, authority một lượt tối đa 40 và bucket cụ thể, không retry. Giá/route/inputs khác gói xin duyệt → không submit.
3. Sau output nếu có: tải exact native giữ nguồn; hash/decode/range kiểm riêng; frame review toàn 123F hoặc toàn duration thực, đặc biệt plate/A/face/mouth/bowls/glass và seam. Timing/số frame thay đổi phải trình conflict, không time-stretch để che.
4. Root/reviewer có thể đóng sampled/full visual scope theo bằng chứng thực. Audio và sync **chưa kiểm trong run này**; owner hoặc reviewer có capability phải xem/nghe đúng output mới, không kế thừa acceptance277 tự động.
5. Chỉ khi một repair đạt đủ scope mới đánh giá route có đáng dùng cho phần phụ thuộc khác, lập lại tổng plan/cost. Một lỗi MAJOR mới → NOT_SELECTED và chẩn đoán, không tự lặp. Không retro-approve failed takes, không đóng FOOD gate toàn phim hoặc cảnh nhận mới từ report này.

**Disposition: CONDITIONAL_PREPARATION_SUPPORTED / PAID_AND_OUTPUT_QUALITY_HOLD.** Điểm còn mở: exact UI route/quote, khả năng bảo toàn source qua cut và dynamic A, acceptance nghe/xem của output, chiến lược sửa những phần món khác cùng ngân sách và cảnh nhận mới. Không có credit debit, audio PASS hay production result từ report.

## 7. Delta sau read-back live của root — quote 12, không lấy 40 làm giá cuối

Root đã cung cấp trạng thái upload hoàn tất và editor asset `/edit/a9912c46-8593-41d0-8d0c-1fe4894169d6`, timeline một clip hiển thị `00:05:03`, model Omni 1.1 Flash, một START ingredient ID `ff0578c3-808f-4504-bd5f-4b294b1c1906`; không END hoặc voice ingredient. Đây là **root-reported live observation**, không phải reviewer này tự truy cập browser. `00:05:03` phù hợp giả thuyết 5 giây + 3 khung tại 24fps nhưng không tự xác nhận fps hoặc output duration.

Reviewer đã trực tiếp đọc đầy đủ exact draft `04_requests/C05_C06_food_only_edit_DRAFT_283.txt`, SHA-256 `332915713148401fe4aacc8ddda761d86c84e5e50cbb2471c2106e854e513faf`. Prompt giữ đúng hai đối tượng món, loại trừ copy pose/lượng/ánh sáng/endpoint, giữ một A không thả và cut, không dựng lại speech hoặc thêm N07. **Đủ scope đề nghị; không là bằng chứng model sẽ tuân thủ.** Không đề nghị bổ sung sửa môi/giọng để làm route nhận vì sẽ lặp khác biệt REC232. Có thể để nguyên draft, không cần sửa thêm chỉ để viết dài hơn.

Đã trực tiếp xem proof `C:/Users/PC/Downloads/du_an_nem_bui/283_REPAIR_PREFLIGHT/Flow_food_edit_live_quote12_283.png`, SHA-256 `d1994f3099127abc13261055f1268dbe5a39795cfb68054c7156246ed9d68e3f`. Ảnh cho thấy source tên đúng, timeline một clip, một thumbnail ingredient, Omni 1.1 Flash và tooltip **“Quá trình tạo sẽ tốn 12 tín dụng”** tại Generate. Không thấy control 720p/x1/source-audio preservation trong screenshot. Prompt hiển thị bị scroll/cắt nên screenshot này không tự chứng minh toàn prompt; exact text/hash và root read-back là evidence riêng.

**Giá published 40 và quote live 12 đang khác nhau.** Dùng quote trên exact configured request để trình cap hiện tại 12; không giữ 40 như chi cuối, không gọi 12 là chắc chắn debit thực hoặc suy toàn bộ edit sau cũng 12. Root chưa submit. Sổ hiện vẫn spent217/remaining283. Nếu đúng một request debit12, trừ retake thì retake46→34, spent229/remaining271, usable161 = first82 + retake34 + post45, reserve110 đóng. Không chi mới từ report, không tăng trần/đổi bucket hoặc batch nhân giá12.

### Gate còn lại: root xác minh và owner chốt khác nhau

- **Root có thể tiếp tục kiểm không trả phí:** exact source/ingredient/provenance, toàn text read-back, model/segment, control hoặc thông tin editor về resolution/output count/source audio nếu có, quote fresh ngay trước submit. Không suy UI editor inherit source720 hoặc giữ tiếng tuyệt đối khi không hiển thị; không dùng DOM thiếu video làm bằng chứng có hoặc không có audio.
- **Nếu không có control/information đó:** ghi rõ `output resolution/count/audio-preservation UNKNOWN`, không gọi package production720/x1 đã khóa. Đề nghị owner **một request capability-bounded tối đa12**, sử dụng source720, chấp nhận chưa xác minh cơ chế output trước submit, không retry, mục tiêu kiểm actual native720 và giữ tiếng/diễn/cut sau tải. Đây là quyết định tiến hành có rủi ro chứ không owner miễn chuẩn chất lượng đầu ra. Owner không đồng ý uncertainty → HOLD, chưa sinh.
- **Không được tự nhờ owner duyệt final720 hoặc audio trên lời hứa:** owner cần thấy unknown cấu hình và sự khác biệt quote trước chọn chạy hay dừng. Quote vượt12 hoặc model/source/bindings thay đổi → STOP và trình lại, không áp giá40 lịch sử vào approval12.
- **Sau nếu có output:** phải đối soát resolution/duration/fps/number of outputs/debit thực, giữ original, đánh giá từng scope mới. Output thấp hơn720 hoặc silence/revoice/re-time không tự nâng/upscale, overdub hoặc gọi đạt; trình đúng sai lệch và không dùng thêm credit. Actual tiếng/sync vẫn cần nghe/xem trên đúng target mới.

Disposition delta: **PROMPT_AND_LIVE_QUOTE_EVIDENCE_REVIEWED / CONFIGURATION_UNCERTAINTY_AND_OWNER_ACTION_HOLD.** Không có paid GO, kỹ thuật output, audio hay AV PASS. Các cảnh món khác và cảnh nhận mới vẫn chưa được sửa.
