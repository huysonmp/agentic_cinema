# REC250 — BM cận riêng Khoai, gói chuẩn bị trình duyệt

**Cập nhật REC251:** owner “duyệt nhé,” cho đúng ảnh v2 và một lượt BM native 720p/K20/x1, tối đa 15 credit sau kiểm live. Xem `C01B-solo-BM-image-and-run-approval-251.json`. Các trạng thái chờ duyệt phía dưới là lịch sử lúc trình 250; native/tiếng/joins mới vẫn chưa được duyệt, BR vẫn giữ dependency gate.

Owner cho tiếp tục chuẩn bị và hỏi ở cổng cần duyệt. Giữ trần đợt quay 30 credit; đã dùng 7 tại REC249, đề xuất đã được cho tiếp tục trong phạm vi tối đa hai đầu ra tiếp theo, thêm không quá 23 credit, từng lượt x1 và không tự retry. **Ảnh mới vẫn chờ owner duyệt; chưa mở submit.** Không chuyển approval ảnh v1 hoặc giọng take cũ sang v2/native mới.

## Thay đổi và lý do

BM v1 vẫn chứa Đào, dẫn tới gaze/hover thay đổi trong nguồn thật và BR bị reset. V2 đổi coverage thành chỉ Khoai trong khung. Đào vẫn ngồi phía phải, ngoài khung; đây không phải xóa nhân vật khỏi câu chuyện. Cách này loại phần gaze Đào nhìn thấy ở BM khỏi nhiệm vụ hình, không chứng minh tay ngoài khung được giữ hoặc video sẽ đạt. Caption tự sinh là lỗi riêng; prompt mới mô tả spoken audio và clean cinematic frame, chưa chứng minh sẽ hết chữ.

## Chuỗi và nguồn giữ nguyên

C01A bản chọn 3,375 giây → BM chỉ Khoai nói “Khoan.” → BR góc bàn gốc, Đào nghe/nâng mắt/buông và thu tay → C02 bản chọn 7,541667 giây. Giữ K20, lời, món nguội, trục Khoai trái/Đào phải và các đạo cụ/canon đã chốt. Chưa mở C03A hoặc hoàn thiện phim.

BR_START giữ exact A80, hash `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb`; BR_END giữ C02F0, hash `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`. Contact ngoài khung BM UNKNOWN; phải đối soát continuity qua các nguồn/điểm nối nhìn thấy, không ghi PASS do phần tay đã khuất.

## Ảnh v2 và giới hạn

`02_refs/C01B_BM_START_v2_SOLO_CHATGPT_FOR_REVIEW_250.png`, SHA256 `ea705dc746d39d40240b21ebd21899cddd09f94b8b9a61250e219dbadc5fa67e`. Tạo bằng công cụ ảnh tích hợp ChatGPT từ ảnh BM v1 và A80, prompt nguyên văn trong cùng thư mục. Bản gốc generated-images, workspace và owner archive cùng hash; không ghi đè nguồn cũ.

Ảnh **941×1672**, gần nhưng không đúng tuyệt đối 9:16, không phải ảnh native 720p. Root đã xem ảnh output: Khoai rõ toàn mặt, miệng khép, hai tay nghỉ và nhìn sang phải; không thấy Đào, chữ hoặc hơi nóng. Đây là kiểm still, không phải continuity/motion/voice/lip-sync PASS. Chỉ thấy phần bát, đũa, chấm và món nằm trong cỡ cảnh; không ép toàn bộ bàn vào BM.

## Request dự thảo và cổng

`04_requests/C01B_BM_T02_solo_prompt_DRAFT_250.txt`: Ingredients, một ảnh v2, một saved custom K20; dự kiến Omni 1.1 Flash, native 720p, dọc, 4 giây, x1. Không tự đổi sang Frames vì UI Frames chưa chứng minh có custom voice. Giá 7 credit của lượt trước là tham khảo, không phải quote cuối có đầy đủ input v2.

Thứ tự: đóng góp chuyên môn → root tích hợp → reviewer khác maker kiểm ảnh/spec → owner duyệt ảnh → kiểm live đầy đủ → một BM → kiểm nguồn/range và nghe thực tiếng mới → BR chỉ nếu dependency đóng → kiểm bản nối thật. Không crop chữ, freeze, lấy đuôi môi khép ghép voice hoặc che lỗi bằng món. Nếu vẫn sai, HOLD, không tự dùng lượt BR thành retry.

## Timing và phạm vi nghiệm thu

A + C02 = 10,916667 giây đã chọn. BM/BR selected timing vẫn UNKNOWN; 4 giây native không đồng nghĩa phải dùng hết. Chỉ chọn range đủ từ/khẩu hình và hành động nghe–buông–thu; không tự giảm lời các đoạn sau để ép 30 giây. EDIT chốt EDL sau nguồn thực. Owner duyệt ảnh chỉ cho phép sử dụng ảnh đó trong request đã kiểm, không nghiệm thu native mới hoặc cả phim.

## Tích hợp các vai chuyên môn

Root đã đọc đầy đủ bốn báo cáo DIR, DOP, ACT và EDIT 250. Không thấy xung đột giấy tờ buộc đổi lời hoặc thứ tự cảnh. DOP ghi gaze Khoai sang phải khác gaze nhìn thấp ở nguồn A/v1: đây là thay đổi nhìn thấy, phải kiểm cut thật, không gọi match pixel. ACT yêu cầu loại giọng gằn/ra lệnh và chuyển động quá mức. DIR/EDIT giữ nhịp ngắt gọn, không lấy toàn bộ 4 giây nếu làm chậm phản ứng; các range vẫn chờ nguồn và nghe thực. Mọi góp ý được giữ trong gói này, không tự chép một biến thể khác vào request.

Reviewer khác maker sẽ kiểm ảnh/spec sau tích hợp. Các đóng góp chuyên môn không tự là review độc lập cuối, approval ảnh hoặc media PASS.

**Đã hoàn tất review độc lập:** `06_qc/C01B_solo_independent_250.md`, root đọc đầy đủ. Không thấy blocker still buộc remake; cho phép trình owner duyệt ảnh. Contact Đào ngoài khung, thay đổi gaze qua cut, motion, tiếng, native không chữ và joins vẫn chưa được chứng nhận. Trạng thái cuối bước chuẩn bị: **OWNER_IMAGE_REVIEW_PENDING — chưa submit video**.
