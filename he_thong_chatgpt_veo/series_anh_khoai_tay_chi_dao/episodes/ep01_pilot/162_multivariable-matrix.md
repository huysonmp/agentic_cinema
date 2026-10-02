# EP01 — ma trận thử nghiệm A–D

Ngày 2026-10-03. Owner duyệt bằng “ok” sau đề xuất ma trận bốn phương án, mỗi phương án ba Lite. Đây là sàng lọc kỹ thuật, chưa duyệt video hay chuyển Quality.

## Thiết kế đã chốt

| Mã | Cách dựng | Cách diễn đạt prompt | Số mẫu |
| --- | --- | --- | --- |
| A | Nâng nem rồi dừng trong một cảnh | Chuyển động vật lý và điểm dừng | 3 |
| B | Như A | Tách nhịp hành động rõ ràng | 3 |
| C | Cắt từ insert C01 sang pose đã giữ nem | Phản ứng tối giản | 3 |
| D | Như C | Đào quay lại → Khoai khựng nhẹ | 3 |

A/B dùng START_short_tuft và END_short_pause của 161. C/D dùng END_short_pause làm START, END_reaction_v0.1 làm END. C01 chỉ đã được duyệt cơ học gắp, không phải duyệt cả cảnh.

Không coi đây là phép thử nhân quả đa biến nghiêm ngặt: đổi cách dựng đồng thời đổi nhiệm vụ hình ảnh/khung nguồn; không khóa được seed. Ba mẫu mỗi ô chỉ cho tín hiệu thực dụng, không suy luận độ tin cậy thống kê.

## Ngân sách và kiểm đầu vào

Trial còn 154 theo đối soát 161; Quality 100 riêng chưa sử dụng. Dự trù 120 cho 12 Lite, dự kiến còn 34 nếu tất cả tính phí 10/mẫu. Phải ghi số dư thực tế sau chạy, không coi dự trù là đã chi.

Khi mở phiên mới, UI mặc định Omni 1.1 Flash, x1, giá 12; đã đổi sang Veo 3.1 - Lite, x3, giá hiển thị 30. Không dùng cài đặt phiên cũ làm bằng chứng phiên mới.

Khung phản ứng mới được tạo bằng imagegen: Đào quay sang Khoai; Khoai liếc sang Đào, môi đóng. Kiểm ảnh: tay, nem, đũa và inventory chính còn đúng pose; chưa chứng nhận đồng nhất pixel hoặc canon món ăn. Không sửa/chấp nhận drift của nguồn 161 như thể đã đạt continuity sản xuất.

## Gate review

Loại nếu ăn/chạm miệng trước khi bị bắt gặp; mất/đổi nem hoặc đũa; đảo grip; sai thứ tự ánh nhìn; biến dạng nhân vật hoặc mất đạo cụ chính; xuất hiện hơi nóng ở nem lạnh. A/B phải nâng rồi giữ, Đào chưa quay lại. C/D phải giữ nem, Đào quay lại và Khoai phản ứng; không chấm việc không nâng tay là lỗi ở C/D.

Đánh giá riêng khả năng dùng đoạn sạch để dựng và độ liền mạch với C01. Chưa chứng nhận voice, lip-sync hoặc cả tập từ thử nghiệm im lời này. Chưa gọi review của điều phối là agent độc lập đã chạy.

## Trạng thái

Đã gửi A/B/C/D x3. Lần đầu: A3, B3, C1 tạo được; C2 và D3 lỗi âm thanh, UI ghi không tính phí. Đã gửi lại D x3, C x2 với nguyên prompt/nguồn để bổ sung mẫu, không vượt trần chi 120. Việc gửi thêm chỉ thay lỗi kỹ thuật, không chọn bỏ mẫu hình kém.

Lưu media qua API giao diện `video.downloadMedia`: menu tải 720p đã bấm nhưng chưa có file mới trong Downloads; không ghi nhận tải thành công từ thao tác bấm. Bảy media thực tế đã lưu và giải mã toàn bộ sạch; grid 2fps phục vụ kiểm hình, chưa chứng nhận âm thanh.

## Prompt thực tế

A: dùng nguyên prompt video của 161 (đã lưu tại tài liệu đó).

