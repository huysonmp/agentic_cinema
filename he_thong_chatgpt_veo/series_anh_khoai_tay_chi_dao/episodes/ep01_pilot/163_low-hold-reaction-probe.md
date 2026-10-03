# EP01 — giữ nem thấp và thử phản ứng riêng

Ngày 2026-10-03. Owner “ok nhes” duyệt đề xuất sau 162: giữ nem thấp, xa mặt; thử phản ứng Đào riêng; kiểm lỗi âm thanh. Khoản thử đầu lượt 84, Quality 100 riêng chưa dùng. Số dư Flow đầu lượt đã kiểm 384. Không đổi story/giọng, không gộp vào ma trận A–D.

## Đầu vào và giả thuyết

Dùng START_short_tuft_v0.1 của 161 làm START: nem trên bát, thấp và xa mặt; không cần sửa thêm tay nguồn. Imagegen built-in dựng END_low_reaction_v0.1: chỉ quay đầu Đào sang Khoai, Khoai nhìn Đào và nhướn mày nhẹ; giữ tay/đũa/nem thấp. Kiểm ảnh actual: inventory chính đủ, môi đóng, grip/pose thấp giữ trong hình. Không chứng nhận pixel-identical hay canon món; vẫn phải kiểm continuity với C01 trước ghép.

Giả thuyết nguồn thấp giảm khả năng tự ăn chưa được chứng minh. Có đổi nhóm nguồn và prompt nên không quy kết một biến nhân quả.

Ảnh mới lưu `C:/Users/PC/Downloads/du_an_nem_bui/163_low-hold-reaction/END_low_reaction_v0.1.png`, ảnh gốc giữ nguyên.

## Phép thử và gate

X3 Lite Frames 9:16, 720p/8s nếu giá UI phù hợp 30/bộ. Chỉ thử giữ tay và quay đầu/ánh nhìn. Không lời thoại; voice đã chốt chưa được ghép. Loại nếu nâng nem về mặt, chạm/ăn; mất/thay nem/đũa; đổi inventory; diễn thứ tự không đúng hoặc tự thêm cử chỉ lớn. Review decode + grid toàn clip, thêm kiểm dày vùng nghi ngờ. Người điều phối review, không giả nhận agent độc lập đã chạy.

## Trạng thái

Đã gửi X3 Lite, preflight và cặp khung đã kiểm thực tế. Đang chờ kết quả; chưa đánh giá hoặc ghi chi phí ròng từ dự trù.

## Prompt video dự kiến gửi

```text
Locked tripod two-shot at the supplied small street eatery. Match the supplied start and end frames. Khoai's right forearm, hand, two wooden chopsticks and small pinched tuft of cool nem stay anchored LOW above his own bowl, at the exact start-frame position for the whole shot. His lips remain closed. Dao slowly turns her head from looking down screen right at her water glass to looking screen left at Khoai, with a gently amused knowing expression. Her hands remain resting at the bowl and glass. After she looks at him, Khoai shifts his eyes toward her and lifts one eyebrow slightly, then they hold the final look. Only heads, eyes and eyebrows move; all hands and the held tuft retain their original position and shape. Preserve the exact adult potato and peach identities, outfits, both bowls, two dipping saucers, nem plate and mound, leaves, spare chopsticks, water glass, lighting, table layout and camera. Audio: quiet street ambience with faint distant traffic only; no dialogue, vocalization or music. Preserve native watermark.
```

Không tìm thấy toggle âm thanh trong panel Lite hiện tại. Prompt vòng mới diễn đạt ambience rõ, bỏ cụm “Silent performance” đi kèm ambience của vòng trước; đây là thay đổi đã ghi, không xác nhận nó là nguyên nhân audio error hoặc coi là cùng điều kiện A–D.

END SHA256 `A85C816872CC794326F07066B90FC8F6A68F500FAC26DF20620E1A2760EFE5F7`; START hash tại 161. Preflight đã chọn Lite Frames 9:16/x3, giá30.

