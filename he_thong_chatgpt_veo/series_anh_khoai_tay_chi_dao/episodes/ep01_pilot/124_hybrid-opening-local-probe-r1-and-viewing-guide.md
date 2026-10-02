# EP01 — bản thử cảnh mở local R1 và hướng dẫn xem

Ngày: 2026-10-02. Trạng thái: **ĐÃ DỰNG HAI BẢN THỬ / CHỜ ĐÁNH GIÁ CHUYỂN ĐỘNG**, chưa duyệt cảnh sản xuất.

## 1. Đã thực hiện

Theo yêu cầu “ok làm đi, nhớ hướng dẫn tôi nhé”, đã dựng hai bản từ cùng ảnh OPEN7 bằng FFmpeg local. Không gọi Veo, không tải lên dịch vụ, không tiêu credit. Ngân sách Quality ở tài liệu 122 chưa được sử dụng.

- A_static.mp4: giữ nguyên khung.
- B_gentle_push.mp4: tiến nhẹ từ hệ số 1 lên 1,015, tăng/giảm tốc ở hai đầu; giữ mép phải để bảo vệ cốc gần rìa ảnh.
- Cả hai: 4 giây, 96 khung hình, 24 fps, 1080×1920, H.264, không có âm thanh. Độ phân giải này là bản dựng từ ảnh, không phải video tạo bằng Quality.
- Giữ tỷ lệ ảnh bằng scale và pad, không kéo giãn; không tạo thêm cảnh, ánh sáng, giọng hoặc chuyển động nhân vật.

Thời lượng 4 giây chỉ để xem thử chuyển động, không khóa 4 giây vào tập 30 giây. Bản này không có thoại hoặc hành động kéo đĩa, không thay thế toàn bộ S01.

## 2. Nguồn và truy xuất

Nguồn: C:\Users\PC\Downloads\du_an_nem_bui\T2-CODEX-OPEN_v0.7.png.

SHA256: A3D80F09BFB7242BAE3007AD7B4F37473BB2F0ED019A84CC4956C4D32A8DBF9A.

Script: scripts/render_ep01_opening_probe.py. Script chỉ nhận đúng hash OPEN7; không ghi đè thư mục kết quả đã tồn tại. Kiểm chống ghi đè đã chạy và trả về lỗi có chủ đích, không làm đổi output.

Hồ sơ đầy đủ: artifacts/opening-hybrid/r1/manifest.json, gồm lệnh dựng, metadata và hash đầu ra.

| Bản | SHA256 |
|---|---|
| A | 0A79B66AF4C3BF3E5F2BC0FB3391F9BE76B9999825F54E4CA737BEC5E1F44B41 |
| B | 2EA76518A61FD890E8A2109A669F4EAFBDE55666893BA9CB1FC2F98A5A1D414D |

Nguồn chỉ được chọn trong phạm vi thử nghiệm hiện hành; bản dựng không tự nâng nguồn thành chuẩn production hoặc xác nhận độ chính xác của món.

## 3. Kiểm đã thực hiện và giới hạn

- Đo đúng kích thước, số khung hình và thời lượng; giải mã toàn bộ hai video không báo lỗi.
- Root xem ảnh nguồn và tám ảnh mẫu mỗi video, khoảng 0,25–3,75 giây. Mặt hai nhân vật, món, rau, hai chén chấm, bát, đũa và cốc còn trong khung ở các mẫu đã xem.
- Phép biến đổi 2D không sinh thêm hành động hoặc thay vật thể. Không có thao tác xóa dấu/hình mờ.
- Chưa kiểm phát liên tục để kết luận chuyển động không giật; ảnh mẫu và giải mã sạch không thay thế đánh giá này.
- Chưa có review độc lập, chưa có tiếng hoặc điểm nối vào đoạn thoại thật. Không ghi production PASS.

Điểm hạn chế sáng tạo: bản B chỉ là tiến nhẹ toàn khung, **chưa thực hiện dẫn mắt món → mắt Khoai như một động tác nâng máy 3D**. Nếu không tạo được sự chú ý mong muốn, phải sửa thiết kế hoặc giữ khung; không gọi nó đã đạt T2 chỉ vì không có lỗi tay.

## 4. Hướng dẫn chủ dự án xem

1. Xem A rồi B ở cùng kích thước, tốt nhất trên điện thoại hoặc cửa sổ dọc. Không cần bật âm thanh vì hai bản không có tiếng.
2. Lần đầu chỉ xem cảm giác: có hợp không khí chill, thân mật ở quán nhỏ không? B có chuyển động dễ chịu hay giống một tấm ảnh được phóng to?
3. Lần hai nhìn mép khung: cốc bên phải, đĩa rau bên trái, đầu hai nhân vật và toàn đĩa nem có bị sát mép hoặc gây khó chịu không?
4. Không đánh giá giọng, động tác kéo đĩa hoặc nhịp cả tập từ hai bản này. Những phần đó chưa được dựng.

Bạn có thể trả lời ngắn:

- “Giữ A” — ưu tiên khung tĩnh.
- “Giữ hướng B” — chấp nhận kiểu tiến nhẹ để phát triển tiếp, chưa duyệt toàn cảnh.
- “Cả hai chưa ổn: …” — nêu cảm giác hoặc điểm hình chưa phù hợp; không cần tự chỉnh file.

Khuyến nghị sơ bộ: dùng B làm ứng viên kiểm chuyển động nếu bạn thấy tự nhiên, nhưng chưa khóa vì nó chưa chứng minh dẫn mắt món → Khoai. A là đối chứng, không mặc định kém hơn.

## 5. Bước tiếp theo

Sau khi có phản hồi: sửa hoặc chọn hướng cảnh mở; chuẩn bị đoạn thoại/hành động riêng và kiểm điểm nối. Tôi tiếp tục chuẩn bị ảnh, prompt và hồ sơ thử Lite; không yêu cầu bạn thao tác dựng.

Điều kiện Quality vẫn giữ: đầu vào, prompt và thử nghiệm tương ứng phải đạt trên Lite trước. **Hai bản local này không phải clip Lite và không đủ để mở lượt Quality.**

Bản sao để xem: C:\Users\PC\Downloads\du_an_nem_bui\124_hybrid_opening_r1. Media và manifest kết quả lưu local; script và tài liệu quản lý bằng Git.
