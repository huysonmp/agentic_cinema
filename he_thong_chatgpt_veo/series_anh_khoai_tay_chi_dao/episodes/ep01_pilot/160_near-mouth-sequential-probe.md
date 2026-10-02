# EP01 — kiểm nhịp đưa nem gần miệng sau C01

## Quyết định và ranh giới

Owner trả lời “ok” sau khi xem C01 của hồ sơ 159. Ghi nhận đồng ý cho riêng động tác gắp, không suy thành duyệt toàn tập hoặc Quality. Khoản trial còn 214 credit ở đầu lượt; số dư Flow lần kiểm trước 514, không dùng toàn số dư làm quyền tiêu. Tiếp tục x3 Lite mỗi bộ.

## Đầu vào / kịch bản

Theo script 32 C-v0.5: Đào lấy cốc, Khoai lấy nem về phía miệng; bị bắt gặp trước tiếp xúc rồi chuyển vào bát. Probe này chỉ kiểm đoạn đưa nem lên khi Đào đang nhìn cốc. Không thoại, không sửa lời, không đút Đào. C01 là insert riêng cơ học, chưa xác nhận continuity với toàn cảnh.

START toàn cảnh: `C:/Users/PC/Downloads/du_an_nem_bui/158_end_frame_control/END_hold_v0.1.png`. Dùng lại pose giữ nem thấp, Đào nhìn cốc. Không tự nâng ảnh thử 158 thành production canon.

## Kiểm ảnh trước generation

Built-in imagegen dựng END từ START. END v0.1 có phần nem quá sát môi, không đủ air gap: loại khỏi input Veo, sửa một nhóm tay/đũa/vị trí nem, giữ bàn và hai nhân vật. Không tiêu Flow credit cho ảnh chưa qua đầu vào.

END v0.2: `C:/Users/PC/Downloads/du_an_nem_bui/160_near_mouth/END_pause_v0.2.png`. Đã xem actual: nem thấp hơn môi, có khoảng cách, hai bát/hai chấm/rau/cốc còn đủ. Dùng làm endpoint thử, chưa phải canon. Prompt sửa ảnh:

SHA256 END v0.2: `2D48D291912CBC80E9B4BE5999C71F094132265656B85A0A2BB5647F14276AD3`.
Ảnh v0.1 bị loại còn tại `C:/Users/PC/.codex/generated_images/01a0eb0e-6ec3-7121-a6a5-ea0ccdb77744/exec-ff4a47a3-38b4-453b-a07c-9ce480642fdd.png`.

```text
Use case: precise-object-edit. Image 1 is the exact edit target. Change ONLY Khoai's right hand, existing pair of chopsticks and the tiny held nem tuft position: lower the tuft to beside his chin, on his own side, with a clearly visible open background gap separating ALL food and chopstick tips from his lips and chin. It should be poised approaching his own mouth but still visibly away, not directly under or touching his smile. Keep his lips CLOSED, exact expression, exact head, left hand, Dao, BOTH bowls, food plate, leaves, TWO dipping saucers, spare chopsticks, water glass, camera, lighting and background unchanged. Keep SAME small amount of held nem, don't enlarge tuft or invent long dangling strands. Two sticks remain continuous, correctly held at thick handles with narrow tips pinching food. No text/diagrams/measurement marks, no steam, no romance. One portrait still.
```

## Kết quả

Đã gửi x3 Veo 3.1 - Lite, Frames, 9:16, 720p/8s. Giá hiển thị trước gửi 30 credit; proof `C:/Users/PC/Downloads/du_an_nem_bui/160_near_mouth/preflight.png`. Kết quả/phí actual bên dưới. Chỉ trình mẫu qua kiểm nội bộ; không giả định agent độc lập đã chạy.

### Đối soát sau chạy

Cả ba tạo và tải được. Số dư actual screenshot `balance-after.png`: **484**, trước lượt 514 => ròng **30 credit**, trial còn **184**. Quality riêng chưa dùng. Native file giải mã toàn bộ sạch; cả ba H264, 720x1280, 24fps, 8s, AAC. Chưa nghe kiểm ambience, chưa ghép voice.

| Mã | Flow ID | Native filename trong Downloads | Review hình |
| --- | --- | --- | --- |
| N01 | 3ebedfe5-e670-47ad-a0d6-3a076dbc3091 | Khoai_holding_nem_at_eatery_20261002224617.mp4 | Đào quay mắt/head sang Khoai sớm; Khoai đưa lên rồi hạ lại/nâng lần nữa, không một chuyển động và giữ; sợi nem kéo dài |
| N02 | 03afbbc9-b5c9-486e-9400-43e89b18072b | Khoai_holding_nem_at_eatery_20261002224632.mp4 | Miệng mở, nem/đũa qua vùng môi khoảng 2–3s; Đào đã nhìn Khoai, sai ranh giới trước ăn |
| N03 | d96c6a54-5930-436c-9a27-4fffa2918c0d | Khoai_holding_nem_at_eatery_20261002224646.mp4 | Hạ nem vào bát riêng trước nâng; sợi kéo dài; Đào nhìn Khoai quá sớm |

