# REC232 — DIR/EDIT/CTD: chẩn đoán route R01 bị từ chối

Ngày 2026-10-07. Local-only. Đã đọc đầy đủ `production-request.json`, `execution-log.md`, `07_generation-rejected-no-charge-ax.txt` và prompt229; đối chiếu thêm snapshot số dư232. Không đọc critic độc lập; không browser/network/generation/chi/Git/sửa nguồn.

## Kết luận có bằng chứng

**OPERATIONAL FAILURE / NO OUTPUT / NO CHARGE.** Một lượt production x1 đã được owner duyệt10credit và gửi đúng route Omni1.1 Flash,360p,9:16, nguồn4s + S/M/E. UI tiến tới3% rồi từ chối với thông báo: “Không thể chỉnh sửa lời nói trong video này.” UI ghi chưa tính phí; snapshot tài khoản sau lỗi còn77. Đây là thông tin UI và đối soát số dư, không phải receipt billing. Không retry được thực hiện hoặc tự cấp quyền từ nút “Thử lại”.

Prompt rehash khớp request: `98ee8c606585da5e8e07bb66199f85a368c25d4b9b80d131d972e0363fde8b29`. Source đã được route nhận trước submit; lỗi này khác lỗi upload/intake trước đó. Không có output để chấm acting, sync, voice, đường tay hoặc join. Trạng thái `GENERATING_NOT_REVIEWED` trong request và các đoạn log “đang kiểm số dư” là snapshot trước lỗi; cần root bổ sung terminal status, không dùng làm trạng thái hiện hành.

## Root cause: chưa được chứng minh

Chứng minh được: hệ thống từ chối request tại khả năng/xử lý sửa lời nói. Không có mã backend hoặc giải thích chi tiết để kết luận prompt classifier, audio unsupported, hai speaker, nguồn cắt ghép, duration4s hoặc tái mã hóa Flow là nguyên nhân thật. Progress3% không xác định giai đoạn nội bộ.

Các instruction có thể bị hiểu thành speech edit, theo thứ tự ưu tiên kiểm:

| Instruction trong prompt | Vì sao đáng nghi | Giới hạn kết luận |
| --- | --- | --- |
| “Do not copy the source video's mouth motion”; “Generate mouth motion … speaker map” | Yêu cầu dựng lại khẩu hình và sửa attribution của nguồn, dù tiếng giữ nguyên | Nghi vấn mạnh nhất; chưa biết hệ thống phân loại qua cụm này hay qua toàn nhiệm vụ |
| “Her mouth follows … female speech”; “Show his speaking mouth … closed lips” | Điều khiển miệng theo từng người và lượt thoại | Là sửa performance nói về mặt hình ảnh; không tương đương chỉ thay bàn/nền |
| “only DAO speaks” tại0–2,15 và “only KHOAI says” tại2,15, kèm nguyên văn | Có thể được hiểu là tạo/thay đoạn nói hoặc lịch phát thoại | Người viết muốn bảo toàn nguồn, chưa chứng minh engine hiểu như vậy |
| “same two voices, exact words, pace, pauses … Do not synthesize new dialogue” | Nêu bảo toàn audio đúng mục tiêu, nhưng vẫn đưa nhiều điều kiện liên quan speech | Không thể chỉ từ lỗi này nhận rằng từ “preserve audio” bị cấm hoặc bỏ nó sẽ thành công |

Phần thay nhận diện/bộ bàn theo S, reach-stop-return theo M/E, máy khóa và F0 chủ yếu là visual repair. Tuy nhiên R01 cần sửa miệng nguồn sai và dựng cảnh mới theo audio; đây là yêu cầu thật của production. Đổi nhãn thành “visual-only” không xóa nhu cầu kỹ thuật đó.

## Quyết định tiếp theo có phạm vi

**Ưu tiên1 — làm một brief production visual repair ngắn hơn, chỉ khi capability đã kiểm hỗ trợ bảo toàn audio và sửa hình người nói.** Giữ nguyên video/audio source, S/M/E và nhiệm vụ mặt–tay. Đặt audio track là bất biến; diễn đạt thay hình diễn xuất theo nguồn thay vì “generate mouth motion”, không lặp nguyên văn lời hoặc ra lệnh ai “says” tại timestamp. Giữ speaker map/tiêu chí sync trong QC manifest, vẫn yêu cầu đúng miệng người nói và người nghe. Đây là giả thuyết request framing, không fix đã chứng minh; không được bỏ lỗi miệng nguồn khỏi brief/QC chỉ để route nhận. Một lần gửi nữa là request production mới cần scope/quote/approval; lượt lỗi không tự mở retry.

**Ưu tiên2 — kiểm read-only khả năng của route Flow hiện có trước request mới.** Cần xác định route cho phép thay speaking picture/khẩu hình mà giữ audio input hay chỉ sửa hình không liên quan speaking performance. Root có thể đọc UI/help đã có trong phạm vi được giao; maker này không truy cập mạng. Nếu có lựa chọn phù hợp trong hệ công cụ hiện dùng, chuẩn bị một output production x1 với nguồn/giá được kiểm; không đoán model khác, quote hoặc đề xuất test riêng. Nếu chỉ hỗ trợ visual repair giữ mouth motion nguồn, route ấy chưa đáp ứng guide hiện có vì source mouth attribution sai.

**Nếu cả hai chưa có cơ sở khả thi — HOLD route R01, trình blocker cụ thể.** Có tiếng nguồn và pose nhưng chưa chứng minh công cụ hiện dùng tạo đúng mặt nói + nghe-dừng-thu tay. Không giải quyết bằng che mặt, người nói ngoài hình mới, clip hai môi khép chồng tiếng, đổi giọng/lời, API/tool mới hoặc trả tiền cho test. Không âm thầm bỏ causal stop hoặc reset tay qua cut. Giữ B audio exact và memory picture sau prefix; boundary1s vẫn provisional, chưa hearing.

## Điều cần root ghi và kiểm

Ghi terminal result FAILED_SPEECH_EDIT_REJECTED, submit_count1, output_count0, UI-no-charge, balance77, retry_not_authorized. Sau đó cụ thể hóa một đường production khả thi trước khi trình lượt mới, gồm capability/ingredients/prompt/hash/quote và scope. Không hỏi lại script, K20/D06, anchorB hay quyền thay picture quanh “Khoan” đã chốt.

Nếu có output về sau, review đúng native/hash với actual audio/AV: N01 Đào, “Khoan” Khoai, listener mouth, reach→cue→stop→return trước usable join, F0 và nối originalB. Prompt ngắn được nhận hoặc audio waveform gần nguồn vẫn không thay QC này. Không self-quality PASS.
