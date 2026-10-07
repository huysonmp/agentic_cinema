# C01B — Coverage mới theo hướng A, DOP248

Run C01B-COVERAGE-DOP-248, ngày 08/10/2026. Vai DOP maker; mode PAPER_PROPOSAL / ACTUAL_REFERENCE_STILL_VIEW. **Disposition: PROPOSAL_COMPLETE / INPUT_AND_FEASIBILITY_GATES_PENDING. Không media PASS, không duyệt ảnh mới hoặc quyền submit.**

## 1. Đầu vào và năng lực thực

Đã đọc đầy đủ kế hoạch236, hợp đồng/vai217, `00_decisions/C01B-stop-and-coverage-options-247.md` và `00_decisions/C01B-repeated-start-stop-247.json`. Theo dispatch REC248, owner chọn A và yêu cầu tiếp tục: mở thiết kế coverage riêng C01B, không chọn B thay hình C01A. Trạng thái “chưa duyệt hướng” trong247 là lịch sử; ảnh/video/request mới vẫn cần gate riêng.

Đã trực tiếp xem hai ảnh local bằng view_image:

1. `02_refs/C01B_START_from_C01A_T04_FLOW_v1.png`: actual A80 source, hash theo manifest `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb`.
2. `02_refs/C01A_F0_from_C02_T02_v1.png`: F0 đầu C02 đã chọn, hash theo manifest `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`.

Tôi không xem/nghe toàn cut trong run này, không certify dense continuity, audio hoặc sync. Giữ C01A exact 3,375s và C02 exact 7,541667s; không crop/offset/overlay/freeze/speed sửa các file đó. Tổng hai cut 10,916667s là phép tính từ handoff, không timing mới tự đo. Không UI, generation, API, Git hoặc chi credit; chỉ viết report được giao. Hợp đồng PROD7/02, DIRECT01/DIRECT03 đã đọc đầy đủ trong các run cùng context được giữ.

## 2. State thực và nhiệm vụ mới

A80 cho thấy Khoai trái, Đào phải; môi khép, mặt rõ. Tay ngoài Đào đang ở mép phải đĩa; tay trong gesture cong gần bát cô, chưa nắm mép trái đĩa. Bát trống, đũa nghỉ; nem nguội giữa bàn, hai chấm, rau trước-trái, cốc ngoài phải. Still không chứng minh toàn prefix chưa kéo đĩa. Ngoại lệ rim-touch/inner-gesture không cho phép một lượt two-hand grasp mới.

C02 F0 có hai tay Đào nghỉ cạnh bát; Khoai tay nghỉ, nhìn món, Đào nghe. END phải về trạng thái tương thích ấy, không reset đĩa/nem/bát/đũa/chấm/rau/cốc. Góc khác chỉ đổi projection, không đổi món hoặc vị trí scene.

Cơ chế kể: **Khoai ngắt nhẹ vì ký ức → Đào nhận lời ngắt → buông contact hiện có → thu về nghỉ**. Không quát, không gắp mới, không kéo đĩa rồi trả. Đổi coverage có động cơ nhìn người ngắt rồi người nghe, không dùng món hoặc crop để né lỗi start.

## 3. So sánh tuyến và khuyến nghị sau tích hợp root

| Tuyến | Giá trị | Rủi ro / điều kiện |
| --- | --- | --- |
| Một shot hai người ở góc mới | Ít cut, có thể thấy lời ngắt và phản ứng cùng lúc | Vẫn speech + contact + inner-hover + release trong một output. Đổi góc không chứng minh đã sửa source-to-start |
| BM thiên Khoai + BR thiên Đào, hai reference mới | Hai nhiệm vụ chuyên biệt; BR có thể nhấn mặt và tay người nghe | Thêm ảnh tái lập bàn/pose và join; vẫn cần chứng minh BR START đúng contact |
| **BM thiên Khoai mới + BR trở về khung chung gốc** | Chuyên biệt mặt Khoai, rồi trực tiếp thấy Đào release trong khung đã có. BR dùng A80/C02 F0 cùng camera, giảm nguồn tái lập | BR vẫn phải thể hiện nghe→buông→thu, không reset. Tính năng dùng hai refs START/END phải kiểm live; không hứa khóa motion |

