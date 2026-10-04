# Truy lỗi cuối chặng về nguồn và nguyên nhân cốt lõi

Ngày 2026-10-02. Chủ dự án yêu cầu ghi kinh nghiệm và thực hiện bóc tách nguyên nhân, không chỉ sửa biểu hiện cuối. Áp dụng cho lỗi hình, thoại, diễn xuất, đạo cụ, nối cảnh và bàn giao; không thay các gate phê duyệt hiện có.

## 1. Nguyên tắc

Tách bốn lớp: lỗi quan sát được; cơ chế gây lỗi đang giả thuyết; sai sót quy trình đã chứng minh; biện pháp đã thử hiệu quả. Không gọi một biện pháp che lỗi là xử lý nguyên nhân. Không gọi checklist hay prompt đã viết là kiểm đã chạy. Ba đầu ra cùng prompt kiểm độ lặp lại trong bộ, không chứng minh quan hệ nhân quả hoặc tỷ lệ lỗi chung của công cụ.

## 2. Truy ngược theo chuỗi

Đầu ra bàn giao → file native → thao tác tải/ghép → model và cấu hình thực → prompt thực gửi → gói đạo diễn/chuyển động/thoại → ảnh và tư liệu nguồn → yêu cầu/kịch bản đã duyệt.

Với từng mắt xích phải có phiên bản, đường dẫn/mã tài nguyên, hash khi có file, thời điểm, trạng thái duyệt và người thực kiểm. Nếu thiếu liên kết thì ghi thiếu; không suy dữ liệu từ tên file. Ghi riêng lỗi xuất hiện ở đâu và vì sao gate trước không phát hiện/ngăn được.

## 3. Quy trình xử lý

1. Đóng băng bằng chứng: giữ file lỗi nguyên bản, prompt nguyên văn, ảnh nguồn, UI cấu hình, log và số dư. Không sửa đè bản đã duyệt.
2. Định nghĩa defect: vùng, thời điểm, expected/observed, mức ảnh hưởng. Không gộp khói, cử chỉ và chữ thành một lỗi.
3. Kiểm nguồn trước: ảnh, crop, nguồn món, state nhân vật, hướng trái/phải; đọc lại yêu cầu và đầu vào đúng phiên bản. Kiểm công cụ/tải/ghép để tách lỗi dịch vụ khỏi lỗi nội dung.
4. Lập bảng giả thuyết: bằng chứng ủng hộ, phản chứng, phần chưa biết, phép thử phân biệt và phạm vi chi phí. Ưu tiên thử phân biệt được giả thuyết thay vì tăng câu cấm.
5. Tạo đối chứng tối giản; giữ các điều kiện có thể giữ, đăng ký trước biến thay đổi. Thay cả nhóm prompt chỉ cho phép kết luận về nhóm, không quy cho một từ. Không có seed hoặc model revision phải ghi rõ.
6. Chạy ba Lite theo quyết định hiện hành, lưu cả kết quả lỗi. Nếu đổi cấu hình phục hồi, tách nhánh trong log. Review toàn clip khi công cụ cho phép; ảnh mẫu chỉ là kiểm có giới hạn. Không chọn mẫu đẹp để bỏ qua hai mẫu lỗi.
7. Tái đưa yêu cầu từng lớp: trạng thái vật lý → hành động → thoại → tích hợp. Kiểm regression cả defect gốc và mặt/món/đạo cụ/giọng/nối cảnh. Tái lập lỗi khi bỏ biện pháp và giảm lỗi khi áp dụng là bằng chứng mạnh hơn một lượt thành công.
8. Đóng hồ sơ chỉ khi có căn cứ: nguyên nhân xác nhận hay chưa biết, biện pháp ở đúng nguồn, kiểm lại phạm vi gốc, reviewer thực chạy và quyết định owner. Nếu chỉ khắc phục được triệu chứng thì ghi workaround, không ghi RCA closed.

## 4. Mẫu hồ sơ tối thiểu

- Defect ID, stage phát hiện, tiêu chí bị vi phạm, file/frame/time.
- Chuỗi nguồn/phiên bản/hash và quyền thao tác.
- Sai sót phát sinh và sai sót bỏ lọt tại gate: phân biệt.
- H1/H2: dự đoán, bằng chứng, phản chứng, điều kiện phân biệt.
- Control/treatment: prompt chính xác, biến đổi và biến cố định, model/UI/audio/START/END/seed, chi phí.
- Kết quả đủ cả ba, phạm vi review, hạn chế và reviewer.
- Kết luận OBSERVED / SUSPECTED / SUPPORTED / CONFIRMED_IN_TEST_SCOPE / UNRESOLVED.
- Biện pháp nguồn, regression, quyết định owner và bài học có điều kiện tái sử dụng.

## 5. Bài học đầu tiên: hơi trắng ở Nem Bùi

Hồ sơ 126/130 → 132/133/134 → 135/136: `extra steam` không mô tả đúng yêu cầu không hơi; tăng danh sách cấm không khống chế được defect trong các bộ mới. Bỏ thoại/mùi vẫn có hơi nên chưa quy nguyên nhân chỉ cho thoại. OPEN7 xem tĩnh không thấy vệt hơi rõ; R03 của vòng 119 cùng ảnh không thấy hơi trong ảnh mẫu, nhưng lỗi tay vẫn còn. Không suy ảnh hoặc Lite luôn lỗi.

Lỗi quy trình đã thấy: dồn nội dung checklist vào prompt và thiếu đối chứng tối giản trước các lần tăng ràng buộc. Cơ chế sinh hơi của model chưa xác nhận. Prompt tối giản là phép thử chẩn đoán, không phải công thức thành công hay cắt giảm tiêu chuẩn nghệ thuật. Chi tiết đối chứng tiếp theo tại hồ sơ 137.

## 6. Bổ sung2026-10-04 — giọng K20 khác audition

Hồ sơ171: phải tách selection approval khỏi integration PASS; thư viện đúng preset chưa chứng minh request video dùng đúng exact nguồn hoặc bảo toàn identity. Đối chiếu PCM loại trừ extraction, không thay so nghe. History preview undefined là bất thường UI, chưa là nguyên nhân server sinh sai. Không quy lỗi cho warm/low/intimate hoặc thiếu @Voice khi chưa đối chứng; không mặc định Quality sẽ sửa. Trước cặp thoại cần control một người/cùng sample; lưu baseline audio/hash khi UI cho phép, nguồn và request riêng; không để tên trùng thay ID. Agent được thiết kế nhưng chưa nghe thực thì ghi chưa chạy gate. Cơ chế sinh lệch vẫn UNRESOLVED, không RCA closed.

## 7. Bổ sung2026-10-04 — control172 bị mất ảnh trước submit

Bấm chip compose để kiểm ảnh đã gỡ ảnh OPEN7, làm bộ172 không còn đối chứng đã duyệt. Root lưu screenshot cuối nhưng chưa xem lại, nên vẫn gửi x3. Đây là sai sót preflight xác nhận, không suy170 cũng mất ảnh. Kiểm nguồn qua picker/mention-ID, không dùng click chip để mở detail; bất kỳ thao tác nào thay compose đều làm lần kiểm trước hết hiệu lực. Trước submit phải readback chip loại/số lượng, không icon error, token đúng ID, route/quote và xem screenshot thực. Nếu control sai input thì giữ media/chi phí/log, đánh dấu INVALID_CONTROL, không dùng kết quả xác nhận model/reference. Không tự retry vượt cap nhằm che lỗi thao tác.
