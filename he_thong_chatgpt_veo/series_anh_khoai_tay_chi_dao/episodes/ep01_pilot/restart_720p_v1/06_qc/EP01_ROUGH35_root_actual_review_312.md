# REC312 — Kiểm bản dựng thô thực tế của root

Ngày 14/10/2026. **Đủ gửi bản dựng thô để owner xem tổng thể; chưa nghiệm thu toàn phim hoặc bản cuối.** Không đồng nhất lấy mẫu hình, ASR hay tương quan PCM với đã nghe/xem liên tục.

## Đối tượng và kỹ thuật đã xác minh

- Exact export `07_edits/EP01_ROUGH35_TRIAL_v1_NOT_FINAL_312.mp4`, SHA256 `44bd2c591a00f085b8d4c4e4e69c5a25fb9d4f4357e7dbc76263ca068fec1e66`; bản owner khớp hash. 9.916.019 byte, H264720×1280/24fps/840khung, video và audio35,000s. Full decode sạch, đã trích đủ840PNG.
- EDL trial ghi nguồn/hash/range/sample offsets, không thay EDL đã duyệt hoặc ghi đè nguồn. C02 [16,173), C04 [12,124), C09 [8,88) là **range thử mới**, chưa được duyệt chỉ vì từng clip nguồn đã được duyệt. Block308 giữ đủ120khung và điểm cắt nội bộ48; qua tái encode không còn file byte-identical nên approval cũ không tự chuyển thành whole-export acceptance.
- Không tăng tốc, đổi pitch/gain, tạo giọng mới, crop hoặc che mặt. C04/C08/C09 dùng silence ở bản QC không thoại; chưa phải thiết kế ambience/mix cuối. Không có phụ đề, nhãn món/địa phương hay hiển thị AI được hoàn thiện trong bản này.

## Hình đã thực kiểm và giới hạn

Root đã xem ba overview (35 mẫu1fps); đủ11 seam16 boards, mỗi bảng bao16khung quanh các cut81/99/149/306/348/398/510/576/624/696/760; đủ17 ending16 boards bao F576–839, ô đen cuối chỉ là padding bảng; đủ7 C04 trial16 boards bao F398–509. Không nhận đã xem toàn840khung riêng lẻ hoặc continuous playback. All-frame nguồn đã có review trước, không thay kiểm bản export này.

| Hạng mục | Quan sát trên export | Trạng thái |
| --- | --- | --- |
| Người nói hiện mặt | Các vùng thoại/mẫu tổng thể thấy mặt Đào hoặc Khoai đúng nhịp hình; “Khoan” dùng cận Khoai. Không thay bằng toàn cận món | Hình tại vùng đã kiểm không thấy mất mặt; nhịp/giọng thực cần owner nghe–xem |
| C02 mới → câu hỏi Đào | Các seam149/306 giữ cảnh/mặt, không thấy props reset lớn; cut dùng offset hình và tiếng cùng nguồn | Chưa chứng nhận âm đầu/cuối “Mùi…/chờ”, chỉ kỹ thuật và ASR |
| C04 bắt gặp | Đào nhìn đi/uống; Khoai lấy A; Đào nhìn lại F500+ trước cut510. Caught hold ngắn hơn bản cũ | Cần xem tốc độ thật để đánh giá punchline, chưa acceptance269 cho cut mới |
| C05 → C06 | F575→576 ở24s đổi hình/chất miếng nem đang kẹp và chất nem đĩa chung, mặt/ánh nhìn cũng có sai biệt tái dựng | **OPEN — không đạt production continuity**, approval block308 không miễn điểm nối này |
| C06 → C07 → C08 | A giữ trên đũa, Đào nâng bát riêng, rồi A đi vào bát và tips rút trống. Khẩu hình người không nói nhìn khép ở vùng đã kiểm | Core causality có bằng chứng hình; tiếp xúc khuất/continuous motion chưa chứng nhận |
| C08 → C09 | EntryC09 bỏ8khung nhưng vẫn empty tips/A trong bát, rồi Đào hạ/đặt cốc và hai tay đỡ bát như ngoại lệ312; Khoai lấy B mới từ đĩa về phía mình | Dùng được cho rough theo ngoại lệ; không gọi đúng FINAL cũ |
| Kết | B còn trên đũa, A trong bát Đào. Hai mắt mở nhìn nhau ở F832–839 chỉ8khung/~0,333s | Rủi ro kết hụt; chưa chốt ending-readability hoặc final30 |

