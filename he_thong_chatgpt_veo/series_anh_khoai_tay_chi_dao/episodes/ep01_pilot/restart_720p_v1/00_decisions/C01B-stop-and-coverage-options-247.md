# C01B — Dừng lặp take và chốt hướng khắc phục

Trạng thái hiện hành — REC248: **OWNER CHỌN A, ĐƯỢC CHUẨN BỊ THIẾT KẾ COVERAGE C01B; CHƯA DUYỆT MEDIA HOẶC CHẠY TRẢ PHÍ**. Owner trả lời “a”, sau đó yêu cầu tiếp tục. Xem `C01B-coverage-direction-248.json`. Nội dung lựa chọn phía dưới giữ làm lịch sử quyết định; STOP tuyến T01/T02 không tự được gỡ.

## Hiện trạng

Đã nhận xác nhận độc lập T02 ngày08/10/2026:25 mẫu và ảnh nguồn, root đọc đầy đủ. Lặp đúng MAJOR start-pose, trong khi đoạn thu/rest có cải thiện riêng; thêm deviation Khoai nâng tay ngoài yêu cầu. Root chốt STOP, không tự T03; xem `C01B-repeated-start-stop-247.json`. Đây là trạng thái mới thay phần pending trong lịch sử mô tả bên dưới.

T01 đã kiểm độc lập trên native và bản ghép thực: lỗi lớn ở đầu C01B, tay trong đổi sang vùng vành trái rồi xuất hiện một lượt hai tay tiến tới đĩa. Lỗi có sẵn ở native, không do Flow ghép đảo clip hoặc dùng nhầm đuôi C01A kéo đĩa.

T02 giữ đúng input, custom K20, lời “Khoan”, shot, mode và cấu hình; chỉ sửa cue tiếp nối, hướng tay trong, sắc diễn và bảo toàn món. Output gốc đã tải:720×1280,24fps,96 khung,4 giây; số dư1.013→1.006, trừ7 credit. Root xem24 mẫu và frame0: thu tay sớm hơn, nhưng start tay trong vẫn sát vành trái thay vì gần bát như cuối C01A. Root dừng sinh thêm theo238; xác nhận độc lập focused T02 còn pending tại thời điểm lập đề xuất này.

Đã dùng74/500, còn426; trong đó110 dự phòng chưa được giải ngân. Không tự T03, không mở C03A, không thay giọng hoặc bỏ beat.

## Nguyên nhân theo tầng

- **Input/thao tác:** đã đối soát đúng ảnh cuối C01A, ID ảnh, một custom K20 đúng ID/performance, không D06; prompt readback khớp, cấu hình và final quote đúng. Không có bằng chứng chọn nhầm input.
- **Request:** cue T01 “giữ ý định lấy tới khi nghe” có thể dẫn tới reach mới. T02 thay bằng contact đang có → nghe → buông → thu và tay trong chỉ về thân/bát; đây là corrective bundle, không thí nghiệm chứng minh riêng một câu gây lỗi.
- **Output/tuyến sản xuất:** yêu cầu giữ một tư thế đang chuyển động tại điểm nối cùng góc máy chưa được output thực đáp ứng. Input đúng và câu “giữ nguyên” không bảo đảm video start khớp nguồn. Chưa biết cơ chế nội bộ hoặc tính năng frame-lock nào có thể áp dụng với giọng; không tuyên bố đã chứng minh giới hạn tuyệt đối của model.
- **Dựng:** bản ghép tái hiện lỗi native; chỉnh raster/PTS khi xuất là vấn đề format riêng, không nguồn chính của hành động sai.
- **Quy trình:** gate actual start/join đã chặn clip trước mở rộng sản xuất. Không dùng paper PASS, endpoint đẹp hoặc audio approval để đóng lỗi hình. Cần đổi đặc tả/tuyến có kiểm chứng, không thêm lời hứa “exact” rồi chạy vòng tiếp.

## Một quyết định cần owner trả lời

**A — Cho phép thiết kế lại coverage riêng C01B (khuyến nghị sơ bộ).**

Đề xuất một shot Khoai nói “Khoan” có mặt/miệng rõ, sau đó shot Đào nhận lời ngắt và buông–thu tay, rồi nối C02 kể ký ức đã chọn. Đây là nhịp đạo diễn có động cơ, không cận bát nem thay mặt người nói. Giữ toàn thoại, tính cách, món/bàn, chất giọng và C01A/C02 đã chọn làm đầu vào. Vẫn phải thể hiện và kiểm động tác buông/thu thực; không audio overlay lên miệng khép, dissolve/freeze/speed hoặc cắt né hành động để giả PASS.

Hệ quả: cần DIR/DOP/ACT/EDIT chuẩn bị coverage, khung tham chiếu và phân bổ nhịp mới trước tạo; có thể tăng số shot. Không hứa tính năng, tỷ lệ đạt hoặc giá từng lượt trước kiểm live. Owner chọn A là chốt hướng khám phá, **không duyệt media hoặc công cụ/giọng mới**. Nếu muốn dùng kỹ thuật/tool ngoài quyền238, trình riêng sau kiểm tính khả thi.

**B — Giữ liền góc hai người, cho phép thiết kế lại tư thế đầu–cuối C01A/C01B.**

Giảm động tác phụ của tay trong, tạo lại nguồn và take cần thiết để một tay đang tiếp xúc còn tay kia có trạng thái nghỉ rõ. Giữ câu chuyện và lời, nhưng có thể phải thay phần hình C01A vốn đã chọn, nên cần khung mới được kiểm/duyệt đúng checkpoint. Hệ quả: nhiều phụ thuộc hơn, vẫn phải chứng minh output giữ trạng thái; không mặc định thêm prompt là đạt.

**Điều có thể tiếp tục mà không hỏi:** giữ nguyên source/voices/C02, lưu T01/T02 và report, đối soát ngân sách, hoàn tất chẩn đoán đã giao. **Điều phải kiểm trước kết luận:** xác nhận độc lập T02, tính khả thi của coverage/tuyến, giá thật và nhịp toàn30 giây. **Chưa mở rộng:** scene sau, final/master/export, công cụ mới hoặc reserve.