**Khuyến nghị sơ bộ ưu tiên tuyến thứ ba**, theo đề nghị tích hợp root: BM mới có coverage thực sự thiên Khoai, BR quay về khung chung gốc. Đây là phương án thiết kế, chưa feature hoặc cost đã kiểm. BR không cần sinh ảnh mới chỉ để đổi cỡ cảnh; exact A80 và C02 F0 là hai state nguồn cần bảo toàn. Nếu tuyến công cụ không dùng được cặp đó theo quyền hiện hành, CTD phải nêu khoảng thiếu, không gọi Ingredients là frame-lock.

Không retry nguyên setup T01/T02 chỉ đổi tên. Không pan từ Khoai sang Đào trong một take để thêm nhiệm vụ camera motion. Root/DIR chốt lựa chọn tích hợp sau ACT/EDIT.

## 4. Spec ảnh BM — Khoai nói “Khoan”

**Ảnh mới BM_START, chưa file thật:** cận vừa thiên Khoai; toàn mặt, mắt, mày và miệng rõ. Camera cùng phía trục, anh nhìn về Đào ở phía phải ngoài máy, không nhìn thẳng ống kính như MC. Có đầu/cuống thân và phần áo đủ giữ identity/clothes; nền quán cùng scene, sắc ấm mềm. Cỡ mặt lớn hơn khung chung có lý do: một lời ngắt nhỏ được đọc bằng mắt và miệng, không bằng tay chặn.

Không cố nhét toàn bàn vào shot khiến BM chỉ là khung chung cũ. Đào và vùng tay/đĩa có thể ngoài coverage BM; **phần ngoài khung là UNKNOWN đối với quan sát shot này**, không bằng chứng đã giữ contact. Không dời/xóa props để tạo cận; chỉ thay vị trí/cỡ nhìn có động cơ trong reference mới. Không digital crop clip T01/T02 lỗi rồi gọi sửa xong; không crop bỏ watermark nguồn.

State scene vẫn lấy A80: Đào outer-hand contact mép phải, inner hover gần bát; Khoai tay nghỉ, đĩa chưa kéo/nem chưa lấy. Khi tạo reference, phải giữ định nghĩa state ngoài khung và nguồn full-scene, không tạo lại toàn bàn tùy tiện. Cận không cấp quyền chấp nhận một reset rồi giấu ở ngoài khung; BR phải hiện đúng contact để nối.

**BM diễn:** chỉ Khoai/K20 nói đúng một lần “Khoan.” ngắt thân mật, không quát hoặc cười punchline; miệng khép sau âm cuối. Không lời ký ức trong BM, không voice Đào hoặc động tác giơ tay. BR nhận cue sau trọn âm ở BM; không chuyển Khoan lên hình miệng nghỉ của Đào.

**Spec END/đệm:** Khoai kết lời, còn nhìn bạn tự nhiên; không hold cố định theo giây giấy. EDIT đo lời/âm cuối thực trước cut. BM không có coverage tay nên không certify release/start geometry bằng shot này. Không extra action được tự chèn ngoài frame.

## 5. BR — khung chung gốc, mặt Đào và release thật

### START

Dùng **A80 thật** đã xem làm state reference, không sinh một two-hand grasp mới. Camera khung chung gốc: hai mặt đầy đủ, Đào phải, Khoai trái; thấy cả hai tay Đào, mép phải đĩa, bát riêng, đôi đũa vùng ngoài bát. Tay ngoài đang chạm vành; tay trong cong gần bát, không chạm vành trái. Đĩa/nem/chấm/rau/cốc giữ source.

