# REC273 — C06 T02: sửa được cốc–bát, diễn chưa đạt hướng A

Ngày 12-10-2026. Trạng thái: **STOP_FOR_DIAGNOSIS / C06 NOT_SELECTED / C07 HOLD**. Một lượt sản xuất đã chạy, giá thực 7 credit; không chạy T03.

## Điều đã xác định và quyết định đã chốt

Owner chọn A sau REC272: giữ tạo hình đã duyệt; Khoai tỉnh, hơi ngượng khi bị bắt gặp, cố chữa cháy bình thản. Không biến anh thành người vui vẻ mời món. Chỉ một nét nhếch rất kín ở cuối câu. Đây là duyệt hướng diễn, không phải duyệt đầu ra, đổi giọng hay mở dự phòng.

Giữ C05 T02 và range đã chốt tại REC269. START của C06 là F65 nguồn C05, SHA-256 `f091e35fc7c779591c918c47ba34752a8a2c3b30de507cd99dc0e76143e83196`. Không thay bối cảnh hoặc đặt cốc ở vị trí mới thiếu nhịp nối.

Hai reviewer kiểm bản cuối trước sản xuất. Tôi tích hợp hai sửa: tay chuyển hướng ngay sau lời/nét nhếch, không thêm khoảng chờ trái chỉ đạo; Đào chuẩn bị bát nhận món ở cảnh sau, không nhận hoặc dịch bát trong C06. Preflight chỉ cho phép chạy có điều kiện, không bảo đảm chất lượng.

## Thực thi và bằng chứng

Dùng trình duyệt tích hợp theo skill Computer Use để kiểm cấu hình, gửi và tải đúng đầu ra qua UI. Account đã xác minh; số dư 924 → 917, khớp giá 7. Route Video Ingredients, Omni 1.1 Flash, 720p, 9:16, 4 giây, x1, Agent tắt, âm thanh bật. Đúng một ảnh START và một giọng Khoai/K20; tên/mô tả giọng được đối chiếu, không có bằng chứng opaque ID của backend.

Prompt cuối: [C06_T02_prompt_273.txt](restart_720p_v1/04_requests/C06_T02_prompt_273.txt), SHA-256 `cbe71e5a5a2085a2d6f27723a230dd5e6707659aa08ae436b3787782348db5b4`. Bản DRAFT được giữ riêng để truy vết, không phải bản gửi.

Native chủ sở hữu: `C:/Users/PC/Downloads/du_an_nem_bui/273_C06_T02/C06_T02_NATIVE_720p.mp4`. Bản gốc download và các bản lưu có SHA-256 `a2422a7e827ef80be3b95ff07335bd66e8ec1207d14af64a3763098e90c91b6a`. Native H.264 720×1280, 24 fps, 96 khung/4 giây; AAC stereo 48 kHz, 4,010 giây. Giải mã đầy đủ thành công. Không dùng bản preview làm native.

Root đã xem đủ 12 board chứa tất cả F0–95; xem thêm ảnh nguyên khung F0/F24/F42/F95 và START. Đọc đầy đủ maker và phản biện độc lập actual. Hai reviewer cũng xem đủ 96 khung, không đọc báo cáo actual của nhau. **Phạm vi là ảnh toàn bộ khung; chưa nghe hoặc kiểm AV liên tục.**

![Bằng chứng tải native](C:/Users/PC/Downloads/du_an_nem_bui/273_C06_T02/C06_T02_DOWNLOAD_PROOF.png)

## Kết quả kiểm actual

| Hạng mục | Quan sát | Kết luận trong phạm vi ảnh |
|---|---|---|
| Đầu cảnh | F0–13 giữ nét bị bắt gặp, môi hơi cụp | Cải thiện so T01; chưa kiểm seam dựng |
| Cốc và bát | Cốc giữ nâng suốt F0–95; bát Đào rỗng, riêng biệt | Không thấy lặp lỗi cốc lọt bát |
| Miếng A | Một miếng đi từ tay Khoai sang phía bát Đào, còn kẹp; cuối có khoảng hở | Chưa thả/nhận; không tự duyệt C07 |
| Diễn Khoai | F20–27, F34–35, F40–46 có nụ cười rõ hai khóe trong chuỗi khẩu hình; F48–95 vẫn mỉm cười | **MAJOR lặp yêu cầu diễn chưa đạt** |
| Tiếng/AV | Có audio; ASR ghi “Anh gấp cho em mà.” | Không thay việc nghe, không chứng nhận K20, “gắp”, nhịp hay sync |

