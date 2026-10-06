# EP01 — Thử phản ứng Đào R2

**Cập nhật kế tiếp tại [195](195_closed-lip-reaction-reference-preparation.md):** owner duyệt chuẩn bị ảnh môi khép; đã tạo hai ứng viên và bảng xem, chờ owner duyệt ảnh thực tế. Không duyệt hoặc gửi video mới. Kết quả R2 và sổ 322/322, còn 0 dưới đây giữ nguyên.

Ngày 2026-10-06. Owner “ok” cho đề xuất sau193: thêm tối đa 30 credit cho **một batch ba Lite R2**. Trần dự án mới 322 (=292+30), đã dùng292 trước lượt, còn30 được phép. Không tự tăng quyền theo account balance.

## Đầu vào và thay đổi đã khóa

Giữ START/END185 v0.2, cùng camera/route Lite/Frames/9:16/720p/8s/x3, silent fallback ON, Agent OFF. START SHA256 `9cefcec59dee6a6e3159d752e8c527f3cb43ec7514865ef61960c0c5674facda`; END `c4e654b09bb856fc0bf40966b79de782d3ed2ce5f7364e70cf1fd573150c9255`. Đã kiểm lại hash local.

R2 dùng đúng draft193: thay câu về môi/nhắc spoken line-dialogue shot bằng mô tả môi khép suốt; bỏ câu cuối nhắc dialogue/music/sound effects. Các câu về một nhịp gaze, thời gian1,2s, tay/cốc, half-smile, camera/ánh sáng giữ nguyên. Đây là phép thử **nhóm chỉ dẫn**, không chứng minh tác động riêng một từ hoặc nguyên nhân model.

P02 range0–2,5s chỉ được duyệt nhịp tại192. C-v0.6/K20/D06 giữ nguyên; SIA HOLD. Không thử thoại, đổi nội dung, mở Quality/master hoặc dùng hình fail trong phim. Quote live vượt30 thì dừng hỏi lại.

## Thực thi

Đã chọn đúng cặp ảnh trong thư viện Flow, xem thumbnail START/END, kiểm Lite/Frames/9:16/720p/8s/x3, Agent OFF và silent fallback ON. Quote live **30 credit**, account trước **184**. Prompt compose đọc lại khớp [bản gửi](evidence/194/prompt-R2-SUBMISSION.txt). Kiểm local xác nhận chỉ hai thay đổi đã khóa so với prompt193, không thêm sửa khác; cũng khớp nguyên draft R2 owner duyệt. [Ảnh preflight](evidence/194/preflight.png).

Gửi **một yêu cầu x3 lúc 2026-10-06T01:16:54.461Z** (08:16:54 giờ Việt Nam). Cả ba hoàn tất, không retry. Account184→154 sau tạo, đọc cuối vẫn154. Chi ròng **30**, sổ **322/322, còn0** trong quyền chi. Không dùng account154 để chạy vượt quyền.

## Đã tải đủ ba native và kiểm kỹ thuật

Tải qua tab riêng đúng asset URL + menu720p gốc. Callback hết thời gian chờ10s cả ba nhưng file đã về máy; kiểm file trước mọi retry. Không tái sinh hoặc upscale. [Manifest ID/path](evidence/194/download-manifest.json), [technical report](evidence/194/technical-report.json), [batch hoàn tất](evidence/194/completed-batch.png).

| Mã local / thứ tự lưới | ID Flow | SHA256 native |
| --- | --- | --- |
| R201 | 25ef2741-7a6d-4cd4-8ff5-9d4975fdcbce | dbd7f10fbfd73119085a2cea1edfc3c9f6d1f3e70d0a0200d8d3a0f5bad6ab46 |
| R202 | f3e2763f-7780-43c2-a284-f96e0f87884e | 1c1be0ff783e32434751669b77c945293e9614451aff94d492610bb2b30a63a2 |
| R203 | a2e5ee99-2f4f-4e64-ba28-7cfd8a7f3a93 | 1449616ecc6bd28adec3aa9d8764da58e95468a9827b5677358f4c42b2d2c568 |

Ba native đều 8s / 720×1280 / 24fps / H.264, full decode sạch. R201 không audio stream; R202/R203 có AAC, chưa nghe nội dung. Không audio không đồng nghĩa môi không chuyển động. Không dùng nguồn này thay giọng K20/D06.

## Review actual — cả ba REWORK, chưa chọn take

Root xem 16 frame mỗi clip cách0,5s trong0–7,5s, toàn72 frame0–3s ở bảng180×320/frame, và mở native frame số32 tại1,333s của từng clip. Chưa independent reviewer, chưa xem mọi frame3–8s ở native resolution hoặc nghe audio. Không gọi technical PASS là creative PASS.

