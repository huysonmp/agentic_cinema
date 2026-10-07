# 226 — REF01-M v03 và bộ tham chiếu mở cảnh

**Cập nhật tại [227](227_owner-reference-lock-and-motion-preflight.md):** owner đã chấp nhận M v03 về tư thế ảnh tĩnh. S/M đã tách thành asset riêng và kiểm đồng byte; gói motion đã chuẩn bị, chưa chạy. Các trạng thái chờ nghiệm thu dưới đây là lịch sử REC226, không ghi đè approval227.

Ngày: 2026-10-07. Giai đoạn P7 khắc phục / hoàn thiện G1. Một lượt sửa M từ S đã tạo, tải native và kiểm độc lập. **V03 dùng được cho tư thế ảnh tĩnh, có lưu ý che khuất mép bát; chờ owner nghiệm thu.**

## Kết quả hiện hành

| Reference | Phiên bản được đề nghị giữ | Kết luận hiện hành |
|---|---|---|
| REF01-S | v01, REC224 | Hai tay nghỉ, môi khép; giữ làm nguồn mở cảnh |
| REF01-M | v03, REC226 | Tay ngoài Đào vươn tới gần vành phải, gap nhìn rõ; usable candidate ảnh tĩnh |
| REF01-E | v02, REC225 | Đã sửa môi cả hai; hai reviewer đánh giá dùng được ở mức ảnh tĩnh |
| REF03-S | v02, REC225 | Đã sửa môi Đào, giữ nụ cười kín Khoai; hai reviewer đánh giá dùng được ở mức ảnh tĩnh |

M v01/v02 giữ làm lịch sử lỗi, không chọn làm nguồn của tư thế vươn tay. Bộ trên vẫn là đề nghị chọn reference; chưa tự biến approval chạy thử thành owner acceptance.

![Đối chiếu S nguồn, M v02 và M v03](C:/Users/PC/Downloads/du_an_nem_bui/226_ref01_m_v03_from_s/REC226_SOURCE_V02_V03.png)

![Chi tiết khoảng hở và mép bát](C:/Users/PC/Downloads/du_an_nem_bui/226_ref01_m_v03_from_s/REC226_HAND_DETAIL.png)

## Kiểm thực tế

[EDIT độc lập](evidence/226/01_edit-pose-review.md): USABLE CANDIDATE, không phát hiện MAJOR. [CONT/FOOD độc lập](evidence/226/02_cont-image-review.md): PASS_WITH_CAVEAT_IMAGE_ONLY. Root đã đọc đầy đủ hai báo cáo sau khi từng reviewer chốt độc lập và cùng kết luận.

Tay đúng phía ngoài, đầu ngón thấp hơn đỉnh món, khoảng nền bàn giữa ngón–vành gốm nhìn thấy. Không thấy chạm nem, cầm đồ, nhấc đĩa, khói hoặc thay số lượng bộ phục vụ. Miệng khép và tay còn lại nghỉ. **Caveat:** tay che một phần mép trước-phải bát Đào trong hình chiếu; chưa thấy nhập/xuyên bát, khoảng cách 3D chưa xác định. Cần kiểm đường tay bằng frame khi có motion, không thêm retry chỉ vì ảnh tĩnh không chứng minh 3D.

Ba bản download/owner/repo đồng hash; JPG native 768 × 1376. Source S và prompt đúng hash; prompt có nguyên văn trong preflight/result. Một request, không retry, quote 0. Số dư sau 77, bằng snapshot cuối REC225; không có phép đo số dư ngay trước request REC226. [Manifest](evidence/226/native-output-manifest.json), [root readback](evidence/226/03_root-image-readback.md), [nhật ký](evidence/226/execution-log.md), [kết luận QC](evidence/226/qc-resolution.json).

## Bài học định danh Flow

Lượt này dùng editor của S, nên M v03 nằm trong lịch sử cùng container có tên S. Tên download cũng kế thừa S. Source image UUID `22a0d77a-c8db-4a62-82ef-9ed93d34e7f2` và output image UUID `944bb01f-da47-4b68-8281-2aa5c04c546a` khác nhau; native S được giữ nguyên. Chọn input tương lai theo exact version/content UUID/hash, không chỉ tên card.

Khi chuẩn bị motion, cần đưa native M v03 vào asset riêng, đối soát lại native/hash, đồng thời kiểm S đúng phiên bản tay nghỉ. Đây là bước chuẩn bị được đề nghị, chưa được thực hiện trong REC226.

![Bản v03 trong lịch sử Flow](D:/Workspace/agentic_cinema/he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/evidence/226/handoff-ui.png)

## Tổng hợp và bước tiếp

Đã xác định: sửa tay M có tiến triển đạt mục tiêu ảnh tĩnh, sửa môi E/R03 đạt; các nguồn được lưu và kiểm định danh. Quyết định đã chốt: gói ba sửa REC225 và một sửa REC226 đã thực thi trong đúng số lượt/quote. Chưa chốt nghiệm thu bộ reference.

Giả định đang dùng: M v03 là khoảnh khắc trước khi chạm đĩa, không đổi kịch bản thành đã cầm/kéo hoặc chuyển món. Còn mở: nghiệm thu reference, đường đi tay qua bát/đũa, kéo–dừng, nối S–M–E, lời–hình và bộ R01–R09 toàn tập. G1/full AV còn mở.

Bước tiếp: owner xem và chọn bộ S v01 / M v03 / E v02 / REF03-S v02; sau đó tách input có định danh riêng, lập preflight chuyển động và phạm vi thử tương ứng. Chưa tạo video/voice/Quality hoặc bản dựng cuối trong lượt này.

Ảnh và hồ sơ ở [folder owner](C:/Users/PC/Downloads/du_an_nem_bui/226_ref01_m_v03_from_s). Áp dụng hướng dẫn [computer-use](C:/Users/PC/.codex/plugins/cache/openai-bundled/computer-use/26.930.61225/skills/computer-use/SKILL.md) cho vận hành và lưu chứng cứ UI; dùng kỷ luật mô tả vùng sửa/giữ của [imagegen](C:/Users/PC/.codex/skills/.system/imagegen/SKILL.md), theo lựa chọn tạo ảnh trên Flow của owner.
