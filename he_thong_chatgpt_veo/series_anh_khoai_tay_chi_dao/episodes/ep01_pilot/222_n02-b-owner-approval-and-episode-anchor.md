# 222 — Chốt N02 B và chuẩn hình nối cảnh của EP01

Ngày 2026-10-07. `N02_B_OWNER_ACCEPTED_SCOPED / EPISODE_ANCHOR_DECISION_PENDING / NOT_RELEASE`.

Cập nhật tiếp nối: owner trả lời **“a”**, duyệt phương án A cho chuẩn hình riêng EP01. [Hồ sơ quyết định223](evidence/223/anchor-decision.json) khóa đúng nguồn B và phạm vi; các phương án/câu hỏi dưới đây giữ làm lịch sử lúc trình. Chưa có quyền tạo media hoặc chi mới.

## 1. Approval đã nhận, không hỏi lại N02

Owner trả lời nguyên văn **“ok rồi nhé”** sau khi root trình đúng `N02_B_NATIVE.mp4`, báo B có biến đổi căn thời gian cục bộ và hỏi: đúng giọng K20, nguyên văn lời, khẩu hình chấp nhận được, cách trở về khung hai người ở giây 7 có ổn không; approval chỉ cho N02, không toàn phim.

Ghi nhận chọn B cho N02 trong các tiêu chí trên. Target đã rehash trong lượt222:

- Local: `C:/Users/PC/Downloads/du_an_nem_bui/221_n02_pa_v_trial/N02_B_NATIVE.mp4`.
- SHA256: `660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535`.
- Flow asset: `65777488-e2fd-464d-9433-763cd6560e8e`.
- Phạm vi được duyệt: nguyên bản tải từ Flow, 10 giây/240 khung hình; không phải bản đã cắt hoặc phối tiếng mới.

Đây là **nghiệm thu của owner**, không phải root/agent đã nghe. Không tự sửa báo cáo reviewer 221 thành đã nghe/xem đạt. Approval không chứng minh dữ liệu âm thanh PCM hoặc thời điểm lời giống tuyệt đối nguồn 200; giữ số đo SIA và ghi nhận chấp nhận đúng bản B sau thông báo. Không chồng tiếng nguồn 200 lên B hoặc chỉnh tốc độ/thời gian của B.

### Disposition theo findings

| Vấn đề | Xử lý tại222 |
|---|---|
| B voice/lời/nhịp/khẩu hình cần human checkpoint | Owner chấp nhận đúng B theo câu hỏi đã trình; không dùng approval201 của source cũ để thay |
| B trở về khung hai người tại giây 7 | Owner chấp nhận cách quay của đúng bản N02 này; không áp mặc định cho các lượt khác |
| B local audio timing difference | Số đo vẫn có thật; acceptance output variation, không ghi “đã khôi phục PCM/timing gốc” |
| A mất mặt/insert lệch; C caption/blend | Không chọn A/C. Không ghi defects của chúng được sửa hoặc xoá media/evidence |
| Gaze, diễn liên tục, source-state toàn tập và các joins | Không tự đóng bằng approval giọng/khẩu hình/cutN02; tiếp tục kiểm ở bộ cảnh và rough cut |
| OPEN7/B so với TABLE08 | Chưa nâng thành chuẩn toàn tập; câu hỏi ở mục3 để tránh trộn hai baseline |

Không có quyền tạo video/Quality/thử lại mới. Lượt 222 không chi credit, không điều khiển trình duyệt, không sửa native hoặc thay WAV 202. Số dư 77 là lần kiểm UI tại 221 ngày 6/10, không xác nhận số dư hiện tại ngày 7/10. Gói chi 30 credit đã hoàn tất.

## 2. Vì sao phải chốt một chuẩn nối cảnh trước phần còn lại?

Root đọc lại 214/215/219/221 và xem trực tiếp khung hình số 0 của B cùng TABLE08. Cả hai có Khoai trái, Đào phải, rau trước-trái, hai đĩa chấm, hai bát cá nhân, hai đôi đũa nghỉ và cốc ngoài phải Đào. Tuy nhiên B khung gần hơn, ụ món rộng/sáng hơn, mặt và nền quán là hình phái sinh khác TABLE08. Đây là khác biệt quan sát, không tuyên bố sai công thức hoặc quyền sử dụng món.

Nếu dùng B cho N02 nhưng mặc định lấy TABLE08 hay các take cũ làm chuẩn ở cảnh kế, có thể lặp jump về mặt, món, bộ bàn hoặc nền. Cần chốt **variation cho riêng EP01**, không thay canon nhân vật của series hoặc nguồn fact. PAIR03 vẫn đối chiếu identity; TABLE08 vẫn giữ ràng buộc phục vụ trừ thay đổi nào được ghi rõ.

### Hình đang được dùng trong B

Ảnh dưới là khung hình số 0 của B đã chọn, không phải ảnh tạo mới hay tư thế mở tập được duyệt. Chỉ minh họa phong cách/bàn/nền; không mặc định dùng khuôn miệng đang mở làm ảnh đầu của Đào nói.

