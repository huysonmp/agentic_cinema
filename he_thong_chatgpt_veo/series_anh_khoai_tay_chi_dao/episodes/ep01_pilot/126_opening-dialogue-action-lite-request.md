# EP01 — gói thử Lite: hai câu mở và động tác định kéo đĩa

Ngày: 2026-10-02. Trạng thái: **GÓI ĐỀ XUẤT CỤ THỂ / CHƯA CHẠY / CHỜ DUYỆT PHẠM VI MỚI**.

## 1. Mục tiêu

Kiểm xem Veo tạo được một cuộc đối thoại đời thường với động tác có chủ đích, thay vì tiếp tục yêu cầu nhân vật bất động. Dùng đoạn này để thử nối từ bản mở chuyển động nhẹ B đã duyệt tại tài liệu 125.

Chỉ gồm hai câu đầu kịch bản C-v0.5:

- Đào: “Anh nhìn mãi. Không hợp thì để em.”
- Khoai: “Khoan. Mùi này làm anh nhớ cái chảo.”

Đào định kéo đĩa; Khoai ngăn bằng lời và chú ý mùi. Không thêm gắp, cầm cốc, ăn, trao món hoặc câu tiếp theo.

Đây là thử khả năng tích hợp diễn xuất, thoại và đạo cụ, không phải phép thử chỉ thay một biến. Nếu lỗi, phải ghi riêng từng lớp rồi tách kiểm phần cần sửa; không suy giọng hoặc động tác là nguyên nhân của mọi lỗi.

## 2. Đối soát đầu vào và điểm nối

Root đã xem ảnh bàn ăn v0.8 và đối chiếu với OPEN7 trong bản mở B. Hai ảnh khác rõ về tỷ lệ nhân vật, khung hình, cách bày món và bối cảnh. Vì vậy **không nối trực tiếp B sang clip dùng v0.8 rồi gọi là liên tục**.

Đề xuất dùng cùng OPEN7 cho thử nghiệm lần này:

- File: C:\Users\PC\Downloads\du_an_nem_bui\T2-CODEX-OPEN_v0.7.png.
- SHA256: A3D80F09BFB7242BAE3007AD7B4F37473BB2F0ED019A84CC4956C4D32A8DBF9A.
- Ảnh đã có trong Flow; không tải file mới hoặc dùng ảnh chỉ phục vụ nghiên cứu.
- Phạm vi mới cần duyệt: dùng OPEN7 cho thử thoại/hành động, ngoài các thử camera/trạng thái nghỉ trước đây. Không tự nâng ảnh thành chuẩn nhân vật, món hoặc đầu vào sản xuất cuối.
- Ảnh đầu: OPEN7. Ảnh cuối: để trống, không lấy ảnh đầu làm ràng buộc kết thúc để ép nhân vật trở về pose.

B kết thúc ở tỷ lệ phóng 1,015, trong khi đầu clip Veo có thể ở tỷ lệ 1. Muốn nối phải đối chiếu frame thật và đề xuất crop khớp, hoặc chỉnh đoạn cuối B về tỷ lệ 1. Chưa thực hiện việc này; không tự gọi điểm nối đã đạt. Mọi crop phải giữ đủ mặt và bộ phục vụ, đặc biệt cốc gần mép phải.

## 3. Cấu hình và ngân sách đề nghị

- Một lượt Veo 3.1 Lite, Frames, một ảnh đầu, dọc 9:16, 720p, 8 giây, một đầu ra.
- Tối đa **10 credit**, không retry tự động. Dự kiến dùng ngân sách thử cũ còn lại, không lấy từ 100 credit Quality hoặc khoản dành riêng V02.
- 10 credit là mức đề nghị dựa trên các lượt trước, **chưa phải giá giao diện mới đã kiểm**. Phải kiểm lại model, cấu hình và giá trước khi gửi; giá vượt 10 hoặc tuyến thực hiện khác thì dừng.
- Thời lượng 8 giây là cửa sổ thử native, không khóa đoạn này dài 8 giây trong tập. Phần có thể dùng phải chọn sau khi đo và kiểm điểm cắt thật.
- Không Extend, Quality, API, mua credit, thêm nhạc hoặc công bố video.

## 4. Prompt nguyên văn đề nghị

