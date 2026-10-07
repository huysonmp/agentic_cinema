# MASTER01 — Preflight độc lập về continuity và món ăn

**Run:** `EP01-720-MASTER01-PREFLIGHT-CONT-FOOD-238`

**Ngày:** 07/10/2026, Asia/Saigon. **Vai:** CONT/FOOD reviewer độc lập.

**Mode:** `PAPER_REVIEW_AND_STATIC_SOURCE_INSPECTION`.
**Disposition:** `PASS_FOR_OWNER_REVIEW` trong phạm vi paper/source; đủ cơ sở chuẩn bị một ảnh MASTER01 mới với các kiểm soát dưới đây. **MASTER01: NOT_CREATED.** Không phải actual output QC, motion PASS, production PASS hoặc owner approval.

## 1. Đầu vào, quyền và khả năng kiểm thực

Đã đọc toàn bộ `agents/production_team/02_common-runtime-contract-v0.1.md` (PROD7-v0.1 và addendum DIRECT-v0.1), `agents/directing_team/01_approval-and-operating-model.md` (DIRECT-v0.1), section AG-CONT-01 trong Tier1 role prompts; kế hoạch236 v1.0, hồ sơ217, authority45, authority78, REC238 và brief MASTER01. Không đọc maker reports, không tự đối chiếu lý do của maker ngoài chính brief được giao.

Quyền thực: đọc local và xem ba ảnh trong allowlist; chỉ viết báo cáo này. Không browser, generation, upload, API, credit, Git hoặc cài đặt. REC238 là authority hiện hành về scoped autonomy, thay quy tắc phải xin lại từng generation trong scope; các dòng lịch sử tại236/217 không thắng REC238. REC238 giữ checkpoint owner duyệt master mới và hai giọng. Báo cáo này không tự sử dụng quyền submit.

Ảnh nguồn được mở bằng công cụ xem ảnh; không chỉ đọc tên file. Hai đường `media/raw/...` được resolve tương đối từ thư mục series, không từ workspace root. Hash dưới đây được tính trực tiếp trong run và khớp brief đối với cả ba ảnh.

| Đầu vào / phiên bản | SHA256 thực kiểm |
| --- | --- |
| `restart_720p_v1/02_refs/MASTER01_BRIEF_DRAFT.md`, DRAFT_FOR_SPECIALIST_PREFLIGHT | `c5221173567b37e504226a59740db54446fb08a96bdbd5aaac9aaeb2481c2a7b` |
| `restart_720p_v1/00_decisions/scoped-autonomy-238.json`, REC238 | `1caa9aaf4de5b491f54779baf895e4eb2c45ac76785533bf3eb0834ad96ea216` |
| `media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg`, PAIR03 | `ecfbe7a3c543730c268a77ca08d508147115ca804154f85ebdbb38c5c601e8c7` |
| `media/raw/ep01_p6_food/T-NB-03_v0.8.jpg`, TABLE08 | `aeb6dfaee1773109243f9f952235a44f2417c6fb7fb4faf15be61c34ca40d924` |
| `C:/Users/PC/Downloads/du_an_nem_bui/nembui.jpg`, ảnh thật owner cho dùng trong dispatch | `a51303f7100edd0944dc00daa19402fecfe24bb0e15a4143da8f8eae7b9e3a2d` |

Không mở demo gốc vì ba nguồn trên đủ cho scope. Quyền ảnh món thật được nhận từ dispatch và brief; run này không là audit độc lập toàn bộ hồ sơ rights. Không có ảnh MASTER01, video, tiếng, UI quote, cloud IDs hoặc request readback để kiểm. Các hạn chế này được giữ `UNKNOWN/NOT_TESTED`, không ghi thành lỗi của output chưa tồn tại.

