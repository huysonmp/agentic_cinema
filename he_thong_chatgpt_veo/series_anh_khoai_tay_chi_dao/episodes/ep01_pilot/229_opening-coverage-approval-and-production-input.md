# 229 — Duyệt coverage mở và chuẩn bị nguồn sản xuất R01

Ngày2026-10-07. Trạng thái: **COVERAGE_APPROVED / PRODUCTION_INPUT_PREPARED / FLOW_RIGHTS_CONFIRMATION_PENDING / NO_GENERATION**.

## Quyết định đã chốt

Owner trả lời “ok” cho đề xuất ở228: chỉ thay hình quanh “Khoan” để thấy Đào nghe→dừng→thu tay; giữ nguyên tiếng Khoai và phần kể ký ức đã duyệt sau đoạn mở. Không đổi C-v0.6, K20/D06, chuẩn B hoặc món/bàn. Original B được giữ nguyên để đối soát. Approval này không nghiệm thu picture/join mới và không cấp thêm credit, Quality, retry hoặc batch thử tay.

Theo228, làm footage phục vụ phim rồi QC; không quay lại bài test tay riêng hoặc x3. Theo215/217, mỗi request cần route/quote/inputs cụ thể và approval chi riêng trước submit.

## Đã làm thực

- Chạy nhận dạng tiếng Việt local offline trên exact B; không API/cài mới. ASR định vị “Khoan”0–0,34s và từ tiếp khoảng1,10s; FFmpeg đo khoảng dưới ngưỡng im lặng0,364292–1,209979s. Đây là locator, không thay việc nghe hoặc quyết định voice. ASR nhầm “rang” thành “gian”; giữ nguyên diagnostic, không sửa thoại đã duyệt.
- Rehash A03, N01 excerpt, B native và B PCM; khớp nguồn. Tạo WAV exact N01[0;103200)+B[0;48000) ở48kHz/stereo, tổng3,150s, đối soát từng sample. Không dùng full A03 audio hoặc old N02 từ WAV202.
- Tạo guide4,000s/96frames/360×640 để đưa tuyến video-edit.0,85s cuối là đệm im/giữ hình, **không phải beat được thêm vào master**. MP4 dùng AAC để upload; exactPCM sidecar giữ riêng. Guide không phải phim: hình N01 cũ sai bộ bàn và có mouth cue sai; cut thô không phải hành động được chấp nhận.
- Xem contactboard guide, S, Bf21 và Bf24. S/M/E có nhiệm vụ khác nhau; M là pose giữa, E chỉ rest-hand pose. Prompt yêu cầu bỏ mouth motion sai của guide và dựng đúng speaker từ audio; không dùng hình người im để che thoại.
- Kiểm UI Flow: Ingredients/Omni1.1 Flash/360p/4s/x1; đã chọn upload guide. Flow dừng ở hộp xác nhận quyền sử dụng video. Đã hỏi owner tại thời điểm hành động, **chưa bấm “Tôi đồng ý” hoặc submit generation**. Quote khi đủ video/refs chưa được xác minh.

## Điểm nối và kiểm tiếp

Boundary picture làm việc là Bframe24/1,000s; provisional, không xác nhận bằng actual hearing/AV mới. Sau sản xuất, picture R01 dự kiến dùng đến2,150+tB rồi nối B tại chính tB; không thêm0,85s pad vào giữa hai câu. Toàn B PCM chạy liên tục đúng một lần từ đầu N02, không cắt/retime/lặp “Khoan”. Chỉ dùng picture mới nếu miệng, nghe–dừng–thu tay và join đạt trên đúng output.

Chuyển từ khung S sang B có khác scale/gaze; output thực phải kiểm cut không nhảy tay/đảo trục hoặc mất nhịp. Reference đẹp hoặc sourceB được222 chấp nhận không tự duyệt join mới. Chưa G1/full AV/30s/master PASS.

## Hồ sơ và giới hạn

- Approval: [owner-coverage-approval.json](evidence/229/owner-coverage-approval.json).
- Nguồn/hashes/ranges: [source-manifest.json](evidence/229/source-manifest.json).
- Brief/prompt: [preparation-notes.md](evidence/229/preparation-notes.md), [R01-production-prompt-DRAFT.txt](evidence/229/R01-production-prompt-DRAFT.txt).
- Nguồn local: `C:/Users/PC/Downloads/du_an_nem_bui/229_r01_production_input/`.
- Script: `scripts/prepare_ep01_rec229_opening_source.py`; compile thành công, guide probe4s/96frames, WAV read-back khớp samples. Originals không sửa; output directory không ghi đè.
- Hai vai maker DIR/EDIT/DLG và critic CONT/DOP/ACT đã chạy preflight local độc lập: [maker](evidence/229/01_maker-preflight.md), [critic](evidence/229/02_independent-preflight.md). Cả hai kiểm6/6 source/artifact hash và PCM samples; chưa hearing/continuous AV. Root đọc toàn reports và sửa mouth attribution, E hierarchy, reach khởi đầu sớm trong vế thoại, yêu cầu tay về nghỉ trước3s để có biên nối, bỏ padding khỏi master và giữ native watermark. Route/quote/output AV còn HOLD/NOT_RUN; không nghiệm thu sản phẩm chưa sinh.

Chi lượt229:0; số dư gần nhất đã kiểm ở228:77. Không nhận forecast7×10=70 là quote hoặc bảo đảm đủ tiền để hoàn tất.

## Tổng hợp vòng

Đã xác định: nguồn mở đúng N01+prefixB và rủi ro guide/mouth/join. Đã chốt: thay picture prefix, giữ tiếng B/phần ký ức; production rồi QC. Giả định: video-edit có thể nhận guide+refs và sửa đúng audio-driven action; chưa chứng minh output. Còn mở: hộp quyền upload, route/quote với đủ đầu vào, preflight và approval chi; sau đó output/AV/join. Bước tiếp: xác nhận hộp quyền, kiểm quote cho **một** request R01, trình đúng khoản đó trước tạo, rồi kiểm sản phẩm — không mở batch thử.
