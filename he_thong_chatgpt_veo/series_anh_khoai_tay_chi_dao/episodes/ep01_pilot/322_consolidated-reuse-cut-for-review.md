# REC322 — Một bản dựng sửa tổng thể từ footage sẵn có

Ngày 16-10-2026. Owner yêu cầu “ok làm 1 lượt đi, hỏi gì mà nhiều vậy”. Đã làm một bản xem chung, không hỏi duyệt từng điểm cắt, không mở chuỗi tạo ảnh/video mới. **Đây là bản dựng thử đã xuất thật, không phải kế hoạch, nhưng chưa phải final30 hoặc bản đã duyệt phát hành.**

![EP01 — bản dựng sửa tổng thể REC322](C:/Users/PC/Downloads/du_an_nem_bui/322_EP01_REUSE_CUT/EP01_REUSE_CUT_v1_322_FOR_REVIEW.mp4)

## Những gì thay đổi

- Lấy câu chuyện và footage REC312 làm nền, không bỏ dự án để dựng lại từ đầu.
- Giữ nguyên mở đầu và cận “Khoan”. Thu gọn8F cuối đoạn Đào thu tay; không bỏ toàn bộ hành động phản ứng.
- Dùng đúng **cảnh cận ký ức đã có REC320**, selected [0,180), 7,5 giây, cả hình và tiếng đồng bộ từ cùng source. Không lồng tiếng cũ lên miệng mới. Exact C02 mới chưa được owner duyệt riêng; đưa vào bản xem chung theo yêu cầu làm một lượt, **không ghi thành đã được chấp nhận**. Giữ nguồn C02 cũ để đối chiếu/fallback.
- C03A bỏ8F đầu/4F cuối; C03B bỏ2F đầu/14F cuối; C05 bỏ12F cuối. Mục tiêu giảm chờ giữa lượt, không tăng tốc hoặc viết lại lời.
- Trả20F native cuối C04 để có thêm nhịp Đào nhìn lại. Không tuyên bố bước này làm mắt/mặt hoặc món tại cut tự khớp hoàn hảo.
- C06 bỏ6F đầu, C07 bỏ4F đầu; giữ nguyên đuôi C07 nối nâng bát sang thả. Sau xem ảnh preflight, quyết định **không** cắt8F cuối C07 như dự kiến đầu vì cần bảo toàn chuyển động bát. Bảng ảnh preflight cũ còn lưu để truy vết; EDL cuối và ảnh trích export mới là mốc thực tế.
- Giữ cảnh thảA vào bát. Trả8F native cuối C09, giữ pickupB và ánh nhìn cuối dài hơn, không freeze/loop.
- Không thêm dissolve, che lỗi bằng cận món, tăng tốc, đổi pitch, đổi giọng hoặc kéo approval của clip cũ sang toàn phim.

## Timeline của bản mới

| Khoảng thời gian | Nội dung / nguồn |
| --- | --- |
| 0–3,375s | Đào mở lời, nguồn312 [0,81) |
| 3,375–4,125s | Khoai “Khoan”, nguồn312 [81,99) |
| 4,125–5,875s | Đào thu tay, nguồn312 [99,141) |
| 5,875–13,375s | Cận Khoai kể ký ức, nguồn320 [0,180) |
| 13,375–14,625s | Đào hỏi, nguồn312 [314,344) |
| 14,625–16,042s | Khoai đáp, nguồn312 [350,384) |
| 16,042–21,542s | Tranh thủ gắpA, nativeC04 [12,144) |
| 21,542–23,792s | Đào bắt gặp, nguồn312 [510,564) |
| 23,792–25,542s | Khoai chữa cháy, nguồn312 [582,624) |
| 25,542–28,375s | Đào đưa bát và đáp, nguồn312 [628,696) |
| 28,375–31,042s | ThảA vào bát, nguồn312 [696,760) |
| 31,042–34,708s | Khoai lấyB mới và kết, nguồnC09 [8,96) |

Các range 0-based, half-open, 24fps. So bản312: C02 thêm23F, C04 thêm20F, kết thêm8F; tổng thêm51F. Các khoảng đầu/đuôi bỏ58F. Net giảm7F:840→833F, tức35→34,7083s. **Không dùng con số giảm thời gian để khẳng định phim đã nhanh/mượt hơn về cảm giác.**

## Kiểm trên chính file đã xuất

