# AEQ-VIS-R1 — V01 actual sampled-frame review

2026-10-01 Asia/Saigon. AV-CUT profile, independent first pass, actual sample review; not MASTER/final approval. **REWORK / REVIEW_REQUIRED for sampled visual constraints; OWNER_LISTENING_REQUIRED for audio; HOLD_FOR_INPUT for full motion/lip-sync/production.**

## Inputs and capability

Read whole current `agents/audio_edit_quality/02_contract-and-role-prompts.md` including v0.1.1 and `episodes/ep01_pilot/85_p6-vietnamese-voice-probe-request-v01.md`. Inspected actual image with `tools.view_image`: `D:/Workspace/agentic_cinema/artifacts/voice-qc/v01-visual-r1/frames-2fps.png`; read `artifacts/voice-qc/v01-lite-local-03/media.json` and `asr.json`. No root findings, other reports/oracle, memory, browser/API, generation or original-media extraction used. Only this report written.

Asset identity from supplied media evidence: V01_Khoai_Lite_v0.1.mp4, SHA256 `a291bf77c9b913de43a006f4737dfcb5d27da2e9811ca6812bdc045c6e81bf76`, 8.000000s, 720×1280, H264/24fps, AAC48k stereo. These are read measurements, not a new probe/hash in this run. 85 supplies requested constraints; its requested Quality setting is not evidence of actual model or UI execution, and its historical approval-pending heading does not grant new generation authority.

Grid mapping supplied in dispatch: 4×4 row-major, zero-based source n=0,12,…180 at 24fps, hence 0.0,0.5,…7.5s. Image viewed as a resized 1152×2048 representation of 1440×2560 grid. Temporal locations are supplied extraction mapping, not burned-in timecodes independently verified here. Only 16/192 frames sampled: 0.5s gaps and the final 0.5s are unobserved. No hearing/full playback channel; no motion between samples, silence, phoneme timing or identity approval inferred from stills. Approved starting reference image is not provided for direct comparison.

## Coverage against V01 request

| Constraint | Sample observation and location | Coverage / limit |
|---|---|---|
| Khoai left, Dao right; both seated | Left potato-like character in dark jacket, right peach-like character with leaf and pale blouse remain in their respective positions in all 16 samples. | MET at sampled frames only; exact face/outfit/reference identity UNKNOWN without approved reference and full playback. |
| Only speaking character mouth movement; Dao listens silently | Khoai mouth shapes differ: closed at 0/.5s, open at 1/1.5s, rounded at 2s, closed at 2.5s, open at 3s, later alternates through 6.5s; closed at 7/7.5s. Dao gaze/blink/expression varies, with no comparably clear wide speaking-mouth opening in these samples. | Khoai facial variation observed; speaker/audio identity, Dao silence and exclusive speech motion UNKNOWN. Stills cannot prove which mouth moves between frames or lip-sync. |
| Only subtle facial movement/speech; no utensil pickup/eating/drinking/plate pulling/transfer | Khoai raises the hand on viewer-left to chest level at 1s(n24), 1.5s(n36), 2s(n48), 2.5s(n60), 3s(n72), 3.5s(n84); by 4s(n96) it rests at table, and 5s(n120) is again partly raised. No utensil visibly held in this gesture. | DEFECT against facial-only action boundary at these samples; no prohibited prop handling observed in samples, but full action coverage UNKNOWN. This is not a feeding/transfer claim. |
| Preserve table/food/leaves/sauces/bowls/chopsticks/glass | Shared plate remains central, leaves viewer-left, bowls before each character, sauces/chopsticks on table, clear glass viewer-right across grid. No visible transfer/contact with mouth in samples. | MET for gross sampled layout; exact prop preservation versus reference and transient changes UNKNOWN. |
| Locked camera | Table edges, bench, plate and lantern arrangement retain approximately same framing across samples; no obvious sampled cut/zoom. | MET for sampled framing; continuous lock/absence of subtle movement UNKNOWN. |
| No captions / extra text; preserve watermark | “Khoai” is readable lower-left in r1c3/r1c4 (1/1.5s) and r2c1–r3c4 (2–5.5s); faint at some other samples. White star-like mark lower-right and tiny “Veo” remain visible. | DEFECT in supplied sample image for extra text vs requested no captions; whether “Khoai” is burned into original video or introduced in grid preparation remains UNKNOWN. Watermark-like mark observed, original platform identity/preservation not certified. |
| No added people | Several human figures exist in the background already at 0s; their positions differ. A helmeted rider is prominent behind characters at 1.5s(n36); other riders/pedestrians appear in later samples. | Background people observed; whether newly added versus approved starting reference UNKNOWN. Do not label every background person a confirmed added-person defect without reference. |
| No music/narration, quiet ambience; exact voice/text | No audio heard. ASR recognizes “Khoan!” at estimated 0–0.4s and remaining text at estimated .66–6.86s. | UNKNOWN for music, narration, ambience, voice quality, pronunciation and audio speaker. ASR has review points, not an audio verdict. |

