# EP01 — Duyệt gói hoàn thiện và chuẩn bị đầu vào sản xuất

Ngày 2026-10-06. Owner **“ok đề xuất, làm đi”** sau hai quyết định tại197. Ghi nhận duyệt **A: lời ngoài hình có chủ ý + x1 mỗi đơn vị + bổ sung tối đa100 credit**, không tuyển giọng lại hoặc mở các bộ thử ba mẫu.

## Quyền hiện hành

- Spent322, cap422 (=322+100), remaining100 trước generation. Lượt này chỉ dùng ngân sách nếu nguồn tiếng và đầu vào đủ, quote actual nằm trong cap; không cấp từ account balance.
- Tám đơn vị đầu; tối đa hai lần sửa có mục tiêu trong20 dự phòng theo giả định10/lượt. Không vượt tổng100 hoặc tự mở thử nhiều hướng; forecast vượt cap phải hỏi.
- Ngoại lệ x1 chỉ cho gói hoàn thiện EP01 này. Các thử nghiệm khác vẫn theo governance08; không sửa quy tắc toàn series.
- C-v0.6/K20/D06/P02range/ảnh195 approval giữ nguyên. Offscreen không là quyền ghép lời lên mặt người nói đang khép môi. Chưa Quality/master/phát hành hoặc API mới.

## Điểm kiểm tiếng còn mở

Nguồn tiếng đã có, owner tạm chấp nhận bộ180 để dựng và cho tái dùng R01 theo168. Tuy nhiên audit183/184 chưa có kết quả nghe đúng người nói từng lượt; không suy lệnh “làm đi” thành reviewer đã nghe.

Đã trình lại bản hiện có `C:/Users/PC/Downloads/du_an_nem_bui/180_c_v06_dialogue/A03_7-luot_REVIEW.wav` và gửi một câu hỏi không chặn việc chuẩn bị: có đúng Đào–Khoai–Đào–Khoai–Đào–Khoai–Đào, giữ chất K20/D06 không. Đây không phải audition hoặc audio mới. **SIA HOLD, chưa chi Flow trước khi đóng điểm kiểm tiếng theo197.**

## Đối soát ảnh thực tế trong vòng này

Root xem START/END195, frame59 nativeP02, ENDnâng189, START/ENDchuyển và ENDđặt189, OPEN7 và hai ảnh món thật owner đã cho dùng. Không review độc lập hoặc video motion mới.

- Cặp195 đủ nguồn tham chiếu U05 trong scope approval196; vẫn chưa chứng minh Veo giữ môi khép.
- ENDnâng189 có cỡ cảnh/vị trí bát khác frame59 P02. Không ghép cứng cặp này để giả continuity. Chuẩn bị ENDnâng sibling198 từ **frame59 native** bằng skill chỉnh ảnh tích hợp; chỉ đổi pose tay/đũa/miếng nem, giữ camera/bàn/bát/món/ánh sáng.
- U06 cỡ cảnh hai thân, bát Đào đã được đỡ trong nguồn189, trong khi phản ứng195 tay còn ở cốc. Cần một nhịp bát vào vị trí nhận trước/ở đầu đổi hướng; không dùng source đang có bát để coi động tác đưa bát đã xong. U06 cần sửa START/coverage trước tạo.
- U07 ENDchuyển189 và STARTđặt là cùng file; là khóa nguồn thuận lợi, không chứng nhận chuyển động hoặc lượng nem bất biến.
- OPEN7 là cảnh rộng thấy hai mặt; không dùng trực tiếp như U01/U02 lúc người nói ngoài hình. Cần chuẩn bị khung cận món/tay có camera được khóa; không crop mặt để chữa output diễn sai.
- U03 cần nguồn trước quay về cốc; START195 đã nhìn cốc, không tự coi đó là video quay đi. U08 cần bắt đầu sau nem đã được đặt, không gắp lại chính miếng vừa trao.

## Kết quả chuẩn bị đã lưu

