# P6 — Ảnh món local và approval sử dụng

Ngày: 2026-10-01. Owner yêu cầu tải ảnh tham khảo xuống `C:\Users\PC\Downloads\du_an_nem_bui` và duyệt hai file dưới đây, xác nhận “có thể sử dụng”. Đây là owner authorization cho tham chiếu hình món trong project, có thể chuẩn bị input Flow. Không ghi thành xác minh độc lập giấy phép của tác giả; không tự phê duyệt một request generation mới hoặc đầu ra.

## Hai file đã duyệt

1. `C:\Users\PC\Downloads\du_an_nem_bui\nembui.jpg`
   - Đã tồn tại trước lượt này; giữ nguyên, đã xem trực tiếp.
   - JPEG 1920×1367, 492138 bytes.
   - SHA256 `A51303F7100EDD0944DC00DAA19402FECFE24BB0E15A4143DA8F8EAE7B9E3A2D`.
   - Hash trùng bản tải FV03a từ cổng du lịch. Món trên đĩa trắng, sợi và lát/bản không đều, thính vàng; lá và ớt xung quanh.
   - Vai trò: tham chiếu texture và màu chính; bố cục lá/ớt không tự trở thành bắt buộc.
2. `C:\Users\PC\Downloads\du_an_nem_bui\z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg`
   - Đã tồn tại trước lượt này; giữ nguyên, đã xem trực tiếp.
   - JPEG 980×739, 227642 bytes.
   - SHA256 `1237956E99458385F95F1EDF18E0A98E1BDDB777030AC1D69FAB05FA7A51D741`.
   - Bài cổng du lịch liên kết đúng filename này: https://mybacninh.vn/vi/detailnews/?id=news_3068&t=nem-bui-mon-an-dan-da-dam-hon-que-kinh-bac . File nguồn: https://media.mybacgiang.vn/resources/portal/Images/BGG/admin.dulich/2026/z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg . Chưa so hash file remote với local; chỉ xác minh liên kết và xem file local.
   - Quan sát: nem rời trên mẹt có lá, nhìn thấy sợi và mảnh/lát phủ thính; các món khác nằm ngoài mẹt. Vai trò: tham chiếu hình dạng phần món rời, không kéo các món khác vào episode.

Hai ảnh này là OWNER_APPROVED_REFERENCE / OWNER_AUTHORIZED_USE, không phải food asset generated hoặc master clip đã nghiệm thu. Không tự suy mọi variant món giống hệt ảnh.

## Đã tải thêm các ảnh tham khảo của shortlist67

Folder đích như owner yêu cầu; không ghi đè file có sẵn:

| File | Kích thước | SHA256 | Trạng thái |
|---|---|---|---|
| FV03a_nem_bui_tren_dia.jpg | 1920×1367 | A51303F7100EDD0944DC00DAA19402FECFE24BB0E15A4143DA8F8EAE7B9E3A2D | Bản tải trùng nembui.jpg; chỉ dùng tên đã duyệt làm input chính |
| FV04a_MinhVu_nem_mo_goi.jpg | 2560×1440 | C01E157230D47901DE524427935C3B907A956962F21A72A04DD75E8108C6CA43 | Research-only, chưa duyệt sử dụng |
| FV04b_MinhVu_nem_goi_la.jpg | 2560×1440 | 212DF216C7CF428F5FCD26E7C463EC9ADBC63884D3BD5CDB5502CF719365601B | Research-only, chưa duyệt sử dụng |

URL nguồn và credit từng file xem67. Đã kiểm decode bằng System.Drawing và hash cả năm file. “Tải hết” trong lượt này được thực hiện với ba ảnh đã xem và liệt kê trong shortlist67; không crawl toàn website hoặc tải ảnh VnExpress bị 403. Không xóa bản trùng để giữ nguyên dữ liệu owner.

## Tổng hợp vòng

- Đã xác định: hai file owner chỉ định tồn tại, đọc được và đã xem; ba ảnh tham khảo tải thành công.
- Chốt: dùng đúng hai file có hash ở trên làm tham chiếu được owner duyệt.
- Giả định: ảnh tham chiếu phục vụ texture/phần món, không sao chép nguyên bố cục hoặc món phụ.
- Còn mở: phần món trên đũa, request ảnh dùng reference, kiểm output, style frame và voice/motion.
- Tiếp theo: chuẩn bị request có vai trò rõ cho hai reference; kiểm điều kiện upload/cài đặt/giá và phê duyệt request trước khi tạo. Chưa upload hoặc generation trong lượt tải này. F03 thất bại và F02 chưa đối soát vẫn giữ nguyên.

Binary nằm trong Downloads, không push lên Git; chỉ metadata và quyết định được commit.
