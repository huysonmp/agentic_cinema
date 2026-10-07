# C02 T02 — Review bản xuất cắt trên Flow độc lập, REC245

Run **C02-T02-FLOW-EXPORT-CRITIC-245**, ngày 07/10/2026. **Disposition: EXPORT_SAMPLE_VISUAL_PASS_FOR_OWNER_REVIEW / HOLD_ACTUAL_AUDIO_AV_AND_CHECKPOINT.** Chỉ chốt phạm vi bản xuất được kiểm; không khóa final EDL, không duyệt giọng/lip-sync hoặc toàn phim.

## Target và bằng chứng

Actual owner file: `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/07_edits/C02_T02_FLOW_0_7p5S_FOR_APPROVAL.mp4`. SHA256 tính lại bằng PowerShell khớp **`d151eb1d9f5f5b4486fed030579d9da3de0d23f434a65db2f6c4dca88b3228f3`**. Parent ghi thao tác Flow UI range 0→7,5 giây, scene `13856f3b-e94b-4ec7-a20f-4761275add18`; reviewer không thao tác/chứng thực UI lại.

Đọc full owner `06_qc/C02_T02_FLOW_245/native_evidence.json` và repo registry245 trước viết report. Nguồn đối chiếu: actual reference medium244 và native T02 hash `2f20ec53…`, đã xem/kiểm hash trong run native245. Prompt245/canon và audioapproval244 giữ nguyên; không edit input hoặc media.

Cold xem actual export overview 1fps (7 samples zero frames 0,24,…144), **toàn bộ ba boards 6fps** (45 samples frames 0,4,…176), full-resolution `00001.png` / frame0 / 0s, `00180.png` / frame179 / 7,458333s, `00181.png` / frame180 / 7,500000s. Tổng **47 unique frame samples**, không xem toàn181 frames, không continuous playback/actual hearing. Technical probe/decode là evidence của root được đọc đầy đủ, không phải reviewer tự chạy lại.

## Findings

| Tiêu chí | Expected → observed | Mức / kết luận trong phạm vi |
| --- | --- | --- |
| Source/format | Bản cắt T02 720p → hash target khớp; evidence H264 720×1280 / 24fps / 181 frames, audio AAC 48k stereo; decode success. | TECHNICAL_EVIDENCE_MET, không chứng minh nghệ thuật/giọng. Không coi filename “7p5S” là duration đã đo. |
| Geometry/frame/set | Giữ native T02 và medium244 → samples giữ hai mặt Khoai trái/Đào phải, torso/tay/bát, phố sâu/đèn lồng/mái bạt phải; không crop thành cận món hoặc quay lại toàn thân/chân/nền tường T01. | SAMPLED_MET. Không phát hiện crop/stretch hoặc set regression trong mẫu. Sai biệt nhỏ cỡ khung từ native T02 vẫn giữ, không pixel-identical reference. |
| F0/props/light | Tay nghỉ riêng, bát trống/đũa bàn; nem nguội/rau/chấm/cốc → mẫu giữ geography và vật dụng, không gắp hoặc visible steam. Mặt/miệng đủ sáng. | SAMPLED_MET; không chứng nhận flicker/chuyển động ở frame chưa xem. |
| Tail Đào | Loại đoạn hé/O của native → export fullframe179/180 đều môi Đào khép, Khoai khép môi/cười nhẹ; boards không thấy O tail. Native lần trước frame182 / 7,583333s mới hé, nên đoạn lỗi đã quan sát nằm ngoài duration export. | **Finding C245-LISTENER-TAIL được loại khỏi selected export range trong phạm vi đã kiểm.** Không suy “Đào không nói bằng âm thanh” từ still. Không cần sinh T03 chỉ để sửa đoạn đã bỏ. |
| Timing inclusive-end | Đề xuất trước [0,7,5s), frames0–179 → actual Flow export có thêm frame180 tại7,5s; video/container **7,541667s**, audio **7,509333s**. | MINOR_TIMING_DISCLOSURE: selection thực là181 frames, không180. Frame thêm sạch; không blocker riêng, nhưng phải ghi measured duration vào assembly. Video/audio duration lệch khoảng32,334ms không tự đồng nghĩa audible gap hoặc lip-sync lỗi. |
| Audio retention | Giữ tiếng native T02, không tái sinh/đổi giọng → parent báo decoded PCM overlap correlation **0,9999900917377019**. Ở lúc reviewer tìm, chưa thấy record local T02 lưu metric này; native_evidence có probe audio, không correlation. | ROOT_REPORTED_RETENTION_METRIC, reviewer không tính lại/nghe. Root nên lưu metric/method/source hashes đúng T02. Correlation cao hỗ trợ cùng signal ở overlap, không certify K20, lời, accent hoặc sync. Không dùng số correlation T01 khác ở record243 để thay. |

## Giới hạn và gate còn mở

ASR native T02 đã đọc trong run trước: segment 0,96–6,94s; silence detector -40dB từ6,968604s. Export dài hơn mốc này nên **bằng chứng offline hỗ trợ** giữ đủ lời và handle; vẫn cần nghe bản xuất thực để xác nhận âm cuối “chờ”, nhịp, phát âm “rang gạo”, cùng K20 xuyên suốt và không giọng ngoài. Không coi ASR là actual hearing hoặc dùng chữ nhận sai để sửa thoại.

Owner voice/audioapproval244 chỉ chốt native **T01 hash5ba2878f…**, không T02 hoặc export này. Kiểm hình mẫu và bảo toàn signal không chuyển approval. Chưa có sync PASS hoặc owner checkpoint đối với exact export hash d151eb1d… tại thời điểm reviewer làm report.

Đã xác định: actual export tồn tại/hash đúng; sampled set/frame/F0 giữ; cuối sạch và tail O quan sát được không còn; inclusive endpoint làm duration7,541667s. Quyết định reviewer: đủ để trình owner xem/nghe bản cắt, không mở full gate mặc định. Giả định có handle theo ASR/silence, chưa thay actual nghe. Còn mở: voice/lời/AV, transition và timeline30s, exact export approval. Bước tiếp: root gửi **đúng file/hash này**, đóng audio/AV và checkpoint, rồi kiểm joins/cảnh phụ thuộc theo243; dùng duration đo thay UI label. Không UI/API/Git/credit/generation hoặc authority retry phát sinh từ report.
