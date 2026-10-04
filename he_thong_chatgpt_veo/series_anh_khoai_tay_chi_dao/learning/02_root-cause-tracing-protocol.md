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

Bộ173 áp dụng lại sau owner duyệt: đọc chip bằng DOM không click, xác minh ảnh OPEN7 và token K20, xem screenshot cuối rồi submit không đổi compose. Nhận ba media và WAV PCM khớp. Biện pháp ngăn mất input đã được thực thi trong bộ173; chưa đồng nghĩa voice/reference output đạt. Giữ gate nghe và RCA mở đến khi có bằng chứng phân biệt nguyên nhân.

Owner tạm chấp nhận cả ba tại174. Ghi đúng mức provisional acceptance, không nâng thành giống hệt hoặc production PASS. Ba mẫu cùng bộ được chấp nhận cho phép dùng làm baseline bước tích hợp; không chứng minh yếu tố nào khắc phục170 hoặc ổn định ở mọi lời/cặp thoại. Giữ tách lỗi thao tác172, khả năng dùng173 và nguyên nhân170.

## 8. Bổ sung 2026-10-04 — kiểm tích hợp lời thật ở bộ 175

Sau duyệt mẫu đối chứng, chuyển sang lời thật và hai giọng phải ghi là kiểm tích hợp, không gọi thử nhân quả đơn biến. Mô tả diễn gắn với câu thử cũ không được đọc thành lời mới; chuyển nhịp diễn sang các câu đã duyệt, giữ preset/ID và lưu nguyên prompt mới. Kiểm cuối phải có ảnh + hai giọng + token vai tương ứng, báo giá thực và screenshot đã xem; không đổi ô nhập sau kiểm.

Bộ 175 tải được đủ ba MP4 bằng menu 360p gốc trong tab tải riêng; kiểm file thực và full decode trước bàn giao, đóng tab tải khi hoàn tất. WAV 48 kHz stereo PCM16bit giữ tốc độ/gain, kiểm hash PCM bằng bản MP4. File 16 kHz mono phục vụ ASR không dùng thay bản nghe của owner.

ASR cả ba nhận khác “nem/chảo/rang”; đây là chỉ điểm nghe lại, không tự chứng nhận giọng miền Nam hoặc phát âm sai. ASR gộp hai câu khác vai không chứng minh lẫn người nói. Kiểm hình thưa phát hiện B02 đổi món và B03 mất trang phục; không nhập voice gate với visual gate, không gọi file giải mã sạch là cảnh đạt. Số dư tài khoản thay đổi giữa các phiên không tự tăng ngân sách được duyệt; chi bộ 175 là 21, quyền chi còn 4.

## 9. Bổ sung 2026-10-04 — test rời không thay review toàn mạch

Owner hỏi kịch bản thiếu nhất quán sau bộ175. Đối soát prompt175 với script32 thấy bốn câu giữa đúng nguyên văn/vai, nhưng test bỏ tiền đề “Mùi này làm anh nhớ cái chảo” và không có hành động/payoff kế tiếp. Vì vậy cần phân biệt lỗi trình bày thiếu ngữ cảnh với tự sửa lời hoặc output nói sai; chưa kiểm tai thì không kết luận loại sau.

Tại176, owner chấp nhận test giọng; root ráp bản kiểm mạch30s với chín captions đúng script, B01 audio giữa và R01 cuối theo quyền tái dùng. Hai câu mở chưa có audio đạt thì để im lặng/nhãn, không dùng mẫu bị phản hồi lệch nhằm lấp timeline. Ghi rõ B01 chỉ là lựa chọn làm việc, thời gian caption từ ASR không chứng minh lời/vai nghe thực. Manifest nối yêu cầu → câu → nhịp hành động → nguồn/hash → slot → phạm vi approval; chỉ27,5s ảnh tạm không tự nâng thành production PASS. Quy trình học: khi trình một diagnostic rời, luôn kèm tiền đề, mục đích và vị trí trong toàn tập; sau acceptance tạo bản kiểm mạch trước sinh thêm lẻ tẻ. Không gọi các agent đã thực review nếu chỉ ghi hợp đồng hoặc chạy kiểm kỹ thuật.
