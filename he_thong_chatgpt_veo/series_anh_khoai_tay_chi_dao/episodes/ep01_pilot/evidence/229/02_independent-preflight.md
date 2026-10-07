# REC229 — Independent CONT/DOP/ACT preflight R01

Ngày: 2026-10-07. Critic local-only, không đọc maker229 trước kết luận. Đã đọc đầy đủ `preparation-notes.md`, `source-manifest.json`, `R01-production-prompt-DRAFT.txt`; xem guide diagnostic, S v01, M v03, E v02 và B native frame24 bằng `view_image(detail="original")`.

**Disposition cập nhật sau đọc prompt đã sửa: READY_INPUT_PREFLIGHT / HOLD_UPLOAD_ROUTE_QUOTE / OUTPUT_AV_NOT_RUN.** Ý đồ production đã cụ thể và đúng phạm vi owner: chỉ thay hình mở quanh “Khoan”, giữ exact B audio và hình kể ký ức sau đoạn mở. Các sửa attribution/E hierarchy quan trọng đã được bổ sung; không cần một paid test mới. Chưa chứng minh route nhận đủ refs, giữ tiếng, output lip-sync/action hoặc nối thực. Đây không phải OUTPUT_PASS, motion PASS, voice PASS hoặc full AV PASS.

## Những gì đã xác minh

Đã rehash sáu tệp source/artifact trong manifest: A03, N01, B, B_PCM, exact PCM sidecar và guide; tất cả 6/6 khớp. Đã đọc WAV bằng Python `wave` ở chế độ chỉ đọc và đối chiếu dữ liệu PCM: N01 103200 sample frames + B prefix 48000 sample frames = 151200 frames, stereo/16-bit/48kHz, đúng 3,150 giây. Hai phần sidecar khớp từng sample với nguồn tương ứng. B_PCM toàn lượt có 480240 sample frames, tương đương 10,005 giây.

Đây là xác minh byte/sample, không phải thực nghe. N01 mang tên `UNVERIFIED` không tự là lỗi speaker đã xác nhận; cũng không được đổi thành hearing PASS từ hash. Metadata/ASR/silence của root vẫn chỉ evidence định vị. Critic không nghe audio, không playback AV, không browser/API/install/generation/spend/Git hoặc sửa source.

## Findings đầu vào và sửa cụ thể

