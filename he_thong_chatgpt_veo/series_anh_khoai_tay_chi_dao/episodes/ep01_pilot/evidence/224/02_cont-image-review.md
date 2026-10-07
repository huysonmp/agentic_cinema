# REC224 — CONT: kiểm bốn ảnh mở tập theo chuẩn B

Ngày 2026-10-07. `INDEPENDENT_IMAGE_ONLY_REVIEW / ONE_USABLE_CANDIDATE / THREE_REWORK / NOT_G1_PASS`.

## Phạm vi và quyết định áp dụng

Đọc `native-output-manifest.json`, `owner-approval.json` của224 và nguyên văn bốn prompt bất biến trong `evidence/223/REF01-S.prompt-DRAFT.txt`, `REF01-M.prompt-DRAFT.txt`, `REF01-E.prompt-DRAFT.txt`, `REF03-S.prompt-DRAFT.txt`. Trực tiếp mở **đúng bốn download original JPEG**, cộng ảnh nguồn B `223_g1_source_frames/ANCHOR_B/frame-0175.jpg`, bằng `view_image` ở chế độ original. Không đọc findings của reviewer khác; không browser, tạo ảnh/video, retry, chi credit, git hoặc sửa nguồn. Chỉ viết report này.

Chuẩn hiện hành là variation B đã được owner duyệt riêng EP01: mặt, ánh sáng, nền và ụ món của B. Không chấm lỗi vì ụ món khác TABLE08 cũ. Vẫn giữ identity/outfit, geography bộ phục vụ, món nguội/không khói và F0. Owner224 duyệt chạy một lần cho mỗi ảnh, **không** nghiệm thu đầu ra hoặc G1 toàn bộ.

Đây là QC ảnh tĩnh: không nghe, xem chuyển động hoặc đo lip-sync. Không chứng minh kéo–“Khoan”–dừng, không chứng minh đĩa đứng yên theo thời gian, không chứng nhận toàn cảnh/toàn phim.

## Đối soát target, bản sao và prompt

Nguồn B f175 = 7.291667 s của N02 B. SHA256 nguồn rehash khớp manifest và owner approval: `5bec51d789cebc8b891b26c70d4c52a4a2185ed18b34d0fb933ab6e1cab8c6c5`.

Đã rehash từng **download original + owner_native + repo_native**: cả ba bản của mỗi ID đồng nhất, khớp native hash trong manifest. Đã rehash bốn prompt, bốn preflight AX và bốn result AX: tất cả khớp hash đã ghi. Exact prompt nguyên văn sau trim có trong cả preflight và result cho từng ID; exact Flow asset ID có trong result tương ứng.

| ID / Flow asset | Native SHA256 | Prompt SHA256 |
|---|---|---|
| REF01-S / `558dc41c-45d2-437d-bcbf-e044ece386d7` | `eba9a13c86f359df458022a5a54664264e5bb29fcca08d6181454cb1ee482422` | `09ab77326cfa1d6c6d85836a44212a215759254cd71fb148ddc7f63b15618451` |
| REF01-M / `3b55884c-9da0-47ee-956e-e08f7adf89cd` | `bd48acb3223c417a22918a9d717cb0e1f5f22e118b8584fd2609581f3460f037` | `38c160d65b4ba1e88e967dee84b2382de1242a29c4114bbf2122718e9bbc0fda` |
| REF01-E / `73a13dbf-4f2a-407e-98cf-de9cf5ee1450` | `887f00f0f78ea093529825b108b16d04a63c541b2b637281c7ebb4a52782c6c4` | `c434ac94c16f7c6b2d341507fedbe68eaa833425e861f88cb5435989da92e6d4` |
| REF03-S / `3da59d10-ab70-498a-9ec0-c5aa5270f6f5` | `4a4c4a9ae0dcd017b44a3e7b59b775577cbe7184594994f674526b93f915962e` | `dd338deadd66412fc5c1ff638c39cf4cf91d7d12043ce6a22d77678a34490a29` |