- H.264 720×1280, 24fps, **833F / 34,708333s**; AAC48kHz stereo, giải mã toàn file exit0. Độ dài PCM đọc được và sai số padding ghi trong verification JSON.
- SHA256 `68d595328bfd858b998583ee56584e20643393c6f3497b3aeb4c47c02afa57b0`. Tất cả bốn source hash còn nguyên sau dựng; bản312 và EDL312 không sửa.
- Đo zero-lag PCM cho các đoạn tiếng nguồn, bỏ biên4096 sampleframes để tránh AAC boundary: các đoạn có tiếng đạt ngưỡng tương quan >0,995. Đoạn BR nguồn vốn im lặng được kiểm bằng mức mẫu, không dùng correlation NaN để báo lỗi giọng. Đây là xác minh tuyến source/timing, không nhận diện người nói hoặc nghe giọng.
- ASR offline hiện nhận đủ chuỗi lời tới “Thế em quay lại đúng lúc rồi”; vẫn nhận “gắp” thành “gấp”. Không sửa script theo lỗi ASR. Câu subscribe máy sinh ở đuôi không có tiếng tương ứng: tái kiểm28,5s→hết,596.000 giá trị mẫu đều0; không tạo voice hoặc xóa tiếng tưởng tượng.
- Root xem overview35 mẫu, bốn khung quanh mỗi trong11cut và đủ16 khung kết; không thấy tệp sai thứ tự, mất mặt người nói ở các mẫu hoặc mất trạng tháiA→bát/B mới. Không gọi việc đó là xem chuyển động liên tục, nghe cảm xúc, đo lipsync hoặc báo cáo độc lập đã đạt.

## Lỗi còn mở — không che hoặc chuyển thành approval

1. **Cut23,792s** (đổi từ24s của bản cũ): nem trên đĩa/phần kẹp vẫn đổi cấu trúc/lượng khi vàoC06; mặt/tông hình cũng có redraw. Chỉnh nhịp không sửa được nội dung nguồn. Không tuyên bố đã chữa lỗi này.
2. Giữa các shot còn những khác biệt nhỏ về mặt/ánh mắt và độ rộng khung. Đã đổi cỡ cảnh có chọn lọc tại ký ức, nhưng chưa chứng nhận tất cả điểm nối mượt.
3. Đuôi mở mắt kết tăng8→16F, khoảng0,667s; không đủ căn cứ gọi đó là nhịp kết1,5s hoặc finalcreativePASS.
4. Bản34,708s **chưa đạt mục tiêu30s**, chưa mix âm nền cuối, phụ đề, nhãn món/địa phương hoặc thông tinAI. Không đặt tên FINAL hoặc publish-ready.
5. Ngoại lệ C09 đặt cốc/hai tay đỡ bát vẫn thuộc phạm vi dựng thử; C02 mới320 và những range sửa chưa có whole-export owner acceptance.

Không đưa lại các take C06/food-edit đã bị loại chỉ vì muốn giảm lỗi nem: bản286 có thay trang phục/hậu cảnh/timing, full275/293 có lỗi endpoint/thả. Trong lượt322 không có đối chiếu AV mới chứng minh một nguồn thay thế đạt, nên giữ phương án nền và công khai blocker thay vì chuyển lỗi sang vị trí khác.

## Tài liệu và chi phí

- EDL: `restart_720p_v1/07_edits/EP01_REUSE_CUT_edl_322.json`.
- Filter thực: `EP01_REUSE_CUT_filter_v2_322.txt`; command/verification/ảnh export tại `06_qc/REUSE_CUT_322/`.
- ASR: `06_qc/REUSE_CUT_ASR_322/`; chỉ bằng chứng máy, không approval tiếng mới.
- Script local: `scripts/build_ep01_reuse_cut_322.py`; FFmpeg, Pillow, NumPy và faster-whisper đã có, không cài hoặc gọiAPI.
- Một lệnh render đầu dùng option FFmpeg đã bỏ bị từ chối trước tạo media. Đã giữ command/filter lỗi, chuyển filter sang `-filter_complex`, có split/asplit rõ; một file video xuất thành công, không ghi đè. Bài học: kiểm khả năng binary đang cài, không dùng option cũ dù có trong ví dụ/lần chạy trước. Kiểm correlation đầu gặp BR silence/NaN; sửa phép kiểm dùng mức mẫu cho tín hiệu hằng, không giảm ngưỡng để ép đạt. Những lần chạy này đều local, Flow0.
- Lượt này **0 credit**, không upload, không paid request hoặc mở reserve. Sổ giữ291/500 đã chi, còn209 (tạo mới66, tạo lại0, coverage33, reserve110đóng); không đọc số dư Flow live.

### Trạng thái cuối vòng

Đã có một bản xem tổng thể thực để owner đánh giá chung, không yêu cầu duyệt từng thao tác. Giữ baseline/nguồn/approval lịch sử; không tự đóng lỗi món, final30 hoặc AV. Các bước tiếp còn là sửa nguồn tại cut23,792s khi có phương án đạt, chốt nhịp/độ dài, finishing và kiểm final; không phải làm lại cả dự án.
