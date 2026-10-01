# P6 — F-NB-05: sửa texture và framing món

Ngày 2026-10-01. Owner “ok tiếp đi” sau đề xuất sửa ba điểm F04: lát thịt quá lớn, thính thô, crop phần món. Approval thực hiện một lượt sửa; không tự nghiệm thu output hoặc mở ghép nhân vật/video.

Giữ F04 và ảnh thật nguyên vẹn. F05 là một generation mới từ cùng hai ảnh thật đã upload/duyệt ở68, không edit ghi đè F04 và không dùng output AI làm bằng chứng món đúng. Chọn `nembui.jpg` trước, ảnh mẹt sau; hai thành phần hiện trong composer. Vai trò texture/màu chính và cấu trúc hỗ trợ như69.

UI preflight: Hình ảnh / Nano Banana Pro / 9:16 / x1 / 0 tín dụng. Submit đúng một lần; UI0% và đúng prompt. Không xác minh billing ledger. F02 UNRECONCILED và F03 thất bại giữ nguyên.

## Prompt thực chạy

```text
Create one food-only reference image of Nem Bui from Bac Ninh, grounded in the two attached real dish photographs. Use nembui.jpg as the primary texture and color reference and the other photograph to support the loose mixture structure. Show a modest serving made of irregular thin curved strips mixed with small thin flat slices of varied sizes; no oversized broad meat slabs dominating the serving. Match the references with a fine toasted rice powder coating, not coarse crunchy granules or large powder clumps. Preserve natural irregularity and recognizable food texture, not uniform noodles or a smooth solid ball. Place the serving on one plain off-white ceramic plate on a warm ivory tabletop. Pull back to show the entire plate and every part of the food, centered with clear space around all edges, three-quarter overhead view, soft natural light, vertical composition. Only food and plate; no leaves, chilies, surrounding dishes, hands, chopsticks, characters, brands or lettering. Preserve the platform watermark.
```

## Kết quả

GENERATED / DOWNLOADED / PARTIAL_IMPROVEMENT / OWNER_TEXTURE_REVIEW_PENDING. Chạy đúng một lần; không tạo thêm.

Flow asset: https://flow.google.com/u/1/project/9276788e-9781-44fb-ba5b-083006667374/edit/56d529b7-b789-4988-b83d-95b2a00ec347 . Editor có đúng prompt và hai thành phần. Tải từ ảnh editor, không thumbnail.

- Download gốc: `C:\Users\PC\Downloads\b30d706d-5d22-4259-89a0-9272d4e3f56a.jpg`.
- Owner file: `C:\Users\PC\Downloads\du_an_nem_bui\F-NB-05_v0.1.jpg`.
- Project: `media/raw/ep01_p6_food/F-NB-05_v0.1.jpg`.
- JPEG 768×1376; UI9:16 nhưng file không đúng tỉ lệ toán học9:16. SHA256 `C562A77D4A79D6A01E1518191796283810B6E40ADEF814A299B85960099C7E28`.
- UI proof: `media/raw/ep01_p6_food/F-NB-05_flow-proof.png`; SHA256 `EA38096CA1B5FFC1693B99BC556CC5A7B2028A04768FFAE998A722AAF181D20A`.

## Root QC trên ảnh tải thực tế

Đã mở và xem ảnh. So với quan sát hai ảnh thật ở68 và lỗi F04:

- Lát quá lớn: giảm rõ các bản lớn nổi trội so F04; vẫn có vài lát dài, chưa suy kích thước thật hoặc công thức từ ảnh.
- Thính: lớp phủ nhìn mịn/đều hơn F04, vẫn có hạt và cục nhỏ; chưa chứng minh độ mịn vật lý hoặc độ đúng nguyên liệu.
- Framing: toàn bộ phần món nằm trong khung, tập trung giữa hơn; hai mép đĩa trái/phải vẫn crop. Không đạt yêu cầu full plate và clear margin all edges.
- Giữ: hỗn hợp sợi cong và lát nhỏ không đều, màu beige-vàng, đĩa trắng ngà/nền trung tính; không nhân vật/đũa/món phụ/chữ, dấu nền tảng còn góc dưới phải.

Chưa PASS food canon, chưa owner nghiệm thu texture hoặc bố cục. Không dùng output AI tự chứng minh món đúng. Chưa phần món trên đũa hoặc motion proof. Có thể trình duyệt texture riêng; nếu owner nhận texture, lượt sau chỉ sửa camera scale/margin, không tiếp tục đổi cấu trúc món đã chốt.

## Tổng hợp vòng

Đã xác định: output F05 có file/hash/proof, cải thiện texture và tránh crop phần món; full-plate framing chưa đạt. Chốt: một lượt sửa, giữ nguyên F04 và reference. Giả định: đĩa/nền là styling. Còn mở: owner texture review, margin đĩa, phần gắp, style frame, voice/motion. Tiếp theo đề xuất: owner duyệt hoặc góp ý texture F05; sửa framing riêng trước style frame, không tự ghép nhân vật. P6 chưa đóng. Binary local, Git chỉ metadata/docs.