B:
```text
Locked tripod two-shot at the supplied street eatery. Match the supplied start and end frames. Beat 1: Khoai holds the same small tuft of cool nem above his own bowl. Beat 2: his forearm makes one gentle continuous rise to the final-frame position beside his chin, below his closed lips, maintaining a clear space between food and face. Beat 3: stop the arm and hold this endpoint for the remaining time. Keep the same two wooden chopsticks, handle grip and pinched tuft throughout. Dao remains with her head turned screen right looking down toward her water glass with her hand resting at it; she does not look back yet. Keep their exact potato and peach faces, outfits, both personal bowls, plate of nem, leaves, two dipping saucers, spare chopsticks and glass unchanged. Preserve light, table layout and camera. The held tuft stays outside the face throughout. Silent performance, no speech or music, subtle street ambience only. Preserve native watermark.
```

C và D nối nguyên đoạn chung cuối:
```text
Keep the same two wooden chopsticks, handle grip and pinched small tuft throughout, outside the face, with closed lips and clear space to the face. Keep their exact potato and peach faces, outfits, both personal bowls, plate of cool nem, leaves, two dipping saucers, spare chopsticks and glass unchanged. Preserve light, table layout and locked camera. Silent performance, no speech or music, subtle street ambience only. Preserve native watermark.
```

C đầu:
```text
Locked tripod two-shot at the supplied street eatery. Match the supplied start and end frames. Khoai keeps his right arm, hand, chopsticks and held nem still in the start-frame position below his lips. Dao gently turns her head from looking down screen right at her glass to looking screen left at Khoai, with a knowing amused look. Khoai only shifts his eyes toward Dao with a tiny caught expression. All hands stay in place. Hold the final look.
```

D đầu:
```text
Locked tripod two-shot at the supplied street eatery. Match the supplied start and end frames. Beat 1: Khoai already holds the nem below his closed lips, his right arm, hand and chopsticks remain anchored in the start-frame position while Dao looks down screen right at the glass. Beat 2: Dao turns her head screen left and looks at Khoai with knowing amusement, her hands remain at bowl and glass. Beat 3: Khoai shifts only his eyes toward Dao and gives a tiny caught-in-the-act eyebrow lift, then freezes. Hold their final look with the held tuft and hand unchanged.
```

END_reaction SHA256: `826FD2680938655183DF5FDEA65B2786F637BE87D85DDC48F33592983E6F6CBE`.

## Manifest media lần đầu

File trong `C:/Users/PC/Downloads/du_an_nem_bui/162_multivariable_matrix`.

| Mã | Flow ID | Tệp tải thực tế trong Downloads |
| --- | --- | --- |
| A01 | 0f0da23d-ebab-4204-a5e0-38120deadef1 | 67c8ac11-7cfc-47f2-9b2d-4da4d684229f.mp4 |
| A02 | 90b96c9c-1fbc-4fee-b4b7-4f21002e1616 | e71066b6-6a21-4737-9307-bc21a1ef5e34.mp4 |
| A03 | 3fd9fb79-15f5-4e7c-9534-3ab70ba2f5ad | 2dbaa455-5692-451d-b6b3-9626d8d34ebc.mp4 |
| B01 | e4bd0e50-8c0f-49aa-922c-d11ec1768d18 | f51e0b10-914b-48e6-8d4e-63385aaaddaf.mp4 |
| B02 | 358266d8-e6a0-45d8-ad6b-9f6e425aa882 | 9ccc42fa-ded3-4574-8649-262800ac2065.mp4 |
| B03 | 7b209299-bbca-40ae-926b-200800520547 | 43b8a2bb-e37d-464e-8868-db1347a0caba.mp4 |
| C02 | 36ea5c58-ce37-470e-a358-69d7e6d7c05c | 30e7e408-5238-43d9-accc-ae3990fddb9d.mp4 |

## Kết quả chốt lượt này

Tổng **17 yêu cầu mẫu**: 12 lần đầu + 5 thử lại lỗi. Có 7 video; 10 lỗi âm thanh, UI ghi không tính phí. Thử lại D3 và C2 đều lỗi. Không tự đổi model, tăng Quality hoặc thay prompt âm thanh rồi coi là cùng ô thử. Nút “chế độ cài đặt” trong báo lỗi chưa mở được tùy chọn âm thanh; menu Lựa chọn khác không có thiết lập này. Chưa xác minh có thể tắt âm thanh cho Lite trong UI hiện tại.

