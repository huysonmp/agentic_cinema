# REC286 — Maker: kết quả sửa món có output nhưng vượt phạm vi food-only

Ngày 13-10-2026. **ACTUAL_OUTPUT_DIAGNOSIS / VISUAL_REWORK / NOT_SELECTED.** Đây là maker diagnosis theo DIR/DOP/ACT/EDIT, không phản biện độc lập hoặc nghiệm thu. Không browser/API/paid retry/media edit/cài công cụ/git trong task này.

## 1. Đúng target và phạm vi kiểm thực

- Output: `C:/Users/PC/Downloads/du_an_nem_bui/286_FOOD_EDIT_PROJECT_PROMPT/EP01_720_C05_C06_FOOD_EDIT_T01_NATIVE_286.mp4`.
- SHA-256 kiểm trực tiếp: `4703fb9b34abbb63144364cb388aa4d9921e06d7b7c597f2da77d04a7299e583`.
- Nguồn đối soát: `C:/Users/PC/Downloads/du_an_nem_bui/276_C05_C06_JOIN/C05_C06_5p125S_JOIN_QC_NOT_FINAL.mp4`, SHA `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`.
- Đã đọc request REC286, approval một lượt cap20, exact draft `04_requests/C05_C06_food_only_edit_DRAFT_283.txt`, native evidence output và evidence source. Request ghi route project composer Omni 1.1 Flash Ingredients 720p 9:16 x1, Agent OFF, source + START; nguồn tiếng/AV approval không tự chuyển.
- Đã trực tiếp xem tám board `native_qc/full16_01.png`…`full16_08.png`, chứa liên tiếp toàn bộ F0–F123; bốn ô trống cuối là padding, không là khung video. Đây là **FULL_FRAME_CONTACT_SHEETS**, không phát video AV liên tục.
- Xem thêm full-resolution output F0, F66, F71, F72, F122 và nguồn F0, F66, F71, F122 trong `encoded_qc/all_native_frames/`; PNG đánh số F+1. Xem lại approved START và hai ảnh thật `nembui.jpg`, `z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg`.
- **Không nghe actual audio, không chứng nhận giọng/lời/lip-sync.** Audio stream tồn tại không thay kiểm nghe. Source REC277 human AV approval giữ đúng source, không gán cho output.

## 2. Kết quả ngắn

Flow đã trả một file native 720×1280 có 124 khung; route thực thi này tạo được output. Món trên đĩa và phần A rõ ràng đã đổi khỏi lát đặc thành thành phần rời phủ thính. Tuy nhiên output **đồng thời thay trang phục Đào và tự đổi hậu cảnh/camera ở giây 3**. Hai thay đổi này nằm ngoài yêu cầu, đã đủ để không thay source trong EDL hiện hành.

Không cần dùng lỗi giọng chưa kiểm để bác file: lỗi hình đã có bằng chứng. Không coi kỹ thuật 720p/full decode hoặc cải thiện món là cách bù MAJOR continuity.

## 3. Findings theo frame/timecode

