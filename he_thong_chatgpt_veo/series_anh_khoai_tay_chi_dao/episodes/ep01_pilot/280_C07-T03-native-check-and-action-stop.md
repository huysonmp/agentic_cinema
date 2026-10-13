# REC280 — C07 T03 đã chạy; dừng vì hành động và trạng thái sai

Ngày 13-10-2026. **C07 NOT_SELECTED / SOURCE_REWORK / NO_T04 / C08 HOLD.** Đã thực hiện đúng một lượt owner duyệt; không tự mở thử nghiệm khác từ câu “tiếp tục đi nào”.

## Kết quả thực tế

T03 giữ được Khoai và Đào là hai nhân vật thực phẩm, có hai bát và đủ bối cảnh. Nhưng **chưa đạt C07**:

- Tư thế tay/miếng nem bị đặt lại ngay đầu, không tiếp đúng điểm cắt C06.
- Khoảng 0,67–1,38 giây, Khoai đưa nem tới miệng Đào; cô há miệng nhận thay vì chuẩn bị bát. Miếng vẫn thấy trên đũa sau đó, nên không khẳng định đã nuốt/thả thật.
- Khoai mở miệng ở đầu dù là vai im lặng; chưa nghe nên không suy thành chắc chắn sai người nói.
- Đào hạ cốc xuống bàn và kéo bát mình quá xa sang trái; bát Khoai vẫn có, không phải lỗi lấy nhầm bát như T01.

Đã tải bản gốc **720×1280, 24 fps, 144 khung / 6 giây**; giải mã toàn file thành công. SHA `ae876978fb19265601e4082c5e4cb7079c481786b11a2f8309be362b0881a50e` khớp giữa bản download, bản owner và repo. Root xem đủ 18 bảng / 144 khung cùng ảnh C06 F56 và các khung nguyên kích thước. Chưa nghe thực tế hoặc xem AV liên tục; không ghi tiếng D06/N07/sync đã đạt.

Maker và reviewer đã được giao actual run theo REC217, nhưng **cả hai gặp giới hạn sử dụng trước khi hoàn tất báo cáo**. Gate phản biện độc lập còn HOLD. Không nhận hai agent đã duyệt T03; kiểm root đủ để bác các lỗi rõ, không thay gate chọn nguồn đạt.

## Nguyên nhân đã xác định và phần chưa biết

**Đã xác định:** lỗi nằm trong bản gốc Flow, trước ghép/cắt. Lịch sử đúng job có cả ảnh pair, exact ảnh cảnh và một voice chip; prompt khớp bản đã khóa. Không có bằng chứng lỗi tải hoặc việc gỡ chip tạm ở REC279 gây ra T03. Request mới vẫn không giữ được tư thế đầu và chuỗi nhận bằng bát.

**Chưa xác định:** nguyên nhân nội bộ khiến mô hình diễn giải thành đút ăn; mức ảnh hưởng của từng ảnh/prompt/voice. Take mới không hóa người thật không chứng minh riêng ảnh pair đã chữa lỗi, vì ảnh và prompt cùng thay đổi so T02. Không kết luận rằng chỉ thêm câu cấm, chuyển chất lượng hoặc chạy tiếp sẽ sửa được.

**Bài học quy trình:** kiểm đầu vào đạt không phải khóa động tác đã được chứng minh. Tuyến Ingredients vẫn dùng tham chiếu mềm; nhiều chỉ dẫn phải được thực hiện cùng lúc và không có điểm đầu/cuối khóa cứng. Tách kiểm nhận diện, trạng thái đầu, hành động, tiếng và điểm nối; không dùng một phần tốt để bù lỗi còn lại.

Chi tiết mong đợi/quan sát theo frame tại `restart_720p_v1/06_qc/C07_T03_root_actual_280.md`; sổ chi và nguồn gốc request tại `restart_720p_v1/04_requests/C07_T03_run_280.json`.

## Ngân sách, tiến độ và tài nguyên đã lưu

Quote/debit đúng **10 credit**, account 1.023→1.013. Dự án đã chi **217/500**, còn **283**: lượt đầu 82, làm lại 46, hậu kỳ 45, dự phòng 110 vẫn đóng. Không có khoản giữ chờ, không thêm lượt hoặc chi mới từ việc kiểm.

Đã chọn đến C06 vẫn dài 689 khung / 28,708333 giây; C07 chưa được cộng vào. Còn 151 khung / 6,291667 giây cho C07–C09 tới bản thô 35 giây. Mục tiêu xuất cuối 30 giây giữ nguyên; chưa đủ nguồn/range để chốt timing hoặc tiến độ theo phần trăm.

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/280_C07_T03/` chứa native, WAV giữ âm thanh nguồn, evidence kỹ thuật, toàn PNG/bảng ảnh và screenshot nhận job/tải. Native không bị sửa, không dựng nối một source lỗi rồi trình như candidate đạt.

## Một quyết định nền tảng trước khi chuẩn bị request khác

Đây là **đề nghị chuẩn bị và đánh giá khả thi, chưa phải quyền chạy trả phí hoặc cam kết giải pháp**:

| Lựa chọn | Việc chuẩn bị | Hệ quả / rủi ro |
| --- | --- | --- |
| **A — tách kiểm soát hình và thoại (khuyến nghị sơ bộ)** | Lập gói hình C07 với exact điểm đầu và ảnh đích bát nhận; đánh giá Frames Start/End cho phần hình. Lập riêng nguồn N07/D06, cách đặt lời và kiểm khẩu hình/nhịp trên hình; trình lại trước thay route hoặc chạy. | Giảm phụ thuộc voice reference và nhiều hành động trong cùng lượt. Nhưng theo kiểm REC278, Frames không có saved-voice slot; ghép riêng **không tự giải quyết khẩu hình**. Không chấp nhận mặt kín miệng trong lúc nói hoặc lấy tiếng sai/thiếu làm nguồn. Chi phí và cách thực hiện tiếng còn phải xác minh, chưa xin credit. |
| B — giữ Ingredients/D06, thiết kế lại nhiệm vụ hình tối thiểu | Lập thẻ C07 chỉ nhìn–đáp–đưa bát trong khi Khoai giữ A; kiểm lại ranh giới chuyển động từ C06 và điểm kết bằng ảnh, rồi mới trình một request. | Giữ tuyến voice hiện có, ít đổi kỹ thuật; nhưng vẫn tham chiếu mềm và cơ chế reset/cho ăn chưa được khắc phục. Không chạy lại nguyên prompt hoặc coi simplification là đã chứng minh tốt hơn. |

Không đổi N07, giọng D06, nhận diện, người nói, câu chuyện hoặc chuyển cảnh nhận món vào miệng. Không bỏ C08 thả hoặc C09 miếng B để ép thời lượng. Cả hai hướng phải đóng gate review mới; agent actual đang thiếu report nên chưa được đánh dấu sẵn sàng sản xuất.

**Owner cần chốt:** chọn A để chuẩn bị phương án tách kiểm soát hình–thoại, hay B giữ Ingredients và thiết kế lại nhiệm vụ hình? Chỉ chốt hướng chuẩn bị; chưa mở T04, reserve hoặc quyền chi mới.
