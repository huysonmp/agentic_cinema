# EP01 — Hồ sơ làm lại trực tiếp ở 720p

Kế hoạch236 đã được owner duyệt tại237. Đây là hồ sơ mới, không nhập footage cũ hoặc coi các approval media cũ là approval clip mới.

## Hiện trạng

- Trần dự trù được duyệt: 500 credit; đã chi: 0; còn trong trần: 500.
- Account đã được owner xác nhận; project **EP01 Nem Bùi — Khoai & Đào — 720p v1** đã tạo, giữ project cũ.
- URL: https://flow.google.com/project/bcb1f53c-13b6-4719-b866-01348dfcddd6.
- Đã kiểm Omni 1.1 Flash / Ingredients / 720p / 9:16 / 10s / x1 / Agent OFF; composer trống báo 15 credit, không quote cuối của C02.
- REC238: owner duyệt hai preset và quyền tự vận hành có giới hạn. K20/Orus và D06/Aoede đã lưu với ID mới; owner chưa nghe duyệt trên nick mới. Xem `03_voices/bindings-238.json`.
- MASTER01 v1 đã tạo/tải gốc; reviewer chặn vì chất liệu nem giống mì. V2 sửa giá 0 đã tải và qua review ảnh tĩnh độc lập: lỗi món đã đóng, crop mép và tỷ lệ file còn nhỏ, cần owner chấp nhận hoặc yêu cầu sửa. Không tự mở C02.
- Clip đầu tiên vẫn là C02, Khoai kể ký ức. Chưa chạy video: cần qua checkpoint ảnh master + hai giọng, rồi đối soát exact inputs, quote và output720p.
- Các đơn vị: C01A, C01B, C02, C03A, C03B, C04, C05, C06, C07, C08, C09. Thứ tự sinh theo kế hoạch 236, không theo tên file.

## Hồ sơ

1. `00_decisions/plan-approval.json`: quyền và phạm vi duyệt.
2. `03_voices/recreation-blueprint.md`: chỉ dẫn gốc; trạng thái tạo thực và ID mới nằm ở `bindings-238.json`.
3. `04_requests`: chỉ dùng cho exactrequest đã chuẩn bị, không ghi giá public như quoteactual.
4. `05_native`: giữ originals khi nhận; không xóa/ghi đè media cũ.
5. `06_qc`: kết quả kiểm targethash/range/capability và findings.
6. `07_edits`, `08_delivery`, `09_lessons`: bổ sung khi thực làm, không placeholderPASS.

Giữ dữ liệu đăng nhập và screenshot account ở máy, không đưa vào Git. Số dư UI không thay trần quyền chi. `00_decisions/scoped-autonomy-238.json` thay quyền xin từng request: chỉ720p/x1/quote≤15 trong phân bổ500, dừng khi lặp cùng blocker lớn hai lần. Dự phòng110, giá cao hơn, đổi công cụ/script/giọng vẫn phải trình owner. Giữ checkpoint chất lượng ban đầu, C02, rough cut và final.