| ID / scope | Expected | Observed trực tiếp | Severity / hệ quả |
| --- | --- | --- | --- |
| M286-01 — DOP/canon trang phục | Giữ áo trắng trước ngực Đào và outfit source; không thay vùng ngoài món | Tại output F0 / 0,000s, Đào có yếm/tạp dề xanh phủ ngực với quai/nút vai; source F0 áo trắng và cúc áo. Approved START cũng áo trắng, không yếm. Yếm xanh còn qua toàn tám board | **MAJOR**, không chỉ đổi food material; nối vào cảnh trước/sau sẽ mất continuity trang phục |
| M286-02 — DOP/EDIT bối cảnh–camera | Giữ phố/source, framing/light và đúng sequence/cut, không dựng camera/background mới | Output F71 / 2,958333s còn phố cũ. Tại F72 / 3,000s, hậu cảnh chuyển sang phố khác với hai đèn lồng lớn phía trên, dây ngang và người đi giữa đường; vị trí bàn/plate/bowls theo khung cũng khác. Đổi này còn đến F122. Source F71 và F122 giữ phố/đèn/camera cũ. Board05 row3 mở tại F72 xác nhận đổi rõ | **MAJOR**, phát sinh một đổi shot/setting ngoài food; không được coi cut source F66 / 2,75s đã bảo toàn đúng chỉ vì output vẫn có hai đoạn |
| M286-03 — EDIT duration | Source 123 khung / 5,125s, giữ exact timing | Native evidence: 124 khung / 5,166667s; thêm một khung so nguồn, audio duration 5,184s so source 5,125s | **TIMING_REWORK / cần đối soát**, +1F không tự chứng minh speech bị đổi hoặc câu bị thiếu; không tự trim khi chưa biết extra frame nằm đâu và AV có ảnh hưởng gì |
| M286-04 — FOOD/A appearance | Sửa slab thành một phần gắp nhỏ rời, cùng vật liệu đĩa | Full-res F0/F66/F122 có các dải thịt/bì phủ thính trên tips, không còn một lát chữ nhật đặc như source; đĩa có các thành phần rời tương tự hướng START/ảnh thật. Không thấy khói trong full-frame boards | **IMPROVEMENT OBSERVED, chưa FOOD PASS**: đối tượng đã sửa đúng hướng, nhưng shape/volume/frame continuity và owner/critic appearance chưa tự đóng |
| M286-05 — ACT/props | Giữ A ở đũa chưa thả, cốc nâng tay ngoài, hai bát riêng, mặt hiện trong đối đáp | Tám board có A trên tips, không quan sát thấy feeding, pickup lại hoặc deposit; cốc vẫn nâng, không vào bát; hai bát còn. Hai mặt hiện. Đào có chuỗi miệng nói ở phần đầu, Khoai ở phần sau | **OBSERVED VISUAL SUPPORT**, không actual listening/lip-sync/canon PASS. Miệng hoạt động đúng vùng thời gian khái quát không chứng minh từng phoneme hoặc đúng giọng |

Khung toàn bộ được đọc ở độ lớn contact sheet, các MAJOR được xác minh full-resolution. Không suy rằng mọi chi tiết mặt/ngón tay/powder trong tất cả 124 khung được kiểm pixel-exact. Không có đo contour/optical flow hoặc frame alignment chuyên sâu trong task này.

### Evidence path cho hai MAJOR

Với base output `C:/Users/PC/Downloads/du_an_nem_bui/286_FOOD_EDIT_PROJECT_PROMPT/native_qc/all_native_frames/`:

- `00001.png`: yếm xanh ngoài scope và food mới, so source `276_C05_C06_JOIN/encoded_qc/all_native_frames/00001.png`.
- `00067.png`: output F66 vẫn phố cũ, yếm xanh vẫn tồn tại; so source cùng frame và source EDL cut F66.
- `00072.png`→`00073.png`: output F71→F72 chuyển phố/camera rõ ràng.
- `00123.png`: output F122 giữ phố mới/yếm mới; source F122 tại `00123.png` vẫn phố cũ và áo trắng.

Đây là bằng chứng native output, không ảnh redraw hoặc thumbnail UI. Platform star còn trong các full-resolution frame; không đề nghị xóa dấu để sửa lỗi hình.

## 4. DIR/DOP/ACT/EDIT integration

**DIR:** Ý đồ vẫn nhận ra hai người đối đáp trong lúc A được giữ; output chưa chuyển thành cảnh nhận–bỏ hoặc đút ăn. Như vậy không cần đổi lại câu chuyện để chữa một phép sửa vật liệu thất bại về giới hạn. Beat REC281 đưa bát–bỏ nem vẫn chưa được sản xuất/duyệt từ file này.

**DOP:** Failure chủ yếu là phạm vi biến đổi vượt hai vùng món. Yếm xanh ở ngực không hề có trong source hoặc approved START; không thể quy đơn giản là copy outfit START. Việc background đổi ở F72 cũng không được yêu cầu và không cần thiết để thay texture thức ăn. Không có cơ sở chốt hai lỗi do một keyword riêng hoặc do backend cụ thể.

**ACT:** Bằng chứng still hỗ trợ cốc/bát/A và vai nói–nghe khái quát; chưa thấy release sớm trong boards. Không được dùng các điểm này để nhận biểu cảm/khẩu hình/voice giống tuyệt đối. Source nghe/AV giữ có điều kiện trên source cũ; output cần nghe và sync thật nếu muốn xét thêm, nhưng lỗi visual đã chặn chọn.

**EDIT:** Source join có internal cut F66; output phát sinh thay hậu cảnh tại F72, nên không đáp ứng bảo toàn source shot/cut như hợp đồng. Duration lệch thêm một khung cũng mở range/AV mapping mới. Không tự sửa bằng bỏ các frame sau 3s, vì đó là phần lời/diễn Khoai và hành động cuối đã được chọn. Không tự chọn riêng prefix phần đầu vì yếm ngoài scope đã có từ F0.