BR không mở bằng đôi tay đã nghỉ để bỏ qua release. Không reset inner-hand ra đĩa rồi thu. Người xem phải thấy quan hệ Đào nhận lời ngắt qua ánh mắt/hướng chú ý và ngừng ý định; không cần thêm thoại hoặc giật mình khoa trương. Không voice Đào, không nhép “Khoan”.

### END và đường diễn

Đích END là C02 F0 thật: outer-hand nghỉ bên phải bát, inner-hand nghỉ bên trái; bát trống, đũa nằm bàn, nem còn đĩa, không kéo/lấy/ăn/lấy cốc. Khoai tay nghỉ, sẵn kể; Đào nghe anh.

Đường phải nhìn thấy: outer-fingers nới contact → tách khỏi vành → cẳng tay thu ngắn qua trên vùng đũa về thân/cạnh ngoài bát. Inner-hand chỉ settle về cạnh trong bát, không reach tới đĩa. Giữ thấy mép đĩa và khoảng tách ngón; đĩa không đi cùng tay hoặc được trả về sau khi kéo. Không teleport contact→rest. Không đổi camera trong BR, tilt theo tay làm mất mặt hoặc insert món che release.

Giữ warmth/readability/identity/clothes từ A80 và C02. Background phụ, không thêm khói/steam/đèn màu hoặc lettering. Watermark nguồn phải giữ; spec reference không quyền xóa/crop nó.

### Trade-off cụ thể

Khung chung không làm mặt Đào lớn bằng BR cận mới, nhưng source hiện có đã thấy rõ mặt, tay và contact; geometry/table được neo ít nguồn tái lập hơn. Nếu actual mặt/ánh nhìn quá nhỏ để đọc phản ứng, đó là finding cần trình, không tự phóng crop hoặc ghi shot đạt vì tay đã về nghỉ.

Nếu FLOW xác minh tuyến Frames phù hợp cặp START/END và quyền mới sau stop, có thể đề xuất dùng cho BR không thoại. Nhưng toggle/refs không chứng minh môi khép, exact start, path đúng hoặc không reset món. DOP không quyết model/mode hoặc gọi tuyến đó trước kiểm live.

## 6. Timing và ba join bắt buộc

Giữ C01A 3,375s và C02 7,541667s. Slot mở 4,5s ở236 chỉ target cũ: nếu giữ nguyên thì còn 1,125s cho BM+BR, **chưa có bằng chứng diễn đủ**. Không ép Khoan + nhận cue + buông/thu vào đó bằng speed hoặc cắt nghĩa. EDIT phải đo actual BM/BR và lập phân bổ 30s; coverage approval không tự duyệt mọi EDL. Không bịa hai mốc giây như actual.

1. **C01A→BM:** chuyển chú ý tới người ngắt, giữ identity, eyeline và scene. Không dùng cận như lý do xóa contact ngoài khung. A exact giữ nguyên.
2. **BM→BR:** Khoan đã thấy mặt Khoai và nghe nguyên âm; BR trở về source contact để thấy release sau cue. Không lặp động tác hoặc để reset. Nếu actual BM cho thấy Đào đã buông dù trong vùng phụ nhìn thấy, derive lại dependency hoặc REWORK, không giả BR START nguyên A80.
3. **BR→C02:** tay đã về nghỉ rồi nối C02 exact; food/table/mặt/light vẫn phải kiểm qua cut. Không dissolve/freeze/overlay để làm biến mất sai state.

## 7. Kiểm dự thảo ảnh BM v1 — maker still feedback

Sau khi lập spec, đã trực tiếp xem `02_refs/C01B_BM_START_v1_CHATGPT_FOR_REVIEW_248.png` và tính lại SHA256 `8ecb1105de2b8a0b786c05ad38e4965206d62a7629741a7863e8fcb77f7bad03`. Đây là ảnh do root tạo bằng công cụ ChatGPT, không ảnh do DOP tạo. Kích thước 941×1672 theo handoff root, chưa đúng tuyệt đối 9:16; không suy thành video720p đạt format.

