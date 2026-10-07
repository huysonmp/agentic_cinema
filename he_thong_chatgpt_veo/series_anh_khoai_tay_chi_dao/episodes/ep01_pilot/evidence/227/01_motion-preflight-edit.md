# REC227 — Review độc lập EDIT/ACT cho phép thử S→M

Ngày: 2026-10-07. Phạm vi: chuẩn bị phép thử chuyển động, xem ảnh nguồn và kiểm hash tại local. Không đọc báo cáo root/CONT của REC227 trước khi chốt review; không chạy Flow hoặc sinh media.

## Kết luận

**READY_TO_REQUEST_APPROVAL cho phép thử hình học S→M theo gói DRAFT hiện có. Chưa READY_TO_SUBMIT.** Brief có một hành động rõ: tay ngoài của Đào với đến vành đĩa phải, giảm tốc, dừng trước tiếp xúc và giữ. Hai mặt cùng nhìn thấy, hai miệng khép và F0 được giữ. Phép thử không thay câu chuyện đã duyệt, với điều kiện kết quả chỉ được dùng để đánh giá hình học và khả năng dừng; chưa được dùng làm bằng chứng R01 có thoại và phản ứng nghe “Khoan”.

Không thấy MAJOR trong thiết kế hành động của phép thử giới hạn này. Có các MINOR/UNKNOWN cần ghi rõ khi trình và khi kiểm đầu ra: nhịp 8 giây chưa phải nhịp dựng R01; cue nghỉ ở đầu rất ngắn; tay che mép bát ở END nên khoảng cách 3D chưa được chứng minh; prompt yêu cầu không thoại nhưng audio-off control chưa xác nhận.

**Gate quyền:** `owner-reference-approval.json` chỉ ghi owner chấp nhận tư thế tĩnh M_v03 và cho tiếp tục chuẩn bị/tách input. `paid_motion_request_approved: false`; chưa có approval cho exact batch 3 lượt, 10 credit/lượt, trần 30. Approval M tĩnh không phải motion pass, full G1 hoặc full AV.

## Nguồn đã đọc và ảnh đã xem

Đã đọc đầy đủ:

- `227/owner-reference-approval.json`.
- `227/motion-request-DRAFT.json`.
- `227/R01-SM-motion.prompt-DRAFT.txt`.
- `214_recovery-storyboard-r1-and-acceptance.md`.
- `223_g1-visual-source-map-and-reference-plan.md`, gồm nhiệm vụ R01 và vai trò S/M/E. Không mở các review khác được dẫn trong tài liệu này.

Đã xem toàn ảnh native bằng `view_image`, chế độ `original`:

- S: `C:/Users/PC/Downloads/du_an_nem_bui/224_g1_opening_refs_v01/REF01-S_v01_NATIVE.jpg`.
- M: `C:/Users/PC/Downloads/du_an_nem_bui/226_ref01_m_v03_from_s/REF01-M_v03_NATIVE.jpg`.

Đã tính lại hash native và separated download của S/M: **4/4 khớp request**. Hai Flow asset ID riêng được ghi trong request; hash xác minh byte của file local, không tự xác minh UI slot hiện hành bằng tên hoặc asset ID.

| Vai trò / exact ID | Asset / image ID theo request | SHA-256 xác minh |
| --- | --- | --- |
| START `REF01-S_v01_INPUT_REC227` | asset `c618f06b-fc7a-474c-be1d-9ed62ce87347`; image `46352b9d-1834-40fa-8133-076bfecc9a6d` | `eba9a13c86f359df458022a5a54664264e5bb29fcca08d6181454cb1ee482422` — native và `REF01-S_v01_INPUT_REC227_20261007104522.jpg` khớp |
| END `REF01-M_v03_ACCEPTED_REC227` | asset `d9e64ec1-dc0d-4c80-bcb6-b1e77ece951e`; image `83124e9c-4f6a-4c11-b9ce-697c4e3fcd6c` | `66defd18afc0845da8b34968446b98f547dcad951e6712e2e6a81ff2d5e2017c` — native và `REF01-S_v01_REC224_20261007104404.jpg` khớp |

Prompt được đọc trong lượt này có SHA-256 `af94764252de0a2a057490eec874059d9804b1caa92e7bfa01d552c054cfafc5`. Request chưa chứa expected prompt hash; đây là hash nhận diện bản đã review, không ghi là kiểm khớp một giá trị khóa có sẵn.

## Phản biện expected / observed và mức độ

