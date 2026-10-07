# REC225-EDIT — Đánh giá độc lập tư thế và độ rõ của câu chuyện

Ngày đánh giá: 2026-10-07. Phạm vi: ảnh tĩnh, sửa tư thế/miệng và khả năng nối các trạng thái tham chiếu. Đã đọc đầy đủ `225/owner-approval.json`, `225/native-output-manifest.json`, `224/repair-request-DRAFT.json` và cả ba prompt sửa được dẫn trong manifest. Không đọc kết quả của reviewer khác trước khi chốt đánh giá này.

## Kết luận

- `REF01-M_v02`: **HOLD / REWORK — MAJOR**. Chưa đạt mục tiêu sửa vị trí bàn tay. Đầu ngón tay vẫn nằm tại mép sau của đống nem, gần giữa khung hình; chưa tiến tới vành đĩa nhìn rõ ở phía phải màn hình, phía gần Đào, với một khoảng hở nhìn thấy được.
- `REF01-E_v02`: **USABLE CANDIDATE** trong phạm vi ảnh tĩnh. Cả hai miệng khép; ánh nhìn, góc đầu và bàn tay nghỉ được giữ ở mức quan sát trực tiếp.
- `REF03-S_v02`: **USABLE CANDIDATE** trong phạm vi ảnh tĩnh. Miệng Đào khép; nụ cười nhỏ, kín miệng của Khoai được giữ.
- `REF01-S_v01` tiếp tục là candidate được giữ nguyên. Chuỗi `S → M → E → B → R03` **HOLD** vì trạng thái M chưa làm rõ ý định đưa tay đến vành đĩa. Hai candidate sửa miệng không đủ để gỡ điểm chặn này.

`USABLE CANDIDATE` chỉ là ý kiến chuyên môn cho ảnh tham chiếu. Không đồng nghĩa với owner acceptance, phê duyệt full G1, chất lượng chuyển động hay âm thanh.

## Bằng chứng đã xem và đối chiếu hash

Đã xem bằng `view_image` ở chế độ `original` cả ba ảnh nguồn v01 và ba ảnh v02 tải gốc, cùng `REF01-S_v01_NATIVE.jpg` và `ANCHOR_B/frame-0175.jpg`. Ba ảnh v02 có kích thước native 768 × 1376 theo manifest; B được xem ở kích thước nguồn 360 × 640. Không tạo crop, ảnh mới hoặc nội dung media mới.

Đường dẫn ảnh nguồn: `C:/Users/PC/Downloads/du_an_nem_bui/224_g1_opening_refs_v01/`. Đường dẫn ảnh giữ S: `C:/Users/PC/Downloads/du_an_nem_bui/224_g1_opening_refs_v01/REF01-S_v01_NATIVE.jpg`. B: `C:/Users/PC/Downloads/du_an_nem_bui/223_g1_source_frames/ANCHOR_B/frame-0175.jpg`.

Đã tính lại SHA-256 cho từng source, prompt, download original, owner native copy và repo native copy: **15/15 khớp manifest**. Hash nguồn/prompt trong manifest cũng khớp các giá trị đã khóa trong request REC224. Ba bản của mỗi đầu ra có cùng hash; không nhầm ảnh giữa các ID.

| ID | Source SHA-256 | Prompt SHA-256 | V02 SHA-256 — cả ba bản khớp |
| --- | --- | --- | --- |
| REF01-M_v02 | `bd48acb3223c417a22918a9d717cb0e1f5f22e118b8584fd2609581f3460f037` | `e57b3a0779b666227d90790498a3eae9fd60fdbac31350feec412922d19b6ca6` | `754f773fb68c9ca824fe9379890694fc98241457542a2f817c0624aa5ed82a23` |
| REF01-E_v02 | `887f00f0f78ea093529825b108b16d04a63c541b2b637281c7ebb4a52782c6c4` | `1eba7b7a9fb9b9e0bcb7ab0da44439fbe997eb2733b01e5defe3685f15fedac9` | `8df19973fa6595cd166cab67b08a2009256091fb05bf14be322b1371308dbc03` |
| REF03-S_v02 | `4a4c4a9ae0dcd017b44a3e7b59b775577cbe7184594994f674526b93f915962e` | `6da403e56c1f2c7d2777a25e26af1203b459afa489d86661f00f20de0fe34ccd` | `a4dba6829a76d430611e9fda3275342c7d07393673bb140dde6338cb99bdc99e` |

Hash bổ sung tính trong lượt đánh giá này, chỉ dùng nhận diện ảnh đã xem, không có expected hash trong manifest REC225:

- `REF01-S_v01_NATIVE.jpg`: `eba9a13c86f359df458022a5a54664264e5bb29fcca08d6181454cb1ee482422`.
- `ANCHOR_B/frame-0175.jpg`: `5bec51d789cebc8b891b26c70d4c52a4a2185ed18b34d0fb933ab6e1cab8c6c5`.

## Đánh giá expected / observed theo exact ID

