# Hệ thống ChatGPT/Codex → Veo (mini)

Đây là vùng thử nghiệm nhỏ bên trong repository `agentic_cinema`, dùng để khám phá một quy trình tạo video trong đó:

- Codex/ChatGPT hỗ trợ biến brief thành các tài liệu và gói đầu vào có cấu trúc;
- con người giữ quyền quyết định tại các điểm ảnh hưởng lớn đến ý tưởng, quyền nội dung, chi phí và đầu ra;
- Google Flow/Veo là nơi tạo video;
- mọi quyết định nền tảng được chốt dần từ pilot thực tế, không sao chép nguyên kiến trúc production của dự án mẹ.

## Trạng thái

`pilot — P7 sản xuất lại 720p, chưa bàn giao` — trạng thái mới nhất tại [291](series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/291_C06-local-food-composite-and-pixel-qc.md): v3 local composite giữ base 720×1280, ngoài mask 0 pixel đổi và reproduce hash trùng; reviewer kiểm độc lập/root đọc đủ, đủ trình duyệt ảnh với caveat nhỏ mép A. Chưa owner duyệt ảnh/diễn B/voice/motion, upload/thay refs/EDL hoặc paid; 237/500 còn 263 credit, dự phòng 110 đóng. Cổng hình món toàn tập/timing/live còn mở. Source of truth là [folder series](series_anh_khoai_tay_chi_dao/README.md) và [EP01](series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/README.md); REC290 trở xuống giữ lịch sử.

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
