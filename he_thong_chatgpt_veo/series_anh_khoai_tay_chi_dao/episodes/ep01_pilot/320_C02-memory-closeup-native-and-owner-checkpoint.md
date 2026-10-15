# REC320 — C02 cận ký ức: đã tạo native, chờ duyệt tiếng/diễn

Ngày 15-10-2026. Đã chạy **một lượt**, không tự chạy lại, trên đúng project EP01 720p. Đây là coverage bổ sung sau bản thô, theo quyền sản xuất REC238; không dùng quỹ tạo lại đã hết và không mở dự phòng. REC319 là gói ảnh tham chiếu riêng, không phải input của lượt này.

## Nguồn và thao tác thực tế

- Một ảnh K-memory ENTRY đã duyệt ở REC315, hash khóa trong request320; không dùng ảnh mới chưa duyệt thay thế.
- Một saved voice `EP01_Khoai_K20_Orus_720p_v1`, ID thực `b447b35c-b35e-4140-af72-ecd277282b1a`; không tạo hoặc sửa preset.
- Ingredients / Omni 1.1 Flash, 720p, dọc 9:16, 8 giây, x1, Agent tắt, âm thanh native. Giá đầy đủ 12 credit.
- Exact prompt và cấu hình/UI đã lưu trước khi bấm tạo. Output: `b7279ad9-50d5-44b2-b0a4-6234270991a3`.
- Tải bằng mục **720p Kích thước gốc**; browser xác nhận tải xong, đã copy nguyên byte vào `05_native/EP01_720_C02_COVERAGE_K20_T01_320_NATIVE.mp4`.

Lời duy nhất: “Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.”

## Đã kiểm và giới hạn kết luận

Native H.264 720×1280, 24 fps, 192 frame/8 giây; AAC 48 kHz stereo đủ 8 giây; 2.025.108 byte. Giải mã toàn file exit 0. SHA256: `32539bfe68fe9518ce7b14732033f5316d9251bafe53b74be8fb0ae65b18af78`.

Root đã xem board 24 ảnh trích ở 3 fps: mặt/miệng Khoai hiện rõ, ánh mắt từ dưới chuyển về Đào, không thấy nhảy góc lớn trong các mẫu, Đào chỉ là một phần tiền cảnh bên phải. Không có thao tác món ăn trong khung được kiểm. Có watermark Flow; không thấy chữ thoại sinh thêm trong mẫu. Đây **không** phải kiểm liên tục mọi frame, đo lipsync hoặc báo cáo độc lập.

ASR offline không initial prompt nhận đúng hai câu: 0–2,50 giây và 3,46–6,90 giây. Audio mean −19,9 dB, max −0,2 dB; silence cuối khoảng 1,081 giây. Không dùng các số này để kết luận giọng đúng K20 hoặc diễn truyền cảm. Chưa cắt đuôi, đổi tốc độ, thay audio hay ghép EDL.

Bundled Python thiếu faster-whisper: giữ diagnostic dở dang trong `C02_COVERAGE_ASR_320`, chạy lại bằng venv sẵn có trong folder mới `C02_COVERAGE_ASR_320_VENV`, thành công; không cài hay gọi API. Lỗi điều khiển card sau tải được xử lý bằng đóng tab lỗi/mở đúng URL output trong tab mới, không tạo video lại.

## Ngân sách đã đối soát

Live account 1.029 → 1.017, delta **12 credit**, khớp quote. Sổ dự án: đã chi **291/500**, còn **209** = tạo mới 66 + tạo lại 0 + coverage 33 + dự phòng 110 còn đóng. Balance tài khoản không phải ngân sách dự án.

## Gate tiếp theo

Owner xem/nghe đúng native mới để chốt **K20 xuyên suốt, đủ lời/nhịp, khẩu hình và diễn** của C02. Approval tiếng cũ không tự chuyển sang take này. Chưa duyệt điểm nối hoặc toàn phim. Không chạy lại trong lượt này.

Nếu C02 được chấp nhận: mới chuẩn range/điểm nối trong dựng thử; bộ REC319 vẫn là still candidates chưa duyệt nguồn video, chất liệu A giữa các ảnh và continuity native còn mở. Final 30 giây, nhịp/góc quay toàn tập, âm thanh và disclosure AI chưa đóng.

Handoff native và bằng chứng tại `C:/Users/PC/Downloads/du_an_nem_bui/320_C02_MEMORY_COVERAGE`. Chi tiết máy đọc: `restart_720p_v1/06_qc/run-registry-320.json` và request320.
