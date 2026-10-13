# REC286 — Review độc lập actual native sửa món C05→C06

Ngày 13-10-2026. Reviewer `food_repair_critic_283`, bounded local REC217. **ALL_124_FRAMES_AT_BOARD_SCALE + CRITICAL_FULL_RESOLUTION_STILLS / NOT_CONTINUOUS_AV_OR_LISTENING.** Không browser/API, paid, git, cài mới hoặc sửa media. **Disposition: NOT_SELECTED — MAJOR_OFF_TARGET_WARDROBE_AND_SCENE_DRIFT.** Không tự retry.

## 1. Kết luận

Tuyến project composer **đã tạo được file native720p**, khác lượt scene editor284 không output. Món trên đĩa và A đọc gần vật liệu thính/thịt/bì hơn lát đặc cũ. Tuy nhiên repair không chỉ tác động món: **Đào bị thêm yếm/dây xanh ngay từ F0**, và đoạn sau có một thay đổi mạnh hậu cảnh/đèn/người đi đường tại F72. Đây là drift ngoài phạm vi đã duyệt, không thể chọn clip làm food-only repair hoặc chuyển approval nguồn sang take mới.

Không gửi owner để họ phải chấp nhận lỗi rõ này thay gate kỹ thuật. Có thể cho xem evidence/kết quả để minh họa thất bại phạm vi, nhưng không hỏi duyệt whole repair như candidate đạt. Giữ output để truy lỗi, source và approval tiếng/nhịp cũ nguyên scope. Không batch sửa các cảnh món khác bằng route này từ một lượt technical success.

## 2. Nguồn, hash và capability thực

Target mới: `C:/Users/PC/Downloads/du_an_nem_bui/286_FOOD_EDIT_PROJECT_PROMPT/EP01_720_C05_C06_FOOD_EDIT_T01_NATIVE_286.mp4`. SHA-256 trực tiếp kiểm `4703fb9b34abbb63144364cb388aa4d9921e06d7b7c597f2da77d04a7299e583`.

Source joined: `C:/Users/PC/Downloads/du_an_nem_bui/276_C05_C06_JOIN/C05_C06_5p125S_JOIN_QC_NOT_FINAL.mp4`. SHA-256 trực tiếp kiểm vẫn `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`.

Đọc đầy đủ approval286 và run286. Approval chỉ một request cap20, không voice/AV/source approval transfer, whole film hoặc retry. Run JSON lúc reviewer đọc còn snapshot `SUBMITTED_UI_PROCESSING_3_PERCENT_NOT_OUTPUT_PASS`/output pending/debit pending; **file downloaded và native evidence mới là bằng chứng output thực tại thời điểm review**, không dùng snapshot stale để nói chưa có file. Root cần cập nhật terminal và charge sau; reviewer không sửa registry.

Đọc `native_qc/native_evidence.json`: verified inspection do root chạy tool có sẵn báo full decode124F/24fps/720×1280/H.264; video5,166667s, AAC stereo48k audio5,184s. Reviewer này đọc evidence, không tự chạy decode. Source123F/24fps/video5,125s/audio5,125s theo evidence276. **Output thêm một khung** (+0,041667s video); audio thêm0,059s. Không tự gọi thêm khung là duplicate padding hoặc lỗi đồng bộ khi chưa kiểm audio.

Reviewer trực tiếp xem **tất cả124 frames** theo tám board `native_qc/full16_01.png`…`full16_08.png`, 16 consecutive/page; trang cuối có **12 khung thật F112–F123 và 4 ô black padding không thuộc video**. Đây là coverage toàn frames ở kích thước thumbnail, không tất cả frames full-resolution hoặc continuous playback. Xem riêng full-resolution output F0/F65/F66/F71/F72/F123; so source full-resolution F0/F65/F66/F72/F122. Hai ảnh thật Nem Bùi và approved START v1 đã trực tiếp xem trong run283 cùng reviewer; chúng là authority vật liệu, không authority thay trang phục/camera/scene.

Critical evidence folder: `C:/Users/PC/Downloads/du_an_nem_bui/286_FOOD_EDIT_PROJECT_PROMPT/native_qc/all_native_frames/`. Zero-based F tương ứng PNG F+1:

