# EP01 — Duyệt chất liệu 188 và đồng bộ khung hành động

Ngày 2026-10-05. Owner trả lời **“ok r nhé”** sau câu hỏi “chỉ duyệt chất liệu, chưa duyệt toàn cảnh”. Ghi đúng phạm vi: **APPROVED_TEXTURE_ONLY** cho hai PNG 188 có hash trong preflight. Không suy thành duyệt lượng/bố cục, khung mới, diễn động, FOOD toàn cảnh hoặc tăng credit. Cập nhật 188 với approval nhưng giữ nguyên media và phần lịch sử.

## 1. Đã thực hiện bước tiếp theo

Dùng skill imagegen tích hợp, đã xem target/reference trước sửa. Bốn ảnh mới tiếp nối chất liệu 188, không dùng API/key, Flow hoặc cài mới. Nguồn 78 hỗ trợ bàn/serving context; H185 chỉ hướng dẫn pose, không đưa food cũ trở lại.

| Nhịp làm việc | START | END | Trạng thái |
| --- | --- | --- | --- |
| Gắp → trước bát Khoai | START gắp 188 | END gắp 188 | Giữ nguyên hai file; owner duyệt chất liệu, chưa diễn hoặc cả cảnh. |
| Nâng → dừng | END gắp 188 | [END nâng mới](../../assets/references/189/END_lift_pause_v0.1.png) | Tuft trước áo, dưới cổ áo. Ảnh dừng không chứng minh diễn khựng khi bị bắt gặp. |
| Đổi hướng → bát Đào | [START mới](../../assets/references/189/START_redirect_food_v0.1.png) | [END chuyển/START đặt](../../assets/references/189/END_redirect_START_deposit_v0.1.png) | Nem từ phía Khoai sang trên bát Đào. Đào đã đỡ bát, chưa thả nem. |
| Đặt xuống bát | Cùng file END chuyển | [END đặt mới](../../assets/references/189/END_deposit_food_v0.1.png) | Phần nem trong bát Đào dưới vành; đầu đũa trống/tách nhẹ; bát Khoai trống. |

END chuyển và START đặt dùng **chính cùng file**, không sinh thêm bản gần giống. END gắp 188 cũng là START nâng. Chỉ identity đầu vào được khóa; chưa video bảo toàn trạng thái hoặc giữ endpoint đúng.

Folder owner `C:/Users/PC/Downloads/du_an_nem_bui/189_synced_action_refs` có đủ sáu PNG. Bốn ảnh mới lưu trong workspace; hai ảnh 188 được tham chiếu nguyên hash và copy vào folder owner để gói local đầy đủ. Không ghi đè nguồn 185–188 hoặc sửa bản 30 giây 182.

## 2. Root kiểm actual cả chuỗi

[Bảng sáu trạng thái](evidence/189/189_SYNCED_STILL_INPUTS_NOT_MOTION_v0.1.png) đã được xem actual. Rau/hai chấm/hai bát/cốc còn trong khung hai nhân vật; crop cận Khoai không thấy mọi vật ngoài khuôn, không đồng nghĩa vật bị dọn. Đầu to đũa ở grip, đầu nhỏ hướng món/bát; không thấy hơi ở bốn ảnh mới. Phần nem trong bát Đào và đầu đũa trống xuất hiện ở END đặt.

Những điều **chưa chứng minh**: lượng/tỷ lệ đĩa qua wide shot 78 và crop mới; tuft giữ nguyên chi tiết/kích thước/khối lượng; chiều dài đũa/giải phẫu qua chuyển động; microgeometry món không đổi pixel. Giữa khung nâng một người và START đổi hướng hai người có đổi cỡ cảnh/pose, chưa match-on-action. Chất liệu đã được chuyển sang ảnh mới nhưng approval của hai file 188 không tự duyệt mọi chi tiết ở ảnh sinh lại.

Chưa có diễn Đào quay lại–Khoai khựng hoặc nhịp Đào rời cốc/đỡ bát. Không gán endpoint một “khựng” đã diễn đạt. Khung bắt gặp 185 vẫn chỉ ảnh tạm, không được dùng như video đã đạt. Chưa chạy reviewer độc lập; đây là root inspection, không independent PASS.

## 3. Bằng chứng và kỹ thuật

[Preflight/hash/approval](evidence/189/action-sync-preflight.json) giữ `ready_for_paid_submission: false`. [Bốn prompt ảnh](evidence/189) và [bốn video draft chưa gửi](evidence/189/video-prompts-DRAFT-NOT-SUBMITTED.txt) mô tả phạm vi riêng, điểm chung và QC. [Report bảng](evidence/189/board-report.json) ghi kích thước/hash sáu PNG, đều 941×1672 RGB và đọc/giải mã ảnh đủ; owner copies khớp source.

Mở rộng script bảng bằng `--config`, không thay default187. Đã render189 1080×1460, xem nhãn/toàn hình, qua py_compile; render lại default187 ra hash nguyên `0cecd73cecef9b6f026fe4324fb1384d1968fb77c79d711c6c081ef009d475c4`. Rerun vào thư mục189 có nội dung bị từ chối exit2, hash bảng không đổi. Đây là kiểm kỹ thuật và layout, không FOOD/diễn PASS.

## 4. Sẵn sàng đến đâu và ngân sách

- C-v0.6/K20/D06 giữ nguyên; SIA HOLD theo việc owner hoãn kiểm, không trở thành PASS.
- Đã có đầu vào tĩnh cập nhật chất liệu cho bốn nhịp. **Không có video mới; coverage đạt tăng 0 giây**, không Quality/master/publish.
- Chi Flow lượt này **0**, sổ **232/255, còn 23**. Không mở Flow hoặc đọc quote/số dư live. Quote x3 Lite lần gần nhất 30 chỉ là lịch sử.
- Nếu vẫn tách bốn nhịp và quote mỗi x3 vẫn 30, dự tính cơ học là 120, thiếu 97 so với số23. Đây không phải báo giá hoặc ngân sách hoàn tất: chưa gồm phản ứng/cốc–bát/cảnh khác và retest. Không hứa 7 credit đủ hoàn thành video.
- Bước thử đề xuất đầu tiên là **gắp từ đĩa về trước bát Khoai**, x3, tổng không quá30 nếu owner duyệt gói thử và quyền chi; với số dư23 cần bổ sung tối đa7 cho riêng một batch. Chưa nhận quyền đó, không gửi x1/x2 để lách standing rule. Đọc live quote trước submit; vượt trần phải hỏi lại.

## Tổng kết vòng

- **Đã xác định:** owner duyệt chất liệu hai ảnh188; tạo bốn ảnh tiếp nối, có bảng sáu trạng thái và gói thử draft.
- **Quyết định đã chốt:** APPROVED_TEXTURE_ONLY đúng hash; nội dung/giọng/claim/bàn ăn giữ nguyên, không chi thêm hoặc duyệt video.
- **Giả định:** endpoint chung có thể giảm lệch nối; lượng/tuft và hiệu quả qua video chưa được chứng minh.
- **Còn mở:** duyệt gói thử, continuity qua cỡ cảnh, lượng/miếng nem, diễn/phản ứng/cốc–bát, speaker QC và ngân sách trước paid batch.
- **Bước tiếp theo:** owner xem bảng/gói, chốt quyền thử đầu tiên và phần credit thiếu; sau đó kiểm quote live rồi mới thử ba Lite. Không tự mở Quality.
