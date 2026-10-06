# EP01 — Chạy các cảnh còn lại theo duyệt 209

Ngày 2026-10-06. Owner trả lời “ok r nhé, tiếp tục đi nào” ngay sau gói 208 và hai quyết định cần chốt. Ghi nhận duyệt ba khung U01 v0.2, U02 v0.1, U08 v0.3 và phương án đề xuất đổi S03 từ mặt Đào sang tay chạm cốc trong phần tiếp của U01. Không mở lại U03 lỗi hoặc sửa giọng.

## Quyết định khóa

- Giữ C-v0.6, tiếng bản 202 đã duyệt và đích 30 giây/24 fps.
- Đổi nguồn S03: U03 → U01 phần tiếp. U03 gốc 208 vẫn REWORK, không được sử dụng.
- U01 cần 179 frame sạch (7,4583 giây) cho ba vùng riêng: 0–100; 100–146; 146–179. Đoạn thứ ba cần thấy tay Đào chạm cốc, không nhấc cốc.
- U02 cần 192 frame/8 giây sạch; U08 cần 36 frame/1,5 giây phù hợp sau trao nem. Việc owner duyệt ảnh không đồng nghĩa các chuyển động đã đạt.
- Còn 33 credit được cấp: mỗi cảnh một lượt Lite dự trù 10, tổng 30, dự phòng 3. Không đủ cho một lượt sửa 10 credit; dừng và báo nếu nguồn không đạt hoặc giá khác.

## Nguồn

Nguồn ảnh trong thư mục series `assets/references/208/`, dùng nguyên bản đã duyệt. Binding hash theo `evidence/208/results.json`. Không gắn bản REWORK/SUPERSEDED. Prompt thực trong `evidence/209/`.

## Kiểm sau tạo

Đối soát quote/debit; nhận native; hash/probe/decode; kiểm frame đầu, toàn clip và đúng range. Chỉ bind range quan sát được, không freeze/slowdown/lặp hoặc crop để che lỗi. Mọi lệch bàn, texture, bát, đũa, khẩu hình và thời điểm hành động phải ghi riêng. Full AV và owner nghiệm thu cuối vẫn chưa đạt ở thời điểm mở lượt.

## Kết quả thực thi

Đã tạo và tải đủ U01, U02, U08, mỗi cảnh một lượt Lite/x1/720p/8 giây/10 credit. Flow 87 → 77 → 67 → 57. Sổ dự án 419/422, còn 3 credit được phép chi; số dư tài khoản 57 không đồng nghĩa được phép chi 57. Không chạy sửa hoặc Quality.

- U01: ứng viên ba vùng riêng 0–100, 100–146, 146–179. Kéo đĩa sớm hơn chỉ dẫn; tay Đào kéo cốc vào trong, không chỉ chạm tại chỗ. Chưa owner duyệt chuyển động này.
- U02: ứng viên 0–192; kiểm lưới 4 mẫu/giây thấy món ổn định, máy tiến nhẹ, không thấy khói hoặc tay trong các mẫu kiểm. Không tuyên bố kiểm độc lập từng frame.
- U08: 0–36 không đạt nhịp gắp. Kiểm toàn bộ 36 frame 66–101 cho thấy nhịp gắp rồi nâng mới; chọn [66,102) cho bản xem có điều kiện. Bỏ phần đũa di chuyển từ bát Đào về đĩa bằng điểm cắt, không tăng tốc. Phần sau có cười hé môi, không dùng. Không báo toàn take đạt.

## Bản xem đầy đủ và giới hạn nghiệm thu

Bản `[EP01_30S_AV_REVIEW_NOT_FINAL.mp4](C:/Users/PC/Downloads/du_an_nem_bui/209_full_AV_review/EP01_30S_AV_REVIEW_NOT_FINAL.mp4)` đã render theo `evidence/209/timeline-v0.5.json`. Đủ 720 frame/24 fps/30 giây, decode exit 0. Từng nguồn được kiểm SHA-256 trước/sau. Toàn bộ PCM của WAV202 được đặt đúng hai vùng đã khóa, không bỏ mẫu hoặc đổi giọng/tốc độ/cao độ; AAC trong bản xem là mã hóa từ PCM đó, không phải âm thanh native Veo. Sáu bài kiểm assembler đạt, không thay cho nghiệm thu nghệ thuật.

Root đã xem contact 1fps và các frame cạnh điểm cắt; chưa nghe/xem toàn phim bằng một công cụ AV có chứng cứ, chưa có báo cáo SIA độc lập mới. Owner cần xem bản thật để đánh giá nhịp, tiếng và điểm cắt. Không tự chuyển thành approved hoặc master.

Các lệch cần xem rõ: cốc U01 kéo vào rồi ở U05 lại bên phải; rau của P02 nằm trên đĩa nem khác cảnh lân cận (P02 trước chỉ được duyệt nhịp); bát Đào đổi vị trí U06→U07; U07→U08 lược bỏ đoạn đưa đũa về đĩa. Đây là thiếu nhất quán hiện hữu, không được che bằng nhãn “technical PASS”.

## Bước kế tiếp

Owner chốt khả năng dùng bản ráp và các lệch trên, hoặc chỉ rõ điểm không thể chấp nhận. Nếu dùng được: làm phụ đề theo đúng WAV202, nhãn món/địa phương theo nguồn đã duyệt, thông báo AI, ambience/mix; kiểm xuất cuối rồi bàn giao MP4 và gói nguồn. Chưa phát hành, chưa thêm lời mới hoặc âm nhạc chưa rõ quyền. Nếu cần tạo lại, phải chốt quyền chi mới vì còn 3 credit không đủ lượt 10.
