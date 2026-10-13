# REC285 — Preflight độc lập tuyến project prompt, chưa trả phí

Ngày 13-10-2026. Reviewer `food_repair_critic_283`, quyền bounded local REC217. **LOCAL_PROOF_AND_INPUT_REVIEW / NEW_ROUTE_PROPOSAL / PAID_HOLD.** Không browser/API, credit, git, công cụ mới hoặc sửa media. Không actual listening/continuous AV hoặc output chất lượng mới.

## 1. Kết luận chính

Tuyến project main composer có video ingredient và cấu hình **Video / Thành phần / dọc 9:16 / Omni 1.1 Flash / 720p / x1** nhìn rõ hơn scene editor REC284. Quote hiện **20 credit**, không phải12. Đây là cải thiện **khả năng quan sát và khóa request**, chưa chứng minh backend nhận request hoặc giữ voice/mouth/cut. Không gọi nguyên nhân gốc REC284 đã được tìm ra hay khắc phục chỉ vì đổi cửa thao tác.

Đủ chuẩn bị đề nghị một request mới với exact inputs/prompt, cap20 và bucket retake; **chưa đủ tự submit**. Owner “ok nhé” chỉ cấp kiểm tuyến không trả phí theo parent context. Approval284 cap12/count1 đã dùng; REC238 max15 không bao gồm request20. Cần owner duyệt riêng một lượt20, không retry và không mở reserve.

## 2. Evidence trực tiếp và root-reported

Reviewer trực tiếp xem `C:/Users/PC/Downloads/du_an_nem_bui/285_ROUTE_PREFLIGHT/Flow_project_prompt_video_edit_quote20.png` và kiểm SHA-256 `d30c36b4c95fcb25fec6f87c931ee9b07953286f40c3b7dcfcb7e0f853711a96`.

Screenshot cho thấy thư viện `Tệp tải lên`, composer có hai thumbnails (một đánh dấu video), menu chọn Video/Thành phần/9:16/Omni1.1Flash/720p/x1, **“Độ dài dựa trên thành phần · 5.14 giây”** và **“Quá trình tạo sẽ tốn 20 tín dụng”**. Các control này không hiện trong proof scene editor284; không dùng hai screenshot như hai giá của một cấu hình giống hệt đã được chứng minh.

Root báo thao tác card upload → More → “Thêm vào câu lệnh”, video ingredient ID `55781f96-55b4-428c-ab54-40f5bc918bc1` có provenance title `C05_C06_5p125S_JOIN_QC_NOT_FINAL`; START ingredient ID `ff0578c3-808f-4504-bd5f-4b294b1c1906`; toàn prompt pasted/read-back không đổi; Agent OFF; chưa submit hoặc debit. Reviewer không tự truy cập browser, không chứng minh IDs/full prompt chỉ bằng screenshot bị menu che.

Đã đọc đầy đủ exact prompt283 và kiểm hash inputs local lại trong run285:

| Input | SHA-256 |
| --- | --- |
| `C:/Users/PC/Downloads/du_an_nem_bui/276_C05_C06_JOIN/C05_C06_5p125S_JOIN_QC_NOT_FINAL.mp4` | `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf` |
| `02_refs/RECEIVE_START_food_v1_CHATGPT_FOR_REVIEW_282.png` | `491575988bbbea26e16fda3a7f02401b874f9abcc24eda7cdef340764ab232d8` |
| `04_requests/C05_C06_food_only_edit_DRAFT_283.txt` | `332915713148401fe4aacc8ddda761d86c84e5e50cbb2471c2106e854e513faf` |

Root báo đã đối chiếu official Google edit16935718, model16352836 và credits16526234 ngày hiện hành. Reviewer này không nghiên cứu web độc lập; quote20 trực tiếp đọc từ local proof. Giá published40, quote scene editor12 và project composer20 đều giữ trong lịch sử đúng từng route/config/thời điểm; chưa xác định cơ chế backend/giá giải thích khác biệt. Không dùng giá40 để phủ định quote20 hoặc lấy20 làm giá mọi lượt sau.

## 3. Prompt và rủi ro còn nguyên

