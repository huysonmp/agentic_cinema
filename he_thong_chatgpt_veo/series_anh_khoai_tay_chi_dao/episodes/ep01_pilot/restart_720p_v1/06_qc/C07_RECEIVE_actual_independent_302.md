# REC302 — Kiểm hình độc lập C07 RECEIVE D06 T01

**Kết luận: NOT_SELECTED — MAJOR_IDENTITY_AND_PROP_CONTINUITY.** Không chọn toàn bản hoặc một đoạn đầu: Đào đã thành người có tóc từ F0 và không trở lại hình tượng quả đào trong toàn bộ 96 frame quan sát. Không trình owner miễn lỗi nhận dạng để dùng bản này.

## Phạm vi và bằng chứng

Review local theo REC217; không browser, sinh lại, chỉnh media/voice/EDL, git hoặc tiêu credit. Đã đọc đầy đủ approval `00_decisions/C07-RECEIVE-D06-one-run-approval-302.json` và prompt `04_requests/C07_RECEIVE_D06_T01_prompt_DRAFT_301.txt`. Approval chỉ cấp một request tối đa 7 credit, không tự retry và không chấp thuận chất lượng đầu ra.

Native thực kiểm:

- Owner: `C:/Users/PC/Downloads/du_an_nem_bui/302_C07_RECEIVE_D06_T01/C07_RECEIVE_D06_T01_NATIVE_720p_302.mp4`.
- SHA-256 tự kiểm: `85fb15de347d8054803eeeef186ea6d4f2985baa9fe46018bf281af9a6cfe527`, khớp hash root cung cấp cho bản repo `05_native/EP01_720_C07_RECEIVE_D06_T01_NATIVE_302.mp4`.
- Evidence có sẵn `native_qc/native_evidence.json`: H.264 720×1280, 24 fps, 96 frame/4 giây; AAC stereo 48 kHz, 4,010 giây, full decode success. Reviewer đọc metadata, không tự chạy decoder.
- Trực tiếp xem đủ sáu bảng `native_qc/full16_01..06.png`, F0–95 theo thứ tự hàng, không padding; xem thêm full resolution `all_native_frames/00001.png`, `00033.png`, `00065.png`, `00096.png` tương ứng F0/F32/F64/F95. Đây là toàn-frame ở kích thước bảng và bốn ảnh full resolution, **không continuous AV playback**.
- Trực tiếp đối chiếu START `02_refs/C07_START_NATIVE_C06_KEEP_A_F47_CANDIDATE_300.png`: Đào là quả đào có cuống/lá, tay ngoài nâng cốc, bát rỗng trên bàn, đũa nghỉ cạnh bát.

## Expected so với actual

| Hạng mục | Quan sát độc lập | Mức độ / xử lý |
|---|---|---|
| Nhận dạng Đào | F0 đã là cô gái có tóc búi, tai và đầu người; mất hình quả đào, cuống và lá. Tình trạng kéo dài F0–95. | **MAJOR / chặn selection**. Không có prefix giữ đúng nhân vật. |
| Cốc và phân công tay | Cốc đã ở trên bàn phía phải từ F0, thay vì trong tay ngoài đang nâng như START. F6–12 hai tay dần vào bát; F32/F64/F95 cả hai tay đỡ bát. | **MAJOR continuity/choreography**: mất yêu cầu một tay giữ cốc, một tay nâng bát. Không phải biến thể đã được duyệt. |
| Đũa nghỉ của Đào | Đôi đũa dọc bên phải bát có trong START không thấy ở F0 và các frame đã kiểm. | Đạo cụ không được bảo toàn; không tự bỏ khỏi canon. |
| Bát nhận / A | Bát riêng được nâng và đưa trái; F32/F64/F95 lòng bát nằm dưới vùng A, bát trông rỗng. A vẫn trên tips trong toàn bảng, không quan sát thấy nhả, gắp lại hay đưa về đĩa chung. | Có đáp ứng **một phần trạng thái hình**; không cứu lỗi nhân vật/tay–cốc và không chứng nhận vật lý chuyển động. |
| Tay nghỉ Khoai | Tay trong nhìn vẫn ở bàn; bát nhận che một phần vùng tay/bát Khoai khi đưa trái. Full F32/F64/F95 không đủ xác nhận toàn bộ khoảng hở phía sau bát. | Không khẳng định xuyên tay, nhưng cũng không cấp clearance/physics PASS từ che khuất. |
| Miệng / người nói | Miệng Khoai mở rõ F5–11, trái yêu cầu nghe với miệng khép; Đào có chuỗi mở miệng từ khoảng F12 đến F60. | Lỗi mouth attribution **trên hình**. Không suy ra Khoai thực nói N07 hoặc giọng bị đổi từ ảnh. |
| Bối cảnh / món | Medium two-shot giữ mặt hai bên, bảng không thấy cut/zoom lớn; có đĩa nem, rau, hai đồ chấm, hai bát và không thấy hơi nóng. | Chỉ phạm vi hình quan sát. Không chứng nhận món, lượng hoặc toàn cảnh giống nguồn tuyệt đối; food seam C05→C06 vẫn mở. |