Quy ước mức độ: MAJOR = chặn việc dùng ảnh cho đúng vai trò đã yêu cầu; NONE = chưa thấy lỗi trong tiêu chí đang xét. UNKNOWN = ảnh không cung cấp đủ bằng chứng, không tự suy thành PASS hoặc FAIL.

### REF01-M_v02

Nguồn đối chiếu: `REF01-M_v01_NATIVE.jpg`. Đầu ra xem trực tiếp: `C:/Users/PC/Downloads/REF01-M_v02_REC225_20261007095224.jpg`.

| Tiêu chí | Expected | Observed | Mức độ |
| --- | --- | --- | --- |
| Đích đến của đầu ngón tay | Ngay ngoài vành gốm nhìn rõ bên phải màn hình, phía gần Đào; không ở trên đống nem hoặc phía sau đĩa | Bàn tay với xuống vẫn gần trung tâm khung hình, phía sau mép trên của đống nem. Vành đĩa phải nhìn rõ nằm xa hơn về bên phải và thấp hơn. Tư thế này không cho thấy sửa vị trí như yêu cầu | MAJOR |
| Khoảng hở ngón tay–vành đĩa | Có khoảng hở nhỏ nhìn thấy được, đủ đọc là ý định lấy đĩa | Chưa có cặp ngón tay–vành gốm mục tiêu cùng nhìn rõ để chứng minh khoảng hở. Đống nem che khu vực dưới đầu ngón tay | MAJOR |
| Tiếp xúc với thức ăn | Không chạm thức ăn | Không thể xác nhận tại phần bị che. Không khẳng định đã chạm thức ăn; lỗi xác định được là vị trí và độ rõ của tư thế | UNKNOWN |
| Cổ tay và ngón tay | Cổ tay thả lỏng, ngón cong tự nhiên | Cánh tay và cổ tay nối tương đối tự nhiên, không thấy tay thừa. Nhưng đầu ngón tay thả xuống tại mép sau đống nem làm ý định lấy vành đĩa khó đọc | MAJOR cho độ rõ hành động; không thấy lỗi giải phẫu độc lập rõ ràng |
| Tránh bát cá nhân | Cánh tay không cắt qua bát của Đào | Cánh tay đi về phía trái bát của Đào trên màn hình; không thấy giao cắt bát | NONE |
| Miệng, ánh nhìn, tay còn lại | Hai miệng khép; ánh nhìn và các tay khác giữ nguyên | Cả hai miệng đọc là khép, hai nhân vật nhìn về nhau. Tay còn lại của Đào và hai tay Khoai ở vị trí nghỉ như nguồn | NONE |
| Đồ vật đang cầm hoặc nhấc | Không cầm, nhấc hay thêm đồ vật | Không thấy đồ vật trong tay. Đĩa vẫn nằm trên bàn; bát, đũa và ly ở vị trí tương ứng nguồn | NONE |

**Quyết định: HOLD / REWORK.** V01 và V02 có hash khác nhau nhưng quan sát toàn ảnh không cho thấy bàn tay đã chuyển đến mục tiêu sửa. Không dùng sự khác nhau của hash làm bằng chứng edit đạt. Không tự tạo prompt mới hoặc thực hiện retry từ kết luận này.

### REF01-E_v02

Nguồn đối chiếu: `REF01-E_v01_NATIVE.jpg`. Đầu ra xem trực tiếp: `C:/Users/PC/Downloads/REF01-E_v02_REC225_20261007095244.jpg`.

| Tiêu chí | Expected | Observed | Mức độ |
| --- | --- | --- | --- |
| Miệng Khoai | Hai môi gặp nhau, cười nhỏ kín miệng; không khe mở, răng hoặc lưỡi | Khe tối rõ của v01 đã biến mất. V02 có đường môi khép và nụ cười nhẹ; không thấy răng hoặc lưỡi | NONE |
| Miệng Đào | Hai môi khép, biểu cảm trung tính thư giãn | V02 có đường môi khép, không thấy khoang miệng. Một đường viền môi tối mảnh là đường phân cách môi, không đọc thành khe mở như v01 | NONE |
| Ánh nhìn và góc đầu | Giữ chú ý bình tĩnh hướng về nhau | Hướng mắt về nhân vật đối diện và góc đầu còn tương ứng nguồn; không tái bố trí tư thế | NONE |
| Tay và trạng thái nghỉ | Tất cả tay ở trên bàn tại vị trí nguồn | Tay Đào nằm hai bên bát; tay Khoai cạnh bát. Không thấy đồ vật được cầm hoặc đĩa được nhấc | NONE |
| Nhận diện và bữa ăn | Giữ nhân vật, trang phục, nơ eo và bố trí bàn | Không thấy thay đổi đáng kể về nhận diện, trang phục, nơ eo, vị trí đĩa nem, rau, hai bát, chén chấm, đũa và ly trong so sánh trực tiếp | NONE |

**Quyết định: USABLE CANDIDATE.** Đạt sửa miệng trong phạm vi quan sát ảnh tĩnh. Trạng thái này có thể dùng làm ảnh nghỉ sau tư thế M khi M được giải quyết; ảnh không chứng minh hành động thu tay đã diễn ra.

### REF03-S_v02

