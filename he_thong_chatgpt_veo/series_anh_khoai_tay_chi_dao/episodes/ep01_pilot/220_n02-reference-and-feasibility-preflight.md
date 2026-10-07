# 220 — Đầu vào N02 và phép chứng minh khắc phục

Ngày 2026-10-06. `G1_N02_PREPARATION_COMPLETE / OWNER_REQUEST_APPROVAL_PENDING / NOT_SUBMITTED`.

Lưu ý phiên bản: đây là trạng thái lịch sử lúc trình220. Owner sau đó duyệt đúng request; kết quả batch30credit và ba review thực ở [221](221_n02-pa-v-approved-trial.md). Không đọc trạng thái pending trên bản220 thành trạng thái hiện tại, và không nâng approval chạy thành approval đầu ra.

Đang ở **P7 recovery/G1**, chuẩn bị checkpoint N02 trước. Chưa đóng G1 toàn tập, chưa có G2 media proof, chưa quay lại finishing. Lượt này không chi credit, sinh ảnh/video, cài công cụ hoặc commit/push.

## 1. Điều đã xác định thêm

Root đọc prompt 200 thực tế, kiểm Flow hiện hành và mở đúng video N02. CONT chạy vòng kiểm độc lập về thứ tự ưu tiên của nguồn, xem chín ảnh; root đọc đầy đủ [báo cáo](evidence/220/01_cont-source-hierarchy-review.md). [Đối soát kỹ thuật](evidence/220/02_preflight-and-source-readback.md) lưu thao tác, mã băm, nguồn chính thức và giới hạn.

- Prompt 200 chỉ yêu cầu **nguồn tiếng thay thế**, không yêu cầu giữ mặt qua hết ý. Nó không phải bản yêu cầu hình ảnh sản xuất; duyệt tiếng tại 201/203 không chứng nhận hình. Không quy cả lỗi cho riêng một câu prompt khi chưa thử đối chứng.
- Video gốc cắt mặt → món tại 6,833333 giây, trở lại hai người tại 8,375 giây theo 216. CONT nay xác định cận món còn có nhánh lá trên đỉnh và bát chất lỏng khác trạng thái phục vụ chuẩn. Không dùng nguyên đoạn cận đó để lấp N02.
- Tìm thấy đúng K20 custom ID trong Flow, không nhầm Orus base/K12. Điều này xác nhận cấu hình, chưa chứng nhận tai nghe hoặc giữ giọng ở đầu ra mới.
- Có tuyến dùng video nguồn làm thành phần trong Omni. **Khả năng sửa hình mà giữ nguyên audio/khẩu hình vẫn chưa được chứng minh.** Không tìm thấy bằng chứng tuyến nhận WAV đã duyệt và giữ PCM tuyệt đối; không mở vendor/API mới.

## 2. Nguồn nào kiểm thuộc tính nào?

| Nguồn | Dùng cho | Giới hạn |
|---|---|---|
| TABLE08/v0.8, owner duyệt tại 78 | Quán, vị trí bàn, bộ phục vụ, ánh sáng và trạng thái trước gắp | Không tự xác nhận công thức/khẩu phần hoặc mọi góc máy |
| PAIR03/v0.3 | Nhận diện và trang phục | Không lấy nền studio/tư thế đứng sang cảnh |
| Hai ảnh món owner cho phép dùng | Hỗ trợ hình thái/texture Nem Bùi | Không chuyển toàn bộ rau/trang trí/món khác sang bàn |
| OPEN7 | Đối chiếu ảnh phái sinh và cảnh N02 hiện hữu | Chưa là chuẩn hình sản xuất; món rộng/sáng hơn, mặt/nền được dựng lại |
| N02_NATIVE, hồ sơ 200/201 | Tiếng đã duyệt, ứng viên hình và đầu vào phép thử | Có đoạn hình lỗi; chưa đạt kiểm toàn bộ hình–tiếng |

Không hỏi lại quyền dùng hai ảnh món đã được owner cấp. Không thu hồi TABLE08 hoặc nâng OPEN7 thành chuẩn chung bằng một approval thử kỹ thuật.

### Đối chiếu ảnh thật để owner nhìn được khác biệt

TABLE08: chuẩn bàn đã duyệt, nhân vật nhỏ hơn trong khung và ụ nem gọn.

