# REC277 — Kiểm C07 T02: maker DIR / DOP / ACT / EDIT / CONT

Ngày 13-10-2026. RUN_ID `REC277_C07_T02_MAKER_ACTUAL`. **COMPLETE_PROOFREAD / SOURCE_REWORK / STOP_FOR_DIAGNOSIS / NOT_SELECTED / C08_HOLD.** Đào bị thay bằng người nữ thật ngay đầu và suốt nguồn; bát Khoai biến mất, cốc đổi tay, trạng thái A/tay đầu cảnh vẫn reset. Không có range dùng được; không T03 tự động.

## Target và capability

- Đã đọc đầy đủ `04_requests/C07_T02_prompt_277.txt`, preparation277 và run277. Exact final SHA đã tự kiểm tại preflight **`ae636235971fb36f5a31234dcb294cb91ea5d12c9231c8b046b797b8ad756ef4`**. Run lúc đọc còn `SUBMITTED_ONCE_RESULT_PENDING`; đây là snapshot trước root cập nhật nhận native, không phủ nhận file đã có.
- **Tự hash** `05_native/EP01_720_C07_T02_NATIVE.mp4`: **`c793308e55ed02f5b61fb9dfd1f4f6edaa4b3302bdb520defb108cfa5b5140da`**. Owner copy và evidence ở `C:/Users/PC/Downloads/du_an_nem_bui/277_C07_T02/`.
- Đọc đầy đủ `native_qc/native_evidence.json` và `action_all/manifest.json`. Evidence: H.264720×1280,24fps,144frames,6s hình; AAC stereo48kHz,6,016s container; full decode success. Maker không tự probe/decode lại. Manifest hash khớp native.
- Trực tiếp xem **ALL144 khung F0–143 qua đủ18 bảng ảnh**, thêm nguyên khung F0/F44/F80/F120/F143 và exact START C06 F56 `02_refs/C07_START_from_C06_T03_selected_F56_276.png`, hash đã kiểm tại preflight `69fb0e62a3a6f138a0eae622603945b248ec8d2809c8cda513dcdfdc33d00863`.
- Capability **ALL_FRAME_STILLS_NOT_AV**. Chưa nghe thực tế hoặc xem chuyển động/AV liên tục. D06/N07/single speaker/sync/âm cuối vẫn UNKNOWN/NOT_CERTIFIED. Không đọc critic T02, không dùng ASR, trình duyệt/API/credit/git, công cụ/script mới, render hoặc sửa media.
- Authority217/scoped238, approval276 và source lesson275/T01 actual đã đọc trong cùng chuỗi maker. Chỉ đánh giá actual T02; không dùng giấy GO hoặc input đúng để gọi output PASS.

## Findings theo bản gốc

| ID / mức độ | Khung / giây | Expected → observed và hệ quả |
|---|---|---|
| ID01 / **MAJOR — thay Đào bằng người nữ thật** | Toàn bộ F0–143 / 0–5,958 | Expected nhân vật quả đào trưởng thành đúng mặt/thân mẫu. Actual từ F0 là người nữ photoreal với da người, tóc nâu, tai/khuyên tai; không còn đầu/thân quả đào. Khoai vẫn hoạt hình khoai tây. Đây là đổi identity/style toàn cảnh, không chỉ lệch nét mặt, không có prefix đúng để tận dụng. |
| PROP01 / **MAJOR — thiếu bát Khoai** | Toàn bộ F0–143 | START có hai bát riêng rỗng. Actual chỉ một bát ở phía nữ; vùng bát riêng bên trái trước Khoai trống ngay F0 và suốt nguồn. Không thể chứng nhận “LEFT bowl untouched and fixed”; nó đã biến mất, không chỉ bị tay che. Hai đồ chấm vẫn có, không được đổi nhãn thành bát cá nhân. |
| HAND01 / **MAJOR — cốc đổi tay, bowl blocking khác nguồn** | Từ F0, giữ suốt nguồn | START Đào cầm cốc bằng tay ngoài screen-right, tay trong screen-left nghỉ bên trái bát cô. Actual người nữ cầm cốc bằng tay trong screen-left; tay ngoài screen-right nắm/dịch bát. Final cấm hand swap và yêu cầu tay trong chuẩn bị bát. Không gọi động tác dịch một bát ở bên phải là hoàn thành blocking đúng trong khi hai vai tay đã đảo và nhân vật đổi. |
| ENTRY01 / **MAJOR — A/tay reset, lặp loại lỗi T01** | START→F0; F0–23 / 0–0,958 | START A/tips đã ở cạnh cẳng tay trong Đào, gần mép trái bát cô và cao hơn vành. Actual F0 tay Khoai kéo về phía mình, A trước ngực/phía mình; sau đó mới tiến nhẹ sang. Không tiếp một đoạn ngắn từ pose đang chuyển F56. T01 cũng có reset vị trí đầu; chỉ dẫn neo mới chưa giữ được source entry. Không nhận điểm nối đạt hoặc tốc độ seamless từ ảnh tĩnh. |
| BOWL02 / **MAJOR — không giữ bát trong vùng cá nhân Đào** | Nắm/dịch khoảng F40–96 / 1,667–4s; kết F97–143 | Bát duy nhất xuất phát bên nữ, được tay ngoài cô kéo xa sang trái tới ngay trước tay trong Khoai. Final chỉ slide nhỏ và vẫn ở nửa phải trực tiếp trước Đào. Full F80/F120/F143 bát ở gần giữa/phía Khoai; không có bát riêng Khoai để phân biệt ownership hợp lệ. **Không tự gọi đây là cùng lỗi “cô lấy bát trái của Khoai” như T01**, vì bát Khoai đã mất ngay entry. Lỗi T02 là missing bowl/hand swap/slide quá xa, không đủ bằng chứng bowl identity giống T01. |
| GLASS01 / **MAJOR trạng thái inherited sai; không cốc vào bát** | Toàn bộ nguồn, rõ F120/F143 | Cốc không nằm trong bát, nhưng đổi sang tay trong và được giữ thấp gần mặt bàn, không đúng pose nâng ngoài phải dưới mặt của reference. Ở cuối đáy cốc sát mặt bàn. Ảnh không đủ chứng minh chính xác thời điểm đặt hẳn; không bịa contact nếu chỉ projection. Hand swap và pose thấp đã đủ sai yêu cầu. |
| A01 / không thấy release/eating; recipient-ready HOLD | Toàn bộ F0–143 | Có một miếng vẫn kẹp trên đôi đũa tay ngoài trái Khoai; không thấy ăn/thả/rơi/nhân đôi hoặc thêm đôi đũa. A ở mức trước ngực, xa miệng. Bát được kéo dưới/gần A nhưng do identity/props/blocking sai, không certify held offer đúng nguồn. |
| MOUTH01 / nữ có khẩu hình; tiếng chưa kiểm | Nữ khoảng F25–111 / 1,042–4,625; Khoai kín môi toàn nguồn | Khoai không có nhóm nói rõ. Người nữ có nhiều khẩu hình và nhìn Khoai; không xác nhận câu N07 đúng một lần, D06 hoặc sync. Miệng đúng vai nữ không cứu việc Đào đã bị thay người. |
| DOP/FOOD01 / continuity layout sai; không khói | Toàn bộ nguồn | Vẫn khung hai người và ánh sáng quán ấm, rau trước trái, đĩa nem/hai đồ chấm/watermark. Một đồ chấm phải sát/cắt mép; tỷ lệ món, người và bàn thay so START. Không thấy khói/hơi nóng hoặc cut trong nội nguồn. Không nhận toàn serving layout giữ đúng vì bát Khoai thiếu và nhân vật/pose đổi. |

