# REC314 — Kiểm ảnh góc cận và ghi kinh nghiệm

Ngày 14/10/2026. **ROOT_STATIC_REVIEW; không phải báo cáo phản biện độc lập hoặc creative/AV PASS.**

## Kiểm theo nhiệm vụ

| Vai kiểm | Evidence / nhận xét | Trạng thái |
| --- | --- | --- |
| DIR |Ảnh ký ức đưa chú ý về Khoai; ảnh hỏi đưa về Đào. Chưa biết hiệu quả khi ghép với tiếng/thời lượng thực |Có ứng viên, chưa nghiệm thu |
| DOP |Đổi coverage từ khung đôi sang cận ưu tiên từng nhân vật. Hậu cảnh/cỡ đầu/headroom chưa khớp hoàn toàn; chưa đo camera geometry cùng world |Owner xem hướng, production HOLD |
| ACT |Khoai cười kín, Đào tò mò thân thiện; miệng khép trong ảnh |Static cue, không phải diễn video |
| CONT |F148 nhìn xuống; K-memory v2 nhìn Đào không dùng làm entry. Đã thêm K-entry nhìn xuống. Props ngoài cận vẫn theo scene state, A chưa được gắp |Có cặp trạng thái để kiểm, chưa nối native |
| EDIT / AV |Không sửa footage/EDL/PCM, chưa có cảnh cận native hoặc môi nói để sync |HOLD, chưa được phép paid |

## Nhật ký bảy ảnh

1. A0 v1: nem cải thiện theo tư liệu, nhưng rau/cốc cắt biên; không chọn.
2. A0 v2: cốc hiện trọn hơn, mép trái rau vẫn thiếu; lỗi chính lặp hai lần. Dừng sửa master nhánh này, không làm input downstream.
3. K-memory v1: mặt có ưu tiên và hướng nhìn, nhưng vùng món ở đáy mang lỗi chất cũ; không chọn.
4. K-memory v2: bỏ bàn khỏi phạm vi cận ký ức, có ứng viên. Đây là coverage đúng mục đích, không sửa được món cũ ở cảnh khác.
5. D-question v1: lá cắt mép, foreground Khoai chiếm quá nhiều; không chọn.
6. D-question v2: lá hiện đủ, foreground giảm; có ứng viên. Headroom Đào còn nhiều và scale giữa hai góc chưa đồng nhất.
7. K-entry v1: đổi gaze xuống từ K-memory v2 để tránh entry nhảy nhìn Đào; có ứng viên. Eyelid/biểu cảm có thay đổi đi kèm redraw, không claim chỉ pixel mắt đổi.

## Kinh nghiệm và giả thuyết nguyên nhân

**Đã quan sát:** yêu cầu giữ trọn mọi đạo cụ trong khung chung không tự được thực hiện dù prompt có câu margin; edit còn giữ bố cục gốc rất mạnh. Cận tạo từ master có thể mang chất món sai vào mép ảnh. “Ảnh mặt đẹp” có thể sai entry gaze so exact đoạn trước.

**Giả thuyết, chưa kết luận về model:** ràng buộc nhiều mục tiêu — mặt lớn, mọi đạo cụ đủ, bối cảnh giữ, portrait cố định — và bố cục tham chiếu đang kéo kết quả về crop cũ. Không có thí nghiệm ablation để chứng minh một câu prompt là nguyên nhân duy nhất.

**Kiểm soát mới:** mỗi prompt có đúng nhiệm vụ cảnh và state ledger; phân biệt giữ scene với bắt hiện mọi prop. Sau hai lỗi chính giống nhau dừng nhánh, không lặp câu “wider” mù. Cận mới phải đọc cùng endpoint trước, không dùng ảnh đang hướng tới cảm xúc làm entry khi trạng thái chưa đến. Với cảnh hành động, không áp giải pháp bỏ bàn ra khỏi cận để giấu A/bát/tay.

## Nguồn và giới hạn

Đã kiểm native dimensions và SHA-256 của chín PNG trong gói (bảy generated, hai sao chép nguyên hình), đã xem từng kết quả. Copy master khớp approval242; F148 sao chép đúng decoded PNG00149 của rough312. Tất cả generated được lưu không chỉnh pixel, có prompt và đầu vào riêng trong manifest.

Không gọi image generation là miễn phí mọi nguồn lực: chỉ xác nhận Flow chi 0 vì không thao tác Flow. Không có tiếng mới, motion, cảnh paid hoặc review độc lập mới. Owner chưa duyệt ba ảnh cụ thể; không chuyển approval hướng A sang production. Budget và reserve giữ nguyên theo sổ gần nhất.
