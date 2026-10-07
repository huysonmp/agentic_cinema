# 230 — Đã xác nhận quyền tải, lỗi intake R01

Ngày: 2026-10-07. Trạng thái: **UPLOAD_CONSENT_EXECUTED / INTAKE_FAILED / GENERATION_NOT_SUBMITTED**.

## Quyết định và thao tác thật

Owner trả lời “có nhé, xác nhận” cho việc bấm **Tôi đồng ý** để tải đúng source AI của project lên Flow. Đã bấm nút đó, không chọn “không hiện lại”. Đây không phải approval tạo video hoặc thêm quyền chi. Phạm vi229 giữ: chỉ thay picture mở quanh “Khoan”, giữ toàn tiếng B và phần kể ký ức sau; không test tay riêng/x3/Quality/retry generation.

Source duy nhất: `C:/Users/PC/Downloads/du_an_nem_bui/229_r01_production_input/R01_SOURCE_GUIDE_NOT_FINAL.mp4`, SHA-256 `1ecc6b496291179ce1f5e82153883e2df826b8cf3d7bfdd64edca2a78530b82f`,420793byte. Media source/refs/prompt229 không đổi.

## Kết quả kiểm trực tiếp

| Lần | Đường thao tác | Kết quả trên UI |
| --- | --- | --- |
| 1 | In-app browser6/tab1, picker Thành phần → Tải nội dung nghe nhìn lên | Rights modal đóng, upload0%, rồi “Không tải được video lên. Hãy thử lại” |
| 2 | Cùng tab/picker, cùng file, retry intake không trả phí | Cùng lỗi; lưới có hai card thất bại, source chưa thành ingredient dùng được |
| 3 | Tab2 đã có đúng project/account, trình đơn dự án → Tải lên | Cùng lỗi và toast “Không tải R01_SOURCE_GUIDE_NOT_FINAL.mp4 lên được” |

Hộp quyền được xác nhận trong cùng thao tác tải đúng file/project khi retry; không đổi đích hoặc quyền “không hiện lại”. Ba lần là **tải tệp**, không ba lần tạo/test video. Không submit generation, không credit charge. Tab1 giữ draft229 trống; tab2 chưa đổi cấu hình sản xuất. Không xóa source/cards thất bại.

Tab2 hiển thị account hiện hành và **77 tín dụng**. Không thêm tiền, không suy số dư thành quyền chi. Không có quote được xác minh với đủ ingredients; giá draft trống không là giá request R01.

## Phân biệt dữ kiện và giả thuyết

Đã kiểm lại source file và FFmpeg decode toàn MP4: exit0, không lỗi giải mã. Hồ sơ229 probe4s/96frames/H.264360×640/AAC48kHz/stereo còn đúng. Browser console error/warn trả danh sách trống trên cả hai tab; không có mã lỗi để quy nguyên nhân cho backend.

**Dữ kiện:** Flow không nhận upload thành công bằng các đường đã thao tác; tệp local đọc/giải mã được; generation chưa được gửi.

**Chưa biết:** lỗi upload do session/trình duyệt tự động, chuyển file, validation của Flow hoặc dịch vụ. Không kết luận file hợp lệ theo FFmpeg đồng nghĩa Flow bắt buộc hỗ trợ; cũng không nói prompt/hành động gây lỗi khi chưa gửi prompt.

Không đổi duration/voice/script/ref hoặc tạo video mới để tránh intake; không cài/mở API/vendor mới. Không lấy source video cũ trên project có nhiều thoại rồi gọi là input229.

## Bước cần human checkpoint

Owner thử **tải đúng một file nguồn trên bằng thao tác tay** vào project EP01 hiện hành (trình đơn dấu+ → Tải lên). Không bấm tạo video. Nếu tải tay thành công, báo tên/card xuất hiện để root chọn nguồn, gắn S/M/E, kiểm route và quote, trình một request production. Nếu cùng file tải tay cũng thất bại, lưu thông báo thực rồi mới chọn bước kiểm định dạng/dịch vụ; chưa có lý do chạy lại nhiều lần tự động.

Đây là checkpoint kiểm nguyên nhân intake, không yêu cầu owner chuẩn bị ảnh, dựng phim hoặc làm QC kỹ thuật thay root. Không tăng credit.

## Evidence và tổng hợp

[Consent](evidence/230/owner-upload-consent.json), [lỗi hai lần](evidence/230/01_upload-failed-twice.png), [lỗi đường dự án](evidence/230/02_upload-failed-project-menu.png); AX cùng tên trong folder230. Gói nguồn/ref/prompt và reports229 giữ nguyên; acceptance sourceB không đổi. G1/outputAV/master chưa đạt.

Đã xác định và chốt: owner đồng ý upload, đã thực hiện đúng nút; lỗi intake lặp ở hai tab; chi0/số dư77. Giả định tiếp tục: giữ package229 và route video-edit dự kiến, chưa nhận capability/quote. Còn mở: file phải được nhận đúng trên Flow và căn nguyên lỗi intake. Bước tiếp: một lần upload tay cùng file để tách lỗi thao tác khỏi lỗi dịch vụ/file; sau thành công mới hoàn tất quote/approval sản xuất, không mở batch test.
