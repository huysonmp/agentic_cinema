# REC305 — C07 hai ảnh: đã chạy, đã tải; chưa chọn vào phim

Ngày 14/10/2026. Owner duyệt chuyển đúng 2 credit từ tạo mới sang tạo lại và một lượt C07 tối đa 7, không tự chạy lại. Quyền này đã sử dụng đúng một lần.

## Quyết định và thực chi

Gói giữ F47 + portrait v1 + một saved Đào/D06, không đổi prompt FINAL304. Kiểm cuối tại UI: Ingredients / Omni 1.1 Flash / 720p / 9:16 / 4 giây / x1, quote 7, Agent OFF, âm thanh ON. Hai ID ảnh khớp manifest; prompt exact read-back. Voice name đã kiểm ở preparation; opaque UUID không được UI lộ, không tuyên bố xác minh UUID live.

Một click tạo, asset `87a190b8-07a4-4285-b7c7-8f9f1479def3`. Account balance 1.022 → 1.015: debit đúng 7. Sổ dự án 265/500, còn235; tạo mới80 / tạo lại0 / hậu kỳ45 / dự phòng110 **đóng**. Không retry hoặc mở dự phòng.

## Bản gốc và evidence

Native `05_native/EP01_720_C07_RECEIVE_TWOREF_T01_NATIVE_305.mp4`, SHA-256 `12a0baa2d7ccedfaa16631b7cddd2c4331480e4fa8784880403eb425a8fb397b`, 1.806.037 byte. Tải qua UI 720p kích thước gốc, không upscale. Bản download, repo và owner copy có cùng hash. H.264720×1280 / 24fps /96F/4s, AAC48kHz stereo4,032s; giải mã toàn tệp thành công.

Root xem đủ sáu bảng16F bao phủ F0–95, không padding, và full PNG critical F0/F10/F24/F48/F58/F60/F62/F64/F67/F69/F72/F74/F76/F78/F80/F95 cùng F47 tham chiếu. Đây là ảnh toàn khung, **không phải đã xem vận động AV liên tục**. Reviewer độc lập kiểm hash, đủ sáu bảng và full khung critical riêng; report đã được root đọc đầy đủ. Report reviewer đọc run snapshot sớm còn pending; terminal receipt nay cập nhật trong run305, không sửa lịch sử review.

## Kết quả thực tế

| Hạng mục | Kết quả | Cổng |
| --- | --- | --- |
| Nhận diện và entry | Đào còn toàn đầu quả đào; Khoai còn củ khoai. F0 gần F47 về mặt/pose/props, không hóa người/reset lớn như302. | Cải thiện trên hình, chưa chốt seam AV hoặc exact pixel. |
| Bát và cốc | Đào nâng chính bát mình bằng tay trong; tay ngoài giữ cốc trên cao. Bát nâng trước rồi tới dưới A. | Không thấy lặp chọn nhầm bát/tay302; clearance phía sau bị che, chưa physics PASS. |
| Khoai nghe | F5–14 có chuỗi mở rồi khép miệng, nhìn như phát âm. | **MAJOR khẩu hình người nói**; chưa nghe nên không kết luận có tiếng Khoai hay sai preset. |
| Đuôi bát | Reviewer fullF76 sạch, F77 bắt đầu oval mờ, F84–95 rõ bát thứ ba trên bàn trong khi Đào vẫn cầm bát. | **MAJOR prop duplication**, không chọn toàn4s. |
| Nem A và bàn | Nem vẫn kẹp; không thấy thả/ăn/cho miệng/gắp lại. Đũa nghỉ, rau, hai đồ chấm còn, không khói. | Không lấy partial pass cứu hai blocker trên. |
| Tiếng | ASR offline không prompt nhận nguyên N07, segment0–2,12s. | Không chứng nhận D06/giọng Bắc/speaker/âm cuối/lip-sync. Owner nghe exact bản3s đang chờ. |

## Bản xem không tốn credit

`C:/Users/PC/Downloads/du_an_nem_bui/305_C07_RECEIVE_TWOREF_T01/C07_TWOREF_0_3s_REVIEW_ONLY_305.mp4`: range **[0,72)**, 72F /3s, tiếng giữ cùng0–3s. SHA `7a7d2bc4d4fdd7a4ec220daa67477e3063583d1b2f9366a089318b9ab1104e18`; probe/decode đúng3s cả hình/tiếng. Bỏ đuôi bát xuất hiện, **không sửa/che lỗi miệng đầu**; không gọi range đạt. Owner được hỏi riêng tiếng, không miễn lỗi hình/range/toàn phim.

Reviewer nêu F15–76 có thể khảo sát, nhưng cắt tớiF15/0,625s có thể mất đầu “Thế”; không tự trim đầu hoặc dời tiếng để tạo false PASS. Hiện chưa có range chứng minh đồng thời trọn câu, attribution, clearance và seam. Không tự dùng F71/F76/F95 làm input C08.

## Truy nguyên và giới hạn

Đã xác minh hai ảnh, prompt và config đúng khi submit; không có bằng chứng chọn nhầm file/voice. Identity đã giữ nhưng object permanence và silent-mouth instruction vẫn không đạt: gói tham chiếu/ngôn ngữ không đảm bảo ràng buộc toàn chuyển động. Hai ảnh và wording cùng thay nên không chứng minh portrait một mình sửa identity; cũng không chứng minh giọng gây hóa người. Bát tái xuất là lỗi đầu ra quan sát được, chưa khẳng định nguyên nhân nội bộ model.

Cổng kiểm actual đã bắt lỗi trước EDL/C08. Bước tiếp: nhận kiểm tiếng exact từ owner, rồi quyết định xử lý khẩu hình/range dựa trên bằng chứng; không đề nghị owner phê duyệt toàn hình bị lỗi để tiếp tục. Mọi sửa hình hoặc paid request mới cần phạm vi/nguồn/ngân sách cụ thể; không tự retry. Food seam C05→C06 và final30/rough35 vẫn mở. Nếu dùng3s thì tới cuốiC07 là752F/31,333s trong rough; final30 chưa đạt và rough35 còn88F/3,667s cho phần còn lại, **chỉ tính giả định, EDL không đổi**.
