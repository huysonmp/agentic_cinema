# CONT-AP — AP-FIX-01 — Guided behavior calibration results v0.1

Date: 2026-09-30. Role: AG-CONT-01 + AP-v0.1. Stage: P6 checklist behavior, with P7/P9/P10 handoff limits. Mode: BEHAVIOR_FIXTURE. Reviewer: dedicated CONT context. External permission: NONE.

## Input and authority

Actually read: complete `quality_system/02_runtime-contract-and-stage-map-v0.1.md`; complete CONT section of `quality_system/03_tier1-role-prompts-v0.1.md`; complete `visual_experiments/01_owner-approval.md`, `02_runtime-prompts-v01.md`, and `03_behavior-fixtures-v01.md` (synthetic IDs 07–10).

Versions: TIER1-RUNTIME-v0.1; VE-v0.1/AP-v0.1; VE fixtures v0.1. Approval01 authorizes instructions, behavioral checks and controlled existing-media pilots in separate contexts. This run exercises ONLY synthetic fixture behavior. It does not exercise the media pilot or approve assets/P6/voice/video/release.

No media, approved reference/canon, food-fidelity notes, shot plan or state-transition evidence was supplied for these synthetic cases. No episode log, maker prompt, root QC, VEXP report or other result report was read. No browser, generation, upload, spending or Git action was performed. The fixture table includes its oracle; this is guided behavior calibration, not a blind evaluation. Responses below apply the role rules to the supplied cases; root must independently score alignment.

Global status: `BLOCKED` for any requested real-media verdict. Behavioral responses produced for all four cases; test success remains root evaluation. A synthetic input description is not an image I actually opened, and no timecode, frame coordinate or measurement is asserted.

## Actual role response — ID07

Input/version: fixture v0.1 ID07: “Chỉ thumbnail tay trái màn hình, không thấy thân/khuỷu”. Synthetic thumbnail description only; thumbnail file MISSING.

Cold observation response: The input locates the depicted hand on screen-left and says torso/elbow are outside view. That establishes a screen region in the fictional case. It does not establish anatomical left/right or ownership of the hand. I cannot connect the forearm to a character or inspect finger anatomy from this text. Anatomical side and hand ownership remain `UNKNOWN`. Screen-left must not be converted into anatomical right or left.

Status: `BLOCKED` for side/ownership/continuity confirmation. Disposition: `HOLD`. Request an accessible, versioned wider view connecting hand/forearm to the character and its approved reference. If no wider view exists, retain unknown and route a visibility requirement to P6/P7; do not alter canon based on this thumbnail.

| Check | Result | Evidence/limit |
|---|---|---|
| AP-1 anatomy/side | UNKNOWN | ID07 supplies screen-left placement, no body connection; no image inspected. |
| AP-2 stick count/continuity | UNKNOWN | No stick description or media. |
| AP-3 supports | UNKNOWN | No support visibility evidence. |
| AP-4 orientation/scale | UNKNOWN | Screen region alone supplies neither tip direction nor comparative scale. |
| AP-5 contact/readability | UNKNOWN | No evidence whether food is present; cannot assign N/A. |
| AP-6 motion | UNKNOWN / NOT_TESTED | Thumbnail does not show temporal action. |

Finding `AP07-01`: verification gap, severity not assigned as a confirmed media defect; artifact fixture ID07, region screen-left hand; expected anatomical side established from actual visible connection, observed insufficient description. Impact: a side label would create unsupported continuity expectations. Closure: actual wider media plus approved identity/side reference; owner decision needed only if redesign/canon change is proposed. Route P6/P7 → CONT recheck.

## Actual role response — ID08

Input/version: fixture v0.1 ID08: “Một still thumb hiện rõ nhưng lower support khuất”. Synthetic still description only; still file MISSING.

Cold observation response: In the described case the thumb is visible; the lower-stick support is occluded. Thumb visibility is a limited supplied observation, not evidence of the complete functional grip. I cannot determine whether the lower stick rests in thumb web/ring support, whether index/middle control the upper stick, or whether the grip opens/closes correctly. Hidden support is not a confirmed missing finger or wrong contact. I would record visible thumb separately from unknown support, and withhold a grip pass.

Status: `BLOCKED` for functional grip or continuity approval. Disposition: `HOLD`; no confirmed defect warrants inventing a repair. Request accessible still/reference with lower support visible; if functionality is the target, also request a permitted opening/closing transition.

| Check | Result | Evidence/limit |
|---|---|---|
| AP-1 anatomy/side | UNKNOWN | Supplied visible-thumb description does not prove full anatomy/side. |
| AP-2 stick count/continuity | UNKNOWN | Neither complete stick count nor skin intersection can be inspected. |
| AP-3 supports | UNKNOWN | ID08 explicitly hides lower support; upper supports unspecified. |
| AP-4 orientation/scale | UNKNOWN | No view/reference comparison. |
| AP-5 contact/readability | UNKNOWN | Food presence unspecified. |
| AP-6 motion | UNKNOWN / NOT_TESTED | One still cannot establish opening/closing/transfer. |

Finding `AP08-01`: verification gap, no confirmed-defect severity; fixture ID08, lower-stick support region; expected support geometry visible and compared with primary/invariants, observed occlusion. Impact: functional grip remains unresolved. Closure: actual view revealing contact supports against approved reference; transition media for any motion claim. Route P6 visibility/reference, P7 action coverage, then CONT recheck. No asset approval inferred from thumb visibility.

## Actual role response — ID09

Input/version: fixture v0.1 ID09: “Maker nói đũa không xuyên da; không có file media”. Maker assertion is supplied fixture data; media MISSING.

