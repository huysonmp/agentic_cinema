# VE run log v0.1

2026-09-30. Đăng ký trước dispatch. Authority01; external tools NONE, local read/view_image/report write only. P6 OPEN. Không generation trong agent runs.

| Run | Role/mode | Inputs | Output | Status |
|---|---|---|---|---|
| VE-FIX-01 | VEXP / BEHAVIOR_FIXTURE | PROD7 contract; VE02; fixtures03 IDs01–06 | 05_vexp-fixture-results-v01.md | COMPLETED; root calibration09 ALIGNED, không production pass |
| AP-FIX-01 | CONT-AP / BEHAVIOR_FIXTURE | Tier1 contract/CONT; VE02; fixtures03 IDs07–10 | 06_cont-fixture-results-v01.md | COMPLETED; root calibration09 ALIGNED, không production pass |
| AP-MEDIA-01 | CONT-AP / MEDIA_REVIEW | primary45 actual; I04/I05 actual, không maker logs | 07_cont-grip-media-review-v01.md | COMPLETED; actual view_image3JPEG, cả hai REWORK; không motion/P6 pass |
| VE-PILOT-01 | VEXP / PAPER_PROPOSAL + actual still inspection | 53–56, primary45/I04/I05; report07 sau độc lập reviewer | 08_vexp-grip-food-pilot-proposal-v01.md | COMPLETED; actual3JPEG + reviewer07; tests NOT_RUN; root disposition09 |
| AP-MEDIA-02 | CONT-AP / MEDIA_REVIEW | I06 actual cold; I04 + primary sau cold; không maker prompt/log | 10_cont-i06-static-review-v01.md | COMPLETED; actual3JPEG; orientation/visible pose MET, grip HOLD; context từng xem I04 nên không fresh blind; không motion/P6 pass |
| AP-MEDIA-03 | CONT-AP / MEDIA_REVIEW | I07 actual cold; I06 actual sau cold; không prompt/QC | 11_cont-i07-close-grip-review-v01.md | COMPLETED; actual2JPEG; bounded static-readability PASS_FOR_NEXT_GATE, không identity/motion/asset approval; generation detail không chứng minh pixels I06 |
| AP-MEDIA-04 | CONT-AP / MEDIA_REVIEW | I09 actual cold; I07/I06 + primary sau cold; không maker prompt/QC | 12_cont-i09-integrated-grip-review-v01.md | COMPLETED; actual4JPEG; bounded static identity+grip-readability PASS_FOR_NEXT_GATE; retainedcontext không freshblind; không motion/asset/P6 approval |

Target paths media: `../../media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg` và `../../media/raw/ep01_p6_consistency/H-K-I04_v0.1.jpg`, `H-K-I05_v0.1.jpg`. Relative tính từ visual_experiments nên actual dispatch dùng absolute workspace paths; manifest episode55 giữ checksum. Food output không có, chỉ execution log56; không giả media.
