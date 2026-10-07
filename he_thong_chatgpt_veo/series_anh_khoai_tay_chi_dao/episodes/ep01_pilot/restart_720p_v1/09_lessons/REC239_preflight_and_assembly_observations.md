# REC239 — Đối soát đầu vào và khả năng dựng trước sản xuất

Ngày 07/10/2026. Phạm vi: preparation trên project mới; chưa gửi request video.

## Quan sát và mức xác nhận

- Owner đã nghe và chấp nhận hai preview phục hồi bằng câu “giọng ok rồi nhé”. Ghi riêng tại `00_decisions/voice-approval-239.json`; không suy thành nghiệm thu thoại/khẩu hình C02.
- Browser binding cũ không còn khả dụng. Đã kiểm inventory và nối lại đúng in-app browser hiện hành, đúng project mới; không chuyển sang project cũ.
- Picker được kiểm đúng MASTER01 v2 và đúng K20 mới. Composer có một image chip và một voice chip, không gắn D06 vào C02. Voice ID xác nhận qua picker; chip voice không tự hiển thị ID trong DOM.
- Cấu hình được nhìn qua UI: Ingredients, Omni 1.1 Flash, 720p, 9:16, 10s, x1, Agent OFF. Quote 15 ở trạng thái prompt còn trống **không là quote cuối**. Chưa bấm tạo.
- Trong tab Công cụ → Mẫu có Stringout Creator, mô tả “Stitch multiple video clips together”. Khi mở template để kiểm, UI tự chuyển sang một bản `Remix of Stringout Creator` trong project. Không yêu cầu sửa công cụ, không nhập media, không chạy hay chia sẻ. Không xóa bản remix vì chưa cần và không có yêu cầu xóa.
- Phần chức năng ghép chưa hiện điều khiển trim/arrange/export trong quan sát; chỉ thấy wrapper và cảnh báo có thể tiêu tốn credit. Vì vậy chỉ xác nhận **template có trong danh mục**, không xác nhận đã ghép được, ghép miễn phí, hoặc thay thế Scenebuilder. Scenebuilder/finishing của account mới vẫn cần kiểm riêng.

## Quy tắc rút ra

1. Việc chọn template có thể tự tạo bản sao; phải ghi nhận side effect thực thay vì báo thao tác hoàn toàn read-only. Không tiếp tục chạy tool nếu giá/chức năng chưa rõ.
2. Phân biệt catalog description, UI control khả dụng và kết quả export đã kiểm. Không lấy một mô tả template làm PASS năng lực dựng.
3. Framing C02 có thể là cận vừa hai người theo kế hoạch236. Props ngoài coverage vẫn phải giữ nguyên geography; không bắt vừa cận mặt vừa thấy trọn toàn bộ serving bằng zoom đơn giản.
4. Approval input, paper preflight và nghiệm thu media là ba cổng khác nhau. Câu “tiếp tục” cho phép chuẩn bị, không thay quyết định cụ thể master còn mở.

## Còn phải kiểm

Owner duyệt đúng master v2; tích hợp báo cáo DOP/ACT/EDIT; reviewer độc lập; prompt/quote cuối; điều khiển dựng đủ yêu cầu trên account mới. Các điều này chưa là bằng chứng footage720p đã đạt.
