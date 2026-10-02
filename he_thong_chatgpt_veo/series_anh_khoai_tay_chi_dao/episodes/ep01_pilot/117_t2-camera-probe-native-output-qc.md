# T2-CAM-02 — Native output QC, root bounded R1

2026-10-02. Input approval/execution116, exact request115. Không là independent CINE verdict.

## Đã xác định

- Flow single-start nhận OPEN7 và tạo được một clip Lite; không generalize mọi ảnh/route.
- Native 720×1280, 8s,24fps; full decode không lỗi. Có AAC stream, chưa nghe/ASR nên audio content UNKNOWN.
- Root xem mẫu0/2/4/6/7.5s. Cả hai mặt vẫn nằm trong các mẫu; ánh sáng ấm và món/rau/hai đồ chấm/hai bát/đũa vẫn hiện, nhưng không giữ trọn presentation ở cuối.
- 2s Khoai nhấc tay; 7.5s lại giơ tay, miệng mở. Confirmed gesture drift, không kết luận thoại từ miệng mở.
- Từ0→7.5s thêm background phía trên, vật bàn lớn hơn và mép phải mất một phần ly/đồ chấm; mép trái cắt lá/đĩa rau. Chuyển khung chưa thỏa no-push-in/full-serving. Không đủ bằng chứng để phân rã chính xác tilt vs zoom vs rerender; smoothness/cut/shake toàn clip UNKNOWN.
- Veo native mark hiện trong các mẫu, không xóa/đè/crop output.

## Quyết định / giả định / vấn đề mở

ROOT_BOUNDED_QC_REWORK; không production master hoặc quality-pass. Giữ directionT2, script32, references45/78 và voice93. OPEN7 chỉ diagnostic input, không ngầm khóa identity/recipe accuracy. Chưa nghe audio hoặc independent motion review; chưa xác nhận trọn vẹn source fidelity trên mọi frame. Không chạy retry trong gói một-lượt115; không dùng reserveV02.

## Đề xuất vòng kế tiếp, chưa submit

Tách kiểm soát: control camera tĩnh cùng input để phân biệt drift mặc định của model với lỗi camera; sau đó camera test biên độ nhỏ, nhấn giữ nguyên framing scale và margin. Mỗi lượt vẫn Lite/x1, read-back giá và cộng tổng trước submit, chỉ chạy trong scope được owner chấp thuận. Không nâng Quality để chữa lỗi gesture/composition khi chưa xác định nguyên nhân. Thử nghiệm này là camera-only, không thay hành động chữa cháy/gắp cho Đào của tập chính.

## Evidence / bàn giao

File/hash116; samples project `media/raw/ep01_t2_camera/sample_0.png`, `sample_2.png`, `sample_4.png`, `sample_6.png`, `sample_7.5.png`. Media/screenshot local gitignored; chỉ docs version-control. Owner có native file để xem đầy đủ; cần feedback về chuyển máy, không yêu cầu owner chuẩn bị reference thay agent.
