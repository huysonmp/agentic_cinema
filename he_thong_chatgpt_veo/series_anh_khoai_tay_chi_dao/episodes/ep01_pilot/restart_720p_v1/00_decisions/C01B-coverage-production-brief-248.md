# C01B — Gói quay mới theo hướng A

Ngày 08/10/2026. Phiên bản 248/v1. **THIẾT KẾ VÀ ẢNH DỰ THẢO — CHƯA CHẠY VIDEO, CHƯA ĐƯỢC CHỌN LÀ MEDIA SẢN XUẤT.** Owner đã chọn hướng A; việc này không tự gỡ STOP của hai take cũ.

**Cập nhật REC249:** owner trả lời “duyệt” cho ảnh/cách quay và tối đa hai đầu ra, tổng ≤30 credit, mỗi đầu ra ≤15 sau kiểm tuyến/quote live. Xem `C01B-coverage-owner-approval-249.json`. Các dòng “chưa owner duyệt”/PRODUCTION_HOLD phía dưới giữ làm lịch sử lúc trình248; nay được mở kiểm live và sản xuất có điều kiện, không tự duyệt chất lượng output, retry cũ hoặc cả phim.

**Kết quả thực REC249:** đã tạo một BM, debit 7 credit; nguồn native được root và reviewer độc lập đối chiếu hình, chưa nghe thực. Burn-in “Khoan” và thay đổi gaze/hover của Đào chặn chọn BM theo gói này. **BM không được chọn; BR chưa chạy và vẫn bị chặn; không automatic retry.** Xem request, native report và bài học 249. Đề xuất cận riêng Khoai/ảnh mới và tăng count cả đợt lên tối đa ba đầu ra trong cùng trần 30 vẫn chưa được duyệt.

## 1. Thay đổi đúng tầng phát sinh lỗi

T01/T02 đã sai tư thế đầu C01B trước khi ghép: tay trong Đào ở vùng vành trái thay vì gần bát. Bản nối Flow chỉ tái hiện lỗi nguồn. Chưa chứng minh một câu prompt cụ thể hoặc cơ chế nội bộ nào là nguyên nhân duy nhất.

Lần này tách nhiệm vụ nói và thu tay thành hai nguồn có thể kiểm riêng. **BM** chỉ Khoai nói; **BR** là Đào phản ứng không lời, quay lại góc bàn gốc. Không đưa nguyên yêu cầu cũ vào T03 rồi đổi tên. Đây là giả thuyết giảm việc model phải làm đồng thời, chưa phải bằng chứng chắc thành công.

## 2. Hai cảnh và ba điểm nối

| Đoạn | Hình và diễn cần có | Tiếng / trạng thái |
| --- | --- | --- |
| C01A đã chọn | Giữ nguyên bản cắt 3,375 giây; kết ở contact vành phải, tay trong gần bát | Đào nói đủ N01; không dùng đuôi kéo đĩa |
| **BM — người ngắt** | Cận vừa thiên Khoai, mặt/miệng rõ. Anh nhìn sang Đào, ngắt mềm, hai tay nghỉ; không diễn một cử chỉ chặn tay. Đào chưa buông hoặc hoàn tất phản ứng trong BM | Chỉ Khoai/K20 nói đúng một lần “Khoan.”; giữ nguyên âm cuối trên hình người nói |
| **BR — người nghe** | Trở về góc bàn gốc. Đào bắt đầu ở contact đang có: nâng mắt về anh → nới ngón khỏi vành → thu tay ngoài về cạnh bát. Tay trong chỉ hạ về thân/bát, không tới vành trái. Hai tay nghỉ trước khi sang C02 | Không thoại/voice mới, không nhép miệng. Đĩa đứng yên, bát trống, chưa gắp/ăn |
| C02 đã chọn | Giữ nguyên bản 7,541667 giây: Khoai kể ký ức | Phần N02 sau “Khoan”; không lặp từ ngắt |

**C01A→BM:** đổi trọng tâm sang người ngắt, giữ người/bàn/trục. Không yêu cầu khớp pixel ở một cỡ cảnh khác, nhưng không được đổi trạng thái hành động.

**BM→BR:** cắt ngay sau trọn từ ngắt, không chèn một khoảng chờ dài. BR dùng trạng thái A80 mắt còn thấp rồi mới phản ứng. Vì vậy BM không được cho Đào đã quay mắt/buông rồi BR trở về pose cũ. Nếu nguồn BM thực làm vậy, không được dùng hai ảnh mong muốn để hợp thức hóa reset; phải xử lý dependency trước chạy BR.

