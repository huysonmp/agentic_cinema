# EP01 — Duyệt và thử phản ứng Đào bằng ba Lite

Ngày 2026-10-06. Owner trả lời “ok” cho câu hỏi tại192: duyệt cặp khung185 v0.2 và bổ sung tối đa30 credit cho **một batch x3 Lite** phản ứng Đào trước N05. Trần dự án292 (=262+30), đã dùng262, còn30 được phép trước chạy. Account balance không thay quyền chi.

## Phạm vi khóa

- START `START_Dao_reaction_v0.2.png`, SHA256 `9cefcec59dee6a6e3159d752e8c527f3cb43ec7514865ef61960c0c5674facda`.
- END `END_Dao_reaction_v0.2.png`, SHA256 `c4e654b09bb856fc0bf40966b79de782d3ed2ce5f7364e70cf1fd573150c9255`.
- Một nhịp mắt/đầu từ cốc bên phải khung sang Khoai bên trái, giữ môi khép/tay/cốc; không thoại, không trao món hoặc diễn tay Khoai ngoài frame.
- Owner duyệt hai khung **cho phép thử này**, không canon/full scene/continuity PASS. C-v0.6/K20/D06 giữ nguyên, SIA HOLD; P02 đầu2,5s vẫn được duyệt về nhịp tại192, không native8s.
- Chỉ chạy khi giá live không quá30 và đủ quyền chi; không Quality/master/publish. Chưa coi bật silent fallback là native không có audio.

## Thực thi

Đầu vào local kiểm hash khớp, xem actual hai PNG, upload/chọn đúng START/END185 v0.2 (không cặp167 cũ). Tab mới ban đầu Omni1.1 Flash/x1; đã chuyển sang Frames/Veo3.1 Lite/9:16/720p/8s/x3, quote live30. Silent fallback ON, Agent OFF. Đọc lại nội dung compose khớp prompt đã trình192 và [bản gửi193](evidence/193/prompt-dao-reaction-SUBMISSION.txt); [ảnh preflight](evidence/193/preflight.png).

Submit **một lần 2026-10-06T00:23:01.464Z** (07:23:01 giờ Việt Nam). Ba video hoàn tất, không retry/generation thêm. Account214→184 sau tạo, kiểm cuối vẫn184: ròng30, sổ **292/292, còn0** được phép chi. Account184 không cấp quyền thử tiếp. [Ảnh batch](evidence/193/completed-batch.png).

## Tải và kỹ thuật

Tải qua tab riêng asset + menu720p gốc. Callback timeout10s cả ba nhưng file thực đến Downloads; không dùng callback làm bằng chứng thất bại, không bấm tạo lại. Đối soát đúng ID, tên file actual, bytes/hash/probe/full decode. [Manifest tải](evidence/193/download-manifest.json), [technical report](evidence/193/technical-report.json).

| Mã local / lưới trái→phải | ID Flow | SHA256 native |
| --- | --- | --- |
| D01 | 647e958a-bd56-44f7-8542-6167f1101cf4 | acd26ad4ada20aa54d7f3e40985f07f8b5bd5ab841b753c1c2058b690032349a |
| D02 | 13ddf229-e93a-4e9c-bd9a-9556d30f5aeb | 79d9941ad7c66956d55738eb21eab6ac5ffaf48e826d8fa775c43fd7f4e1db54 |
| D03 | 8933c7b7-eb8a-4611-b994-660d5edbc705 | 3e5caabe57688ee8fc1ffaad614328fdc2edb65ca98c98f26ef2210fcb442d72 |

Đều8s/720×1280/24fps/H.264, giải mã sạch. D01/D02 có AAC, chưa nghe nội dung; **D03 không audio stream**. Không suy D03 môi khép chỉ vì không tiếng. Các bản gốc giữ nguyên; bản so sánh/nối bỏ audio local, không thêm lời hoặc thử giọng mới.

## Review hình actual — cả ba REWORK

Root xem16 khung mỗi clip cách0,5s trong0–7,5s; thêm toàn72 frame0–3s trong bảng180×320/frame cho cả ba; mở native frame D01 tại1,25s, D02 tại1,125s, D03 tại1,458s. Không review mọi frame3–8s ở native resolution, không agent độc lập/listening hoặc full creative PASS.

| Mẫu | Quan sát | Quyết định |
| --- | --- | --- |
| D01 | Miệng mở từ khoảng0,4s, trước và trong quay sang trái; tay thêm cử chỉ thấp; nhìn xuống/quay lại nhiều lần về sau. | REWORK, không chọn phản ứng im lặng. |
| D02 | Thêm cúi/chớp mắt, giơ tay rõ khoảng0,95–1,6s; miệng chuyển động, gaze không giữ một điểm cả clip. | REWORK, không chọn. |
| D03 | Không audio nhưng miệng mở trước/trong quay, nhìn xuống rồi trở lại; người nền đi qua vùng đầu. | REWORK, chỉ đưa vào bản chẩn đoán để thấy lỗi. |

