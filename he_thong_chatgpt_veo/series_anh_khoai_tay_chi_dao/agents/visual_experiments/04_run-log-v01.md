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

## 2026-10-01 — TABLE-BATCH01

Episode73 có pre-dispatch register, actual output manifest và root adjudication. Dòng food chưa có ở đoạn trên giữ lịch sử lượt56, không áp dụng cho batch mới này.

| Run | Role/mode | Inputs | Output | Status |
|---|---|---|---|---|
| FOOD-TABLE-BATCH01 | Food/leaf evidence / MEDIA_REVIEW+RESEARCH | A/B/C cold, rồi F05/two owner-authorized photos; source text | 13_food-table-batch-evidence-review-v01.md | COMPLETED; six actual images; REWORK all three, sprigs UNKNOWN |
| TABLE-BATCH01-STAGING | CONT / MEDIA_REVIEW | A/B/C cold, rồi script32/serving invariants | 14_food-table-batch-staging-review-v01.md | COMPLETED; static counts/layout limited pass, action HOLD; root73 watermark exception supersedes remove action |
| TABLE-BATCH01-SELECTION | VEXP / MEDIA_REVIEW+PROPOSAL_ONLY | Six actual images, maker73, final13/14 | 15_food-table-batch-selection-v01.md | COMPLETED; C proposed repair base; L01/F01 NOT_RUN; no owner asset approval/P6 closure |

## 2026-10-01 — Context-linked repair and integrated reconstruction

Episode74 records actual R01/R02/R03/R04; ledger75 registered current independent runs before dispatch. R04 was incompletely pre-registered and has retrospective UI reconciliation; do not claim flawless pre-log compliance. Episode76 records R05 reconstruction and R06 correction separately from specialist runs.

