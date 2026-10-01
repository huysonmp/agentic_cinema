# EP01 — Duyệt probe tiếng và kiểm giá thực

2026-10-01 (Asia/Saigon). Owner trả lời `duyệt nhé` trực tiếp request85. `REQUEST85_APPROVED / COST_VERIFIED_UI / CAP_RECONCILIATION_HOLD / NOT_GENERATED`.

## Phạm vi được duyệt

Hai probe V01/V02 và reference T-NB-03_v0.8 theo85; V01 trước rồi đối soát, V02 sau; Quality/frames/9:16/8 giây/x1; không retry/biến thể, đổi model/provider, mua credit hoặc sản xuất toàn tập. Giữ điều kiện giá/cap/terminal của85. Không coi approval request là duyệt voice take chưa tồn tại.

## Preflight thực hiện

- Đọc account panel đúng Flow project9276788e-9781-44fb-ba5b-083006667374: số dư1.050 credit. Không có ledger itemized trong panel đã đọc; các đường account/credits hiển thị AccountChooser nên không mở sang tài khoản khác hoặc tự mua/upgrade.
- Đóng agent settings không Lưu. Tắt chế độ composer Tác nhân để kiểm cấu hình tạo trực tiếp, không đổi bảo vệ `Luôn luôn` trong agent settings. Composer ban đầu Image/Pro/9:16/x3; KHÔNG tạo theo mặc định này.
- Đổi riêng cấu hình request sang Video → Khung hình → Veo3.1Quality → x1. AX và screenshot:9:16, giá100 credit; composer badge720p/8 giây/x1. Trước chọn đúng Quality/x1, giá36 của model trước/x3 và300 của Quality/x3 không phải giá request được duyệt.
- Bằng chứng local: `C:/Users/PC/Downloads/du_an_nem_bui/P6_VOICE_QUALITY_x1_100credits.jpg`. Chưa chọn ảnh đầu, chưa nhập prompt, chưa bấm Bắt đầu tạo; không có generationID/output hoặc khoản trừ do vòng này. Cấu hình request còn trên UI cho lượt sau, không lưu mặc định tài khoản.

## Điểm dừng ngân sách

Hai lượt100+100=200 credit dự kiến sẽ dùng trọn trần200 cũ. Các lượt ảnh trước có giáUI0 và nhiều số dư quan sát không đổi; F02 còn UNRECONCILED, chưa ledger itemized xác định tổng đã dùng. Không lấy số dư1.050 làm bằng chứng còn200 trong cap của dự án. Theo85, chưa đủ điều kiện xác nhận cả hai lượt nằm trong phần cap còn lại; vì vậy HOLD trước V01, không tiêu thử100 rồi mới hỏi.

Đề nghị owner cấp **ngân sách riêng tối đa200 credit cho đúng hai probe V01/V02**, thay điều kiện phải dùng phần còn lại của trần cũ cho request này, không thay/xóa lịch sử cap41. Nếu owner muốn giữ nguyên cap cộng dồn cũ, cần đối soát khoản cũ trước; không tự hạ model để vượt qua điểm dừng. Giá thay đổi hoặc tổng vượt ngân sách riêng nếu được duyệt → dừng hỏi, không auto retry.

## Tổng hợp

Đã xác định: request85 approved, giáQuality x1 thực trênUI100/lượt, video720p/8giây/dọc. Đã chốt: hai nội dung probe và input v0.8. Giả định: giáUI là dự toán trước submit, không billing actual. Còn mở: quyền ngân sách riêng hoặc đối soát cap cũ; ảnh đầu binding, đầu ra tiếng/QC/selection. Tiếp theo: owner giải quyết đúng điểm ngân sách; operator bind v0.8/nhập exact V01/read-back rồi submit một lần nếu đủ điều kiện, lưu và nghe trước V02. Voice vẫn NOT_TESTED, P6/P7 chưa đóng.
