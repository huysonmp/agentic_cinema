# 221 — Phép thử N02 PA-V đã được duyệt

Ngày 2026-10-06. Trạng thái hiện tại: `TRIAL_COMPLETE / THREE_REVIEWS_READ_BACK / G2_HOLD / NOT_RELEASE`.

Tiếp nối ngày7/10: owner đã chọn B đúng phạm vi N02 ở [222](222_n02-b-owner-approval-and-episode-anchor.md). Các trạng thái HOLD/đề nghị nghe bên dưới là snapshot lúc trình221; không tự nâng thành approval toàn tập, PCM bit-exact hoặc chuẩn hình toàn EP01.

Trạng thái lúc lập bản: `OWNER_APPROVED / PRE_SUBMIT_CHECK`; phần kết quả dưới ghi thực thi tiếp theo. Đã dùng đúng30credit, không còn quyền retry từ request này.

## Quyền chạy

Owner trả lời **“ok”** trực tiếp cho đề nghị REC220-N02-PA-V-R1 tại tài liệu 220. Duyệt đúng một batch ba đầu ra, tối đa 30 Flow credit; không phải duyệt chất lượng đầu ra hay toàn tập.

- Project composer, video N02 `Character recording audio direction`, asset kỳ vọng `3b312ed6-ac2b-4798-b965-cffe5f738893`.
- Omni 1.1 Flash, 360p, 9:16, thời lượng theo thành phần video 10 giây, x3, Agent OFF.
- Prompt nguyên văn tại `evidence/220/N02-PA-edit-DRAFT.txt`, SHA256 `efd9770484a8274c6601c366ca5cb9f8b48be80f67ca8e9742717ff2928c9233`.
- Không thêm voice preset, thu lời mới, Quality, fallback, retry, cảnh khác, vendor/API hoặc nạp credit.
- Kiểm nguồn duy nhất, prompt, settings, quote và số dư trước gửi. HOLD nếu nguồn mơ hồ, giá vượt 30 hoặc cơ chế thay đổi.

## Khóa nghiệm thu

Giữ nguyên lời Khoai, tiếng và thời gian nguồn là giả thuyết phải kiểm. Khoai hiện mặt/miệng qua hết lời; Đào nghe im lặng; bàn ăn lạnh không khói, tay nghỉ, không gắp sớm. Không tự chồng audio cũ lên khẩu hình mới. Chấm riêng dữ liệu kỹ thuật, ảnh lấy mẫu và nghe/xem liên tục đúng năng lực kiểm.

Đang ở P7 recovery, phép chứng minh N02 trước checkpoint G2. G1 toàn tập, G4 rough cut và G5 export chưa hoàn tất. Không có full-film PASS.

Kết quả chạy, nguồn, bằng chứng UI và media sẽ được bổ sung tại `evidence/221/`; tài liệu 220 giữ trạng thái lịch sử trước approval.

## Kết quả chạy thực

Đã gửi một batch, tải đủ ba native 360×640/24fps/10s. Số dư trước107 → sau77, giảm30credit, đúng cap; đây là đối soát số dư, không phải biên nhận billing. Không chạy thêm/Quality/fallback hoặc sửa voice preset. [Manifest](evidence/221/run-manifest.json) gắn cloud asset, local path và SHA256 cho từng bản.

![Ba đầu ra hoàn tất trên Flow](D:/Workspace/agentic_cinema/he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/evidence/221/outputs-completed.png)

### So sánh để owner không phải tìm lại lỗi kỹ thuật

| Bản | Quan sát hình thực | Tiếng và kết luận hiện tại |
|---|---|---|
| A | Còn cận món `[7,000;8,375)` không mặt; insert có lá trên đỉnh và bát chất lỏng lệch wide | Waveform gần nguồn, nhưng lỗi hình trọng yếu vẫn còn. Không đề nghị chọn |
| B | Không cận món trong mẫu; cận → hai người ở7,000s, mặt/miệng Khoai vẫn hiện; không thấy caption hoặc serving-state blocker trong mẫu | Có thay đổi alignment cục bộ, chưa nghe/kiểm AV thực. **Ứng viên để owner xem, không PASS** |
| C | Mặt còn hiện nhưng tự thêm caption; nativef97/4,041667s có chữ, f175/7,291667s còn chữ, f176/7,333333s không chữ. Vùng chuyển f53–63 hòa chồng hai vị trí mặt | Waveform gần nguồn không bù lỗi caption/hình chồng. Không đề nghị chọn nguyên bản |

Không có mẫu được nhận đã đạt toàn bộ brief. Số đo waveform/PCM khác không tự chứng minh đổi giọng, và correlation cao không thay actual hearing. Đặc biệt B không giữ waveform ở đúng thời điểm nguồn trên mọi đoạn đã đo; không dùng approval201/203 cũ để đóng việc này.

Nguồn diagnostic vẫn có ụ món rộng/sáng và nền/khung khác TABLE08. Phép thử này chưa khóa variation làm production anchor; không đổi canon của toàn tập từ approval30credit. Cần xử lý/chốt riêng khi hoàn thiện G1 toàn tập.

