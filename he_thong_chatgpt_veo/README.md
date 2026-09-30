# Hệ thống ChatGPT/Codex → Veo (mini)

Đây là vùng thử nghiệm nhỏ bên trong repository `agentic_cinema`, dùng để khám phá một quy trình tạo video trong đó:

- Codex/ChatGPT hỗ trợ biến brief thành các tài liệu và gói đầu vào có cấu trúc;
- con người giữ quyền quyết định tại các điểm ảnh hưởng lớn đến ý tưởng, quyền nội dung, chi phí và đầu ra;
- Google Flow/Veo là nơi tạo video;
- mọi quyết định nền tảng được chốt dần từ pilot thực tế, không sao chép nguyên kiến trúc production của dự án mẹ.

## Trạng thái

`pilot — P5 owner content approved / final review pending` — P0/P1/P2/P3 đã duyệt; owner đã chấp nhận [C-v0.5](series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/32_p5-script-c-v0.5-approved-content.md), có [approval đúng nội dung](series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/33_p5-c-v0.5-owner-content-approval.md). Chưa toàn bộ P5 quality pass, chưa media/generation. Source of truth là [folder series](series_anh_khoai_tay_chi_dao/README.md); thiết kế Tier 1 đã duyệt, runtime version chờ review.

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
