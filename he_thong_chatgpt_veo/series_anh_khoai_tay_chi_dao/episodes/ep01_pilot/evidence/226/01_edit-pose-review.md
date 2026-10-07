# REC226-EDIT — Đánh giá độc lập tư thế REF01-M_v03

Ngày đánh giá: 2026-10-07. Phạm vi: ảnh tĩnh và xác minh hash. Đã đọc đầy đủ `226/owner-approval.json`, `226/native-output-manifest.json` và prompt `225/REF01-M.repair-v03-DRAFT.txt`. Không đọc review root hoặc CONT trước khi kết luận.

## Kết luận

**REF01-M_v03_REC226: USABLE CANDIDATE cho tư thế ảnh tĩnh.** Tay phía ngoài của Đào, bên phải màn hình và phía ly nước, đã với xuống và vào trong, gần phía phải của vành đĩa nem. Các đầu ngón tay thấp hơn đỉnh món; không còn nằm sau đống nem. Có khoảng hở nhìn thấy giữa đầu ngón tay thấp nhất và vành gốm gần đó. Ý định đưa tay đến đĩa đọc được, chưa có tư thế cầm hoặc nhấc đĩa.

Không thấy lỗi MAJOR về tư thế trong phạm vi ảnh đã xem. Có một điểm **MINOR / cần theo dõi**: cẳng tay và bàn tay che một phần mép trước-phải của bát Đào trong hình chiếu. Các đường viền vẫn đọc thành hai vật riêng, không thấy nhập hình hoặc xuyên bát rõ ràng. Ảnh tĩnh không đủ xác nhận khoảng cách theo chiều sâu; không suy che khuất thành va chạm.

Kết luận này không phải owner acceptance, full G1 pass, xác nhận chuyển động hoặc âm thanh; không cấp quyền retry/generate.

## Ảnh đã xem và hash

Đã dùng `view_image` với `detail: original` để xem toàn ảnh:

- SOURCE S: `C:/Users/PC/Downloads/du_an_nem_bui/224_g1_opening_refs_v01/REF01-S_v01_NATIVE.jpg`.
- M_v03 tải gốc: `C:/Users/PC/Downloads/REF01-S_v01_REC224_20261007103419.jpg`.
- E_v02 để xét S–M–E: `C:/Users/PC/Downloads/du_an_nem_bui/225_g1_repaired_refs_v02/REF01-E_v02_NATIVE.jpg`.

Tên download gốc vẫn chứa S_v01 theo manifest, nhưng ảnh xem là đầu ra M_v03. Xác minh theo hash và manifest, không suy ID từ tên download. Manifest xác định source Flow image `22a0d77a-c8db-4a62-82ef-9ed93d34e7f2`, output Flow image `944bb01f-da47-4b68-8281-2aa5c04c546a` trong cùng container `558dc41c-45d2-437d-bcbf-e044ece386d7`.

Tính lại SHA-256: **5/5 kiểm tra REC226 khớp** source, prompt và ba bản đầu ra. Source hash cũng khớp owner approval. E_v02 được kiểm tra thêm với manifest REC225: **khớp**.

| Đối tượng | SHA-256 | Kết quả |
| --- | --- | --- |
| SOURCE REF01-S_v01 | `eba9a13c86f359df458022a5a54664264e5bb29fcca08d6181454cb1ee482422` | Khớp manifest REC226 và owner approval |
| Prompt sửa v03 | `ef802f99ccc590e70b63c0e36cd9cee1c9cfd11962020bdb04bd11c89547a26d` | Khớp manifest REC226 |
| M_v03 download original | `66defd18afc0845da8b34968446b98f547dcad951e6712e2e6a81ff2d5e2017c` | Khớp manifest REC226 |
| M_v03 owner native | `66defd18afc0845da8b34968446b98f547dcad951e6712e2e6a81ff2d5e2017c` | Khớp download original |
| M_v03 repo native | `66defd18afc0845da8b34968446b98f547dcad951e6712e2e6a81ff2d5e2017c` | Khớp download original |
| E_v02 owner native | `8df19973fa6595cd166cab67b08a2009256091fb05bf14be322b1371308dbc03` | Khớp manifest REC225 |

## Expected / observed theo exact ID

ID mục tiêu: `REF01-M_v03_REC226`; tên bản native: `REF01-M_v03_NATIVE.jpg`. Các mô tả dưới đây là quan sát ảnh, không phải chứng minh hình học 3D.

