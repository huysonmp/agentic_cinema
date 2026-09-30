# Quality-agent design proposal v0.1

- **Project:** `he_thong_chatgpt_veo / series_anh_khoai_tay_chi_dao`.
- **Purpose:** trình owner duyệt thiết kế các agent/checker bổ sung cho chuỗi chất lượng; chưa chạy production.
- **Status:** `OWNER_APPROVED — OPTION A` ngày 2026-09-30; implementation contracts chưa hoàn tất.
- **Scope:** EP01 pilot trước, sau đó mới mở rộng thành SOP cho 10 tập.
- **Owner authority:** owner duyệt claim, concept/script, generation spend, asset rights, exception và release. Không agent nào tự approve cuối.

## 1. Vì sao thiết kế theo agent + checker

Các lỗi khác nhau cần bằng chứng khác nhau. Một reviewer sáng tạo không nên tự xác nhận quyền ảnh; một fact auditor không nên quyết định câu thoại hấp dẫn; một checker kỹ thuật không nên sửa canon. Vì vậy gói này tách:

- **Agent suy luận:** Cultural Context, Flow/Veo Feasibility, Rights/Provenance.
- **Agent review chất lượng:** Continuity, Audio–Caption–Accessibility.
- **Checker định lượng:** Master/Platform QC.

Tất cả dùng cùng status contract, evidence record và human gate.

## 2. Contract chung cho mọi role

### Input envelope

Mỗi run phải ghi: `run_id`, ngày/giờ, stage, artifact/version đầu vào, owner decisions đang có hiệu lực, rubric version, reviewer role, và những file/asset không được đọc vì blind boundary.

### Finding envelope

Mỗi phát hiện phải có:

`finding_id → severity → artifact/version → line/beat/time/frame/asset → expected rule → observed issue → evidence → impact → recommended action → route → owner decision needed`.

Không chấp nhận kết luận chỉ có điểm số hoặc “cảm giác chưa ổn”.

### Status

- `PASS_FOR_NEXT_GATE`: đủ điều kiện chuyển stage trong phạm vi đã kiểm.
- `PASS_WITH_ACTIONS`: được chuyển nhưng phải hoàn thành action đã ghi trước gate kế tiếp.
- `REWORK`: quay lại maker/agent đúng stage.
- `BLOCKED`: thiếu input, quyền, evidence hoặc lỗi hard-boundary.
- `ESCALATE_HUMAN`: cần owner, cultural reviewer, rights specialist hoặc người đọc/nghe thật.

### Authority rule

Agent chỉ recommend/status trong scope. `BLOCKED` ngăn chuyển stage cho tới khi owner ghi exception hoặc defect được đóng; nó không tự sửa file gốc và không tự biến recommendation thành approval.

## 3. Agent 1 — Cultural Context & Sensitivity Reviewer

- **ID:** `AG-CULT-01`.
- **Stage:** P2/P3/P5; chạy lại khi script/hình thêm claim văn hóa mới.
- **Mục tiêu:** phát hiện diễn giải văn hóa sai mức, giản lược, áp đặt một phiên bản duy nhất, gán nhãn vùng/địa danh không chắc chắn hoặc hài hước gây định kiến.

### Input

P2 research pack + claim register; script/caption/visual brief; source spans; conflict log; P1 audience/risk boundaries; asset descriptions.

### Công việc bắt buộc

1. Gắn từng câu/hình vào `FACT`, `ANECDOTE`, `OPINION`, `HUMOR`, `FICTIONAL_DEVICE`.
2. Kiểm câu có nói mạnh hơn nguồn, có biến một lời kể thành lịch sử chắc chắn, hoặc biến một vùng/nhóm thành tính cách chung không.
3. Kiểm tên địa phương, quan hệ món–nơi, cách gọi món và những phiên bản diễn giải khác nhau.
4. Tách “có nguồn” khỏi “được cộng đồng xác nhận”; không đếm bài đăng lại thành nguồn độc lập.
5. Kích hoạt `ESCALATE_HUMAN` nếu có nguồn mâu thuẫn trọng yếu, nội dung nghi lễ/identity nhạy cảm, hoặc cần người địa phương xác nhận cách diễn đạt.

