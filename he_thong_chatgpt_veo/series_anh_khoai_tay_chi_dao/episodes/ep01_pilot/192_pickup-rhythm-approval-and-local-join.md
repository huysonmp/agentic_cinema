# EP01 — Duyệt nhịp P02 và kiểm nối local

## Cập nhật tại193

Owner đã “ok” cặp185 v0.2 và bổ sung30 cho một x3 Lite tại[193](193_dao-reaction-x3-approved-execution.md). Đã chạy/tải đủ nhưng cả ba REWORK diễn, chưa chọn phản ứng; chi30, trần292, còn0. Các đoạn chờ quyền thử/còn0 trên trần262 dưới đây là lịch sử. P02 chỉ được duyệt nhịp0–2,5s, không mở rộng từ approval phản ứng.

Ngày 2026-10-05. Owner trả lời **“duyệt”** cho đề xuất sau191: dùng nhịp gắp P02 đầu2,5s rồi kiểm nối local sang cảnh Đào nhìn lại. Khóa approval theo file SHA256 `9dde08e3bef922ee8b1456b10d2bb6552ff40d6406eea6d9ae73cddc34b5045b`, range0–2,5s/60frame. Không duyệt native8s còn lỗi, FOOD toàn cảnh, continuity, ảnh phản ứng, giọng, master hoặc credit mới.

## Quyết định dựng thử

Dùng P02 duy nhất cho gắp khỏi đĩa và kéo nem về trước bát. Không ghép lại C01 hoặc V02 cũ để lặp gắp/đổi miếng món. Giữ toàn bộ186/182 và media191 nguyên bản, dựng sibling192. Chưa thay bản30s bằng kết quả kiểm này.

Đối soát169/185/186: chưa có video phản ứng Đào đạt. Hai ảnh185 chỉ làm placeholder có nhãn, không nội suy chuyển động hoặc gọi quay đầu đã hoàn tất. Frame59 lấy từ **chính file P02 owner vừa duyệt**, không lấy lại PNG ảnh sinh188 làm endpoint giả. Freeze cuối chỉ kiểm bố cục, không thay diễn khựng.

## Kết quả dựng và kiểm actual

Config/timeline: [join-config.json](evidence/192/join-config.json). Đã render bản6s không tiếng: `C:/Users/PC/Downloads/du_an_nem_bui/192_approved_pickup_join/render_v0.1/EP01_PICKUP_TO_DAO_6s_PLANNING_v0.1.mp4`.

| Timeline | Loại/ý nghĩa |
| --- | --- |
| 0–1,25s | Ảnh185 Đào ở cốc; thiếu động tác quay đi. |
| 1,25–3,75s | P02 đoạn0–2,5s: nhịp gắp đã duyệt. |
| 3,75–5s | Ảnh185 Đào nhìn trái; thiếu quay lại thật. |
| 5–5,5s | Freeze frame59 từ P02; không gọi đã diễn khựng. |
| 5,5–6s | Thẻ thiếu nâng–khựng và phản ứng động. |

Chỉ2,5s nhịp video owner duyệt;3s ảnh tạm và0,5s thẻ thiếu. Không biến6s thành coverage diễn đã đạt hoặc thời lượng final đã khóa. Không kéo dài P02 bằng nội suy/freeze không nhãn; không cắt/tăng tốc động tác owner vừa duyệt.

Root đã xem hai ảnh185, frame cuối P02 và contact sheet12 khung cách0,5s của bản6s. Toàn hình được thu vừa bên dưới dải nhãn, không che grip/cốc/watermark; không dùng crop để giấu điểm nối. **Trục làm việc có cơ sở trên ảnh**: Đào bên phải, Khoai/jacket ở mép trái, gaze END Đào sang trái. Tuy nhiên ảnh START mới chỉ nhìn xuống cốc, chưa quay người ra khỏi Khoai; không tuyên bố hoàn tất “quay lưng”. Trong shot Đào không thấy nem/tay Khoai, nên chưa thể kiểm bảo toàn miếng nem hoặc nhịp nâng bị bắt gặp qua cut. Ánh sáng chủ thể đều ấm; background Đào có sắc xanh/chạng vạng, cận tay chưa đủ background để chứng nhận thời điểm/ánh sáng toàn cảnh đồng nhất. Chưa independent reviewer hoặc creative PASS.