| Tiêu chí | Expected | Observed | Mức độ / kết luận |
| --- | --- | --- | --- |
| Đúng cánh tay | Chỉ đổi tay phía ngoài Đào ở bên phải màn hình, gần ly; tay phía trong gần Khoai vẫn nghỉ | Tay bên phải màn hình với xuống; tay bên trái thân Đào vẫn nghỉ sát bên bát. Hai tay Khoai vẫn nghỉ | NONE — đạt |
| Đích đến | Đầu ngón tay gần bên phải vành gốm nhìn rõ, hướng xuống và hơi vào trong | Bàn tay hiện ở phía phải món nem, gần cung trên-phải của vành đĩa. Đầu ngón tay thấp nhất ở ngay trên và ngoài cung vành này | NONE — đạt mục tiêu tư thế |
| Khoảng hở | Khoảng không nhỏ giữa đầu ngón tay và vành gốm phải nhìn rõ | Có dải nền bàn nhìn thấy giữa đầu ngón tay thấp nhất và vành gốm. Khoảng hở đọc được ở ảnh native; không thấy bàn tay đặt lên hoặc nắm vành | NONE — đạt; đây là khoảng hở trong hình chiếu |
| Độ cao / tránh phía sau món | Đầu ngón tay thấp hơn đỉnh món, không sau đống nem hoặc trên thức ăn | Đầu ngón tay thấp hơn đỉnh đống nem, nằm bên phải và ngoài đường biên món; không bị đống nem che như tư thế lỗi trước | NONE — đạt |
| Tiếp xúc thức ăn và cầm đồ | Không chạm, gắp hoặc cầm thức ăn/đĩa; đĩa không nhấc | Không thấy đầu ngón tay chạm đường biên thức ăn. Bàn tay rỗng, chưa tạo thế nắm; đĩa vẫn nằm trên bàn | NONE theo quan sát ảnh |
| Tay và cổ tay | Khuỷu tay, cổ tay, ngón cong tự nhiên; không tay thừa | Cánh tay nối từ tay áo tới cổ tay và bàn tay theo đường liên tục; cổ tay mềm, các ngón hơi cong. Không thấy tay thừa hoặc khớp gãy rõ | NONE — usable |
| Bát cá nhân | Đi quanh phía ngoài bát, không xuyên hoặc nhập hình | Cẳng tay/bàn tay che một phần mép trước-phải bát trong hình chiếu. Đường viền bàn tay và bát vẫn tách được; không thấy bát bị kéo méo hoặc tay nhập vào gốm | MINOR — lưu ý che khuất; khoảng cách 3D UNKNOWN, chưa có bằng chứng va chạm |
| Đũa, ly, chén chấm | Không giao cắt hoặc nhập hình; không cầm các vật này | Bàn tay ở phía trong cặp đũa bên phải, phía trái ly và phía trên chén chấm phải. Không thấy nhập hình với đũa, ly hoặc chén chấm; đũa vẫn nằm trên bàn | NONE — đạt trong ảnh |
| Miệng và ánh nhìn | Hai miệng khép, giữ gaze nguồn | Hai miệng khép; Khoai nhìn về Đào và Đào nhìn về Khoai như S nguồn | NONE — đạt |
| Nhân vật và bố trí bữa ăn | Giữ mặt, quần áo, nơ eo, khung hình, bối cảnh và đồ vật | Nhận diện, nơ eo, ánh sáng và bố trí bàn tương ứng S. Thay đổi rõ nằm ở tay ngoài và tay áo liên quan. Không thấy đĩa hoặc các vật trên bàn được chuyển vị trí đáng kể | NONE trong so sánh thị giác; không tuyên bố pixel-identical |

## Khả năng nối S–M–E

`REF01-S_v01 → REF01-M_v03 → REF01-E_v02` có cơ sở để dùng làm ba trạng thái ảnh tham chiếu. S và M giữ biểu cảm, gaze và bố trí bàn tương ứng; thay đổi tay ngoài của Đào tạo một ý định với tới đĩa có đích rõ. M và E phân biệt được trạng thái với tay với trạng thái tay nghỉ, trong khi bữa ăn vẫn ở bố trí tương ứng. E có Khoai cười nhẹ hơn S/M và Đào trung tính hơn; đây là khác biệt biểu cảm nhìn thấy, không phải lỗi miệng mở.

Ảnh tĩnh chỉ cho thấy các trạng thái. Chưa xác nhận đường đi của tay qua bát/đũa, động tác thu tay, nhịp dừng, tính liên tục theo thời gian, speech-end hoặc giọng nói thực tế. Gaze vẫn hướng vào nhau trong M, nên ý định lấy đĩa được truyền qua bàn tay; không suy nhân vật đã nhìn xuống món.

## Điều đã xác định và vấn đề còn mở

Đã xác định: đúng source S và đúng prompt theo hash; ba bản M_v03 đồng nhất; tư thế tay ngoài đến gần vành đĩa phải với gap nhìn rõ; miệng khép và trạng thái bàn tay còn lại được giữ. Quyết định reviewer: **USABLE CANDIDATE, không có lỗi MAJOR phát hiện trong phạm vi EDIT/pose ảnh tĩnh**.

Giả định làm việc: các ảnh S/M/E là các trạng thái tham chiếu có thể đề xuất nối, không phải bằng chứng đã quay hành động. Vấn đề còn mở: khoảng cách 3D giữa tay và bát ở phần bị che; chuyển động và AV; owner output acceptance. Bước tiếp theo: root tổng hợp review độc lập và trình candidate cùng giới hạn quan sát cho owner, theo thẩm quyền hiện có.

Không dùng Flow, tạo lại ảnh, tạo video/voice, chi tiêu hoặc Git trong lượt review này.
