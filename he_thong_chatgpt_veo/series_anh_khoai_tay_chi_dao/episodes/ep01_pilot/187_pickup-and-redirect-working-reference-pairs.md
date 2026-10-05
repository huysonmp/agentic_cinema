# EP01 — Chuẩn bị khung gắp–nâng và đổi hướng sang bát Đào

Ngày 2026-10-05. Owner đồng ý tiếp tục bước local đã trình ở 186; không tăng ngân sách hoặc nghiệm thu video. Giữ C-v0.6/K20/D06, bàn ăn 78 và SIA-01 HOLD theo việc hoãn kiểm speaker. Không sửa bản kiểm nối 186 hoặc bản planning 30 giây tại 182.

## Đã thực hiện

Skill imagegen tích hợp, không API/key/cài đặt mới: xem nguồn, tạo START gắp v0.1, sửa điểm tiếp xúc thành v0.2, tạo START đổi hướng v0.1. Hai END sao nguyên byte từ nguồn thực tế. Lưu ở `C:/Users/PC/Downloads/du_an_nem_bui/187_action_bridge_inputs` và workspace; giữ tất cả bản gốc.

| Nhịp dự kiến | START | END | Giới hạn |
| --- | --- | --- | --- |
| Gắp từ đĩa về trước bát Khoai | [START v0.2](../../assets/references/187/START_pickup_v0.2.png) | [END native](../../assets/references/187/END_pickup_NATIVE_H185_in_0.png) | START mới chạm phần nem trên đĩa. END sao frame đầu V02. Chưa có chuyển động nối. |
| Đổi hướng từ Khoai sang Đào | [START v0.1](../../assets/references/187/START_redirect_v0.1.png) | [END từ 186](../../assets/references/187/END_redirect_EXACT_186_START.png) | Nem ở phía Khoai rồi trên bát Đào; Đào đã giữ bát. Không gồm nhịp rời cốc/đưa bát hoặc release. |

START gắp v0.1 có miếng nem treo trên đĩa: REWORK, [giữ bản lỗi](../../assets/references/187/START_pickup_v0.1_REWORK.png). v0.2 sửa đầu đũa chạm phần nem trong mound. Chưa thử video, không gọi sửa ảnh là chữa nguyên nhân gốc của lỗi động tác.

## Kiểm actual và gate còn mở

Root đã xem các ảnh: đầu to đũa ở grip, đầu nhỏ hướng món; không thấy hơi ở các ảnh này. Đây không phải kiểm dynamic anatomy, bảo toàn miếng nem hoặc vapor toàn video. Gói gắp giữ trục/cỡ cảnh làm việc của H185 nhưng START mới 941×1672, END native 720×1280; hình tạo không pixel-invariant. Gói đổi hướng rộng hơn H185; cần kiểm trạng thái tay/góc đũa/phần nem qua đổi cỡ cảnh, không suy cùng trục là đã nối đúng.

**FOOD còn REWORK:** mound lớn/sợi to của nguồn cận tay khác món gọn/sợi mảnh ở bàn ăn 78. Dùng nguồn để lập đường hành động không duyệt lại hình món. Cần sửa/thống nhất nguồn trước thử có phí. Nếu sửa food ở END native, nó không còn nguyên frame của V02: phải kiểm lại nguồn nâng, không ép nối source sai chỉ vì muốn tận dụng clip.

END đổi hướng trùng file với START đặt nem 186 chỉ là identity của đầu vào, không bảo đảm Veo giữ END pixel-identical hoặc match-on-action. Đào đã giữ bát trong gói này; nhịp rời cốc/đưa bát vẫn thiếu. Còn thiếu diễn quay lại–Khoai khựng và kết. Không chạy agent/reviewer độc lập; root inspection không independent PASS. Không đổi voice hoặc dùng script/ASR để nhận diện người nói.

## Bằng chứng và kiểm kỹ thuật

[Bảng sáu khung](evidence/187/187_STILL_INPUTS_NOT_MOTION_v0.1.png) là bố trí ảnh QA, không nội suy hoặc tăng coverage video. Root đã xem actual: nhãn không che grip/watermark, có ghi chỗ đổi cỡ cảnh và nhịp cốc/bát thiếu. [Preflight/hash](evidence/187/bridge-input-preflight.json) giữ `ready_for_paid_submission: false`; [report bảng](evidence/187/board-report.json) ghi sáu nguồn và kích thước/hash.

Ba prompt ảnh và hai video draft nằm trong [evidence](evidence/187), chưa gửi video. Script `scripts/render_ep01_bridge_reference_board.py` chỉ bố trí ảnh: đã chạy thực tế bằng runtime bundled có Pillow, kiểm hash/đọc sáu PNG, xuất 1080×1460, qua py_compile và thử từ chối ghi đè. Python mặc định thiếu Pillow; dùng runtime có sẵn, không cài mới. Đối soát hai END với nguồn và năm asset workspace với folder owner. Technical checks không là creative PASS.

## Ngân sách và thứ tự tiếp tục

Chi Flow lượt này 0; sổ 232/255, còn **23 credit**. Không mở Flow/đọc giá live. Quote x3 Lite lần gần nhất 30, không phải giá mới; không gửi x1/x2 để lách standing rule. Nếu vẫn 30, riêng một batch thiếu ít nhất 7, không có nghĩa 7 đủ hoàn thành các cảnh. Chưa xin/nhận tăng trần hoặc Quality/master/publish.

Tiếp theo: sửa hình món bằng nguồn đã duyệt → khóa lại khung và nhịp cốc/bát–quay lại–khựng → kiểm quyền chi/quote live trước x3 → tải/decode/kiểm actual và điểm nối → cập nhật coverage thật. SIA, thoại–môi, dựng, nhãn AI và QC bản xuất vẫn bắt buộc trước bàn giao.

## Tổng kết vòng

- Đã xác định: hai cặp khung làm việc, bảng sáu trạng thái, lỗi START gắp đã sửa và lưu lịch sử.
- Quyết định giữ nguyên: nội dung/giọng, hoãn speaker check, đặt nem vào bát, không chi thêm Flow.
- Giả định: nguồn cùng cỡ cảnh và END nguyên file có thể giảm lệch nối; chưa có video chứng minh.
- Còn mở: FOOD/source fidelity, diễn động, cốc/bát, điểm nối, speaker QC và ngân sách.
- Bước tiếp theo: sửa nguồn món trước khóa gói thử động; còn 23, chưa paid batch.