![TABLE08 — serving-state đã duyệt](D:/Workspace/agentic_cinema/he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/media/raw/ep01_p6_food/T-NB-03_v0.8.jpg)

OPEN7: khung gần hơn, ụ nem rộng/sáng hơn; hiện chỉ là ảnh chẩn đoán/ứng viên.

![OPEN7 — derivative candidate, không canon mới](C:/Users/PC/Downloads/du_an_nem_bui/T2-CODEX-OPEN_v0.7.png)

Phép thử dưới dùng **video N02 hiện có**, không nhập thêm TABLE08/PAIR03/ảnh món để model trộn các trạng thái mâu thuẫn. Các ảnh này là nguồn reviewer đối chiếu. Duyệt phép thử không là duyệt variation production của OPEN7. Khi chọn anchor cho phần hình toàn tập, phải trình variation exact hash riêng trước lock.

## 3. Quyết định hiện cần chốt: thử tuyến nào?

| Tuyến | Đầu vào và giá đã kiểm | Hệ quả |
|---|---|---|
| **PA-V — khuyến nghị thử trước** | Video N02 làm thành phần + prompt sửa hình; Omni 1.1 Flash / 360p / 9:16 / thời lượng theo nguồn 10 giây / x3. **UI báo 30 credit** | Thử bảo toàn tiếng đã duyệt đồng thời sửa mặt/ánh nhìn. Có thể vẫn sinh lại tiếng/hình; phải đo và nghe, không cam kết model giữ nguyên |
| PA-N — dự phòng, chưa xin chạy | OPEN7 + đúng K20; tạo mới 360p / 10 giây / x3, UI báo 21 credit | Bản thu mới dù cùng preset. Phải nghiệm thu lại tiếng/nhịp/hình–tiếng, không lấy 201 làm duyệt đầu ra mới |
| Chỉnh trực tiếp trên N02 — chưa đủ gói để chạy | Omni ở màn chỉnh sửa; giá công bố 40 credit/đầu ra, chưa thấy giá live của đúng yêu cầu | Có thể là cơ chế sửa khác; không lấy giá 7/10 của composer để chạy tuyến này. Cần kiểm trước chạy và duyệt riêng nếu chuyển |

Khuyến nghị PA-V vì tiếng N02 đã được chấp nhận và ưu tiên tái dùng tại 215, **không chỉ vì giá**. Không chạy PA-N hoặc tuyến chỉnh trực tiếp tự động nếu PA-V không đạt. Ba đầu ra cùng nguồn/prompt là kiểm độ ổn định, không phải phép đa biến tách riêng nguyên nhân ánh nhìn/cắt cảnh/món.

### Phạm vi xin duyệt — REC220-N02-PA-V-R1

Cho đúng **một batch x3**, trần riêng **30 credit**, chỉ tuyến composer video-conditioned tại project `9276788e-9781-44fb-ba5b-083006667374`. Input dự kiến: asset N02 `3b312ed6-ac2b-4798-b965-cffe5f738893`, title `Character recording audio direction`; native local `C:/Users/PC/Downloads/du_an_nem_bui/200_n02_replacement/N02_NATIVE.mp4`, hash theo216/218 `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153`.

Prompt exact: [N02-PA-edit-DRAFT](evidence/220/N02-PA-edit-DRAFT.txt). Không gắn D06 hoặc thêm preset giọng để thu lại. Agent OFF; không Extend/Quality/retry, không mua credit, không sản xuất phần khác. Input selection phải đối soát lại: DOM chip chỉ hiện thumbnail, không lộ video UUID; tên duy nhất/thumbnail là evidence hiện có, không giả đã hash cloud bytes. Nếu selection mơ hồ, cấu hình/giá thay đổi hoặc tổng>30: HOLD/trình lại **trước submit**.

Đầu ra là proof `NOT_RELEASE`, không final N02 hoặc approval hình/voice. Ngân sách cũ không được dùng thay quyết định này. Tài khoản đủ số dư phải kiểm trước chạy; thiếu thì báo, không nạp.

![Actual preflight — video ingredient và prompt, x3, UI30 credit, chưa gửi](D:/Workspace/agentic_cinema/he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/evidence/220/flow-video-ingredient-prompt-x3.png)