## Findings and routing

| ID / asset | Expected → observed; evidence / uncertainty | Severity, action / owner-stage | Closure evidence |
|---|---|---|---|
| VIS-01 / V01 hash above | 85: “Only subtle natural facial movement and speech” → conspicuous raised chest-level hand gesture, e.g. 1.0s/n24, 2.5s/n60, 3.5s/n84 versus hands at table 0s/n0 and 4s/n96. Actual inspected grid; transitions and exact gesture duration unobserved. | MAJOR scoped visual mismatch; CONT/PERF review at P7/P9 whether diagnostic gesture is acceptable or correction needed. No script rewrite or generation authorized here. | Full versioned playback for hand trajectory and prop contact; owner explicitly accepts this probe deviation or new version rechecked against constrained action. |
| VIS-02 / V01 sample grid | 85: “No … captions” → visible “Khoai” lower-left at 1.0s/n24, 1.5s/n36, 2.0s/n48 and later samples. Inspected pixels; original-video vs montage-overlay provenance unverified. | MAJOR REVIEW_REQUIRED for original-media caption constraint; MASTER/AV P11 checks native source at same frames. | Native-source frame/playback proves whether text exists in video; if montage label only, close as grid artifact. If source text, corrected version/hash plus actual render review or explicit owner deviation acceptance. Watermark must be preserved. |
| VIS-03 / V01 ASR | Exact request “hồi bé” / “rang gạo” → ASR “hội” at estimated 3.76–3.90s and “răng” at 5.20–5.42s. Read ASR, not hearing; error may be recognition. | MAJOR REVIEW_REQUIRED, not confirmed pronunciation/dialogue defect; AV/owner P6/P9 prioritized listening around 3.5–4.3s and 4.7–5.8s. | Actual listening with exact quoted words and timestamps; retain original text unless P5/P2 + owner approve change. |

No finding establishes lip-sync error, Dao speaking, unwanted voice, food transfer, temporal object discontinuity, added background people or camera drift. Missing reference/playback/hearing is UNKNOWN, not an automatic defect. No average score masks the observed action mismatch or unresolved text provenance. No maker plan executed.

## Separate verdicts and five-part handoff

Sample visual review complete: gross composition/props/framing covered only at selected frames; facial-only action constraint has sampled mismatch; extra text visible in grid needs native-source attribution. Measurement coverage is supplied metadata only. Listening remains OWNER_LISTENING_REQUIRED; full motion/lip-sync/continuity and production HOLD_FOR_INPUT. No character/voice identity lock, full dialogue continuity, final episode, Quality-model, cost/rights or owner take acceptance follows from this run.

1. **Đã xác định:** Actual image shows stable sampled left/right seating and table layout, Khoai hand gesture, varying Khoai mouth poses, visible “Khoai” text and watermark-like mark. Background people are visible from first sample.
2. **Quyết định:** Flag facial-only action deviation and native-text review; do not approve lip-sync, silence, voice or final production from grid/ASR.
3. **Giả định:** Use dispatch row-major extraction times and supplied media hash as asset linkage; not independently regenerated. Request85 is comparison criteria, not proof of settings or newly granted authority.
4. **Còn mở:** Grid text provenance, starting-reference preservation, continuous camera/prop/hand behavior, Dao silence, exact words and synchronization.
5. **Bước tiếp:** Native-source check “Khoai” at 1/2s; full playback for raised hand and speaking mouths; owner/AV prioritized listening at ASR review windows. CONT handles reference/prop/body states, PERF diagnostic action/readability, AV audio/timing, MASTER final/render; any new version gets separate QC and owner acceptance.