**BR→C02:** thấy động tác buông–thu hoàn tất, rồi nối đúng trạng thái nghỉ. Không cắt bỏ release, không dùng cảnh món, freeze, tua nhanh, hòa cảnh hoặc tiếng chồng lên môi khép để che thiếu hình.

## 3. Bộ ảnh — nguồn và giới hạn

| Vai trò | File dưới `02_refs/` | Định danh / trạng thái |
| --- | --- | --- |
| BM_START mới | `C01B_BM_START_v1_CHATGPT_FOR_REVIEW_248.png` | SHA256 `8ecb1105de2b8a0b786c05ad38e4965206d62a7629741a7863e8fcb77f7bad03`; **941×1672**, gần nhưng không đúng tuyệt đối 9:16; chưa owner duyệt |
| BR_START | `C01B_START_from_C01A_T04_FLOW_v1.png` | Exact A80, SHA256 `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb`; 720×1280 |
| BR_END / đích C02 | `C01A_F0_from_C02_T02_v1.png` | SHA256 `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`; 720×1280 |

BM được tạo bằng công cụ ảnh tích hợp ChatGPT từ A80, không gọi API hoặc dùng credit video Flow. Prompt nguyên văn lưu tại `02_refs/C01B_BM_START_v1_image_prompt_248.txt`.

Root đã xem ảnh: Khoai rõ toàn mặt, lớn hơn khung cũ, giữ áo và hướng trái/phải; tay trong Đào gần bát còn nhìn thấy. Tay ngoài/contact không nằm trong khung BM, nên **không thể chứng nhận tư thế tay đó bằng BM**. Mặt Đào bị cắt ở biên phải là phạm vi speaker coverage, không ảnh master hai người. BR phải trả lại mặt và toàn đường tay để kiểm; không coi phần ngoài khung là được phép diễn khác. Món/đồ ngoài khung BM cũng không có PASS từ ảnh này.

Không tự resize/crop ảnh để gọi đã đạt 720p. Độ phân giải/aspect của video phải kiểm riêng trên cấu hình live và native; nếu UI xử lý input làm mất mặt hoặc thông tin cần thiết, dừng sửa input trước submit.

Nguồn A80/C02F0 giữ nguyên, không sửa/xóa dấu gốc. DOP ghi watermark nguồn không nằm trong phạm vi ảnh BM mới; ảnh này là reference tái dựng coverage bằng ChatGPT, không một bản native đã xóa watermark. Không lấy sự vắng dấu trong preview làm quyền xóa dấu trên bất kỳ native/export nào. Provenance của reference gồm ảnh nguồn, prompt và hash output; nếu reviewer thấy phạm vi xử lý chưa phù hợp, sửa/chốt trước upload, không tự gọi rights gate đã đạt.

## 4. Tuyến thực thi dự kiến — còn cổng kỹ thuật

- BM: tuyến Ingredients đã sử dụng, chỉ custom K20 mới; một ảnh BM, một voice, một câu. Không thêm D06 hoặc lấy tiếng T01 ghép vào miệng tĩnh. Take BM mới phải kiểm/nghe đúng giọng riêng.
- BR: khảo sát tuyến Frames không lời với hai ảnh START/END cùng góc bàn gốc. **Chưa xác minh lại trên UI ở REC248 rằng tuyến này nhận hai ảnh theo cách cần, giữ cấu hình 720p và không speech.** Nếu composer thiếu tính năng hoặc tự fallback, HOLD; không tự quay về Ingredients với lời hứa “exact” hoặc cài tool mới.
- Endpoint đúng không chứng minh path đúng. Chỉ nguồn BR thực có release→retract, không extra reach/pull/teleport, mới được chọn.
- Thứ tự: chốt thiết kế/ảnh → kiểm tuyến và quote → BM → chọn range hợp lệ/kiểm dependency → BR → dựng thử C01A/BM/BR/C02 → phản biện actual. Không tạo BR trước khi biết BM có bảo toàn trạng thái chưa phản ứng hay không.

## 5. Nhịp và ngân sách

A+C02 giữ nguyên: **10,916667 giây**. B mới giả định cần khoảng **2–3 giây selected**, chưa có native để đo. Phần C03A trở đi còn khoảng **16,083333–17,083333 giây**. Không ép B vào slot 1,125 giây giấy trước đây; không tự rút lời hoặc bỏ nhịp các đoạn sau để vừa 30 giây. EDIT lập range/EDL thật sau khi có nguồn, hiện range BM/BR là UNKNOWN.

