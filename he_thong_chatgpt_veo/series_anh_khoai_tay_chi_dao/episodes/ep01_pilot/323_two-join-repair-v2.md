# REC323 — Sửa hai điểm nối trên bản REC322

Ngày 17-10-2026. Owner nhận xét “giây 15-16 chuyển cảnh chưa ổn, giây 20-21 cũng thế; sửa nốt bản cuối này đi là ổn rồi đó”. Đã sửa đúng hai vùng trên bản322, không mở lại kịch bản, giọng, thiết kế nhân vật hoặc sản xuất footage. Phản hồi được ghi là yêu cầu sửa có phạm vi, không tự biến thành duyệt bản mới hoặc cho phép phát hành.

![EP01 — bản sửa hai điểm nối v2](C:/Users/PC/Downloads/du_an_nem_bui/323_EP01_TWO_JOIN_REPAIR/EP01_TWO_JOIN_REPAIR_v2_323_FOR_REVIEW.mp4)

## Thay đổi cụ thể

| Vùng phản hồi | Cut thực trên322 | Vùng hình được xử lý, 0-based/half-open ở24fps |
| --- | --- | --- |
| Quanh15–16s | C03B→C04 tạiF385 /16,0417s | F381–388, range[381,389),15,875–16,2083s; neo đầuF381, neo cuốiF388 |
| Quanh20–21s | C04→C05 tạiF517 /21,5417s | F513–519, range[513,520),21,375–21,6667s; neo đầuF513, neo cuốiF519 |

Nguyên nhân trực tiếp quan sát được: cùng cỡ/góc bàn nhưng mặt và hướng nhìn đổi đột ngột qua một khung cắt. Không kết luận chỉ do sai thời điểm, cũng không tái tạo cả cảnh để sửa hai chuyển trạng thái nhỏ.

Dùng **nội suy chuyển động bù chuyển động của FFmpeg đã cài** để tạo vài khung trung gian giữa hai neo thực trong mỗi vùng. Không hòa mờ chồng hai mặt, không freeze/loop, không sinh AI qua API/Flow, không tạo tiếng. Đây là xử lý hình có tạo khung dẫn xuất, không được gọi là toàn bộ frame native nguyên bản hoặc pixel-lock. Giữ nguyên833khung và tất cả mốc thoại; đoạn J2 kết thúc trước khung gốcF520 được giữ lại, không cắt đầu câu Đào.

Toàn bộ audio lấy nguyên AAC từ bản322 bằng stream-copy. Không revoice, mix, gain, pitch hoặc retime. Ngoài hai vùng, không thay lựa chọn cảnh hoặc range; video được encode lại nên không tuyên bố pixel ngoài vùng giống tuyệt đối.

## Kiểm thực tế và giới hạn

- File mới: H.264720×1280/24fps,833khung/34,708333s; AAC48kHz stereo. Full decode exit0. SHA256 `d7f380e05bdcafb3eb2768ce0cc4d011c6ee7570a4ec24788ce0cdf4305e2845`.
- Đối chiếu **1.628 gói audio**: PTS, DTS, duration, size và SHA256 payload khớp tuyệt đối322. Không cần chạy ASR lại để giả lập nghiệm thu tiếng; tuyến âm giữ nguyên, không là chứng nhận giọng/diễn mới.
- Xem đủ15 khung dẫn xuất,23 ô quanh hai điểm nối trên file encode, thêm F384/F516 ở kích thước đầy đủ. Không thấy mắt nhân đôi hoặc bàn tay mới rõ ở vùng đã xem; đường nét nội suy có thể mềm cục bộ. Đây không phải xem chuyển động liên tục hoặc owner acceptance.
- Trong ROI cố định bao mặt/thân trên, mức chênh ảnh liền khung cực đại giảm12,39→3,70 và13,21→4,00/255. Chỉ số hỗ trợ xác nhận cú nhảy đã được trải ra nhiều khung, **không chứng minh chuyển động đẹp hoặc không có artefact**.
- 14 khung đối chứng ngoài vùng được đo PSNR RGB; mức thấp nhất 43,46dB so322. Đó là kiểm tái encode, không chứng minh mọi pixel hoặc mọi khung ngoài vùng đồng nhất.
- Bản322 còn nguyên, hash `68d595328bfd858b998583ee56584e20643393c6f3497b3aeb4c47c02afa57b0`; không ghi đè file dựng/EDL cũ.

## Giới hạn phạm vi

Chỉ sửa hai điểm owner nêu. Không tự sửa/thay món tại23,792s, ép thời lượng30s, thêm phụ đề/mix/AI label hoặc gọi đây là finaltechnical/releasePASS. Những mục còn mở ở322 không bị xóa khỏi hồ sơ; cũng không đưa thành một vòng câu hỏi mới trong lượt sửa này. Chủ yếu để owner xem một bản sửa tổng thể, không xin duyệt từng khung hoặc từng thao tác.

## Lưu trữ

- Video: `restart_720p_v1/07_edits/EP01_TWO_JOIN_REPAIR_v2_323_FOR_REVIEW.mp4`.
- Nguồn, neo, lệnh, hash, ảnh trước/sau và kiểm: `restart_720p_v1/06_qc/TWO_JOIN_REPAIR_323/`.
- Script: `scripts/repair_ep01_two_joins_323.py`, dùng lại utilities đã có trong script322; không cài công cụ mới.
- Bàn giao: `C:/Users/PC/Downloads/du_an_nem_bui/323_EP01_TWO_JOIN_REPAIR`.
- **Flow0 credit**; sổ dự án giữ291/500 đã chi, còn209, dự phòng110 đóng. Không refresh số dư tài khoản hoặc upload/generate trên Flow.
