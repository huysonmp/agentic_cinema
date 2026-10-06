# EP01 — Duyệt bản nối tiếng và chuyển sang sản xuất hình

Ngày 2026-10-06. Owner trả lời **“ok r đấy”** sau khi được trình bản nghe bảy lượt và hỏi về người nói/chỗ nối. [Approval](evidence/203/owner-approval.json) gắn đúng file/hash của bản 202.

## Quyết định đã chốt

Nguồn tiếng hiện hành là `EP01_7_LUOT_N02_MOI_REVIEW_NOT_FINAL.wav`, SHA256 `3c83b7d6188f5b973b0ef5c77ebc1fc16afde7c11827764c5302145741b736d4`. Owner chấp nhận người nói và chỗ nối của cả bản. N02 mới tiếp tục giữ nguyên toàn nguồn đã duyệt 201; không đưa N02 cũ trở lại hoặc tuyển giọng lại.

Điểm nghe của owner trước sản xuất hình theo 197/198 đã được giải quyết. Đây là **nghiệm thu người dùng trên bản nghe cụ thể**, không giả thành một lượt chạy SIA độc lập đã so file reference. Formal SIA với local reference chưa có report; AV_ASSEMBLY/FINAL_AV vẫn phải kiểm bản hình–tiếng thật. Không tự gắn PASS toàn phim hoặc master.

Giữ hình thức A đã duyệt: lời của nhân vật ngoài hình có chủ ý ở cận món/tay; không ghép tiếng lên mặt nhân vật đang khép môi rồi gọi là offscreen. Giữ C-v0.6, K20/D06, quán nhỏ bình dân gọn gàng, nem nguội không hơi nóng, rau thơm/đồ chấm thuộc cùng bàn và một miếng nem chưa ăn xuyên hành động chuyển vào bát Đào.

## Cập nhật timing làm việc, không ép tiếng vào slot cũ

[Timeline 203-v0.2](evidence/203/timeline-v0.2.json) thay timing làm việc 197-v0.1 vì N02 mới dài hơn. Giữ toàn PCM của bản nghe, không tăng tốc hoặc thêm thoại. Đoạn N01–N04 đặt từ 0 đến 14,055 giây. Chèn nhịp quay về cốc → gắp → nâng → nhìn lại; toàn tiếng R01 của N05–N07 bắt đầu ở 21,9583 và kết thúc ở 29,9583 giây. Biên hình nằm trên lưới 24 fps, đích vẫn 30 giây.

Không sinh thêm một đơn vị U02 chỉ để bù độ dài: dự kiến U01 cung cấp đoạn mở 4,1667 giây và một đoạn giữ bàn **khác, tiếp sau trong cùng take**, dài 1,9167 giây; U02 cung cấp tám giây cận món ở giữa. Không lặp đoạn, đóng băng, tua chậm hoặc dùng ảnh tĩnh để giả video đã đạt. Nhận diện món được tích hợp vào cảnh mở có N01, không cần giữ hai giây intro riêng không thoại.

U07 cần nhả nem trong 1,5417 giây sử dụng; U08 còn 1,5 giây cho kết. Đây là yêu cầu cần kiểm ở chuyển động thực, không bảo đảm Veo sẽ đạt. N07 ước tính kết lời ở 28,3233 giây theo ASR; hình hai mặt môi khép chỉ được xuất hiện sau khi tiếng thực kết thúc. Nếu coverage không đủ, điều chỉnh dựng có ghi phiên bản và kiểm lại bản hiện hành; không tự bỏ hành động hoặc cắt lời để giữ số 30.

## Thực thi tuần tự

Theo thứ tự đã duyệt 197/198, bắt đầu **U05: Đào nhìn lại một lần, môi khép**. Dùng nguyên START/END 195 đã duyệt 196 và prompt R2, không đưa D06/K20 hoặc thoại vào yêu cầu video. Root đã xem lại hai ảnh và kiểm hash; chúng đúng cặp nguồn, không tự chứng minh chuyển động đạt.

Nguồn START `c7e84f873fd19e7919d0f2d5d8c4877c345dde6a402f91330ea48e4ff894fcf3`; END `0e6a2f348ecd1cde923fa668d7b2163ad8b584f3be1e3a8cb7a91fa04b33e4de`. Hai PNG giữ nguyên kích thước 937×1678; không crop trước upload hoặc xóa watermark output.