Các preflight đã lưu đều thể hiện Nano Banana 2.1, x1, radio9:16 được chọn, quote “0 tín dụng” và tên nguồn `frame-0175.jpg`. Không truy cập cloud hoặc hash cloud bytes trong review này: tên thumbnail/AX không tự chứng minh byte nguồn upload. Hash local và chuỗi provenance đã lưu được đối soát; không đổi chúng thành xác nhận billing receipt. Manifest ghi native JPEG768×1376, bốn submissions và0 retries; quality vẫn cần kiểm ảnh thực.

## Kiểm chung trên cả bốn ảnh

| Expected | Quan sát thực trên REF01-S, REF01-M, REF01-E, REF03-S | Đánh giá / phụ thuộc |
|---|---|---|
| Giữ Khoai trái, Đào phải; đủ gương mặt/miệng | Đúng phía màn hình, đủ mắt–mũi–miệng của hai người; không thấy swap/mirror. Viền đầu/lá bên phải Đào sát hoặc bị mép ảnh cắt, tương tự nguồn B; không phải mất mặt/miệng. | OBS: đặc điểm mặt cần đọc vẫn thấy rõ. Không chứng nhận identity xuyên chuyển động. |
| Outfit/nhận diện B | Khoai jacket tối/shirt kem; Đào blouse kem, waist tie hồng, váy xanh phần lộ, cuống/lá trên đầu. Texture và tỷ lệ giữ được family B. Biểu cảm khác nhau theo pose. | OBS; thân dưới/giày ngoài khung, không full outfit PASS. |
| Herbs front-left; hai dipping dishes | Đủ đĩa rau trước-trái; dip nhỏ cạnh đũa/bát Khoai và dip trước-phải. Không có garnish mới trên đỉnh nem. | OBS: đúng geography. Một phần dip phải/herbs bị biên ảnh cắt, không quy là xóa vật. |
| Hai bát cá nhân trống; hai đôi đũa nghỉ; glass ngoài phải Đào | Hai bát trơn trước hai người đều không thấy thức ăn. Hai đôi đũa đặt trên bàn. Glass vẫn bên phải Đào, một phần ngoài crop; không ai cầm glass/đũa hoặc miếng ăn. | OBS, F0 trong ảnh. REF01-M chỉ Đào vươn một tay, không cầm thức ăn. |
| Món nguội, không steam/smoke/text mới | Mound còn dạng B; không thấy khói từ món, spilled sauce, food transfer hoặc caption/branding trong bốn ảnh. Dấu watermark dạng ngôi sao còn hiện dưới phải. | OBS về hình; không suy ra công thức/định lượng hay nhiệt độ thực từ ảnh. |
| Đĩa chung/bát không đổi vị trí để làm reach dễ | Đĩa vẫn giữa bàn, hơi bên phải trung tâm khung; bát trước chủ thể tương ứng. S/M/E giữ vị trí tương đối gần nhau, không thấy đĩa chuyển sát riêng Đào. | OBS trong bốn pose, không motion proof. Mound/plate/background được dựng lại và scale khác nguồn360p; exact join với B vẫn cần review. |

Severity: `P1` = trái trực tiếp yêu cầu pose/khóa cần dùng cho ảnh đó; `P2` = rủi ro match hoặc diễn giải cần kiểm; `OBS` = nhìn thấy phù hợp trong ảnh; `UNKNOWN` = ảnh không thể chứng minh. Không cộng OBS thành media/full G1 PASS.

## Findings riêng theo exact ID

### REF01-S — usable candidate có điều kiện

- **Expected:** opening trước reach; Đào nhìn Khoai, Khoai chú ý món; hai miệng đóng, cả bốn tay nghỉ cạnh bát riêng.
- **Observed:** hai miệng đóng. Đào nhìn về Khoai; Khoai nhìn chếch xuống/phải, nét trầm nghĩ, không hướng thẳng camera. Hai tay Khoai và hai tay Đào đều trên bàn gần bát, không chạm đĩa chung, không gắp. Không thấy lỗi nối chi hoặc hand–bowl merge.
- **Severity:** OBS cho pose tay/miệng/F0. P2 cho việc hướng mắt Khoai có đọc đúng “chú ý món” khi nối câu mở: ảnh cho thấy nhìn xuống/phải nhưng không chứng minh một eyeline động chính xác tới món.
- **Dependency:** cần DOP/ACT kiểm biểu cảm và khung nối sang đúng B; không dùng ảnh này để gọi động tác kéo–dừng đã có.
- **Recommendation:** **USABLE CANDIDATE cho G1 ảnh REF01-S**, trình cùng giới hạn; chưa là ảnh production lock hoặc footage đạt.