Đề nghị giới hạn lần sản xuất đầu theo coverage mới: **hai đầu ra, tối đa 15 credit/đầu ra = trần 30**, từng request x1, quote cuối phải kiểm live. Đây là trần đề nghị, **chưa là quote hoặc quyền chi mới**; không tự retry, không giải ngân 110 dự phòng. Nếu cần retake phải chẩn đoán và đối chiếu phạm vi quyền trước.

Snapshot REC247: đã dùng **74/500**, còn **426**, trong đó **316 đã phân bổ còn lại +110 dự phòng chưa duyệt**. REC248 chưa chi credit video; không kiểm lại số dư tài khoản live ở lượt thiết kế này. Dự toán 30 chưa trừ khỏi sổ chi thực.

## 6. Cổng kiểm và điều kiện loại

1. **Thiết kế/ảnh:** DIR/DOP/ACT/EDIT đóng góp riêng; root đọc đầy đủ, reviewer khác maker phản biện. Owner duyệt đúng coverage/ảnh mới, không hỏi lại A/B.
2. **Trước submit:** nguồn/hash/cloud ID; một voice đúng ID K20 ở BM; BR không voice; prompt readback; mode/model/720p/9:16/x1/Agent OFF; giá cuối và quyền chi. Chưa có các field live thì không ghi READY.
3. **BM native:** Khoan một lần, đúng người/giọng, thấy môi nói trên đủ từ; không giơ tay hoặc cho Đào phản ứng hoàn tất rồi reset qua BR. Nghe thực bởi owner hoặc reviewer có capability, không lấy ASR/preset làm PASS.
4. **BR native:** đầu đúng chức năng hai tay, mắt nghe → outer release → return, inner settle inward, đĩa/nem/bát/đũa/rau/chấm/cốc không đổi. Trích toàn khung và mẫu dày bằng công cụ QC đã có; mẫu ảnh không được gọi là full AV.
5. **Bản ghép thực:** kiểm ba điểm nối, lời/nhịp/người nói/nghe, thời lượng/raster/FPS thực. Source đạt riêng không thay review target export. Chưa đạt chuỗi này chưa mở C03A, finishing hoặc bàn giao.

## 7. Quyết định cần chốt tiếp

**Kết quả phản biện độc lập đã được root đọc đầy đủ:** `06_qc/C01B_coverage_independent_248.md` cho phép trình gói thiết kế/ảnh có điều kiện, không thấy lỗi buộc remake BM trước trình; vẫn PRODUCTION_HOLD. Đã kiểm ba still/hash, chưa nghe/xem video mới. Root chốt tài liệu tích hợp này và DOP/EDIT cập nhật là chuẩn chuyển request; yêu cầu thấy đủ tay trong BM hoặc để Đào đã phản ứng trước cut ở DIR ban đầu là đề xuất lịch sử, không được chép vào prompt hiện hành. Bổ sung DIR phải đồng bộ, không đổi lại gói này âm thầm.

**Đóng xung đột spec bởi root:** DIR đã bổ sung phụ lục tích hợp ngày 08/10, root đọc đầy đủ phần mới: đồng ý BM contact ngoài khung UNKNOWN, BR nguyên góc chung A80→C02F0, phản ứng chỉ bắt đầu ở BR. Yêu cầu cũ được đánh dấu lịch sử. Reviewer độc lập chưa kiểm phụ lục sau đó; closure này là đối soát văn bản của root, không review độc lập video hoặc gỡ STOP. Trạng thái cuối lượt248: **GÓI THIẾT KẾ CÓ THỂ TRÌNH OWNER; SẢN XUẤT VẪN HOLD**.

Một quyết định: duyệt **BM cận Khoai mới → BR trở về góc bàn gốc, dùng A80/C02F0**, cùng ảnh BM dự thảo, để mở kiểm tuyến/quote và lần sản xuất giới hạn hai đầu ra ≤30 credit. Nếu owner chỉ duyệt nghệ thuật/ảnh mà chưa cho chạy, ghi riêng phạm vi đó; không mặc định media đã đạt.

Đã xác định lỗi nguồn và các mốc thật; đã chốt hướng A và giữ C01A/C02/giọng/lời. Giả định mới là tách nhiệm vụ có lợi, không cam kết tỷ lệ thành công. Còn mở: duyệt gói này, feature/quote live, output/joins/timing actual. Bước tiếp là đóng review thiết kế/ảnh và trình quyết định có phạm vi rõ.
