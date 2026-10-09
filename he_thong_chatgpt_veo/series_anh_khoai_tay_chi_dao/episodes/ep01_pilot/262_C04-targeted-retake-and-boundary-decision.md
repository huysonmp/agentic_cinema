# REC262 — Kết quả sửa C04 và quyết định cách nối cảnh

## Quyết định đã xác nhận

Owner trả lời: “uh, đúng rồi đó, chạy tiếp đi” — xác nhận khoản giảm 97 credit trước C04 là chi ngoài EP01. Khoản này không tính vào thực chi dự án; đã bỏ trạng thái giữ tạm. Quyền sản xuất theo scoped238 vẫn giữ nguyên, quỹ dự phòng 110 credit chưa được mở.

## Đã thực hiện

1. Chuẩn bị prompt T02: giữ tư thế tay nghỉ ở đầu cảnh; Đào nâng cốc hơi vào trong để đọc được động tác; Khoai dùng đôi đũa riêng, gắp một miếng về phía mình. Nhấn mạnh Đào tiếp tục nhìn về cốc tới khung cuối và cả hai giữ môi khép. Không đổi thoại, giọng, món, nhân vật hoặc góc máy.
2. Nhóm DIR/DOP/ACT/EDIT và người phản biện độc lập kiểm lại T01, rồi kiểm đầu vào T02. Root đọc đầy đủ các báo cáo theo đúng hash. Báo cáo kiểm T01 hoàn tất trong REC262, không ghi hồi tố rằng REC261 đã có báo cáo này.
3. Đối soát trên Flow: START đúng khung F49 của đoạn C03B đã chọn; không có END hoặc tham chiếu giọng. Cấu hình Omni 1.1 Flash, Frames, 720p, 9:16, 6 giây, x1; Agent tắt; tùy chọn không âm thanh bật. Prompt đọc lại khớp, giá hiển thị 10 credit. Computer Use hỗ trợ kiểm đầu vào và tải bản gốc, không thay thế kiểm nội dung phim.
4. Chạy đúng một T02, số dư tài khoản từ 894 xuống 884; chi 10 credit từ quỹ làm lại. Tải bản gốc 720p thành công qua nút tải của Flow; không gặp lỗi “stopped”, không tạo lại video để xử lý tải xuống.
5. Kiểm tệp: 720×1280, 24 fps, 144 khung, 6 giây; giải mã đầy đủ. Root và hai vai trò chuyên môn đều kiểm đủ 144 khung, có xem thêm ảnh nguyên khung ở những thời điểm quan trọng. Đây là kiểm toàn bộ ảnh khung, chưa phải nghiệm thu chuyển động bằng playback hoặc nghe âm thanh liên tục.

Cloud job: `ee3e0a99-dc11-4f10-a896-ef64db4dda25`.

SHA-256 bản gốc: `8ad98f21c0c904b01055d6f579900cd60c107a152a9166a8cfa563165a47a209`.

## Kết quả: chưa chọn C04, chưa chạy C05

- Có tiến bộ: Khoai giữ môi khép. Đào đổi chú ý và nâng cốc trước khi Khoai lấy đũa. Miếng nem A rời đĩa khoảng F105–107 (4,375–4,458 giây), **trước** khi Đào nhìn lại khoảng F113–114 (4,708–4,750 giây). Không chép lỗi thời điểm của T01 sang T02: ở T01, Đào nhìn lại trước khi A được nâng.
- Chưa đúng điều kiện hiện hành: Đào đưa cốc sát môi và hé môi, gợi động tác chuẩn bị nhấp nước; chưa có bằng chứng cô đã uống hoặc nuốt. Sau đó cô nhìn lại Khoai/A trước khi kết thúc nhịp giữ miếng nem. Điều kiện “Đào tiếp tục nhìn về cốc, môi khép tới hết C04” không đạt. Lỗi nhìn lại trong C04 đã lặp qua hai lượt.
- Không có đoạn cắt liên tục nào được chứng minh là hoàn thành toàn bộ yêu cầu cũ: cắt trước khi cốc sát môi thì chưa gắp A; cắt trước khi Đào nhìn lại thì vẫn có động tác cốc/môi và chưa đủ nhịp dừng. Không dùng cắt giấu mặt, khung đứng hoặc tăng tốc để ghi nhận đạt.
- Tệp vẫn có AAC dù tùy chọn không âm thanh bật. Đo mức tín hiệu cho kết quả trung bình −42,0 dB, cực đại −4,5 dB. Chưa nghe/phân loại nội dung; không chứng nhận im lặng, lời thoại hay giọng.

Theo scoped238, dừng tạo lặp để chẩn đoán. Không tự chạy T03, không tự dùng khung cuối T02 làm đầu vào C05. Giữ nguyên hai bản gốc và bằng chứng.

## Truy nguyên: điều đã biết và điều chưa biết

Lỗi có trong bản gốc, trước khi cắt ghép. Prompt đã nêu ràng buộc; ảnh START, nội dung đọc lại và cấu hình đã được đối soát. Chưa có bằng chứng sai nguồn, tráo người nói hoặc tải xuống hỏng ở lượt này.

