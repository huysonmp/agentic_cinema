# MASTER01 v2 — Review ảnh tĩnh độc lập và đóng lỗi món

**Run:** `EP01-720-MASTER01-V2-STATIC-238`

**Ngày:** 07/10/2026, Asia/Saigon. **Vai:** CONT/FOOD reviewer độc lập.

**Mode:** `COLD_REPAIRED_NATIVE_REVIEW_AND_REGRESSION_AGAINST_SOURCES_V1`.
**Disposition:** `PASS_FOR_OWNER_REVIEW` trong scope ảnh tĩnh, **FOOD-M01 đã đóng trên đúng v2**; không thấy CRITICAL hoặc MAJOR còn mở. **COMP-m02 và FORMAT-m03 vẫn MINOR, chưa đóng; cần ghi rõ khi owner chọn master.** Root/owner chưa approve candidate. Không phải motion, voice, lip-sync, production clip, toàn phim hoặc release PASS.

## 1. Input và khả năng kiểm thực

Đã cold-view v2 trước, sau đó tự mở ảnh thật `nembui.jpg`, v1, PAIR03 và TABLE08 theo thứ tự đối chiếu được giao. Không đọc maker rationale hoặc repair prompt; đánh giá từ ảnh thực. Đã đọc `06_qc/run-registry-238.json`, thấy run được đăng ký trước dispatch. Hợp đồng PROD7/02, DIRECT01, AG-CONT-01 và authority45/78/236/REC238 đã đọc trong các run ngay trước; không mở rộng quyền. Chỉ local read/view và viết báo cáo này; không UI/API/Git/generation/source edits.

| Ảnh đã thực xem và hash thực tính lại | SHA256 |
| --- | --- |
| `02_refs/MASTER01_v2_NATIVE.jpg` | `239e91f53e00de3caeb7d9153c473b6ae4aadcb70945dfe5462a6b8a2d52115f` |
| `C:/Users/PC/Downloads/du_an_nem_bui/nembui.jpg` | `a51303f7100edd0944dc00daa19402fecfe24bb0e15a4143da8f8eae7b9e3a2d` |
| `02_refs/MASTER01_v1_NATIVE.jpg` | `816ea0a17a0351e09ef443c4ef8d9fc8b79247f8fab0d9609e25298de50aee65` |
| `media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg` | `ecfbe7a3c543730c268a77ca08d508147115ca804154f85ebdbb38c5c601e8c7` |
| `media/raw/ep01_p6_food/T-NB-03_v0.8.jpg` | `aeb6dfaee1773109243f9f952235a44f2417c6fb7fb4faf15be61c34ca40d924` |

Source paths `media/raw` tương đối từ thư mục series; `02_refs` tương đối từ restart. Native v2 metadata thực **768×1376**, hash khớp dispatch. Công cụ xem toàn ảnh và nguồn; tọa độ mô tả theo screen/vùng vì đây là still. Không có motion/audio để suy frame/timecode hoặc nghe giọng. Không dùng hash bằng nhau làm bằng chứng thẩm mỹ; mọi kết luận dưới đây dựa vào phần đã xem.

## 2. Cold interpretation của v2

Hai nhân vật 3D bên trái/phải ngồi cùng cạnh bàn; Khoai nhìn xuống vùng món, Đào nhìn anh, cả hai có nét thân thiện và môi khép. Bốn bàn tay nghỉ trên mặt bàn, không cầm dụng cụ hoặc thức ăn. Hai bát riêng trống. Đũa/chấm/rau/cốc vẫn ở vị trí nhận ra được.

Đĩa trung tâm nay là một ụ gồm **miếng rộng màu nâu-beige xen với dải dẹt vàng-beige, độ dài/bề rộng và mép khác nhau**, phủ hạt/bột bề mặt. Không còn đám sợi cong tròn, gần đồng dạng chi phối như v1. Phần nem đọc như hỗn hợp miếng/dải được áo bột trong cùng ngôn ngữ 3D của cảnh. Không thấy hơi nóng hoặc khói quanh món. Viền đĩa rau tiếp tục vượt khung trái; cốc tiếp tục sát khung phải.

## 3. Closure FOOD-M01 và kiểm hồi quy

