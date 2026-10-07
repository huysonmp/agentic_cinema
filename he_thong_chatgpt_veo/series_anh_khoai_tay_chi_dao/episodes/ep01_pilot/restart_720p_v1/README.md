# EP01 — Hồ sơ làm lại trực tiếp ở 720p

Kế hoạch236 đã được owner duyệt tại237. Đây là hồ sơ mới, không nhập footage cũ hoặc coi các approval media cũ là approval clip mới.

## Hiện trạng

- Trần dự trù được duyệt: 500 credit; đã chi: 15; còn trong trần: 485. Số dư accountcurrent sauC02:1.035.
- Account đã được owner xác nhận; project **EP01 Nem Bùi — Khoai & Đào — 720p v1** đã tạo, giữ project cũ.
- URL: https://flow.google.com/project/bcb1f53c-13b6-4719-b866-01348dfcddd6.
- Đã kiểm Omni 1.1 Flash / Ingredients / 720p / 9:16 / 10s / x1 / Agent OFF; composer trống báo 15 credit, không quote cuối của C02.
- REC238 cho quyền tự vận hành có giới hạn. REC239: owner đã nghe và duyệt K20/Orus, D06/Aoede trên nick mới. Xem `03_voices/bindings-238.json` và `00_decisions/voice-approval-239.json`; clip sản xuất chưa được nghiệm thu tiếng.
- MASTER01 v1 đã tạo/tải gốc; reviewer chặn vì chất liệu nem giống mì. V2 sửa giá0 đã đóng lỗi món. Owner239 chọn sửa khung trước C02, không chấp nhận v2. V3 và v4 mỗi bản một lượt quote0 đã tải/kiểm native; đều chưa sửa được margin rau/cốc. Dừng sinh tiếp theo ngưỡng lặp lỗi, chờ hướng xử lý. C02 chưa chạy.
- Bốn vai DIR/DOP/ACT/EDIT239 đã giao báo cáo, root đọc đầy đủ và tích hợp một khung cận vừa hai người/diễn tiết chế/dựng liên tục. Prompt239 là draft từ v2; cần rebind ảnh mới, review độc lập và finalquote.
- Công cụ dựng của account mới chưa được xác nhận đủ tính năng; mô tả Stringout Creator trong catalog không thay bằng chứng trim/arrange/linked audio/export. Xem `09_lessons/REC239_preflight_and_assembly_observations.md`.
- Sau hai lượt sửa khung, số dư UI vẫn1.050; observed debit0, quyền video500 chưa sử dụng. Reviewer static khung bị ngắt trước report, không nhận đã hoàn tất independent review v3/v4.
- REC241: owner cho phép tạo ảnhChatGPT. V5 tạo bằng built-in, đã tải/lưu và root kiểm: trọn rau/cốc, giữ F0/hai mặt, có minorlimits về margin/fidelity/ratio941×1672. Đang trình owner, chưa uploadFlow/duyệt master hoặc sinhC02. Xem `04_requests/MASTER01_chatgpt_241.json`.
- REC242 cập nhật: owner đã duyệt exactv5, checkpoint master+hai voice đóng. Đã uploadv5 và gắn riêngK20, prompt242/cấu hình720p/Ingredients/Omni1.1Flash/10s/9:16/x1/AgentOFF, quote15 đủ inputs. Reviewer độc lập refreshv5 paperpassconditional, root đọc đầy đủ.
- Scenebuilder gốc đã mở timeline trống và lưu scene8136b4bc-5020-4f7a-afd9-635f8ccf8629. Chưa video để đo trim/export thực. Đang hỏi dùng chínhC02 đầu để kiểm tích hợp hay clipcũQC riêng; chưa submit C02, không tự coi masterapproval là miễn kiểm dựng.
- REC243 hiện hành: owner chọnA. MộtC02đãsinh/tải/kiểm,REWORKhình(dođổiset/khungrộng/Đàochắptayđầu);chưaC01A. Nativevoice chưahumanaccepted. Flowtrim/exportmộtclip đãkiểmactual;output9,041667s/217frames/720×1280,giữtiếngnguồn. KhôngcoiQCexportlàfilmapproved; xem243và`07_edits/C02_flow_trim_export_243.json`.
- REC244: owner đã chấp nhận riêng tiếng của C02 T01, đúng K20, lời và nhịp. Hình T01 vẫn cần sửa; không chuyển duyệt tiếng này sang take mới. Ảnh cận vừa riêng C02 đã qua kiểm độc lập ảnh tĩnh; giữ master v5 làm chuẩn toàn cảnh.
- REC245 hiện hành: đã sinh một C02 T02 sửa bằng ảnh cận vừa, giữ lời/K20. Ba lỗi lớn T01 không lặp trong mẫu kiểm; phần Đào hé môi ở đuôi đã loại khỏi bản cắt Flow. Export 720×1280, 24 fps, 181 khung, dài 7,541667 giây, đang chờ owner duyệt hình–tiếng. Chưa mở C01A.
- Ngân sách REC245: tab tạo video ghi 1.020 sau T02, trừ 15. Sổ dự án tính bảo thủ đã dùng 30/500, còn 470. Tab mới sau đó hiển thị 1.050, chưa đối soát nguyên nhân; không suy hoàn phí hoặc tăng quyền chi. Native, bản cắt, kiểm và bài học đã lưu riêng.
- Các đơn vị: C01A, C01B, C02, C03A, C03B, C04, C05, C06, C07, C08, C09. Thứ tự sinh theo kế hoạch 236, không theo tên file.

## Hồ sơ

1. `00_decisions/plan-approval.json`: quyền và phạm vi duyệt.
2. `03_voices/recreation-blueprint.md`: chỉ dẫn gốc; trạng thái tạo thực và ID mới nằm ở `bindings-238.json`.
3. `04_requests`: chỉ dùng cho exactrequest đã chuẩn bị, không ghi giá public như quoteactual.
4. `05_native`: giữ originals khi nhận; không xóa/ghi đè media cũ.
5. `06_qc`: kết quả kiểm targethash/range/capability và findings.
6. `07_edits`, `08_delivery`, `09_lessons`: bổ sung khi thực làm, không placeholderPASS.

Giữ dữ liệu đăng nhập và screenshot account ở máy, không đưa vào Git. Số dư UI không thay trần quyền chi. `00_decisions/scoped-autonomy-238.json` thay quyền xin từng request: chỉ720p/x1/quote≤15 trong phân bổ500, dừng khi lặp cùng blocker lớn hai lần. Dự phòng110, giá cao hơn, đổi công cụ/script/giọng vẫn phải trình owner. Giữ checkpoint chất lượng ban đầu, C02, rough cut và final.