Bản lưu `N01.mp4`, `N02.mp4`, `N03.mp4` và grid mỗi 0,5s toàn clip ở folder 160. N02 kiểm thêm ảnh 6fps từ 1,5–3,5s (`N02-mouth-dense.png`). Không khẳng định xem từng frame 24fps; có lỗi đủ loại cả ba khỏi ghép, không cần gọi tất cả là đã cắn/ăn. Trong các khung kiểm đạo cụ chính vẫn còn, nhưng không dùng riêng tiêu chí này để PASS.

### Truy ngược đầu vào / giả thuyết chưa xác nhận

START hash `0E42DDD4703C38EB8E2AA9ADC4DF938968AD421AC3A85130203208DB9FE811BD`. START 158 có các sợi nem rủ về bát và Đào chỉ cúi mắt, chưa có pose quay rõ ràng ra hướng cốc. END v0.2 cũng giữ mặt Đào gần chính diện. Preflight đã kiểm inventory/gap nhưng chưa kiểm độ rõ của trạng thái “không quan sát Khoai”. Đây là thiếu sót ở kiểm đầu vào, không khẳng định là nguyên nhân duy nhất model tự ăn.

Prompt yêu cầu Dao không nhìn lại nhưng nguồn pose chưa biểu đạt mạnh điều đó; source chứa sợi dài trong khi story cần phần nem nhỏ. Giả thuyết: nguồn ảnh và kỳ vọng diễn chưa đồng nhất; ngữ cảnh đưa thức ăn lên vẫn có thể dẫn model tới ăn dù END chưa ăn. Chưa thử kiểm soát nên không quy lỗi riêng từ “mouth” hoặc khẳng định sửa source chắc chắn giải quyết.

### Bước sửa tiếp — chưa chạy

1. Sửa START riêng pose Đào: đầu/gaze quay rõ về cốc ngoài phía cô, không nhìn Khoai. Giữ bàn, Khoai và món không đổi, QC ảnh trước.
2. Chuẩn hóa riêng phần nem cầm theo C01: ít sợi ngắn, không dây kéo về bát; đối chiếu continuity, không đổi thành cuộn. Tách lần sửa để truy biến.
3. Từ START đã qua QC dựng END chỉ nâng tay; kiểm air gap ở môi. X3 Lite, không retry nguyên bộ 160.
4. Nếu vẫn ăn, thử phương án cắt từ insert C01 sang pose đang giữ bên cằm rồi kiểm phản ứng Đào; đây là giả thuyết dựng thử, không tự đổi canon hoặc dùng miếng đã ăn để đưa bát.

Chưa có winner để gửi owner thử cảnh kế tiếp. C01 owner chấp nhận riêng cơ học vẫn giữ, không bị ghi đè bởi bộ thất bại này.

### Prompt video thực tế

```text
Locked tripod two-shot at the supplied street eatery. Match the supplied start and end frames. Khoai gently raises the same small tuft of cool nem from above his own bowl to the final-frame position beside his chin, then holds it there with his lips closed and a clear space between food and face. One small continuous arm movement only. Keep the same two wooden chopsticks, handle grip and pinched tuft throughout. Dao remains looking down toward her water glass with her hand resting at it; she does not look back yet. Keep their exact potato and peach faces, outfits, both personal bowls, plate of nem, leaves, two dipping saucers, spare chopsticks and glass unchanged. Preserve light, table layout and camera. The held tuft stays outside the face throughout. Silent performance, no speech or music, subtle street ambience only. Preserve native watermark.
```

### Prompt END v0.1 (bị loại trước Veo)

```text
Use case: precise-object-edit / identity-preserve. Image 1 is the edit target and exact START frame of an adult potato man Khoai and adult peach woman Dao at the supplied small street eatery. Produce a single portrait END frame. Change ONLY Khoai's right forearm, hand and existing wooden chopsticks position: he lifts the SAME small loose tuft of cool nem he is currently holding, toward his own mouth, stopping in front of his CLOSED lips with a clearly visible air gap. The tuft has NOT touched his lips, no bite, no chewing. Preserve grip at the thicker blunt handles, two long continuous sticks with narrow tips pinching the same little tuft. His left hand stays on table. Keep Khoai's exact face, potato texture, calm expression and outfit. Dao remains looking down and away at her water glass, her hand still at the glass, not watching Khoai. Preserve her exact peach face, proportions and clothing. Camera, crop, light and background unchanged. Keep BOTH personal bowls, nem plate/mound, two dipping dishes, leaf plate, spare chopsticks and water glass at exactly their original positions. No additional hands, props, steam, text, graphic or romantic gesture. Same food quantity suspended, not a long noodle strand. One 9:16 still, not a montage.
```
