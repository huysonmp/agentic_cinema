# REC261 — Chọn C03B ngắn, kiểm C04 và giữ C05

Ngày 09-10-2026. Owner chấp nhận đúng C03B ngắn bằng “ok đấy”, rồi yêu cầu tiếp tục. Chọn range `[0,50)` / 2,083333 giây, hash `87a5d8639ce89ae6bfc4c99cc0f2e67ed7dd65737e57f5b2437634f5c091481c`. Approval này xác nhận K20, trọn “Chờ mẹ quay lưng.” và nhịp/khẩu hình của đoạn ngắn; không duyệt native đủ 4 giây hoặc toàn bản nối 17,583 giây.

## Đã làm

- Đọc đầy đủ phản biện preflight261. Kiểm live: START đúng ảnh F49 đã chọn, END trống, không voice, Frames / Omni 1.1 Flash / 720p / 9:16 / 6 giây / x1 / Agent OFF, return-no-audio ON. Prompt readback khớp bản260.
- Chạy đúng một C04 giá10 trong scoped238. Số dư904 → 894. Khi tab lỗi mở output, đóng tab lỗi và mở tab project mới theo hướng dẫn owner; không sinh lại video để xử lý lỗi tải.
- Tải native và bản owner, cùng SHA `4ff4d25320105bc3dee04f28741038c0ce1dc90bb3510ca67ed57a60b6369d83`. Video720×1280,24fps,144 khung/6 giây, giải mã đầy đủ. Root kiểm đủ144 khung trên18 board, sau đó xem nguyên khung F96/F112/F124/F140/F143. Đây là kiểm từng khung, không thay cho nghe và xem liên tục AV.

## Kết luận đầu ra: NOT_SELECTED; C05 giữ lại

| Bằng chứng native, frame đánh số từ0 | Kết luận |
| --- | --- |
| Đào quay/nâng cốc trước khi Khoai lấy đũa | Cue mở đầu có thực hiện; không coi toàn cảnh thất bại mọi mặt. |
| F96 /4,000 giây: mắt Đào đã quay về phía Khoai/đĩa; F112 /4,667 giây: miếng nem mới bắt đầu nâng rõ | Sai quan hệ lén gắp → bị phát hiện. C05 chưa thể nhận endpoint này như đã đạt. |
| F124 /5,167 giây: A nằm ở phía Khoai, chưa ăn, nhưng Đào đã quan sát | Hướng gắp tương đối đúng không bù được lỗi hướng nhìn. |
| F140–143 /5,833–5,958 giây: Khoai hé rồi mở miệng | Sai yêu cầu môi khép của cảnh không thoại. |
| AAC48k stereo6,016 giây; mean−42,1dB/max−11,6dB | File có tín hiệu âm thanh dù setting ON. Chưa nghe nên không khẳng định có lời, tiếng gì hoặc giọng nào. |

Số lượng miếng A chưa được chứng nhận: hình phóng nguyên khung có thể là một lát cong; không ghi “hai miếng” thành lỗi chắc chắn khi bằng chứng chưa đủ. Chưa thấy một range cắt liên tục giữ đủ gắp A **và** Đào còn nhìn cốc. Cắt trước F96 bỏ mất gắp; cắt đuôi chỉ bỏ mở miệng, không sửa ánh nhìn. Bỏ tiếng cũng không sửa hình. Không dựng bản nối để báo đạt khi nguồn chưa đạt.

## Truy nguyên, phân biệt quan sát và giả thuyết

1. **Đã xác định:** lỗi xuất hiện trong native, trước ghép. Không phải do chọn nhầm người nói, tải hỏng hoặc đảo cảnh trong timeline. File giải mã được; live input/readback đúng, chỉ một ảnh START, không voice.
2. **Đã xác định:** prompt260 đã yêu cầu Đào giữ nhìn cốc, không bắt gặp, và hai môi khép. Do đó không thể kết luận đơn giản rằng “quên viết yêu cầu”. Output không tuân thủ các ràng buộc đó.
3. **Giả thuyết cần thử:** cùng một shot phải giữ hướng nhìn của Đào trong lúc điều khiển chuỗi lấy đũa–gắp–nâng của Khoai; START hai người nhìn nhau có thể làm mô hình quay về tương tác hai người. Chưa có bằng chứng về cơ chế nội bộ hoặc thử đối chứng, không tuyên bố đây là nguyên nhân đã chứng minh.
4. **Điểm quy trình cần khóa:** paperPASS chỉ cho phép chạy, không dự báo chắc chắn thành công. Cổng actual phải kiểm trạng thái nhìn-away từ đầu đến endpoint, không chỉ kiểm cue đầu và động tác gắp riêng lẻ. C05 không được dùng ảnh cuối một take có lỗi major.

## Chuẩn bị sửa, chưa chạy lại

DraftT02 giữ kịch bản và một shot; đưa “Đào giữ nhìn cốc đến khung cuối, chưa phát hiện” thành trạng thái xuyên suốt, đồng thời mô tả profile/hướng mắt cụ thể. Không đổi lời/giọng hoặc thêm cảnh. Đây là đề xuất kiểm chứng, **không** cam kết sửa prompt sẽ chắc chắn đạt. Cần kiểm lại thời lượng nối và phản biện trước khi chạy một retake; nếu cùng major lặp lần thứ hai phải dừng chẩn đoán theo238. Không tạo thử tay riêng, không tăng tốc để ép vừa30 giây.

Hai reviewer actual đã được giao nhưng đều lỗi giới hạn sử dụng; không nhận được báo cáo actual. Preflight độc lập đã hoàn tất không thay được actual độc lập. Root đã kiểm hình và ghi rõ giới hạn, chưa gọi review tổng thể hoàn tất.

## Ngân sách và việc còn mở

- Chi mới10; chi đã đối soát EP01 **139/500**, còn361: lượt đầu109, retake97, sau rough45, reserve110 **chưa mở**.
- Trước lượt này account có chênh−97 từ1.001 ởREC259 xuống904; chưa biết khoản đó thuộc EP01 hay sử dụng khác. Tạm giữ97 từ quỹ lượt đầu, còn12 khả dụng ở quỹ này; không hạch toán97 thành thực chi khi chưa đối soát. Nếu cả97 thuộc EP01, tổng là236/500, còn264, vẫn gồm110 reserve đóng.
- Đã hỏi owner khoản chênh97. Không dùng số dư account894 để suy thành ngân sách dự án894.
- Bước kế: đối soát khoản chênh; hoàn tất review độc lập actual và draft sửa; đóng gate T02 trước retake. **Chưa mở C05, chưa có rough cut/final.**

Native để xem lỗi: `C:/Users/PC/Downloads/du_an_nem_bui/261_C04/C04_T01_NATIVE_720p.mp4`. Evidence/boards ở cùng folder. Hồ sơ số: `restart_720p_v1/06_qc/run-registry-261.json`.
