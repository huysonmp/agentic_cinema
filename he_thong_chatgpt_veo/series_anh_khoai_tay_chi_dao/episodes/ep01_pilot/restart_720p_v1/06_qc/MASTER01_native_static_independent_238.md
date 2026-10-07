# MASTER01 v1 — Review độc lập trên ảnh native thực

**Run:** `EP01-720-MASTER01-NATIVE-STATIC-238`

**Ngày:** 07/10/2026, Asia/Saigon. **Vai:** CONT/FOOD reviewer độc lập.

**Mode:** `COLD_NATIVE_IMAGE_REVIEW_THEN_COMPARE_SOURCE_AUTHORITIES`.
**Disposition:** `REWORK` trong scope ảnh tĩnh: **một MAJOR chặn dùng v1 làm master production về chất liệu nem; hai MINOR về margin và tỷ lệ file**. Không thấy CRITICAL. Owner checkpoint vẫn `PENDING`; không phải motion, voice, lip-sync, toàn phim hoặc release approval.

## 1. Phạm vi và trình tự thực

Đã xem `MASTER01_v1_NATIVE.jpg` trước khi đọc prompt cuối hoặc mở lại source, không nhận maker rationale/report. Sau cold interpretation, đã tự mở PAIR03, TABLE08 và ảnh thật `nembui.jpg`, đọc toàn bộ `MASTER01_prompt_v1.txt`, kiểm hash và kích thước native. Đã đọc registry đúng đường `06_qc/run-registry-238.json`: run được đăng ký trước dispatch, chỉ local read/view và viết report này. Không browser, generation, API, credit, Git, source edits hoặc chọn ảnh thay owner.

Hợp đồng PROD7/02, DIRECT01 và AG-CONT-01 cùng authority45/78/236/REC238 đã đọc ở run preflight ngay trước run này; giữ đúng giới hạn scope. Các source roles hiện hành: PAIR03 identity/outfit; TABLE08 địa lý bàn/quán/ánh sáng/ụ gọn; ảnh thật chỉ chất liệu món. Prompt là expected intent, không là bằng chứng ảnh đạt.

| Đầu vào thực | Phiên bản / SHA256 |
| --- | --- |
| `02_refs/MASTER01_v1_NATIVE.jpg` | v1; `816ea0a17a0351e09ef443c4ef8d9fc8b79247f8fab0d9609e25298de50aee65` |
| `02_refs/MASTER01_prompt_v1.txt` | v1; `676dd8e1375f9cdcd65f9412e33dc79e1d9f890bb137ac31ffbce893ce8e45e8` |
| `media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg` | PAIR03; `ecfbe7a3c543730c268a77ca08d508147115ca804154f85ebdbb38c5c601e8c7` |
| `media/raw/ep01_p6_food/T-NB-03_v0.8.jpg` | TABLE08; `aeb6dfaee1773109243f9f952235a44f2417c6fb7fb4faf15be61c34ca40d924` |
| `C:/Users/PC/Downloads/du_an_nem_bui/nembui.jpg` | Ảnh thật owner cho dùng; `a51303f7100edd0944dc00daa19402fecfe24bb0e15a4143da8f8eae7b9e3a2d` |

Đường media tương đối từ thư mục series. Kích thước native đọc trực tiếp bằng metadata ảnh: **768×1376**. Vị trí dưới đây theo screen và vùng ảnh; không bịa frame/timecode vì target là một still. Công cụ xem đã hiển thị toàn native và cả ba source; không có video/audio/UI để đóng các scope tương ứng.

## 2. Cold interpretation — trước khi đối chiếu intent

Hai nhân vật quả/củ có tạo hình 3D ngồi cùng cạnh bàn ở quán ven phố. Khoai lớn hơn, bên trái; Đào bên phải nhìn về anh. Cả hai có vẻ thân thiện, môi khép. Khoai nhìn xuống vùng bàn/món; bàn tay hai người đặt trên mặt bàn, không cầm đũa hay thức ăn. Khoảng ngồi không tạo gesture tình cảm; không thấy ôm, tựa đầu hoặc đút ăn.

Trên bàn nhìn thấy một ụ món vàng-beige giữa đĩa, một đĩa lá/rau trước-trái, hai bát rỗng, hai đĩa chấm, hai đôi đũa đặt nghỉ và một cốc nước ngoài phải. Ụ món có nhiều sợi cong nổi bật, tiết diện và độ dày tương đối giống nhau, bề mặt hạt vụn; đọc giống một đám mì phủ vụn hơn là hỗn hợp miếng thịt/bì đa dạng. Một vài miếng rộng hơn có xuất hiện nhưng không chi phối nhận diện. Đây là nhận xét thị giác, không phải kết luận về thành phần thật hoặc công thức.