## DIR / ACT / EDIT disposition

Lỗi identity đã có từ F0 nên **không có candidate prefix hoặc range hoàn thành nhiệm vụ**. Không thể cứu bằng cắt trước bát trượt xa, che mặt/cận món hoặc dùng giọng Đào gắn lên người nữ khác. Những frame tay/bát có vẻ vật lý hợp lý không được chọn riêng làm C07 rồi giả nhận whole shot đạt; việc này còn thay coverage/continuity và cần quyết định mới.

Hành động nhìn/nói rồi đưa bát có trong source, nhưng chủ thể, hand assignment, số bát và điểm vào đều sai. Đánh ACT về hình không cần hạ yêu cầu thành “nữ nào cũng được” hoặc gọi giọng nữ đúng từ preset. Audio/AV chưa nghe và approval T01 chưa có; không tự chuyển voice approval clip khác.

151 khung =6,291667s còn lại tới35 cho C07–09 vẫn là giới hạn, không đo selected range của T02. Full6s sẽ chỉ còn7 khung cho C08–09, nhưng T02 đã không chọn vì lỗi nguồn chứ không vì timing. Không ép bỏ nhận/thả/kết B hoặc dùng clip lỗi để vừa35.

## Nguyên nhân và quy tắc dừng

Đã chứng minh lỗi ở native trước cắt/encode: nhân vật bị thay, bát thiếu, hand swap và A entry reset. Final đã khóa đúng reference/identity/hai bát/tay/cốc/entry; source không giữ. Chưa chứng minh lý do model sinh người thật: mật độ quan hệ trái/phải, ngữ nghĩa “woman”, binding ảnh/route hoặc variation đều cần evidence riêng; **không kết luận input ảnh bị gỡ, preset sai hoặc thay tool là cách chữa chắc chắn** từ ảnh output.

T01 và T02 đều còn lỗi reset A/tay ở đầu cảnh theo maker findings, nên **STOP_FOR_DIAGNOSIS** dưới scoped238/run277. T02 còn các MAJOR mới; không đổi tên wrong-bowl counter để lấy quyền T03. Maker không tự cấp retry hoặc bỏ checkpoint. Root đọc critic và đối soát findings/counter hiện hành; dù bất đồng severity entry, source T02 vẫn NOT_SELECTED và không có quyền tự sinh tiếp từ report này.

## Kết luận đã proofread

**SOURCE_REWORK / STOP_FOR_DIAGNOSIS / NO_SELECTED_RANGE / C08_HOLD.** Đào thành người thật, bát Khoai mất, tay cốc/bát đảo, A/tay entry reset và bát bị kéo quá xa. Không giả gán lỗi chọn bát Khoai ở T01 sang T02; ghi đúng từng observed failure. Chưa audio/AV/sync PASS. Root phải chẩn đoán theo exact source/input/live provenance và trình quyết định mới nếu cần; **không T03 tự động**, không sửa/xóa bản gốc hoặc truyền endpoint sai xuống C08.