| Rule / disposition | Bằng chứng trên đúng v2 | Kết luận / giới hạn |
| --- | --- | --- |
| CONT-2 / FOOD-M01 CLOSED, MET trong static scope | Nửa dưới trung tâm: có các miếng thịt rộng tối hơn và các dải bì dẹt sáng hơn, kích thước/hình dạng không đều, lớp hạt bám bề mặt. So v1, silhouette sợi cong kiểu mì đã được thay. So ảnh thật, đạt các đặc điểm material cần phân biệt miếng/dải/lớp thính. | Đóng lỗi MAJOR đã nêu; không yêu cầu sao chép nguyên bố cục, tỷ lệ thành phần hoặc từng mảnh ảnh thật. Không xác nhận công thức/thành phần thực từ ảnh tạo. |
| CONT-2 presentation / MET | Giữ ụ gọn ở giữa một đĩa gốm, không rải phẳng toàn bàn; không nhập lá xếp vòng/ớt trang trí/đồ nền ảnh thật. Món không có steam visible. | Chênh cách xếp và cảm giác texture trong 3D là ACCEPTABLE_VARIATION, chưa có căn cứ nâng thành lỗi mới. |
| CONT-1 identity/outfit / MET, không thấy MAJOR regression | So PAIR03 và v1: giữ mặt khoai vàng lấm tấm/mày dày/mắt nâu; Đào giữ rãnh/cuống/lá và mắt/lông mi. Giữ jacket xanh than/sơ mi kem; blouse cổ/nút, nơ hồng đất/váy sage. Hai mặt/mắt đều đầy đủ. | Không tuyên bố pixel-identical hoặc continuity đa góc. |
| CONT-1 adultfriends / MET trong visible scope | Tạo hình/trang phục vẫn như hai người bạn trưởng thành theo baseline stylized; không ôm/tựa đầu/đút ăn hoặc gesture romance. Khoai lớn hơn không phải drift mới so v1. | Không phải audience test hoặc proof tuổi từ dữ liệu ngoài ảnh. |
| CONT-3 F0 / MET | Cả hai môi khép; cả bốn tay nghỉ trên bàn; không có món/đũa đang cầm; hai bát trống; món còn trên đĩa. | Không chứng minh reach/grip hoặc các state F1–F4. |
| CONT-3 count/geography / MET | Khoai trái/Đào phải cùng cạnh; một đĩa nem giữa, một đĩa rau trước-trái, hai bát cá nhân, hai chấm lệch trái/phải, hai đôi đũa nghỉ, một cốc ngoài phải Đào. Đũa Đào ở giữa bát và cốc, đũa Khoai bên trái bát anh. | Không thấy đồ biến mất/nhân đôi/đổi phía do sửa món. |
| CONT-4 light/background/provenance / MET | Ánh sáng ấm, mắt/tay đọc rõ; nền quán mềm và trục cảnh như v1/TABLE08; watermark giữ ở góc dưới-phải. | Không suy tính năng/model hoặc provenance toàn pipeline chỉ bằng watermark. |
| CONT-4 / COMP-m02 OPEN, MINOR | Đĩa rau trước-trái vẫn có phần viền/lá ra ngoài biên trái; cốc sát biên phải, thiếu khoảng thở. | Count/trục đọc được nhưng không đạt đầy đủ tiêu chí “entire serving set ... breathing room”. Chưa đóng. |
| CONT-4 / FORMAT-m03 OPEN, MINOR đối với ref | Metadata vẫn768×1376; khác9:16 chính xác khoảng0,78% ở chiều cao. | Native là still dọc, chưa tự thành file720p9:16 hoặc final. Chưa đóng. |

**Không phát hiện MAJOR hồi quy** ở mặt/outfit/tay/môi/count/geography hoặc ụ gọn. Việc sửa món thành công không tự đóng hai finding MINOR còn nguyên. V2 được đề xuất trình owner vì lỗi food nhận diện chính đã đóng, không phải vì prompt hoặc root đã chọn.

## 4. Minor còn mở và cách trình owner

**COMP-m02:** cho owner thấy rõ crop đĩa rau và cốc sát mép. Khuyến nghị có thể chấp nhận v2 **làm reference identity/food/F0 với giới hạn margin được ghi lại**, nếu owner chọn tại checkpoint hiện hành; đây là ngoại lệ ở master still, không miễn tiêu chí đủ serving/mặt/tay cho các output về sau. Nếu owner muốn chính master thấy toàn viền serving, route DOP/root sửa framing/version mới, giữ vị trí tương đối; không tự dời rau/cốc vào giữa. Reviewer không tự accept exception hoặc cấp thêm generation authority.

**FORMAT-m03:** giữ native nguyên vẹn và ghi kích thước thực. Khi route sử dụng cần9:16 chính xác, tạo derived riêng với hash/metadata và kiểm ảnh thực; tránh cắt thêm vùng trái/phải đã thiếu margin. Không đổi nhãn native thành720p chỉ vì đích phim là720p. Owner chấp nhận reference không tự waive chuẩn export cuối.

Không đề xuất generation tiếp theo chỉ để sửa những thay đổi nhỏ mà owner có thể xem và quyết định ở checkpoint đang chờ. Không lấy status PASS này làm quyền bypass checkpoint hoặc tự mở C02.

## 5. Handoff và trạng thái

**Đã xác định:** v2 khớp hash dispatch; FOOD-M01 đóng bằng ảnh actual so real source và v1; identity/F0/serving không có MAJOR regression. **Đã chốt trong review:** `PASS_FOR_OWNER_REVIEW` về static identity/food/state, với COMP-m02 và FORMAT-m03 còn mở ở MINOR. **Giả định:** giữ v2 như ứng viên master và giữ native; không suy owner đã accept ngoại lệ. **Còn mở:** owner chọn đúng candidate/hash và xử lý/accept minor; mọi motion/grip/A-B/voice/lip-sync/30giây. **Bước tiếp:** root đọc report và trình v2 cùng hai giới hạn rõ ràng tại checkpoint master, lưu quyết định exact asset trước downstream.

Một still đạt nhận diện/chất liệu không chứng minh hành động, khẩu hình hoặc toàn phim đạt. Report này chỉ đóng FOOD-M01 trên hash v2 nêu trên; không sửa status REWORK lịch sử của v1 và không tự bao phủ revision khác.
