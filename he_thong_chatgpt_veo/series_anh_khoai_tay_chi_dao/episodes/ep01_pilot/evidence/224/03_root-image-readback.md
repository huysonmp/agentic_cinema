# REC224-ROOT — Đọc lại ảnh native

Scope: đã xem trực tiếp B frame175 và đủ bốn ảnh JPG native bằng công cụ xem ảnh. Chỉ kiểm ảnh tĩnh; không nghe, không xem video liên tục, không chứng minh chuyển động hoặc khẩu hình.

## Những gì đã kiểm được

- Dùng đúng một nguồn B cho cả bốn lượt. Manifest xác minh prompt nguyên văn có trong preflight và nhật ký output đúng UUID; không có bằng chứng trộn nguồn, chuyển sang video hoặc gửi nhầm prompt.
- Đủ Khoai bên trái, Đào bên phải, trang phục và dây eo hồng, cảnh quán nhỏ ven phố, ánh sáng ấm, bát riêng rỗng, rau phía trước-trái, hai bát chấm, đũa đặt trên bàn và cốc bên phải Đào. Không thấy khói/hơi nóng hoặc miếng nem đã vào bát riêng.
- Ảnh được tăng chi tiết từ nguồn 360 × 640; hình dạng mặt/món có sai khác nhỏ khi tái sinh. Không coi tái dựng chi tiết là bảo toàn pixel của B, không quay lại áp hình món TABLE08 cũ để bác biến thể B đã duyệt.

## Đọc từng ảnh

| ID | Quan sát trực tiếp | Ranh giới sử dụng hiện tại |
|---|---|---|
| REF01-S | Hai miệng khép, tay nghỉ; Đào nhìn Khoai, Khoai nhìn xuống bữa ăn. Lông mày và môi Khoai khiến sắc thái khá băn khoăn, chưa hẳn dịu và hồi tưởng. | Ứng viên mở đầu; cần review diễn/owner, không tự duyệt vì đúng đồ vật. |
| REF01-M | Đào vươn một tay, tay còn lại nghỉ; đĩa vẫn gần vị trí nguồn. Điểm ngón tay tiến vào phía sau-trái của đĩa, sát phần món phía trên; chưa đọc rõ ý định nắm vành phía gần-phải để kéo đĩa. | HOLD tư thế hành động. Không kết luận chắc chắn chạm đồ ăn khi vị trí bị che; nhưng chưa chứng minh được đích vươn tay đúng brief. |
| REF01-E | Hai tay đã nghỉ; miệng Khoai hở rõ và miệng Đào cũng hở. | REWORK ảnh exit miệng khép. Không dùng làm reference neutral đã đạt. |
| REF03-S | Khoai cười kín; miệng Đào còn hở, khác trạng thái reference miệng khép được yêu cầu. | REWORK trạng thái Đào. Không gọi đây là lỗi lip-sync: chưa tạo video. |

## Truy tầng phát sinh

Đầu vào/hash → prompt/preflight → output native đã được đối soát. E và REF03-S không giữ miệng khép dù prompt ghi rõ, nên lỗi quan sát nằm ở output tạo ảnh; chưa có cơ sở nói do tải nhầm, nhầm người nói, thiếu thông tin thoại hoặc lỗi dựng. M có yêu cầu vành gần-phải nhưng output không làm rõ điểm tiếp cận; vẫn cần review độc lập về cách đọc tư thế. Nguyên nhân nội tại của model chưa biết.

Các cụm mô tả ý định hội thoại có thể kéo model về miệng đang nói là **giả thuyết để thiết kế phép thử**, không phải nguyên nhân đã được chứng minh. Nếu sửa: chỉ thay cue hình học của miệng/tay và vùng được phép sửa; giữ B, bàn ăn, camera, trang phục. Không giải quyết bằng che mặt hay chuyển sang cảnh món ăn.

## Không vượt quyền

Đã dùng đủ bốn lượt ảnh được duyệt, số dư 77 → 77. Không retry, không sinh video, không chuyển Quality hoặc ghép thành phim. Root đã đọc lại đầy đủ hai báo cáo độc lập: EDIT và CONT cùng giữ S làm ứng viên, cùng xác nhận lỗi miệng E/REF03-S. EDIT HOLD M vì đích ngón tay chưa rõ; CONT REWORK/HOLD vì không đúng vành gần-phải. Root giữ blocker M và đề nghị sửa đúng vùng, không coi khác biệt nhãn là PASS. Bản này không thay hai báo cáo. G1 toàn tập vẫn mở.
