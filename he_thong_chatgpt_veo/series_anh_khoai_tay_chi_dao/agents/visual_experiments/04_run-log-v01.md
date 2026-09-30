# VE run log v0.1

2026-09-30. Đăng ký trước dispatch. Authority01; external tools NONE, local read/view_image/report write only. P6 OPEN. Không generation trong agent runs.

| Run | Role/mode | Inputs | Output | Status |
|---|---|---|---|---|
| VE-FIX-01 | VEXP / BEHAVIOR_FIXTURE | PROD7 contract; VE02; fixtures03 IDs01–06 | 05_vexp-fixture-results-v01.md | COMPLETED; root calibration09 ALIGNED, không production pass |
| AP-FIX-01 | CONT-AP / BEHAVIOR_FIXTURE | Tier1 contract/CONT; VE02; fixtures03 IDs07–10 | 06_cont-fixture-results-v01.md | COMPLETED; root calibration09 ALIGNED, không production pass |
| AP-MEDIA-01 | CONT-AP / MEDIA_REVIEW | primary45 actual; I04/I05 actual, không maker logs | 07_cont-grip-media-review-v01.md | COMPLETED; actual view_image3JPEG, cả hai REWORK; không motion/P6 pass |
| VE-PILOT-01 | VEXP / PAPER_PROPOSAL + actual still inspection | 53–56, primary45/I04/I05; report07 sau độc lập reviewer | 08_vexp-grip-food-pilot-proposal-v01.md | COMPLETED; actual3JPEG + reviewer07; tests NOT_RUN; root disposition09 |

Target paths media: `../../media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg` và `../../media/raw/ep01_p6_consistency/H-K-I04_v0.1.jpg`, `H-K-I05_v0.1.jpg`. Relative tính từ visual_experiments nên actual dispatch dùng absolute workspace paths; manifest episode55 giữ checksum. Food output không có, chỉ execution log56; không giả media.