| Run | Role/mode | Inputs | Output | Status |
|---|---|---|---|---|
| TABLE-CONTEXT-R01-CONT | CONT / MEDIA_REVIEW | C_v0.2 cold, then control/script/serving/real refs | 16_context-linked-table-staging-review-v01.md | COMPLETED; leaf mismatch REWORK, functional staging HOLD |
| TABLE-CONTEXT-R01-FOOD | Food/leaf / MEDIA_REVIEW | C_v0.2 cold, then control/F05/two real refs | 17_context-linked-table-food-review-v01.md | COMPLETED; leaf/texture REWORK, sprigs UNKNOWN |
| TABLE-CONTEXT-R02-CONT | CONT / MEDIA_REVIEW, retained context | C_v0.3 actual first, then retained references/context | report16 append | COMPLETED; deep-lobe mismatch bounded resolved; leaf ring unselected, actual access/motion HOLD |
| TABLE-CONTEXT-R02-FOOD | Food/leaf / MEDIA_REVIEW, retained context | C_v0.3 actual first, then controls/F05/two refs | report17 append | COMPLETED; deep-lobe defect only resolved; food REWORK/sprigs UNKNOWN |
| EP01-P6-R03R04-CONT-02 | CONT+AP / MEDIA_REVIEW | C_v0.4 and T03_v0.1 cold, then ledger75/script/primary | 18_integrated-table-staging-review-v01.md | COMPLETED; T03 same-edge/bowl-assignment REWORK, C HOLD; historical72 prompt/QC exposure after cold disclosed |
| EP01-P6-R03R04-FOOD-02 | Food/leaf / MEDIA_REVIEW+SOURCE_CHECK | Same targets cold, F05/two actual refs + primary source text | 19_integrated-table-food-review-v01.md | COMPLETED; both texture REWORK; sprig evidence UNKNOWN; historical72 exposure after cold disclosed |
| EP01-P6-CONTEXT-CTD-01 | Existing AG-CTD-01 / PAPER_REVIEW | Ledger75, exact approvals/script; primary/C_v0.4/T03_v0.1 actual | ../production_team/09_episode-context-preflight-ep01-v01.md | COMPLETED; paper context recommendation for new frame, not asset approval/model feasibility |
| EP01-P6-R05-CONT-03 | CONT+AP / MEDIA_REVIEW, retained context | T03_v0.2 actual first, then allowed primary/ledger | report18 append | COMPLETED; same-edge/static bowl assignment supported; REWORK third bowl/sign, background counter variant; no action pass |
| EP01-P6-R05-FOOD-03 | Food/leaf / MEDIA_REVIEW, retained context | T03_v0.2 actual first, then F05/two real refs | report19 append | COMPLETED; REWORK dominant rounded cords/smooth pink pieces and three-bowl count; limited leaf appearance compatible, species UNKNOWN |
| EP01-P6-ART-TEXTURE-01 | Existing AG-ART-01 / PAPER_PROPOSAL | Actual F05/two real refs/T03_v0.2/v0.3; ledger75/71/68 | ../production_team/10_integrated-food-repair-brief-v01.md | COMPLETED; mound-only supporting-source proposal + one focused test/stop; no generation/asset pass; registration recorded after dispatch in76 |
| EP01-P6-R09-CONT-04 | CONT+AP / MEDIA_REVIEW, retained context | Exact T03_v0.6 F631378E…; target first then approved primary/ledger75/script32 | report18 append | COMPLETED; KEEP_FOR_OWNER_REVIEW for bounded static layout/count/visible identity; background counter MINOR selection item; food/leaf/motion not certified; no maker76/10/root QC; P6 open |
| EP01-P6-R09-FOOD-04 | Food/leaf / MEDIA_REVIEW, retained context | Exact T03_v0.6 F631378E…; target first then actual F05/two real refs/source ledger75 | report19 append | COMPLETED; REWORK food geometry/coating verified whole-frame/native region/comparable-scale reference; static count/limited leaf cues MET, species/motion unknown; no maker76/10/root QC; P6 open |
| EP01-P6-ART-TEXTURE-02 | Existing AG-ART-01 / PAPER_ANALYSIS | Actual R08/R09/F05; exact request76 section R09; source75/71/68 | ../production_team/10_integrated-food-repair-brief-v01.md append | COMPLETED; two bounded alternatives, A recommended (empty intermediate then F05), no causal mechanism conclusion; no Flow/generation/asset pass; root A1 started from provisional message transparently logged |
| EP01-P6-R11R12-CONT-05 | CONT+AP / MEDIA_REVIEW, retained context | Exact T03_v0.7 584A61…C0E85 + v0.8 AEB6DF…0D924; both targets first then approved primary/ledger75/script32 | report18 append | SAVED_DISPOSITION_ROOT_VERIFIED / TURN_FAILED_QUOTA; full neutral static report present: PASS_WITH_ACTIONS bounded scope, v0.8 first KEEP_FOR_OWNER_REVIEW, warm variation owner choice; no asset/food/motion/P6 pass |
| EP01-P6-R11R12-FOOD-05 | Food/leaf / MEDIA_REVIEW, retained context | Same two exact targets first, then F05/two real refs; originalR09 only plate/projected-portion context | report19 append | SAVED_DISPOSITION_ROOT_VERIFIED / TURN_FAILED_QUOTA; complete report present: both PASS_FOR_OWNER_REVIEW for observable food/leaf/count, compact footprint MINOR presentation note; no species/recipe/motion/asset/P6 pass |
| EP01-P6-CONTEXT-CTD-02 | Existing AG-CTD-01 / PAPER_REVIEW | Approved script/handoff38, P6 plan39, primary45, owner grip62/input64, serving71–72/source ledger75; final candidates/reviews pending within adviser input snapshot | ../production_team/11_p6-next-gate-readiness-v01.md | SAVED_DISPOSITION_ROOT_VERIFIED / TURN_FAILED_QUOTA; complete paper next-gate map present, no new production choices/Flow/asset pass |

Report contexts are separate model-based checks, not human audience validation. Earlier quota failures affected R03 specialist dispatch; reports18/19 now inspect the actual R03/R04 versions rather than pretending the failed agents completed those runs. Context gate08 remains a proposal; existing CTD run09 and root ledger75 are actual bounded actions, not implementation of a new runtime role.

Final runtime notes: three last turns ended with usage-limit errors; root did not retry or record successful final returns. Local reports18/19/11 already contain complete notes/access/coverage/findings/disposition/handoff rows; root read back those saved artifacts and checked media hashes. Saved report content is usable scoped evidence, not proof runtime succeeded. Owner packet77 aggregates those actual artifacts, with exact-frame/style/compactness selection pending and no new generation in progress.
