# 14 — Chính sách cập nhật upstream

Submodule giúp giữ nguyên nguồn, lịch sử và giấy phép của dự án ngoài, đồng thời ghim chính xác phiên bản đã kiểm tra. Việc một upstream cập nhật không tự động thay đổi Agentic Cinema.

## Nhịp cập nhật

- Kiểm tra trước khi bắt đầu milestone mới hoặc khi cần bản sửa lỗi/API cụ thể.
- Không cập nhật hàng loạt chỉ vì upstream có commit mới.
- Mỗi lần cập nhật phải ghi rõ lý do, release notes liên quan và phạm vi kiểm thử lại.

## Quy trình

1. Bảo đảm working tree cha và toàn bộ submodule sạch.
2. Chạy `powershell -NoProfile -ExecutionPolicy Bypass -File ./scripts/update-submodules.ps1 -WhatIf` để xem phạm vi.
3. Chạy `powershell -NoProfile -ExecutionPolicy Bypass -File ./scripts/update-submodules.ps1` trên branch riêng.
4. Xem diff gitlink bằng `git diff --submodule=log`.
5. Kiểm tra license/NOTICE, breaking changes, security advisory và dependency requirements.
6. Chạy test/eval của milestone chịu ảnh hưởng.
7. Commit gitlink sau khi review; không commit trực tiếp trên branch mặc định.

## Release gate

Một cập nhật chỉ được chấp nhận khi:

- tám submodule khởi tạo được bằng `scripts/bootstrap.ps1` trên Windows;
- `scripts/verify-submodules.ps1` xác nhận đúng commit, sạch và không shallow ở checkout mặc định;
- không có license mới hoặc NOTICE bị bỏ sót;
- API/pattern được tham khảo có test hoặc tài liệu xác minh tương ứng;
- không thêm import runtime từ `ext/`;
- rollback chỉ cần hoàn nguyên gitlink về commit trước.

## Xử lý Windows long paths

`generative-ai` có đường dẫn đủ dài để checkout lỗi khi đặt repository trong thư mục sâu. Các script luôn truyền `-c core.longpaths=true` cho Git và dùng `ext/` để giữ đường dẫn ngắn. Nếu workspace cha vốn đã quá sâu, clone Agentic Cinema gần gốc ổ đĩa trước khi bootstrap.

## Shallow checkout

`-Shallow` chỉ dành cho CI hoặc máy tạm cần build nhanh. Contributor nghiên cứu/đối chiếu lịch sử phải dùng checkout mặc định đầy đủ. Verification mặc định coi shallow repository là lỗi; chỉ `bootstrap.ps1 -Shallow` mới cho phép trạng thái này.