| Frame | File | SHA-256 kiểm trực tiếp |
| --- | --- | --- |
| F0 | `00001.png` | `3f65d51ae518449faf9277aa8b5eb1626a823280844eed9123895149309c545e` |
| F71 | `00072.png` | `462652ad9d0ac964ec6e6aadb8a477fb0828f0504ffa0c3b10e1135f0861d01a` |
| F72 | `00073.png` | `368cdbd9c1ab27f5b2b29a7c7d74cec2da1eeeb03c8debb81bd317b7aea90361` |
| F123 | `00124.png` | `d5e92b9d5d5e9030e58593af9d85d2ab373706b6bec17167bc4174d41288bb0e` |

## 3. Findings theo scope

| ID / mức | Expected | Observed và evidence | Disposition |
| --- | --- | --- | --- |
| F286-01 **MAJOR** wardrobe | Chỉ món đổi; Đào giữ blouse trắng/source outfit | Ngay F0 có mảng yếm xanh trước ngực và dây qua vai; tiếp tục ở toàn sequence. Source F0/F65/F66/F72/F122 vẫn blouse trắng, xanh ở phần váy dưới. Không phải lighting tint đơn thuần. | REWORK/NOT_SELECTED, không transfer canon/outfit approval. |
| F286-02 **MAJOR** scene/cut | Giữ source street/camera/light và cut66/2,75s | Output F71 còn mái hiên/cụm đèn nguồn; **F72/3,0s** chuyển sang đường thoáng hơn, nhiều đèn lồng lớn cao trước khung và người/background khác. Source cut F65→66 rất nhỏ trong cùng bố cục, sourceF72 vẫn hậu cảnh cũ. | Không bảo toàn sequence appearance/cut như request. Không chọn từ việc món đẹp hơn. |
| F286-03 timing **OPEN** | Giữ duration/timing nguồn123F | Actual124F và audio dài hơn. Output visible scene transition ởF72, khác source EDL66; không đủ xác định toàn alignment chỉ bằng hai cut. | Root đo/map nếu cần chẩn đoán; không trim/time-stretch để hợp thức hóa. |
| F286-04 FOOD **IMPROVED_BUT_NOT_FINAL_PASS** | Thịt/bì/thính, không slabs/mì/khói; plate và A đồng vật liệu | FullresF0/F72/F123 có thịt nâu hồng và dải phủ thính; A không còn lát chữ nhật đơn, có thịt và vài dải rủ. Plate đổi ở cả hai phần. Không thấy khói, đồ mới, pickup hoặc release qua124 thumbnail frames. | Đúng hướng vật liệu hơn nguồn; không bù MAJOR hoặc đóng FOOD toàn phim. |
| F286-05 A quantity/trajectory **LIMITED_VISUAL** | Một phần nhỏ trên tips, theo source không phình/nhân bản/thả | Một nhúm giữ liên tục và đũa tiến về bát Đào ở cuối; phần rủ dài hơn lát nguồn. Không thấy spontaneous multiplication/drop tại board scale, chưa chứng minh conservation/size pixel-exact. | Không claim lượng/motion tuyệt đối đạt; no new take needed chỉ để audit phần này khi clip đã rejected. |
| F286-06 faces/acting/tableware **PARTIAL_VISUAL_ONLY** | Giữ nhận dạng, diễn và người nói; bát/cốc/rau/chấm nguyên | Hai mặt vẫn đọc Khoai/Đào; Đào mouth activity phần đầu, Khoai phần sau; hai bát còn rỗng, cốc nâng tay ngoài, rau/chấm còn. Không thấy feeding. Mặt/mắt/diễn có redraw; chưa fullres/continuous comparison toàn phần. | Không identity/performance/sync PASS; source acceptance không truyền. |

Lưu ý cut: evidence khẳng định **có transition hậu cảnh mới tại outputF72**, không khẳng định mọi động tác/âm bị trễ đúng sáu khung. Original cut có thể bị smooth/replaced; phải mapping thực mới kết luận retiming chính xác. Clip dài thêm một khung không giải thích được MAJOR đổi outfit hoặc đổi toàn hậu cảnh.

## 4. Voice, audio và AV

`actual_listening = NOT_PERFORMED`, `continuous_AV = NOT_PERFORMED`, `lip_sync = NOT_CERTIFIED`. AAC48k/stereo hoặc mouth mở ở nhân vật phù hợp về thứ tự không chứng minh đúng câu, K20/D06, âm cuối, nhịp hay sync. Không dùng ASR/transcript/codec/PCM correlation để ghi heard_text hoặc voice PASS.

