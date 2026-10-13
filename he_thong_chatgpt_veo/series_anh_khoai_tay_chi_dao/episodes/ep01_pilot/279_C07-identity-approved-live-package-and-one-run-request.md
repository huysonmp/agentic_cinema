# REC279 — Ảnh nhận diện được duyệt; gói C07 T03 chờ duyệt chạy

Ngày 13-10-2026. **LIVE_PREPARED / NOT_SUBMITTED / OWNER_PAID_GATE_PENDING.** C07 chưa chọn, C08 giữ chờ; approval hình/giọng/các điểm nối cũ không thành approval video mới.

## Đã chốt và đã kiểm

Owner “ok nhé” duyệt chân dung đôi v1 SHA `122b6bbbb129361e6fb494fe74935afc510280c1bebf529d8a136ddf95a92f8f` **chỉ làm nhận diện phụ**. Giữ ảnh C06 F56 làm chuẩn cảnh, tỷ lệ, biểu cảm, ánh sáng, chất liệu và tư thế; không đổi master/canon. Quyết định mới: `restart_720p_v1/00_decisions/C07-pair-identity-owner-approval-279.json`.

Đã upload đúng một ảnh nhận diện vào project hiện hành, gắn một saved D06 và khôi phục/kiểm lại ảnh cảnh. Cuối preflight, DOM có **ba chip = hai ảnh + một giọng**, không video, không K20. Ảnh cảnh có Flow image ID `9d2280e2-bb03-437a-98f2-553a7d481144`; ảnh pair mới có ID `ded2a157-f2d7-4be7-9185-31d5fc87f3ea`. Hash hai file local đã kiểm; ID là quan hệ với ảnh đã chọn/upload trên UI, chưa băm byte ảnh server.

D06 đã đọc tên, mô tả diễn giọng và ID `6dadc0b1-00c3-493c-943d-f4a1e4a88feb` trước bấm thêm. Không sửa preset hoặc phát preview. N07 nguyên văn: **“Thế em quay lại đúng lúc rồi.”**, chỉ Đào nói. Có đúng preset tham chiếu không chứng minh tiếng video mới sẽ đạt.

Prompt cuối `04_requests/C07_T03_prompt_279.txt` SHA `5f3f00fde211ba58118927c9cd3b6e5229938293b913c02b91766ee32a0cd9d3` **giữ nguyên byte của bản v2 đã phản biện tại REC278**. Đã điền và đọc lại nội dung trên UI, khớp sau chuẩn hóa khoảng trắng. Không thêm chỉ dẫn diễn xuất hoặc sửa câu chữ sau khi khóa bản cuối.

Gói đầy đủ trên UI: **Omni 1.1 Flash / Video Ingredients / 720p / 9:16 / 6 giây / x1**, Agent tắt; “Trả về video không có âm thanh” tắt, tức giữ âm thanh. Quote trực tiếp sau đủ inputs/prompt: **10 credit**. Không thấy cảnh báo input không hỗ trợ, nút tạo được bật; đó là bằng chứng chuẩn bị trên UI, **chưa chứng minh backend nhận job hoặc chất lượng output** vì chưa submit.

Bằng chứng lưu tại `C:/Users/PC/Downloads/du_an_nem_bui/279_C07_T03_PREFLIGHT/`: `C07_T03_FULL_INPUTS_CONFIG_QUOTE10.png`, `C07_T03_AUDIO_ON.png`, `C07_T03_BALANCE_1023_NOT_SUBMITTED.png`, `C07_T03_READY_NOT_SUBMITTED.png`. Tab1 trong browser2 được giữ để tiếp tục, tab2 cùng project không thao tác/xóa.

## Phát hiện thao tác UI và cách chặn tái diễn

Khi định kiểm ảnh cảnh, root đã bấm chip “Thành phần”. Bấm chip ở composer thực chất gỡ attachment, không mở preview; ảnh cảnh tạm bị gỡ. Screenshot ngay sau thao tác còn hiển thị trạng thái cũ, trong khi AX/DOM refresh tiếp theo chỉ còn hai chip. Không submit. Root gắn lại exact C06 F56 qua picker, kiểm lại đủ ba chip và image IDs rồi mới điền final/đọc quote.

