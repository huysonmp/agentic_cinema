# REC229 — Chuẩn bị R01 có thoại và phản ứng

Owner đã duyệt thay **hình** quanh “Khoan”; giữ nguyên tiếng Khoai và phần hình kể ký ức sau đoạn mở. Không đổi kịch bản, K20/D06, B làm anchor; không mở batch test tay hoặc Quality.

## Nguồn và điểm nối làm việc

Đã chạy ASR local offline trên exact B, không API/cài mới. ASR định vị “Khoan” 0–0,34s, từ tiếp theo khoảng1,10s. FFmpeg đo khoảng dưới ngưỡng im lặng0,364292–1,209979s. ASR đọc nhầm “rang” thành “gian”; lưu nguyên transcript diagnostic, **không sửa lời đã duyệt theo ASR**. Chưa nghe trực tiếp hoặc kiểm AV mới; hai phép đo chỉ hỗ trợ chọn boundary.

Chọn điểm hình **tạm** B frame24/1,000s. Guide chứa N01 PCM [0;103200) và B PCM [0;48000), rate48kHz/stereo, tổng3,150s; WAV khớp samples nguồn. Guide video4s/96frames/360×640 có0,85s đệm. N01 picture từ A03 chỉ là nguồn timing; thiếu bàn và không phải chuẩn hình. Cut guide và hình tay nghỉ chưa phải chuyển động được nghiệm thu. Bố cục S/M/E sẽ là yêu cầu sửa.

Manifest/media local: `C:/Users/PC/Downloads/du_an_nem_bui/229_r01_production_input/`. Script `scripts/prepare_ep01_rec229_opening_source.py` giữ nguyên originals và từ chối ghi đè thư mục output.

Master sau này phải đặt **toàn B PCM liên tục đúng một lần** tại đầu N02. Chỉ thay picture prefix nếu khẩu hình/cue/hành động/nối của output sản xuất đạt. Boundary1s là candidate, không khóa trước QC. Không cắt tiếng B, chồng tiếng lên hình im rồi gọi lip-sync đạt hoặc đưa old N02 của A03/WAV202 vào master.

## Trạng thái tuyến Flow

Đã chọn Ingredients → Omni1.1 Flash →360p/4s/x1 trên project hiện hành. Chưa xác minh quote với video được nhận: thao tác upload guide hiện dừng ở hộp xác nhận quyền sử dụng video. Đã hỏi owner xác nhận tại thời điểm hành động; chưa bấm “Tôi đồng ý”, chưa submit generation/chi credit. Không ghi giá trước khi UI nhận video và đủ refs/prompt.

## Kiểm sau sản xuất, không mở test riêng

Đã thực chạy maker và critic local độc lập, root đọc toàn reports. Prompt đã bổ sung bỏ mouth motion sai của guide, E chỉ pose tay nghỉ, reach bắt đầu trong vế thoại thay vì âm cuối, tay return/settle trước3s để có biên nghỉ trước candidate join3,15s, không dùng0,85s pad trong master và không xóa native watermark. Đây là sửa brief, không motion/sync PASS.

1. Native output/hash/decode/frame-range; giữ nguồn B nguyên.
2. Người nói–giọng–lời–miệng: N01 Đào, “Khoan” Khoai; listener không nói thay. Cần nghe/AV thực cho scope đó, ASR không thay hearing.
3. Thứ tự reach→nghe cue→stop→return; path quanh bát không xuyên vật, gap trước tiếp xúc, không teleport/reset qua cut.
4. S/M/E, B anchor, trục/mặt/đèn/bàn/món nguội/F0; hai bát rỗng, không giấu mặt để vá lỗi.
5. Nối picture mới sang B ở range thực; tiếng B nguyên và không lặp. Không thừa hưởng whole-native acceptance222 cho join mới.

Đã xác định nguồn, phép đo và guide. Đã chốt phạm vi coverage và production-only. Giả định làm việc: route edit video có thể sửa R01 với refs và giữ tiếng; chưa chứng minh output sẽ đạt. Còn mở: xác nhận hộp quyền sử dụng, route nhận đủ ingredients, quote live, preflight độc lập và chi riêng. Bước tiếp: xử lý đúng các gate này, rồi một output sản xuất và QC, không batch thử.
