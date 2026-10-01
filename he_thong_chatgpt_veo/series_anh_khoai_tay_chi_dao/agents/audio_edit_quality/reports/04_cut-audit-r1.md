# AEQ-CUT-R1 — independent AV-CUT review

2026-10-01 Asia/Saigon. Scope: BEHAVIOR_FIXTURE C-A/B/C/D + MEASURED_MEDIA_EVIDENCE local diagnostic. Fixture response: **FIXTURE_RESPONSE_COMPLETE**. Actual repeat: **REWORK** relative to its expected map. Actual control: bounded technical concat checks MET; **OWNER_LISTENING_REQUIRED** for subjective audio, **HOLD_FOR_INPUT** for motion/production. No production or owner acceptance granted.

## Inputs, authority and capability

Read fully: `01_owner-approval-and-run-log.md`, `02_contract-and-role-prompts.md`, `06_cut-audit-fixtures.md`, `07_local-diagnostic-evidence.md`; actual `artifacts/voice-assembly/aeq-r1/manifest.json`; `artifacts/voice-assembly/aeq-repeat-asr-r1/{asr.json,media.json,transcript.txt,audio-diagnostics.log}`. Paths are relative to the role folder for numbered documents and workspace root for artifacts. Used the allowlisted ffprobe 9.0.2 read-only on `control.mp4` and `repeat.mp4`; independently hashed those exact bytes with SHA256. Both probes completed with exit 0. Dossier was treated as measurements, not a maker verdict; no script source, oracle, other reports, memory, browser/API or generation used. Only this report written.

Authority: owner approved bounded test under 01, not script/canon edits, production approval, release or replacement of P6/P9/P10/P12 decisions. Reviewer can read maps/ASR/logs, probe streams/durations and hash outputs. No listening, full playback or visual frame interpretation was performed. Missing: approved production takes/EDL/exact dialogue reference, hearing evidence, full video playback, actual rendered caption inspection and shot-state coverage. No speaker identity, pronunciation, emotion, safe cut, audible pop, lip-sync or scene continuity pass follows from metadata/transcript.

## Coverage and fixture decisions

| Case | Coverage and evidence boundary | Verdict / route |
|---|---|---|
| C-A, fictional A3s/B5s | DEFECT: supplied machine map A→B→B vs expected A→B; 13s vs 8s and supplied final speech repeats B. UNKNOWN: listening, motion/sync, captions. | REWORK, audio/edit P10/P11 → DLG-EDIT/EDIT + AV. Fixture evidence only; do not confuse its 3s/5s split with actual diagnostic. |
| C-B, fictional cut2 | DEFECT: request to inherit cut1 QC despite changed SHA256, music and in/out. UNKNOWN: current cut2 audio, trims, sync, captions, continuity; supplied 30s/portrait metadata does not cover these. | HOLD_FOR_INPUT; withhold release PASS. MASTER/P12 + owner require QC bound to cut2; AV reassesses music/masking/joins/truncation/sync, CONT affected states, PERF affected beats, MASTER export and actual caption render. |
| C-C, fictional clean concat | MET: supplied technical concat 8s, H264 720×1280/24fps, AAC48k stereo and same-source split. UNKNOWN: safe speech boundary, listening, lip-sync/quality/canon. N/A: cross-scene proof from this same-clip test. | Bounded measured concat pass only; OWNER_LISTENING_REQUIRED and HOLD_FOR_INPUT for production. Source identity and format are not episode approval. |
| C-D, fictional annotations | Paper inconsistency identified: nem outside mouth / empty bowl → bowl contains nem without transfer coverage; Khoai hand changes side without shot-plan allowance. UNKNOWN: actual frames, temporal transition and permitted axis/state. | HOLD_FOR_INPUT, CONT/P7 shot-state investigation; PERF checks cause→action→reaction when media arrives. No claim of having seen frames or confirmed video defect. |

## Actual measurements and exact map

Version keys are the current hashes (independently matched to manifest):

- Source V01: `a291bf77c9b913de43a006f4737dfcb5d27da2e9811ca6812bdc045c6e81bf76` (manifest/dossier identity; source bytes not independently inspected here).
- control: `088d4ac5005e03343016cd4388d08a58d3fcb832a08bcd29121e3b51184709e0`.
- repeat: `2638598b2017c181768ea79222ebb812a8f5ec6eb59f87be3f9d59ce244176d9`; ASR media input hash matches this output.

Manifest expected A=V01[0,2.5s), B=V01[2.5,8s). control executed A→B: destination A[0,2.5), B[2.5,8). repeat executed A→B→B: destination A[0,2.5), B1[2.5,8), B2[8,13.5). Destination boundaries are derived from exact trim/map arithmetic, not a sample-accurate listening measurement. Manifest commands explicitly apply those same source ranges to video and audio. This establishes the supplied render mapping; ffprobe alone cannot reconstruct content mapping.

