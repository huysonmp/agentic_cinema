# 237 — Duyệt kế hoạch 720p và tiếp nhận tài khoản

Ngày: 07/10/2026. Trạng thái: **PLAN_APPROVED / ACCOUNT_CONFIRMED / NEW_PROJECT_CREATED / VOICE_DRAFT_PENDING_AUTHORIZATION / NO_GENERATION**.

## Approval đã nhận

Owner: “chấp thuận kế hoạch, làm tuần tự đi nào”. Target: kế hoạch 236/v1.0 tại commit 6718209; SHA-256 trước khi bổ sung ghi chú approval: `805bfb1d00f1fd24e7b4bba929c369c979348ad9b0b3c668238a9a651508af4f`.

Chốt kế hoạch: làm mới footage 720p trực tiếp trên tài khoản mới, 11 đơn vị dự kiến, giữ creative/thoại/giọng theo hướng đã chọn và trần dự trù 500. Không mở vòng 360p/thử tay/x3. Bắt đầu tiếp nhận tài khoản và chuẩn bị đầu vào.

Approval không là nghiệm thu ảnh/giọng/video chưa tạo, không cấp quyền mua/nạp tiền, không tự xóa project cũ và không bỏ quy tắc trình request/quote cụ thể trước từng generation trả phí. Ngân sách đã chi trên kế hoạch mới: **0/500**.

## Kiểm Flow thực tế

Đã đọc skill computer-use và hướng dẫn liên quan, sử dụng trình duyệt được hỗ trợ để kiểm trạng thái Flow. IAB không có tab Flow lúc kiểm, nên mở một tab mới ở `https://flow.google.com/`, hiển thị cho owner.

Quan sát UI đầu lượt: một tài khoản đang đăng nhập, gói Pro, số dư 1.050 credit và một project cũ. Root chưa thao tác vào project cũ hoặc tự suy tài khoản này là nick owner giao.

Sau câu hỏi, owner trả lời: **“Đúng tài khoản này — tạo project EP01 mới, giữ project cũ”**. Ghi nhận identity tài khoản và quyền tạo project mới, không xóa/sửa project cũ. Chỉ ghi dữ liệu account tối thiểu ở repo, không commit email, thông tin đăng nhập, cookie hoặc danh sách tab không liên quan. Ảnh UI có account để owner đối soát được giữ local:

`C:/Users/PC/Downloads/du_an_nem_bui/237_account_intake/FLOW_ACCOUNT_FOR_OWNER_CONFIRMATION.png`

SHA-256 screenshot: `6ac4c876aa95a9428ce8fe21e5c9605d27ad22b07ee1a11cb24c979e39a4e0fd`. Số dư 1.050 là snapshot UI, không tăng trần 500 hoặc thay quyền chi từng request. Có project cũ không làm sai phạm vi: account được owner xác nhận, đợt EP01 dùng project mới riêng.

### Project mới đã tạo và kiểm cấu hình

- Tên thực: **EP01 Nem Bùi — Khoai & Đào — 720p v1**; đã nhập tên và xác nhận tiêu đề UI đổi đúng.
- URL: `https://flow.google.com/project/bcb1f53c-13b6-4719-b866-01348dfcddd6`.
- Cấu hình đã kiểm: Video / Ingredients / Omni 1.1 Flash / 720p / 9:16 / 10 giây / x1 / Agent OFF.
- Quote 15 credit khi composer trống; **chưa là quote cuối của C02 có đủ ảnh/voice/prompt**, không có submit hoặc output.
- Nút bắt đầu tạo chưa được bấm. Không upload hoặc lấy footage cũ làm ingredient.
- Screenshot local: `EP01_NEW_PROJECT_720P_SETTINGS.png` trong folder 237 ở trên. Không dùng ảnh này như bằng chứng master/voice/QC đã đạt.

### Giọng đang chuẩn bị, chưa tạo

Đã mở thư viện Voices, tìm đúng base Orus và điền sample/performance K20 từ 148/149 cùng tên nháp `EP01_Khoai_K20_Orus_720p_v1`. UI đọc lại đúng sample 109 ký tự và chỉ dẫn đầy đủ. Chưa bấm preview hoặc lưu; chưa có custom ID mới.

Giao diện có nút xem trước/lưu nhưng **không hiển thị phí cho các thao tác đó**. Không coi “không thấy giá” là quote 0. Đã gửi câu hỏi riêng cho owner cho phép đúng hai mẫu phục hồi K20/D06, đối soát credit sau mỗi mẫu và dừng nếu thấy có phí trước mẫu tiếp. Chưa có câu trả lời tại lúc ghi báo cáo. Không sửa chỉ dẫn hoặc tạo thêm mẫu trong lúc chờ.

Skill [computer-use](C:/Users/PC/.codex/plugins/cache/openai-bundled/computer-use/26.1002.51308/skills/computer-use/SKILL.md) dẫn đến thao tác qua UI được hỗ trợ, kiểm trạng thái sau thao tác và giữ tab cho owner; không điều khiển đăng nhập hay lấy mật khẩu.

## Công việc local đã bắt đầu

- Khởi tạo hồ sơ `restart_720p_v1/`, ghi quyền, ngân sách và checklist tiếp nhận.
- Trích chỉ dẫn phục hồi hai preset đã chọn từ 148/149/150/151; không nghĩ lại giọng hoặc thay K20 bằng K12.
- Kiểm tồn tại ảnh demo gốc và hai ảnh món owner đã cho dùng; chưa upload hoặc tạo master mới.
- Project URL mới đã có; refs và voice ID mới chưa có. Không nhận cloud ID cũ làm binding trên nick mới.

## Bước tiếp theo

1. Nhận phản hồi riêng về thao tác phục hồi hai giọng không có giá hiển thị; lưu quyền đúng phạm vi trước preview/save.
2. Tạo và đọc lại voice ID mới, kiểm credit thực từng mẫu; owner nghe đối chiếu hướng đã chọn, không tuyển hàng loạt.
3. Chuẩn master/refs/voice bindings và gói C02; ảnh chỉ tạo nếu quote 0 hoặc đã có quyền chi cụ thể. Gói ảnh mới vẫn cần kiểm chuyên môn.
4. DIR/DOP/ACT/EDIT cùng reviewer kiểm gói đầu vào hiện hành; không ghi agent đã review khi chỉ có thiết kế.
5. Trình request C02 thực: đúng giọng Khoai, lời ký ức không lặp Khoan, Ingredients/Omni 720p/9:16/x1/Agent OFF, quote và trần thực. Chỉ submit sau owner duyệt request đó.

## Tổng hợp

- **Đã xác định:** account đã được owner xác nhận, project mới đã tạo, UI hỗ trợ cấu hình và Voices cần thiết.
- **Đã chốt:** trực tiếp 720p, phân cảnh/trần 500, làm tuần tự và giữ gate trả phí, giữ project cũ.
- **Giả định:** giọng có thể phục hồi từ thông số đã chọn, chưa khẳng định identity output giống hệt hoặc preview miễn phí.
- **Còn mở:** quyền cho preview/save không có giá hiển thị, master và voice ID mới, quote đầy đủ của C02.
- **Tiếp:** phục hồi hai giọng theo phản hồi owner, chuẩn bị refs rồi trình C02; chưa chi credit.