Prompt giữ đúng food-only replacement trên đĩa và A đã cầm, không đổi pose/ánh sáng/lượng/endpoint theo START; không thả, gắp lại hoặc thêm N07; giữ camera, diễn, miệng, tiếng và cut nguồn. Không yêu cầu rebuild speech. Không đề nghị chỉnh prompt thêm chỉ để làm nó khác sau failure chưa biết nguyên nhân.

Tuy nhiên video ingredient **không tự là bản sao pixel/timing**. Model vẫn có thể tạo lại mặt/mouth/voice, smooth seam 2,75s, đổi lượng A hoặc bàn/cốc/bát. Whole START còn tín hiệu pose/mặt dư; material-only instruction giảm xung đột ngữ nghĩa nhưng không là mask/object lock. Không dùng END v2 hoặc voice presets mới vào request này.

Điểm duration: nguồn123F/24fps = **5,125 giây**, UI5,14. Sai biệt0,015 giây có thể do metadata/audio/container/display nhưng **nguyên nhân chưa được kiểm**. Không tự gọi đó là chính xác123F hoặc đã re-time. Root có thể đọc metadata upload/preview bằng UI trước; nếu vẫn không rõ, nêu uncertainty này trong đề nghị. Output phải đo fps/frames/duration/cut và đủ âm cuối, không time-stretch/rút câu để ép khớp.

Không có explicit control “giữ tiếng gốc” được xác minh. Audio icon/control không chứng minh source speech bit-exact. Giữ audio được prompt yêu cầu nhưng khả năng thực hiện chưa chứng minh. Nếu output sinh khác/silence, không tự overdub đè lên mouth lệch hoặc chuyển voice preset rồi gọi source approval còn hiệu lực.

## 4. Budget và gate trước click

Hiện spent217/500, còn283 = first82 + retake46 + post45 + reserve110 đóng. Nếu owner duyệt một request20 và actual debit20: spent237, còn263 = first82 + retake26 + post45 + reserve110. Allocated usable còn153; không tự chuyển bucket. Hiện chưa chi20 hoặc dự trù trả lại từ lỗi284.

Trước submit cần root giữ đủ provenance từ upload title/asset đến exact local source và START hash, fresh quote/config/prompt read-back, account/balance, approval riêng cap20/count1/bucket retake. Quote>20, inputs/model/resolution/output count đổi hoặc Route chuyển sang Frames/new scene → STOP, không dùng permission283/284 thay approval mới.

Nếu owner duyệt tiếp: đây là **một request mới trên tuyến khác**, không là retry miễn phí hay đơn giản khôi phục request284. Không batch/partial trial tiếp hoặc tự sửa prompt và bấm thêm. Net0 ở284 không mở số lượt mới. Sau lỗi tiếp, lưu exact error/debit/history và chẩn đoán; không loại tất cả nguyên nhân bằng cách đổi tab hoặc tăng credit.

## 5. Gate output — chưa thể đóng tại preflight

- Tải đúng native mới nếu có, giữ nguồn cũ, hash/probe/decode; xác nhận actual720×1280, fps/count/duration và actual debit/output count. Paper/config không thay metadata output.
- Visual review toàn đoạn mới, không chỉ poster: đĩa cùng vật liệu A; A nhỏ, chỉ một lần giữ, không thả/gắp mới/phình/khói; giữ bát/cốc/rau/chấm, face/mouth/acting và seam. Kiểm các frame seam theo mapping thực; không tự áp F66 nếu output timing đã đổi.
- Đúng N05 rồi N06, Đào/D06 rồi Khoai/K20, đủ âm cuối, nhịp và sync cần nghe/xem AV thật đúng hash mới. Source acceptance277 không tự truyền. PCM correlation hoặc transcript không thành actual hearing.
- Repair này dù đạt chỉ đóng phạm vi C05→C06 riêng. Các cảnh món cũ khác và cảnh nhận–bỏ mới vẫn cần phương án/quote/budget/approval; không làm lại toàn tập hoặc gọi gói cuối sẵn sàng từ một take.

**Disposition: CONFIGURATION_OBSERVABILITY_IMPROVED / EXACT_PROMPT_SCOPE_SUPPORTED / OWNER_ONE_REQUEST20_AND_OUTPUT_QUALITY_HOLD.** Nguyên nhân gốc284 vẫn UNKNOWN; voice preservation/duration/cut acceptance chưa kiểm; không credit debit, audio/AV PASS hoặc production GO trong report.