Nguồn đối chiếu: `REF03-S_v01_NATIVE.jpg`. Đầu ra xem trực tiếp: `C:/Users/PC/Downloads/REF03-S_v02_REC225_20261007095307.jpg`.

| Tiêu chí | Expected | Observed | Mức độ |
| --- | --- | --- | --- |
| Miệng Đào | Khép hoàn toàn, nhỏ và thư giãn; không khe tối mở, răng hoặc lưỡi | Khe mở của v01 được thay bằng đường môi khép và biểu cảm rất nhẹ. Không thấy khoang miệng, răng hoặc lưỡi | NONE |
| Nụ cười Khoai | Giữ nụ cười riêng, nhỏ, kín miệng | Nụ cười kín miệng và hướng mắt về Đào được giữ ở mức quan sát; không mở miệng hoặc thêm răng | NONE |
| Sự tò mò và ánh nhìn Đào | Giữ ánh mắt tò mò nhẹ hướng về Khoai và góc đầu hiện có | Mắt mở, hướng sang Khoai và góc đầu tương ứng nguồn; cảm giác tò mò nhẹ vẫn đọc được | NONE |
| Tay, đồ vật và tư thế nghỉ | Giữ toàn bộ trạng thái nguồn | Các tay vẫn nghỉ trên bàn; không cầm thức ăn hoặc dụng cụ. Bát, đĩa nem, đũa, rau, chén chấm và ly ở vị trí tương ứng | NONE |
| Nhận diện và trang phục | Giữ mặt, tỷ lệ, áo và nơ eo | Không thấy thay đổi đáng kể trong nhận diện, tỷ lệ hoặc trang phục khi đối chiếu trực tiếp | NONE |

**Quyết định: USABLE CANDIDATE.** Đạt sửa miệng Đào và giữ nụ cười kín miệng của Khoai trong phạm vi ảnh tĩnh.

## Khả năng nối S → M → E → B → R03

| Nối trạng thái | Quan sát có thể dùng | Giới hạn / kết luận |
| --- | --- | --- |
| REF01-S_v01 → REF01-M_v02 | Cùng hai nhân vật và bố trí bàn; S có các tay nghỉ, M có một tay Đào với xuống; hai miệng đều khép | Có sự khác biệt tư thế đủ nhận ra một ý định với tay. M chưa chỉ rõ đích vành đĩa nên chưa đọc chắc là ý định lấy đĩa. HOLD ở M |
| REF01-M_v02 → REF01-E_v02 | E trở lại tay nghỉ, cùng môi khép và giao tiếp bằng mắt | Hai trạng thái tĩnh có thể biểu diễn trước/sau về mặt bố trí. Không chứng minh đường đi của tay, thu tay, thời lượng, hay một hành động đã quay |
| REF01-E_v02 → B/frame-0175 | B có tay nghỉ, miệng khép, hai nhân vật nhìn nhau và bố trí bữa ăn tương ứng; Đào ở B có nụ cười rõ hơn E | Khả năng nối biểu cảm có cơ sở thị giác. B là một frame riêng được xem; không có bằng chứng trong lượt này về speech-end, nhịp thoại hoặc thực tế âm thanh |
| B/frame-0175 → REF03-S_v02 | R03 giữ bữa ăn và tư thế nghỉ; nụ cười nhỏ kín miệng Khoai cùng ánh mắt tò mò nhẹ của Đào phù hợp một trạng thái tiếp theo có thể đề xuất | Chưa kiểm chứng chuyển động giữa các trạng thái hoặc đồng bộ âm thanh. Candidate continuity, chưa phê duyệt chuỗi |

Bố trí chung đủ nhất quán ở mức quan sát để tiếp tục xét ảnh tham chiếu: Khoai bên trái, Đào bên phải, đĩa nem giữa tiền cảnh, rau bên trái, ly bên phải và các tay nghỉ tại E/B/R03. Đây là nhận xét thị giác, không phải kiểm chứng pixel toàn bộ đồ vật hay nhận định về chuyển động.

## Điều đã xác định và vấn đề còn mở

Đã xác định: nguồn/prompt/các bản sao đúng hash; hai sửa miệng đạt về ảnh tĩnh; lỗi vị trí và khoảng hở mục tiêu bàn tay M còn tồn tại. Giả định làm việc: S, M, E, B và R03 được xét như các trạng thái tham chiếu theo chuỗi yêu cầu, không suy ra hành động hoặc âm thanh giữa chúng.

Vấn đề còn mở: tư thế M; tiếp xúc tại vùng ngón tay bị đống nem che; chất lượng chuyển động, continuity theo thời gian, speech-end và giọng nói thực tế. Owner approval REC225 chỉ phê duyệt ba yêu cầu sửa đã giới hạn, không phải output acceptance, retry, video, voice hoặc full G1.

Bước tiếp theo trong phạm vi báo cáo: root tổng hợp các đánh giá độc lập và trình kết quả candidate/HOLD cho owner. Báo cáo này không cấp thẩm quyền tạo lại ảnh, tạo video/voice, chi tiêu, công bố hoặc dùng Git.
