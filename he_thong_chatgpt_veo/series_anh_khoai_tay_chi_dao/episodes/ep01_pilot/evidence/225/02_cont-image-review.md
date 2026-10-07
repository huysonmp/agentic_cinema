# REC225-CONT — Kiểm tra độc lập ảnh tĩnh và liên tục bàn ăn

Ngày: 2026-10-07. Vai trò: CONT/FOOD, kiểm tra đầu ra Flow do root tạo. Phạm vi: ba ảnh v02, ba ảnh nguồn v01 tương ứng và khung B `frame-0175.jpg` đã duyệt. Kết luận này được lập trước khi đọc bất kỳ báo cáo của reviewer khác hoặc kết luận QC của root.

**Kết quả: 2/3 ảnh đạt yêu cầu sửa ở mức ảnh tĩnh; REF01-M_v02 không đạt. Lỗi sửa tay M chưa đóng.** E và R03 có thể trình owner xem xét; đây không phải sự chấp nhận đầu ra của owner hoặc phê duyệt toàn bộ G1.

## Năng lực và bằng chứng thực tế

Đã đọc đầy đủ `225/owner-approval.json`, `225/native-output-manifest.json`, `224/repair-request-DRAFT.json` và ba tệp prompt sửa chính xác tại 224. Đã mở bằng `view_image(detail="original")` cả ba ảnh tải xuống v02 nguyên gốc, cả ba ảnh nguồn v01 nguyên gốc và khung B tại `C:/Users/PC/Downloads/du_an_nem_bui/223_g1_source_frames/ANCHOR_B/frame-0175.jpg`. Không dùng thumbnail hoặc bảng ghép để thay cho ảnh gốc.

Năng lực thực tế của lượt này là xem ảnh tĩnh và đối chiếu tệp tại máy. Không truy cập trình duyệt; không tạo ảnh thay thế, video hoặc giọng; không chi tiêu; không thao tác Git. Không kiểm tra chuyển động, lời nói, đồng bộ môi, âm thanh hoặc toàn bộ AV. Ảnh không đủ để xác nhận nhiệt độ hay thành phần món ăn ngoài biểu hiện nhìn thấy.

Đã tính lại SHA-256 cho 21 tệp: nguồn v01, ảnh tải xuống v02, bản owner, bản repo, prompt, preflight và result của từng ID. Cả 21/21 khớp trường tương ứng trong manifest; cả 6/6 hash nguồn/prompt khớp request đã duyệt. Ba bản v02 của mỗi ID trùng hash. Đã xác nhận kích thước ba ảnh v02 bằng bộ đọc ảnh: JPEG, 768 × 1376, đúng kích thước manifest; đây là canvas native quan sát được, không phải 9:16 chính xác theo phép chia kích thước.

## Kỳ vọng và quan sát theo ID

| ID | Kỳ vọng được phép sửa | Quan sát trên v02 so với v01 | Mức độ | Disposition / closure |
| --- | --- | --- | --- | --- |
| REF01-M_v02 | Chỉ đổi tay/cánh tay đang vươn của Đào; đầu ngón tay ở ngoài mép phải đĩa nhìn thấy rõ, phía gần Đào; có khoảng hở; không trên ụ nem, không phía sau đĩa, không giao bát. Hai môi khép; các tay khác giữ vị trí. | Tay vẫn nằm phía sau đĩa ở vùng gần giữa khung hình, cạnh đỉnh ụ nem; đầu ngón tay không được đưa ra ngoài cung mép phải gần Đào. Không thấy khoảng hở rõ giữa đầu ngón tay và đường bao món/đĩa tại vùng này. Tư thế tay đọc gần như cùng vị trí v01; hash khác không chứng minh sửa đúng. Không thấy tay giao bát cá nhân; hai môi vẫn khép, tay còn lại của Đào và hai tay Khoai nghỉ trên bàn. | BLOCKER — mục tiêu chính của sửa M không đạt. | **FAIL_IMAGE_REPAIR; OPEN.** Giữ làm bằng chứng đầu ra, không đánh dấu sửa xong hoặc đưa vào tập ảnh đã chấp nhận. Không tự tạo lại vì retry chưa được cấp quyền. |
| REF01-E_v02 | Khép môi cả hai: Khoai cười nhỏ, Đào trung tính thư giãn; giữ mắt, góc đầu, tay, nhân dạng, bàn ăn và nền. | Miệng Khoai đã thành nụ cười khép nhỏ; Đào khép môi, biểu cảm gần trung tính. Không còn khoang miệng tối mở như v01, không thấy răng/lưỡi. Hướng nhìn, góc đầu, tay nghỉ và bố cục giữ như nguồn; không phát hiện drift có ý nghĩa ngoài vùng miệng. | Không có lỗi chặn quan sát được. | **PASS_IMAGE_REPAIR; CLOSED_AT_IMAGE_QC.** Đủ để trình owner; owner acceptance vẫn mở. |
| REF03-S_v02 | Chỉ khép môi Đào; giữ tò mò nhẹ trong mắt và hướng nhìn Khoai; nụ cười riêng của Khoai giữ nguyên. | Môi Đào đã khép thành đường nhỏ, không thấy khoang miệng tối/răng/lưỡi. Đào vẫn nhìn Khoai với mắt tò mò; góc đầu giữ. Khoai vẫn có nụ cười khép kín riêng và mắt hướng Đào. Không phát hiện tái dàn dựng hoặc đổi tay/bàn ăn. | Không có lỗi chặn quan sát được. | **PASS_IMAGE_REPAIR; CLOSED_AT_IMAGE_QC.** Đủ để trình owner; owner acceptance vẫn mở. |

