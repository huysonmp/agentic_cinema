# REC220 — Root: đối soát đầu vào và tuyến Flow

Ngày 2026-10-06. Scope: local source-readback, actual Flow UI, official documentation, request preparation. Không sinh video/ảnh/preview mới, upload, chi credit hoặc git commit/push. Không actual listening/full-AV mới. Không ghi owner approval mới.

## Nguồn đã đọc/xem thực

Root đọc đầy đủ 219, prompt-actual200,196,101,78,178,109,111,114,115 và report CONT220. Các khóa212–218 giữ nguyên từ vòng trước. Root xem trực tiếp TABLE08, PAIR03 và OPEN7 bằng view_image; hash thực của cả ba trùng101/109. Không suy toàn media đủ chuẩn từ ba stills.

| ID | File thực | SHA256 |
|---|---|---|
| TABLE08 | `media/raw/ep01_p6_food/T-NB-03_v0.8.jpg` dưới series root | `aeb6dfaee1773109243f9f952235a44f2417c6fb7fb4faf15be61c34ca40d924` |
| PAIR03 | `media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg` | `ecfbe7a3c543730c268a77ca08d508147115ca804154f85ebdbb38c5c601e8c7` |
| OPEN7 | `C:/Users/PC/Downloads/du_an_nem_bui/T2-CODEX-OPEN_v0.7.png` | `a3d80f09bfb7242bae3007ad7b4f37473bb2f0ed019a84cc4956c4d32a8dbf9a` |

CONT đã xem/hash thêm hai ảnh món và bốn frame native; root đọc FULL report, không nhận root đã tự xem thêm các ảnh đó trong220. Native N02 và WAV202/provenance giữ theo216/218, chưa hash/nghe lại vòng này.

### Bổ sung authority của REAL2 — không yêu cầu duyệt lại

Trong lịch sử chat, owner trực tiếp nói hai ảnh món `nembui.jpg` và `z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg` đã duyệt, có thể sử dụng. Do đó cả hai có quyền dùng làm tham khảo món theo yêu cầu human. Nhận xét của CONT “sáu hồ sơ chưa có selection record REAL2” là giới hạn bộ evidence được cấp, không phải tuyên bố chưa có human permission. Quyền dùng ảnh tham khảo không thay serving-state78 hoặc xác nhận recipe/quyền pháp lý tuyệt đối. Không chuyển đồ ở mép ảnh/lá trang trí sang bàn chỉ vì ảnh đã được phép dùng.

## Actual UI

Đúng in-app Flow project `9276788e-9781-44fb-ba5b-083006667374`, title `EP01_P6_Khoai_Dao_Pilot`. Đầu vòng: Video/Khung hình/720p/8 giây/x1; prompt/input trống, Generate disabled. Chỉ mở/đổi các setting phục vụ preflight, không submit.

- Model menu có Omni1.1Flash, Veo3.1Lite/Fast/Quality. Chuyển Omni thực hiện đổi summary thành360p/10 giây; không coi thao tác Expand chỉ đọc submenu: nó đã chọn model. Sau đó chọn Thành phần để kiểm voice route.
- Omni/Thành phần/9:16/360p/10 giây/x1: quote7. Chọn x3: quote21 thực trên UI. `flow-omni-preflight-x1.*`, `flow-omni-preflight-x3.*` là evidence. Đây quote tạo mới, không quote sửa video.
- Voice picker tìm Orus: có hai bản custom cùng tên và bản base. Bản performance “Nam khoảng33 tuổi… bo tròn âm” có field IDs `fb1188da-e6c8-4156-9bba-0576c01a8da6-*`, đúng K20. Không sửa performance/name/sample, không bấm preview hoặc Add. `flow-k20-picker.*`. Mới kiểm K20; D06 ID giữ theo152, chưa live-readback D06 vòng này.
- Mở exact N02 asset `3b312ed6-ac2b-4798-b965-cffe5f738893`: title Character recording audio direction,360p,total10 giây, lịch sử đúng prompt200 và hai thành phần. Timeline trực quan có cận mặt rồi cận món rồi trở lại hai người. Composer edit ghi Omni1.1Flash. `flow-n02-edit-route.*`.
- Nhập nguyên file `N02-PA-edit-DRAFT.txt` để kiểm trạng thái edit; nút tạo enabled nhưng không có giá hiển thị trong AX hoặc title/aria của nút. Không bấm tạo để dò một dialog có thể không tồn tại. Lưu `flow-n02-edit-draft-not-submitted.*`; xoá prompt nháp, xác minh nút tạo disabled. Không source/output nào bị xoá hoặc thay.
- Báo dư thấp ở đầu vòng, nhưng không đọc số dư live. Số dư lịch sử57 và quyền chi còn3 của210 không được dùng cho request mới. Không mua/nạp hoặc đổi gói.

## Đối chiếu tài liệu chính thức — đọc ngày2026-10-06