### REF01-M — REWORK mục tiêu reach

- **Expected:** Đào vươn đúng một tay, đầu ngón vừa tới **mép gần bên phải đĩa chung**, đĩa chưa chuyển; tay kia cạnh bát riêng. Khoai chú ý Đào, tay nghỉ, hai miệng đóng.
- **Observed:** một tay Đào vươn về giữa/trái hơn của ụ nem, ở vùng **viền sau/trên đĩa**; đầu ngón nằm sát vùng món, không đọc được hành động sắp nắm mép gần bên phải. Tay còn lại vẫn cạnh bát Đào; Khoai nhìn cô, tay nghỉ. Hai miệng đóng. Arm reach nhìn có thể thực hiện được; không thấy thêm tay hay hợp nhất tay với bát.
- **Severity:** **P1 sai reach target** đối với exact prompt. P2 nguy cơ hiểu thành với lấy/thò tay về thức ăn vì rim contact chưa rõ; không kết luận ngón đã chạm/gắp thức ăn từ ảnh này. Bộ bàn/F0 không có lỗi trọng yếu khác nhìn thấy.
- **Dependency:** đây là pose trung gian làm rõ ý định kéo đĩa cho R01. Dùng nguyên ảnh sẽ làm chuỗi S→M→E kể khác hành động đã khóa, dù đĩa vẫn giữa bàn.
- **Recommendation:** **REWORK/HOLD REF01-M**. Khi có quyền xử lý tiếp, sửa riêng đường tay/điểm chạm tới vành gần bên phải, giữ đĩa/bát/props và tay kia ổn định; kiểm đầu ngón nhìn rõ tách khỏi món. Không được tự retry trong scope224.

### REF01-E — REWORK miệng đóng

- **Expected:** pose đã ngừng ý định với đĩa, tay trở về nghỉ; cả hai miệng đóng, Khoai hướng chú ý Đào, cô nghe tò mò nhẹ.
- **Observed:** hai người nhìn nhau, cả bốn tay đã nghỉ gần bát, không tiếp xúc đĩa hoặc nhau; plate geography tương thích S/M. **Khoai có khe miệng mở nhìn rõ**, Đào cũng hé miệng nhỏ. Không phải cả hai miệng đóng như prompt.
- **Severity:** **P1 mouth-state mismatch** của ảnh exit. Tay nghỉ/phục vụ OBS; việc đã thật sự dừng động tác là UNKNOWN vì ảnh tĩnh.
- **Dependency:** R01 exit là trạng thái reference nối sang N02, không được dùng miệng mở để ngầm chứng nhận speech/lip-sync hoặc gán lượt nói cho Đào.
- **Recommendation:** **REWORK/HOLD REF01-E** về miệng; giữ nguyên tay/đĩa/bát/nhận diện và hướng nhìn. Không đổi lời hay tự dựng khẩu hình từ ảnh này.

### REF03-S — REWORK/HOLD miệng Đào

- **Expected:** sau ký ức, Đào tò mò hướng Khoai, anh cười kín; cả hai miệng đóng, tay nghỉ, chưa chuyển sang cốc/gắp.
- **Observed:** Khoai cười nhỏ, miệng đóng; Đào nhìn Khoai với lông mày hơi nâng và **môi hé, có khe nhỏ ở miệng**. Tay hai người nghỉ, glass/đũa chưa cầm, bát trống. Không có dấu hiệu pose caught/receiving-bowl hoặc romance trong ảnh.
- **Severity:** **P1 đối với yêu cầu “both mouths are closed” của exact pose**, dù độ hé của Đào nhỏ hơn lỗi Khoai ở REF01-E. OBS cho F0 và bộ bàn. Không khẳng định Đào đang nói từ một ảnh.
- **Dependency:** cần một neutral closed-mouth pose làm đầu R03; ảnh hiện chưa đúng yêu cầu ấy. Độ gần về biểu cảm không thay thế kiểm mouth state.
- **Recommendation:** **REWORK/HOLD REF03-S** về miệng Đào; giữ nét tò mò và smile kín của Khoai. Không dùng kết quả generation làm approval tự động.

