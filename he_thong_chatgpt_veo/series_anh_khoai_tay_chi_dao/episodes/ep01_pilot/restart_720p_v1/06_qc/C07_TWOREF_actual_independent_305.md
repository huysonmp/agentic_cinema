# REC305 — Kiểm actual độc lập C07 RECEIVE TWOREF T01

**FULL_SOURCE_NOT_SELECTED / RANGE_NOT_CERTIFIED / AUDIO_AV_HOLD / C08_HOLD.** Tạo hình thực phẩm và phân công tay đã giữ tốt hơn lịch sử, nhưng Khoai có chuỗi mở miệng đầu cảnh và một bát thứ ba xuất hiện dần trên bàn ở đuôi. Không chọn toàn nguồn hoặc tự trim để biến các gate còn mở thành PASS.

## Phạm vi và target

- Chỉ local đọc/view/hash và viết report theo quyền reviewer REC217; không browser/API/chi/retry/Git, không sửa media/EDL hoặc nghe/phát AV.
- Native: `05_native/EP01_720_C07_RECEIVE_TWOREF_T01_NATIVE_305.mp4`; tự tính SHA-256 `12a0baa2d7ccedfaa16631b7cddd2c4331480e4fa8784880403eb425a8fb397b`, khớp evidence.
- Đọc đủ approval305, preparation304, run305 và native_evidence. FINAL304 đã đọc toàn văn ở preflight; hash kiểm lại vẫn `e07e76d6b798e59d4443bcad016655b9ab72e204e67dfc52a3c84631dde9e435`.
- Đã đọc actual T01/T02 REC277, root actual280, independent actual302 và regression303 trong review304 liền trước; giữ những kiểm hồi quy ấy, không tái audit toàn native cũ.
- Trực tiếp xem đủ sáu board `full16_01..06.png`, toàn F0–95 theo hàng không padding; xem thêm full PNG F0/F4/F5/F6/F13/F14/F24/F48/F76/F77/F78/F79/F80/F81/F84/F95 và đối chiếu F47 cùng portrait303.
- Quy ước F bắt đầu từ0; PNG=F+1, thời gian=F/24. Phạm vi **ALL_FRAME_STILLS_NOT_CONTINUOUS_AV**; toàn frame ở board và 16 khung full resolution, không kiểm vận động liên tục.
- Evidence đọc: H.264720×1280,24fps,96 frame/4s; AAC48kHz stereo4,032s, full decode success/source unchanged. Reviewer không chạy decoder lại.
- Preparation304 còn trạng thái chưa gửi; run305 lúc đọc còn native/debit pending. Đó là snapshot lịch sử chưa cập nhật, không phủ định native đã hash và xem ở đây.

## Expected → actual

| Mục | Quan sát độc lập | Disposition |
| --- | --- | --- |
| Identity / entry | F0 gần F47 về hai mặt, biểu cảm, tay, A, cốc và hai bát; Đào vẫn toàn đầu đào có cuống/lá, Khoai vẫn củ khoai tây suốt F0–95. Không thấy hóa người hoặc reset kiểu lịch sử277/280/302. | Không thấy MAJOR identity/entry trong ảnh; không chứng nhận exact pixels hoặc actual C06→C07 seam. |
| Khoai / vai nghe | F4 môi khép; F5 bắt đầu tách, F6–12 mở rõ, F13–14 còn chuyển về khép; F15 trở đi nhìn khép trên board. Chuỗi này trông như khẩu hình phát âm, trái yêu cầu Khoai chỉ nghe và không speaking mouth movements. | **MAJOR visual mouth attribution ở đầu**; không suy anh đã phát tiếng, nói N07 hoặc preset sai vì chưa nghe. |
| Bát đúng chủ / tay trong | Tay trong Đào chạm chính bát bên phải của cô khoảng F12–20; bát nâng khỏi bàn khoảng F24, sau đó tiến trái tới dưới A khoảng F48–64. Bát Khoai bên trái không bị cô chọn/kéo. Tay ngoài không tham gia nâng bát. | Có tiến trình nâng đúng bát trên hình; không lặp sai-owner277T01 hoặc hai-tay302. |
| Cốc / tay ngoài | Cốc còn nâng trong tay ngoài screen-right suốt nguồn, không uống/đặt xuống/đổi tay hoặc vào bát. | Không thấy MAJOR cốc; có dịch nhỏ theo diễn, không phải pose bất biến pixel. |
| Bát / count đuôi | F76 chưa thấy bát tại vị trí gốc Đào; F77 đã có hình oval mờ, F78–81 dần rõ, F84 và F95 là một bát riêng rõ trên bàn cạnh đũa, trong khi cô vẫn giữ bát đã nâng và bát Khoai còn nguyên. | **MAJOR duplicated prop: tổng ba bát cá nhân**, không phải bát cô đã đặt xuống. F77/3,2083s là mốc bắt đầu thấy trên full PNG đã kiểm; F76 là mốc sạch liền trước. |
| A / endpoint | Cùng nhóm nem vẫn trên tips đôi đũa Khoai qua toàn board, không thấy thả/ăn/gắp lại/đưa miệng hoặc về đĩa. Bát Đào tới vùng dưới A, lòng nhìn rỗng, giữ ở tay trong. | Đáp ứng một phần target hình; không xác nhận mọi ribbon cùng vật thể bất biến, lực kẹp hoặc physics từ ảnh. |
| Clearance / grip | Full F24 thấy bát được nâng trước khi tiến trái; F48 trở đi bát và tay đỡ che một phần tay nghỉ Khoai. Không thấy xuyên tay rõ, nhưng không đọc được mọi khoảng hở phía sau. | **CLEARANCE_NOT_CERTIFIED**, không gán collision chắc hoặc cấp physics PASS từ che khuất. |
| Đào / diễn / props | Đào có chuỗi mở/khép môi từ khoảng F12 đến F50, sau đó khép và cười nhẹ; hai mặt rõ. Đũa nghỉ phải, hai đồ chấm, rau, đĩa nem lạnh và watermark còn; không thấy caption/cut/zoom lớn/steam. | Chỉ kết quả hình, không xác nhận đủ N07, D06, nhịp hoặc lip-sync. |