Bài học áp dụng: **không bấm chip để preview**; đối chiếu provenance khi thêm, đọc DOM ảnh/loại/count và screenshot mới sau UI ổn định. Không dùng screenshot trung gian làm bằng chứng gói đầy đủ. File trung gian được giữ riêng, không xóa nguồn. Mọi lần quay lại phải đọc lại toàn bộ gói trước paid action, không tin tên file/ảnh thumbnail đơn lẻ.

## Một request đề nghị — chưa được cấp quyền

- Mục tiêu giữ nguyên C07: tiếp chuyển động A → Khoai giữ kẹp → Đào đáp N07 và đưa **bát riêng phía phải** vào vị trí nhận; cốc ở tay ngoài phải vẫn nâng, bát Khoai đứng nguyên; kết bát Đào rỗng và còn khoảng hở với A/cả hai tips. C08 mới thả.
- Chỉ **một C07 T03**, giá hiển thị hiện là 10 credit; không chạy ba lượt, không tự T04. Lỗi MAJOR về danh tính, mất bát, đặt lại tư thế hoặc hành động sai: dừng, lưu nguồn và trình chẩn đoán; không cắt che mặt, đổi nhãn bát hoặc đổi ranh giới cảnh để nhận đạt.
- Sổ hiện ghi đã chi 207/500 credit, còn 293; quỹ làm lại còn 56, sản xuất lượt đầu còn 82, hậu kỳ còn 45, dự phòng 110 vẫn đóng. **Nếu** khoản trừ đúng 10 thì tổng chi thành 217, còn 283, quỹ làm lại còn 46; đây là dự kiến, chưa ghi chi thực. Số dư tài khoản vừa kiểm vẫn là 1.023, không phải trần ngân sách dự án. Lượt làm việc này chi 0 credit.
- Các đoạn đã chọn đến C06 dài 689 khung / 28,708333 giây; còn 151 khung / 6,291667 giây tới bản dựng thô 35 giây cho C07–C09. Chưa có đoạn C07 được chọn hoặc các nguồn cuối, không hứa vừa 35 giây, đạt mục tiêu cuối 30 giây hoặc đạt ngay một lượt. Video sinh dài sáu giây không bắt buộc dùng đủ sáu giây.
- Ingredients vẫn là tham chiếu mềm, không khóa pixel-exact F0/vận tốc; hai ảnh có thể tranh ảnh hưởng. Approval portrait không chứng minh lỗi chuyển động/bát đã được khắc phục.

## Review hiện hành và bước tiếp

Đã đọc lại maker/reviewer REC278 trên đúng hash v2. Hai agent đã hoàn tất kiểm lại tại REC279 trên prompt cuối, approval mới, ảnh và bằng chứng UI. Root đã đọc đầy đủ cả `06_qc/C07_T03_maker_preflight_279.md` và `06_qc/C07_T03_independent_preflight_279.md`, rồi đối chiếu theo cùng hash. Cả hai không thấy điểm chặn mới trên hồ sơ; kết luận **đủ điều kiện trình duyệt một request**, chưa chứng nhận đầu ra sẽ đạt. Reviewer không thao tác trình duyệt, chi credit, sửa media/prompt hoặc tự nhận đã nghe giọng từ screenshot.

Sau owner duyệt đúng một request: kiểm lại đầu vào, prompt, cấu hình, giá và số dư trên UI rồi gửi một lần. Khi có đầu ra: tải bản gốc 720p, tính hash, kiểm giải mã và đối soát khoản trừ; xem toàn bộ khung hình, cho maker–reviewer thực kiểm, chọn đoạn hoàn thành nhiệm vụ nếu có. Owner kiểm D06, trọn N07, khẩu hình, nhịp và đúng bản nối C06→C07 đã xuất. C08 giữ chờ tới khi đóng các gate phụ thuộc. Không tự hoàn thiện hoặc phát hành phim.

**Owner cần chốt một điều:** có duyệt một C07 T03 giá 10 credit theo gói này không? Đây không phải duyệt phim, không mở lượt làm lại tự động hay quỹ dự phòng.