| ID / mức độ | Quan sát hoặc giới hạn đã biết | Hệ quả / sửa trước sản xuất |
| --- | --- | --- |
| PF229-01 — MAJOR conditioning risk | Guide diagnostic phần đầu chỉ đĩa chung, thiếu rau/hai chén chấm/bát/đũa/ly ở vùng bàn lộ. Có Khoai mở miệng trong các panel thuộc phần nguồn N01 cũ; không có reach–stop–return được chứng minh. | Không lấy guide picture/mouth làm target. Prompt đã phủ nhận bàn/nền/cut cũ nhưng cần bổ sung rõ **ignore all source-video mouth animation and hand poses; derive new mouth motion only from the supplied audio and speaker schedule**. Nếu root có thể chuẩn bị guide hình sạch bằng refs đúng mà giữ timing/audio, đây là sửa local input, không paid test; không gọi chuyển ảnh tham khảo thành action đã đạt. |
| PF229-02 — MAJOR attribution/audio fidelity | Upload guide AAC lossy; sidecar PCM exact tách riêng. Lời “preserve supplied audio” trong prompt không chứng minh output Flow sẽ giữ đúng K20/D06, PCM hoặc timing. | Giữ exact PCM làm audio master; nhận native production rồi so thời gian, nghe giọng/lời và AV thực. Nếu tool sinh lại/retime tiếng, không tự cứu bằng đè PCM lên miệng sai. Có thể dùng exact source tiếng khi picture thực đồng bộ, không thay speaker bằng silent clip. Route/quote chưa xác minh sau nhận video/refs là điều kiện còn mở. |
| PF229-03 — MAJOR nếu khóa sai boundary | B frame24/1s được chọn từ ASR và silence, chưa actual hearing; prompt yêu cầu stop–return xong khoảng3,15s. | Đây là giả thuyết thời gian hợp lý để production, không cut cuối đã khóa. Đo/nghe output và B tại điểm nối; nếu return chưa xong, không đổi tiếng/speed để ép. Cập nhật boundary trong đúng vùng mở đã owner cho thay nếu có bằng chứng AV; không mở rộng thay hình ký ức. |
| PF229-04 — MAJOR nếu dùng padding trong master | Guide audio hữu ích3,15s, video4s có0,85s đệm. Audio N02 nguyên tiếp tục sau B1s; nó không có một khoảng im0,85s được thêm vào master. | Ghi explicit ở notes/request: **padding is for tool input only and will not be inserted into the master**. Nếu dùng hình4s trước B picture1s, hình B sẽ chậm0,85s so với audio nguyên. Không retime/cắt B để bù. |
| PF229-05 — P2 join risk | E có tay nghỉ, hai mắt nhìn nhau; Bf24 hai nhân vật mắt nửa khép/hướng xuống và khung rộng hơn S/E. Bố trí phục vụ tương thích về nội dung nhưng tỉ lệ/điểm nhìn không identical. | E chỉ reference **resting-hand geometry**, không bắt exact gaze/biểu cảm/framing ở điểm cuối. Bf24 hoặc frame nối thực là target đối chiếu cho gaze/head/table projection cuối. Giữ camera cố định trong production; cho phép một cut có lý do sang original B, nhưng không dùng dissolve/zoom/crop giấu jump. Không tuyên bố seamless từ hai still. |
| PF229-06 — P2 native mark conflict | S/M/E có dấu native dưới phải; prompt nói không visible logos/text nhưng không phân biệt dấu native với logo mới. | Thêm **preserve any existing/mandatory native watermark; add no new text or logos**. Không xóa watermark để làm đẹp input/output. |

Các finding trên là lỗi/rủi ro của đầu vào hoặc điều kiện kỹ thuật chưa xác minh, không phải lỗi của output chưa có. Maker/root có thể sửa prompt/notes/ingredient mapping ngay trong preparation scope; critic không yêu cầu batch ×3 hoặc phép thử có phí.

## Action và attribution cần giữ trong production

Prompt đã làm rõ N01 Đào0–2,150s, Khoai nghe; Khoai nói “Khoan” tại đầu B tương ứng2,150s trên guide; Đào nghe với môi khép. S là identity/outfit/table, M là giữa hành động và E là tay nghỉ, không phải ba scene. Đây là cấu trúc đúng để tránh silent hand-test thay scene thoại.

Đào bắt đầu vươn ở ý “để em”, bằng tay ngoài screen-right gần ly, quanh ngoài bát. Không rút trước cue nam. Sau cue phải có **nghe → dừng rõ → đưa cùng tay về nghỉ**, không giật/reset qua cut hoặc cùng lúc bất khả đọc. M có gap nhìn thấy với đĩa, không chạm món; tay che một phần bát ở hình chiếu vẫn là caveat cần kiểm toàn path. Không đòi gap nền giữa mọi pixel tay–bát, nhưng nhập ngón vào gốm, xuyên miệng/thành bát hoặc vật bị đẩy để mở đường là fail.

Khoảng từ cue tới boundary tạm1s của B cho phép khoảng1s để nghe–dừng–return. Chưa có thực motion/acting để chứng minh nhịp này đủ tự nhiên. Không cam kết “chỉ prompt là xong”; dùng chính candidate sản xuất để QC. Không biến Đào thành rút tay anticipatory hoặc diễn gấp để kịp marker. Không thêm kéo đĩa/gắp/ăn/uống, thoại mới hoặc romantic gesture.

