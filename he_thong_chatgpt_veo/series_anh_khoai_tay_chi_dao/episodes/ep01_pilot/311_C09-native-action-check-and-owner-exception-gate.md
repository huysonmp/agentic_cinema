# REC311 — C09 đã tạo; đúng miếng B nhưng sai vai trò tay Đào

Ngày 14/10/2026. Chạy đúng một lượt C09 đầu theo238 sau preflight310; không tự chạy lại, không mở dự phòng hoặc chi từ tạo lại.

## Kết quả và ngân sách thực

- Native asset `316cd8b4-2826-408f-8caa-6fa1be5766a1`, tải qua trình duyệt tích hợp đúng720p kích thước gốc. File853.335byte,720×1280,24fps,96khung/4s; toàn tệp giải mã sạch.
- SHA native `d06160b0efbb2ee5e7188d4748ffe3ae915abb0036b31ec12ae52788affd72e3`; bản tải, repository và bản owner khớp. Native giữ nguyên.
- Số dư tài khoản1.008→1.001, chi thực7. Dự án đã chi279/500, còn221: tạo mới66 / tạo lại0 / hậu kỳ45 / dự phòng110 vẫn đóng.

## Root đã kiểm gì

Đã xem đủ sáu bảng dày bao phủ96khung và ảnh nguyên khung F0/20/28/31/40/54/56/58/64/72/80/84/95. Đầu cảnh đũa trống, A còn trong bát riêng Đào. Khoai hạ đũa tới đĩa chung, lấy B mới rồi nâng về phía mình; B không lấy lại từ bát Đào, không trao lại, không ăn. Cuối có ánh nhìn và nét cười hiểu nhau; hai nhân vật và mặt vẫn hiện rõ, không thấy bát thứ ba hoặc khói. Đây là kiểm ảnh khung, chưa chứng nhận chuyển động liên tục hoặc tiếp xúc khuất.

Lỗi thực: Đào hạ bát/cốc trong phần đầu. F31 còn thấy tay ngoài giữ cốc; F40 trở đi cốc đứng trên bàn phía sau bát và tay ngoài chuyển sang đỡ bát. Như vậy không chỉ giảm độ cao mà đã **đổi vai trò tay**, trái FINAL yêu cầu giữ cốc và giữ bát bằng tay trong. A vẫn trong bát, không thấy cốc đặt vào bát. Lỗi nằm trước khi B được nhấc (~F57–65), nên cắt đuôi không sửa được hợp đồng cảnh; lấy riêng đoạn cuối sẽ giấu chuyển động hoặc làm sai điểm nối từ C08.

Kiểm độc lập actual đã giao, report riêng đang hoàn tất tại thời điểm viết; không ghi reviewer đã xong chỉ từ thông báo sơ bộ. Root không tự miễn trừ yêu cầu đã chốt.

Cập nhật: reviewer đã lưu `C09_PICK_B_actual_independent_311.md`; root đọc toàn report. Reviewer tự hash/probe/full decode, xem đủ96khung và dày các ảnh nguyên khung quanh hạ cốc, đổi tay, pickup B, kết. Kết luận khớp root: core A/B có giá trị, hand-role sai brief trước pickup nên không chữa bằng trim đuôi. Không nghe hoặc chứng nhận chuyển động liên tục.

## Bản để xem, không phải sản xuất được chọn

Native vẫn có AAC4,01s dù no-audio toggle bật; PCM khác0, maxabs0,38949585/RMS0,03263018. Chưa nghe nên không kết luận nội dung/giọng. Đã tạo bản riêng không thoại `C09_PICK_B_FULL_SILENT_REVIEW_ONLY_311.mp4` bằng copy video bitstream, bỏ riêng track âm phát sinh của C09. SHA `68589b58fcc342fc1d72c111828c9bf430d4713a2ba9ee78ed60f57bc09f5958`; đủ96khung/4s, video-only, giải mã sạch. So sánh framemd5 toàn96khung với native bằng nhau. Không sửa K20/D06 đã duyệt, không re-encode hình hoặc xóa nguồn.

Owner folder: `C:/Users/PC/Downloads/du_an_nem_bui/311_C09_PICK_B_T01/` giữ native và bản xem im tiếng. Bản xem không có nhãn fullfilm/finalPASS.

## Cổng quyết định và bước tiếp

Đề xuất sáng tạo: cho phép Đào đặt cốc xuống bàn rồi đỡ bát bằng cả hai tay trong cảnh kết, vì đường A/B và nét hiểu nhau vẫn đúng; dùng nguồn này để dựng thử, không đồng nghĩa owner duyệt clip hoàn chỉnh hoặc toàn phim. Đây là thay đổi brief cần owner chốt, agent không tự waive. Nếu owner giữ yêu cầu tay cũ thì nguồn C09 hiện tại không được chọn; chưa có quyền retry vì tạo lại0 và dự phòng chưa mở. Phải trình phương án/ngân sách mới trước chạy.

Timing chưa đóng. Dùng đủ4s C09 sẽ đưa chuỗi hiện hành tới912khung/38s, vượt rough35. EDIT đang khảo sát candidate cắt phần đệm có bằng chứng; không bỏ B, cắt lời hoặc tăng tốc để ép số. Final30, food seam C05→C06, nghe–nhìn toàn phim và cổng rough/final vẫn mở. EDL toàn tập chưa thay.

Cập nhật cổng REC312: owner chọn A, cho phép Đào đặt cốc rồi đỡ bát hai tay **để dựng thử**. Không biến take thành đúng FINAL cũ, không duyệt range/clip hoàn chỉnh/toàn phim. EDIT đã khảo sát candidate C02 [16,173), C04 [12,124), C09 [8,88): số học840khung/35s nhưng chỉ còn8khung nhìn nhau rõ ở cuối, cần kiểm cảm giác kết trên bản thật. Root đọc toàn follow-up timing311. Bước tiếp là một bản rough nháp có EDL/hash và kiểm các seam mới, không chạy Flow hoặc sửa giọng.

Đã xác định: native tải/giải mã/credit đúng; B mới có diễn biến đầy đủ; tay/cốc Đào sai brief. Đã chốt: không retry hoặc chọn production tự động. Giả định làm việc: bản silent chỉ phục vụ xét hình của cảnh không thoại. Vấn đề mở: ngoại lệ động tác, timing, điểm nối và bản dựng toàn tập. Bước tiếp: hoàn tất báo cáo độc lập, owner chốt ngoại lệ rồi dựng một rough có EDL/range rõ để kiểm và duyệt tổng thể.