Mục tiêu phép thử được thu hẹp đúng: kiểm thứ tự/cỡ cảnh/trục dự kiến, không chứng minh motion match-on-action. P02 đã lấp **đường đĩa→bát Khoai trong chính clip**, vì vậy không mang thẻ thiếu cầu nối cũ của186 sang bản192. Nhịp nâng thêm về mình, phản ứng Đào thật, biểu cảm bị bắt gặp và chuyển sang bát Đào vẫn mở. Frame59 native được lưu để khung tay tiếp theo bám actual, không mặc định END188 khớp video.

Kỹ thuật:720×1280/24fps/144frame/6s, không audio, full decode sạch. SHA256 `f46f7a9721122c5ced10b07dc99e72246d9d5a51e8f9aa4161f47895b46e33e6`. [Manifest](evidence/192/manifest.json), [contact](evidence/192/contact.png). SIA HOLD được ghi trong manifest và không dùng audio A03/R01.

Mở rộng `scripts/render_ep01_action_join_probe.py` bằng config/hash khóa cho từng source, duration/framecount động và approval theo shot. Không đổi default186: render hồi quy cho hash nguyên `996f250d9e34ac05520495d308678475fba397d4172901f7fde517d9d400965e`. py_compile đạt; rerun vào folder192 không rỗng bị từ chối, output hash không đổi. Đây là kỹ thuật, không chứng nhận diễn.

[Verification](evidence/192/verification.json) ghi read-back: hash mọi nguồn khớp, tổng timeline 6s = 2,5s nhịp video + 3s ảnh tạm + 0,5s thẻ thiếu; không audio hoặc chi mới. Owner tiếp tục yêu cầu “tieeps di”: hoàn tất gói local và trình bước còn cần quyền, không suy thành cấp30 credit chưa được hỏi trước đó.

## Gói tiếp theo đã chuẩn bị, chưa được phép chạy

Ưu tiên **Đào quay nhìn lại một lần, trước câu N05**. Dùng cặp185 v0.2 đã xem trong bản kiểm này; khác cặp167 đã thất bại ở169 ở chỗ foreground trái chỉ mép áo, không có má Khoai lớn phải giữ ổn định. Đây là giả thuyết giảm việc diễn/foreground, chưa chứng minh sẽ tốt hơn. Không tiếp tục lấy cặp167 fail và gọi là sửa đã kiểm.

[Prompt draft](evidence/192/dao-reaction-DRAFT-NOT-SUBMITTED.txt), [gói cổng kiểm](evidence/192/reaction-next-gate.json): một x3 Lite, chỉ mắt/đầu quay về Khoai; môi khép/tay/cốc giữ. Shot này không dùng làm cảnh Đào đang nói, chưa xử lý lipsync N05 hoặc cả đoạn bắt gặp. Không yêu cầu model làm tay Khoai/trao món ngoài frame.

Cần owner duyệt **cặp ảnh185 v0.2 làm đầu vào thử** và **bổ sung tối đa30 cho một batch x3**, giá30 là quan sát191, chưa đọc live lượt này. Nếu được duyệt, trần tăng262→292; phải kiểm lại giá và dừng nếu vượt30. Không cam kết30 đủ hoàn thành tập; không mở Quality từ approval nhịp P02.

## Tổng kết vòng

- Đã xác định: nhịp P02 có owner approval, bản kiểm6s dựng/decode, trạng thái thiếu đã tách rõ.
- Quyết định chốt: range0–2,5s/60frame được duyệt về nhịp; chỉ kiểm local, giữ C-v0.6/K20/D06.
- Giả định: cận Đào với mép áo trái có thể đọc được ánh nhìn sau insert; chưa thử diễn động.
- Còn mở: Đào quay lại, Khoai nâng/khựng, nối trạng thái nem, hình thoại/chuyển–nhận/kết và SIA HOLD.
- Tiếp: owner xem bản kiểm và chốt cặp khung/quyền thử phản ứng; không chạy thêm khi chưa có quyền.

Chi0, quyền còn0; không mở Flow hoặc đọc số dư live lượt này. Approval không thay gate FOOD toàn cảnh/continuity/master/publish.
