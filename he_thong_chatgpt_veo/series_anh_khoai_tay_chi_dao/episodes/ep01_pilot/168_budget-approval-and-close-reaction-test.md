# 168 — Duyệt ngân sách, tái dùng audio và thử cận phản ứng

Ngày 2026-10-03. Owner trả lời “làm tiếp đi nào, ok nhé” sau hai câu cụ thể ở167: điều chuyển100 Quality sang hoàn thiện (trần134), và tái sử dụng audio R01 ba câu cuối. Ghi nhận chấp thuận hai đề xuất đó, giữ hướng chuyển động; không phải duyệt toàn tập, lip-sync, claim placement hoặc release. Audio là OWNER_REUSE_APPROVED, không gắn nhãn independent-ear-QC PASS. Root đã thông báo cách hiểu trước thao tác; có thể cập nhật nếu owner sửa ý.

## Quyền chi mới

Trial34 + khoản Quality100 điều chuyển = **134 credit còn được phép chi**. Không giữ thêm một khoản Quality100 đồng thời để tránh đếm hai lần. Số dư account đầu vòng đọc actual334; không coi toàn bộ334 là quyền chi. Bộ cận này dự kiến x3 Lite30, để lại104 nếu charged đủ; không bảo đảm toàn tập hoàn thành trong trần. Chi actual đối soát cuối vòng, không lấy lỗi audio/refund làm tiền chắc chắn.

## Input và mục tiêu

Cặp khung167: `C:/Users/PC/Downloads/du_an_nem_bui/167_reaction_reference_pair/START_Dao_close_v0.1.png` và `END_Dao_close_v0.1.png`. Hash/provenance trong167, không sửa ảnh ở lượt này. Mục tiêu chỉ phản ứng một nhịp nhìn cốc/phải → nhìn Khoai/trái → giữ, môi khép/thân/tay/foreground ổn. Không coi việc tay/món ngoài khung là đã đạt cảnh nâng-khựng hoặc chuyển-nhận.

## Prompt nguyên văn

```text
Locked camera. Match the supplied frames. Dao slowly turns her head once from looking down at her glass on screen right to looking up at Khoai on screen left, then holds a gently amused knowing look. Her lips stay closed. Her torso and arms remain at their supplied positions. Keep the blurred potato cheek and navy shoulder still at the left edge. Preserve the same peach face, leaf, blouse, glass, light and background.
```

Gói dự thảo167 giữ nguyên, không thêm audio clause hoặc tự đổi script/giọng. Flow project `9276788e-9781-44fb-ba5b-083006667374`; media/evidence tại `C:/Users/PC/Downloads/du_an_nem_bui/168_close_reaction_lite/`.

## Nhật ký actual / kết quả

Đã mở lại tab trong đúng IAB2 sau khi tab cũ không còn. Đọc số dư334 (`balance-before.png`); tải hai ảnh qua file chooser, chọn đúng START/END và xác nhận Thêm vào câu lệnh. UI preflight ghi Veo3.1 Lite, Khung hình, 9:16, 720p,8s,x3, giá30; Tác nhân tắt. Đã submit một bộ ba cùng prompt, không đổi model/route/ảnh. `preflight.png` lưu cấu hình và hai thumbnail; kết quả/gate/credit sẽ cập nhật sau thao tác thật.

Bộ đầu: một video và hai audio-failure. X2 thay đúng hai slot lỗi với cùng input cũng audio-failure, UI ghi không tính phí. Tổng5 yêu cầu, một video trên Flow, bốn lỗi; chưa đủ ba mẫu. Video R02 ID `d09ae2c8-510c-4f18-8217-af49464d5ab8`, title `Dao turning head`. Menu tải720p tạo toast nhưng chưa thấy file local; download event timeout; pageAssets bundle qua capability được hỗ trợ cũng failed-fetch (không dùng URL ẩn/shell). Đã mở tab mới cùng asset để thử native lại. Không ghi đã tải/decode/QC toàn clip và chưa ghép animatic v0.2.

Số dư actual cuối168324, trước334 => chi ròng10; ngân sách hợp nhất còn **124**. `balance-after.png` đã lưu actual panel; `results-final.png` và `playback-check.png` là bằng chứng UI, không thay file media. Đã khôi phục x3 sau x2 thay lỗi. File audio R01 được copy thành `closing_voice_R01_OWNER_REUSE_APPROVED.wav`; nguồn UNAPPROVED cũ giữ lịch sử. Script dựng được bổ sung tham số version/reaction/owner-voice status, chưa chạy render mới khi chưa có video local qua gate.

Owner tiếp tục chỉ vị trí toggle không âm thanh; xem169. Không tự kết luận nguyên nhân lỗi168 từ trạng thái toggle sau shortcut.

## Cập nhật nhận file và kiểm hình

Đường tải native trên tab mới đã nhận được `C:/Users/PC/Downloads/Dao_turning_head_20261003110658.mp4` (1.955.325 byte). Đã copy vào folder 168 dưới tên `R02.mp4`. File dài 8 giây, H.264, 720 × 1280, 24 fps, có audio AAC; giải mã không báo lỗi. Toast trên tab cũ không đủ chứng minh tải thành công; file thực tế trên tab mới mới là căn cứ. Không tạo lại video để xử lý tải.

Kiểm grid toàn clip mỗi 0,5 giây (`R02-grid.png`): Đào quay thêm về phải, có cử chỉ tay khoảng 1–2 giây, rồi mới nhìn trái; mở miệng ở nhiều khung sau 4 giây. Má Khoai ở tiền cảnh dịch/chuyển kích thước. **REWORK**, chưa đạt phản ứng một nhịp với môi khép và tay ổn định. Không đưa vào bản ráp mới hoặc nâng Quality. Chưa nghe audio, không suy mở miệng thành chắc chắn có lời nói.