Giữ F0 toàn đoạn: A chưa được Khoai gắp; hai bát rỗng; đũa nghỉ; cùng món nguội, rau trước trái, hai chén chấm, ly ngoài Đào. Mặt và miệng hai nhân vật cùng tay động luôn nhìn rõ. Khẩu hình người nói được phép mở theo speech; người nghe không mấp máy nói thay. Ảnh tham khảo môi khép không được dùng làm chỉ thị đóng môi speaker khi có thoại.

## Quy tắc nối hình/tiếng cụ thể

Tạm lấy `tB=1,000s` nhưng chỉ khóa sau thực nghe/AV. Master đặt N01 source0–2,150s rồi **toàn B_PCM liên tục đúng một lần** từ master2,150s. Không lặp “Khoan”, không lấy old N02 của A03/WAV202, không dùng tiếng native output mới thay B đã chọn vì nghe gần giống.

Picture production mới dùng tới master `2,150 + tB`; picture B cũ bắt đầu tại native `tB` và tiếp phần kể ký ức. Với candidate tB1s: picture mới0–3,15s → B picture từ frame24; đệm production3,15–4s không đưa vào master. Quy tắc này giữ đồng hồ B audio và B picture thẳng hàng. Không thêm0,85s tail hold vào câu chuyện, không cắt/speed B audio, không trim “Khoan” theo mốc camera3s.

Nếu hand return/gaze chỉ hợp tại marker khác, chọn frameB thực trong vùng mở được owner cho thay, cập nhật mapping và QC; không gọi tB1s là đã đạt do silence-detection. Original B later memory picture giữ nguyên nhiệm vụ và nội dung; approval222 đúng native B không tự nhận join mới PASS.

## QC candidate sản xuất — chỉ kiểm những điểm chống lặp lỗi

1. **Voice/word/speaker/miệng thực:** N01 Đào đúng lời/D06; Khoan Khoai đúng B/K20. Miệng khớp source thời gian, listener khép, không stale mouth A03. Cần người/công cụ thực nghe và AV; transcript không thay evidence này.
2. **Causal/path:** xem liên tục rồi từng frame quanh cue, stop, return; đúng tay ngoài, không contact món/đĩa hoặc xuyên bát/đũa/ly, không retract trước cue, đủ nhịp hiểu được.
3. **Preservation/F0:** camera khóa, đúng mặt/trục/outfit/nơ, đủ serving set và trạng thái rỗng/đũa nghỉ, không khói/chữ/props mới; native watermark đúng yêu cầu.
4. **Biên mới→B:** kiểm trước/sau cut cùng playback: tay đã nghỉ, mặt/gaze và bàn không jump gây đổi ý nghĩa; native B picture và exact B audio cùng clock; không pad hoặc duplicate Khoan. Ghi frame/range/hash thực thay vì marker dự kiến.

FAIL rõ phải sửa tại lớp gây lỗi; chưa có capability nghe/xem thì giữ UNKNOWN/HOLD scope đó. Không đè exact PCM lên silent mouth sai để tuyên bố AV đạt. Đạt R01/join cũng chưa là toàn phim30s hoặc full G1 PASS.

## Hash và closeout

- Manifest được review: `9e98d8f1d38eb149fca082ebaaa77b4b3ec0aa472fc4f89566c5588238beb203`.
- Prompt draft ban đầu được review: `44a4caba6a9c4d39a62555a45e4b7f1e01ab0d8257f9f6e92b44c3dcce1c27ff`.
- Prompt sửa đã đọc đầy đủ và rehash: `1085c89be58aee20340443a2a6ff42623ae0a085a81e29b9549c897515eed1ed`.
- Exact PCM sidecar: `594e815ec69ee0e10e5881bceb20470ec09e54fcda61704d80439a4c157adfb4`.
- Guide MP4: `1ecc6b496291179ce1f5e82153883e2df826b8cf3d7bfdd64edca2a78530b82f`.
- B native: `660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535`.

## Correction read-back trước handoff

Root gửi phản hồi đã áp warning; critic đọc lại đầy đủ đúng prompt sửa, không đọc maker report:

