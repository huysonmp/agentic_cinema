# REC264 — Duyệt bản dựng thô tới 35 giây; kiểm nguồn C05

## Quyết định và công việc đã làm

Owner trả lời “a” cho lựa chọn A tại REC263: bản dựng thô được dài tối đa 35 giây, giữ lời và nhịp tự nhiên; vẫn ưu tiên gần 30 giây nếu cắt an toàn. Không duyệt phim cuối, tăng trần 500 credit hoặc mở dự phòng 110.

Đã chạy đúng một C05 T01: Omni 1.1 Flash, Ingredients, 720p, dọc 9:16, 4 giây, x1, Tác nhân tắt, âm thanh bật. Đầu vào là đúng F143 cuối C04 đã chọn, prompt cuối REC263 và chỉ preset Đào/D06. Root đối soát ảnh, tên preset và mô tả giọng hiển thị, đọc lại prompt khớp tuyệt đối. UI picker không lộ ID giọng opaque; không tuyên bố đã xác minh backend ID.

Đã tải bản gốc qua nút tải của Flow. Nguồn `restart_720p_v1/05_native/EP01_720_C05_T01_NATIVE.mp4`, SHA-256 `82478230b9a4c298f3a28f4432474822e406586693c0a49381278cd3d7d1f648`: 720×1280, 24 fps, 96 khung, hình 4 giây; giải mã đủ, bản nguồn được giữ nguyên. Bản dành cho owner: `C:/Users/PC/Downloads/du_an_nem_bui/264_C05/C05_T01_NATIVE_720p.mp4`.

Skill Computer Use được dùng để kiểm đầu vào, trạng thái âm thanh, giá và tải native qua giao diện. Không dùng API ẩn, không sinh lại để sửa lỗi tải, không cài công cụ mới.

## Kết quả kiểm và nguyên nhân

**C05 T01: REWORK / NOT_SELECTED. C06 giữ lại.** Root kiểm đủ 96 ảnh khung qua 12 board, thêm ảnh nguyên khung F0/32/63/95 và START F143. Maker và phản biện độc lập kiểm riêng theo cùng target; phạm vi là ảnh từng khung, không phải xem/nghe AV liên tục.

- Đã giữ: mặt cả hai người, miếng nem A trên đôi đũa riêng của Khoai, chưa ăn/trao/thả; Đào không lặp quay đầu; người nghe không có khẩu hình nói rõ; món nguội, rau và hai đồ chấm còn trong bố cục.
- Lỗi lớn ngay F0: cốc của Đào bị đặt lại xuống sát bàn, thay vì giữ tư thế nâng dưới mặt từ cuối C04.
- Lỗi lớn F0–95: bát riêng của Đào, có rõ trong START, không còn hiện trong nguồn C05. Không đủ bằng chứng để gọi đó chỉ là bát bị cốc che. Đây là vật thể cần cho chuỗi nhận và thả miếng nem, không được cho xuất hiện lại vô cớ ở C07.
- Không có đoạn cắt nào khôi phục hai trạng thái đó; lỗi đã có trong native, trước dựng. Chưa ghép C04→C05 và không ghi điểm nối đạt.

Nguồn ảnh và prompt đã đối soát đúng, không có bằng chứng chọn nhầm ảnh hoặc tải nhầm kết quả. Tầng lỗi quan sát được là **tái dựng trạng thái đầu và đồ vật trong output**. Ingredients dùng ảnh tham chiếu, không khóa pixel khung đầu. Giả thuyết góp phần: câu “inherited position below her mouth” chưa khóa độ cao cốc đủ cụ thể; yêu cầu hai bát còn ở mức tổng quát, chưa mô tả độc lập bát Đào so với cốc. Không có bằng chứng rằng đó là nguyên nhân duy nhất hoặc thêm chữ chắc chắn sẽ sửa được.

