# REC276 — Phản biện độc lập điểm nối C05→C06 đã encode

Ngày 12-10-2026. RUN_ID: REC276-C05-C06-ENCODED-SEAM-INDEPENDENT. Kết luận: **NO_OBVIOUS_MAJOR_IN_INSPECTED_SEAM_STILLS / JOIN_AUDIO_AV_HOLD**. Không gọi JOIN human PASS hoặc chứng nhận đã nghe/xem AV liên tục.

## Target và scope thực kiểm

Target: `C:/Users/PC/Downloads/du_an_nem_bui/276_C05_C06_JOIN/C05_C06_5p125S_JOIN_QC_NOT_FINAL.mp4`. SHA-256 tự tính lại: **`42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`**, khớp evidence và manifest.

Đã đọc đầy đủ `00_decisions/C06-prefix57-and-cut-on-motion-approval-276.json`. Owner đã duyệt đúng derivative prefix57 hash `58f13ea424300e0cde09000d37cf42839ac7b8ba7c6d2d6f64c02eeb9022594d`: tiếng K20/trọn N06, diễn hơi ngượng, sync/nhịp và boundary cut-on-motion. Approval cá nhân này **không duyệt encoded join mới**; full nativeT03 vẫn bị bác vì thả sớm. C07 mở chuẩn bị có dependency seam/preflight, không tự production PASS.

Đã đọc đầy đủ `encoded_qc/native_evidence.json` và `encoded_qc/action_all/manifest.json`. Trực tiếp xem board07–11, đủ **F48–87 quanh cut**, cùng PNG nguyên khung F65/F66/F122 (tên file=F+1). Xem đối chiếu exact native C05F65 qua ref `C06_START_from_C05_T02_selected_F65_269.png` và ref mới `C07_START_from_C06_T03_selected_F56_276.png`. Không nhận đã xem đủ123 encoded frames trong lượt seam này. Không đọc maker276.

Scope: **DENSE_SEAM_STILLS_PLUS_EXIT_NOT_CONTINUOUS_AV**. Không nghe, không ASR; không browser/generation/new script/render/git hoặc media edit. Evidence kỹ thuật đã đọc: H264720×1280,24 fps,123 frames/video5,125 giây; AAC48 kHz stereo5,125 giây, decode thành công. Không tự chạy lại probe/decode.

Ref C07 mới đã tự tính SHA-256: `69fb0e62a3a6f138a0eae622603945b248ec8d2809c8cda513dcdfdc33d00863`. So khớp hình với exit là kiểm bằng mắt, không tự gọi nó pixel-identical từ derivative encode.

## Mapping điểm nối

- C05 native range [0,66): encodedF0–65, thời lượng2,75 giây.
- C06 native range [0,57): encodedF66–122, thời lượng2,375 giây.
- Cut tại encoded **F66 / 2,75 giây**. F65 /2,708333 giây là frame cuối C05; F66 là nativeC06F0. EncodedF122 /5,083333 giây là nativeC06F56, giữ tới hết video5,125 giây.

## Findings thực tế

| Scope | Quan sát quanh F65→F66 | Kết luận |
|---|---|---|
| Tay / SAME A / own pair | Hai phía cut đều có cùng miếng A đang kẹp tại tip đôi đũa riêng trong tay ngoài trái Khoai, dưới ngực trên phía bàn của anh. Tay trong vẫn nghỉ; chưa đưa A sang bát ở cut. | Không thấy jump lớn về tay, đổi pair, nhân miếng, ăn hoặc thả tại seam. Không chứng nhận vật lý liên tục từ ảnh tĩnh. |
| Miệng / vai nói | F56–65 C05 đã về môi khép. C06 vàoF66–74 cũng môi khép, rồi Khoai mở khẩu hình khoảng encodedF75 trở đi. Đào vẫn khép môi ởF66–87 đã xem. | Vai nói/nghe trên ảnh nối đúng hướng N05→N06. Không suy ra không overlap tiếng, đủ âm cuối N05 hoặc onset N06/sync khi chưa nghe. |
| Cốc / hai bát | Cốc Đào vẫn nâng, đáy riêng khỏi bát; hai bát cá nhân rỗng ở đúng phía. F65→F66 không reset cốc xuống bàn hoặc vào bát. | Không thấy MAJOR continuity cốc/bát tại seam. |
| Mặt / mắt / diễn | Khoai giữ nét môi cụp và hướng mắt nhìn Đào qua cut; Đào giữ nét biết chuyện, mặt rõ. Có thay đổi rất nhỏ ở môi Đào giữa hai ảnh, không thấy head turn/discovery mới hoặc reset Khoai cười sẵn. | Không thấy morph/reset lớn tại seam. Diễn nguồnC06 prefix đã được owner duyệt đúng phạm vi; ảnh seam không thay human review nhịp thực. |
| Bố cục / ánh sáng / bàn | Framing hai người, camera cao độ, nền phố/đèn, áo, bàn, đĩa nem, rau trước trái/hai chấm giữ. Mức chi tiết/texture tái dựng có khác rất nhỏ nhưng không thấy jump ánh sáng lớn ởF65→F66. | Không thấy MAJOR hình rõ trong vùng kiểm. Không gọi seamless hoặc grading-final PASS. |
| ExitF122 / C07 dependency | EncodedF122 vẫn có A kẹp, tay đang đưa vềĐào, cốc nâng, bát nhận rỗng và khoảng hở tới vành. Đối chiếu refC07 mới có cùng trạng thái. | Cut-on-motion đúng boundary owner vừa chốt, không chuyển thành endhold của brief cũ. C07 phải tiếp tục/giảm tốc rồi giữ chờ, không reset thành A đã thả. Chưa có C06→C07 encoded seam để kiểm. |

## Tiếng và encoded target mới

Target này chứa **AAC encode mới** để nối hai range; không phải chỉ preview từng source đã duyệt. Source/prefix approvals giữ cho scope của chúng, nhưng không chứng nhận đường tiếng mới tạiF66. Evidence audio duration5,125 giây chỉ chứng minh độ dài stream, không chứng minh lời, K20/D06, không click/cắt âm cuối, nhịp hoặc sync.

Reviewer chưa nghe; cần owner hoặc capability nghe thực kiểm trên đúng joinhash: cuối N05, khoảng chuyển lượt, trọn N06, speaker/voice, môi và nhịp. Không tự gọi human JOIN PASS từ câu “duyệt nhé, làm tiếp đi” vốn trả lời prefix57/boundary trước khi join mới được xem.

## Disposition

Có thể trình join để kiểm tiếp, với trạng thái **không thấy MAJOR rõ trong ảnh seam đã xem** và **audio/AV join HOLD**. C07 chỉ mở chuẩn bị dưới dependency đã ghi276; chưa có bằng chứng bảo đảm nối chuyển động C06→C07 hoặc đủ timing C07–09. Không chạy C06T04, không sử dụng tail native bị bác, không thay voice/tool hoặc tăng ngân sách từ báo cáo này.