| Mẫu | Quan sát | Kết quả |
| --- | --- | --- |
| R201 | Miệng mở rõ trước/trong quay, tay giữ cốc thêm cử chỉ/thay vị trí; quay nhìn xuống rồi về trái về sau. Không có audio nhưng vẫn diễn miệng. | REWORK. |
| R202 | Miệng mở trước/trong quay và nhiều lần về sau; gaze về trước/xuống khoảng3,5s trở đi, không giữ END suốt clip. | REWORK. |
| R203 | Miệng mở ở ngay phần đầu và lúc quay, sau đó gaze về trước/xuống rồi quay lại; không giữ một nhịp. | REWORK. |

Không thấy giơ tay như D02 trong bảng R202/R203, nhưng không dùng một lỗi giảm để tuyên bố cải thiện toàn cảnh hoặc hiệu quả do prompt. Chưa chọn đoạn cuối để làm giả đã có phản ứng quay lại sạch. Không crop mặt, đóng miệng hậu kỳ hoặc ghép lời lên hình REWORK rồi nghiệm thu.

## Bộ đối chiếu đã lưu

Folder owner `C:/Users/PC/Downloads/du_an_nem_bui/194_dao_reaction_R2/` có ba native, report và bảng review. File `R201-R202-R203_FULL8s_SILENT_COMPARISON.mp4` giữ nguyên đủ8s, trái→phải R201/R202/R203, thu mỗi ảnh360×640, không đổi tốc độ hoặc bỏ khung lỗi; bỏ audio local. Full decode sạch. SHA256 `36ca4fb3752545a3766297f98f7abb9c6a711758f923bc0bfdb09334b61768d8`.

Không sửa bản ráp182 hoặc kiểm nối192, không thêm coverage sản xuất đã duyệt. Không cần dựng lại cùng chẩn đoán P02→phản ứng fail của193 để gọi là bước tiến mới. P02 đầu2,5s vẫn giữ approval nhịp; full native8s chưa đạt. C-v0.6/K20/D06/SIA HOLD giữ nguyên.

## Kết luận phép thử và hướng tiếp

**Đã biết:** R1 và R2 đều0/3 đạt phản ứng im lặng theo cổng đang dùng. R2 đã thực sự bỏ nhóm nhắc lời thoại và dùng môi khép tích cực nhưng vẫn mở miệng. Thay nhóm này **không đủ chữa lỗi trong bộ thử194**. Từ kết quả này không thể khẳng định nhóm từ đó không có tác động, không thể gán lỗi chắc chắn cho ảnh hoặc kết luận mọi Veo/model đều bất lực: seed không khóa, các batch diễn ở thời điểm khác nhau, còn yếu tố pose/smile/reference conditioning/model.

**Quyết định vận hành:** dừng lặp nguyên cặp ảnh185 với chỉ sửa tiếp câu chữ về môi. Không tự mở Quality hoặc xin một batch giống hệt ngay. Giữ tất cả nguồn và mẫu lỗi để truy ngược.

**Đề xuất chuẩn bị đầu vào trước chi tiếp:** tạo cặp khung có đường môi khép rõ và biểu cảm cười bằng mắt, thân/tay/cốc cố định; chỉ khác nhau ở gaze/góc đầu cần thiết. Xem đối chiếu với hình hiện hành, kiểm hướng nhìn và canon trước khi thử động. Đây là thay nhóm ảnh nguồn để kiểm, không đổi thoại/câu chuyện/nhân vật, không khẳng định sẽ đạt và chưa tạo ảnh mới trong vòng194. Brief [bước tiếp](evidence/194/next-reference-preparation-DRAFT.md) là draft, cần owner duyệt hướng trước làm. Paid test tiếp vẫn phải có quyền riêng và quote live.

## Tổng kết vòng

- Đã xác định: đủ ba native kỹ thuật sạch; không có phản ứng im lặng đạt; lỗi môi/gaze còn sau thay nhóm prompt.
- Quyết định đã chốt: thực thi một x3 R2 trong30; không thêm generation, giữ P02/script/giọng và SIA HOLD.
- Giả định đang dùng: thiết kế pose/smile của ảnh nguồn có thể tác động diễn; chưa kiểm chứng.
- Vấn đề mở: phản ứng quay lại, Khoai nâng–khựng, chuyển–nhận/kết, nối hình thoại và speaker identity.
- Bước tiếp: chuẩn bị/kiểm khung môi khép trước khi xin chi thử mới. Chi30, trần322, còn0; chưa Quality/master/publish.