Hai mặt/mắt đầy đủ, ánh sáng ấm và tay đọc rõ. Đĩa lá/rau bị cắt ở biên trái; cốc áp sát biên phải. Nền trên chiếm diện tích đáng kể và được làm mềm. Có watermark nền tảng ở góc dưới-phải; không thấy overlay chữ tự thêm.

## 3. Đối chiếu nguồn và coverage

| Rule / kết quả | Bằng chứng trên native và đối chiếu | Giới hạn |
| --- | --- | --- |
| CONT-1 identity / MET, ACCEPTABLE_VARIATION | Vùng hai đầu: Khoai giữ vàng lấm tấm, mày dày, mắt nâu, silhouette khoai; Đào giữ rãnh đào, cuống/lá, mắt nâu/lông mi. Jacket xanh than/sơ mi kem và blouse kem cổ/nút, váy sage/nơ hồng đất nhận ra theo PAIR03. Thay gaze và pose ngồi không tự là identity drift. | Không chứng minh consistency đa góc hoặc pixel-identical. |
| CONT-1 adult/friends / MET trong scope visible | Trang phục và ngữ cảnh đọc như hai người bạn theo baseline stylized đã duyệt; không thấy marker rõ buộc kết luận trẻ em hoặc romance. Chênh cỡ Khoai/Đào có ở source. | “Adult” ở prompt không tự chứng minh tuổi; đây là nhận định tạo hình tĩnh, không phải audience test. |
| CONT-3 F0 / MET | Cả hai miệng khép; cả bốn tay nằm trên bàn, không có món hoặc dụng cụ đang cầm. Hai bát thấy rỗng; nem còn trên đĩa. | Không chứng minh grip, reach, cue, đường A/B hoặc chuyển trạng thái tương lai. |
| CONT-3 serving/geography / MET về count/trục; MINOR về khung | Khoai trái/Đào phải cùng cạnh; món giữa; rau trước-trái; bát cá nhân trước đúng người; đĩa chấm trái ở giữa bát Khoai và đĩa nem, đĩa phải ở trước-phải nem. Đũa Khoai trái bát anh, đũa Đào phải bát cô và phía trong cốc. Một đôi/người, một cốc đúng phía. | Không thêm đồ để chữa crop; margin chưa đạt ở biên. |
| CONT-2 food / DEFECT MAJOR | Vùng ụ nem ở nửa dưới trung tâm: nhiều sợi cong dài, khá đồng đều; thiếu ưu thế của miếng/dải dẹt không đều và khác texture thấy trên ảnh thật. Hình này gần texture TABLE08 hơn nguồn material thứ ba. | Có phủ hạt/beige và vài miếng rộng; không nói mọi sợi đều sai hoặc món thật không có dải bì. Lỗi là tổng thể nhận diện còn thiên về mì. |
| CONT-2 cool/presentation / MET | Không thấy hơi nóng/khói quanh đĩa; giữ ụ gọn giữa đĩa, rau tách riêng. Không nhập lá xếp vòng và đồ nền ảnh thật. | Still không chứng minh nhiệt độ thực; chỉ kiểm absence of visible steam. |
| CONT-4 composition/light/provenance / MET từng phần | Mặt/mắt hoàn chỉnh, tay sáng đủ, ánh quán ấm; nền mềm; giữ watermark. | Margin phục vụ chưa đủ; tỷ lệ file chưa đúng tuyệt đối9:16. |
| CONT-5 traceable repairs / OPEN | Exact native/prompt/source hashes đã có; findings gắn đúng v1. | Chỉ đóng khi có candidate mới/hash và reviewer xem lại vùng sửa cùng các invariants. |

## 4. Findings và remedy theo scope

### FOOD-M01 — MAJOR, chặn dùng v1 làm master về food fidelity

**Vị trí:** đĩa nem trung tâm, chủ yếu lớp trên của ụ món. **Expected:** ảnh thật có nhiều miếng thịt/bì dẹt, rộng-hẹp và chiều dài không đều, lớp thính phủ bề mặt; giữ ụ gọn và địa lý TABLE08. **Observed:** phần đọc nổi trội là sợi cong gần đồng dạng, có cảm giác mì/đồ giòn phủ vụn. Prompt đã ghi “not uniform noodles” nhưng native không vì vậy mà đạt.

