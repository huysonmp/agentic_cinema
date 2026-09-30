# EP01 — Pilot

## Hiện hành — P6 sau vòng thử 2026-09-30

Update mới nhất: [rework49](49_p6-targeted-profile-eyeline-grip-rework-v01.md) đã tạo/lưu6output versions nữa (3generation +3editor revisions). Root thấy E-D03 sửa được left gaze, chưa owner approval; profile screenRIGHT và functional chopstick grip vẫn fail. Tổng15output versions từ46–49, không15asset cards riêng. Số dư sau49 vẫn1.050/observed delta0; primary45 không thay. Các kết luận lỗi46–48 bên dưới là baseline trước rework.

Ưu tiên phần này hơn các dòng trạng thái lịch sử bên dưới. P5 nội dung đã handoff theo38; [owner duyệt visual baseline bộ đôi v0.3](45_p6-owner-v03-visual-baseline-approval.md). Đã thực hiện [5 ảnh angle/rework](46_p6-consistency-front-profile-run-v01.md), [2 ảnh expression](47_p6-expression-diagnostics-v01.md), [2 ảnh hand/prop](48_p6-static-hand-prop-diagnostics-v01.md). Tổng9output mới đã lưu local và root review; không đồng nghĩa QC PASS hoặc owner duyệt từng asset. Góc Khoai chưa exact90°, eyeline Đào và grip đũa cần sửa. Primary duo45 vẫn là nguồn identity, geometry phần khuất chưa chốt.

P6 ACTIVE_DIAGNOSTICS / OWNER_REVIEW_PENDING, chưa hoàn tất. Food visual, voice và motion chưa kiểm; chưa video/master. Cap tổng200credit theo41; Flow số dư sau vòng vẫn1.050, UI0 mỗi still request và observed delta0. Không upload reference mới. Media tại media/raw/ep01_p6_consistency/ là gitignored; docs chứa manifest/hash, không có binary trên GitHub.

## Lịch sử trước vòng P6 hiện hành

Authority mới nhất: [owner cho thử P6 trong tổng200 credit, dùng in-app browser](41_p6-owner-trial-authority-200credits-and-iab-login.md); thay cap40/no-retry của proposal40. Đã mở tab Google xác minh cho owner; chưa generate.

P6 update: [intake và request40](40_p6-reference-intake-and-character-trial-request-v0.1.md) có text sources/Flow preflight và hai prompt base với count/cap/stop. Chờ owner duyệt chạy; chưa food visual verification hoặc output media.

**Hiện hành:** [owner duyệt Q0 và V1A/V2A/V3A](38_p5-content-handoff-and-p6-direction-approval.md); P5 CONTENT_BASELINE_APPROVED_FOR_P6_HANDOFF, P6 OPEN_FOR_DESIGN_PREPARATION / ASSET_APPROVAL_PENDING. [Spec/sample plan39](39_p6-character-voice-design-and-sample-plan-v0.1.md) chưa tạo asset; các status pending cue/review trong lịch sử bên dưới không thay biên bản38.

- **Status:** P5_C_V0.5_OWNER_CONTENT_APPROVED / FINAL_REVIEW_PENDING / AI_PERFORMANCE_UNTESTED
- **Current stage:** cuối P5: P0–P3 đã duyệt, owner chọn C và chấp nhận nội dung v0.5; chưa full quality pass, chưa duyệt hình/giọng/shot/prompt hoặc video
- **Outcome:** một video TikTok dọc khoảng 30 giây, đi đủ P2–P14.
- **Phân công bàn giao hiện hành:** [owner tự dựng Canva, hỗ trợ bàn giao clip pack theo cảnh/đoạn](35_owner-canva-assembly-and-shot-delivery-decision.md). Giữ kiểm chất lượng từng clip và khả năng nối; chưa media, chưa master QC PASS.
- **Update cuối P5:** [hai review độc lập exact C-v0.5 hoàn tất](36_p5-v0.5-final-paper-reviews-and-cue-decision.md), cue decision pending; [P6 hình/giọng](37_p6-visual-voice-direction-proposal-v0.1.md) mới là proposal. Cập nhật này ưu tiên hơn trạng thái pending review trong các đoạn lịch sử dưới đây.

Món pilot: Nem Bùi – Bắc Ninh. Wordplay “thả thính” là một hướng sáng tạo cũ, chưa được duyệt; không suy claim “đãi khách” từ trò chơi chữ. Episode brief P3 v0.1 đã được owner duyệt; concept và script chưa khóa.

Xem [01_input-review-nem-bui.md](01_input-review-nem-bui.md).

Pack P2 cũ tại [02_p2-research-pack-nem-bui.md](02_p2-research-pack-nem-bui.md) là tư liệu lịch sử; baseline được duyệt là [v0.2](06_p2-research-pack-v0.2.md) kèm [E1](07_p2-v0.2-erratum-and-owner-gate.md). Không bản P2 nào tự duyệt lời thoại.

Owner đã chấp nhận [ranh giới claim P2](03_p2-claim-boundary-decision.md), duyệt [gói P2 v0.2 + E1](08_p2-approval-record.md) và [Episode Brief P3 v0.1](10_p3-approval-record.md) với D1=A, D2=A. P4 chưa có concept pass; Script Lab cũ vẫn `NON-FINAL`.