## Kiểm nguồn âm bằng đo máy, không phải nghe

Root tự giải mã output và nguồn về float32 PCM48kHz stereo bằng FFmpeg rồi so các đoạn nội bộ (chừa4096sampleframes mỗi biên). Đủ1.680.000sampleframes/35s. Six source-synchronous segments có tương quan zero-lag:

| Đoạn | Tương quan | Offset sample khớp frame |
| --- | --- | --- |
| C01A/BM/BR |0,999992897|Có |
| C02 |0,999947534|Có |
| C03A |0,999745378|Có |
| C03B |0,999957020|Có |
| C05 |0,999990989|Có |
| Block C06/C07 |0,999982471|Có |

Đây là bằng chứng tiếng tương ứng nguồn, không voice identity, phát âm, cảm xúc hoặc lip-sync PASS. AAC tái encode không bit-exact; mẫu biên bị loại khỏi phép correlation nên phải nghe biên trên bản thực.

ASR unprompted/offline nhận đủ nhóm N01–N07, nhưng nhận “rang” thành “găng”, “gắp” thành “gấp”. Không sửa kịch bản/caption theo chữ ASR. Câu subscribe ở estimate33,58–34,98s là output nhận dạng không có âm tương ứng: root đo PCM vùng29,25–35s, 0 sample khác0, maxabs0. Không có cơ sở báo voice lạ ở cuối; không cần đổi giọng hoặc chạy Flow để sửa hallucination ASR. Hồ sơ ASR giữ nguyên làm bằng chứng lỗi máy, không chỉnh transcript lịch sử.

## Review độc lập — chưa đóng

Hai nhiệm vụ kiểm exact rough đã được giao; reviewer EDIT gửi thông báo kiểm hash/count/audio correlation/seam, nhưng dừng do giới hạn dùng trước khi có report riêng đã lưu. Reviewer visual chưa có report riêng. Kiểm hiện tại thấy cả hai `EP01_ROUGH35_*_actual_independent_312.md` không tồn tại. **Không ghi hoàn tất/PASS hoặc gán phép đo root cho agent.** Không đổi model/tạo agent mới để vượt giới hạn. Các report C09 actual311 và timing follow-up311 có thật, root đã đọc; đó không phải report fullrough312.

## Gate còn mở và đề xuất tiếp

1. Owner xem/nghe đúng rough35 để đánh giá nhịp, đối thoại, động tác cho–nhận và kết; chỉ creative feedback hoặc rough acceptance có phạm vi, không release.
2. Hoàn tất kiểm độc lập exact export khi khả dụng; không cần tốn credit Flow cho việc này.
3. Xử lý food seam24s bằng phương án có bằng chứng; không tự phủ approval hình lên nem lệch.
4. Sau phản hồi rough mới chốt timing cuối. Bản35 là quyền xem thô264, không phải đổi target30. Không đủ bằng chứng cắt thêm5s an toàn hiện tại.
5. Hoàn thiện nhận diện món/địa phương, nội dung hiển thị AI, phụ đề/mix và kiểm bản xuất cuối sau khi hình/nhịp khóa; không chèn claim mới chưa source hoặc coi file nháp là publish-ready.

Flow chi0 cho vòng dựng này; dự án279/500, còn221, dự phòng110 đóng. Không có release hoặc auto retry.
