# P6 — F-NB-04: thử ảnh món dùng reference

Ngày 2026-10-01. Owner: “chạy tiếp đi nào”, sau approval sử dụng hai ảnh ở68. Thực hiện một lượt food-only có hai reference; không ghép nhân vật hoặc voice/video. Không coi owner authorization là giấy phép tác giả được xác minh độc lập.

## Input và preflight

Upload đúng `nembui.jpg` và `z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg` từ folder Downloads đã duyệt; hash/quan sát tại68. Đã thấy upload hoàn tất và gắn hai thành phần vào composer. Vai trò: ảnh thứ nhất texture/màu chính; ảnh mẹt hỗ trợ cấu trúc phần món rời. Không dùng ảnh Minh Vũ.

Flow project 9276788e-9781-44fb-ba5b-083006667374. UI xác nhận Hình ảnh / Nano Banana Pro / 9:16 / x1 / 0 tín dụng trước submit. Đã nhấn Bắt đầu tạo một lần; UI xuất hiện 0% với đúng prompt. Giá UI không xác nhận billing ledger. F03 thất bại và F02 UNRECONCILED không bị ghi đè.

## Prompt thực chạy

```text
Create one food-only reference image of Nem Bui from Bac Ninh using the two attached photos. Use nembui.jpg as the primary reference for the actual dish texture and warm beige-golden color. Use the other photo as a supporting reference for the loose mixture of irregular thin strips and wider flat slices coated with toasted rice powder. Preserve recognizable real food structure rather than converting it into uniform noodles or a smooth solid mass. Present a modest serving on one plain off-white ceramic plate on a warm ivory tabletop, three-quarter overhead close-up, soft natural light. Only the dish and plate; omit surrounding foods, leaves, chilies, packaging, hands, chopsticks, characters, brands and lettering. Vertical composition. Preserve the platform watermark.
```

Đây là request reference-grounded cho chất lượng hình món, không phải khẳng định đã biết nguyên nhân moderation F03 hoặc tìm cách vượt bộ lọc.

## Kết quả

GENERATED / DOWNLOADED / ROOT_QC_REVIEW_REQUIRED / OWNER_OUTPUT_APPROVAL_PENDING. Không retry hoặc tạo thêm.

Flow asset: https://flow.google.com/u/1/project/9276788e-9781-44fb-ba5b-083006667374/edit/4a8875d7-7363-4747-8175-516cbdc66006 . Editor hiển thị output với hai thành phần và đúng prompt; tải từ ảnh editor, không từ thumbnail.

- Download: `C:\Users\PC\Downloads\d1855b80-acd6-4404-8272-b9e84ffed663.jpg`.
- Bản owner: `C:\Users\PC\Downloads\du_an_nem_bui\F-NB-04_v0.1.jpg`.
- Bản project: `media/raw/ep01_p6_food/F-NB-04_v0.1.jpg`.
- JPEG 768×1376 (khung dọc, không đúng tỉ lệ toán học 9:16 dù UI chọn9:16). SHA256 `BB8F290BA6DDF29262879B7E20AB7FA6927690E4F084687825D59AA586D04FEC`.
- UI proof: `media/raw/ep01_p6_food/F-NB-04_flow-proof.png`; SHA256 `D02120C149166979D06EBF665F01C8B81B28CC29399DB14A87FD9532B35E3046`.

## Kiểm ảnh thực tế — root review

Đã mở file tải được và quan sát. Món gồm sợi cong và lát/bản không đều, màu beige-vàng, lớp bột/hạt bám; đĩa trắng ngà, nền trung tính. Không thêm món phụ, lá/ớt, người hoặc chữ; dấu nền tảng còn ở góc dưới phải. Có texture gần ảnh nguồn hơn mô tả toàn sợi, nhưng đây không phải chứng minh mọi nguyên liệu/công thức đúng.

Các hạn chế: vài lát thịt phẳng lớn trở thành điểm nổi bật hơn ảnh nguồn; thính có hạt/cục khá thô so với target lớp bột mịn; đĩa và phần món bị crop mép phải, bố cục lệch và nhiều khoảng trống trên. Chưa cho PASS food canon hoặc bàn giao style frame. Chưa có phần gắp bằng đũa hoặc motion proof. Hai nguồn thật được dùng để đối chiếu, không lấy output AI khác làm bằng chứng món đúng.

## Tổng hợp và bước tiếp theo

Đã xác định: upload hai ảnh thành công, generation một lượt thành công, tải được output và lưu hash. Chốt: chỉ hai ảnh đã duyệt được dùng input. Giả định: đĩa/nền là styling của project. Còn mở: owner đánh giá texture, sửa tỉ lệ lát/thính và bố cục, phần gắp, style frame, voice/motion. Đề xuất lượt sửa riêng: giữ reference, giảm các lát lớn/hạt thính thô, đưa toàn bộ phần món vào khung; chưa thực hiện trong lượt này. Không tự coi lệnh chạy là owner nghiệm thu output. P6 chưa đóng.

Binary lưu local, Git chỉ hồ sơ metadata và hash.
