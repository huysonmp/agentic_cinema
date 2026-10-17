# REC325 — Đã chuyển media về một kho, bỏ các bản rải rác

Ngày 17-10-2026. Owner yêu cầu chuyển media về một thư mục để có thể tự xóa cho nhẹ máy. Sau khi được hỏi rõ phạm vi, owner chốt: **“Chỉ gom, để tôi tự xóa kho”**. Vì vậy agent giữ nguyên kho cuối cùng, không xóa thêm.

## Kết quả đã kiểm

- Đã bỏ **13.020 bản nguồn** đúng danh mục REC324 V2, tổng dung lượng logic 11.056.581.980 byte (khoảng 11,06 GB). Không quét xóa tùy ý toàn bộ Downloads hoặc dự án khác.
- Kho còn giữ tại `D:/Workspace/agentic_cinema_media_archive/EP01_Nem_Bui_20261017`: **11.784 nội dung media duy nhất**, 9.447.100.717 byte (khoảng 9,45 GB), kèm hồ sơ. Các bản trùng được gộp theo hash; không loại bỏ phiên bản có nội dung khác.
- Trước khi bỏ nguồn, đã tái kiểm SHA256 toàn bộ 13.020 nguồn và 11.784 tệp kho. Khi xử lý từng file, kiểm lại kích thước và thời gian sửa đổi để dừng nếu tệp thay đổi sau bước kiểm đầu vào.
- Dùng PowerShell native `Remove-Item -LiteralPath` cho từng file trong danh mục đã xác thực. Không xóa đệ quy, không xóa thư mục hoặc chuyển thao tác xóa qua shell khác.
- Kiểm sau cùng: không còn đường dẫn nguồn nào trong 13.020 mục; toàn bộ 11.784 tệp kho còn tồn tại, kích thước và thời gian sửa đổi khớp lần kiểm trước.
- Video REC323 đang chọn trong kho vẫn khớp SHA256 gốc: `d7f380e05bdcafb3eb2768ce0cc4d011c6ee7570a4ec24788ce0cdf4305e2845`.
- Bốn vùng đã gom hiện có **0 tệp media** theo tập đuôi đã kiểm: thư mục dự án mini, artifacts, Downloads/du_an_nem_bui và generated_images của đúng thread. Tài liệu văn bản và cấu trúc thư mục vẫn giữ nguyên.
- Không xóa tài liệu/mã nguồn, dự án khác hoặc dữ liệu Flow; không cài công cụ hay dùng credit.

## Dung lượng quan sát

| Ổ | Trống trước bước bỏ nguồn | Trống sau bước bỏ nguồn | Chênh tại lần đo |
| --- | --- | --- | --- |
| C | 8.059.150.336 byte | 16.656.252.928 byte | +8.597.102.592 byte, khoảng 8,60 GB |
| D | 83.227.234.304 byte | 85.692.977.152 byte | +2.465.742.848 byte, khoảng 2,47 GB |

Đây là chênh dung lượng tại hai thời điểm, có thể chịu ảnh hưởng của ghi log và phân bổ hệ thống tệp. Kho media khoảng 9,45 GB vẫn chiếm ổ D. So với trước khi tạo kho ở REC324, bước chuyển tập trung chủ yếu loại bỏ các bản trùng; chưa xóa toàn bộ nội dung media khỏi máy.

## Khả năng khôi phục và ảnh hưởng

Các bản nguồn bị xóa trực tiếp, **không qua Thùng rác**, nhưng có thể khôi phục nội dung từ kho và danh mục khi kho còn nguyên. Biên bản ghi chính xác đường dẫn nguồn, vị trí tệp trong kho và hash. Không thực hiện liên kết lại tự động: script/EDL dùng đường dẫn cũ sẽ không dựng lại trực tiếp cho tới khi phục hồi hoặc cập nhật đường dẫn.

Có 62 tệp media được Git theo dõi đã bị xóa khỏi working tree; không sửa lịch sử Git. Media từng bị ignore không có cơ chế phục hồi từ Git; kho là bản lưu local hiện tại của chúng. Biên bản này chỉ ghi việc chuyển kho, không thay đổi các giới hạn nghiệm thu chất lượng của REC323. Media chỉ có trên Flow chưa được kiểm kê hoặc tải bổ sung.

## Biên bản

- Script: `scripts/consolidate_ep01_media_325.ps1`.
- Kế hoạch, biên nhận, nhật ký từng file, kết quả và kiểm sau thao tác: `restart_720p_v1/06_qc/MEDIA_CONSOLIDATION_325/`.
- Bản sao biên bản trong kho: `09_BIEN_BAN_CHUYEN_325/`.
- SHA256 biên nhận: `f0c76963c60482187f20e23b1127874a0fbbd526fae8ebc0da3dfe33580e56c7`.
- SHA256 kế hoạch: `975f361b31fcb2ded333f1bcfc018a449c89c6621f45ee945c6291089d3e544e`.
- SHA256 danh mục nguồn REC324 V2: `07ece0c8bff5a98dd3caae2b09a9ec9e42c62fe41cccd8169697ac46e4d29ead`.

CSV lịch sử REC324 được giữ nguyên; cột `source_retained` mô tả thời điểm sao chép, không phải trạng thái sau REC325.

## Quyết định cuối

Đã chốt chỉ gom, để owner tự xóa kho. Agent không được giao xóa thư mục kho duy nhất này. Khi owner tự xóa hẳn kho, phần lớn media sẽ không còn bản local để khôi phục; tài liệu/mã nguồn, lịch sử Git và dữ liệu Flow không nằm trong thao tác gom này.
