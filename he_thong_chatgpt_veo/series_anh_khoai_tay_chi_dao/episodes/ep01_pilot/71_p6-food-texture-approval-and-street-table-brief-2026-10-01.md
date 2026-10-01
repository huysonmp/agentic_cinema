# P6 — Duyệt texture và brief bàn ăn ven phố

Ngày 2026-10-01. Trạng thái: TEXTURE_APPROVED / SET_DIRECTION_APPROVED / SERVING_DESIGN_PROPOSED / NOT_GENERATED.

## Quyết định owner

Owner “duyệt nhé” cho F-NB-05, đồng thời yêu cầu có rau/lá, đồ chấm, cách dùng và bàn ăn. Sau giải thích phạm vi, owner chọn “kiểu quán nhỏ ven phố, bình dân và gọn gàng như hướng trước”.

- Chốt texture món F-NB-05_v0.1, SHA256 `C562A77D4A79D6A01E1518191796283810B6E40ADEF814A299B85960099C7E28`; file và QC tại70. Không sửa texture tiếp nếu chưa có vấn đề mới được owner xác nhận.
- Chốt quán nhỏ ven phố, bình dân/gọn gàng, ánh sáng chiều tối theo64. Không đổi sang mẹt nhiều món hoặc nhà hàng sang trọng.
- Không chốt framing crop của F05, đồ ăn kèm cụ thể, food motion hoặc P6 toàn bộ. Không generation trong vòng này.

## Tư liệu cách phục vụ — đã kiểm lại trực tiếp

1. [VnExpress, Phong Vinh,16/01/2016](https://vnexpress.net/nem-bui-mon-dac-san-dan-da-o-bac-ninh-3341749.html): mô tả cuốn lá sung hoặc lá đinh lăng, chấm tương ớt hoặc nước mắm tùy khẩu vị. Đây là lựa chọn được nguồn mô tả, không một chuẩn duy nhất cho mọi nơi.
2. [Cổng du lịch Bắc Ninh, Út Thương,23/04/2026](https://mybacninh.vn/vi/detailnews/?id=news_3068&t=nem-bui-mon-an-dan-da-dam-hon-que-kinh-bac): mô tả ăn kèm lá sung/lá đinh lăng. Không kế thừa claim độc quyền, sức khỏe hoặc hạn bảo quản vào episode.

Ảnh tham chiếu owner duyệt68 dùng cho cấu trúc món và tham khảo lá, không tự xác định mọi loại lá qua ảnh. F05 đã bỏ đồ ăn kèm để test thành phần; không còn dùng food-only prompt đó cho bàn ăn đầy đủ.

## Bộ phục vụ đề xuất cho EP01

Một đĩa gốm trắng ngà chứa nem như texture đã duyệt; một đĩa nhỏ riêng có lá sung và ít lá đinh lăng; hai chén nhỏ tương ớt đỏ cho hai người. Chọn tương ớt cho phiên bản bàn ăn này vì có nguồn hỗ trợ, nhìn rõ trên hình; không tuyên bố loại chấm bắt buộc. Hai chén riêng là thiết kế phục vụ cho hai bạn, không claim phong tục.

Không thêm rau húng/mùi tùy tiện, bánh tráng, bún, tôm, giò hoặc đồ chiên từ ảnh mẹt. Không thêm chai nhãn hiệu, bia hoặc bảng tên quán. Hai bát nhỏ để nhận món; hai đôi đũa gỗ theo hướng grip đã duyệt62; cốc nước không nhãn phục vụ cue lấy cốc của Đào. Ly nước/bàn gỗ là styling, không fact địa phương.

## Bố trí chức năng — draft, kiểm bằng ảnh sau

Khoai phía trái/Đào phía phải theo set draft65, chưa khóa mọi camera axis. Bàn gỗ chữ nhật đủ mặt bàn cho hai người, ghế thấp bình dân. Đĩa nem giữa, đĩa lá phía sau đĩa nem nhưng trong tầm với; bát mỗi người ở phía trước; chén chấm cạnh bát nhưng ngoài đường đưa đũa. Cốc Đào bên ngoài bên phải để cô quay sang lấy; không nằm giữa hai người hoặc che món. Không đặt props chắn bát đưa ra nhận nem. Tỉ lệ/khoảng cách phải kiểm style frame, không bịa kích thước vật lý.

Background: quán ven phố hư cấu chiều tối, vài chi tiết bàn ghế và đèn ấm, không biển hiệu/logo/landmark. Món chính rõ, không decor lá rải đầy bàn. Không lấy việc giữ gọn làm lý do bỏ lá/chấm/cách ăn.

## Cách dùng nối kịch bản đã duyệt — không sửa thoại/hành động ngầm

Script32: Khoai gắp một phần nem rời, đưa về phía miệng nhưng chưa chạm; bị Đào bắt gặp, đổi hướng và đặt vào bát Đào. Không đổi thành cuốn lá hoặc đút ăn trong nhịp chữa cháy; không miếng đã cắn. Cảnh kết anh gắp phần khác, không bắt buộc quay cảnh nhai.

Lá và tương ớt sẵn trên bàn thể hiện lựa chọn ăn kèm. Nếu muốn quay rõ bước Đào cuốn/chấm/ăn, đây là action bổ sung cần owner duyệt riêng và kiểm thời lượng30s; không tự thêm ngay. Gắp cho người khác chưa phải thao tác ăn hoàn chỉnh; không trình bày cú gắp như hướng dẫn duy nhất ăn nem Bùi.

## Kiểm chất lượng cần làm

- Texture nem giữ F05, không biến thành sợi mì/nem chua/roll; phần gắp phải có test riêng.
- Lá sung/đinh lăng cần đúng hình thái, không lá trang trí chung chung. Nhãn prompt không đủ làm bằng chứng; đối chiếu tư liệu actual image khi kiểm output.
- Đồ chấm phân biệt chén tương ớt với canh/đồ uống; không thêm nhãn hàng.
- Bàn có đủ lá/chấm/bát/đũa/cốc, số lượng nhất quán, đường đưa bát/gắp/lấy cốc không xung đột.
- Food set đủ trước integrated frame, rồi kiểm lại khi có hai nhân vật: nhân vật, tỷ lệ đồ vật, mặt/áo, chiều tay và continuity. Không đóng P6 bằng ảnh đẹp duy nhất.

## Tổng hợp và next gate

Đã xác định: texture được owner duyệt và set quán nhỏ đã chốt; có nguồn cho lá/chấm. Quyết định: giữ F05 và script32. Giả định đề xuất: lá sung + ít đinh lăng, hai chén tương ớt riêng, bàn gỗ và nước không nhãn. Còn mở: owner chấp nhận bộ phục vụ; hình lá/portion, style frame và voice/motion. Bước tiếp theo: duyệt bộ phục vụ trên → chuẩn bị/chạy một food-table still với cài đặt/giá kiểm trước submit → QC → mới ghép nhân vật. Chưa chạy ảnh mới trong vòng này.

Các hồ sơ65–70 giữ lịch sử. Approval texture không đồng nghĩa có quyền tác giả được xác minh độc lập; authorization sử dụng input vẫn theo68. Git chỉ docs; ảnh local.