Số dư Flow sau chạy **384**, bằng chứng `balance-after.png`; lần trước 454, chênh lệch ròng **70** phù hợp 7 video x10. Khoản thử còn **84**, chưa dùng Quality 100 riêng. Chưa có số dư trước lượt được chụp riêng, dùng đối soát 161 làm mốc nên chênh lệch tài khoản không tự chứng minh độc lập không có giao dịch khác.

| Ô | Video / yêu cầu | Qua gate hình | Quan sát và quyết định |
| --- | --- | --- | --- |
| A | 3/3 | 0/3 | A01 nâng qua vùng mắt, mở miệng và Đào quay lại sớm. A02/A03 đưa nem qua vùng mũi-môi, hạ về bát rồi nâng lại. Không giữ endpoint; sợi dài tái xuất hiện. Loại |
| B | 3/3 | 0/3 | B01 nâng-hạ-nâng, Đào quay lại sớm. B02/B03 giữ đoạn cuối tốt hơn A nhưng vẫn vượt điểm dừng ở đoạn đầu; Đào đổi hướng nhìn/tay ngoài yêu cầu, sợi nem dài. Loại khỏi ghép |
| C | 1/5 | 0/1 | C02 có mở miệng và đưa nem/đũa vào vùng miệng trước phản ứng; Đào tự làm thêm cử chỉ tay. Không đạt giữ tay, không dùng đoạn sau động tác ăn để trao miếng đó cho Đào |
| D | 0/6 | Chưa chấm | Tất cả lỗi âm thanh; không có hình để kết luận tốt/xấu |

Bảy tệp H264 720x1280, 24fps, 8s, AAC; giải mã toàn bộ sạch. Review grid toàn clip mỗi 0,5s; B02/B03/C02 thêm 6fps đoạn 0,5–3s. Đây là review khung mẫu, không phải chứng nhận từng frame hoặc đã nghe toàn âm thanh. Inventory chính còn trong các khung kiểm, nhưng không thay thế gate diễn.

**Điều đã xác định:** prompt tách nhịp B có đoạn giữ khá hơn trong nhóm nhỏ này, chưa giải quyết vượt endpoint. Nguồn pose đã giữ sát mặt C vẫn không ngăn động tác ăn ngoài yêu cầu.

**Quyết định trong scope:** không chọn ứng viên sản xuất; không gọi D fail hình; không ghép thoại/Quality trên bản lỗi. Giữ ma trận chưa hoàn tất vì thiếu mẫu C/D.

**Giả định/hypothesis chưa kiểm chứng:** pose nem sát mặt và ngữ cảnh ăn có thể gợi động tác ăn; chưa xác nhận nguyên nhân riêng. Không quy lỗi cho một từ trong prompt hoặc cho cơ chế âm thanh.

**Bước tiếp đề xuất, chưa thực hiện:** kiểm tùy chọn không âm thanh của Lite; nếu không có, trình owner chọn một probe mới giữ nem thấp và lệch khỏi mặt, rồi quay phản ứng riêng. Ghi phiên bản mới và không gộp kết quả vào A–D hiện tại. Chỉ ghép C01 với phản ứng khi có đoạn sạch trước bất kỳ ăn/chạm miệng, kiểm lại continuity và duyệt nhịp tổng thể. Không cần owner nghe/chọn giọng ở lượt này.

## Prompt tạo END phản ứng thực tế

```text
Use case: identity-preserve. Image 1 is the exact edit target, a portrait reference frame for an animated scene. Change ONLY Dao the adult peach woman's head orientation and gaze: she turns back toward screen LEFT to look at Khoai's face with a gently amused, knowing look. Change ONLY Khoai's pupils to glance toward her, with a tiny caught-in-the-act eyebrow lift; his lips remain CLOSED. Preserve Khoai's entire arm, hand, two wooden chopsticks, small held nem tuft and its precise position below his lips UNCHANGED. No food contact, no eating, no new gesture. Preserve both identities, adult proportions, clothing, Dao's two hands at the existing bowl and glass, both bowls, nem mound and plate, leaves, TWO dipping dishes, spare chopsticks, glass, camera, crop, lighting and background exactly unchanged. No steam, text or extra props. One still image.
```