**Readback khi đóng run:** brief đã được chỉnh cách trình bày tiếng Việt trong lúc review, hash mới `95f3a9fd0a3f255fcfe091766054b61fbce49b1541cfc2dabf68ed7c9b475ef6`. Đã đọc lại toàn bộ bản này: prompt tiếng Anh và direction/source roles không đổi; findings và disposition dưới đây áp dụng cho cả bản readback này. Nếu root tiếp tục chỉnh prompt theo góp ý thì ghi hash mới và closure riêng, không coi report tự động bao phủ mọi revision.

## 2. Quan sát nguồn và đánh giá brief

| Rule / trạng thái | Quan sát thực và ý nghĩa | Handoff / bằng chứng đóng |
| --- | --- | --- |
| CONT-1 / MET ở lớp paper | PAIR03 thấy Khoai có da vàng lấm tấm, lông mày dày, mắt nâu, jacket xanh than và sơ mi kem; Đào đầu đào có rãnh/cuống/lá, blouse kem có cổ/nút, váy sage, nơ hồng đất. Authority45 ưu tiên đúng primary này; prompt giao identity/outfit cho Image1 là phù hợp. | CHAR/CONT đối chiếu chính ảnh mới. Không dùng khuôn mặt nhỏ/đầu lớn hơn ở TABLE08 để ghi đè PAIR03. |
| CONT-1 / MET ở lớp paper | Hai nhân vật trong PAIR03 có tạo hình người trưởng thành, trang phục trưởng thành; không có gesture tình cảm. Prompt dùng “adult”, “two friends”, khoảng tự nhiên và không romantic gesture. Biểu cảm F0 mới không cần sao chép nụ cười portrait. | Candidate phải còn đọc như hai người bạn trưởng thành; tuổi thực/nhận diện nhiều góc không được chứng minh bằng một still. |
| CONT-2 / MET ở lớp paper | TABLE08 có ụ nem gọn giữa đĩa; ảnh thật có miếng và dải không đều, lớp thính dạng hạt/bột, sắc vàng-beige; có cả phần thịt và bì khác cấu trúc. Prompt dùng ảnh thật cho material, không mang lá xếp vòng/đồ nền vào cảnh, là phân vai đúng. | FOOD kiểm texture thật trên MASTER01; thẩm mỹ 3D không được biến món thành mì đồng dạng, viên tròn hoặc đồ nóng. Không suy công thức/định lượng từ ảnh. |
| CONT-3 / MET ở lớp paper | TABLE08: Khoai trái, Đào phải, cùng cạnh bàn, camera đối diện; một đĩa nem trung tâm, một đĩa rau/lá trước-trái, hai bát riêng phía sau đĩa nem, hai đĩa chấm lệch trái-phải, hai đôi đũa nghỉ và cốc ngoài phải Đào. Brief giữ đúng số lượng và trục; F0 bát trống, không cầm món. | CONT kiểm count/vị trí trên output; đặc biệt không biến hai đôi đũa thành đũa cầm cộng đũa nghỉ hoặc đặt cốc giữa hai người. |
| CONT-4 / MET ở lớp paper | TABLE08 có quán ven phố, bàn gỗ, ánh đèn ấm; mắt/tay/serving nhìn được. Prompt khung dọc, đủ hai mặt/mắt/tay và serving, tách nền mềm, không khói quanh món. Không yêu cầu fullbody như PAIR03. | DOP/CONT kiểm headroom, tay không bị che/cắt, mắt Đào còn đọc khi nhìn Khoai, đủ khoảng quanh rau/cốc. Tỷ lệ output và geometry phải đo/quan sát trên file thật. |
| CONT-3, CONT-4 / UNKNOWN với motion | F0 là điều kiện khởi đầu hợp lý nhưng không chứng minh với đũa tới được đĩa, Đào lấy cốc/đưa bát, đường A/B hoặc cut nối được. | Chỉ đóng bằng clip/range/frame thật ở các stage phụ thuộc; approval master không thay review đó. |
| CONT-5 / MET ở lớp hồ sơ | Brief ghi NOT_CREATED và phân biệt source roles, hash, owner checkpoint. Không hứa pixel-identical hoặc motion từ ảnh tĩnh. | Root lưu brief/request version mới nếu chỉnh; report này chỉ gắn hash draft đã nêu. |