![B — ứng viên chuẩn nối cảnh EP01](C:/Users/PC/Downloads/du_an_nem_bui/221_n02_pa_v_trial/inspection/N02_B_NATIVE/all_frames/frame-0000.jpg)

Frame SHA256: `b483a087a50b878051a201da0ac23ced2eebcd80b7b8e214387f5bc67f04f225`.

### TABLE08 — chuẩn bàn đã duyệt trước đó

![TABLE08 — chuẩn bàn trước đó](D:/Workspace/agentic_cinema/he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/media/raw/ep01_p6_food/T-NB-03_v0.8.jpg)

TABLE08 SHA256 đã rehash: `aeb6dfaee1773109243f9f952235a44f2417c6fb7fb4faf15be61c34ca40d924`.

## 3. Một quyết định nền tảng tiếp theo

**A — Đề xuất:** giữ N02 B đã duyệt, lấy hình của B làm chuẩn variation về mặt/ánh sáng/nền và hình thái ụ món cho **EP01**. Giữ bộ phục vụ TABLE08, món nguội/không khói, quan hệ bạn bè, outfit/identity đã khóa. Chọn frame/pose riêng đúng nhiệm vụ mỗi cảnh; không ép tất cả góc máy giống một ảnh. Hệ quả: các take cũ phải match baseline B theo thuộc tính hoặc sửa; không tự tái dùng vì đã tốn credit. Approval này chỉ khóa hướng hình, không cấp lượt sinh hay chứng nhận món/acting/continuity toàn phim.

**B:** giữ TABLE08 là chuẩn hình chặt cho EP01. B vẫn là phép chứng minh N02 được chấp nhận, nhưng cần kiểm/sửa variation hình của N02 và phần còn lại để về TABLE08 trước production lock. Hệ quả: có thể phải thay take đã chọn và nghiệm thu lại phần hình–tiếng bị ảnh hưởng; chưa có quote hoặc bảo đảm công cụ giữ được tiếng khi sửa lần nữa.

Khuyến nghị A vì hai người và bữa ăn của N02 đã được owner chấp nhận; thống nhất theo một baseline rõ giảm xung đột nối cảnh. Không khuyến nghị vì tự động/nhanh, không coi B đẹp hơn TABLE08 là kết luận khán giả hoặc fact.

**Owner cần trả lời:** A hoặc B. Không cần trả lời lại tên/giọng/lời/động cơ đã chốt. Không có quyền chi phát sinh từ lựa chọn này.

## 4. Bước thực thi sau quyết định này

1. Root lập gói G1 storyboard ảnh R01–R09 với nguồn/hash/tư thế, ai nói–ai nghe, F0–F4 và A/B, đánh dấu phần thiếu; cảnh nói phải có mặt, hành động phải có nguyên nhân. Ảnh ứng viên không tự là footage đạt.
2. Ưu tiên đối soát R01 → N02 B → R03 (N03/N04), gồm kéo–“Khoan”–dừng và hỏi–đáp. Không áp thời gian của WAV 202 cũ vào B mới; nếu đề xuất thay tiếng N02 trong bản nối, phải đo theo đúng B.
3. Dùng gói hình và đoạn nguồn khả thi để trình bản dựng thử; kiểm độc lập theo các vai tại 217, owner duyệt tại G1. Không vượt phần thiếu bằng nhiều cảnh bát nem hoặc giữ cảnh không mặt.
4. Sau đó mới trình phép thử có tuyến công cụ/giá/số đầu ra/trần chi/tiêu chí riêng cho đoạn còn thiếu; không tự dùng 77 credit lịch sử. Chuỗi cốc→gắp A→bị thấy→đổi hướng→bát→gắp B vẫn phải chứng minh ở G3, rồi G4/G5.

Đang ở P7 recovery: N02 B đã được chọn trong scope human checkpoint, G1 toàn tập chưa hoàn tất; không phải P11 finishing hoặc P13 bàn giao.

## 5. Tổng hợp vòng

- **Đã xác định:** exactB/hash không đổi; approval của owner đã gắn đúng target và phạm vi. Hình B/TABLE08 có variation cần thống nhất khi nối toàn tập.
- **Quyết định đã chốt:** B cho N02; K20/lời/khẩu hình và return7s được chấp nhận ở đúng B. Giữ C-v0.6, K20/D06, storyboard214, bạn bè và đườngA→bát→B.
- **Giả định đang dùng:** acceptance “ok rồi nhé” trả lời đúng đề nghị cuối về N02; không là cấp thêm credit hoặc blanket film approval.
- **Còn mở:** A/B chuẩn hình EP01, nguồn/range các cảnh còn lại, gaze/acting/continuity tại joins, nhịp30s và full-film review.
- **Tiếp:** owner chọn chuẩn hình → root chuẩn bị bộ G1 thật, không yêu cầu owner tự dựng khung.
