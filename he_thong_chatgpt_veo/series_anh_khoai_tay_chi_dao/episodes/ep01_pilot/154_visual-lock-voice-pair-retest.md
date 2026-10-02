# Thử lại khóa hình ảnh với cặp giọng đã chọn

Ngày 2026-10-02. Owner trả lời “ok” sau kết quả 153 và bước tiếp khóa hình/món. Ghi nhận cho tiếp tục thử, không suy thành nghiệm thu giọng V01. Giữ ngân sách thử, không Quality/release.

## Thiết kế thử

Giữ ảnh OPEN7, hai preset K20 Orus `fb1188da-e6c8-4156-9bba-0576c01a8da6` và D06 Aoede `0ce1551e-e74b-481c-bb9e-d31e04f8b352`; đã đọc ID/performance actual khi thêm lại compose. Giữ thoại, diễn mặt/tay nghỉ, camera, route Omni 1.1 Flash/Thành phần/9:16/360p/8s/x3, quote18. Khoản thử còn152 trước submit; số dư652 từ lượt153.

Đã xem ảnh OPEN7 local và kiểm khung bàn ăn đã duyệt tại78. OPEN7 là nguồn diagnostic, không canon sản xuất mới. Không thêm ảnh/preset khác, không sửa kịch bản hoặc tạo thêm claim. Dùng skill computer-use cho UI.

## Delta prompt actual so với153

Giữ toàn bộ prompt153, chỉ thay hai đoạn mô tả hình bên dưới. Đây là sửa một nhóm hình ảnh (nhân vật, món, đạo cụ), không thử một biến/từ đơn lẻ; không kết luận nhân quả riêng nếu cải thiện.

Thay đoạn bắt đầu “Preserve the adult potato man…” bằng:

```text
Visual identity: the supplied image defines the entire scene. Khoai on the left is an adult male 3D anthropomorphic POTATO character: his head and body are an elongated golden potato with speckled potato skin, thick eyebrows and the exact dark jacket and cream shirt shown. Dao on the right is an adult female 3D anthropomorphic PEACH FRUIT character: her head is a round pink-orange peach with a peach crease, brown stem and green leaf, large brown eyes and eyelashes; keep the exact cream blouse, green skirt and pink waist ribbon shown. Animate these same two fruit-and-vegetable characters in the same stylized 3D scene, with their original faces, proportions and seated positions. The supplied evening street-side eatery, camera composition, table and props remain identical.
```

Thay “The Nem Bui dish is served cool, matching the image.” bằng:

```text
The central ceramic plate holds the exact loose mound of fine pale-golden shredded pork and pork-skin strands dusted with roasted rice powder shown in the supplied image, served cool. Keep its loose shredded texture and irregular mound. Preserve the separate green leaf plate, both dipping saucers with red chilli slices, two bowls, wooden chopsticks resting on the tabletop, and water glass in their original positions.
```

Không thêm câu cấm hơi do lịch sử lỗi153/139 chưa có kết luận nguyên nhân. Chỉ tiếp tục mô tả món nguội. Câu “no picking up food, no eating or feeding” của probe153 giữ nguyên; không phải thay hành động của tập chính.

## Gate

Chờ submit/kết quả actual. Kiểm đủ ba bản, download file thật, decode/ASR và khung hình. Đối chiếu tạo hình Đào, khuôn mặt, món dạng ụ sợi, rau/chấm/bát/đũa và bối cảnh với OPEN7. ASR không nghiệm thu accent/voice identity/lip-sync; owner nghe vẫn là gate. Không tự mở Quality chỉ vì một tiêu chí tốt hơn.

## Kết quả actual

Đã submit một lần, tạo/tải đủ ba video. Nhật ký từng output có ảnh và hai voice inputs, model Omni 1.1 Flash. Số dư live634, giảm18 từ652; khoản thử mới còn134/200. Quality riêng chưa dùng. Không retry generation, không thêm route/model khác.

| Bản | Asset ID | Source download, bytes |
|---|---|---|
| R01 | 5f48f3fa-c366-4f44-a72a-2aa1a9c2b909 | Characters_speaking_at_street_ea…_20261002213850.mp4, 883343 |
| R02 | 854383fd-5523-4adf-a00f-22052f3e2bd2 | Characters_speaking_at_street_ea…_20261002213911.mp4, 891301 |
| R03 | 0675b4b3-6937-484c-8d53-03fa454d3f7f | Characters_speaking_at_street_ea…_20261002213928.mp4, 829807 |

URL theo cùng project153 + `/edit/{asset-id}`. Folder owner `C:/Users/PC/Downloads/du_an_nem_bui/154_visual_lock` gồm R01/R02/R03.mp4, contact sheets tám khung mỗi clip, preflight/results-flow.png. Tải native trực tiếp trên tab2, đối soát file thực thành công, không chờ download event.

Cả ba 8s, 360×640, H.264/24fps, AAC48kHz stereo; full decode FFmpeg không báo lỗi. Local QC offline ở `artifacts/voice-qc/154-R01` tới `154-R03`, có hash/media/WAV/ASR. Cả ba ASR có đủ ba câu nhưng vẫn ghi “Anh gấp cho em mà”; không tự kết luận lỗi phát âm hoặc PASS lời. Root chưa nghe xác nhận voice identity/accent/biểu cảm, không gọi các agent đã nghiệm thu âm thanh.

Review trực quan từ tám khung mỗi bản:

- Cả ba giữ Khoai dạng khoai tây và Đào dạng quả đào, không thấy Đào thành người ở các khung kiểm; nhóm lỗi chuyển sang người cải thiện trong bộ thử này, không bảo đảm mọi lượt sau.
- Món cả ba dạng ụ sợi thay cho các phần tròn ở153, nhưng sợi khá đồng nhất như mì; chi tiết thịt/bì/thính chưa giống source. FOOD fidelity chưa đạt.
- Giữ được bố cục chung Khoai trái/Đào phải và hai bát, hai đôi đũa, lá riêng, hai đồ chấm, ly nước trong khung kiểm; không đồng nghĩa exact địa lý/proportions. Khuôn mặt, tỷ lệ và framing tái dựng khác source. R03 tay Đào chuyển về lòng; không hoàn toàn giữ tay nghỉ trên bàn.
- Chưa thấy vệt hơi ở tám khung mỗi clip; không chứng nhận toàn bộ clip không hơi. Lip-sync/người nói/voice còn phải nghe-xem, không suy từ ảnh hoặc ASR.

## Tổng kết vòng và bước tiếp

Đã xác định: nhóm chỉ dẫn hình ảnh rõ hơn có kết quả tốt hơn về loại nhân vật/món trong bộ ba, download hoạt động. Đã chốt: chưa chọn production winner; đề nghị xem R01 trước để owner nghe giọng/nhịp, không gọi owner đã duyệt R01. Giả định: giữ cặp voice/preset làm baseline, không đổi script. Còn mở: exact identity, food texture, nhịp/voice/lip-sync và độ ổn định.

Bước tiếp đề nghị: owner nghe R01 và so sánh R02/R03; sau đó kiểm route khóa ảnh làm frame-start có dùng được đúng voice presets hay không, trước khi quyết định cách giảm tái dựng hình. Chưa thao tác đổi route hoặc gửi thêm generation. Nếu route không giữ được cả hình và voice, trình phương án tách hình/âm thanh, không mặc định owner chấp nhận hoặc buộc Canva. Chưa chuyển Quality.