Owner duyệt source C05→C06 tiếng/nhịp/cut tại277; request286 không cho tự kế thừa. Native mới có audio duration khác, cần actual listening/AV nếu muốn đánh giá scope đó. **Chưa nói voice sai**, vì chưa nghe. Không cần dùng credit hoặc bắt owner nghe để chữa MAJOR visual đã rõ. Nếu giữ riêng audio làm resource ứng viên tương lai, phải kiểm/duyệt riêng trước dùng, không tự chọn vì file được sinh thành công.

## 5. Nguyên nhân và bài học đúng phạm vi

**Đã xác định:** project composer route sinh được file; kết quả sửa vật liệu món nhưng đồng thời redraw vùng ngoài món. Điều kiện invariant trong prompt không được bảo toàn đầy đủ. Source/refs không bị ghi đè.

**Chưa cô lập:** outfit/background drift do whole-image ingredient, video-to-video model behavior, source-cut handling hay câu nào cụ thể. START có tín hiệu người/pose ngoài món là rủi ro từng nêu; không đủ một take để khẳng định nó là nguyên nhân duy nhất của yếm hoặc hậu cảnh. Không tuyên bố đổi thành crop chắc chắn khắc phục, cũng không dùng success286 giải thích generic failure284.

Bài học vận hành: “video edit + preserve source” **không phải object mask/local patch**. Duyệt still vật liệu hoặc quote720 không chứng minh người/camera/cut giữ nguyên. Phải xem cả124F và vùng ngoài vật thể, không chỉ món hoặc poster. Route này chưa đủ cơ sở nhân rộng để sửa các đoạn món cũ.

## 6. Quyền, sổ và bước tiếp

Quote/approval cap20 là known; **debit thực đang chờ root đối soát** khi reviewer đọc registry. Không ghi actual spend20 hoặc final remaining263 trước snapshot/ledger. Nếu actual20 thì công thức cap/bucket theo285 giữ, reserve110 đóng; báo cáo này không cập nhật sổ hoặc mở request mới.

Đề nghị root:

1. Cập nhật terminal run bằng exact file/hash/metadata, charge thật khi kiểm được, report và MAJOR; giữ take NOT_SELECTED, không xóa source/job.
2. Trình owner kết quả ngắn với evidence outfit và scene drift; không xin họ miễn chuẩn cả clip. Không retry hoặc batch sửa tiếp dưới approval286.
3. Trước phương án khác, phân biệt bảo toàn source qua edit với tạo lại/asset-mask/crop. Mọi thay đổi công cụ/script/ref mới hoặc paid request cần scope/cap/checkpoint phù hợp; không dùng report này cấp quyền.
4. Giữ đoạn nguồn đã duyệt cho tiếng/diễn đúng scope nhưng food gate mở; repair286 không đóng cảnh nhận–bỏ hoặc whole film. Không chuyển gói mới vào timeline production/finishing.

**FINAL: NOT_SELECTED_FOR_FOOD_ONLY_REPAIR / MAJOR_VISUAL_DRIFT / AUDIO_AV_UNKNOWN / NO_RETRY_AUTHORIZED.**

## Delta closeout root — charge đã đối soát, không mở quality gate

Root báo đã reload và kiểm cùng account1.013→993, debit thực20; project spent237/500, remaining263 gồm retake26 và reserve110 vẫn đóng. Đây là **root-reported live charge verification**, reviewer này không truy cập browser. Nó thay trạng thái debit pending tại thời điểm phần6 được viết, không đổi visual disposition hoặc quyền retry.

Root cũng xác nhận ffprobe hiện hành source video/audio đều5,125s. ASR offline trả “Chờ em quay lưng nữa à” / “Anh gấp cho em mà” và decoded PCM hash khác source là technical/transcription evidence do root báo, **không actual heard text, voice-ID FAIL/PASS hoặc sync PASS**. ASR có thể nhận sai từ; hash PCM khác có thể liên quan encoding/length/âm thanh, không đủ chứng minh K20/D06 đổi. Các scope nghe/AV của reviewer vẫn NOT_PERFORMED.