```text
Use the supplied starting image for one continuous eight-second dialogue-and-action test. A locked tripod holds the starting composition throughout. The potato man Khoai is seated on screen left; the peach woman Dao is seated on screen right. They are adult friends having a casual meal, not presenters addressing the audience.

Dao looks at Khoai with friendly curiosity and a restrained teasing smile. She speaks exactly once in natural Vietnamese: "Anh nhìn mãi. Không hợp thì để em."
As she finishes, Dao begins reaching her left hand toward the near-right edge of the shared food plate, as if about to pull it toward herself. Her right hand remains resting near her own bowl. She does not complete the pull or lift the plate.

Khoai then looks from the food to Dao and gently interrupts with exactly: "Khoan. Mùi này làm anh nhớ cái chảo."
His delivery is quietly personal: a warm, comfortably low adult male voice, a light Northern Vietnamese accent, clear diction, a small pause after "Khoan", and subtle recognition on "mùi này". He is recalling something familiar, not making a speech. No forced bass, gravelly tone, announcer delivery, exaggerated sadness or flat monotone.

Dao pauses her reaching hand at Khoai's interruption and listens. Her voice is an original adult female voice, clear and lively with a light Northern Vietnamese accent; friendly rather than childish or scolding. Only the current speaker's mouth moves for speech. Preserve this speaker order and every Vietnamese word. Do not add, repeat, paraphrase or truncate dialogue. No overlap.

Keep the food plate, herb plate, both sauces, both eating bowls, both resting chopstick pairs and water glass in the frame. Apart from Dao's small left-hand reach, preserve the table layout and object positions. The shared food plate stays on the table. Khoai keeps both hands resting; neither person picks up chopsticks or the glass, eats, drinks or transfers food. Preserve the reference faces, clothing, food appearance, warm lighting and background. No camera move, zoom, cut, extra steam, added text, captions, narration or music. Quiet street ambience beneath clear dialogue. Preserve the native output watermark.
```

Prompt là yêu cầu, không bảo đảm model tuân thủ. Những mô tả giọng chưa phải giọng cố định đã được nghe duyệt. Không sửa prompt sau khi gửi mà vẫn gọi cùng phiên bản.

## 5. Kiểm sau khi có kết quả

| Nhóm kiểm | Điều kiện cần kiểm | Bằng chứng phải có |
|---|---|---|
| Lời và lượt nói | Đúng hai câu, đúng người/thứ tự, không thiếu hoặc thêm lời | ASR hỗ trợ, nghe thật và vị trí câu trên timeline |
| Giọng và diễn xuất | Trưởng thành, đời thường; Đào trêu nhẹ, Khoai ấm và liên tưởng | Chủ dự án nghe đánh giá; không suy từ transcript |
| Động tác | Đào dùng tay trái định kéo, dừng khi Khoai ngăn; không kéo cả bàn hoặc xuyên đĩa | Xem liên tục, kiểm frame lúc tiếp cận/dừng nếu có |
| Hình và đạo cụ | Đủ mặt, món, rau, chấm, bát, đũa, cốc; không đổi vật hoặc tự sinh động tác | Đối chiếu ảnh nguồn và video theo thời gian |
| Đồng bộ môi | Đúng người đang nói, người nghe không nói theo | Kiểm hình–tiếng liên tục; nếu công cụ không đủ thì ghi chưa kiểm và trình chủ dự án |
| Điểm nối từ B | Không nhảy scale, mặt hoặc bố trí bàn; không cắt mất đầu câu | Bản ráp local, nguồn/crop/in–out cụ thể và playback |
| Kỹ thuật | File lưu được, giải mã sạch, metadata đúng, có hash | File native và báo cáo local |

Nếu chỉ xem ảnh mẫu hoặc đọc ASR thì chưa đủ kết luận toàn clip đạt. Không dùng lỗi do chưa nghe làm bằng chứng phát âm sai. Nếu phát hiện defect, ghi “cần sửa”; không lấy vẻ đẹp của khung hình bù lỗi lời/động tác.

## 6. Vai trò và việc chủ dự án cần làm

Tôi kiểm đầu vào/giao diện, thao tác Flow nếu gói được duyệt, lưu file và log, chạy kiểm kỹ thuật/ASR, lập báo cáo và bản nối khi đủ điều kiện. Chưa có báo cáo độc lập cho gói này; không ghi agent đã kiểm khi chưa thực hiện.

Chủ dự án hiện chỉ cần duyệt hoặc sửa **gói thử cụ thể này: OPEN7 dùng cho hai câu mở và động tác định kéo đĩa, một lượt Lite, tối đa 10 credit**. Sau đó tôi trình video có hướng dẫn xem/nghe; bạn không phải tự chuẩn bị ảnh hoặc prompt.

Đây là quyền thử mới, không phải yêu cầu duyệt lại kiểu chuyển động B hoặc ngân sách Quality. Một mẫu giọng phù hợp ở đây cũng chưa khóa giọng xuyên suốt series.

## 7. Tổng hợp

Đã xác định: cần cùng nguồn để tránh nhảy bàn ăn giữa B và clip thoại. Đã chốt: hướng B, kịch bản và staging tay trái Đào. Giả định: hai câu và một động tác nhỏ có thể nằm trong cửa sổ 8 giây; phải đo thật. Còn mở: quyền thử gói này, giá giao diện, kết quả giọng/diễn xuất và nối cảnh. Bước tiếp theo: chủ dự án duyệt gói → kiểm giao diện → chạy đúng một lần → kiểm và trình kết quả. Quality vẫn chưa mở cho tới khi điều kiện Lite tại tài liệu 122 đạt.