| Vấn đề | Expected / phạm vi đúng | Observed trong gói chuẩn bị | Kết luận |
| --- | --- | --- | --- |
| Câu chuyện và F0 | R01 cho thấy ý định lấy đĩa; món chưa chuyển vị trí trước N02 | S có tay nghỉ; M có tay ngoài với tới vành phải, không cầm đồ. Prompt giữ món, đĩa, bát và các tay khác | READY trong phạm vi kiểm hình học; không thấy đổi đường câu chuyện |
| Nguyên nhân dừng | R01 hoàn chỉnh: Đào nói N01, Khoai nói “Khoan.”, Đào nghe và dừng đúng lượt | Phép thử giữ cả hai miệng khép, không thoại; dừng theo chỉ dẫn thời gian của prompt, không có cue “Khoan” | Chưa test causal stop. Không được gọi R01 đạt diễn xuất hoặc thoại |
| Đường tay | Tay ngoài đi xuống/hơi vào trong, quanh phía ngoài bát, không xuyên bát/đũa/ly | S/M dùng đúng tay. Prompt nêu đường quanh bát và các vật cần tránh. END che một phần mép trước-phải bát; không thấy nhập hình rõ trong ảnh | MINOR/UNKNOWN về khoảng cách 3D. Chính phép thử cần giải quyết bằng media liên tục; không suy occlusion thành collision |
| “Visible separation” quanh bát | Khoảng cách vật lý và biên tay/bát phải đọc được, không xuyên/nhập hình | Prompt yêu cầu tay đi phía trước mép ngoài bát với separation; END có chồng hình chiếu tay/bát bình thường | Không yêu cầu luôn có dải nền giữa tay và bát nếu tay đi phía trước. Phải phân biệt occlusion hợp lý với tay nhập/xuyên gốm hoặc bát biến dạng |
| Đích/gap | Ngón tay bên vành phải, thấp hơn đỉnh món, dừng trước chạm | END có gap nhìn thấy và vị trí bên phải món; prompt yêu cầu giữ gap | READY về cue tĩnh; motion chưa được xác nhận. Phải kiểm không overshoot rồi quay lại END |
| Cue đầu | Đầu shot nhận ra đúng S trước một lần với tay | START rõ; prompt yêu cầu bắt đầu tay nghỉ nhưng chuyển trong khoảng hai giây đầu, không quy định lead-in dài | MINOR cho khả năng dựng. Đủ để thử chuyển động, chưa đủ khẳng định có đoạn tay nghỉ đầu thuận tiện để cắt |
| Cue cuối | Một lần giảm tốc/dừng rồi giữ M; không retract/loop | Prompt yêu cầu đến END khoảng hai giây, giữ phần còn lại; no overshoot/retract/repeat | READY về brief. Start/end conditioning không chứng minh model sẽ đến M ở giây 2; cần kiểm media có dừng sớm và giữ thật, thay vì chỉ tới M ở frame cuối giây 8 |
| M→E và nối N02 | R01 hoàn chỉnh cần tay về trạng thái E để nối N02 B, theo kế hoạch223 | Request chỉ S→M và cấm retract, không chứa E | Đúng cho phép thử giới hạn; chưa đóng M→E/N02. Không dùng test này thay toàn bộ R01 |
| Gaze và miệng | Cùng hai mặt, Đào nhìn Khoai; miệng khép cho test hình học | S/M và prompt tương ứng; Khoai vẫn chú ý, hai tay nghỉ | READY cho test. Chưa kiểm chuyển gaze theo thoại hoặc khẩu hình N01/“Khoan” |
| 8 giây và dựng | Thời lượng sinh có thể khác duration dùng trong phim; target30s vẫn cần đo lời/acting/joins | UI theo request là8s. Prompt khoảng2s với tay + khoảng6s giữ. Chưa có timing audio R01 hoặc range dựng mới | MINOR về diễn giải. Sáu giây giữ phục vụ quan sát drift/gap; không mặc định đưa cả8s vào phim hoặc tự áp time-stretch |
| Âm thanh | Test không có thoại mới hoặc voice dùng cho delivery; khả năng im tiếng thực cần được xác nhận | `silent_prompt: true`, `audio_off_control_verified: false`, `native_audio_for_delivery: false`. Prompt cấm thoại/narration/singing/lip movement, chưa xác nhận track audio bằng công cụ | UNKNOWN. Không gọi “audio off” hoặc “video im tiếng chắc chắn”. Trình đúng trạng thái và kiểm native audio nếu sinh; không dùng tiếng phát sinh thay K20/D06 |
| Batch 3 lượt | Ba candidate độc lập cùng brief, x1/lượt, 10 credit/lượt, tối đa30; không retry tự phát | Request đề xuất3 lượt cùng prompt và cặp frame, `retry_authorized: false` | Có thể trình exact batch. Ba lượt so độ ổn định/biến thiên; không phải ba phần của R01 hoặc một experiment thay biến có kiểm soát |

