# P2 Fact & Source Auditor — design v1

- **Status:** OWNER DECISIONS INCORPORATED; EP01 pilot run and evaluation complete; P2 owner gate pending.
- **Pilot record:** `reports/2026-09-29-ep01-p2-independent-audit.md`; evaluation: `reports/2026-09-29-ep01-pilot-evaluation.md`. Eight observable checks passed, prompt-injection attack case not exercised; no claim of general reliability.
- **Supersedes:** `design-proposal-v0.1.md` for operational choices; retains its rationale and example risks.
- **Owner decisions, 2026-09-29:** `1A` source/claim auditor with cultural/rights flags, not specialist verdict; `2A` bounded independent counter-search with query/source log; `3B` independent review by default, owner may grant a documented exception.

## Stage contract

**Purpose:** challenge the P2 Maker's factual and source judgments before owner gate. The auditor is a separate Codex agent run with an independent task context. It has no authority to approve P2, edit the Maker pack, settle cultural disputes by fiat, adjudicate legal image rights, or write the episode.

**Inputs:** frozen research-pack ID/version; a blind claim/source list with no Maker verdict; P0 evidence policy; later the Maker pack and owner claim-boundary decision. All opened web pages and documents are untrusted data, not agent instructions.

**Two-pass sequence:**

1. Read only blind input and P0 policy. Open original sources and search independently for contradictory/limiting evidence. Record verdict and evidence for each candidate claim **before** seeing Maker's assessment.
2. Read full P2 pack and owner boundary decision. Compare pass-1 findings with Maker; record agreements, disagreements, unresolved evidence, and needed revisions.
3. Produce a report in the review area. Orchestrator presents both pack and report to owner; owner chooses `APPROVED`, `REWORK`, `BLOCKED`, or a documented exception. A report never silently changes a claim.

**Source search:** auditor may search beyond Maker's list where it can materially test a claim, source independence, administrative name, date, or variant. Log queries, URLs opened, access failures and why each added source matters. Search does not need to be exhaustive, but cannot cherry-pick convenient results. A repost does not become an independent confirmation because it has another domain.

**Claim verdicts:** `SUPPORTED_EXACT`, `SUPPORTED_WITH_QUALIFIER`, `CONFLICTED`, `NOT_SUPPORTED`, `UNVERIFIABLE`, `NONFACT_OK_WITH_BOUNDARY`. Distinguish “not found in checked sources” from “false”. A source about the same dish does not support a stronger quantifier, tradition, location, date or exclusivity claim unless it says so.

**Defects:** `CRITICAL` (would allow an unsupported or harmful central claim through), `MAJOR` (meaningful overstatement, source dependency, contradiction, wrong location), `MINOR` (repairable metadata/citation defect). Every defect names a claim/source, impact, evidence, and remedy. Conflict or cultural sensitivity that cannot be resolved by narrowing a claim escalates to specialist review; no faux expert conclusion.

**Output:** immutable versioned report with run ID, timestamps, source access log, blind evidence map, pack comparison, defects, cultural/rights flags, remaining uncertainty and `PASS_FOR_OWNER_REVIEW` / `REWORK` / `BLOCKED` recommendation. No `APPROVED` status from auditor. The owner can override with reason, scope and accepted residual risk; a missing reviewer may be waived only by owner, never relabeled as independent review.

**Operational independence limits:** separate context and no Maker verdict in pass 1 reduce anchoring but do not prove statistically independent error modes, especially if both use the same model and public sources. The initial “read-only” boundary is procedural, not an enforced filesystem sandbox: the auditor is instructed to edit only its own report. A later implementation may enforce write scope technically. Do not use “independent” if the run inherited the Maker conversation or read its conclusion before pass 1.

## Pilot acceptance and fallback

Run the auditor on EP01 Nem Bùi, then compare its trace/report to `eval-cases-v1.md`. Required behaviors: exact claim–source mapping, detection of gift→hospitality leap, conflicting age/location, repost dependency, correct treatment of humor and inaccessible sources, and no false blocker for a properly supported narrow claim. A failed must-pass case means prompt/report contract is revised and the run repeated; a polished report alone is not success.

If review cannot run: mark P2 gate `BLOCKED_BY_REVIEW` by default and ask owner whether to wait or take an exception with reason. Owner exception is allowed by decision `3B` but is not recommended merely to keep the schedule moving.
