# 169 — Kiểm tùy chọn trả video không có âm thanh

Ngày 2026-10-03. Trạng thái: đã nhận đủ ba file; hình cần làm lại; chưa ghép vào EP01.

Chủ dự án nhắc vị trí tùy chọn âm thanh rồi yêu cầu tiếp tục. Giữ phạm vi hoàn thiện được duyệt tại 168, kịch bản 32, cặp giọng K20 Orus / D06 Aoede và hai khung 167. Không dùng lại khoản Quality 100 như một ngân sách riêng sau khi đã điều chuyển.

## 1. Tùy chọn thực sự làm gì?

Nút `chế độ cài đặt` ở thẻ lỗi âm thanh mở menu **Cài đặt lưới ô**, không phải bảng chọn model. Menu có hai công tắc khác nhau: `Âm thanh khi di chuột` và **`Trả về video không có âm thanh`**. Công tắc thứ hai được quan sát ở trạng thái bật sau khi mở từ thẻ lỗi; đã đặt bật và kiểm lại trước khi gửi bộ ba.

Không có ảnh trạng thái trước khi mở shortcut, nên không kết luận công tắc trước đó đã tắt hoặc mọi lỗi 168 xuất phát từ đó. Ảnh bằng chứng: `C:/Users/PC/Downloads/du_an_nem_bui/168_close_reaction_lite/audio-return-setting.png`.

Kết quả file xác nhận N01 và N03 không có luồng âm thanh, còn N02 có AAC. Vì vậy **không được coi công tắc này là chế độ ép tất cả video im lặng hoặc bảo đảm không chạy nhánh tạo tiếng**. Trong bộ này, tùy chọn cho phép nhận hai video được UI ghi “Chưa tạo âm thanh nào”. Khả năng tránh mọi lỗi âm thanh trong các bộ sau chưa được chứng minh.

## 2. Cấu hình và nhận file

Prompt giữ nguyên văn tại 168; START/END giữ đúng cặp 167. Veo 3.1 Lite, Khung hình, 9:16, 720p, 8 giây, x3, Tác nhân tắt, giá hiển thị 30. Đã gửi một bộ, không chạy lại trả phí.

Folder tài nguyên: `C:/Users/PC/Downloads/du_an_nem_bui/169_no-audio-return/`.

| Mẫu | ID trên Flow | File native trong Downloads | Kết quả âm thanh |
| --- | --- | --- | --- |
| N01 | `31b44fe2-b1ff-4c65-a0e2-e6296fe5b397` | `Dao_turns_head_slowly_20261003113041.mp4` | Không có audio stream; UI ghi chưa tạo âm thanh |
| N02 | `6fa25720-d08b-470d-b2ec-de0c39c297de` | `Dao_turns_head_slowly_20261003113115.mp4` | Có AAC; chưa nghe nghiệm thu |
| N03 | `bef7b227-ff0a-44b5-829e-59ea53a04164` | `Dao_turns_head_slowly_20261003113135.mp4` | Không có audio stream; UI ghi chưa tạo âm thanh |

Đã copy thành N01.mp4, N02.mp4, N03.mp4 trong folder 169. Cả ba đều H.264, 720 × 1280, 24 fps, 8,000 giây; giải mã toàn file không báo lỗi. Kích thước lần lượt 1.833.249 / 1.788.563 / 1.913.250 byte.

SHA-256 theo thứ tự N01–N03:

```text
2E582B655922E8D7D7B2018F115C445AAA058CD07E25B4E728A221DC524B89AB
10799E7A5B292CC877FFEA3CC8E8F5D4839CD5978DB15E6EDDDE56F869A33737
03264B2161AC3A9FF810C9D8904683071A945C89F1B2BF99A2408B8F21E3A551
```

Tải native 720p trên tab đầu chưa thấy file. Mở tab mới đúng URL N01 rồi tải native thành công; từ tab này tải tiếp N02/N03 cũng nhận file thực tế. Không tạo lại media để chữa tải, không dùng URL ẩn hoặc shell network. Phiên UI mới không còn các tab cũ; mở lại dự án không gửi generation trùng.

## 3. Kiểm hình và quyết định sử dụng

Root kiểm 16 khung mỗi mẫu, cách nhau 0,5 giây trên toàn clip; chưa review độc lập hoặc kiểm nghe. Gate lỗi thấy rõ đủ loại khỏi việc sử dụng toàn clip; kiểm dày đoạn cắt vẫn cần làm nếu sau này cứu một phần.