## Kiểm tư liệu công cụ

Ngày truy cập 2026-10-03, nguồn primary [Google Flow Help](https://support.google.com/flow/answer/16353333?co=GENIE.Platform%3DDesktop&hl=en), mục Audio Generation Failed: âm thanh có thể bị đánh giá chất lượng thấp, video không được tạo và hoàn credit; khuyến nghị thử lại hoặc đổi prompt. Đây là giải thích chung của Google, không chứng minh lý do cụ thể của prompt dự án. Không có hướng dẫn tắt audio Lite trong phần FAQ đọc được.

[Bảng model chính thức](https://support.google.com/flow/answer/16352836?hl=en) xác nhận Lite hỗ trợ khung đầu-cuối và 4/6/8s cả hai tỷ lệ. Không dùng bài community, giả thuyết ngôn ngữ hay tải máy chủ để kết luận gốc lỗi.

## Prompt ảnh END thực tế

```text
Use case: identity-preserve. Image 1 is the exact edit target: a reference frame for an adult animated scene at a small neat street eatery. Change ONLY the peach woman Dao's head orientation and eyes: turn her head toward SCREEN LEFT, looking at Khoai with a gently amused knowing expression, lips closed. Change ONLY the potato man Khoai's eyes toward Dao, a very slight raised eyebrow caught-in-the-act expression, lips CLOSED. Preserve Khoai's entire right forearm, hand, grip, TWO wooden chopsticks and small nem tuft in the EXACT original LOW position above his bowl, far below and away from his face. Do not raise or lower food or hand. Preserve both adult character identities, outfits, bodies and remaining hands. Preserve Dao's hands at bowl and glass. Preserve exact camera, portrait crop, lighting, street background, BOTH bowls, TWO dipping dishes, plate and mound of cool nem, leaf plate, spare chopsticks, water glass. No eating, no food contact with face, no extra gesture, text or steam. Single END reaction frame.
```

## Nhật ký kết quả / biến thể âm thanh

V0.1 X3: R01/R03 lỗi audio, R02 thành công. Đã thử lại nguyên đầu vào x2 cho hai lượt lỗi, cả hai vẫn lỗi audio và UI ghi không tính phí. Không gọi đây là đủ ba video so sánh.

R02 Flow ID `03693b01-4b00-452d-b17c-b4df12560eb9`, native `Dao_looks_at_Khoai_20261003072031.mp4`. Lưu `R02.mp4` trong folder 163, decode toàn bộ sạch; H264/720x1280/24fps/8s/AAC. Grid2fps toàn clip +8fps đoạn0–2s: Khoai vẫn nâng nem vào vùng ngực/cằm và mở miệng, rồi hạ về bát; Đào tự cử chỉ tay/đổi gaze. Chưa đạt hold-locked. Không đủ bằng chứng từ khung mẫu để khẳng định nem đã chạm miệng hoặc bị cắn; không ghi “tự ăn” như fact. Chưa nghe ambience, chưa voice/lip-sync PASS.

Ở editor UI mới, `video.downloadMedia` không có DOM video để lưu; không gọi đó là hỏng file. Menu tải720p hoạt động: toast và file thực tế trong Downloads được kiểm lại rồi copy. Footer Omni Flash của edit không phải model tạo; model tạo vẫn Lite theo preflight.

V0.2: giữ nguyên tất cả khung và câu prompt V0.1, **chỉ xóa chính xác** đoạn `Audio: quiet street ambience with faint distant traffic only; no dialogue, vocalization or music. `; gửi x3 Lite mới giá30. Đây là bỏ ép mô tả âm thanh, không phải API/UI tắt audio, không cam kết video câm hoặc lỗi sẽ hết. Không gộp số mẫu V0.2 vào V0.1 để tạo tỷ lệ thành công giả. Tổng chi tối đa lượt này dự kiến40 nếu bộ mới đủ ba thành công, khoản thử vẫn >=44; cần đối soát actual sau.

## Kết quả đối soát cuối lượt

Tổng 8 yêu cầu mẫu: V0.1 ba lượt và hai lượt thay lỗi; V0.2 ba lượt. Có **3 video thực tế**, **5 lỗi âm thanh** được UI ghi không tính phí. V0.1 đạt 1/3 video ban đầu và 0/2 video thay lỗi; V0.2 đạt 2/3 video. Không gọi đây là một bộ ba cùng điều kiện, không chứng minh bỏ đoạn mô tả âm thanh đã sửa nguyên nhân gốc.

Số dư đầu 384 (`balance-before.png`), cuối 354 (`balance-after.png`) => chi ròng **30**, khoản thử còn **54**. Quality 100 riêng chưa sử dụng. Media ở folder 163; cả ba giải mã sạch, 720x1280/24fps/8s, H264 + AAC. Không suy luận việc có AAC đồng nghĩa âm nền đúng hoặc giọng đã đạt.

| Mã | Flow ID | Native filename trong Downloads | QC hình / trạng thái |
| --- | --- | --- | --- |
| R02 V0.1 | 03693b01-4b00-452d-b17c-b4df12560eb9 | Dao_looks_at_Khoai_20261003072031.mp4 | Nâng/hạ và mở miệng, tự thêm cử chỉ. Không đạt cả cảnh |
| V02-02 | a3dbbc32-0f3e-44bd-b0ad-02f588eea1b3 | Two_people_at_street_eatery_20261003072724.mp4 | Nâng nem ở đoạn đầu; Đào tự nhấc cốc và làm cử chỉ, không giữ pose. Không đạt |
| V02-03 | e41e7366-bd13-49a8-b7fb-89338bcfdb0d | Two_people_at_street_eatery_20261003072829.mp4 | Nem vẫn ở thấp trên bát, không thấy đường nâng lên mặt trong grid. Tay có dao động nhỏ, hai nhân vật thêm cử chỉ/mở miệng; gaze quay qua lại không chỉ một phản ứng. Tiến bộ riêng giữ thấp, chưa đạt cả cảnh |

Kiểm toàn clip ở 2fps mỗi mẫu; R02 thêm 8fps đoạn 0–2s và 36 frame đầu tại 24fps; V02-03 thêm 6fps đoạn 3–5,5s. R02 không thấy tiếp xúc nem–mặt trong 36 frame đầu được kiểm; không khẳng định đã cắn/ăn. V02-03 không có hơi nóng hoặc mất đạo cụ chính trong khung kiểm, nhưng chưa hoàn tất kiểm tính liên tục với C01, hình chuẩn của món và toàn bộ frame.

### Tổng hợp vòng quyết định

- Đã xác định: có một mẫu giữ nem thấp tốt hơn; audio vẫn lỗi ngắt quãng; menu tải720p native lại hoạt động trong phiên hiện tại.
- Đã chốt trong phạm vi: không gửi bản lỗi để duyệt sản xuất, không ghép thoại/Quality, giữ V02-03 làm bằng chứng tiến bộ kỹ thuật, không tự ghi owner approved cảnh.
- Giả định: bối cảnh ăn/khung có nem có thể gợi động tác ngoài yêu cầu; prompt dài hoặc thời lượng8s có thể khuyến khích bổ sung diễn; chưa kiểm chứng các nguyên nhân này.
- Còn mở: giữ phản ứng đúng một nhịp, không tự nói/cử chỉ, tính liên tục với C01, khả năng tạo âm thanh ổn định, giọng và khớp môi.
- Tiếp theo đề xuất: giữ vị trí thấp này, thử prompt ngắn chỉ một hành động quay đầu/ánh nhìn; nếu đổi góc cận thì thiết kế cảnh có mục đích kể chuyện và duyệt nối C01, không dùng việc che tay/món để gọi lỗi ăn đã giải quyết. Còn 54 đủ một bộ ba Lite giá 30 trong hạn mức; chưa gửi bộ này.