### Output

`cultural_review_report.md` gồm claim/visual matrix, safe wording, excluded wording, risk severity, human-review trigger, source gaps và route P2/P3/P5.

### Quyền block

Block nếu script dùng claim văn hóa vượt evidence, gán một dị bản là duy nhất, hoặc dùng hình/đùa tạo định kiến mà chưa có quyết định xử lý.

### Không được làm

Không tự nhận là đại diện cộng đồng; không cấp quyền dùng ảnh/người/địa điểm; không thay Fact Auditor về độ xác thực nguồn.

## 4. Agent 2 — Flow/Veo Feasibility & Shot Planner

- **ID:** `AG-FLOW-01`.
- **Stage:** P7 trước prompt, P8 trước generation; re-check khi đổi model, độ dài, ingredient hoặc voice.
- **Mục tiêu:** biến script đã khóa thành kế hoạch clip/generation có thể làm trong Flow/Veo, giảm yêu cầu mâu thuẫn và phát hiện điểm không thể kiểm soát trước khi tiêu credit.

### Input

Script version + timing target; character sheets; food reference pack; environment/style references; voice policy; output spec; available credit/budget; current Flow model/features.

### Công việc bắt buộc

1. Chia video thành shot/clip với thời lượng, action, camera, dialogue, start/end state và transition.
2. Chỉ rõ ingredient/reference nào bắt buộc cho mỗi shot: Khoai, Đào, món, đạo cụ, background, voice.
3. Kiểm hành động dễ lỗi: hai người cầm/gắp/chia món, lip-sync, camera move, hand continuity, food transformation, text overlay và voice timing.
4. Kiểm prompt conflict: reference nói một kiểu nhưng text prompt nói kiểu khác; nhiều chủ thể/hành động không thể cùng giữ continuity.
5. Lập phương án `A/B` khi shot fail và điểm dừng credit; không tự gọi generation.
6. Ghi rõ điều cần thử bằng một probe nhỏ trước khi tạo cả sequence.

### Output

`flow_shot_plan.md` gồm shot ID, duration, prompt intent, ingredients, voice, start/end frame, join risk, expected failure, probe, estimated generation count và owner approval point.

### Quyền block

Block generation nếu thiếu reference canon, shot yêu cầu hành động không kiểm soát được, model không hỗ trợ feature cần dùng, hoặc credit/cost chưa được owner xác nhận.

### Không được làm

Không tự viết lại premise để “dễ cho Veo”; không coi một clip đẹp đơn lẻ là continuity pass; không tự chi credit.

## 5. Agent 3 — Character–Food Continuity Auditor

- **ID:** `AG-CONT-01`.
- **Stage:** P6 reference approval, P8 batch review, P10 final visual review.
- **Mục tiêu:** bảo đảm character canon, food identity và state continuity không trôi giữa các shot.

### Input

Approved P1/P6 character sheets; voice/style lock; food reference/fidelity notes; Flow shot plan; generated images/videos; previous accepted frame/clip; asset register.

### Công việc bắt buộc

1. So sánh khuôn mặt, silhouette, màu/texture, biểu cảm, tay, trang phục, đạo cụ và voice cue của Khoai–Đào với canon.
2. So sánh hình dạng, màu, cấu trúc, phần đã gắp/cắt, thính/lá/đĩa và vị trí món qua shot; phân biệt “biến đổi có chủ ý” với lỗi continuity.
3. Kiểm screen direction, eyeline, hand ownership, camera axis, lighting/style và background.
4. Đánh dấu frame/time cụ thể; không dùng “nhìn hơi khác” không có vùng đối chiếu.
5. Đề xuất correction prompt hoặc re-generate đúng shot, không sửa âm thầm canon.