| Mẫu | Quan sát trong các khung kiểm | Gate |
| --- | --- | --- |
| N01 | Mở miệng trước và sau lúc nhìn trái; tay đưa ra bên phải rồi có cử chỉ ở bàn; người/xe nền đi qua | REWORK: không giữ môi khép và tay ổn định |
| N02 | Tay phải đưa lên gần cốc; miệng mở; sau khi nhìn trái lại cúi xuống rồi quay lên | REWORK: thêm động tác và không giữ một nhịp nhìn |
| N03 | Tay đưa ra bên phải; nhìn lên cao, mở miệng khoảng giữa clip rồi đổi về trái | REWORK: hướng mắt/đầu không đúng đường diễn và môi không ổn định |

Hai file không có tiếng vẫn mở miệng. Đây là bằng chứng **không âm thanh không đồng nghĩa diễn câm đúng yêu cầu**. Không gọi chuyển động miệng là lời nói chắc chắn, không gắn lip-sync PASS. Không coi món ngoài khung là đã đạt cảnh nâng-khựng hay chuyển-nhận.

Đã dựng bản đối chiếu `169_three-take-comparison_REWORK.mp4`: N01 0–8s, N02 8–16s, N03 16–24s; có nhãn loại mẫu, toàn bản đối chiếu tắt tiếng để xem hình. N02 gốc có tiếng vẫn được giữ riêng. File đối chiếu 24,000 giây, 720 × 1280, không audio, giải mã sạch; không phải bản EP01 hoặc đề nghị duyệt sản xuất. Có `comparison-contact.png` và ba grid toàn clip. Chưa dựng animatic v0.2 với bất kỳ mẫu này.

Script dựng nháp đã bổ sung tham số phiên bản, đoạn phản ứng và trạng thái chủ dự án cho phép tái dùng audio; không tự gán QC PASS. Đã kiểm `--help` và xác nhận chặn folder đầu ra có dữ liệu trước khi ghi file, giữ bản 166 nguyên trạng. Chưa chạy render nhánh phản ứng mới vì chưa có mẫu đạt; kiểm CLI không thay kiểm bản render thực tế. Nhãn chèn thử phản ứng vẫn ghi thiếu nâng-khựng, tránh coi một shot Đào thay được hành động Khoai.

## 4. Credit và kiểm soát chi tiếp

Số dư trước bộ 169 là 324, sau là **294**; chi ròng **30**. Ngân sách được phép chi trước là 124, còn **94**. Tổng 168–169 đã dùng 40 trong trần hợp nhất 134. Ảnh đối soát `balance-after-294.png`.

Không tự chi thêm 30 để lặp phản ứng cùng cách, không chuyển Quality để né lỗi. Với 94, dự toán có điều kiện cho hai nhóm audio đầu (2 × 18 theo giá lịch sử), một nhóm chuyển-nhận (30) và dự phòng là 36 + 30 + 28. Đây là phương án phân bổ tiếp, **không bảo đảm đủ tập**: phản ứng, quay đi, nâng-khựng, mở/kết và nối cảnh vẫn chưa khóa; giá phải đọc lại trước gửi. Không thay các cảnh thiếu bằng ảnh tĩnh ngầm hoặc bỏ lời/nhịp đã duyệt để khớp tiền.

## 5. Thiếu sót quy trình, giả thuyết và bước tiếp

- Đã xác định: preflight trước đây tìm tùy chọn âm thanh trong bảng composer mà bỏ menu Cài đặt lưới ô. Đã bổ sung kiểm công tắc và bằng chứng file thật; nhận được đủ ba mẫu trong bộ này.
- Quyết định thực thi: loại toàn bộ ba clip khỏi bản ráp mới; giữ nguyên câu chuyện và giọng; dừng lặp phản ứng cùng cấu hình, giữ 94 credit.
- Giả thuyết chưa xác nhận: chuyển ánh nhìn và biểu cảm trên clip 8 giây khiến model tự thêm diễn; chỉ có START/END và câu hạn chế môi/tay chưa đủ ràng buộc chuyển động giữa hai khung. Không tuyên bố đây là nguyên nhân gốc đã chứng minh.
- Vấn đề mở: chưa có phản ứng đạt, audio sáu câu đầu, nhịp quay đi/nâng-khựng/chuyển-nhận, kiểm nối cảnh và nghiệm thu âm thanh đầy đủ.
- Bước tiếp: ưu tiên gói sáu câu đầu theo đúng hai preset đã chọn, đo nhịp trước khi dựng. Với phản ứng, chuẩn bị phương án đầu vào chỉ cho một nhịp mắt/đầu ngắn và phần giữ; kiểm endpoint cùng continuity trước khi gửi. Đây là đề xuất thử tiếp, chưa tự sửa ảnh hoặc hạ gate. Không thử tiếp các lỗi hình đã biết bằng ghép tiếng hay Quality.
