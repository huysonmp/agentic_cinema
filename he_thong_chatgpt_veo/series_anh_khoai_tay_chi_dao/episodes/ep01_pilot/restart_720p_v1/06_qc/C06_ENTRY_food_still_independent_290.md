# REC290 — Review độc lập ảnh entry C06 sửa món v1

Ngày 13-10-2026. Reviewer `food_repair_critic_283`, bounded local REC217. **ACTUAL_FULL_STILL_COMPARISON / NOT_VIDEO_OR_PERFORMANCE_PASS.** Chỉ đọc brief, kiểm hash và xem ảnh source/candidate/hai ảnh món thật. Không browser, generation, script/media edit, credit, EDL hoặc git.

**Disposition: HOLD_AS_EXACT_ENTRY / FOOD_MATERIAL_CANDIDATE_ONLY.** Món tiến đúng hướng, nhưng ảnh đã redraw vùng ngoài món và phần A đọc lớn hơn; chưa đạt scope giữ entry nguồn như đã dự kiến. Không upload/bind như đầu vào đã chuẩn từ báo cáo này.

## 1. Đã đọc/xem và hash

Đọc đầy đủ `04_requests/C06_ACT_v0p2_nuance_B_290.md`: sắc thái B đã chốt, không dò xem Đào tin chưa, không gồng→thở phào hoặc diễn trêu; trạng thái đầu kế thừa C05, cùng A, chưa nhận/thả. Đây không phải approval take hay acting trên ảnh.

Trực tiếp xem cả bốn ảnh đầy đủ, không chỉ vùng món; SHA-256 kiểm lại:

| File | SHA-256 |
| --- | --- |
| `02_refs/C06_START_from_C05_T02_selected_F65_269.png` | `f091e35fc7c779591c918c47ba34752a8a2c3b30de507cd99dc0e76143e83196` |
| `02_refs/C06_ENTRY_food_v1_CHATGPT_FOR_REVIEW_290.png` | `40be91b97b873979f09f01d1e530cd9512674dd2b26b1fc339237b0f23f37077` |
| `C:/Users/PC/Downloads/du_an_nem_bui/nembui.jpg` | `a51303f7100edd0944dc00daa19402fecfe24bb0e15a4143da8f8eae7b9e3a2d` |
| `C:/Users/PC/Downloads/du_an_nem_bui/z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg` | `1237956e99458385f95f1edf18e0a98e1bddb777030ac1d69fab05fa7a51d741` |

File tương đối tính từ `restart_720p_v1`. Source là khung C05 selected F65, không START283 ở C06 exit hoặc rejected native286.

## 2. Quan sát theo đối tượng

| Scope | Quan sát actual | Kết luận |
| --- | --- | --- |
| **Food plate** | Source có các phiến đặc khá rộng; candidate có thịt nâu hồng, dải bì mỏng/rời và thính, mép không đều hơn. Cả hai ảnh thật cũng có độ rộng thịt/bì khác nhau; candidate không biến cả đĩa thành mì hoặc nhập tôm/giò/đậu từ ảnh thật2. Không thấy khói. | **IMPROVED_MATERIAL_DIRECTION**, chưa recipe/cách phục vụ duy nhất hoặc owner approval món mới. |
| **Held A** | Candidate giữ nhúm ở tips phía Khoai, trên khu vực bát riêng/giữa ngực và bàn; không chuyển sang miệng, bát Đào hoặc tư thế đã thả. Nhưng nhúm có nhiều dải dài rủ xuống, diện tích treo đọc lớn hơn lát nguồn. | Đúng trạng thái đang cầm, **quantity/footprint continuity chưa khóa**; không chứng minh cùng phần nhỏ từ C05. Không dùng tính chất mềm mảnh để tự cho tăng serving. |
| **Hand/chopsticks/phase** | Vẫn một đôi đũa trong tay ngoài Khoai, tay trong nghỉ trên bàn; hướng tips/A rộng ra trước người, chưa phải entry nhịp nhận. Không có tay mới/gắp lại/nhận bát trong still. | Stage đúng tổng quát; không grip physics hoặc motion PASS từ ảnh. |
| **Dao bowl/glass** | Hai bát beige đều rỗng và đặt trên bàn; bát Đào nửa phải, dưới và phía trong so cốc. Cốc vẫn nâng ở tay ngoài, đáy không nằm trong bát; tay trong còn nghỉ, không kéo bát hoặc uống. | Props/state broadly preserved. Không đảm bảo spatial continuity exact hoặc video sau không đặt cốc vào bát. |
| **Clothes/identity** | Khoai vẫn vest tối/blouse trắng, Đào blouse trắng/váy xanh/nơ; không yếm xanh như286. Hai người nhận diện được, môi khép và nhìn về nhau. Tuy nhiên mặt/da/mắt/lông mày/chất liệu được redraw, không là source pixel giữ nguyên. | Không có gross character swap hoặc costume redesign thấy rõ; **exact entry identity/expression invariant chưa chứng minh**. Sắc thái B là chuỗi diễn, không thể chấm đạt trên môi khép một ảnh. |
| **Background/framing/light** | Giữ loại quán ven phố và đèn ấm, hai người trái/phải, bàn/lá/chấm. Song nhà/đèn/xe/người phía sau được vẽ lại và chi tiết sắc/ánh sáng khác; ví dụ xe đỏ phía trái đọc rõ hơn, các hình người/xe trung tâm không đúng nguồn. | Cùng ý đồ bối cảnh nhưng không đúng yêu cầu chỉ đổi food. Không gọi crop/framing/geometry seamless hoặc camera đã khóa. |
| **Platform mark/provenance** | Sao Flow trắng có ở đáy phải source, không thấy trong candidate. | Candidate phải ghi **ChatGPT-generated redraw**, không native Flow hoặc exact frame corrected. Source không bị sửa/xóa watermark; không nhận đã giữ mọi invariant. Không thêm watermark giả hoặc che/crop để sửa tình trạng này. |

