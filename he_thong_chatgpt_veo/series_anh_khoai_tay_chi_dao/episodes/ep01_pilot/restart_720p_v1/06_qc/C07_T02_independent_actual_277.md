# REC277 — C07 T02: phản biện độc lập bản gốc

Ngày 13-10-2026. RUN_ID: REC277-C07-T02-INDEPENDENT-ACTUAL. Kết luận: **IDENTITY_AND_ENTRY_STATE_MAJOR / REWORK / STOP_FOR_DIAGNOSIS / NOT_SELECTED / AUDIO_AV_HOLD / C08_HOLD**.

Đào đã biến thành phụ nữ người thật ngay F0, bát Khoai biến mất, cốc và vị trí A bị reset. Không có prefix đạt để chọn. Không dùng việc một bát bên phải được kéo sang trái để bù sai nhân vật và mất state.

## Target và bằng chứng thực kiểm

Native: `05_native/EP01_720_C07_T02_NATIVE.mp4`, SHA-256 tự tính lại **`c793308e55ed02f5b61fb9dfd1f4f6edaa4b3302bdb520defb108cfa5b5140da`**, khớp evidence/manifest. Owner copy và evidence tại `C:/Users/PC/Downloads/du_an_nem_bui/277_C07_T02/`.

Đã đọc đầy đủ final `04_requests/C07_T02_prompt_277.txt`, preparation277 và run277. Final hash đã tự xác minh trong preflight: `ae636235971fb36f5a31234dcb294cb91ea5d12c9231c8b046b797b8ad756ef4`. Run lúc bắt đầu đọc còn `SUBMITTED_ONCE_RESULT_PENDING`; đó là snapshot chưa cập nhật receipt, không phủ định nguồn mới đã tự kiểm hash. Root cần lưu actual disposition đúng native mới.

Đã đọc đầy đủ `native_qc/native_evidence.json` và `native_qc/action_all/manifest.json`. Trực tiếp xem **tất cả18 board action_all_01–18.jpg, đủ144 khung F0–143**, tám khung mỗi board. Xem thêm full PNG F0/F64/F143 (tên file=F+1), cùng exact START từ C06 nativeF56 (`02_refs/C07_START_from_C06_T03_selected_F56_276.png`, hash đã tự xác minh `69fb0e62a3a6f138a0eae622603945b248ec8d2809c8cda513dcdfdc33d00863`). Không đọc maker actual T02.

Scope: **ALL_FRAME_STILLS_NOT_AV**. Không nghe hoặc xem AV liên tục; không ASR. Evidence kỹ thuật đã đọc: H264720×1280,24fps,144 khung/video6 giây, AAC stereo48kHz/audio6,016 giây, full decode success/source unchanged. Reviewer không chạy probe/decode lại. Không browser/API/credit/git/new tool/script/media edit. Không chứng nhận giọng D06, trọn N07 hoặc sync từ metadata/preset.

## Findings thực tế

F tính từ0; thời gian=F÷24.