### Bản B cần nghe/xem đúng file

![N02 B — chưa nghiệm thu](C:/Users/PC/Downloads/du_an_nem_bui/221_n02_pa_v_trial/N02_B_NATIVE.mp4)

Đối chứng tiếng đã duyệt ở nguồn200/201:

![N02 nguồn — đối chứng tiếng đã được chấp nhận](C:/Users/PC/Downloads/du_an_nem_bui/200_n02_replacement/N02_NATIVE.mp4)

Owner cần nghe/xem **toàn B**, chú ý6,25–10s: đúng một giọng Khoai/K20 xuyên lượt, nguyên văn câu dài, nhịp/âm cuối tự nhiên, miệng người nói phù hợp và Đào nghe không nói thay. Nếu có lỗi, chỉ rõ timecode. Đây là phần human checkpoint do reviewer không có actual hearing/fullAV, không phải giao owner làm lại audit file/nguồn/hình đã được sàng lọc.

B trở về khung hai người tại7s thay vì giữ cận đến sau từ cuối như brief PA-V. Nếu sau kiểm AV vẫn có mặt người nói rõ và nhịp tốt, có thể **đề xuất** owner chấp nhận cách coverage này cho N02; chưa tự coi deviation đó được duyệt. Không chồng WAV cũ, retime hoặc crop để lách kiểm.

Các native khác để đối chiếu khi cần: [A](C:/Users/PC/Downloads/du_an_nem_bui/221_n02_pa_v_trial/N02_A_NATIVE.mp4), [C](C:/Users/PC/Downloads/du_an_nem_bui/221_n02_pa_v_trial/N02_C_NATIVE.mp4). Folder có đủ originals, WAV review và toàn240frame mỗi output: `C:/Users/PC/Downloads/du_an_nem_bui/221_n02_pa_v_trial/`.

## Bằng chứng và bài học đã lưu

- [SIA — đo âm thanh độc lập](evidence/221/01_sia-output-review.md): hash/probe/PCM, global/local alignment; actual hearing/identity/lip-sync HOLD.
- [CONT — continuity ảnh độc lập](evidence/221/03_cont-output-review.md): xem60thumbnail và30fullframes; không gọi sampled frames thành fullAV.
- [Picture coverage — kiểm hình độc lập](evidence/221/02_picture-coverage-review.md): biên cut native, mặt/miệng/gaze/listener lấy mẫu và C blend/caption; không áp ASR nguồn vào lời đầu ra mới.
- [Nhật ký root](evidence/221/04_root-run-and-download-readback.md): pre/post-submit, download timeout nhưng file thực đã lưu, cách đối soát trước retry và khôi phục phiên reviewer. Root đã đọc đầy đủ ba báo cáo độc lập, chưa có actual hearing/fullAV PASS.
- [Đối soát kỹ thuật](evidence/221/technical-inspection.json): native/hash/probe/audio. Mỗi output trích đủ240frame và WAV, không sửa nguồn.
- Board cũ dùng `fps=2` không có mapping exact frame tại mọi nhãn. Đã lưu thêm `contact-exact-native-0.5s.png`, chọn nativeframe0,12,…228 tại24fps; giữ evidence cũ. Biên lỗi trên đây dùng nativeframe, không dùng thumbnail resampled làm onset chính xác. Inspector đã sửa cho lần sau.

Skill computer-use hỗ trợ kiểm cấu hình, gửi đúng một batch và tải media qua UI. Kiểm local sau tải phát hiện event timeout không là download failure; không tái sinh video để lấy file. Không sửa tài khoản, watermark hoặc source. Không commit/push trong run này.

## Tổng hợp vòng và bước tiếp

- **Đã xác định:** batch30 thực có ba native; A/C có blocker hình, B sửa được food-only coverage trong mẫu nhưng chưa bảo toàn timing nghiêm ngặt/kiểm AV.
- **Đã chốt:** quyền chạy đã dùng hết đúng scope; lời C-v0.6, K20/D06 và storyboard214 vẫn giữ. Chưa chọn output cuối hoặc mở Quality.
- **Giả định đang kiểm:** sửa video có thể giữ cảm nhận giọng đã chọn; acoustic similarity hỗ trợ quan hệ nguồn nhưng không đủ duyệt nghe.
- **Còn mở:** owner nghe/xem B, chấp nhận hay sửa return7s, production-anchor variation và fullG1; chưaG2PASS hoặc full-filmPASS.
- **Tiếp:** owner checkpointB, gồm voice/lời/nhịp/khẩu hình và disposition của coverage. Duyệt tiếng riêng chỉ đóng phần tiếng đã được nghe; không tự đóng gaze/continuity/acting hoặc anchor variation. Khi N02 đủ bằng chứng đúng scope mới tiếp phần phụ thuộc. Nếu không, trình phương án/giá trước request mới. Không tự chi77credit còn lại.
