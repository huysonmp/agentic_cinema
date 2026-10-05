# EP01 — Thêm SIA-01 và chặn nguồn chưa kiểm đúng người nói

Ngày2026-10-05. Owner: “làm sao để không bị lỗi này, hãy thêm agent check cái này đi”. Đã triển khai scoped agent/check gate, không chỉ viết đề xuất. Không sinh lại hoặc sửa giọng trong lượt này.

## Đã bổ sung

- [SIA-01 — Speaker Identity & Turn Auditor](../../agents/audio_edit_quality/10_speaker-identity-auditor-v1.md): vai độc lập maker, chuyên câu/người nói/giọng chuẩn/nhân vật trên hình. Không thay AV-VOICE về độ ấm, accent hoặc diễn; không tự phát hành.
- `scripts/ep01_speaker_gate.py`: chuẩn bị request bound script/package/source/range; kiểm evidence/report, từ chối thiếu/stale/wrong vai, file chuẩn sai hoặc không có audio. AV scope yêu cầu target thật có video+audio, timeline trong duration, full AV review và từng lượt sync/offscreen approved.
- `scripts/build_ep01_c_v06_assembly.py`: bắt buộc `--speaker-review` đúng nguồn và AUDIO_SELECTION PASS. Muốn dựng nháp chưa kiểm phải chỉ định `--allow-unverified-planning`, hình có nhãn CHƯA KIỂM VAI/GIỌNG, manifest giữ HOLD. Lệnh cũ bị chặn trước render. Builder vẫn chỉ tạo PLANNING, không có chế độ master.
- Caption metadata mới ghi `expected_speaker`, không gọi vai từ script là kết quả observed. Script audit183 tương thích tên cũ/mới. Media182 không bị thay; bản cũ vẫn chưa đạt speaker gate theo183.
- Contract02/log01 của AEQ đã nối DLG-EDIT → SIA nguồn, AV-CUT/EDIT → SIA bản ghép, MASTER → SIA final. Chưa có khóa tự động cho mọi công cụ khác; ngoài builder được hook, điều phối phải thực hiện gate theo contract.

## Quy tắc ngăn lặp lỗi

1. Audition approved chỉ khóa K20/D06, không nghiệm thu mọi output dùng hai token. Approval “giọng tạm được” không thay kiểm vai từng lượt.
2. Nghe/so mẫu từng lượt và toàn câu, đặc biệt N02 có đổi voice giữa câu không; kiểm nói chồng. Không tự điền observed=expected hoặc dùng ASR/peak/hash làm identity PASS.
3. Sai có bằng chứng → REWORK phần tương ứng. Chưa nghe/reference → HOLD, không khẳng định đã tìm được câu sai.
4. Report độc lập gắn đúng bytes/range/version. Đổi take/cut/mix/source range → kiểm lại, không tự thừa kế QC.
5. Trước chọn nguồn, sau ghép và trước bàn giao là ba scope riêng. Audio PASS không tự thành môi đúng người; final SIA PASS không thay QC khác/owner approval.
6. Sinh chung lẫn vai lặp lại → đề xuất chỉ một vai nói mỗi lượt hoặc stem riêng nếu công cụ hỗ trợ. Chưa chạy; vẫn kiểm nguồn/bản nối. Không chọn lại giọng đã chốt hay đổi pitch để giả giọng chuẩn.

## Thử và phản biện thực tế

- **39/39** unittest synthetic PASS: ASR-only/anonymous diarization, missing hearing/reference, wrong voice/role/text, đổi giọng giữa câu/nói chồng, stale hash/range, malformed schema/package, fake audio/AV, self-review, audio-only final, offscreen thiếu approval, duration và builder thiếu flag/review. WAV/AV test là synthetic, không audition/kiểm chất giọng thật.
- **5/5** tests ghép source cũ PASS; scripts mới/sửa qua py_compile; diff check sạch.
- Root integration builder với report183 chưa xác minh: bị SIA chặn trước mkdir/render; không tạo output.
- [Source-request](evidence/184/source-request.json) actual7 lượt A03/R01 và [kết quả gate](evidence/184/current-source-gate.json) khi thiếu review identity: **HOLD_FOR_INPUT**, defects=[], release_authorized=false. Đây là thử chặn, không nhận diện voice thực tế.
- Reviewer độc lập `/root/speaker_gate_critic` phản biện code/contract và chạy capability-first trên bộ thật: [report07](../../agents/audio_edit_quality/reports/07_sia-01-capability-and-gate-review-r1.md). Không có nghe actual trong run này.

Lỗi gate được phát hiện/sửa qua tests và critic: duplicate observations zip sang line khác gây false REWORK; WAV hỏng gây EOFError thay HOLD; bool schema/package array thiếu type guard; target AV chỉ hash từng nhận file text. Đã thêm hồi quy từng nhóm. Bài học: thử positive case không đủ, phải kiểm input thiếu/sai/giả để ngăn PASS không có căn cứ.

## Cách chạy local

Từ root repo, `python scripts/ep01_speaker_gate.py prepare --package <package.json> --manifest <manifest.json> --out <request.json>` tạo AUDIO_SELECTION request. Reviewer có nghe/reference thực trả JSON theo contract10; `python scripts/ep01_speaker_gate.py check --request <request.json> --review <review.json> --out <gate.json>` kiểm. Không có review thì HOLD, CLI không-PASS trả mã lỗi; ghi file không đồng nghĩa đạt.

Scope AV thêm `--mode AV_ASSEMBLY` hoặc `FINAL_AV` và `--target <actual-cut.mp4>` lúc prepare. Không ghi đè output cũ, không dùng report fixture làm approval EP01. Bản tạm có flag riêng vẫn là PLANNING_NOT_DELIVERY, không được đổi nhãn thành master.

## Điều chưa hoàn tất

Đây là **agent contract + evidence validator + workflow guard**, không phải mô hình nghe/nhận dạng giọng đã tích hợp. Máy kiểm cấu trúc/hash/file không xác minh lời khai reviewer có thật sự nghe; cần reviewer có năng lực nghe, log thật và human control. Chưa có local reference K20/D06 và acoustic review; bảy lượt vẫn chưa xác minh identity. Không hứa ngăn100% lỗi sinh, chỉ chặn output chưa kiểm đi qua như đã đạt.

Chi0, không browser/API/install/generation hoặc sửa audio/Quality. Sổ202/255, còn53; account224 chỉ snapshot182, chưa đọc live lại. Không yêu cầu owner tuyển giọng lại.

## Tổng kết vòng

- Đã xác định: thiếu gate người nói tại chọn nguồn; nay có role độc lập và chốt chặn cụ thể.
- Đã chốt: thêm SIA-01, giữ K20/D06/C-v0.6; ASR/metadata không thay nghe, planning ngoại lệ phải explicit.
- Giả định: reviewer trung thực, có bằng chứng thực; code không tự nghe; actor và voice có thể sai riêng.
- Còn mở: audio reference đúng preset, năng lực nghe/identity, các câu sai thật và bản ghép đạt.
- Tiếp: hoàn thiện mẫu chuẩn/phương tiện nghe để chạy SIA actual, sửa đúng lượt lỗi rồi kiểm AV. Chưa Quality/bàn giao từ fixture PASS.