### Output

`continuity_report.md`, frame comparison, defect severity, repair prompt, disposition từng clip và residual risk.

### Quyền block

Block nếu nhân vật không nhận ra, món bị biến thành món khác, hành động liền trước/liền sau không nối được, hoặc sửa cần thay canon nhưng chưa có owner decision.

### Không được làm

Không phê bình sức hút/kịch bản; không “chữa” lỗi bằng cách làm món đẹp hơn nhưng sai reference.

## 6. Agent 4 — Rights, Provenance & AI-Disclosure Auditor

- **ID:** `AG-RIGHTS-01`.
- **Stage:** P6 asset intake, P8 generation references, P11 release package.
- **Mục tiêu:** bảo đảm asset, người, địa điểm, nhãn hiệu, nguồn tham chiếu và disclosure được truy vết và có phạm vi sử dụng rõ.

### Input

Asset/source register; uploaded references; prompt/ingredient history; generated master; music/voice records; owner IP policy; TikTok disclosure plan; project AI disclosure text.

### Công việc bắt buộc

1. Phân loại asset: original project asset, owner-provided, public/unknown, licensed, source-only research, generated.
2. Cấm dùng source photo/video/person/brand làm reference production khi chưa có quyền/định danh và quyết định owner.
3. Kiểm attribution/permission, people/likeness, brand/location appearance, music/voice terms và derivative risk.
4. Kiểm visible disclosure trong video/caption và platform AIGC setting; ghi rõ cái nào là project disclosure, cái nào là platform label.
5. Lưu provenance manifest: source asset ID, transformation, tool/model, date, operator, output ID, replacement/exception.

### Output

`rights_disclosure_report.md`, asset disposition matrix, missing-permission list, disclosure verification, provenance manifest và release recommendation.

### Quyền block

Block release nếu asset/voice/likeness/right unknown trong phạm vi cần dùng, disclosure bắt buộc chưa bật/không thể xác nhận, hoặc output làm người thật/nhãn hiệu xuất hiện ngoài scope.

### Không được làm

Không đưa ra kết luận pháp lý tuyệt đối nếu không có legal specialist; không coi watermark/provenance là bằng chứng nội dung đúng.

## 7. Agent 5 — Audio–Caption–Accessibility QC

- **ID:** `AG-AV-01`.
- **Stage:** P6 voice test, P9 audio/caption, P10 final media review.
- **Mục tiêu:** kiểm tiếng Việt nghe tự nhiên và hiểu được, caption không làm sai claim, audio–visual–text đồng bộ và người xem không bị mất ý chính khi tắt tiếng.

### Input

Rendered video; isolated dialogue/music/SFX; final script and claim IDs; pronunciation/name list; caption file/text; voice reference; AI disclosure text.

### Công việc bắt buộc

1. Kiểm phát âm Nem Bùi, Bùi Xá, Bắc Ninh, thính và tên nhân vật; đánh dấu timecode.
2. Kiểm Khoai/Đào có đúng voice canon, nhịp hơi, ngữ điệu, overlap, lip-sync và emotion không.
3. Kiểm caption: đúng từng câu đã duyệt, không rút qualifier làm claim mạnh hơn, timing/line-break/readability/safe zone.
4. Kiểm audio mix: thoại nghe rõ, nhạc/SFX không che, không clipping, silence/pause có chủ ý.
5. Chạy `sound-off` và `audio-only` pass; ghi phần nào mất nghĩa và có cần text/transcript/visual alternative không.

### Output

`audio_caption_qc.md` với timecoded defect list, corrected caption candidate, pronunciation notes, sound-off/audio-only result và disposition.

### Quyền block

Block nếu caption làm sai claim, tên/địa danh nghe sai nghiêm trọng, disclosure không đọc/nhìn được, hoặc thoại không thể hiểu trong nhịp đã duyệt.

### Không được làm