Kiểm board ban đầu cho thấy diễn và miếng A ổn nhưng chưa đủ để kết luận toàn bàn ăn đạt. Đối chiếu **từng đồ vật trong START với F0 nguyên khung** đã phát hiện reset/mất bát. Giữ bước này trước khi nhận clip hoặc kiểm điểm nối, không chỉ kiểm đũa và miệng.

## Tiếng và giới hạn bằng chứng

Công cụ ASR cục bộ đã có, chạy offline tiếng Việt, không initial prompt, nhận dạng: “Chờ em quay lưng nữa à”, ước lượng 1,10–2,44 giây. Đây không phải chứng nhận D06, một người nói, biểu cảm hoặc đồng bộ môi–tiếng. Root và reviewer không nhận đã nghe. Đã gửi native để owner nghe **riêng tiếng**; approval này không duyệt hình và không tự chuyển sang take mới.

Chưa chọn range C05, chưa dùng cả 4 giây làm độ dài dựng. Những range tới C04 hiện vẫn 566 khung / 23,583333 giây. Quỹ thời lượng còn tới 35 giây là 11,416667 giây; C05–C09 thực tế chưa đo đủ. Không bảo đảm phim đã vừa 35 giây.

## Chuẩn bị sửa — chưa chạy lượt thứ hai

Đã viết draft T02 cùng ảnh/giọng/lời/model/camera; chỉ làm rõ trạng thái cốc nâng ở ngang vai/ngực trên, và bát gốm rỗng riêng của Đào phải hiện dưới cốc trên bàn. Không tự đổi sang cảnh cận món, giảm mặt người nói, đổi lời hoặc cho Đào đặt cốc xuống để hợp thức hóa lỗi.

Draft và phiếu: `restart_720p_v1/04_requests/C05_T02_prompt_DRAFT_264.txt`, `C05_T02_preparation_264.json`. Chưa upload, chưa kiểm quote mới, chưa submit. Cần đọc đầy đủ maker và phản biện draft hiện hành, tích hợp bất đồng rồi mới đóng live gate. Nếu cùng lỗi lớn cốc/bát lặp ở output kế tiếp, dừng chẩn đoán, không tự chạy T03. Không gọi sửa prompt là kết quả đã sửa.

Root đã đọc đầy đủ hai báo cáo actual và phản biện draft. Bản cuối riêng `C05_T02_prompt_264.txt`, SHA-256 `33d87040e8fe90ddb69fca46f2942e62f56d685c40248ac6f78173e55056c3c3`, giữ độ cao đúng ảnh thay vì ép theo cằm/vai; thêm môi khép tại entry, chỉ Đào mở khi nói, và cốc không thay/che bát. Không áp đề nghị dịch cốc ngang thành pose mới: giữ vị trí tay ngoài kế thừa và yêu cầu bát đọc được. Draft cũ không bị ghi đè. Maker và reviewer độc lập đã đọc lại đủ, xác minh hash bản cuối và bổ sung kết luận; root đọc đủ cả hai phần bổ sung. Chỉ GO đầu vào và bước live sau đó, không là GO trả phí trước kiểm live hoặc output đạt.

## Chi phí, vấn đề mở và bước tiếp

Chi lượt này 7 credit: số dư cùng tab 934→927. So với lần quan sát trước 884 có tăng 50 chưa giải thích; không tính đó là quyền chi thêm hay chi phí EP01. Sổ dự án: **156/500 đã dùng, còn 344**, gồm lượt đầu 102, tạo lại 87, sau rough cut 45, dự phòng 110 đóng.

Đã chốt: hướng thời lượng A, kết quả T01 không được chọn và input bản cuối T02 qua kiểm giấy hiện hành. Giả định: giữ canon, hai giọng, cùng A, bố cục bàn và tuyến đã dùng. Còn mở: tiếng C05 T01, live gates T02, khả năng giữ cốc–bát của output mới, range và điểm nối thực. Bước tiếp: live gates cho một sửa có mục tiêu trong scoped238 → kiểm lại toàn nguồn → xử lý checkpoint tiếng/AV trước C06. Không cần owner duyệt phần hình lỗi đã rõ. T02 chưa chạy trong REC264.