Không đánh lỗi chỉ vì thấy răng lúc phát âm. Vấn đề là cả hai khóe nâng/nét cười lặp trong nhiều vùng lời và còn duy trì sau đó, thay vì nhếch một khóe rất kín ở cuối. Mày có nét hơi ngượng nhưng chưa bù được sắc thái vui ở miệng. Không gọi đây là lệch identity khi chưa có bằng chứng.

Cắt tail không sửa được nụ cười nằm trong lời. Không giấu người nói bằng insert món để gọi cảnh đạt. C06 chưa có range được chọn; không lấy endpoint chưa duyệt làm tham chiếu cho C07.

![Native C06 T02 — chưa chọn](C:/Users/PC/Downloads/du_an_nem_bui/273_C06_T02/C06_T02_NATIVE_720p.mp4)

## Nguyên nhân: đã biết và chưa biết

**Đã biết:** lỗi diễn có ngay trong native, trước khi ghép/cắt. START và đầu T02 đúng nét bị bắt gặp; biểu cảm chuyển thành cười trong phần nói. Prompt cuối đã chỉ đạo má thư giãn, không cười rộng, chỉ nhếch kín cuối câu. Vì vậy thiếu một câu cấm không phải giải thích đủ cho lỗi này.

**Chưa chứng minh:** mô hình/route, sắc thái giọng, ngữ nghĩa “gắp cho em”, mật độ prompt hay thời lượng là nguyên nhân duy nhất. T02 đổi cả hướng diễn và 6 → 4 giây, nên không tách được tác động từng biến. Cốc đúng lần này không chứng minh mọi cảnh 4 giây đều giữ cốc đúng.

**Khe hở quy trình đã chặn:** giấy đạt không thay actual đạt; đạo cụ tốt không bù diễn bị owner bác. Lỗi trọng yếu lặp qua T01/T02 kích hoạt dừng chẩn đoán theo scoped238. Không tự hạ severity, chạy thêm hoặc coi lựa chọn A là approval take này.

## Kinh nghiệm công cụ và lưu trữ

- Tool trình duyệt gọi trực tiếp đã hoạt động trong lượt này; không kết luận nó vắng mặt chỉ vì không được liệt kê trong tập metadata công cụ khác.
- Project có thể hiện grid cache cũ. Refresh UI rồi kiểm lại tài sản/tên và nguồn cụ thể; không coi grid thiếu là đã mất project.
- Picker hiện cần chọn tài sản **và** bấm “Thêm vào câu lệnh”. Đọc lại tên/chip và prompt sau chuyển trạng thái, không dựa vào snapshot trước đó.
- Kiểm quote sau khi hoàn tất cả prompt và ingredients. Khóa x1 và kiểm số dư trước/sau; không tự retry nếu output chưa tải.
- Native được tải qua nút UI đúng kích thước gốc; xác minh file, hash, probe và decode trước review. Lưu proof/config, native, toàn bộ khung và ASR riêng trong `273_C06_T02`.
- Agent actual không được chứng nhận tiếng hoặc sync từ khẩu hình/preset/ASR. Báo cáo registry cũ tại lúc reviewer bắt đầu được giữ như lịch sử, không phải hiện trạng cuối.

## Sổ và việc còn mở

Đã dùng **180/500**, còn **320**: first-pass 92, retake 73, post/rough 45, reserve 110 vẫn đóng. Account 917 không phải ngân sách còn được ủy quyền cho EP01. Chi lượt này 7, không có lượt chờ.

Giả định làm việc: giữ hướng A, identity, K20/D06, set, C05 đã chọn và câu thoại N06. Không mặc định owner muốn nới chuẩn diễn.

Bước tiếp theo: xem đúng native này, chẩn đoán sự chuyển nét mặt bằng nguồn/prompt hiện có và trình can thiệp có căn cứ trước lượt trả phí mới. Có thể nghiên cứu phương án tách diễn lời khỏi chuyển tay hoặc tham chiếu biểu cảm chặt hơn, nhưng **chưa chứng minh hiệu quả và chưa duyệt đổi coverage/route**. Không thêm câu cấm hoặc thử thêm dưới danh nghĩa QC. Nếu owner chủ động chấp nhận mức diễn hiện tại, phải ghi quyết định mới đúng take/phạm vi, rồi vẫn kiểm tiếng, AV và seam; không hồi tố T02 thành đạt A.

Hồ sơ: [run-registry-273.json](restart_720p_v1/06_qc/run-registry-273.json), [maker actual](restart_720p_v1/06_qc/C06_T02_maker_actual_273.md), [reviewer độc lập actual](restart_720p_v1/06_qc/C06_T02_independent_actual_273.md).