Đã viết [tám prompt cảnh](evidence/198/production-prompts-DRAFT.txt), có vai trò nguồn, hành động, range dựng và điều kiện điểm nối từng đơn vị. Đây là **draft**, không tám gói đều đã sẵn sàng gửi. U05 giữ nguyên prompt R2, dùng cặp195 đã duyệt; U07 phải lấy endpoint thực của U06 sau tạo, không giả mọi clip kết ở ảnh END. Bảng [input/tool state](evidence/198/input-and-tool-state.json) ghi readiness từng đơn vị.

Khung ENDnâng198 tạo bằng imagegen tích hợp, không CLI/API: `assets/references/198/END_U04_from_P02_v0.1.png`, owner copy `C:/Users/PC/Downloads/du_an_nem_bui/198_completion_production/END_U04_from_P02_v0.1.png`. PNG RGB941×1672; SHA256 `235b502f377cc293af7d5c1740901b8d90a060d069213e333c73010bcfbd76e4`. [Prompt ảnh](evidence/198/prompt-U04-END-image.txt). Root xem actual: tay/đũa/miếng nem đã nâng, chưa chạm miệng nhìn thấy; bát và chi tiết món vẫn có khác biệt do tái tạo. **Ứng viên, chưa continuity PASS**, không thay frame cuốiP02 hoặc coi ảnh mới là endpoint native. Không chạy thêm biến thể ảnh trong vòng này.

Theo hướng dẫn skill thao tác máy tính, dùng điều khiển trình duyệt để kiểm Flow, không tự động hóa cửa sổ native/login. Đã chọn x1 theo quyền mới; read-back trực tiếp **Veo3.1Lite / Khung hình /9:16/720p/8s/x1, giá10 credit**. [Ảnh cấu hình](evidence/198/Flow_x1_quote10.jpg), hash `9732cdbd3d80435e9b071f1a81bfed47b41507da62cb8588db82136e8398213a`. Account panel hiển thị154credit; không mở rộng cap100 theo số dư. UI watermark đang ON/disabled; không tắt, crop hoặc xóa. Agent không bật theo checkbox quan sát; silent fallback chưa kiểm lại vòng này. Cần kiểm đầy đủ lần gửi thực tế, không thừa kế snapshot.

Không bấm tạo, không upload nguồn mới hoặc sửa compose/prompt. Giữ tab handoff ở cấu hìnhx1; đóng bảng tài khoản bằng nút “Đóng bảng điều khiển tài khoản” sau khi click anchor/Escape không đóng, không logout hoặc đụng tài khoản. Không lưu email/thông tin đăng nhập vào hồ sơ.

Bản nghe A03_7-luot giữ18,005giây; hash `9d060627117db229e143768f465f6cddf56196d364db1200c17d93c9e88b00da`. Đối chiếu bảy hash excerpt với183 đều khớp. Đây là kiểm nguồn bytes, **không phải kết quả nghe**. Câu hỏi nghe đã gửi, chưa có phản hồi owner trong hồ sơ; không điền observed=expected hoặc speaker PASS.

Skill chỉnh ảnh dẫn đến cách làm: lấy frame cuối native làm nguồn chính, chỉ yêu cầu đổi tư thế và lưu bản mới riêng; kết quả thực tế vẫn phải kiểm thay vì tin điều kiện giữ nguyên trong prompt. Lượt này chi **0 credit Flow**, quota của công cụ tạo ảnh chưa được đối soát. Không ghi đè file gốc 185/189/191/195 hoặc tiếng 183. [Kiểm hồ sơ](evidence/198/verification.json) ghi kiểm hash, prompt R2, phép tính ngân sách và giới hạn kiểm.

## Tổng hợp

- Đã chốt: formA/x1/cap100; cap422/spent322, còn100 chưa chi; giáx1 actual10 đã kiểm.
- Giả định: tám đơn vị và dự phòng đủ; giá x1 cần kiểm trực tiếp, không bảo đảm hoàn tất.
- Còn mở: người nói thực tế; các đầu vào và điểm nối chưa đủ; chất lượng video/mix cuối.
- Tiếp: nhận kết quả nghe để đóng SIA nguồn trước paid generation; các đầu vào/điểm nối chưa sẵn sàng tiếp tục chuẩn bị đúng thứ tự, không tuyên bố đã sản xuất video cuối.

Owner folder: `C:/Users/PC/Downloads/du_an_nem_bui/198_completion_production/`.
