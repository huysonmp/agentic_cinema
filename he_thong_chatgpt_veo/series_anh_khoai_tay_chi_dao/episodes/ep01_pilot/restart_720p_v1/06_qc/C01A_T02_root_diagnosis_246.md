# REC246 — C01A T02: truy nguồn và phương án sửa

Trạng thái: ROOT_DIAGNOSIS_INTEGRATED / T02_REWORK / T03_PREFLIGHT_PENDING. Root là maker tích hợp, không reviewer độc lập. Native T02 SHA256 `0b5615beef4e23a42428771109fe36544510270281ae35129de6f6c585a398a7`; các phát hiện không áp sang C02 đã duyệt.

## Bằng chứng và phạm vi

Root xem nguồn F0, toàn ba board6fps/36 mẫu và overview, full native indices0/56/88/143. Source hash `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`. Native720×1280/24fps/144 khung/6s; audio6,016s; giải mã toàn file thành công. Trích khung không đồng nghĩa đã xem AV liên tục. Root không tự nghe hoặc xác nhận lip-sync.

Owner đã nghe PCM trích từ T02, hash `1082833d4066616f50b410ffa3c820373063acf12c18ebe1ea3dc91fde699863`, trả lời “Đúng D06, lời và nhịp chấp nhận được”. Đóng checkpoint nghe output Đào đầu tiên, không duyệt hình/khẩu hình hoặc chuyển waveform approval sang T03. ASR offline chỉ đối chứng N01; mốc “em”2,98–3,22s là ước lượng, không chứng nhận cut.

## Tầng phát sinh đã đối soát

| Điểm | Quan sát | Kết luận / chưa biết |
| --- | --- | --- |
| Nguồn F0 | Bàn không có lettering; chỉ biểu tượng bốn cánh sáng ở góc dưới-phải | Không phải chữ đã có trong ảnh đầu vào |
| Prompt T02 | Cấm chữ mới nhưng vẫn có câu chung “Preserve source watermark”; gọi customvoice bằng filename | Câu watermark thiếu mô tả phạm vi. Có thể góp phần, chưa chứng minh causal; cùng câu từng có trong T01 mà không phát hiện chữ này |
| Native T02 | Dòng “Khoai.ayKhanh.om” có tại full0/56/88/143 và các mẫu board | Chữ phát sinh ở take đã tải, trước dựng. Không phải lỗi phụ đề/EDL do root ghép; không có clean range trong các mẫu. Không tự gọi là watermark gốc hoặc xóa/che để PASS |
| Chọn tay | Truy cẳng tay về vai ngoài SCREEN-RIGHT ở ảnh lớn | Nghi ngờ nhầm tay ban đầu đã rút lại; không đưa lỗi chưa đúng vào RCA |
| Dáng tay | ACT và DOP thấy palm-up/xòe; đọc giống giới thiệu món | Judgment diễn có bằng chứng mẫu. Pose orientation chưa mô tả dương đủ rõ, đích HIGH ABOVE/gap cứng có thể làm nghĩa lấy yếu; không causal proof |
| Tiếp xúc/thu | Khoảng hở rõ hơn T01, còn giữ tay ở mẫu cuối | Chưa tự đóng whole-path/candidate; phải đọc critic hiện hành |
| Khoai nghe | Môi hé ở đầu/tail của mẫu, sau lời Đào | Môi mở không tự chứng minh nói giọng nam. Không dùng ASR để đóng speaker/lip-sync |

Root đọc đầy đủ ACT diagnosis và DOP diagnosis. ACT không thay critic; DOP trực tiếp xem hai ảnh, không whole-path. Không xếp hạng thành công hoặc dự báo phần trăm từ một output.

Root đã đọc đầy đủ native critic T02:52 unique frames, REWORK_VISUAL_INTENT_AND_ADDED_TEXT/HOLD_C01B. Hai MAJOR T01 rim-occlusion/early-retract không quan sát lặp; hand-width literal T02 chưa đạt rõ, không dùng partial đó gọi tất cả clearance đã PASS. Lỗi chữ và palm-up là mới; không có bằng chứng nguyên nhân chung được chứng minh để phân loại same-MAJOR. Vì vậy ngưỡng mandatory STOP238 chưa kích trong scope đã xem. Root vẫn dừng paidrun để chẩn đoán và tích hợp ACT/DOP/critic; không miễn stop-rule hoặc chạy hàng loạt. Một retake giữ nguyên canon/route chỉ có thể tiếp sau independent preflight và kiểm live trong quyền238. Nếu phát hiện blocker lặp nguyên dạng, dừng lại và trình.

## Sửa tầng nguồn lỗi, không sửa bằng che cảnh

Giữ source, camera, cảnh, diễn tiến trước-contact, lời, speaker và đúng D06. DOP xác nhận có thể đề xuất cùng khung trên giấy: ngón đi tới khoảng gỗ bên trái–trước bát Đào, hướng mép trên-phải đĩa, vẫn thấy gỗ ngăn ngón và rim. Mu tay lên/lòng xuống, ngón hơi cong; bỏ HIGH ABOVE và khoảng cách cứng một bề rộng bàn tay. Không ép cả bàn tay nằm trong một vùng gỗ rộng vốn không có.

Đặc tả biểu tượng chỉ giữ biểu tượng bốn cánh hiện có, bàn không lettering; không đưa chữ hallucination vào prompt để model sao chép. Bỏ production filename khỏi creative prose nhưng vẫn bắt buộc bind exactD06 UUID và kiểm chip/readback. Không đổi tên giọng hoặc mẫu giọng. Đây là change set có liên quan, không thí nghiệm một biến.

Prompt T03 có nhãn DRAFT, submit_count0, quote chưa kiểm; không được dùng nhãn draft làm quyền gửi. Trước paidrun: đọc critic actual và giải quyết stop-rule → độc lập preflight T03 → exact binding/readback/livequote≤15/budget → một output → hồi quy toàn clip. Nếu cần đổi canon/camera/công cụ/voice hoặc sử dụng reserve, phải trình owner.

## Trạng thái và bước tiếp

- Đã xác định: C02 exact export đã duyệt; tiếng T02 D06/lời/nhịp được owner chấp nhận. T02 picture còn lỗi chữ/ý định, không nguồn C01B.
- Đã chốt: chưa ghép C01A này vào phim, không crop/food cutaway/đổi phụ đề để che lỗi.
- Giả định: pose palm-down và vùng gỗ thấp có thể giữ nghĩa lấy trước-contact; phải kiểm output.
- Còn mở: critic actual, stop-rule, endpoint/range/lip-sync và điểm nối C01B.
- Bước tiếp: tích hợp critic, chốt nhánh xử lý có bằng chứng; chưa trả thêm credit từ tài liệu này.

Sổ bảo thủ50/500 đã dùng, còn450; firstpass140, retake155, postrough45, reserve110 chưa được giải ngân. C01A T01 và T02 cùng tab quote10/debit10 mỗi lượt, không suy chênh số dư tab cũ thành hoàn tiền.