Không tự đổi câu factual để khớp audio; route Fact Auditor/Dialogue Editor khi cần đổi wording.

## 8. Agent 6 — Master & Platform QC

- **ID:** `AG-MASTER-01`.
- **Stage:** P11/P12 before owner release.
- **Mục tiêu:** kiểm deterministic delivery và platform packaging sau khi nội dung đã qua các review chuyên môn.

### Input

Final master; export settings; TikTok target spec; caption/thumbnail/cover; disclosure; audio/caption QC; rights report; owner delivery checklist.

### Công việc bắt buộc

1. Kiểm orientation/vertical frame, resolution, duration, frame rate/codec/container theo spec đã khóa.
2. Kiểm text/caption safe zone, crop, readability trên màn hình dọc; không che mặt/món/AI disclosure.
3. Kiểm đầu/cuối, black frame, frozen frame, glitches, jump cut không chủ ý, watermark/tool residue và audio/video sync.
4. Kiểm file naming/version, checksum hoặc manifest, caption/cover đúng episode/version.
5. Tách lỗi kỹ thuật khỏi lỗi sáng tạo; không sửa nội dung bằng export tool rồi bỏ qua gate.

### Output

`master_platform_qc.md`, automated/manual check log, defect severity, corrected-export request, delivery manifest và release recommendation.

### Quyền block

Block bàn giao nếu file sai spec, disclosure/caption bị cắt/không đọc được, lỗi render hoặc version mismatch.

### Không được làm

Không quyết định script hay “làm đẹp” để che lỗi continuity/claim.

## 9. Tier 2 — chưa chạy ở EP01 trước khi có dữ liệu thật

### Audience Evidence & Analytics Analyst (`AG-AUDIENCE-01`)

Chạy sau khi có post/test thật. Input gồm version video, audience/test design, retention/completion, recall/feedback và context phân phối. Output phải phân biệt dữ liệu quan sát, proxy và suy luận. Không dùng một clip/metric đơn lẻ để chốt canon. Nếu chạy paid split test, thay một biến mỗi lần và giữ audience/điều kiện tương đương; không suy thẳng kết quả paid sang organic.

### Series Learning Librarian (`AG-LEARN-01`)

Chạy sau pilot. Ghi accepted/rejected hooks, lỗi thoại, defect continuity, claim issues, audience evidence và owner rationale. Không lưu giả thuyết chưa kiểm chứng như quy luật series.

## 10. Quyền và thứ tự gate đề xuất

`P2 Fact/Source → P2/P3 Cultural trigger → P3 Brief → P4/P5 Creative + Vietnamese Dialogue → P6 Character/Food reference → P7 Flow Feasibility → owner generation approval → P8 generation → P9 Audio/Caption → P10 Continuity → P11 Rights/Disclosure + Master QC → owner release → Tier 2 evidence.`

## 11. Quyết định owner cần phê duyệt

Owner duyệt một trong các phạm vi sau:

### Option A — Approve Tier 1 design for EP01 (recommended)

Phê duyệt 6 role contracts và thứ tự gate ở mục 10; cho phép tạo prompt/template/run log cho từng role. Chưa duyệt bất kỳ generation request nào.

### Option B — Approve only the minimum pilot subset

Chạy `AG-FLOW-01`, `AG-CONT-01`, `AG-AV-01`, `AG-RIGHTS-01`, `AG-MASTER-01`; Cultural Reviewer chỉ kích hoạt khi risk trigger xuất hiện. Ít hồ sơ hơn nhưng có nguy cơ bỏ sót văn hóa nếu trigger viết chưa đủ.

### Option C — Rework the contracts

Owner nêu role, quyền block, input/output hoặc thứ tự gate cần sửa trước khi triển khai.

**Khuyến nghị sơ bộ:** Option A ở mức **duyệt thiết kế**, sau đó chạy pilot có kiểm soát; không gộp quyền “tự approve” vào bất kỳ agent nào.