Quan sát: mặt Khoai lớn hơn rõ so khung chung, toàn mắt/mày/miệng trong khung, anh bên trái và nhìn xuống vùng món. Phần mặt Đào ở phải bị cắt biên, không phải shot đủ hai mặt; điều này phù hợp nhiệm vụ BM thiên người nói, nhưng không dùng để kiểm toàn phản ứng Đào. Áo/quán/palette ấm tương thích về nét chính trên still; Khoai hai tay nghỉ, bát/đũa trước anh thấy được. Tay trong Đào cong ở vùng gần bát bên phải khung, không thấy một two-hand grasp. Tay ngoài và mép phải đĩa ngoài khung: **contact/state đó UNKNOWN**, không được chứng nhận đã giữ nguyên bằng ảnh này.

Khung đã có khác biệt coverage có động cơ, không cần nhét lại toàn bàn. Props và món bị cắt biên; tôi không có bằng chứng các props ngoài khung được giữ đúng vị trí, nên chỉ gọi “không quan sát được”, không claim đã cropped-not-relocated về mọi đồ. Phần nem nhìn thấy vẫn nguội/không thấy khói; lượng, từng miếng và full plate contour không kiểm được trong cận. Không thấy watermark nguồn gốc trong phạm vi ảnh này; root/RIGHTS cần đối soát provenance/chính sách giữ watermark, không DOP tự chấp nhận bỏ dấu.

**Đề xuất giữ BM v1 làm candidate trình review đúng phạm vi framing**, chưa self-PASS hoặc owner-approved. Khi video BM có, actual face/miệng/K20/nhịp phải kiểm; phần tay nếu lộ ra phải đúng source, không dùng offscreen để hợp thức hóa reset. BR original wide A80→C02 F0 vẫn là nơi bắt buộc proof contact→release→rest, không lấy BM đẹp làm bằng chứng thay. Actual BM→BR và BR→C02 phải xem bản ghép mới; still không certifies motion hoặc continuity.

## 8. Cổng kiểm và handoff

| Rule | Hiện tại | Closure |
| --- | --- | --- |
| DOP248-DIRECTION | Owner A mở design mới | Root version-lock coverage sau tích hợp; stop T01/T02 không tự biến thành quyền T03 |
| DOP248-BM | Cận Khoai rõ, scope bàn có thể ngoài frame | Ảnh mới kiểm identity/axis/clothes; actual tiếng K20/mouth/nhịp. Ngoài frame không certify geometry |
| DOP248-BR | A80→C02 F0 đã xem, direct-release specification | Actual START/path/END + face/eyes/hands/rim; no extra reach/two-grasp/pull/reset |
| DOP248-TIMING | Target, chưa EDL | EDIT/SIA đo nguyên âm và diễn actual, full30s gate |
| DOP248-TOOLS | Feature/cost chưa kiểm trong run này | CTD/FLOW UI/live quote/input/mode/scope; không hứa STARTlock |
| DOP248-QUALITY | Still spec không chứng nhận media | Reviewer độc lập paper/actual theo capability, owner checkpoint đúng target |

Đã xác định: hai source ảnh thực và repeated-start STOP; contact/inner-hover→F0 là nhiệm vụ không được bỏ. Chốt từ owner248: hướng A, giữ exact C01A/C02/canon/table/voice. Đề xuất DOP: BM mới thiên Khoai, BR trở về khung chung gốc với source state thật; không buộc full-table vào cận hoặc dùng ngoài khung miễn lỗi. Giả định: chuyên biệt shot giúp ý nghĩa và QC rõ hơn, chưa chứng minh model đạt. Còn mở: DIR/ACT/EDIT integration, BM reference, công cụ/giá, actual voice/motion/timing/joins. Bước tiếp: root đọc full contributions, hợp nhất specs và preflight trước generation. Không ảnh/video/credit mới từ DOP.