Không có measurement registration/crop alignment trong run; nhận xét kích thước A là đọc ảnh tương đối, không con số volume/mass hoặc bounding-box đã đo. Whole redraw làm việc so trực tiếp pixel chưa hợp lệ; không lấy độ sắc/đẹp hơn làm chuẩn entry.

## 3. Scope fail và scope có thể giữ

Nếu mục tiêu là **sửa món trên đúng khung entry, giữ phần còn lại**, v1 chưa đạt: redraw mặt/background và dấu nguồn mất, A chưa giữ footprint. Đây là finding trên ảnh thực, không chỉ disclaimer chung rằng generative edit có thể drift. Root không nên trình cả ảnh như entry ready rồi để owner phải tự phát hiện lại.

Có thể giữ candidate làm **đề xuất vật liệu món trên đĩa và nhúm nhỏ**, với lineage/hash và trạng thái chưa approved; không âm thầm đổi vai trò thành canon/entry. Owner chọn sắc thái B không cấp approval redraw này hoặc mở paid request. Nếu muốn dùng một entry mới khác nguồn, đó là quyết định khác có tác động seam/identity/camera cần nói rõ, không tự coi mọi drift đều được phép vì sẽ tạo cảnh mới.

C05 trước đó vẫn món sai. Dù chuẩn được ảnh C06 entry sau, nguồn C05 cần cổng continuity/food riêng; một ảnh đẹp không khắc phục toàn chuỗi hoặc hứa video30s đạt.

## 4. Bước tiếp đề nghị, chưa thực hiện

1. Root ghi v1 **không chọn làm exact entry**, giữ source và v1 để truy; không paid generation hoặc approval transfer.
2. Nếu tiếp sửa ảnh trong phạm vi đã có, tập trung giữ toàn khung nguồn và giới hạn món/A thật nhỏ; kiểm tất cả vùng ngoài món và lineage lại trước dùng. Không hứa next edit giữ pixel. Không tự thêm composite/script/crop mới như quyền đã có; trình riêng nếu cần thay phương pháp.
3. Tách gate vật liệu với gate entry: vật liệu có thể trình owner theo scope rõ, nhưng dùng làm ingredient không cho phép mang mặt/pose của redraw vào source. Khóa image role trước technical request; Ingredients không tự bảo đảm F0.
4. Chỉ khi input đạt/chốt mới lập prompt/voice/live quote cho C06 ACT B. Native sau phải kiểm chuỗi diễn mặt–thân, speaker/voice/sync, lượng A và hai điểm nối thật; không chấm B từ still hoặc dùng source acceptance276 thay actual review.

**FINAL: MATERIAL_IMPROVEMENT_OBSERVED / EXACT_ENTRY_REWORK_HOLD / NO_ACTING_VOICE_AV_OR_PAID_GO.**
