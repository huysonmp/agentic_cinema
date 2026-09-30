# Quality-agent expansion research v0.1

- **Date:** 2026-09-30.
- **Purpose:** rà các lỗ hổng kiểm duyệt/xây dựng nội dung ngoài Vietnamese Dialogue & Voice Editor cho series TikTok AI.
- **Status:** research-informed proposal; chưa phải owner-approved architecture.

## 1. Dữ kiện nền đã kiểm tra

### TikTok creative guidance

TikTok's official creative guidance emphasizes vertical/mobile-first creative, sound and motion, captions, a clear hook in the opening seconds, and testing different creative versions. The guidance is aimed at ads and is not a guarantee for organic series performance; it is a platform constraint signal, not a script formula.

Sources:

- https://ads.tiktok.com/business/en/guides/what-is-ad-creative-guide
- https://ads.tiktok.com/business/creativecenter/quicktok/online/5_creative_tips/pc/en
- https://ads.tiktok.com/help/article/split-testing?lang=en

### TikTok AI disclosure and provenance

TikTok's official AIGC guidance says creators should label completely AI-generated or significantly AI-edited content, and explains that Content Credentials/C2PA may help TikTok apply an automatic label. This is separate from a visible project disclosure chosen by the owner; both need a deliberate check.

Source: https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content?authuser=0

### Google Flow/Veo production constraints

Google Flow supports text-to-video, frames, ingredients/references, character references and (for supported Omni generations) voice references. The official model table shows different supported lengths/features by model, including short clips and model-specific limits; Flow also advises clean reference ingredients and non-conflicting prompts. Therefore a 30-second TikTok cannot be treated as one unconstrained generation: it needs shot decomposition, reference continuity and an edit plan.

Sources:

- https://support.google.com/flow/answer/16353334?hl=en
- https://support.google.com/flow/answer/16352836?hl=en

### Captions and accessible alternatives

W3C's prerecorded-media guidance recommends captions/transcripts or equivalent alternatives so information is not available only through one sensory channel. For this project, caption text is also a factual/claim surface, not merely decoration.

Source: https://www.w3.org/WAI/WCAG21/Understanding/audio-only-and-video-only-prerecorded

### Provenance standard

C2PA defines technical standards for certifying the source and history/provenance of media. It can support disclosure and asset records, but it does not replace human fact, cultural or creative review.

Source: https://spec.c2pa.org/specifications/

## 2. What the current system already covers

- Fact & Source Auditor: claim/source boundaries and provenance limits.
- Creative Explorers + Diversity Editor: concept breadth and duplicate detection.
- Audience-Pull, Dramaturgy, Character Chemistry: script-level creative critique.
- Cold Reader/Pairwise: proxy comprehension and comparison.
- Vietnamese Dialogue & Voice Editor: natural Vietnamese, voice and spoken rhythm.

These do not yet verify rendered video, Flow-specific feasibility, provenance/disclosure, captions or post-publication evidence.

## 3. Agents/checkers still needed

### Tier 1 — add before the first Veo generation

| Role | What it prevents | Stage/gate | Recommendation |
|---|---|---|---|
| **Cultural Context & Sensitivity Reviewer** | Local history/ritual/identity being flattened, disputed or stereotyped even when a sentence has a citation | P2/P3/P5, triggered by cultural sensitivity or conflicting sources | Add as an independent advisory role; owner decides. Not every episode needs an outside specialist, but the trigger must be explicit. |
| **Flow/Veo Shot & Prompt Feasibility Agent** | One 30s prompt asking for impossible continuity, lip-sync, eating/hand actions, camera moves or voice behavior | P7/P8 before any generation | Add. Decompose into feasible clips, reference ingredients, start/end frames, voice references, edit joins and credit assumptions. |
| **Character–Food Continuity Auditor** | Khoai/Đào face, body, voice, wardrobe, props, dish form or visual style drifting across clips | P6/P7 and after each generation batch | Add. Check against approved character sheets and food reference pack; do not approve a pretty but inconsistent frame. |
| **Rights, Provenance & AI-Disclosure Auditor** | Reusing source photos/people/brands; missing TikTok AI label or project disclosure; loss of provenance metadata | P6/P8/P13 | Add as one combined gate for this project. Split into legal specialist later if scope expands. |
| **Audio–Caption–Accessibility QC** | Vietnamese pronunciation, voice mismatch, lip-sync/audio timing, captions that change a claim, sound-off incomprehension | P6/P9/P10 | Add. Captions must be checked as factual text, not only spelling. |
| **Master/Platform QC** | Wrong 9:16, unreadable safe-zone text, duration/export defects, AI disclosure missing from final file, audio/video artifacts | P11/P12/P13 | Add as a deterministic checklist/validator first; an agent can summarize exceptions but should not replace the checklist. |

### Tier 2 — add after the first publishable pilot

| Role | Purpose | Why not before |
|---|---|---|
| **Audience Test & Analytics Analyst** | Distinguish actual retention/recall/comment signals from AI proxy opinions; compare one variable at a time | Needs real viewer exposure and a defined measurement plan. TikTok's official split-test guidance is for controlled ad tests; organic-post conclusions need a separate design. |
| **Series Learning Librarian** | Convert accepted/rejected hooks, voice fixes, continuity failures and audience evidence into reusable canon | Needs at least one or more real episodes; otherwise it stores speculation as “learning”. |

## 4. Important separation of authority

- Creative critics recommend; owner selects.
- Fact Auditor verifies claim support; it does not decide whether a scene is entertaining.
- Cultural Reviewer flags context/uncertainty; it does not impersonate a community or grant rights.
- Flow Feasibility Agent identifies technical risk; it does not authorize credit spend or generation.
- Rights/Disclosure Auditor can block release for an unresolved rights or disclosure issue.
- Master QC can block delivery for deterministic defects; it cannot improve weak writing.

## 5. Suggested minimum complete chain for EP01

`P2 Fact/Source → P2/P3 Cultural Context (if triggered) → P3 Brief → P4 Concept/Creative Critics → P5 Vietnamese Dialogue + Script Critics → P6 Character/Food Reference + Continuity → P7 Flow Feasibility/Shot Plan → P8 Prompt & Human Generation → P9 Audio/Caption/Accessibility → P10 Visual/Continuity QC → P11 Master/Platform/Disclosure/Rights → Owner release gate → post-publish Audience Evidence.`

This is a quality chain, not an autonomous pipeline. Human gates remain at claim use, concept/script lock, generation spend, asset rights and release.

## 6. Open decisions before implementing all roles

1. Should Cultural Context Reviewer be an internal agent with escalation, or should certain episodes require an external/local human reviewer?
2. What exact disclosure format does the owner want in-video/caption/post settings, in addition to TikTok's platform label?
3. Is the first pilot allowed to use Flow's custom voice/voice references, or must voice be added in post?
4. Which visual/voice properties are immutable canon for Khoai and Đào before P6 starts?
5. Which audience outcome is measured after publication: completion, recall of dish/place, saves/comments, or a defined combination?
