# REC296 — Review độc lập hai ảnh nháp tư thế nhận–cho

Ngày 13-10-2026. Reviewer `food_repair_critic_283`, bounded local REC217. **ACTUAL_FULL_STILL_INSPECTION + PAPER / POSE_CANDIDATES_REVIEWABLE_WITH_CAVEATS.** Không imagegen/browser/API/scripts/media-edit/voice/EDL/git/paid. Không actual physics, acting B, voice hoặc video continuity PASS.

## Evidence thực

Đọc đầy đủ approval296, state map295 và `04_requests/receiver-pose-imagegen-prompts-296.md`. Trực tiếp xem toàn base v3, P1v1, P1v2 và P2v1. Owner cấp **chuẩn hai ảnh nháp**, không tự nghiệm thu chúng hoặc paid video. File dưới `02_refs` trong restart:

- Base `C06_ENTRY_LOCAL_v3_FOR_REVIEW_291.png`,720×1280: source-derived entry đã duyệt.
- `RECEIVER_P1_v1_NOT_SELECTED_296.png`: lịch sử không chọn.
- `RECEIVER_P1_v2_FOR_REVIEW_296.png`: bát nhận rỗng gần A, v2 sau sửa gaze.
- `RECEIVER_P2_v1_FOR_REVIEW_296.png`: bát có A, tips trống/rút.

Hash kiểm trực tiếp qua filesystem trong run này: base `7c8023cbe655745b941e1a47dd1df3614ba66fcef512a41c5c4c4048bb33f8cc`; P1v1 `3c2a6146d2af7a0f0aaaa1de3e3da13274b258be596ec01a0f1d4c9fa786483c`; P1v2 `1eff2b05e8fa423b7499ab48114800a0d1e667641497deb2a3b30a2cc2ec54f8`; P2v1 `fe60f3fabf1297810c4457d2adf4b24aa77b6d4c671e2a16cca62266ffe57474`. Root cần gắn exact candidate hashes vào owner checkpoint/registry. Ba ảnh sinh 941×1672 là redraw, không pixel-locked base720×1280; review này không crop/resize/registration.

## Findings

| Scope | Observed / disposition |
| --- | --- |
| **P1v1→v2 gaze** | V1 Khoai chú ý vùng A/bát nhiều hơn, v2 mắt hướng Đào rõ hơn và giữ môi khép; root ghi v1 không chọn. Không chấm gaze v2 là ACT B đạt từ still. Giữ chỉ v2 khi trình cặp pose. |
| **P1 S2** | Đào dùng tay trong nâng bát rỗng sang trái màn hình; cốc vẫn tay ngoài phía phải. A nhỏ còn trên đôi đũa, nằm cao hơn mép bát/vùng lòng, chưa thấy nem trong bát. Đích nhận đọc rõ hơn ảnh START282; không thêm pickup hoặc nhận bằng bát Khoai. |
| **P2 S3** | Bát cùng người nhận có phần nhỏ dưới lòng, tips trống ở trên/trái và tách khỏi A. Không A còn trên đũa đồng thời nhân bản trong bát. Đây ý nghĩa đã nhận, không chứng minh release một lần hoặc giữ mass từ P1. |
| **Bát–tay Khoai** | Bát Đào gần và ở phía trên tay trong Khoai đang nghỉ, có overlap theo projection; vùng hở/clearance dưới đáy khá sát, nhất là P2. Tay Đào vẫn đọc là tay đỡ bát, không rõ là bát đặt lên tay Khoai, nên chưa kết luận lỗi contact MAJOR. **Caveat**: actual path/pose source tiếp theo phải giữ clearance rõ, không ép depth từ một still. |
| **Cốc/bát/đĩa chung** | Cốc nâng tay ngoài và ngoài lòng bát nhận; bát Khoai riêng còn rỗng trên bàn. Đĩa chung dưới/trước vùng nhận, không là target deposit của P2. Rau/lá, hai chấm và đũa Đào ngoài phải còn. Không thấy đổi tay hoặc cốc trong bát. |
| **Food quantity/material** | Đĩa có thịt/bì/thính, không smoke/slabs đồng dạng. A P1 nhỏ và P2 trong bát là phần nhỏ, không mound tự tăng lớn. Không đo gram/volume, từng ribbon conservation hoặc giới thiệu công thức/cách dùng duy nhất từ các ảnh. |
| **Identity/clothes/base drift** | Vẫn Khoai/Đào, vest tối/blouse trắng/váy xanh; không yếm xanh lỗi286. Cả hai mặt và vùng thao tác hiện rõ. Tuy nhiên mặt/mắt/material/sharpness, framing/background và position tay/đũa/A đã redraw so base. Khoai outer hand/tips đọc cao/xa hơn base; P1 không exact same pose cần kế thừa. Không nối base→P1 bằng giả định pixel/geometry giữ. |
| **P1v2→P2 layout** | Bố cục/table/character pose tương đối gần; bát P2 có thay hình/vị trí nhỏ và đũa rút theo phase, là thay đổi được thiết kế. Không exact-camera/body/hand measurement hoặc seam guarantee. |
| **Provenance/platform mark** | Sao ở đáy phải có trong ảnh sinh, không bằng chứng đó là native Flow frame hoặc same source pixels. Ghi đúng ChatGPT-generated pose refs; source v3 không đổi. Không giả mạo native provenance bằng việc giữ biểu tượng. |

Không thấy lỗi rõ MAJOR trong cặp **v2/P2v1 về ý nghĩa S2/S3** khiến phải bác toàn pose draft. Nhưng nguyên tắc giữ base exact chưa đạt vì imagegen redraw là giới hạn đã khai; approval pose không được biến thành approval tất cả drift hoặc final reference binding.

## Đề nghị trình owner đúng scope

Trình **P1v2/P2v1 về cách đưa đúng bát riêng rỗng gần A, rồi A trong bát/tips rút**; nêu caveat bát sát tay Khoai và redraw/pose khác base. Không hỏi lại sắc tháiB/giọng, không đưa P1v1 như một option đã sàng lọc đạt. Nếu owner chốt pose, đó là direction/reference scope, không video hoặc pixels seamless.

S1 thật cần lấy từ C06 mới được chọn; S2 thật từ nhịp Đào nếu tách, như state map295. Hai ảnh nháp hiện không đủ làm cặp Frames endpoints production hoặc jump khỏi speaking source. Live route/voice/quote/bounded request còn cần gate riêng; Inputs/Frames không tự kết hợp savedvoice. Không need guarantee trước sinh, nhưng phải nói rõ actual middle/contact/voice unknown và kiểm output sau owner request approval.

Chưa trả phí, thay source/EDL hoặc đóng FOOD cũ/timing30s. Cặp still không tự chứng minh N07 có khẩu hình hoặc action4s đủ ending.

**FINAL: P1v2_AND_P2v1_POSE_REVIEWABLE / CLEARANCE_AND_REDRAW_CAVEATS / OWNER_OUTPUT_ACCEPTANCE_PENDING / NO_MEDIA_OR_PAID_GO.**
