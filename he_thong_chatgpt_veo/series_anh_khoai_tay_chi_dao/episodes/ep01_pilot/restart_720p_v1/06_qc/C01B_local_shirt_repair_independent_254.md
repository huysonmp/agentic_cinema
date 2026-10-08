# REC254 — Review độc lập bản sửa áo đã mã hóa

Kết luận: **GO_FOR_OWNER_AV_CHECK**. Bản local đủ để trình owner xem/nghe; chưa chọn nguồn/range BM, chưa nghiệm thu tiếng hoặc mở BR.
Đã đọc đầy đủ approval254, `scripts/repair_ep01_shirt_region_254.py`, manifest compositor_v2, encoded evidence và comparison; trực tiếp xem đủ 12 board `all_frames_01.jpg`–`12.jpg` chứa cả 96 frame output F0–F95, đối chiếu source cạnh repair, thêm PNG encoded F23/F36/F57.
Review là kiểm toàn frame trên board và ba PNG, không phải phát/xem/nghe AV liên tục. Không sửa media, UI/network/generation/credit/Git.

- Output `07_edits/C01B_BM_T02_LOCAL_SHIRT_REPAIR_T01_FOR_REVIEW.mp4` đã rehash khớp manifest/evidence: `cd4213d393798ca3baf45603a9c40215b7f08ffcf7091418238e183abb76b198`.
- Approval254 cho sửa riêng vùng áo local, giữ tiếng nguồn; không cho thay mặt/miệng/tay/voice, crop/freeze toàn cảnh hoặc paid generation. Script thực hiện patch x260–462/y830–917 trên F23–F57, lấy áo sạch F22/F58, đăng ký dịch chuyển, trộn hai anchor và feather8px; không tái tạo lời/mặt.
- Manifest ghi pre-encode ngoài patch và 61 frame khác nguyên vẹn. Sau libx264/yuv420p, pixel ngoài patch không bảo đảm bit-exact; không dùng assertion trước encode để gọi toàn video sau encode pixel-identical.
- Trong cả 96 output frame đã xem, không còn chữ “Khoan” tại vùng áo; nguồn cạnh đó vẫn có chữ F23–F57. PNG F23/F36/F57 xác nhận vùng phục hồi sạch chữ ở độ phân giải720×1280.
- Đường áo và hàng nút vẫn đọc được; không thấy nút nhân đôi/đứt đường áo hoặc mảng chữ còn sót rõ. Vùng giữa đoạn hơi mềm, có chuyển sắc nhẹ ở mép dưới patch (ví dụ F36); không thấy lỗi tĩnh đủ buộc HOLD, nhưng chưa loại rung/nhấp nháy texture khi phát liên tục.
- Hai biên F22→F23 và F57→F58 không thấy pop lớn trên chuỗi ảnh. Registration dịch đến khoảng6px ngang/24px dọc trong manifest; translation/blend không khôi phục chính xác vải bị chữ che, chất lượng mép/nút khi chuyển động vẫn cần owner xem.
- So sánh source/repair từng cặp không thấy thay đổi rõ mặt/mắt/khẩu hình, tay, bát/đũa/chén/món, camera hoặc nền ngoài mục tiêu sửa. Vẫn solo Khoai nhìn phải, tay nghỉ; không thấy crop, cut hoặc freeze toàn cảnh mới.
- Comparison map F0–F95 cùng index/timestamp nguồn; chuỗi miệng mở rồi khép giữ cùng thời điểm trong board. Không thấy action bị dịch, lặp hoặc cắt; không tự chứng nhận tiếng–môi sync từ hình.
- Evidence encoded ghi 720×1280/24fps/96frame, video4s/audio4,01s và full decode thành công; đây là bằng chứng kỹ thuật, không approval chất lượng.
- Script/manifest ghi189 audio packet hashes+timing bằng nguồn; comparison ghi decoded stereo48kHz PCM bằng tuyệt đối, cùng SHA256 `4c4bbe1c14ad2f6184c6b64bd310c9187245929e323dc64685fdff5484686c0c`. Bằng chứng này xác nhận giữ audio gốc, không chứng minh đúng K20/sắc thái/đúng lời hoặc sync đạt; reviewer chưa thực nghe.

Giới hạn còn mở: owner cần phát bản encoded để xét áo rung/nhấp nháy/đường nút, nghe nguyên “Khoan” và giọng/sắc thái, xem sync thực. T02 nguồn chưa được nghe/duyệt nên bit-exact audio không chuyển thành approval.
Đào/contact ngoài khung UNKNOWN; cut A→BM→BR→C02 chưa kiểm. Không chọn BM range/EDL, không toàn-film PASS, BR vẫn HOLD và chưa có authority chi. REC254 local submit0/credit0 theo hồ sơ; reserve đóng.
Root đọc full report rồi trình đúng artifact/hash này tại cổng owner AV; nếu owner thấy jitter/voice/sync lỗi, giữ HOLD và ghi cụ thể, không tự mở generation hoặc che bằng crop/freeze/ghép tiếng lên môi khép.
