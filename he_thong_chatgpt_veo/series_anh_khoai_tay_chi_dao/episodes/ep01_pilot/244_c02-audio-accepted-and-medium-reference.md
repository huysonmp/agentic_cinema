# REC244 — Chốt tiếng C02 và chuẩn bị khung cận vừa

Ngày 07/10/2026. Owner xác nhận **“Đúng K20, lời và nhịp chấp nhận được”**, riêng audio của C02 T01, hash `5ba2878f…`. Không gộp thành duyệt phần hình đang REWORK. Không chuyển acceptance này sang tiếng sinh lại trong tương lai.

## Đã làm tiếp

- Ghi đúng phạm vi nghe tại `00_decisions/C02-audio-approval-244.json`. Không tuyển lại giọng, đổi lời hoặc sửa script theo lỗi ASR “Giang Gạo”.
- Đổi tên scene Flow thành **EP01_QC_C02_T01 — CHƯA DUYỆT HÌNH**, đã đọc lại tên lưu thực. Không xóa native hoặc scene kiểm.
- Dùng tuyến ảnh ChatGPT đã được cho phép để chuẩn bị reference cận vừa riêng C02 từ master v5. Một lượt ảnh, không sinh video thứ hai hoặc dùng credit Flow.
- Đã lưu ảnh mới, tính hash và xem native: hai mặt lớn hơn, bỏ phần chân/bàn dưới; còn đúng phố mở, đèn lồng và mái bạt; tay nghỉ, môi khép. Một số props ở ngoại vi bị cắt vì coverage gần, không dời vị trí scene.
- Review độc lập đã hoàn tất: PASS_FOR_HANDOFF_STATIC, không thấy lỗi lớn trong ảnh tĩnh đã xem. Root đọc toàn báo cáo khi tiếp tục ở REC245. Đây không phải duyệt video hoặc duyệt thay owner.

## Đầu ra và ranh giới

Ảnh: `02_refs/C02_MEDIUM_v1_CHATGPT_NATIVE.png`, hash `c0ec77283233b4b4f49c172697f8c7b42fd2a7cc4bf3960670723b1a871fd0a7`, 941×1672. Bản owner trong folder 
`C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/02_refs/`.

Đây là **shot-specific reference**, không thay master đã duyệt hoặc yêu cầu mọi shot đều cận. Prompt nguyên văn tại `02_refs/C02_medium_reference_244.txt`; request tại `04_requests/C02_medium_reference_244.json`.

Giả định làm việc: reference thể hiện camera trực tiếp sẽ giảm việc video tự diễn giải lại bố cục. Đây là giả thuyết sửa có mục tiêu từ lỗi T01, không dự báo chắc chắn đạt. Vẫn cần kiểm actual take mới về nền, tay, mặt, tiếng và khẩu hình.

## Bước tiếp

Đóng review khung tham chiếu; cập nhật request retake chỉ diễn mắt/đầu/miệng nhẹ, giữ nguyên camera/nền/tay. Trước gửi phải kiểm đúng ảnh/voice/quote ≤15 và quyền ngân sách. Chưa chạy retake; còn 485 trong trần 500, số dư Flow quan sát 1.035. Không mở C01A từ một C02 hình chưa đạt.

Skill [imagegen](C:/Users/PC/.codex/skills/.system/imagegen/SKILL.md) định hướng sửa một biến và giữ invariants từ v5. Ảnh thực tạo bằng built-in, không CLI/API. Skill [computer-use](C:/Users/PC/.codex/plugins/cache/openai-bundled/computer-use/26.1002.51308/skills/computer-use/SKILL.md) dùng để kiểm trim/export và lưu nhãn QC thực.