**Impact:** master này có thể lan sai texture sang các clip và làm miếng A/B thành sợi không rõ. **Route:** ART/FOOD → PROMPT/Flow trong quyền root hiện hành; chưa mở C02 dựa trên v1 này.

**Remedy đề xuất:** tạo revision có mục tiêu ở món, giữ identity/geography/ụ gọn. Làm rõ Image2 không được cấp texture món; nhấn Image3 cho các mảnh/dải dẹt bề rộng khác nhau, mép không đều, sự khác nhau giữa miếng thịt và bì, lớp thính bám bề mặt thay vì các sợi tròn đồng đều. Không thêm lá xếp vòng, ớt trang trí hoặc tăng khẩu phần để giống ảnh thật. Nếu công cụ hiện hành hỗ trợ sửa vùng bằng UI trong scope được root xác nhận, ưu tiên sửa đúng vùng đĩa; nếu không thì tạo candidate mới có kiểm hồi quy toàn scene. Đây là proposal, không phải quyền reviewer tự gọi tool hoặc cam kết fix thành công.

**Owner decision needed:** không cần chọn lại direction để thử sửa lỗi trong scope; owner checkpoint chọn master mới vẫn bắt buộc. **Closure:** ảnh mới có hash; mở thực và đối chiếu food cạnh ảnh thật, đồng thời kiểm mặt/outfit/F0/serving không trôi. Hai output liên tiếp cùng MAJOR thì dừng chẩn đoán theo REC238, không tiếp tục lặp prompt.

### COMP-m02 — MINOR, thiếu margin phục vụ

**Vị trí:** đĩa rau/lá ở mép trái nửa dưới; cốc tại mép phải cạnh tay Đào. **Observed:** một phần viền đĩa/lá vượt khung trái; cốc không có khoảng thở ở phía phải. **Expected:** prompt yêu cầu toàn bộ serving trong khung có breathing room. **Impact:** master khó làm chuẩn đầy đủ, dễ crop sâu hơn khi tạo cảnh dọc; count vẫn đọc được nên không nâng thành MAJOR.

**Remedy:** giữ các vị trí tương đối, điều chỉnh khung/camera để thấy viền plate và cốc có khoảng trống; bớt ưu tiên phần nền trên nếu cần. Không tự dời rau/cốc vào giữa hoặc thu mất mặt để cứu margin. **Route:** DOP/PROMPT; không cần direction mới từ owner. **Closure:** candidate mới thấy đủ viền serving trái/phải và hai mặt/tay, count/geography giữ nguyên.

### FORMAT-m03 — MINOR đối với reference still; chưa phải delivery defect

**Evidence:** native768×1376; tỷ lệ chính xác9:16 ở bề rộng768 tương ứng chiều cao khoảng1365,33. File hiện cao hơn khoảng0,78%. **Impact:** nhãn portrait9:16 trong prompt không xác minh được tỷ lệ file đúng tuyệt đối. Không phải căn cứ gọi ảnh/video720p đã đạt.

**Remedy:** lưu native nguyên vẹn, ghi kích thước thật trong manifest. Nếu cần một derived9:16, root xử lý version riêng và kiểm crop/padding đối với margin đang thiếu; không ghi đè native hoặc cắt thêm đĩa/cốc để hợp số. **Route:** root/CTD/DOP; chưa bắt buộc chỉnh tỷ lệ source trước mọi Ingredients request nếu route thực cho phép. **Closure:** file derived cùng metadata/hash và visual readback, khi thật sự cần.

## 5. Bàn giao

**Đã xác định:** v1 đủ nhận diện hai nhân vật, adultfriends theo baseline, F0 và count/trục serving; ánh sáng và hai mặt/tay rõ. **Đã chốt:** reviewer không chọn master; disposition tĩnh `REWORK` vì FOOD-M01, owner checkpoint pending. **Giả định:** sửa food trong hướng đã duyệt, không đổi plating/scene. **Còn mở:** candidate sửa, margin/tỷ lệ cần sử dụng thực, mọi motion/voice/AV/30giây. **Bước tiếp:** root đọc finding, thực hiện một sửa có mục tiêu trong quyền hiện hành; review độc lập candidate mới và trình owner khi MAJOR đã đóng.

Không dùng preflight paper PASS hoặc prompt compliance để đóng FOOD-M01. Không đưa v1 thành production reference đã đạt chỉ vì face/table đẹp. Báo cáo này chỉ áp dụng exact native/prompt hashes nêu trên.