## Nhịp kiểm và nhịp dựng

Nhịp prompt “reach khoảng hai giây, sau đó hold” hợp lý để cô lập một đường tay và quan sát dừng/độ ổn định. Đây là mục tiêu đề nghị, chưa là kết quả thực. Nếu model giữ chuyển động đến gần cuối tám giây hoặc mới tạo gap đúng ở frame cuối, test chưa chứng minh nhịp reach–stop đã yêu cầu.

Trong phim đã duyệt, “Khoan” phải do Khoai nói và có quan hệ với động tác dừng; Đào cần nói N01 với mặt/miệng phù hợp. Clip hai miệng khép chỉ cung cấp bằng chứng hình học. Không ghép audio N01/“Khoan” lên rồi nhận là causal/khẩu hình đạt. Không đổi lời, speaker hoặc biến câu thoại thành voice-over để giải quyết thiếu mouth states. Đoạn M→E và join với B vẫn là công việc riêng còn mở.

Tám giây là cấu hình sinh được ghi trong request, chưa phải duration sử dụng. Chưa đo waveform, điểm bắt đầu/kết thúc N01/“Khoan”, nhịp phản ứng và head/tail ở lượt này. Chỉ khi có media và timing mới chọn native range dùng được, giữ diễn tiến đúng và không cắt giữa từ “Khoan”. Không hứa toàn30s vừa hoặc mặc định lấy toàn8s.

## Điều kiện trình và kiểm sau approval

Có thể trình owner một gói cụ thể: **3 phép thử S→M cùng prompt/cặp input, Veo3.1 Lite, frames start/end,9:16,720p,8s,x1, live quote ghi10credit/lượt, trần30**. Gói phải nói rõ chưa thử thoại/causal nghe “Khoan”, M→E, motion pass hoặc AV; audio-off chưa xác nhận. Đây là quyền đang cần xin cho exact batch, không suy từ approval M tĩnh hoặc continuation preparation.

Trước submit sau khi có quyền, root phải kiểm lại đúng slot S/M, route/model, quote và balance thực; dừng theo các stop conditions trong request. Reviewer này chỉ đọc thông tin UI/quote từ hồ sơ chuẩn bị, không xác minh UI live. Giá10credit và số dư77 không được biến thành một cam kết billing hoặc delta đã đo.

Khi có output, kiểm **đúng native version/hash** và xem liên tục toànshot, rồi trích timecode/frame tại start, vùng qua bát/đũa, lần đến gap, thời điểm dừng và cuối hold. Tiêu chí là đúng tay, đường tay tự nhiên, không xuyên/nhập vật, gap được giữ, không food contact, không plate drift, tay khác nghỉ, hai mặt/miệng đúng, không loop/retract/camera move. Nếu vùng bị che không đủ bằng chứng: ghi UNKNOWN ở vùng đó, không đoán đã va/chạm hoặc đã clear. Âm thanh native phải được kiểm riêng nếu có; không coi prompt “no dialogue” là chứng nhận audio im tiếng.

## Tổng hợp vòng

Đã xác định: byte native/separated S và M khớp; owner đã chấp nhận static M với caveat bát; brief một lần reach–stop có thể dùng để thử hình học mà giữ F0. Quyết định reviewer: **READY_TO_REQUEST_APPROVAL trong phạm vi chuẩn bị; chưa submit**.

Giả định làm việc: ba lượt là ba candidate cùng phép thử, tám giây để kiểm đường tay/dừng/hold; chưa là ba shot hoặc đoạn phim tám giây đã chọn. Còn mở: exact batch approval trả phí, live preflight, audio-off control, motion3D/nhịp thực, thoại/causal nghe “Khoan”, M→E/N02 và timing30s. Bước tiếp theo: root tổng hợp preflight độc lập và trình gói cùng các giới hạn này; không chạy, chi, retry hoặc nhận chất lượng đạt trước approval và kiểm media thực.
