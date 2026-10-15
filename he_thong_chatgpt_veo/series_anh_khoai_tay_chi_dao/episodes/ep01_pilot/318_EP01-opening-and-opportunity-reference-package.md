# REC318 — Khung mở đầu và chuỗi tranh thủ đã chuẩn thành một gói

Ngày 15/10/2026. **Đã tạo ảnh, kiểm tĩnh và kiểm Flow trực tiếp; không video/voice mới hoặc credit Flow phát sinh.** Owner yêu cầu tiếp tục nhanh, không hỏi nhiều. Root tự xử lý các bước chuẩn bị trong phạm vi đã chốt, chưa suy thành quyền sinh trả phí, thay lời hoặc mở dự phòng.

## 1. Bốn ảnh dùng để đối chiếu — không trình cả tám bản ngang nhau

| Thứ tự kể | Ảnh cần xem | Trạng thái và nhiệm vụ |
| --- | --- | --- |
| Mở đầu R01 | [R01-start v5](restart_720p_v1/02_refs/coverage_completion_318/R01_START_v5_CANDIDATE.png) | Hai bát rỗng, cốc trên bàn ngoài bát Đào, hai đôi đũa đang nghỉ; Khoai nhìn món, Đào nhìn anh. Đủ đĩa rau/hai chén chấm/cốc trong khung sau sửa bố cục |
| Trước tranh thủ R04 | [R04-entry](restart_720p_v1/02_refs/coverage_completion_318/R04_ENTRY_v1_CANDIDATE.png) | Khoai vừa đáp tỉnh, nhìn Đào; A chưa được lấy. Cốc/bát/đũa còn trên bàn như trạng thái trước hành động |
| Cơ hội R04 | [R04-mid](restart_720p_v1/02_refs/coverage_completion_318/R04_MID_OPPORTUNITY_v1_CANDIDATE.png) | Đào nhìn ra phố về phía ngoài, tay ngoài cầm cốc; Khoai đã giữ một phần A thấp phía mình. Tay nghỉ không đỡ bát cô, hai bát vẫn rỗng |
| Đào nhìn lại R04 | [R04-exit](restart_720p_v1/02_refs/coverage_completion_318/R04_EXIT_v1_CANDIDATE.png) | A vẫn kẹp; Đào đã nhìn về Khoai. Chưa ăn/cho/thả; bát Đào chưa nâng. Từ đây sang xác nhận/bắt gặp, không diễn lại một lần quay đầu |

Đây là **ứng viên do root kiểm tĩnh**, chưa phải owner duyệt ảnh mới, nguồn production hoặc native entry/exit. R04-mid được tạo sau exit để chỉ đổi trạng thái đầu/ánh nhìn Đào; thứ tự sinh không phải thứ tự câu chuyện. Không cắt nối bốn still rồi gọi đã có chuyển động.

Khung mở rộng hơn T-caught cũ để lấy đủ bàn; mặt vẫn đủ lớn trong ảnh tĩnh, nhưng nền phố còn khá nhiều ở phía trên. Không hủy hướng cận K/D đã duyệt ở R02/R03/R06 hoặc trở lại khung đôi cố định cả tập.

## 2. Kiểm đã làm và lỗi không được tự bỏ qua

Root xem từng output được trả về, đối chiếu vật thể và chủ thể. Đã lưu nguyên byte tám ảnh vào project, kèm tám prompt và [manifest nguồn/hash/kích thước/thứ tự input](restart_720p_v1/02_refs/coverage_completion_318/reference_manifest_318.json). Không sửa pixel local, crop/scale hoặc ghi đè ảnh cũ.