UI báo 30 credit cho composer, khác giá chỉnh trực tiếp 40 credit/đầu ra trong [bảng Google công bố](https://support.google.com/flow/answer/16526234). Hai tuyến được ghi riêng; giá UI không phải biên nhận phí thực. Không bỏ qua sự khác nhau hoặc tự chi 120 credit cho tuyến khác từ duyệt 30 credit. Google mô tả Omni có chỉnh video và tham chiếu trong [hướng dẫn mô hình](https://support.google.com/flow/answer/16352836?hl=en), nhưng có nút/tính năng không là bằng chứng bảo toàn tiếng đã thu.

## 4. Sau khi được duyệt, tôi xử lý theo thứ tự nào?

1. Đọc lại khóa178/214, source/prompt/hash, preset/source role, actual settings/quote/balance; lưu pre-submit trước đúng một lần gửi. Không nhầm giọng nam/nữ hoặc source cũ.
2. Lưu job IDs, đủ ba native outputs, hash/probe/giải mã. Tải không thành công: xử lý download, không sinh lại để lấy file. Không chỉ chấm thumbnail.
3. **SIA/AV:** tách PCM, so audio/time với N02 nguồn đã duyệt; ASR chỉ hỗ trợ phát hiện, không thay nghe/so giọng. Bytes khác có thể do codec, nên cần alignment/sai số và actual listening để phân biệt; không gán sai giọng chỉ từ unequal hash. Không tự ghép tiếng cũ lên khẩu hình mới hoặc retime để giả giữ nguyên.
4. **DOP/CINE + ACT/PERF:** kiểm mặt/miệng Khoai qua hết “anh đứng chờ”, người nghe im lặng, gaze hướng tới Đào, sắc thái ký ức và động cơ cut; trích ảnh toàn take/biên cut rồi kiểm chuyển động và AV đúng capability. Nếu chỉ có ảnh, ghi sampled-frame verdict, không full-AV PASS.
5. **CONT:** phục vụ/khói/outfit/trục/F0; không gắp/đưa bát sớm. So baseline theo thuộc tính, không đếm vật khuất vì crop là bị xoá. Không lá đỉnh/bát mới không có nguyên nhân.
6. Root tổng hợp expected/observed/timecode/severity/source-fix từng output; giữ lỗi trọng yếu mở, gửi bản có hash và checklist nghe/xem cho owner. Chọn đúng N02 proof chỉ sau checkpointG2, không tự cộng các PASS riêng thành phim đạt.

Nếu cả ba không đạt giữ tiếng+mặt: dừng batch, ghi học được gì và trình trade-off tiếp. Không phủ lại cả lượt bằng món, không đổi lời, không tự thu mới. Giữ201/203 cho audio cũ.

## 5. Tổng hợp vòng và bước sau

- **Đã xác định:** thứ tự ưu tiên của nguồn, lỗi trạng thái phục vụ tại đoạn cận; đúng K20 và ba tuyến Flow khác nhau; gói dựa trên video nguồn có đầu vào/prompt/giá 30 credit thực trên UI.
- **Đã chốt:** giữ C-v0.6, K20/D06, storyboard 214, bạn bè/cốc tự nhiên/đường A→bát→B, Flow + local và duyệt từng phép thử trả phí riêng. Không có duyệt mới trong 220.
- **Giả định kiểm thử:** video reference có thể giúp giữ voice/timing khi sửa coverage; OPEN7/N02 chỉ làm đầu vào diagnostic, chưa canon production.
- **Còn mở:** quyền batch30, actual giữ audio/face/lip/gaze, variation anchor toàn tập và fullG1 storyboard ảnh, causal chain, nhịp30s/fullAV. Finishing vẫn chặn.
- **Bước tiếp:** owner duyệt/không duyệt REC220-N02-PA-V-R1; nếu duyệt, root chạy và review đúng batch, không hỏi lại nền tảng/nhân vật. Sau N02 đạt: chọn/sửa bộ ảnh cả tập → lời còn lại → chuỗi A/bát/B → rough cut không tiếng+có tiếng → owner duyệt → xuất và QC.

Skill computer-use được dùng để kiểm/chuẩn bị UI và lưu proof, qua browser CUA; không native Windows/login automation. Composer đã trả về Lite/Khung hình/720p/8s/x1, START/END/prompt trống và Generate disabled; nguồn và voices không bị sửa. Tài liệu/prompt/report lưu tại project; các file evidence UI không phải approval hoặc billing.
