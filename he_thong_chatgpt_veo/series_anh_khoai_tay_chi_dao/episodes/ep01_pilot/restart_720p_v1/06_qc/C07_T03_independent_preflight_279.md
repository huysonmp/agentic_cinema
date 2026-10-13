# C07 T03 — Kiểm đầu vào độc lập REC279

Trạng thái: **CONDITIONAL_PRESENT_ONE_PAID_REQUEST — PAID APPROVAL PENDING / NOT SUBMITTED / NOT SELECTED**.

Ngày: 2026-10-13. Phạm vi cục bộ theo 217. Báo cáo đã đọc lại đầy đủ và rà câu chữ; không đọc báo cáo maker REC279, không dùng trình duyệt, API, credit, git, script mới hoặc chỉnh media. Kết luận chỉ về đầu vào đã chuẩn bị, không chứng nhận video hoặc tiếng.

## 1. Tài liệu và hình ảnh đã kiểm

Đã đọc đầy đủ:

- `00_decisions/C07-pair-identity-owner-approval-279.json`.
- `04_requests/C07_T03_preparation_279.json`.
- `04_requests/C07_T03_prompt_279.txt`; tự tính SHA-256: `5f3f00fde211ba58118927c9cd3b6e5229938293b913c02b91766ee32a0cd9d3`. Nội dung giữ nguyên bản v2 REC278 đã phản biện; không đề nghị tối ưu thêm câu chữ trong lượt này.

Đã trực tiếp xem lại toàn ảnh cảnh `02_refs/C07_START_from_C06_T03_selected_F56_276.png` và chân dung `02_refs/C07_PAIR_IDENTITY_v1_CHATGPT_FOR_REVIEW_278.png`. Các hash khóa theo hồ sơ lần lượt là `69fb0e62a3a6f138a0eae622603945b248ec8d2809c8cda513dcdfdc33d00863` và `122b6bbbb129361e6fb494fe74935afc510280c1bebf529d8a136ddf95a92f8f`.

Đã trực tiếp xem ba screenshot trong `C:/Users/PC/Downloads/du_an_nem_bui/279_C07_T03_PREFLIGHT`:

1. `C07_T03_FULL_INPUTS_CONFIG_QUOTE10.png`.
2. `C07_T03_AUDIO_ON.png`.
3. `C07_T03_READY_NOT_SUBMITTED.png`.

Reviewer không nghe voice, không thao tác UI và không xem video đầu ra T03 vì chưa có lượt chạy.

## 2. Quyền duyệt và phạm vi nhận diện

Owner nói “ok nhé” trong gate duyệt **chân dung bổ sung để nhận diện**. Hồ sơ đã công bố ảnh mới có chi tiết bề mặt sắc hơn và nụ cười rõ hơn cảnh. Approval này không duyệt master mới, thay tỷ lệ, camera, pose hoặc biểu cảm của cảnh; cũng không duyệt trả phí, retry hay C08.

Ảnh chân dung giữ Khoai là củ khoai tây và Đào là quả đào có cuống/lá, không thành diễn viên người thật. Sai khác chất liệu, mắt/môi, ánh sáng và cảm giác tỷ lệ đã được ghi ở REC278; nay không cần mở lại gate dung sai đã được owner chấp nhận trong đúng phạm vi bổ sung nhận diện. Prompt vẫn giao ảnh cảnh kiểm soát bố cục, tỷ lệ, biểu cảm, màu, chất liệu và hành động. Approval ảnh không làm mất yêu cầu kiểm những yếu tố đó trong video mới.

## 3. Đối soát gói UI đã chuẩn bị

| Hạng mục | Bằng chứng reviewer trực tiếp thấy | Phần chỉ được xác nhận từ hồ sơ/root |
| --- | --- | --- |
| Số thành phần | Cả ba screenshot cho thấy ba chip: một chip voice màu xanh, một ảnh chân dung đôi và một ảnh cảnh bàn ăn. | Root readback đúng một D06, không voice khác; tên `EP01_Dao_D06_Aoede_720p_v1`, ID `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`. Screenshot không hiện toàn tên/ID hoặc performance. |
| Ảnh cảnh | Thumbnail cảnh có hai nhân vật thực phẩm và bàn ăn, không phải thumbnail Đào người thật ở lịch sử dự án phía sau. | Scene ID `9d2280e2-bb03-437a-98f2-553a7d481144`; đã phục hồi sau khi click chip làm gỡ ảnh. |
| Chân dung | Thumbnail chân dung khớp loại ảnh mới nền xám và cặp nhân vật thực phẩm. | Pair ID `ded2a157-f2d7-4be7-9185-31d5fc87f3ea`, gắn với đúng ảnh owner duyệt. |
| Route/cấu hình | Screenshot cấu hình cho thấy Video, Thành phần, Omni 1.1 Flash, 9:16, 720p, 6 giây, x1 và quote 10 tín dụng. | Chưa có request backend; khả năng nhận gói sau submit chưa được thử. |
| Âm thanh | Screenshot AUDIO_ON cho thấy “Trả về video không có âm thanh” đang tắt. | Không chứng minh D06 sẽ được dùng đúng hoặc không phát sinh lời nam. |
| Prompt và readiness | Phần đầu prompt trên ảnh đúng final: cảnh sáu giây, phân vai hai ảnh, hai miệng khép và tiếp chuyển động A. Nút tạo hiện có thể dùng; không thấy cảnh báo input trên các ảnh này. | Root đã readback toàn prompt chuẩn hóa khớp final. Screenshot không bao phủ mọi dòng; reviewer xác nhận đầy đủ nội dung qua file local, không tự nhận đã kiểm toàn DOM. |

