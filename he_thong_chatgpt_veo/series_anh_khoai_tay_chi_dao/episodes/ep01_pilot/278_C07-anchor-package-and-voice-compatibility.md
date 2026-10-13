# REC278 — Chuẩn bị neo hình C07, giữ giọng D06

Ngày 13-10-2026. Owner chọn **A** tại REC277: chuẩn bị lại gói neo hình, giữ kịch bản, chưa trả phí thêm. **PREPARATION_ONLY / NO_T03 / C07 NOT_SELECTED / C08 HOLD.** Approval được lưu riêng tại `restart_720p_v1/00_decisions/C07-anchor-preparation-A-278.json`.

## Kết quả kiểm công nghệ trước khi chọn cách làm

Đã mở lại đúng project trên trình duyệt tích hợp, không đổi tài khoản hoặc tạo project khác. Giao diện có Omni 1.1 Flash, 720p, 9:16, x1. Chế độ **Khung hình** có hai ô Start/End; đã gắn ảnh C06 F56 vào đúng Start để kiểm bước chuẩn bị. Bộ chọn chỉ có ảnh/tệp tải lên, không thấy ô giọng. Đây là khác biệt thật với việc dùng một ảnh trong Ingredients; không gọi Ingredients là khóa khung đầu.

Google xác nhận Omni hỗ trợ Frames đầu/cuối và Ingredients. Tuy nhiên **voice reference chỉ dùng được với Ingredients**, không phải các chế độ còn lại. Vì vậy không đề xuất một request “Start + End + D06” không tương thích. Nguồn kiểm ngày 13-10-2026: [hướng dẫn tạo clip và giọng](https://support.google.com/flow/answer/16353334?hl=en), [model và tính năng](https://support.google.com/flow/answer/16352836?hl=en). Google cũng khuyến nghị ảnh chủ thể nền sạch/tách nền và chỉ dẫn ảnh–text không mâu thuẫn; đó là cơ sở chuẩn bị, không bảo đảm tỷ lệ đạt.

Đã trở về **Ingredients** sau kiểm: 6 giây, 720p, 9:16, x1; quote 10 credit. Đọc nguyên tên, mô tả diễn giọng và ID saved D06 `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`; không chỉnh giọng hoặc chạy preview. Ô nhập hiện chỉ có ảnh cảnh, prompt trống/nút tạo vô hiệu: **chưa phải bộ đầu vào hoàn chỉnh**. Chưa upload/gắn ảnh nhận diện mới và D06, chưa kiểm quote trên gói đầy đủ.

## Gói tham chiếu đề nghị — ba vai, không ba cảnh

| Thành phần | Vai trò duy nhất | Không được dùng thay |
|---|---|---|
| Ảnh native C06F56 SHA `69fb0e62a3a6f138a0eae622603945b248ec8d2809c8cda513dcdfdc33d00863` | Toàn cảnh: camera, trang phục, hai bát, cốc/tay, rau/chấm/nem nguội và tư thế vào | Không sửa/tái sinh ảnh này; không dùng T01/T02 sai làm opening |
| Ảnh pair nhận diện nền sạch v1, SHA `122b6bbbb129361e6fb494fe74935afc510280c1bebf529d8a136ddf95a92f8f` | Chỉ hình mẫu hai nhân vật không phải người: Khoai có da khoai; Đào có đầu quả đào/lá/cuống | Không thay camera, cỡ cảnh, biểu cảm/diễn, bàn hoặc tư thế; không là master/endframe |
| Một saved D06 Aoede | Chỉ giọng Đào cho nguyên văn N07 “Thế em quay lại đúng lúc rồi.” | Không thêm K20, chỉnh preset, hoặc kế thừa approval giọng từ take khác |

Chân dung đôi v1 được tạo bằng ImageGen built-in, tham chiếu duy nhất ảnh C06 F56, kích thước 1672×941 RGB. Đã lưu không ghi đè tại `02_refs/C07_PAIR_IDENTITY_v1_CHATGPT_FOR_REVIEW_278.png` và folder owner `C:/Users/PC/Downloads/du_an_nem_bui/278_C07_ANCHOR_PREP/`. Prompt tạo ảnh lưu tại `04_requests/C07_PAIR_IDENTITY_image_prompt_278.txt`. Root đã xem nguyên ảnh mới và ảnh cảnh. Đây là ảnh sinh lại, không phải cắt nguyên pixel: chất liệu, tỷ lệ, góc đầu hoặc cổ áo có thể khác. Phải qua reviewer/owner trước dùng, không gọi là “giống mẫu tuyệt đối”.

## Thay gì, giữ gì và giới hạn

Thêm một tham chiếu nhận diện riêng, phân rõ cảnh và nhận diện; draft tránh gọi Đào bằng danh từ người thật và gom chỉ dẫn theo thứ tự hành động. Không đổi thoại, nhiệm vụ C07/C08, hai vai tay, giọng, góc máy, món hoặc cap. Đây là hai nhóm can thiệp input+text, không phép thử một biến. Draft v1 SHA `4ff0cf359431b3bf119b0890b09ca7c69a592a909d7a36da626e6118a3ae527e` giữ lịch sử. Current `04_requests/C07_anchored_Ingredients_DRAFT_v2_278.txt` SHA `5f3f00fde211ba58118927c9cd3b6e5229938293b913c02b91766ee32a0cd9d3` bổ sung hai môi khép lúc vào, chỉ Đào mở môi khi nói, khoảng hở cả A/tips với vành ở cuối, và ảnh cảnh ưu tiên scale/expression/material hơn portrait. Chưa là final được phép gửi; mọi phạm vi duyệt vẫn chờ.

Đích vẫn: tiếp A đang đưa → giữ kẹp → Đào đáp/chuẩn bị bát riêng → bát rỗng chờ C08 thả. Kiểm ID của hai bát xuyên suốt, không chỉ nhìn vật thể có dịch. Phân biệt tay tiếp cận sang phải và bát dịch trái; cốc nâng tay ngoài phải. Mọi nguồn mới phải kiểm cả danh tính/props/entry trước động tác chính, không cắt che sai chủ thể.

**Rủi ro chưa đóng:** Ingredients không khóa F0 hay vận tốc; portrait bổ sung có thể lấn framing/scale và vẫn không sửa bát/tay. Việc thêm ref không chứng minh chắc model sẽ đạt; chưa có output mới hoặc xác suất dự báo đáng tin. Frames neo trạng thái có tiềm năng nhưng sẽ phải tách/ghép voice theo route khác, có rủi ro sync và cần approval riêng; không tự chuyển hướng đó.

Qua C06 vẫn có 689 khung / 28,708333 giây; còn 151 khung / 6,291667 giây tới trần bản dựng thô 35 giây cho C07–C09. Chưa có thời lượng/đoạn nguồn cuối; không hứa vừa 35 giây hoặc cắt câu, bỏ nhịp thả/kết. Sinh sáu giây không có nghĩa chọn đủ sáu giây. Ngân sách dự án đã dùng 207/500, còn 293: first-pass 82, retake 56, post-rough 45, dự phòng 110 đóng. Vòng này **0 Flow credit / 0 lượt gửi tạo video**; số dư tài khoản 1.023 khớp biên lai REC277, không tự cấp quyền chi.

## Review và cổng kế tiếp

Maker CTD/DIR/DOP/ACT/CONT và reviewer độc lập đã hoàn tất local theo217, xem exact original + portrait và đọc v2, không browser/credit/edit media/git. Root đã đọc đầy đủ hai báo cáo COMPLETE_PROOFREAD: `06_qc/C07_anchor_maker_preparation_278.md` gồm refreshv2, và `06_qc/C07_anchor_independent_preflight_278.md` currentv2. Cả hai cho phép trình ứng viên, không nhận PAPER thành source/AV PASS.

Sai khác cần owner biết: da/đốm và màu sắc nét hơn, mắt/môi/nụ cười rõ hơn; rãnh/lá/cuống Đào nổi hơn, cổ mảnh hơn. Maker cảm nhận Khoai cao hơn tương đối; critic cảm nhận đầu Đào lớn hơn. Do crop khác và chưa đo hình học, root không chọn một nhận xét làm tỷ lệ chính xác; giữ **scale/expression/material theo ảnh cảnh**, không theo portrait. Không gọi portrait là clone hoặc master mới.

1. Owner duyệt hoặc yêu cầu sửa **portrait chỉ cho scope tham chiếu nhận diện**, không duyệt đổi master/camera hoặc chi.
2. Sau chân dung và prompt được chốt, kiểm trực tiếp đủ hai ảnh + một D06, khả năng nhận đầu vào, đúng thumbnail/version, quote ≤15, âm thanh bật/Agent tắt, cấu hình/hash; không mặc định quote 10 hôm nay thay quote lúc chạy.
3. Trình đúng một request sau STOP với budget/tiêu chí, xin quyền chạy trước submit. Không lấy câu “A chuẩn bị” hoặc approval portrait làm quyền T03.
4. Nếu được chạy sau đó: tải native, đối soát debit, kiểm từng frame/maker–critic, chọn range hoàn thành nhiệm vụ nếu có; human checkpoint D06/N07/diễn–sync và encodedC06→C07, đo timing cuối. Nếu vẫn MAJOR thì dừng, không batch/retry/C08.

Chỉ hỏi owner một quyết định hình ở vòng này sau phản biện; giữ những chốt trước, không mở thêm danh sách câu hỏi nền tảng.
