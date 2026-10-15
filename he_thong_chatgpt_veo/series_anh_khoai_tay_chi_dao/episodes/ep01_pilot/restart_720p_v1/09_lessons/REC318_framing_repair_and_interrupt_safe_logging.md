# REC318 — Sửa bố cục phải đúng đối tượng; lưu prompt trước tác vụ dài

## Quan sát và nguyên nhân giả thuyết

Nguồn T-caught có sẵn đạo cụ sát/cắt biên; yêu cầu vừa giữ khung vừa đưa toàn bộ đạo cụ vào khung tạo sức ép bố cục. V1/v2 vẫn cắt cốc/rau. Đây là lỗi thực thi quan sát được; nguyên nhân model giữ bố cục nguồn mạnh là **giả thuyết**, không kết luận đã bóc hết cơ chế model.

Đổi chiến lược có ghi rõ: v3 về v1 chỉ dịch hai vật thể vẫn chưa đủ mép rau; v4 dựng lại khung thiết lập theo nguồn nhận diện/state, rồi v5 chỉ dịch cốc. V5 nhận đủ vật thể ở still, nhưng không đạt bằng chứng pixel lock, motion hoặc cùng geometry các góc khác.

Không “khắc phục” bằng việc chuyển rau sang một vị trí không hợp bối cảnh, nhân đôi cốc hoặc bỏ bát riêng. Trong suốt sửa giữ quan hệ rau trước-trái, cốc ngoài Đào, hai bát/two chopstick pairs trước gắp. Thay kích thước/vị trí tương đối nhỏ có redraw; cần kiểm các cảnh liên quan, không coi local request là local pixel edit thực.

## Lỗi lưu trữ khi user tiếp tục giữa tác vụ

Promptset ban đầu chỉ giữ trong store của orchestration. Sau lượtv5 bị ngắt, không đọc được các key prompt trước ở lượt tiếp; có một lần gọi orchestration thất bại vì thiếu prompt, **không có imagegen mới được gọi ở lần lỗi đó**.

Khắc phục: copy output đã nhận vào project; phục hồi nguyên văn promptv1–v4 từ nội dung toolcall còn trong hội thoại, không gọi là runtime export byte-exact; lưu promptv5 ra file sau khi nhận output. Từ entry/exit/mid đã ghi prompt ra file trước khi sinh. Từng output có tên/hashes/lineage và trạng thái không chọn hoặc candidate. Không dựa vào store qua interruption để bảo toàn record.

V5 bị ngắt chưa trả output. Trước gọi lại đã kiểm thư mục generated_images của đúng chat: mới nhất vẫn làv4, không tìm thấy filev5. Chỉ sau đó gọi lại một lần và nhậnv5. Đây không bảo đảm backend không xử lý call bị ngắt, chỉ khẳng định không có output trả về/tệp mới được tìm thấy ở thời điểm kiểm; Flow không liên quan đến các call built-in này.

## Quy tắc áp dụng lần sau

1. Lưu prompt cùng input có thứ tự vào project **trước** call dài, không đợi lúc bàn giao.
2. Nếu ngắt, kiểm output/thư mục/scope trước retry; không đếm attempted thành completed.
3. Lặp lỗi biên thì dừng nhánh sửa chung, phân biệt giữ pixel, giữ góc và chỉ giữ nhận diện. Mỗi cách có ảnh hưởng khác tới continuity; ghi rõ đã đổi gì.
4. Mỗi thay đổi kiểm lại toàn scene inventory và các shot kề, không chỉ vật vừa sửa.
5. Native kích thước có thể đổi940/941 và1672/1673 giữa các output; đo từng tệp, không kế thừa format từ tên “9:16”.
6. Saved voice có tên/mô tả đúng không đồng nghĩa tiếng mới, khẩu hình hay exact WAV đã nghiệm thu.

Root làm kiểm tĩnh, chưa reviewer độc lập/motion/AV PASS. Không ghi kinh nghiệm này vào memory hệ thống; chỉ lưu bài học trong project theo yêu cầu nhật ký của owner.