Các thumbnail T01/T02 lỗi nằm ở nền thư viện không phải bằng chứng chúng được gắn làm ingredients. Gói cuối đã có lại ba chip sau sự cố gỡ scene. Không thấy thiếu scene ở những screenshot cuối được kiểm. Tuy nhiên, screenshot và ID trong hồ sơ không chứng minh hash byte server hoặc cơ chế trọng số giữa hai ảnh.

**Phân biệt trạng thái:** UI đã cho phép chuẩn bị gói đúng cấu hình; backend chưa được submit; nhận diện, F0, động tác, tiếng D06, khẩu hình và seam thực tế vẫn chưa biết. Không được gọi gói này là đã chạy thành công hoặc đã sửa được lỗi.

## 4. Preflight đạo diễn và liên tục hành động

Ảnh F56 có A đang kẹp phía trái bát Đào, cao hơn vành, cạnh cẳng tay tự do; hai bát trống, cốc trong tay ngoài của Đào vẫn cao. Final giữ đúng điểm này, cho tay Khoai tiếp một đoạn ngắn rồi lắng xuống, không rút về ngực hoặc mời lại.

Đào nhìn từ A sang Khoai, nói một câu N07: “Thế em quay lại đúng lúc rồi.” Chỉ D06; Khoai im miệng và bình thản, hơi ngượng. Đào dùng tay trong tiếp cận thành trái bên ngoài **bát mình ở nửa phải màn hình**, rồi trượt bát ngắn sang trái dưới A. Bát Khoai giữ nguyên. Cốc giữ ở tay ngoài; đũa riêng Đào vẫn đặt trên bàn. Kết yêu cầu bát trống, A còn kẹp, khoảng hở với vành bát, hai miệng khép; release dành C08.

Không thấy mâu thuẫn giấy bắt buộc sửa final trước khi trình xin chạy. Không thêm nhịp vội, biểu cảm cười một khóe, nhận món sớm hoặc action mới. Phân vai hai ảnh và khoảng hở cuối rõ hơn hồ sơ T01/T02, nhưng không tạo bảo đảm thực thi. Rủi ro còn nguyên: portrait lấn pose/camera của scene; Ingredients tái dựng F0; sai bát; tay xuyên hoặc chạm A; cốc đổi tay/hạ; Khoai nói thay Đào. Chỉ video thật mới kết luận được.

## 5. Ngân sách và thời lượng

Hồ sơ ghi đã chi 207/500 credit, còn 293, khoản dự phòng 110 credit vẫn đóng; chưa submit và chưa debit REC279. Tài khoản 1.023 credit là readback từ root, không phải ngân sách dự án tăng thêm. Quote UI đang là 10 credit cho một lượt. Nếu giá và debit đúng như quote, dự án sẽ thành 217 đã chi/283 còn lại; quỹ retake từ 56 xuống 46. Đây là phép tính điều kiện, không ghi nhận đã chi.

Đã chọn đến C06: 689 frame ở 24 fps, tương đương 28,708333 giây. Còn 151 frame/6,291667 giây tới trần kỹ thuật 35 giây cho cả C07–C09. Clip C07 yêu cầu sáu giây không tự được chọn toàn bộ, nhưng chưa có phần cắt hợp lệ để hứa đủ thời gian cho C08/C09. Không đổi mục tiêu 30 giây hoặc mở trần chỉ vì gói đã chuẩn bị.

## 6. Kết luận và gate bắt buộc

**Có thể trình owner một yêu cầu trả phí T03 duy nhất, giá live 10 credit, sau STOP REC277. Chưa được submit chỉ dựa vào approval chân dung.** Đây là kết luận có điều kiện về đầu vào hiện hành, không phải quyền chạy do reviewer cấp.

Trước submit, root cần đọc đầy đủ báo cáo hiện hành, giữ đúng final/hash và gói ba chip; nhận approval riêng cho một lượt mới. Nếu cấu hình, input, voice hoặc quote khác snapshot, phải đối soát lại trước khi chạy. Không tự thêm wording, đổi route hoặc loại ảnh đã khóa.

Sau một lượt, kiểm actual toàn dải frame và các mốc chuyển động; nghe/duyệt N07, đúng người nói, đúng D06 và seam C06→C07. **Bất kỳ MAJOR nào đều STOP và báo cáo, không tự T04; C08 HOLD.** Không chọn prefix chỉ vì bớt lỗi nếu chưa hoàn tất lời, chuẩn bị bát đúng và trạng thái A còn kẹp có khoảng hở ở endpoint. UI readiness, giấy preflight và approval tiếng cũ không thay các gate này.