Cốc/tay giữ cốc còn ở phía phải trong các frame xem; không dùng một tiêu chí này để bỏ qua lỗi môi/hành vi. Không thấy hơi nổi bật trong mẫu frame, chưa chứng nhận không haze toàn video. Không lấy đoạn cuối đã nhìn trái để gọi đã có chuyển động quay lại sạch; không cắt khỏi mắt/miệng để giấu lỗi.

## Bản đối chiếu và nối chẩn đoán

Folder owner `C:/Users/PC/Downloads/du_an_nem_bui/193_dao_reaction/` giữ D01–D03 nguyên8s.

- `D01-D02-D03_FULL8s_SILENT_COMPARISON.mp4`: đầy đủ8s, trái→phải D01/D02/D03, mỗi ảnh360×640, không đổi tốc độ; bỏ audio local. Decode sạch, SHA256 `cd44a03fc4f768959a42f399a504bf504ec349cf71fadc63e1efd9439cd155cf`.
- `join_diagnostic_v0.2/EP01_P02_D03_4.5s_REWORK_DIAGNOSTIC.mp4`: P02 đã duyệt2,5s → D03 đầu2s **REWORK**, nhãn không chọn rõ. Chỉ xem lỗi trong mạch, không candidate/final, không thay bản192/182.720×1280/24fps/108frame/4,5s, không tiếng, full decode sạch. SHA256 `6b0fdb0367d72c633d3a5036beec7f8ec89d4a91e6dd9862a660c5e64bfd3e6e`. [Config](evidence/193/join-diagnostic-config.json), [manifest](evidence/193/join-manifest.json).

Root xem contact sửa đủ9 khung0–4s, thấy trục nhìn trái vẫn hợp ý định nhưng miệng mở khiến nhịp nhìn lén→bắt gặp không đạt phản ứng trước thoại. Chưa thêm coverage sản xuất hoặc nghiệm thu nối. Không dùng shot Đào này thay biểu cảm nâng–khựng của Khoai ngoài khung.

### Lỗi công cụ review đã sửa riêng

Contact của bản chẩn đoán v0.1 chỉ hiện4 khung D03, thiếu phần P02. Frame đầu extract cho thấy video vẫn có P02; log FFmpeg hiện `Reconfiguring filter graph because video parameters changed` ở tag màu khi concat. Bộ lọc tile bị khởi tạo lại, bỏ phần đang đệm. Không truy nhầm lỗi này sang Veo hoặc video mất đoạn.

Sửa riêng export contact trong `render_ep01_action_join_probe.py`: giữ filter review qua cut bằng `-reinit_filter 0`, dùng cho các segment đã encode cùng720×1280/pixel format. Render sibling v0.2, contact đủ9 khung; **hash video v0.1/v0.2 giống nhau**. Không sửa ảnh/model/native hoặc màu nội dung của video. Default186 render hồi quy giữ video hash `996f250d9e34ac05520495d308678475fba397d4172901f7fde517d9d400965e`; py_compile đạt. Lưu contact lỗi, contact sửa và log trích tại[review-export-check](evidence/193/review-export-check.json). Không dùng contact thưa/sai đếm frame để duyệt sản phẩm.

## Bước tiếp đề xuất — chưa chạy R2

Đã chuẩn bị [prompt R2 draft](evidence/193/prompt-R2-DRAFT-NOT-SUBMITTED.txt): chỉ mô tả môi khép, mắt dẫn đầu quay ngắn, tay/cốc cố định; bỏ nhóm nhắc `spoken line`, `dialogue shot`, `dialogue/music/sound effects` trong prompt, giữ route/reference/silent setting. Đây là giả thuyết cấp nhóm chỉ dẫn về diễn, **chưa chứng minh các từ đó gây mở miệng**. Không gọi prompt mới đã cải thiện; chưa generation R2.

Trước paid retest phải có owner approval một x3 mới tối đa30 và kiểm quote live; hiện còn0. Không lặp cùng prompt193 hoặc mở Quality để mong tự hết lỗi. Nếu owner muốn dừng thử, giữ nhịp P02 đã duyệt và báo rõ phần phản ứng chưa hoàn tất, không thay ngầm bằng ảnh tĩnh hoặc đổi kịch bản.

## Tổng kết vòng

- Đã xác định: ba native và bản so sánh/nối chẩn đoán; kỹ thuật đạt nhưng cả ba chưa đạt diễn phản ứng.
- Đã chốt: cặp185 được duyệt cho phép thử, một x3 trong30 đã thực thi; P02 approval/C-v0.6/K20/D06 giữ nguyên.
- Giả định: nhóm diễn liên quan lời nói trong prompt có thể kích hoạt mở miệng; cần thử kiểm soát, chưa nguyên nhân xác nhận.
- Còn mở: phản ứng im lặng, nâng–khựng Khoai, chuyển–nhận/kết, hình thoại và SIA HOLD.
- Tiếp: owner xem bộ đối chiếu; xem xét R2 trong quyền mới trước chạy. Chi30, sổ292/292, còn0; không Quality/master/publish.
