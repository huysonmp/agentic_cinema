# Hệ thống ChatGPT/Codex → Veo (mini)

Đây là vùng thử nghiệm nhỏ bên trong repository `agentic_cinema`, dùng để khám phá một quy trình tạo video trong đó:

- Codex/ChatGPT hỗ trợ biến brief thành các tài liệu và gói đầu vào có cấu trúc;
- con người giữ quyền quyết định tại các điểm ảnh hưởng lớn đến ý tưởng, quyền nội dung, chi phí và đầu ra;
- Google Flow/Veo là nơi tạo video;
- mọi quyết định nền tảng được chốt dần từ pilot thực tế, không sao chép nguyên kiến trúc production của dự án mẹ.

## Trạng thái

[REC302](series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/302_C07-native-rejected-and-regression-diagnosis.md): một C07 max7 đã chạy/tải native720p/hash/decode/QC96F. Root và reviewer loại: Đào hóa người, cốc về bàn/hai tay nâng bát; không prefix hoặc retry/C08. Sổ258/500, còn242, retake5/reserve110 đóng. Đã truy input đúng F47 và thiếu kiểm hồi quy277/280; gói sửa nhận diện/ngân sách chờ quyết định. REC301 bên dưới giữ lịch sử.

[REC301](series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/301_C07-receive-live-preparation-and-one-run-gate.md): gói C07 từ native F47 + một D06 đã chuẩn live, quote7/720p/4s/x1; Agent tắt, giữ tiếng. Chưa submit, đang chờ duyệt một lượt; motion/food seam/timing cuối còn mở. Chi0, sổ251/500/còn249, retake12/reserve110 đóng. REC300 bên dưới giữ lịch sử.

[REC300](series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/300_C06-range-approved-and-receive-preflight.md): owner duyệt range C06 2 giây và đối thoại/sync exact bản nối 4,75 giây. Đã chuẩn START ứng viên từ native F47 và preflight nhịp Đào nhận; chưa chạy thêm. Món/A đổi tại cut vẫn mở; rough35 đã được cho phép tại REC264, không final35. Chi 0; còn 249, tạo lại 12, dự phòng 110 đóng. Nội dung REC299 bên dưới giữ lịch sử.

`pilot — P7 sản xuất lại 720p, chưa bàn giao` — trạng thái mới nhất tại [299](series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/299_C06-accepted-native-and-short-join-trial.md): tiếng/K20 và diễn native C06 được owner chốt, ánh nhìn đầu chấp nhận cho chuẩn nối. Trial C05→C06 mới dài 4,75 giây đã dựng/kiểm; range 48 khung và đối thoại/sync trên bản encode chưa duyệt, hình món đổi tại cut vẫn là lỗi mở. Không trả phí hoặc thay EDL chính; 251/500, còn 249, phần tạo lại 12, dự phòng 110 đóng. Thời lượng 30 giây và chất lượng toàn tập chưa đóng. Source of truth là [folder series](series_anh_khoai_tay_chi_dao/README.md) và [EP01](series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/README.md); REC298 trở xuống giữ lịch sử.

## Tài liệu đang dùng

Các tài liệu khám phá bên dưới giữ lịch sử quyết định. Trạng thái stage hiện tại và các approval cụ thể đọc tại [index series](series_anh_khoai_tay_chi_dao/README.md) và [EP01](series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/README.md), không suy từ một working draft cũ.

- [Khám phá vòng 1](docs/00-kham-pha-vong-1.md)
- [Chốt vòng 1 và khám phá nội dung vòng 2](docs/01-chot-vong-1-va-kham-pha-noi-dung.md)
- [Định hướng quality-first và khung quy trình kế thừa](docs/02-dinh-huong-quality-first.md)
- [Giải thích 15 stage và các giả thuyết chưa kiểm chứng](docs/03-giai-thich-va-cai-tien-cac-stage.md)
- [Hiệu chỉnh: baseline đầy đủ và khám phá Human × AI](docs/04-hieu-chinh-va-kham-pha-human-ai.md)
- [P0 — Project Foundation working draft](docs/05-p0-project-foundation.md)

## Nguyên tắc tạm thời

1. Bắt đầu bằng một outcome video cụ thể, không bắt đầu bằng danh sách agent.
2. Tự động hóa việc chuẩn bị và kiểm tra tài liệu trước; chưa tự động chi tiền hoặc tạo video hàng loạt.
3. Mọi đầu ra gửi sang Veo phải được con người duyệt.
4. Phân biệt rõ dữ kiện, giả định, đề xuất và quyết định đã chốt.
5. Agent/skill/tool bám contract và phạm vi owner đã duyệt; hiệu quả phải kiểm bằng pilot, không mặc định có nhiều agent là chất lượng đã đạt.
6. “Mini” là tối giản hạ tầng và tự động hóa, không tối giản quy trình kiểm soát chất lượng.