| ID / mức độ | Mong đợi và quan sát | Bằng chứng / kết luận |
|---|---|---|
| IDENTITY01 — **MAJOR toàn nguồn** | Expected Đào là nhân vật đào nhân hóa trưởng thành đã duyệt. Actual là phụ nữ người thật: tóc nâu, tai/khuyên tai, mặt và hai tay người; không còn đầu quả đào/lá hoặc tỉ lệ tạo hình mẫu. | F0–143, đủ18 board/fullF0/F64/F143 so START. Không phải đổi biểu cảm hoặc drift nhẹ. Không thể crop/trim để phục hồi nhân vật. |
| BOWL_STATE01 — **MAJOR ngay entry** | START có bát Khoai bên trái trước anh và bát Đào bên phải. Actual chỉ thấy một bát bên phải trước nhân vật nữ; bát Khoai không tồn tại tại vị trí thừa kế. Cô kéo bát duy nhất sang trái tới trước Khoai. | FullF0/F64/F143 và toàn nguồn. Không được gọi bát Khoai giữ cố định; không thể kiểm ownership đúng hai bát khi model đã loại một bát. |
| ENTRY_A01 — **reset lặp, cần STOP** | Expected A đang ở gần cẳng tay trong Đào, bên trái bát cô và cao hơn vành, tiếp motion đã chọn. Actual F0 A/tip trở lại phía Khoai, gần ngực/bên trái vùng cốc; A còn đổi thành miếng dày, nâu hơn hình mẫu. | START→F0, board01–03. T01 đã có entry lùi trái; T02 yêu cầu chống reset nhưng vẫn tái dựng state mạnh. Không có C06→C07 seam hợp lệ từ trạng thái này. Không bịa nguyên nhân route/prompt riêng lẻ. |
| GLASS01 — **MAJOR trạng thái/vai tay** | Expected cốc nâng bằng tay ngoài bên phải Đào, dưới mặt và đáy lơ lửng. Actual cốc nằm thấp sát bàn, được giữ bởi tay phía trong/bên trái của người nữ; cô dùng tay phía ngoài phải kéo bát. Về đuôi cốc đứng trên bàn, có lúc cả hai tay ở quanh cốc. | Toàn144 khung; fullF0/F64/F143, board13–18. Đây không phải cốc vào bát, nhưng mất pose nâng và đổi nhiệm vụ hai tay. |
| BOWL_ACTION01 — không phải sửa đạt ownership | Bát duy nhất bắt đầu bên phải, được bàn tay phía ngoài phải kéo sang trái khoảngF38–94, sau đó tới vùng trước Khoai. Không có tay trong từ vị trí nghỉ đi ngắn sang phải rồi nắm thành trái đúng bát. | Board05–13/fullF64/F143. Không lặp đúng kiểu “chạm bát Khoai bên trái” của T01 vì bát ấy đã mất; không ghi giả same wrong-owner event. Nhưng nhiệm vụ chuẩn bị bát trong scene đầy đủ vẫn không đạt. |
| ACTION_A01 — không thấy release, nhưng endpoint chưa đúng | Một miếng còn kẹp trên đôi đũa tay ngoài trái Khoai qua toàn nguồn; không ăn hoặc lấy miếng B. A không vào bát. Vị trí cuối vẫn lệch bên phải so bát bị kéo sang trái, không được kiểm như offer đúng trên bát Đào. | Đủ18 board/fullF0/F64/F143. “No release” không bù missing bowl, sai tay hoặc identity. Phạm vi là ảnh, không chứng nhận mọi vật lý chuyển động. |
| MOUTH01 — attribution hình phần chính | Nhân vật nữ người thật có chuỗi khẩu hình từ khoảngF25 tớiF111; Khoai phần này môi khép. | Board04–14. Không chứng nhận D06/N07/nhịp/sync; miệng của người thật không thay requirement thấy mặt Đào đúng tạo hình. |
| FOOD/DOP01 — bố cục bị tái dựng | Khung chuyển khác tỉ lệ nhân vật và bàn; đũa riêng Đào nghỉ bên phải không còn đọc được như START, đĩa nem và miếng A đổi hình/chất liệu rõ hơn. Rau/hai chấm còn trong cảnh, không thấy hơi/khói. | START/fullF0/F143 và toàn board. Không gọi scene chỉ có một lỗi mặt; nhiều dependency thừa kế đã mất ngay entry. |

## Không có prefix hoàn thành nhiệm vụ

Identity sai và thiếu bát Khoai bắt đầu ở F0, tồn tại toàn nguồn. Không có frame nào phục hồi Đào quả đào và scene hai bát đúng. Một phần đường kéo bát có thể nhìn được, nhưng thuộc nhân vật và state sai; không chọn prefix, không lấy refC08 từ nguồn này.

Trạng thái này khác T01 ở lỗi chọn bát cụ thể: T01 có hai bát, cô đụng bátKhoai; T02 chỉ có một bát nên không được gọi là sự kiện ownership giống hệt. Tuy nhiên **entry/state preservation đã không đạt qua cả hai take**, và T02 có MAJOR identity/props rõ. Root phải STOP_FOR_DIAGNOSIS, không tự T03 chỉ vì lỗi ownership mang hình thức khác hoặc ngân sách còn.

## Tầng lỗi và giới hạn chẩn đoán

Lỗi có trong native ngay entry, trước cut/encode. Prompt final vẫn gọi fictional non-human food characters / adult peach woman và giữ exact faces/two bowls/glass; model output không tuân thủ. Không kết luận do sai input/binding nếu chưa đối soát UI hoặc provenance thực. Không chứng minh các từ RIGHT-SCREEN/LEFT-SCREEN gây hóa người; cũng không chứng minh thêm nhiều câu cấm sẽ sửa.

Hướng an toàn tiếp là đóng băng nguồn/prompt/inputs và đối soát exact reference thực được chọn trên UI, route/config và provenance của đúng job; sau đó phân biệt khả năng model tái diễn giải semantic với lỗi chọn input. Phần này reviewer chỉ đề xuất kiểm, chưa thao tác browser hoặc xác minh nó. Nếu cần thay route/ref, giảm coverage hoặc tách nhiệm vụ, phải trình đổi phạm vi và quyền mới sau diagnosis; không tự chạy trả phí.

## Disposition và timing

C07T02 **NOT_SELECTED / REWORK / STOP_FOR_DIAGNOSIS**; C08 **HOLD**. Hình lỗi rõ không cần owner duyệt như candidate đã đạt. Có thể nghe source riêng nếu phục vụ diagnosis, nhưng approval tiếng không làm hình đạt hoặc chuyển tự động sang take khác.

Qua C06 hiện689 khung, còn151 khung /6,291667 giây đến rough35 cho C07–09. Vì chưa có range C07 đạt, không tính phần nguồn lỗi thành tiến độ đã hoàn thành, không tăng tốc/cắt beat để ép35 giây. Run tại lúc đọc chỉ ghi quote10/account before1033, chưa có after/debit; reviewer không đoán ledger sau run từ quote và không đối soát account live. Root lưu debit và kết luận actual khi receipt hoàn tất.