## Range và âm thanh còn mở

- Toàn nguồn không đạt do khẩu hình Khoai đầu cảnh và bát nhân đôi đuôi. Không lấy F95 làm endpoint C08 hoặc chọn đủ4s.
- F15–76 là vùng có thể khảo sát kỹ thuật tiếp: không thấy hai blocker trên trong các ảnh, đã chứa phần nâng/đưa bát. Đây **không phải selected range** và không cấp approval.
- Đã đọc ASR305 khi hoàn tất: máy nhận nguyên N07 trong segment0,00–2,12s; từ “Thế” được máy gán0,00–0,84s. Cắt đầu tới F15/0,625s có nguy cơ bỏ đầu câu; timestamp máy không đủ chứng minh từ ấy còn nguyên hoặc đúng speaker.
- Giữ F0 để bảo toàn entry/lời thì vẫn giữ chuỗi miệng Khoai; cắt sau chuỗi đó phải kiểm actual tiếng/AV và seam C06→range, không được nói “chỉ trim là đạt”. Cắt đuôi trước F77 cũng chưa giải quyết blocker đầu hoặc clearance.
- Không có range đã chứng minh đồng thời trọn N07/D06/attribution, nhịp nhận, hai bát, clearance và nối đầu–cuối; **RANGE_HOLD**. Không bác khả năng kỹ thuật chỉ bằng ASR, cũng không nhận khả năng đó từ stills.
- `actual_listening=NOT_PERFORMED`, `lip_sync=NOT_CERTIFIED`; ASR không chứng nhận giọng nữ Bắc, D06, âm cuối, không tiếng nam, trọn lời thực hay lip-sync. Không chuyển approval tiếng cảnh/take khác.

## Hồi quy, quyền và bước tiếp

- So lịch sử: 305 không hóa người/mất bát ngay entry như277T02/302, không cho ăn/cốc hạ như280; lỗi miệng Khoai tiếp tục và lỗi count mới ở đuôi. Hai ảnh + wording cùng đổi, không kết luận portrait là nguyên nhân độc lập sửa identity.
- Root báo debit1022→1015/7; project265/500, remaining235, first80/retake0/post45/reserve110 CLOSED. Reviewer không đối soát account live; run snapshot cần root cập nhật terminal receipt.
- Giữ source/evidence làm nguồn chưa chọn; C08 HOLD cho tới source/range hợp lệ được kiểm thực. Không ghép/crop che bát, không tự sửa giọng/EDL, chuyển bucket hoặc chạy tiếp.
- Nếu root tiếp tục khảo sát range local, cần exact tiếng/AV, nguyên câu/attribution và seam/clearance trước kết luận dùng; report này không yêu cầu owner miễn lỗi hoặc đề nghị thêm lượt trả phí. Food seam và final30/rough35 vẫn mở.