Không phát hiện mâu thuẫn nền tảng buộc chọn lại nhân vật, món, quan hệ hoặc serving. Khác texture giữa TABLE08 và ảnh thật đã được brief phân vai: giữ địa lý và ụ gọn của TABLE08, dùng ảnh thật để tránh món quá giống mì. Đây không là quyền đổi presentation tùy ý.

## 3. Chỉnh câu chữ khuyến nghị trước submit

Ba điểm dưới đây là **MINOR ở lớp prompt**, không phải lỗi output được quan sát. Không cần owner quyết định nền tảng mới; root/PROMPT có thể làm rõ trong phạm vi direction đã duyệt và ghi revision.

1. Câu “at the same wooden table” chưa nhắc trực tiếp cách ngồi cùng cạnh/camera đối diện của authority78. Thêm: **“Both sit on the same side of the table, with the camera facing them, preserving Image 2's left-right axis.”** Giữ khoảng tự nhiên nhưng không để model chuyển thành ngồi đối diện hoặc góc bàn khác.
2. “Two dipping saucers” chưa nêu vị trí chi tiết. Thêm: **“Keep one dipping saucer between Khoai's bowl and the central plate on screen left, and the second at the front-right of the central plate. Keep Khoai's resting chopstick pair to the screen-left of his bowl and Dao's pair to the screen-right of her bowl, between her bowl and her water glass.”** Đây là địa lý thấy trên TABLE08; không tự quy định loại nước chấm hoặc lượng ăn.
3. “small loose mixed mound” có thể bị đọc thành rải phẳng, còn “both resting hands” có thể chỉ tạo hai bàn tay tổng cộng. Thay bằng **“a modest compact mound of irregular loose pork and pork-skin pieces with granular rice-powder coating”** và **“Both characters' hands rest visibly on the tabletop, clear of the food, with no utensils held.”** Giữ ụ gọn được authority78 chấp nhận và F0; không ép ảnh thành bốn bàn tay xếp đối xứng để làm đẹp.

Prompt hiện tại đã truyền đạt đúng ý qua chỉ dẫn “Keep Image 2's table geography”; các bổ sung này tăng độ rõ, không phải bảo đảm model làm đúng. Giữ câu “same ... 3D material language as Image 1” để ảnh thật không kéo toàn bộ scene sang photorealism. Không cần nạp demo hay reference thứ tư.

## 4. Disposition và bước tiếp

**Blocker paper/source quan sát được:** không có. **Generation/request readiness chưa kiểm:** thứ tự Image1–3 và chip/cloud IDs, exact prompt cuối, x1, tỷ lệ, quote0 và provenance readback. Plan236 mục5.1 quy định ảnh miễn phí chỉ tạo khi quote thực0; nếu ảnh có phí thì route owner cho khoản riêng, không suy trần15/video của REC238 thành quyền trả phí ảnh.

Root/PROMPT tích hợp các làm rõ phù hợp, version-lock prompt; kiểm request đúng ba nguồn, một output và quote0 theo quyền hiện hành. Sau khi có MASTER01: lưu native/hash, xem thực toàn ảnh, kiểm identity/adultfriends/F0/serving/texture/composition bằng candidate mới, rồi trình owner đúng candidate. Nếu candidate có MAJOR, sửa đúng scope trước mở C02.

**Đã xác định:** ba nguồn có hash đúng và vai trò không chồng lấn; direction master tương thích45/78/236. **Quyết định đang kế thừa:** PAIR03 identity, TABLE08 geography/ánh sáng/ụ gọn, quan hệ bạn bè, F0, owner checkpoint theo REC238. **Giả định làm việc:** ảnh thật phục vụ material và dùng được theo dispatch; không là nguồn plating. **Còn mở:** output mới, rights audit rộng hơn, UI quote/request và mọi performance/motion/AV. **Bước tiếp:** chuẩn bị rồi tạo ảnh trong scope; review actual candidate và owner chọn trước sản xuất phụ thuộc.