Vị trí lỗi M có thể kiểm tra trực tiếp trên canvas 768 × 1376: đầu ngón tay ở khoảng x=400–440, y=990–1020, phía xa/sau đĩa; cung mép phải nhìn thấy nằm về phía x≈620–650. Đây là tọa độ ước lượng thị giác để định vị vấn đề, không phải phép đo tiếp xúc hoặc khoảng cách 3D. Chưa thể kết luận ngón tay chạm đồ ăn; có thể kết luận rõ rằng tiêu chí ngoài mép phải và khoảng hở chưa được đáp ứng.

## Kiểm tra liên tục và thay đổi ngoài ý muốn

| Hạng mục | REF01-M_v02 | REF01-E_v02 | REF03-S_v02 |
| --- | --- | --- | --- |
| Nhân dạng, khuôn mặt, trái/phải | Khoai bên trái, Đào bên phải; đặc trưng mặt giữ nguồn. | Giữ nhân dạng, tỷ lệ mặt và trái/phải; sửa môi trong phạm vi. | Giữ nhân dạng, tỷ lệ mặt và trái/phải; nụ cười Khoai giữ. |
| Quần áo và nơ hồng | Khoai áo khoác tối/áo sơ mi sáng; Đào áo sáng, váy xanh, nơ hồng ở eo giữ. | Như nguồn v01. | Như nguồn v01. |
| Ánh sáng, nền, khung hình | Phố/quán với đèn lồng ấm, chiều sâu nền, vị trí nhân vật và khung hình giữ; không thấy đổi cảnh. | Như nguồn v01. | Như nguồn v01. |
| Nem Bùi và bàn | Cùng ụ sợi nhạt trên đĩa chung, cùng bàn gỗ và vị trí đĩa; không thấy bị nhấc, cầm, thêm món hoặc hơi nước/khói. | Như nguồn v01. | Như nguồn v01. |
| Rau phía trước bên trái | Đĩa rau lá vẫn ở trước bên trái khung hình. | Giữ. | Giữ. |
| Hai chén chấm | Một chén bên trái đĩa chung, một chén phía trước bên phải; giữ số lượng/vị trí và màu đỏ trong chén. | Giữ. | Giữ. |
| Hai bát cá nhân rỗng | Hai bát nhìn thấy lòng rỗng, đặt trước mỗi nhân vật. | Giữ. | Giữ. |
| Hai đôi đũa nghỉ | Đôi trái cạnh bát Khoai, đôi phải cạnh bát Đào; không cầm đũa. | Giữ. | Giữ. |
| Ly nước phía ngoài Đào | Ly ở rìa phải, phía ngoài Đào; không cầm/uống. | Giữ. | Giữ. |
| Watermark/chữ mới | Watermark native ở dưới phải giữ; không thấy chữ hoặc panel mới. | Giữ; không thấy chữ/panel mới. | Dấu native dưới phải có hình chồng đã có ở v01; vẫn giữ, không ghi nhận là drift mới. |

Không phát hiện thay đổi ngoài ý muốn đáng kể ở các hạng mục trên khi so từng cặp v01–v02. “Giữ” ở đây là đánh giá nội dung nhìn thấy tại độ phân giải native; không phải chứng nhận pixel-identical giữa nguồn và ảnh đã sửa.

Khung B `frame-0175.jpg` xác nhận bộ nhận dạng nhìn thấy: Khoai trái/Đào phải, trang phục, nơ hồng, bàn gỗ, Nem Bùi giữa bàn, rau trước trái, hai chén chấm, hai bát, hai đôi đũa nghỉ và ly phía ngoài Đào. Các ảnh v01/v02 có khung gần hơn và trạng thái biểu cảm khác B; đối chiếu B dùng để kiểm tra nhận dạng và bố trí liên tục, không coi mọi khác biệt với khung B là lỗi sửa v02. Không thấy đảo trái/phải hoặc thay bộ đồ/bộ bàn ăn so với B.