- R01 v1/v2: cốc/rau bị cắt mép. Dừng nhánh sửa chung sau lặp lỗi, không gọi là master đạt.
- V3 đổi chiến lược sang vị trí hai vật thể cụ thể từ v1: cốc vào được khung nhưng mép rau còn cắt; không chọn. Đây là sửa khoảng hở trong cùng vị trí tương quan, không đưa rau ra bàn khác để dọn đường tay.
- V4 dựng lại khung thiết lập rộng hơn, chỉ dùng ảnh cũ theo vai nhận diện/state: đĩa rau/đồ chấm vào khung nhưng cốc lại chạm/cắt biên. Giữ làm intermediate, không chọn như master.
- V5 chỉ yêu cầu dịch một cốc vào trong; cốc có khoảng hở, rau/đồ chấm còn trong khung, đúng hai bát rỗng và hai đôi đũa nghỉ. Có redraw ngoài vùng yêu cầu; không gọi pixel lock hoặc mọi vị trí giữ tuyệt đối.
- Entry chưa A; mid/exit có đúng vai cầm A/cốc, đôi đũa Khoai không còn nằm thêm trên bàn; đũa Đào vẫn nghỉ. Đầu cầm dày ở tay Khoai, đầu gắp thuôn ở A theo quan sát tĩnh. Chưa kiểm ngón tay/lực kẹp/đường đũa bằng video.
- Hai bát trống trong cả cụm; không có B, không chuyển A vào miệng/bát hoặc trả về đĩa. Cốc không nằm trong bát. Không thấy khói ở món trong các ảnh mới.
- Món có lớp hạt/thính và phần mảnh hơn footage C04 cũ; vẫn có sắc hồng và độ đều của vật liệu AI, **không nghiệm thu chính xác món chỉ nhờ nhìn tĩnh hoặc approval tư thế**. Tỷ lệ/lượng trên đĩa có biến thiên giữa các redraw, chưa chứng minh bảo toàn lượng.
- V1–v3:941×1672; v4:940×1672; v5 và ba ảnh R04:940×1673. **Không ảnh nào đúng tuyệt đối9:16**, chưa gate định dạng720×1280. Không ép kéo giãn để gọi đạt.

### Các điểm nối còn hở sau gói này

1. **R01→K-entry:** có hướng gaze xuống, nhưng cỡ cảnh/hình học và native exit thật chưa kiểm. Ảnh master đầu không thay endpoint sau “Khoan”.
2. **R03→R04:** entry mới không tự là frame cuối của cận K mới chưa tồn tại. Đạo cụ ngoài khung ở cận vẫn tồn tại trong thế giới cảnh.
3. **R04-entry→mid→exit:** thiếu chuyển động actual: Đào chuyển chú ý/nhấc cốc, Khoai lấy A, rồi cô nhìn lại. Không có chứng cứ tốc độ, cơ hội hoặc timing chỉ từ ba still.
4. **R04-exit mới→T-confirm315:** khác cỡ mặt/bàn, render món và lượng A; không được dùng cut thay cho giải quyết seam. R04-exit mới không phải nativeC04F143 và không có quan hệ range với F123 của rough312.
5. **Cụm cũ R05→R09:** bộ318 không tự thay chất liệu/khung của những reference315/316 đã duyệt. Nếu muốn áp vật liệu mới cho chúng phải bảo toàn đúng pose đã chốt và kiểm lại phạm vi thay đổi; không chuyển approval sang ảnh mới chưa kiểm.

Không có báo cáo agent phản biện độc lập mới; root không gán các nhận xét này thành agent/AV PASS.

## 3. Flow đã kiểm trực tiếp — giữ tiếng đã chọn, không tự hứa chức năng

Đã mở đúng project `EP01 Nem Bùi — Khoai & Đào — 720p v1`, tài khoản `cutebabyshop2026@gmail.com`, tierPRO, trên trình duyệt tích hợp. [Ảnh bằng chứng hai saved voice](restart_720p_v1/06_qc/flow_live_318/saved_voices_UI_318.png) và [sổ quan sát chép từ output giao diện thực](restart_720p_v1/06_qc/flow_live_318/observations_318.json) đã lưu. `saved_voices_AX_318.txt` chỉ chứa diff nút nghe trước ở lần đọc sau, **không phải full panel voice**; không dùng nó một mình để chứng minh mô tả preset.

**Quan sát được:**

- Bộ chọn Thành phần có mục Giọng nói; hai saved voice `EP01_Khoai_K20_Orus_720p_v1` và `EP01_Dao_D06_Aoede_720p_v1` vẫn hiện trong project, mô tả tiếng Việt Hà Nội miền Bắc và sắc thái đã chọn.
- D06 hiện ID trong field `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`, có hội thoại mẫu và hướng diễn. Chỉ đọc, không sửa tên/nội dung, không bấm nghe trước, thêm vào prompt hoặc tạo tiếng.
- Menu nhóm model liệt kê Omni1.1Flash và Veo3.1Lite/Fast/Quality. Không khẳng định model nào đang chọn chỉ từ thứ tự menu.
- Cấu hình ban đầu Frames/720p/9:16/8s/x1/AgentOFF. Tạm xem Ingredients để kiểm voice, rồi khôi phục Frames; [AX khôi phục](restart_720p_v1/06_qc/flow_live_318/restored_settings_AX_318.txt). Không đính kèm input/prompt hoặc submit.
- UI hiển thị12credit cho cấu hình trống8s tại lúc kiểm; **không phải quote cho request mới có đủ input**, không phải giá mọi route và không debit. Chưa mở thông tin balance nên không cập nhật số dư live.
- Danh mục công cụ có Stringout Creator với mô tả ghép clip và các công cụ khác; không chạy chúng. Danh mục thành phần/tệp đã xem chưa cung cấp bằng chứng về điều khiển khẩu hình bằng WAV cũ.