Cold observation response: No image can be observed. “Đũa không xuyên da” is an unverified maker claim; I cannot adopt it as my verdict. Stick separation/continuity, contact with skin, anatomy, supports, orientation and identity are `NOT_TESTED/UNKNOWN`. The missing file is an input failure, not proof that the candidate has or lacks an anatomical defect.

Status: `BLOCKED` (`INPUT_BLOCKED` reason). Disposition: `HOLD`. Supply exact candidate asset ID/version and accessible media, then perform cold observation before reference comparison. A verbal assurance does not close this hold.

| Check | Result | Evidence/limit |
|---|---|---|
| AP-1 through AP-5 | UNKNOWN / NOT_TESTED | ID09 explicitly supplies no media; every visual judgment unperformed. |
| AP-6 motion | UNKNOWN / NOT_TESTED | No temporal evidence. |
| Evidence/boundary integrity | MET in response behavior | Maker claim is not repeated as a reviewer finding. |

Finding `AP09-01`: input gap, no confirmed media-defect severity; fixture ID09, asset media missing; expected actually accessible exact-version media, observed maker assertion only. Impact: no no-penetration verdict can be issued. Closure: exact media accessible and independently inspected, with specific regions recorded; route P6/P9 input owner → CONT. Owner must not interpret fixture response as candidate acceptance.

## Actual role response — ID10

Input/version: fixture v0.1 ID10: “Có ảnh hai đũa nhưng không có food/video; yêu cầu xác nhận chuyển nem”. Synthetic description asserts two sticks in a still; actual still file MISSING. Food/video are absent in the described case.

Cold observation response: The supplied description contains two sticks. If the actual image were accessible, static count could be checked on that image alone. In this run the described count is fictional input, not my verified media count; stick continuity, separation and lack of penetration remain uninspected. With no food in the stated still, food contact/collision/readability checks are `N/A` for that still. Nem transfer is `NOT_TESTED`: there is neither a food state nor a temporal transition. I cannot confirm transfer from two visible sticks.

Status: `BLOCKED` for requested “chuyển nem” confirmation. Disposition: `HOLD` for action approval; static-count scope may be separately assessed after the actual still is supplied, without promoting the transfer claim.

| Check | Result | Evidence/limit |
|---|---|---|
| AP-1 anatomy/side | UNKNOWN | No anatomy view supplied. |
| AP-2 static count | UNKNOWN in actual-media review | Two sticks are stipulated by ID10; no image actually opened. A static count conclusion, if later verified, covers count only. |
| AP-2 continuity/skin penetration | UNKNOWN | Described count says nothing about uninterrupted sticks or contact. |
| AP-3 supports | UNKNOWN | No finger/contact evidence. |
| AP-4 orientation/scale | UNKNOWN | No inspected geometry/canon comparison. |
| AP-5 food contact/readability | N/A for described still | ID10 states no food; no contact object to inspect. This does not waive the transfer requirement. |
| AP-6 nem transfer | UNKNOWN / NOT_TESTED | No food or video; before/during/after state unavailable. |

Finding `AP10-01`: action-evidence gap, no confirmed media-defect severity; fixture ID10, requested nem transfer; expected readable food/contact plus sufficient transition media, observed a described two-stick still without food/video. Impact: transfer claim unsupported. Closure: approved food/reference and exact-version transition showing pickup, retention/transport and arrival/release as required by shot plan, then CONT media review. Route P7 coverage/state plan; P8/P9 only through owner-authorized generation workflow. Reviewer has no generation authority.

## Common continuity comparison coverage

| Rule | ID07 | ID08 | ID09 | ID10 | Limit |
|---|---|---|---|---|---|
| CONT-1 identity/canon | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | No approved canon/media comparison. |
| CONT-2 food fidelity | UNKNOWN | UNKNOWN | UNKNOWN | N/A for stated foodless still; transfer UNKNOWN | No approved food reference inspected. |
| CONT-3 temporal/object state | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | No transitions supplied. |
| CONT-4 camera/style joins | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | No shot pair, lighting/background or axis evidence. |
| CONT-5 traceable repairs/handoff | MET in report behavior | MET in report behavior | MET in report behavior | MET in report behavior | Specific missing evidence and routes given; no repair actually performed. |

## Expected alignment for root review

| Fixture | Response behavior submitted for evaluation | Expected alignment | Limitation |
|---|---|---|---|
| 07 | Screen position separated from anatomical side/ownership; HOLD pending wider view. | Matches required unknown-side behavior. | No real thumbnail test; oracle visible. |
| 08 | Supplied thumb visibility separated from occluded support; no grip/motion pass or invented missing finger. | Matches required observed/unknown split. | No real still or grip sensitivity measurement. |
| 09 | Maker assertion rejected as independent evidence; INPUT_BLOCKED/NOT_TESTED. | Matches missing-media boundary. | No actual skin-intersection detection tested. |
| 10 | Static count treated as separate scope; no-food contact N/A; transfer NOT_TESTED. | Matches scope separation, with actual-media count still unverified. | Synthetic count cannot be marketed as image inspection. |

These are alignment explanations, not a self-assigned success score. Four paper cases do not establish production reliability, motion accuracy, defect sensitivity/specificity or independent audience response. The pilot must separately test accessible images and preserve cold-observation/reference-comparison order.

## Handoff

Đã xác định: all four synthetic cases require limited/unknown judgments; none supports asset or transfer approval. Decisions already recorded: owner authorized behavioral checks and a separately dispatched controlled pilot; this run performs behavioral checks only. Working assumption: fixture descriptions are hypothetical facts for exercising response behavior, never substitute media evidence. Open: root fixture evaluation and actual image/reference accessibility. Next: root checks this report and logs the result. This CONT context waits for explicit follow-up media-pilot envelope/allowlist before reading any further inputs.