Giả thuyết làm việc: mô hình có thể nối động tác “nâng cốc” với “chuẩn bị uống”, và nối “người bên cạnh gắp” với “quay lại nhìn”. Đây không phải kết luận về cơ chế nội bộ của mô hình. Hai lượt cho thấy ràng buộc trạng thái kéo dài chưa được thực thi ổn định; chưa chứng minh rằng chỉ nhấn mạnh thêm câu phủ định sẽ khắc phục được.

Quyết định cần chốt lúc này là **giữ nguyên ranh giới cảnh hay thay đổi cách phân bổ nhịp bắt gặp**, không phải tiếp tục thử prompt mù.

## Hai phương án để owner quyết định

Nhãn thống nhất trong toàn bộ hồ sơ REC262: **A = điều chỉnh ranh giới cảnh; B = tách cảnh để giữ ranh giới cũ**. Cả hai chưa được duyệt.

| Phương án | Cách thực hiện và hệ quả |
| --- | --- |
| **A — Dùng nhịp bắt gặp ở cuối C04** | Cho phép Đào chuẩn bị nhấp nước, cốc sát môi và môi hé; cô nhìn lại sau khi Khoai đã gắp. C05 bắt đầu khi ánh nhìn đã trở lại, nối câu “Chờ em quay lưng nữa à?”, không quay đầu lần nữa. Khoai vẫn phải nhận ra bị bắt gặp và khựng trước khi chữa cháy. Có thể tận dụng T02, không cần tạo thêm C04; nhưng thay điều kiện cốc/môi và ranh giới C04–C05 đã duyệt. Chỉ được chọn đoạn cụ thể sau khi kiểm chuyển động và điểm nối, không tự chuyển thành đạt theo yêu cầu cũ. |
| **B — Tách C04, giữ Đào chưa nhìn lại tới hết cảnh gắp** | Cân nhắc phần đầu T02 `[0,76)`, tức F0–75, dài 3,166667 giây, cho nhịp đổi chú ý → nâng cốc → chuẩn bị lấy đũa. Từ đúng F75, tạo cảnh riêng hoàn tất lấy đũa → gắp một A → dừng; Đào vẫn nhìn về cốc và môi khép. Phần đầu chỉ là một phần C04, chưa được chọn. Giảm số bước trong yêu cầu mới, nhưng tăng điểm nối, chi phí và rủi ro liên tục tay/đũa/miếng nem. Phải kiểm đầu vào và giá mới trước khi chạy; chưa bảo đảm thành công. |

**Khuyến nghị sơ bộ: A.** T02 giữ được quan hệ “Đào phân tâm → Khoai tranh thủ gắp → Đào nhìn lại”. Nhịp chuẩn bị nhấp nước có thể là hành động đời thường hợp lý, và lời trêu ở C05 tiếp nối được mà không diễn lại cú quay đầu. Đây là đánh giá sáng tạo cần owner chốt sau khi xem, không phải tự hạ chuẩn để tiết kiệm credit. Nếu ưu tiên giữ đúng phân bổ cảnh cũ, chọn B.

## Thời lượng còn phải kiểm

Opening đang có độ dài 17,583333 giây; approval đoạn C03B ngắn không đồng nghĩa owner đã nghiệm thu toàn bộ bản nối opening. Còn 12,416667 giây cho C04–C09 nếu giữ tổng 30 giây.

- Nếu dùng đủ 6 giây T02, còn 6,416667 giây cho C05–C09.
- Với B, sau phần đầu 3,166667 giây, còn 9,25 giây cho cảnh gắp mới và C05–C09.

Chưa chốt đoạn dùng hoặc đo đủ lời/động tác của chuỗi còn lại. Không cam kết vừa 30 giây bằng phép cộng trên giấy; không tăng tốc, nuốt lời hoặc che mặt người nói để ép thời lượng.

## Sổ chi, lưu trữ và bước tiếp theo

EP01 đã dùng **149/500 credit**, còn **351**: lượt đầu 109, làm lại 87, sau bản dựng thô 45, dự phòng 110 chưa mở. Số dư tài khoản 884 không phải quyền chi 884 credit cho EP01. Không mua hoặc nạp thêm.

Bản gốc cho owner: `C:/Users/PC/Downloads/du_an_nem_bui/262_C04/C04_T02_NATIVE_720p.mp4`. Ảnh kiểm khung, chứng cứ kỹ thuật và ảnh chụp thao tác nằm trong thư mục `262_C04`. Request, registry, quyết định và bài học lưu trong `restart_720p_v1`; hồ sơ REC261 giữ nguyên lịch sử.

**Bước tiếp:** owner chọn A/B → cập nhật đúng quyết định dàn cảnh → kiểm đoạn dùng, trạng thái nối và thời lượng → mới mở sản xuất cảnh phụ thuộc. Chưa có bản dựng thô hoặc bản cuối.