## Review ngắn đề xuất sửa v02 — chưa duyệt, chưa thử

Sau QC độc lập, đọc ba draft `REF01-M.repair-v02-DRAFT.txt`, `REF01-E.repair-v02-DRAFT.txt`, `REF03-S.repair-v02-DRAFT.txt` do root chuẩn bị trong evidence224. Không sửa prompt, không gửi, không hash/chứng nhận input cloud đã chọn. Input **dự kiến** là đúng output v01 tương ứng với UUID/hash đã đối soát ở bảng trên; giữ REF01-S, không sinh lại.

| Draft | Độ rõ và mức phù hợp findings | Điều còn phải chứng minh trên output nếu được duyệt |
|---|---|---|
| REF01-M repair | Nêu rõ chỉ arm/hand của Đào; right-hand rim screen-right, phía gần Đào; không over mound hoặc behind plate; có khe nhỏ trước ceramic rim; arm tránh xuyên bát; giữ các tay khác và miệng đóng. Phù hợp lỗi reach target. | Đường arm có chiều dài/góc khớp tự nhiên, không xuyên bát hoặc đổi camera/đĩa để né; rim và gap nhìn rõ. Ngôn ngữ “stationary/exactly” không tự bảo đảm bảo toàn pixel hoặc chuyển động. |
| REF01-E repair | Chỉ khép môi cả hai, không dark gap/teeth/tongue; giữ eyes/head/gaze/hands/meal. Khớp blocker của E. | Cả hai miệng thật sự kín mà không đổi identity/biểu cảm, không reset tay hoặc props. |
| REF03-S repair | Chỉ môi Đào; giữ curiosity trong mắt và closed-mouth smile của Khoai. Khớp phạm vi cần sửa. | Đào kín môi, Khoai không bị mở môi hoặc đổi smile; các thuộc tính B và F0 còn đúng. |

Ba draft đủ rõ để root trình một đề nghị sửa có giới hạn. Đây là **PROPOSAL ONLY / NOT_TESTED**, không nghiệm thu tính khả thi model hoặc kết quả v02. `owner-approval.json` của224 khóa một attempt mỗi ảnh và retry=false; proposal này cần approval mới cho hành động sửa trước submit. CONT không tự cấp quyền hoặc đánh dấu ba blocker đã đóng.

## Disposition cuối vòng

| Exact ID | Kết luận CONT ảnh | Blocker / dependency chính |
|---|---|---|
| REF01-S | Usable candidate có điều kiện | Eyeline/acting và join B chưa kiểm động |
| REF01-M | REWORK/HOLD | Tay chưa hướng đúng mép gần bên phải, vùng món/rim dễ hiểu sai |
| REF01-E | REWORK/HOLD | Miệng Khoai mở và Đào hé, trái pose đóng miệng |
| REF03-S | REWORK/HOLD | Miệng Đào hé, chưa neutral closed-mouth start |

Đã xác định: exact source/prompt/copies đúng chuỗi evidence local, serving set/F0 còn đủ trong bốn ảnh; không có lỗi food/steam mới nhìn thấy. Quyết định cũ về B được giữ, không nâng bốn ảnh thành đã được owner nghiệm thu. Giả định làm việc: pose nguyên văn là tiêu chí ảnh, không là speech frame. Còn mở: sửa/đổi disposition ba ảnh, acting/eyeline/joins và G1 toàn tập. Bước tiếp: root tổng hợp với reviewer khác, trình đúng findings và phạm vi cần xử lý; không generation/retry/video/voice/chi mới từ report này.