Independent ffprobe: both H264 720×1280, 24/1 fps; AAC 48000Hz, 2 channels; both streams start 0.000000. control video/audio/container each 8.000000s, 192 video frames, 1,489,411 bytes. repeat each 13.500000s, 324 video frames, 2,516,441 bytes. Stream endpoints show no container-duration discrepancy; they do not establish perceptual sync or absence of local drift. control technical coverage MET (hash/streams/duration/supplied expected=executed map); control words/truncation remain UNKNOWN without transcript/listening. repeat streams/hash MET; expected-map coverage DEFECT (+5.5s duplicate B).

Repeat ASR quotes exactly as received; times below are **estimated ASR segment times**, not acoustic cut points:

| Text | First occurrence | Repeated occurrence |
|---|---|---|
| “Bếp nhà anh, hội bé.” | 2.44–4.16s (segment 3) | 7.92–9.66s (segment 5) |
| “Mẹ rang gạo, anh đứng chờ.” | 4.78–6.86s (segment 4) | 10.18–12.36s (segment 6) |

The second occurrences shift roughly 5.5s, consistent with the extra B. ASR begins the lines slightly before map boundaries (2.44 vs 2.5; 7.92 vs 8), so it cannot certify the 2.5s split as silence or rule out clipped speech. “hội” is retained as ASR output; no approved text supplied here to decide mismatch or alter dialogue. “rang” recognition is not pronunciation approval. Log reports 1,296,000 samples, mean −20.1dB, maximum −0.7dB; these are technical volume readings, not loudness compliance, audible clipping/pop/masking or quality pass.

## Findings and closure

| ID / asset-version | Expected → observed; method / uncertainty | Severity; action and owner | Closure evidence |
|---|---|---|---|
| CUT-01 / C-A fixture | A→B,8s → A→B→B,13s plus supplied repeated B; fictional machine/speech evidence, no hearing. | MAJOR; P10/P11 EDIT/DLG-EDIT remove unintended duplicate, AV recheck. | New fixture-version final map + speech evidence match A→B; actual QC still separate. |
| CUT-02 / C-B cut2 fixture | QC belongs to exact current bytes → changed hash/music/trim seeks cut1 PASS; paper evidence only. | MAJOR; MASTER/P12 withhold release; rerun affected AV/CONT/PERF and export/caption checks on cut2, owner decides. | cut2 hash/version-linked rerun reports + actual listening/playback/render evidence + final owner acceptance. |
| CUT-03 / C-D fixture | Covered transfer and allowed hand state → annotation gap/change; media truth UNKNOWN. | MAJOR review risk, not confirmed temporal media defect; CONT/P7 request actual end/start/transfer coverage and approved shot constraints. | Inspected versioned video with time/frame references; explanation consistent with shot plan or approved pickup/corrected cut. Canon change → P6; no dialogue workaround. |
| CUT-04 / actual repeat hash above | Expected V01 A→B,8s → extra V01[2.5,8) at destination[8,13.5),13.5s; manifest mapping + independent probe/hash + repeated ASR pairs. Content mapping confirmed by supplied executed map; hearing exact words UNKNOWN. | MAJOR relative-to-control defect (intentional negative diagnostic); P10/P11 EDIT/DLG-EDIT produce A→B version, AV independently verify. Do not repair this test artifact in this run. | New version/hash + expected/executed map, 8s streams, transcript comparison and targeted listening at join/duplicate region; statement “fixed” alone insufficient. Current control is comparator, not a retroactive closure of repeat. |

No maker edit plan executed by reviewer. No missing-input item is itself labeled a confirmed media defect. Narrative continuity, object/identity, subjective voice, ambience and lips remain UNKNOWN on actual diagnostic. Caption render UNKNOWN; no SRT/render supplied. AV owns audio/words/timing, CONT object/identity, PERF joke/agency/readability, MASTER final/export. Exact dialogue/claim changes route P5/P2 + owner; no retention claim.

## Five-part handoff

1. **Đã xác định:** Four fixture responses complete; actual control matches bounded 8s map/format/hash checks; actual repeat adds B and 5.5s, corroborated by estimated repeated ASR pairs.
2. **Quyết định:** Repeat REWORK against expected map; cut1 approval cannot carry to cut2; no quality/canon/episode/release pass. Owner decision remains separate.
3. **Giả định:** Manifest executed map is supplied render provenance; intervals above use half-open notation and mapped-duration arithmetic. Fixture facts are fictional; actual outputs are same-source diagnostic copies, not production takes.
4. **Còn mở:** Safe cut at 2.5s, actual words/pronunciation, pops/masking, speaker turns, perceptual drift/lip-sync, motion/object states and captions need their corresponding evidence. No evidence here resolves these.
5. **Bước tiếp:** AV/owner targeted listening around diagnostic 2.5s and 8s plus quoted repeated regions; for production obtain selected approved takes and full versioned playback/caption render, route state checks to CONT and beat checks to PERF, then MASTER/P12 + owner final acceptance. Any new version receives its own QC.