Đã đọc skill computer-use và hướng dẫn thao tác/confirmation, dùng API trình duyệt được cung cấp; không thao tác login/cửa sổ native. Flow kiểm lại route Lite/Khung hình/9:16/720p/8 giây/x1, báo giá 10 credit. Phải đọc lại prompt, cặp nguồn và quote trước gửi; không lấy snapshot cũ thay kiểm lần này. Tải/giải mã và kiểm đường chuyển động ngay sau tạo, rồi mới xử lý cảnh phụ thuộc. Lịch sử thất bại 194 dùng cặp 185; lần này chỉ đổi sang cặp 195 đã duyệt, không tự mở bộ thử ba mẫu.

## Ngân sách và ranh giới

Trước thực thi: trần 422, đã chi 329, còn 93. Tám đơn vị đầu dự kiến 80 nếu giá thực vẫn 10/x1; còn 13 dự phòng, không phải 20 như trước sửa N02. Một lần sửa dự kiến 10 còn vừa trần; hai lần sửa 20 không còn vừa. Không suy số dư tài khoản thành quyền chi hoặc hứa 93 đủ hoàn tất.

Chưa Quality, API mới hoặc phát hành. Không báo các agent đã chạy độc lập nếu chỉ root kiểm; scope này dùng các contract kiểm hình và hồ sơ nghe owner hiện có.

## Tổng hợp

- Đã xác định: owner chấp nhận bản tiếng hiện hành đủ bảy lượt.
- Đã chốt: giữ giọng/lời, dùng bản 202 và tiến sang hình theo A/x1 đã duyệt.
- Giả định: U01 đủ đoạn sử dụng để bù timing kể; U07/U08 đạt nhịp ngắn, cần video thực kiểm chứng.
- Còn mở: chuyển động và điểm nối các cảnh; AV toàn tập, mix, phụ đề và bản xuất.
- Tiếp: thực thi U05, kiểm và lưu kết quả; sau đó U04 → U06/U07 và các cảnh còn lại theo readiness.

## Kết quả U05 thực tế

Đã gửi một lần/x1, Flow trừ 10 credit: số dư hiển thị 147 → 137. Sổ dự án: đã chi 339/trần 422, còn 83. Clip `66acfad3-a32a-4cae-9227-aa38e05def0d` hoàn tất. Một yêu cầu tải native không trả tín hiệu trong 20 giây, nhưng kiểm Downloads đã có file 2.104.195 byte; không gửi tải lại hoặc tái sinh. Hash bản gốc và bản lưu được đối soát; native H264 720×1280/24 fps/8 giây, 192 frame, **không có audio stream**; giải mã toàn bộ sạch.

Root kiểm 48 frame lấy mẫu xuyên tám giây, khung native đầu và đủ 36 khung cận môi trong 1,5 giây đầu. **REWORK**: môi vẫn mở/khép, tay không cầm cốc giơ lên diễn, hướng nhìn quay sang Khoai rồi trở lại cốc và lặp. Không chọn range hoặc tính thêm coverage đã đạt. Bằng chứng [kết quả](evidence/203/results.json), [toàn cảnh](evidence/203/U05_all8s_48frames.png), [môi từng frame đầu](evidence/203/U05_opening_mouth_all36.png). Không có reviewer độc lập được dispatch; không nhận kết quả root thành agent PASS.

Đổi cặp ảnh 185 → 195 mà giữ R2 chưa loại được lỗi. Không có audio không đồng nghĩa nhân vật không diễn miệng; nguyên nhân nội bộ của model chưa được chứng minh. Không mở thêm bộ thử nhiều hướng. Dùng tối đa một lượt sửa x1 giá kiểm trực tiếp trong dự phòng 13 còn lại: biểu đạt nhìn lại bằng cú cắt sang ánh nhìn đã hướng Khoai, chỉ cho blink/hold nhẹ. Giữ chuyện/lời và điểm nhìn; ghi thay đổi chỉ đạo/nguồn riêng ở lượt 204. Nếu sửa vẫn không đạt hoặc giá vượt forecast, dừng chi tiếp theo điều kiện 197/198.