P4 đã chạy vòng 1; xem [decision packet](15_p4-round1-decision-packet-v0.1.md). Chưa có owner shortlist P4 chính thức; P5 chỉ mở thử nghiệm theo ngoại lệ bên dưới.

Owner đã chọn ngoại lệ B để thử hai hướng A và B ở P5; xem [ủy quyền test](16_p5-provisional-test-decision-2026-09-30.md) và [hai test script](17_p5-provisional-test-scripts-v0.1.md). Đây là thử nghiệm tạm thời, chưa phải script production.

Hai bản đã qua lượt ngôn ngữ đầu tiên và có [candidate rewrite v0.2](20_p5-language-rewrite-candidates-v0.2.md); bản v0.1 giữ nguyên để so sánh. Timed read vẫn chưa chạy.

Hai context đọc lạnh đảo thứ tự và Fact Auditor đã [chẩn đoán v0.2](22_p5-v0.2-independent-read-and-claim-review.md). Đây là paper diagnostic trước timed read, không formal P5 pass. [Hai bản sửa v0.3](23_p5-test-scripts-v0.3.md) đã có [review tiếng Việt/kịch tính, fresh cold reader và delta claim check](24_p5-v0.3-independent-review-and-owner-packet.md). Packet 24 là recommendation tại thời điểm review, không decision của owner.

Owner đã [giữ A-v0.3 làm một hướng thử và hiệu chỉnh cách kể](25_owner-creative-correction-and-a-v0.3-retention.md): Khoai–Đào gặp món tự nhiên trong câu chuyện đời thường, không mặc định nhiệm vụ sản xuất/giới thiệu món. Giữ nguyên A-v0.3, chưa script lock hoặc quyền generate; không tự thực thi đề nghị quay P4 cả hai ở packet 24.

Theo [yêu cầu thêm ít nhất hai hướng thử](26_owner-expanded-script-test-set.md), đã viết và phản biện [C/D đời thường v0.2.1](28_p5-additional-everyday-test-scripts-v0.2.1.md), có [lịch sử rework](27_p5-additional-drafts-and-review-history.md) và [packet A/C/D](29_p5-expanded-test-set-owner-packet.md). C/D là candidate đề nghị thử tiếp, chưa owner chọn, chưa timed read hay script lock.

Owner đánh giá C/D nhạt, yêu cầu cải thiện: [hai chuyện viết lại v0.3](30_p5-everyday-script-rebuild-v0.3.md) là bản hiện hành để đọc, do root viết; chưa reviewer độc lập/owner duyệt. TEST_FURTHER của v0.2 không áp cho v0.3. C có ký ức mới dạng fiction chưa canon; D còn rủi ro lệch trục thính P3, không tự đổi brief. Bản cũ và packet 29 giữ làm lịch sử.

Owner chọn C để sửa tiếp: [C-v0.4 với payoff nhanh tay lấy nem và bị Đào bắt gặp](31_p5-script-c-v0.4-owner-payoff-revision.md) là bản hiện hành của C; v0.3 giữ lịch sử. Exact v0.4 chưa duyệt/review độc lập/timed read; D tạm không xử lý lượt này, không DROP; A vẫn giữ nguyên.

**Cập nhật quyết định hiện hành:** owner chấp nhận kết chữa cháy gắp cho Đào; [C-v0.5 đầy đủ](32_p5-script-c-v0.5-approved-content.md) thay v0.4 để phát triển tiếp, có [approval record](33_p5-c-v0.5-owner-content-approval.md). Các status trong đoạn lịch sử trên không thay quyết định này. Final review chưa chạy đúng v0.5; kiểm nhịp bằng đầu ra AI, không yêu cầu người diễn. Chưa P5 full quality PASS hoặc generation authority.

[Gap register review cuối P5](34_p5-final-review-gap-register-c-v0.5.md) ghi ba việc còn mở: independent narrative/khẩu ngữ, exact claim/fiction review, alignment thính với brief. Các việc timing/action/voice/media thuộc P6–P12, không yêu cầu human rehearsal. [Bảy vị trí production đã duyệt chuẩn bị](../../agents/production_team/01_owner-preparation-approval.md), có package PROD7-v0.1 chưa test hành vi/episode run.

Owner đã duyệt toàn bộ thiết kế [Tier 1 quality agents/checkers](../../agents/quality_system/01_tier1-owner-approval-2026-09-30.md). Đây là quyền triển khai contract và test fixture; chưa mở generation hoặc release approval.

[Runtime v0.1 và stage map](../../agents/quality_system/02_runtime-contract-and-stage-map-v0.1.md), [sáu role prompts](../../agents/quality_system/03_tier1-role-prompts-v0.1.md) và [behavior fixtures](../../agents/quality_system/04_tier1-behavioral-fixtures-v0.1.md) đã được tạo. Runtime version cần owner review trước run trên artifact EP01; có prompt không đồng nghĩa đã QC media thật.

[Textual behavior probe](../../agents/quality_system/05_tier1-behavior-probe-report-v0.1.md) đã chạy trên Case hư cấu, giữ ranh giới unknown/authority; không phải EP01 hoặc media run.

FLOW output đã có [retest và readiness](../../agents/quality_system/06_flow-fixture-retest-and-runtime-readiness-v0.1.md); runtime version vẫn chờ owner review, media/production capabilities chưa được kiểm.