- [Create videos](https://support.google.com/flow/answer/16353334?co=GENIE.Platform%3DDesktop&hl=en): voice references cho Omni/Ingredients; chọn preset/custom voice. Không mô tả một tuyến nhận WAV và bảo toàn PCM đã duyệt. **Khả năng WAV→khẩu hình/PCM nguyên bản: chưa được chứng minh**, không suy chắc chắn hỗ trợ hoặc tuyệt đối không hỗ trợ.
- [Models/features](https://support.google.com/flow/answer/16352836?hl=en): Omni1.1 hỗ trợ10s và video editing; VeoLite không video-to-video edit. Không gọi thử Omni là “ba lượt VeoLite”;360p là mức draft của tuyến Omni này.
- [Edit videos](https://support.google.com/flow/answer/16935718?hl=en): Omni có thể edit phần video tới10s. Có đường edit không chứng minh giữ audio, khẩu hình hoặc identity; chưa thử server trong220.
- [Credits](https://support.google.com/flow/answer/16526234): bảng công bố Omni360p10s7/đầu ra; video edit40/đầu ra cho mọi độ dài/độ phân giải. Quote tạo mới x3 trên UI21 khớp bảng. **Edit40 chỉ là giá công bố, chưa quote live exact request; không lấy7 làm giá edit.** Không dùng số subscriber monthly trong trang để phủ định quyền credit user đã cấp lịch sử.

## RCA được làm rõ

Prompt200 ghi rõ audio-source replacement/not final picture, giữ tay nghỉ nhưng không ràng buộc speaking-face coverage, gaze tới bạn hoặc động cơ cut. Đầu ra đã có insert món. Đây là thiếu specification cho hình nếu đem sử dụng sản xuất, **không chứng minh chỉ một câu prompt gây ra cut**. Lỗi quy trình là biến source được duyệt tiếng thành picture đạt mà không đo/full-review trước ráp. Insert còn có serving-state drift theo CONT; chỉ xóa insert không tự đóng gaze/diễn/khẩu hình/voice.

Hai draft mới tách edit-preserve-audio và new-take. Yêu cầu trong prompt không là enforcement; output phải tải native, hash/probe, map7 lượt/within-turn, trích frame và review đúng capability/version. Chưa xin chạy cả hai tuyến hoặc auto fallback.

## Preflight bổ sung: dùng video làm thành phần — không đồng nhất với editor

Sau khi đọc giá edit40 chính thức, root kiểm thêm composer project để có quote đúng loại request. Chuyển tạm Omni/Thành phần, tìm exact title `Character recording audio direction`; picker trả một kết quả Video. Bấm kết quả đã **gắn video chip ngay**, không chỉ mở preview. Không upload hoặc submit. Không lặp lại sai mô tả “chỉ xem” khi thao tác đã thay composer.

DOM chip chỉ lộ thumbnail image ID `bfa1790d-1e53-427e-9645-8c74931c5b7e`, không lộ asset UUID của video. Không gọi thumbnail ID là clip ID. Grounding input hiện có: unique result trong đúng project, exact title và thumbnail hai mặt phù hợp N02 đã mở ở editor đúng UUID. Trước submit phải đối soát lại source selection/history; nếu mơ hồ hoặc có nhiều bản cùng tên: HOLD, không thay video ngầm.

- Một video ingredient: summary360p/10 giây/x1, duration “Độ dài dựa trên thành phần ·10 giây”, quote**10** thực. Không còn quote7 của input ảnh/voice hoặc composer trống.
- Nhập đúng `N02-PA-edit-DRAFT.txt`, chọnx3: quote**30** thực, prompt và video chip cùng hiện. Screenshot/root đã mở ảnh này lại bằng view_image: `flow-video-ingredient-prompt-x3.png`; AX cùng tên.txt. Không bấm tạo.
- Đây là **video-conditioned candidate generation trong composer**, không khẳng định có cùng semantics/cost với editor sửa trực tiếp. Official edit40 và live ingredient10 là hai signal khác tuyến; không hứa giữ PCM hoặc billed cost từ quote. Đề xuất thử chỉ route composer này, cap30; nếu UI đổi sang edit40/đầu ra hoặc tổng>30: dừng xin duyệt, không tự chuyển tuyến.
- Xoá gói nháp trong composer: cả text lẫn video chip biến mất, Generate disabled; video asset vẫn ở thư viện. Trả về VeoLite/Khung hình/9:16/720p/8 giây/x1, giá10, START/END/prompt đều trống, Agent OFF. `flow-final-empty-restored.*` là evidence cuối; giữ tab handoff. “Khôi phục” là cấu hình quan sát tương ứng đầu vòng, không tuyên bố đã biết initial model UUID từ tree đầu.

Giọng K20 hiện tại đã kiểm đúng preset, nhưng request video-conditioned đề xuất **không gắn thêm preset hoặc D06**, để không ra lệnh thu mới. Audio-preservation là hypothesis kiểm bằng native output/PCM/timing; thiếu matching PCM không tự kết luận sai identity, nhưng không đạt mục tiêu giữ nguyên bản thu. Không tự ghép WAV cũ lên khẩu hình/timing mới để báo đạt.

Voice-reference local: root truy hồ sơ149–152. Hai audition được owner chọn chủ yếu là preview trong Flow;149/151 ghi rõ không có file audio local. Đây là khoảng evidence, không lời yêu cầu tuyển lại giọng. Có thể bố trí owner nghe so trong Flow khi kiểm candidate; không gán actual listening cho root hoặc reviewer chỉ từ screenshot/preset ID.

Các AX.txt ban đầu là output **diff** theo mặc định CUA, không gọi là full DOM snapshot. Chúng giữ ID/quote thay đổi, cùng screenshot đầy đủ và tool transcript của lượt220. `flow-end-full-ax.txt` được lấy riêng với disableDiffing=true để lưu full state cuối; không tái dựng snapshot lịch sử bằng chữ viết tay. K20 sample109 ký tự tự hiện khi chọn preset, root không thay sample/performance và không bấm phát/sync/save. Việc nó xuất hiện không là preview mới đã chạy hoặc evidence root nghe được.
