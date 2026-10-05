# EP01 — Tiếp tục hình, tách tay và phản ứng
Ngày 2026-10-05. Owner: “kiểm lại sau, giờ làm gì tiếp thì xử lý tiếp đi nào”.

## Phạm vi
Hoãn kiểm identity giọng theo owner; SIA-01 và bảy lượt vẫn **HOLD**, giữ K20/D06/C-v0.6. Không sinh thoại mới, không Quality/master. Tiếp tục hình theo hướng tách tay/ánh nhìn đã ghi tại182, không đổi câu chuyện lấy trộm → bị bắt gặp → chữa cháy gắp cho Đào bằng cùng miếng nem chưa ăn.

## Bốn khung tham chiếu mới
Dùng imagegen tích hợp; giữ gốc, lưu sibling tại `assets/references/185/` và `C:/Users/PC/Downloads/du_an_nem_bui/185_split_motion/`. Không khẳng định giá imagegen hoặc trừ vào Flow.
- Nguồn bàn ăn: T-NB-03_v0.8.jpg, owner duyệt78. Khoai trái, Đào phải, rau/chấm trái, đĩa giữa, bát riêng, cốc phải Đào. 161 START chỉ hỗ trợ grip/tuft, không nguồn scene/food approved.
- Tay START/END: cận dưới cằm–bàn, mặt/miệng ngoài khung ngay từ thiết kế; đầu to đũa trong tay, đầu nhỏ kẹp một phần nem. Nâng ngắn từ trên bát về ngực dưới; tay trái đặt trên bàn, rau/chấm/đĩa ở phía đúng. Root xem actual hai ảnh, không thấy khói/chữ.
- Cận cảnh làm đĩa trông lớn; chất liệu/chi tiết món vẫn khác78. **Chưa FOOD/continuity PASS**, chưa owner canon approval.
- Đào START/END: nhìn xuống cốc phải → nhìn lên Khoai ở trái; môi khép, tay ở cốc. Root xem actual hai ảnh. **Chưa video phản ứng**, không lấy ảnh tĩnh làm động tác quay đi/quay lại đã đạt.

Cận tay là coverage mới thiết kế trước generation, không crop một cảnh đã ăn để giả chưa ăn. Hành động ngoài khung không thể suy từ crop. Prompt: [tay](evidence/185/image-prompts.txt), [phản ứng](evidence/185/reaction-image-prompts.txt), [video](evidence/185/prompt-hand-lift.txt). Hash/cấu hình: [preflight](evidence/185/preflight.json).

## Ba Lite đã chạy và tải đủ
Flow UI: Veo3.1 Lite /Frames /9:16 /720p /8s /x3 /Tác nhân tắt. Giá30, endpoint đúng thứ tự; innerText khớp nguyên prompt. Công tắc trả video không âm thanh bật. **Chỉ một submit**, không gửi lại khi download callback timeout.

Account đọc live224 →194; chi30. Sổ202/255 → **232/255, còn23**. Account194 không cấp thêm quyền chi. Không đủ bộ cùng giá30, không chuyển x1/x2 để né quy định ba Lite.

Ba native720×1280/H.264/24fps/8s giải mã sạch. **Cả ba có AAC audio stream**, chưa nghe nội dung. Công tắc bật không bảo đảm output thiếu audio; không gọi track là thoại/nhạc/im lặng chỉ từ probe.

| Mẫu | Quan sát root trên16 khung, cách0,5s | Kết quả |
| --- | --- | --- |
| V01 | Nâng cao hơn END rồi hạ; vệt hơi quanh thân/tay ở các khung sau, chưa xác định xuất phát từ đĩa. | REWORK toàn take. |
| V02 | Không thấy hơi trong grid; vẫn nâng cao rồi hạ thay vì giữ END một lần. | REWORK toàn take; ứng viên đoạn đầu. |
| V03 | Nâng gần/vượt mép trên, hạ và đổi đường đi; vệt hơi quanh thân. Contact ngoài khung chưa biết. | REWORK toàn take. |

Không agent độc lập hoặc review mọi frame native trong vòng này. Grid không thay xem liên tục/continuity cuối. [Kết quả/hash](evidence/185/results.json), [gridV01](evidence/185/V01-grid.png), [gridV02](evidence/185/V02-grid.png), [gridV03](evidence/185/V03-grid.png).

## Ứng viên hẹp V02
Đã xem **42 frame của0–1,75s ở180×320/frame**, thêm grid đầu12fps/240×426. Trong phạm vi này thấy một nhịp nâng ngắn, nem còn trước áo/bát, tay trái giữ bàn; không thấy hơi/chữ. Chưa kiểm pixel ở native resolution hoặc chứng nhận mọi lỗi vật lý đã hết.

Xuất riêng `V02_0.00-1.75_SILENT_CANDIDATE.mp4`:1,75s/42frame/720×1280, loại audio local, không crop/đổi tốc độ hoặc ghi đè native. **Chỉ ứng viên cơ học nâng ngắn**, chưa freeze/FOOD/continuity/owner PASS. Toàn take giữ REWORK, lỗi về sau công khai; không gọi take đã đạt từ đoạn cắt. Không đưa vào bản182 hoặc thay storyboard. [42frame](evidence/185/V02-range-all42.png).

Có khoảng chờ đầu; cần thử nhịp C01 → đoạn nâng → Đào nhìn lại và kiểm vị trí tay. Khung END tay tĩnh không mặc định khớp frame cuối đoạn cắt.

## Bài học và bước tiếp
- Đầu–cuối đúng không khóa đường đi: cả bộ vẫn vượt rồi quay về. Tách shot bỏ diễn mặt khỏi phép thử, chưa chứng minh sửa nâng–khựng.
- V01/V03 còn vệt hơi dù “cool/no steam”; batch đổi nhiều nhóm không chứng minh một từ/ảnh/ánh sáng là nguyên nhân.
- Không tiếng phải kiểm stream thật; insert riêng loại track mà không đổi giọng đã chốt.
- Tab cũ chưa tạo file; tab mới đúng URL + menu720p tải đủ dù callback timeout. Đối soát bytes/hash/probe/decode; không tái sinh vì lỗi tải.

Tiếp: nối thử ứng viên trên **planning có nhãn**, kiểm continuity với C01/cặp phản ứng mới; chuẩn bị chuyển nem sang bát Đào. Chưa chạy phản ứng hoặc chi thêm.23 không đủ batch30; nếu cần vượt phải có quyền bổ sung cho phép thử rõ ràng. Các cảnh mở, thoại/khớp môi, quay lấy cốc, chuyển–nhận, kết còn thiếu như182; không cam kết đủ hoàn tất phim trong23.

## Tổng kết vòng
- Đã xác định: bốn ảnh, ba video native và một đoạn ứng viên1,75s; cả ba take toàn clip chưa đạt.
- Đã chốt: tiếp tục hình, hoãn kiểm giọng nhưng giữ HOLD; một bộ ba Lite.
- Giả định: cut sang cận Đào có thể giữ nhịp bị bắt gặp; chưa kiểm chứng hiệu quả trong mạch.
- Còn mở: continuity món/đũa/điểm dừng, phản ứng động, chuyển–nhận, hình thoại và speaker identity.
- Tiếp theo: thử nối local và chuẩn bị chuyển–nhận; trình bổ sung khi phải chạy bộ vượt23. Chưa Quality/master/publish.