## Giới hạn âm thanh và nguyên nhân

Reviewer chưa nghe native hoặc xem AV liên tục; **D06, giọng Bắc, đủ N07, âm cuối, diễn, nhịp và lip-sync chưa PASS**. Root báo ASR tự động nhận N07 ở khoảng 0,86–2,60 giây: đó là thông tin máy, không thay kiểm nghe hoặc xác nhận người nói. Không diễn giải lời trong prompt, tên preset hay luồng AAC thành giọng đạt.

Đã trực tiếp xem JPEG `C:/Users/PC/Downloads/e40803c5-9a46-44af-84d6-a588ef762895.jpg`, tự kiểm SHA `2d195991e9db1194f34edb4ca1c0f1df09faac79733185d0ebe63a05cee90176`: ảnh vẫn là Đào quả đào, cốc đang nâng, khớp trạng thái START về mặt nhìn. Việc JPEG này là ingredient khớp URI history do root đối soát; reviewer không tự đọc browser/backend. Không so hash JPEG tái mã hóa với PNG để tuyên bố identical pixels. Bằng chứng này không ủng hộ giả thuyết đã chọn nhầm ảnh người, nhưng chưa chứng minh nguyên nhân duy nhất của humanization. Các tiền lệ REC277/280 và thiếu kiểm hồi quy preflight là root báo, chưa được reviewer tái audit ở task này; không tuyên bố hai ảnh, preset giọng hoặc câu prompt riêng lẻ chắc chắn gây/chữa lỗi.

## Cổng tiếp theo

Giữ native và evidence làm bản thất bại; không chọn range, ghép production, dùng frame ra để chuẩn nhịp thả hoặc chuyển approval nguồn sang bản này. REC301 đã có appendix live proof; mức PAPER phù hợp bounded experiment không phải dự báo chắc chắn giữ nhận dạng, và actual REC302 đã không qua gate đó.

Root báo debit thực 1.029→1.022, 7 credit: project 258/500, còn 242, retake còn 5, reserve 110 CLOSED. Đây là đối soát browser của root, không tự kiểm bởi reviewer. Mức tăng 50 trước request chưa xác định nguồn không cộng cap. Snapshot run JSON còn generating không thay thế bằng chứng native đã có; root cần cập nhật trạng thái terminal, không sinh tiếp dựa trên snapshot cũ.

Bước an toàn là hoàn tất hồi quy input/prompt/config và chọn phương án xử lý có ngân sách/quyền mới rõ ràng. **Không retry tự động; không gọi clip đạt hoặc xin owner bỏ qua lỗi nhận dạng.** Các approval B, K20/D06 và REC300 về nối C05→C06 không được mở lại hay mở rộng bởi review này. Conflict rough 35 giây so với final 30 giây vẫn chưa được xử lý.