- PF229-01 input instruction: đã thêm “Do not copy the source video's mouth motion” cùng speaker map theo supplied audio. Sửa input đã đóng; guide cũ vẫn là rủi ro conditioning cần output QC, không tự trở thành clean visual evidence.
- PF229-05 E hierarchy: đã ghi E chỉ resting-hand pose, không khóa eye expression/camera scale. Sửa instruction đã đóng; framing/gaze join vẫn chưa PASS.
- PF229-04 master padding: root xác nhận mapping `picture prefix end=2.15+tB`, `B picture suffix start=tB`, whole B_PCM liên tục một lần và không dùng0,85s đệm. Report này ghi rule cụ thể ở trên; kiểm implementation/export vẫn chưa thực hiện.
- PF229-06 còn khuyến nghị P2 về ngoại lệ native watermark trong “no logos”; không dùng nó để yêu cầu batch test hoặc approval mới. Cần giữ nguyên dấu native khi chọn output và chuẩn bị finishing.

Preflight đầu vào corrected prompt sẵn sàng chuyển qua xác minh upload/route/quote. **HOLD_UPLOAD_ROUTE_QUOTE** còn thật: theo preparation-notes upload đang ở hộp quyền sử dụng chưa được xác nhận, chưa có quote khi video/refs đã được nhận, chưa xác minh route hỗ trợ đúng tập ingredients và nhiệm vụ sửa AV. Không bỏ qua các điều kiện này hoặc nhận authorization từ critic. Account77 không thêm credit; quote Omni thoại không được suy từ Lite10 ở227.

Byte/sample PCM đã xác minh; attribution/motion/voice/lip-sync/join thực là OUTPUT_AV_NOT_RUN. Sau khi điều kiện upload/route/quote được root giải quyết đúng authority hiện hành, đây là một production candidate rồi QC, không standalone test hoặc authority chi mới từ critic.

### Addendum — prompt cuối / watermark

Đã đọc đầy đủ và rehash prompt cuối: `755255a553e720efaa841c3c11435e0e4cae72d22f4306058081a155ec9124b3`. Delta cuối chỉ phân biệt **added** subtitles/text/logos với native provenance/watermarks bắt buộc phải giữ. PF229-06 đóng ở mức instruction preflight; không thay lời, speaker, timing, hành động, nguồn B hoặc scope sản xuất. Kết luận giữ nguyên: **READY_INPUT_PREFLIGHT / HOLD_UPLOAD_ROUTE_QUOTE / OUTPUT_AV_NOT_RUN**. Không review rộng hoặc chạy paid test mới; watermark thực trên output vẫn thuộc QC khi có candidate.

### Addendum — delta nhịp reach/return và padding

Đã đọc đầy đủ prompt cập nhật và rehash: `98ee8c606585da5e8e07bb66199f85a368c25d4b9b80d131d972e0363fde8b29` — đây là phiên bản hiện hành được critic read-back. Reach bắt đầu trong vế “Không hợp thì để em”, không đợi âm cuối hoặc snap vào M; sau cue “Khoan” mới dừng/rút cùng tay, hoàn tất và settle **trước3,000s**, để có nhịp nghỉ ngắn trước join dự kiến3,150s. Prompt nay ghi rõ0,85s đệm chỉ cho tool input, không vào master và không dùng để hoàn tất return.

Delta làm rõ thứ tự và giảm nguy cơ rút tay quá muộn ở điểm nối, không đổi lời/speaker/voice/nguồn B hoặc phạm vi production-only. Mốc hoàn tất là yêu cầu đầu ra cần QC, không phải evidence rằng khoảng0,85s sau cue đủ cho diễn tự nhiên. **Output acting/join/timing vẫn UNKNOWN; boundary B1s vẫn provisional.** Disposition giữ **READY_INPUT_PREFLIGHT / HOLD_UPLOAD_ROUTE_QUOTE / OUTPUT_AV_NOT_RUN**; chỉ kiểm lại đúng delta local, không review rộng hoặc mở paid test.