## 5. Bóc layer — điều biết và điều chưa chứng minh

1. **Authority/input:** Source/hash/range và appearance START đã khóa; input có hai speaker/cut và still nguyên cảnh với pose khác, rủi ro preflight đã nêu. Authority ảnh không cho đổi outfit/setting.
2. **Prompt:** Exact draft yêu cầu giữ outfit, street setting, camera/light, hai-shot cut, duration/audio; không chỉ nói chung “food edit”. Vì vậy lỗi không phải chưa viết yêu cầu bảo toàn các hạng mục này. Prompt bảo toàn bằng văn bản vẫn không là kiểm soát vùng cứng.
3. **Route/output:** File nhận đã biến đổi nội dung ngoài vùng món. Dữ liệu cho thấy route này chưa chứng minh bảo toàn đủ để triển khai hàng loạt. Không suy ra backend có mask hoặc thực sự chỉ chỉnh local; cũng không khẳng định tất cả video edit sẽ luôn thất bại.
4. **QC/selection:** Phải giữ finding M286-01/02 mở và không thay source. Nếu chỉ kiểm “món đẹp/720p/có bát/không khói” thì lại lọt lỗi ngoài scope. Bộ board/full-res đã ngăn bước đó trong lần này.
5. **Khác REC284:** REC286 chạy qua project composer và có output không đóng nguyên nhân lỗi request/editor trước tại REC284. “Route này chạy được” khác “đã biết vì sao route cũ lỗi” và khác “media đạt”. Cần giữ issue kỹ thuật284 riêng với issue preservation286.

Giả thuyết làm việc: đây là phép tái dựng có điều kiện, không chỉnh vật thể pixel-locked, nên có thể trôi các vùng không được yêu cầu đổi dù prompt cấm. Bằng chứng output hỗ trợ nhận xét phạm vi drift, **không xác minh thuật toán/backend hoặc tính tất yếu**. Không hứa thêm một negative prompt sẽ sửa hết.

## 6. Quyết định tiếp theo an toàn — không paid retry

- Giữ native source276/approval277 và native output286 riêng; không ghi đè source, không update EDL/approval thành PASS. Báo cáo này đề xuất **VISUAL_REWORK / NOT_SELECTED** để root/critic tích hợp.
- Một lượt owner cho phép đã dùng. Budget/debit thực chờ root đối soát tài khoản; maker không suy đã chi đúng20 chỉ từ quote. Không tự chạy lần2, mở reserve hoặc đặt thêm quota.
- Chốt với owner mức bắt buộc giữ source/canon. Khuyến nghị vẫn giữ outfit/setting/acting/audio/cut đã duyệt; không nhận các đổi ngoài scope làm canon mới chỉ để giữ food tốt.
- Nếu tiếp tục nghiên cứu route, trước paid action phải có một cơ chế giới hạn vùng/refs rõ hơn hoặc một phương án chia đúng source shot có giá/rủi ro/gate cụ thể. Không tự coi “crop ingredient món” hay tách shot là đã được phép, sẽ thành công hoặc giữ tiếng; phần A chuyển động/occlusion vẫn khó. Phương án mới cần root/critic và owner duyệt scope/cap riêng.
- Không dùng revoice/mute/lồng lời trên mặt kín, giấu mặt, cận đĩa che đối đáp hoặc loại nửa cảnh để hợp thức hóa. Local sửa vùng áo tĩnh trước đây không chứng minh local composite thức ăn/tay động; không viết script mới hay hứa patch động từ tiền lệ đó.
- Ngay cả một sửa C05→C06 sau này đạt cũng không đóng food dependencies các cảnh còn lại hoặc seam vào nhịp nhận–bỏ. Không sản xuất cả chuỗi trên route này trước khi có bằng chứng preservation đủ.

Đã xác định: thực thi có file, món tốt hơn về hướng hình thái, hai lỗi ngoài phạm vi rõ và thời lượng thêm 1F. Quyết định maker đề nghị: không chọn output hiện hành, không tự retry. Giả định chưa chứng minh: điều kiện tốt hơn có thể giảm drift, chưa có tỷ lệ đạt. Còn mở: critic, kiểm nghe/sync nếu root cần, debit thực và lựa chọn route sửa tiếp. Bước tiếp theo: root đọc lại/đối soát findings, trình owner lỗi và lựa chọn mới có giới hạn; không trả phí từ báo cáo này.
