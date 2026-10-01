# P6 — Chốt đầu vào vòng tiếp theo

2026-10-01. Owner: “làm tiếp 6 đi nào, cần gì hỏi thì hỏi đi, đề xuất gì thì đề xuất đi”. Working interpretation tiếp tục P6, không tự đóng gate6. DRAFT_FOR_OWNER_DECISION, chưa generation/voice/video approval mới.

## Baseline và actual inspection

- Script C-v0.5 + cue38 giữ nguyên; primaryduo45 identity/outfit, không dùng outfit proposal39 cũ thay primary.
- Grip direction ownerselected62: I03/I05; không mở lại sửa đũa hoặc dùng I07/I09 làm geometry ref.
- Root đọc39/56/62 và actual view_image R03_sidewalk_v0.3.jpg + R04_kitchen_v0.2.jpg. R03: hai bạn ngồi nhìn nhau, dusk street, mặt bàn nhỏ; chưa đủ layout đĩa/bát/cốc, không serving shotlock. R04: standing pair kitchen, chưa seating/action layout. Cả hai là mood candidates, chưa tự approve location.
- F-NB-02 unresolved theo56/57, chưa output usable; không retry mù. Food evidence54 còn provenance/portion gaps.

## Bốn quyết định owner cần trả lời

1. **Bối cảnh tập1:** A bàn quán nhỏ ven phố, giờ chiều tối (đề xuất, tiếp nốiR03; natural gặp món/chill, cần bàn đủ rộng và bớt nền gây xao nhãng); B bàn ăn trong bếp/nhà (ấm, nối ký ức tốt nhưng cần dựng seating mới, không gán sống chung); C bối cảnh khác do owner mô tả. Không địa điểm thật/nhãn hiệu/landmark chưa nghiên cứu.
2. **Ai hỗ trợ xác nhận tạo hình món:** A root tìm tư liệu ảnh có xuất xứ rõ, dựng comparison và trình owner (đề xuất nếu owner không có tư liệu; chưa tự certify khi nguồn thiếu); B owner cung cấp ảnh món/nguồn hoặc người am hiểu để đối chiếu (sát mong muốn hơn nếu có, cần xác định provenance/quyền trước upload). Không ảnh báo uploaded tự động; dữ liệu thực quyết định dạng món/phần gắp, không chọn thẩm mỹ thay fact.
3. **Lượt món mất kết quả:** A cho kiểm Flow thêm một lần; nếu vẫn không có terminal/output, cho phép chuẩn bị một request food-only mới riêng, giữ02 unresolved và trình exact request trước submit (đề xuất, không chờ vô hạn và không che lịch sử); B chưa mở request mới, owner kiểm tài khoản/notification trước (giữ không phát sinh nhưng food dependency chờ). Lựa chọn này không ghi02 success/fail hoặc nocharge.
4. **Hướng thử tiếng:** A ưu tiên một probe đối đáp ngắn trong Flow/Veo sau khi xác minh feature/model/cost và duyệt request (đề xuất vì provider dự trù hiện có; chưa đảm bảo voice consistency/lipsync); B tách audio AI riêng rồi ghép (kiểm giọng riêng thuận tiện, thêm provider/workflow và đồng bộ miệng phải kiểm, chưa cấp quyền nhà cung cấp mới). Cả hai chỉ decision hướng, không tự mở voice/video ngay.

## Sáu work packages P6

| Nhóm | Đầu ra và kiểm bắt buộc | Dependency/decision |
|---|---|---|
| W1 Character/expressions | Baseline exact-version; lựa chọn attention/khựng/chữa cháy và Đào nhận ra/trêu, pose/angle kiểm so primary | Đã có candidates, chưa broad approval; góc side Khoai còn gap, không ghi PASS |
| W2 Props/staging | Layout đĩa ở giữa, bát trước mỗi người, cốc bên ngoài Đào; hand refs I03/I05; tránh va chạm, đủ diện tích bàn | Q1; giữ grip, chưa motion proof |
| W3 Food evidence/candidate | Appearance/portion ledger, provenance; food-only candidate đối chiếu nguồn, ownerselection riêng | Q2/Q3; không AItoAI food validation |
| W4 Set/style frame | Reference bối cảnh, pair seated, tabletop and food composition; không driftface/outfit hoặc romance | Q1 + W2/W3; không ghép món chưa khóa thành approved frame |
| W5 Voice/performance | Exact script samples, nghe attitude/phát âm/nhịp, log measured duration; không clone giọng người thật | Q4 + feature/cost/request approval riêng |
| W6 Gate package | Reference index selected/rejected/unknown, source/rights scope, findings/dependencies, owner approval P6 | W1–W5; missing critical inputs không complete |

## Giả định làm việc không cần hỏi lại

Hai người trưởng thành, bạn bè; giữ outfit primary, props bình dân khôngbrand; không thêm flashback mẹ/hồi bé; cốc có sẵn trong tầm lấy, không đổi script. Khoai bên trái/Đào bên phải là staging draft để so với candidates, không axis/camera lock. Final video9:16 ~30s, Canva ownerassembly; mọi motion request thuộc planning/gate sau.

## Thứ tự tiếp tục

Sau answers, record exact decisions: food evidence/reconciliation và set/props spec → thử thành phần có version/QC → integrated style frame → expressions/voice tests theo request đủ quyền → owner P6gate. Có thể lập P7 draft action/coverage khi dependency đã rõ, nhưng không ghi productionready khi refs/food/voice thiếu. Chưa cần dựng agent mới trước kiểm thiếu input cụ thể; role hiện có hỗ trợ từng chuyên môn theo contracts, không gọi tất cả role như checklist hình thức.

Đã xác định: existingmoodframes + grip refs dùng để tiếp tục, tablelayout phải thiết kế. Quyết định đã chốt: chỉ baseline cũ, không có answers mới. Giả định: phục vụ episode1 trước, không đổiseriescanon. Còn mở: bốn decisions trên và evidence món/voice/media. Tiếp theo: owner answers; root lo research/verification/request/artifact, không đẩy câu hỏi fact cho owner đoán.
