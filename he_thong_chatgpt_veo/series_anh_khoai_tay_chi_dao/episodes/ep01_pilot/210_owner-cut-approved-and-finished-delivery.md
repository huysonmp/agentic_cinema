# EP01 — Owner duyệt bản ráp; xuất gói hoàn thiện v1.1

Owner trả lời “được rồi, ok rồi” sau bản AV209 và bốn ngoại lệ được trình rõ. Ghi nhận owner chấp nhận đúng MP4 hash `ef23dfd4eddf7b6e2379a5504c2aea751a32b8056b9f6e1f79e5221faabb58d7` và cho tiếp tục finishing local. Không suy ra phát hành công khai, generation hoặc Quality mới.

## Đã làm

- Giữ nguyên timeline209-v0.5, C-v0.6, bảy lượt thoại WAV202 và các ngoại lệ được owner chấp nhận. Hình decoded của bản clean đã kiểm khớp hình209.
- Xuất phụ đề mười cue/bảy lượt. N02 dùng timing ASR riêng nguồn201; N03/N04 chặn theo nguồn clip vì ASR cả bài có lệch sang vùng N02. Chữ/vai lấy từ package179, không đưa từ nhận dạng nhầm “gian” vào phụ đề “rang”. Timing vẫn là gợi ý ASR, chưa nghe kiểm độc lập/forced alignment.
- Thêm nguyên văn F01/F02/AI theo duyệt38 được giữ trong178/179; không claim mới, không đổi địa danh thành cấp hành chính hiện hành. Hồ sơ nguồn P2 được copy kèm erratum và approval.
- Chỉ giảm đều tiếng 3,22 dB: mức nguồn −12,78 LUFS/−0,34 dBTP; MP4 −15,98 LUFS/−3,67 dBTP. Không đổi tốc độ/cao độ/EQ/nén động hoặc tạo voice; không thêm nhạc/ambience/foley mới.
- MP4 có chữ và clean, SRT, WAV nguyên/gain, mười clip đã cắt, text cue, manifest, hướng dẫn Canva và nguồn nghiên cứu nằm trong folder owner `C:/Users/PC/Downloads/du_an_nem_bui/210_EP01_ban_giao_v1.1`.

## Kiểm chứng

`scripts/test_finish_ep01_approved_cut.py`: năm bài kiểm exact text/speaker/overlap/time đạt. `scripts/verify_ep01_finished_export.py`: hash đọc lại, hình clean trùng decoded209, toàn PCM sau gain khớp phép scale với sai số lượng tử tối đa0,502, mười ba text cue UTF-8/LF, asset hash và mapping bảy lượt đạt. 720 frame/24 fps/30 giây/720×1280, decode không lỗi.

Root xem contact 1fps và các khung1s/6,4s/12,4s của v1.1; chữ đọc được, không thấy mất dấu/cắt chữ trong các khung đã xem. Không đo hết layout bằng máy hoặc tuyên bố đã nghe/xem liên tục toàn phim. Owner đã duyệt AV trước finishing; chữ/mức tiếng/export cuối còn chờ xem. Không báo SIA/agent mới PASS.

Đã chạy hồi quy 54 bài kiểm EP01, tất cả đạt ở lớp thuật toán/fixture; không thay cho test nghe thực tế. ZIP bàn giao `210_EP01_ban_giao_v1.1.zip` có53 entry, đã mở đọc và hash MP4 có chữ trong ZIP khớp file local. Gói ZIP không phải authority phát hành.

## Kinh nghiệm local

Lượt đầu dừng do drawtext dùng `iw` thay vì `w`; giữ folder lỗi và tạo folder mới. Bản v1.0 xuất được nhưng chữ hai dòng cách quá rộng: file UTF-8 trên Windows dùng CRLF, drawtext tạo khoảng dòng không mong muốn. Sửa ghi LF rõ ràng, xuất v1.1 và kiểm lại. Không phải lỗi nguồn Veo, không tiêu credit. Audit dự kiến đo glyph cần PIL nhưng venv không có; bỏ claim đo tự động, không cài thêm thư viện chỉ để thay cho kiểm ảnh đã render.

## Trạng thái và bước tiếp

`FINISHED_EXPORT_READY_FOR_OWNER_TEXT_MIX_DELIVERY_REVIEW`; bản ráp/các ngoại lệ được chấp nhận, nhưng bản hoàn thiện chưa được owner nghiệm thu cuối. Chi lượt210=0; sổ419/422/còn3, số dư Flow57 là lần kiểm209, không kiểm mới. Không generation hoặc phát hành. Owner chỉ cần xem MP4 có chữ và nghe mức tiếng, chốt bàn giao hoặc nêu điểm sửa local; không mở thêm thử nghiệm nếu không có lỗi cụ thể.