**Kết luận có giới hạn:** saved voice còn đó là cơ sở dùng đúng K20/D06 trong một request native có kiểm; không chứng minh waveform mới giống tuyệt đối hoặc khẩu hình đạt. Route nhận exact WAV để điều khiển miệng mới vẫn **UNKNOWN**, không viết thành “Flow không hỗ trợ” hay “đã hỗ trợ”. Không dùng chồng WAV lên miệng khác để thay kiểm AV, không tạo lại hàng loạt voice.

Phương án làm việc: giữ audio/take đã duyệt làm đối chứng; footage giữ được thì giữ cùng tiếng/range. Cảnh nói cần hình mới phải có route rõ và gate một speaker/đúng giọng/đủ câu/khẩu hình, kèm quote và quyền chạy riêng. Các approval K20/D06 trước vẫn đúng bản cũ, không được suy sang take mới.

## 4. Việc tiếp theo — gom việc, không hỏi lẻ

- Tích hợp bốn ảnh này vào kiểm điểm nối toàn tập; ưu tiên R04-exit→T-confirm và việc giữ cùng vật liệu món qua các cụm. Không tạo thêm agent thay cho giải quyết nguồn/khung cụ thể.
- Chuẩn camera counterpart/đầu–cuối của các shot nói theo reference đã chốt và phương án voice có bằng chứng; không quay lại hỏi tên/giọng/quan hệ/câu thoại.
- Gộp những thay đổi hình mới và phương án chạy thành một gói production preflight khi đủ đầu vào, thay vì xin duyệt từng cử chỉ. Nếu cần đổi quyết định đã khóa, quote/bucket hoặc mở chi phí thì trình đúng một gate có nội dung rõ.
- Chưa có EDL30 mới. Baseline vẫn35s; bộ ảnh này không chứng minh rút được5s hay chuyển động mới vừa slot. Không đổi lời, tăng tốc hoặc bỏ phản ứng để báo đủ30.

### Tổng hợp vòng318

- **Đã xác định:** có khung mở đầu và bộ entry/mid/exit cho tranh thủ; saved K20/D06 được xác minh tại Flow.
- **Đã chốt giữ:** mọi quyết định317 và trước đó; root chỉ chọn ứng viên, không tự duyệt ảnh mới hoặc trả phí.
- **Giả định:** khung thiết lập rộng hơn và bộ state này có thể hỗ trợ đường kể; chưa dự báo native thành công hay giảm số lượt.
- **Còn mở:** seam giữa bộ318 và315/316, likeness/texture cuối, format, motion/voice/AV và timing30.
- **Bước tiếp:** xử lý cùng nguồn và cặp nối trước production request; chưa cần câu trả lời mới của owner ở vòng này.

Built-in imagegen theo skill: tách vai ảnh đầu vào, sửa có mục tiêu, chuyển từ bố cục chung sang từng đối tượng và lưu prompt/lineage. Tám output nhận được; một callv5 bị ngắt không trả ảnh, đã kiểm không có file mới trước khi gọi lại. Không đếm lần bị ngắt thành output đạt. Flow chi **0**; không CLI/API mới, không video/voice/EDL mới, không chuyển ngân sách. Sổ dự án gần nhất vẫn279/500/còn221, dự phòng110đóng, chưa refresh balance live.

Theo `.gitignore` dự án đã chốt14/10, PNG/JPG/QC media không đưa lên Git. Ảnh vẫn lưu đủ trong workspace và gói owner; Git lưu tài liệu/prompt/manifest/hash và quan sát chữ. AX text đã chuẩn khoảng trắng cuối dòng khi lưu hồ sơ, không tuyên bố raw byte export; screenshot là ảnh UI thực chưa chỉnh.
