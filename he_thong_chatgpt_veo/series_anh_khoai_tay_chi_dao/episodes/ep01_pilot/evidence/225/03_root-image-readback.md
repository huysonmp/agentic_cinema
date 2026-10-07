# REC225 — Root đọc lại ba ảnh sửa v02

Ngày 2026-10-07. Đã trực tiếp xem đủ ba v01 và ba native v02. Scope chỉ ảnh tĩnh, không chuyển động/AV hoặc speaker/lip-sync. Chưa thay nghiệm thu owner hoặc review độc lập.

## Quan sát

| Ảnh | Expected | Observed trên native v02 | Disposition sơ bộ |
|---|---|---|---|
| M | Chỉ đổi tay đang vươn: ngón ở ngoài vành phải nhìn thấy, có khoảng hở, không nằm trên vùng món | Tay Đào vẫn vươn vào phía sau-trái của đĩa/vùng trên món, gần tư thế v01. Hai môi khép, tay kia nghỉ, bộ bàn giữ. Không đọc được vành phải/gap như yêu cầu. | REWORK/HOLD. Không chọn làm reference của động tác lấy đĩa. |
| E | Khép môi cả hai, giữ phần còn lại | Khoai có nét cười kín; môi Đào khép. Ánh nhìn qua nhau, tay nghỉ, bát trống và đồ phục vụ còn đúng vị trí tương đối. | Ứng viên đã sửa được yêu cầu môi; cần hai reviewer/owner. |
| REF03-S | Chỉ khép môi Đào, giữ Khoai cười kín | Môi Đào khép, Khoai vẫn cười kín. Ánh nhìn qua nhau và bộ bàn F0 giữ. | Ứng viên đã sửa được yêu cầu môi; cần hai reviewer/owner. |

Không thấy khói từ nem, food transfer, đũa/cốc cầm sớm, bát riêng có thức ăn hoặc đổi người/đổi phía. Tái sinh có thay chi tiết/độ nét nhỏ; không gọi là chỉ đúng một vùng pixel thay đổi.

## Truy nguồn lỗi còn mở

Đã kiểm hash source v01 và prompt trong request; đúng một source tương ứng qua picker, đúng model/image/9:16/x1/quote 0 trước mỗi submit. Output M có UUID mới `c7f5c1f4-4020-408d-b317-d81634dfa964`, prompt sửa đúng trong nhật ký output, native download/hash mới. Không có bằng chứng dùng nhầm E/R03, gửi prompt cũ, tải source v01 hoặc lỗi dựng.

M thất bại ở **tuân thủ thay đổi hình học tay trong output**. E và R03 sửa môi được trên cùng route, nên không kết luận toàn route edit không hoạt động. Vì sao model không đổi tay chưa xác định. Khả năng nguồn M đã neo mạnh tư thế sai và cách khóa phần còn lại làm thay đường tay khó hơn chỉ là giả thuyết.

Quan sát hình học để chuẩn bị đề nghị tiếp: tay M đang vươn là tay phía trong, gần Khoai; đích vành phải nằm cạnh/phía dưới bát Đào. Đổi tay đó sang đích phải có nguy cơ che/xuyên bát. Có thể dùng S với cả hai tay nghỉ làm nguồn mới và chọn tay phía ngoài, bên phải ảnh gần cốc, để hướng xuống vành phải; không tự đổi nguồn hoặc chạy lượt thứ hai trong quyền hiện tại.

## Ranh giới

Đã dùng đủ ba lượt được duyệt, mỗi lượt quote 0; số dư live 77 → 77. Không retry, không video/voice/Quality. Hai reviewer độc lập đang kiểm nguyên bản, chưa lấy việc giao task làm PASS. G1 toàn tập vẫn mở; sửa được môi ảnh không chứng minh hành động kéo–dừng hoặc AV đã đạt.