## Dấu vết hash

Hash v02 trong bảng áp dụng đồng thời cho ảnh tải xuống nguyên gốc, bản owner tại `Downloads/du_an_nem_bui/225_g1_repaired_refs_v02/` và bản repo tại `media/225_g1_repaired_refs_v02/`. Hash prompt áp dụng cho ba tệp `224/*.repair-v02-DRAFT.txt`; preflight/result là tệp cùng ID tại 225, đúng đường dẫn manifest.

| ID | Nhóm tệp | SHA-256 tính lại | Đối chiếu |
| --- | --- | --- | --- |
| M | Nguồn v01 | `bd48acb3223c417a22918a9d717cb0e1f5f22e118b8584fd2609581f3460f037` | Manifest + request: khớp |
| M | V02 original / owner / repo | `754f773fb68c9ca824fe9379890694fc98241457542a2f817c0624aa5ed82a23` | Cả ba khớp manifest |
| M | Prompt | `e57b3a0779b666227d90790498a3eae9fd60fdbac31350feec412922d19b6ca6` | Manifest + request: khớp |
| M | Preflight | `cb4ca62041f7458a167c417bc35064e390002172c4c1eeb7b767025301082293` | Khớp manifest |
| M | Result | `ef0cfdf6ec61e8cff97f74aa78af88ef25bd0e553577c7174e4050b36770e68e` | Khớp manifest |
| E | Nguồn v01 | `887f00f0f78ea093529825b108b16d04a63c541b2b637281c7ebb4a52782c6c4` | Manifest + request: khớp |
| E | V02 original / owner / repo | `8df19973fa6595cd166cab67b08a2009256091fb05bf14be322b1371308dbc03` | Cả ba khớp manifest |
| E | Prompt | `1eba7b7a9fb9b9e0bcb7ab0da44439fbe997eb2733b01e5defe3685f15fedac9` | Manifest + request: khớp |
| E | Preflight | `6a6dd13bb0c87164f8f2fdac5ca4d74eac69a902e0a5c190eec7209c3f24b385` | Khớp manifest |
| E | Result | `2b283bad94854e5ad8ad417fcdc1f3972dce877dff2ad5c76f72b087bb4ceac3` | Khớp manifest |
| R03 | Nguồn v01 | `4a4c4a9ae0dcd017b44a3e7b59b775577cbe7184594994f674526b93f915962e` | Manifest + request: khớp |
| R03 | V02 original / owner / repo | `a4dba6829a76d430611e9fda3275342c7d07393673bb140dde6338cb99bdc99e` | Cả ba khớp manifest |
| R03 | Prompt | `6da403e56c1f2c7d2777a25e26af1203b459afa489d86661f00f20de0fe34ccd` | Manifest + request: khớp |
| R03 | Preflight | `fa3e56959790890786dbbde3f01733c36c1520fd7d25d64a47f50e6aa95e0db0` | Khớp manifest |
| R03 | Result | `cb7d163513b0b699de4f57766820a029ea6b096764939c975eb0ff8a2918ec3c` | Khớp manifest |

Các hash tài liệu nền tính lại để định danh lượt kiểm tra; không có hash chuẩn độc lập trong request cho bốn tệp dưới đây:

- `225/owner-approval.json`: `00b7e8e8cc417627463651556fcafc1d560f337d2f2f142ec45b0b054750b82f`.
- `225/native-output-manifest.json`: `2a2663a38fc82397591e23588fa71855c70cbdd4621e5f4e6b3d91a3ede916d9`.
- `224/repair-request-DRAFT.json`: `6e8ff1c0a9358334bf0181676a68cb0c4002dafdf6425ddf1a8bbc7490d265fe`.
- B `frame-0175.jpg`: `5bec51d789cebc8b891b26c70d4c52a4a2185ed18b34d0fb933ab6e1cab8c6c5`.

## Đóng lượt review

Lượt CONT/FOOD độc lập đã hoàn thành trong phạm vi ảnh tĩnh và xác minh tệp. Hai lỗi khép môi E/R03 đóng ở mức QC ảnh; lỗi định vị tay M còn mở và chặn kết luận bộ sửa ba ảnh hoàn tất. Không có sự chấp nhận đầu ra tự động của owner, không cấp quyền retry, không phê duyệt chuyển động/giọng/đồng bộ môi/full AV/full G1 hoặc phát hành. Bước tiếp theo là root tổng hợp review độc lập và trình owner quyết định đối với lỗi M còn mở; reviewer không tạo đầu ra mới.
