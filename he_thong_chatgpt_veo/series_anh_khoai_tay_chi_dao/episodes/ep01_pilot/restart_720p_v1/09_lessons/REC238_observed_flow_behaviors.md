# REC238 — Quan sát thực khi phục hồi đầu vào

## Nguồn và chất liệu món

Ba ảnh được gán vai rõ, prompt đọc lại khớp, nhưng v1 vẫn lấy hình thái sợi món từ TABLE08 hơn ảnh nem thật. Đây là bằng chứng output, không đủ để khẳng định cơ chế nội bộ model. Giả thuyết làm việc: ảnh scene mạnh có thể kéo theo texture món dù đã ghi vai tham chiếu.

Khắc phục đang kiểm: dùng v1 làm nền edit, thêm riêng ảnh thật và chỉ rõ mảnh thịt dẹt/bì không đều, giữ scene/geography. Không sửa kịch bản để né lỗi món. Chưa đóng nguyên nhân hoặc remedy khi chưa xem output sửa. Nếu hai output liên tiếp lặp MAJOR thì dừng báo owner.

## Giá và preset giọng

Hai preset được phục hồi bằng đúng source text, sample dài/ngắn/biểu cảm và base đã chọn; ID mới thực khác ID cũ. Sau mỗi preset, UI vẫn1050. Sau thêm một lần phát Đào và ảnh v1, UI vẫn1050. Không suy ra mọi lượt voice luôn miễn phí hoặc cùng prompt luôn cùng waveform.

Mở picker ở tab mới có thể tự hiển thị một giọng với sample trống; chọn rõ dòng preset trước khi kết luận dữ liệu không lưu. Khi chọn K20, UI đã đọc lại sample109 ký tự đã lưu. Không sửa performance/name chỉ để nghe lại.

## Tab và tải xuống

- Mở chi tiết v1 từng báo lỗi kiểm shadow root dù thực đã chuyển màn hình. Đã lưu screenshot, lấy URL thực, đóng tab và mở tab mới đúng URL; không sinh lại ảnh.
- Tải ảnh qua menu1K gốc thành công, thông báo download + file184283 bytes + hash/decode xác nhận. Không upscale hoặc ghi đè bản gốc.
- `downloadMedia(audio)` của preview Đào mở native audio document rồi timeout; không có file audio local mới. Không đồng nhất lỗi export với lỗi tạo/đã mất preset. Giữ màn hình Flow đúng giọng và sample cho owner nghe; không gọi API ẩn hoặc tự thay dịch vụ voice.
- Tỷ lệ UI9:16 không bảo đảm file ảnh đúng tuyệt đối: v1 thực768×1376. Giữ native nguyên vẹn, ghi metadata; không gọi đó là video720p đã đạt.

## Cách dùng lại

Kiểm output và exact hash trước production; paper PASS không thay media PASS. Giữ ba trạng thái riêng: saved preset, owner listening accepted, production voice/lip-sync accepted. Không dùng bằng chứng của trạng thái trước để đóng trạng thái sau.
