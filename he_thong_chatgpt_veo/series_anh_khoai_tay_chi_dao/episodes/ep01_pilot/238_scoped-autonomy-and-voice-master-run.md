# REC238 — Quyền tự vận hành và phục hồi đầu vào trên nick mới

Ngày 07/10/2026. Owner trả lời nguyên văn: **“1a; 2a”** cho hai câu hỏi tại REC237. Đây là quyền thao tác, không phải duyệt hình hoặc giọng đầu ra chưa xem/nghe.

## Điều đã xác định và quyết định đã chốt

- Cho phép preview/save đúng hai preset phục hồi K20/Orus và D06/Aoede dù UI không hiển thị phí; đối soát số dư sau từng preset, thấy phí thì dừng báo trước preset kế tiếp.
- Cho phép tự tạo/sửa trong kế hoạch 236: video native 720p, x1, giá hiển thị ≤15 credit mỗi đầu ra, tổng 500 theo phân bổ 165/180/45 và dự phòng 110. Dự phòng không tự giải ngân.
- Dừng khi cùng blocker lớn lặp hai lần; không tự đổi tool, script thoại, voice, giá cao hoặc mua/topup. Giữ checkpoint owner: master+hai voice → C02 → rough cut → final.
- Giữ project cũ. Không dùng footage cũ làm output mới hoặc coi approval cũ là approval trên nick mới.

## Thực hiện có bằng chứng

Hai preset đã lưu thực, mỗi giọng một lần tạo bản nghe trước và một lần lưu. ID mới, câu mẫu, nguồn chỉ dẫn diễn giọng và kết quả đọc lại nằm tại `restart_720p_v1/03_voices/bindings-238.json`. Sau từng preset, số dư là 1.050. Có một lần phát Đào bổ sung để chuẩn bị bàn giao; sau lượt này và MASTER01 v1, UI vẫn hiển thị 1.050. Root không tự chứng nhận đã nghe đúng giọng.

MASTER01 v1: Nano Banana 2.1/Image/9:16/x1, giá 0 sau khi đã gắn đủ 3 nguồn và prompt; một lần bấm tạo, một đầu ra. Đã tải bản gốc 1K, mở ảnh native và ghi hash. Review độc lập chặn FOOD-M01: hình thái món quá giống mì; nhận diện nhân vật, trạng thái F0, số lượng và vị trí đồ ăn/dụng cụ đạt trong phạm vi ảnh tĩnh. Khoảng trống ở mép và tỷ lệ file còn lỗi nhỏ. Không mở C02 từ v1.

MASTER01 v2: một lượt sửa giá 0 trên v1, thêm ảnh nem thật làm nguồn chất liệu, sửa món và đề nghị thêm khoảng trống ở mép; không đổi nhân vật/F0/vị trí đồ ăn. Đã tải native riêng, giữ v1 và file gốc. Review độc lập đóng lỗi món, không thấy lỗi lớn phát sinh; crop đĩa rau/cốc sát mép và native 768×1376 còn là lỗi nhỏ. Candidate được trình owner với giới hạn đó, chưa được duyệt. Đối soát sau v2: UI vẫn 1.050; đã chi quan sát trong run mới là 0.

## Giả định đang sử dụng và vấn đề còn mở

- Phục hồi đúng text/base tạo lại hướng giọng, không phải clone waveform tuyệt đối. Owner cần nghe trên nick mới.
- Source scene có thể kéo texture món sang output dù prompt phân vai; đây là giả thuyết từ v1, không kết luận cơ chế model.
- Không coi giá 0 hoặc số dư chưa đổi là quy tắc giá vĩnh viễn.
- Chưa có video sản xuất mới; chưa nghiệm thu chuyển động, khớp môi, bản 30 giây hay bản cuối. C02 chưa qua checkpoint đầu vào và chưa có mức giá với đầy đủ đầu vào thực.

## Công cụ/skill đã ảnh hưởng thao tác

[computer-use](C:/Users/PC/.codex/plugins/cache/openai-bundled/computer-use/26.1002.51308/skills/computer-use/SKILL.md) được dùng để thao tác Flow theo UI, kiểm quote/readback và đóng tab lỗi rồi mở tab mới. [imagegen](C:/Users/PC/.codex/skills/.system/imagegen/SKILL.md) và hướng dẫn prompting được dùng để phân vai nguồn, giữ invariants và sửa có mục tiêu; theo lựa chọn của owner, ảnh vẫn tạo trong Flow, không gọi API/CLI khác.

## Bước tiếp theo

Đóng review v2 bằng ảnh/hash thật, trình ảnh và hai tab nghe preset cho owner. Khi owner chốt đầu vào, mới chuẩn bị request C02/720p/x1/K20, kiểm giá ≤15, tạo một đầu ra và tải/kiểm từng khung cùng tiếng thực trước checkpoint C02. Không chạy thêm tuyển giọng hoặc thử tay riêng.
