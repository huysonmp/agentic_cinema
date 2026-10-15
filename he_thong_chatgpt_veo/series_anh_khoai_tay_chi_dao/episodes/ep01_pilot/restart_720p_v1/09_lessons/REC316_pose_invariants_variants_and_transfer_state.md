# REC316 — Bất biến tư thế, biến thể dàn cảnh và trạng thái cho–nhận

15/10/2026. Kinh nghiệm từ các output tĩnh thực, không phải thử nghiệm motion hoặc kết luận phổ quát về model.

## Quan sát có bằng chứng

- S1 v1 nâng/chìa tay kẹp A khi brief chỉ muốn Đào đưa bát. S1 v2 sửa từ v1 vẫn giữ phần tư thế đã lệch; không đạt brief giữ tay ban đầu.
- Sau hai lỗi cùng loại, dừng nhánh sửa đó, quay về S0 đã duyệt với prompt hẹp hơn. V3 đưa tay gần mốc hơn nhưng bát/hand hỗ trợ quá sát tay nghỉ Khoai theo hình chiếu, chưa chấp nhận clearance.
- V2 có bố trí đón dễ đọc hơn trong still, nhưng chỉ có thể trình dưới nhãn **biến thể thay đổi blocking**, không đổi lịch sử thành brief cũ đã đạt.
- S2 thể hiện A trong bát/tips trống; S3 còn A trong bát và có B ở đũa Khoai. Điều này chưa chứng minh nhả một lần hoặc B thực sự được gắp mới.

## Giả thuyết cần giữ đúng mức

Dùng output lệch làm edit target có thể củng cố tư thế sai. Việc đổi về nguồn gốc trong lần v3 là thay chiến lược sau chẩn đoán, không phải thêm một lượt cùng prompt cho tới khi may mắn. Chưa có ablation để khẳng định input priority hay một câu prompt cụ thể là nguyên nhân duy nhất.

Ảnh có khoảng tách nhìn rõ hơn không chứng minh đường chuyển trong 3D thuận hơn hoặc tỷ lệ thành công native cao hơn. Không dự báo tiết kiệm credit từ các still này.

## Quy tắc vận hành áp dụng tiếp

1. Tách **đúng bất biến**, **đẹp/đọc được**, **biến thể có điều kiện** và **actual native PASS**. Một ảnh có thể hợp ý đồ nhưng không đạt bất biến đã yêu cầu.
2. Nếu muốn giữ output vi phạm bất biến làm một hướng mới, khai đúng phần thay đổi, giữ hash/bản lỗi cũ và xin quyết định trước production. Alias cùng byte không tạo ra approval mới.
3. Ledger chuyển trạng thái phải theo đối tượng: S0 A còn kẹp/bát trên bàn; S1 bát rỗng đón; S2 A ở bát/tips trống; S3 A giữ nguyên và B mới. Không hoán đổi endpoint sau nhận làm START trước nhận.
4. Chỗ khác pose cần cầu chuyển động: nâng bát/dịch tay, nhả A, gắp B mới, đưa bát về. Không dùng cut hoặc reframe để che việc nguồn chưa làm được.
5. Kiểm cả bàn và quyền sở hữu tay/bát/cốc, không chỉ miệng. Không giải clearance bằng thêm bát, cốc vào bát, tay Khoai đỡ bát cô, hoặc âm thầm đặt cốc xuống.
6. Approval cấp hướng/ảnh không mở paid request, không thừa kế ngoại lệ của một rough khác và không đóng final30/AV.

Hồ sơ ảnh/inputs/prompt: `02_refs/receive_ending_316/reference_manifest_316.json`. Phạm vi kiểm: root static only, không báo cáo phản biện độc lập mới. Không chạy Flow; chi Flow 0, không khẳng định toàn bộ usage imagegen miễn phí.
