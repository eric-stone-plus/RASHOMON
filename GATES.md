# The Five Gates (五つの門)

QUINTE's five mandatory gates. **Parallel execution (~5s), hm-operated.** Shōmon gate layer makes a rapid "does this need QUINTE?" determination; if passed, the full pipeline executes.

Update: 憲門 (Kennōmon) added as Gate 5, ratified 2026-06-19 — architecture gate enforced by HIGHBALL's BANNIN layer. Shōmon now has two layers: the Shōmon gate, where hm makes a rapid judgment about whether the output is consequential; and Shōmon execution, where the full review protocol runs with hm per-phase synchronous veto.

## Gate 1: 雨門 Amamon · Ambiguity Gate

**Rashōmon metaphor**: The woodcutter walks through the Rashōmon gate in the rain — before entering, confirm what you are here to examine.

**Failure mode**: Wrong question asked.

**Trigger**: User question is ambiguous — vague intent, unclear scope, undefined reference.

**Action**: Must `clarify()` before acting. Do not guess.

**Design rationale**: Spending 30 minutes running a full QUINTE only to discover everyone misunderstood the question is far more expensive than asking one clarifying question.

**Operator**: hm (xhigh reasoning), executed in parallel in Phase -1.

**Naming**: ame = rain. The film opens in heavy rain at the Rashōmon gate. Amamon is the entry point — if the question is unclear, do not enter.

## Gate 2: 鏡門 Kyōmon · Mirror Gate

**Rashōmon metaphor**: The woodcutter checks his own eyes — "Did I see what I think I saw, or was it a trick of the light?" The mirror does not speak. It does not argue. It does not favor. It only reflects what is there.

**Failure mode**: hm comprehension error — hm makes directional factual errors in comparative analysis, based on memory/impression rather than line-by-line verification.

**Trigger**: Whenever hm is about to make a comparative claim — "A has X, B has Y," "local added Z compared to repo."

**Action**: Six rules —
1. **Bidirectional verification**: Independently verify each side of the comparison. For existence claims, cite `file:line`. For absence claims, cite the search command and result.
2. **Evidence anchoring**: Existence claims include exact location. Absence claims include search command and result.
3. **Directional explicitness**: state whether the comparison is local-to-repo, repo-to-local, or symmetric.
4. **Declared assumptions**: State baseline assumptions before each comparison, then verify and correct.
5. **Three-tier disposition**: confirmed means pass; falsified means hard block; uncertain means tag and pass.
6. **Memory declaration**: unsourced memory must be labeled `[memory/unsourced]` and treated as uncertain.

**Mechanical enforcement**: Every comparative statement must begin with `[鏡門 ✓]` followed by verification evidence.

**Operator**: hm (xhigh reasoning), executed in parallel in Phase -1.

**Naming**: kagami = mirror. Yata no Kagami, the sacred mirror that reflects truth without interpretation.

## Gate 3: 證門 Shōmon · Testimony Gate

**Rashōmon metaphor**: Witnesses testify inside the gate. Truth emerges when one witness, reviewing *another's* account, spots what that witness could not see about themselves.

**Two-layer design**:

Shōmon has a fast hm gate layer and a full execution layer. The gate layer is
intended to take about one second; the full execution layer typically takes
30-180 seconds.

### Gate Layer (Phase -1, hm parallel execution)

**Failure mode**: Unnecessary QUINTE (trivial query getting full debate) or missed QUINTE (conclusion user may rely on but not debated).

**Trigger**: User question may produce a conclusion the user will rely on.
**Action**: Rapid judgment. Consequential output enters the pipeline; non-consequential lookups such as "where is this file" skip QUINTE.
**Do not self-judge simplicity**: "This is too simple for QUINTE" = violation. Simple tasks hiding subtle errors are exactly why QUINTE exists.

### Execution Layer (Phase 0-6, hm-coordination + hm synchronous veto)

Pipeline phases:

1. Phase 0 records the agent manifest.
2. Phase 1 runs R1 parallel independent analysis.
3. Phase 2 auto-diffs claims into consensus, dispute, and residual pools.
4. Phase 3 runs R2 adversarial verification.
5. Phase 4 preserves consensus, contested claims, and residual provenance in a
   structured synthesis.
6. Phase 5 checks convergence; Phase 5a verifies executable claims with direct
   runtime evidence when needed.
7. Phase 6 produces the R3 dual verdict and residual trace.

Each phase is subject to hm synchronous veto: APPROVE, REJECT, ABORT, or MODIFY.

**Operator**: hm owns gate judgment. hm-coordination owns execution. hm owns
synchronous veto oversight.

**Naming**: shō = testimony, evidence. Shōmon is the complete gate + confrontation mechanism.

## Gate 4: 閂門 Kan'nukimon · Anti-Drift Gate

**Rashōmon metaphor**: The bolt — witnesses must not collude. Each testimony must be independent, uncontaminated by external associations.

**Failure mode**: Prompt contamination / concept collision.

**Trigger**: Every prompt dispatch to a host-bound perspective, debate party,
auditor, implementation route, or runtime-verification route.

**Action**: Three-layer defense —
1. **Task-first**: The specific task goes at the very beginning of the prompt
2. **Semantic isolation**: "ONLY Y" replaces "NOT X" — build a positive identity rather than suppressing a negative one
3. **Forced first-line restatement**: Require `TASK: [restatement]` — drift is caught in the first sentence, not after 120 seconds of wasted computation

**Operator**: hm (audits prompt wrapping during Phase -1 parallel execution).

**Naming**: kan'nuki = bolt, latch.

## Gate 5: 憲門 Kennōmon · Architecture Gate

**Rashōmon metaphor**: The constitution — the gate itself must not be rewritten by those it constrains. Architecture changes require adversarial review outside hm's session.

**Failure mode**: hm makes unilateral architecture changes (protocol rewrites, gate modifications, README restructuring) without QUINTE review. The constrained party is also the enforcer — text rules in SOUL.md are self-read, self-interpreted, self-enforced.

**Trigger**: `write_file`, `patch`, or `terminal(git commit/push)` targeting
public repo architecture files (`README*`, `specs/**`, `skills/**/SKILL.md`,
`ontology/**`, `lib/**`, or protocol scripts).

**Action**: BANNIN layer intercepts the write attempt and checks for a valid
verdict trail. When the verdict contains a residual trace, BANNIN also checks
that high-risk residuals are closed, blocked, waived, or not applicable with
evidence and scope. Without adequate trail or closure, the protected write is
blocked.

**Provenance**: Enforced by HIGHBALL's BANNIN layer and specified in HIGHBALL
`specs/residual-closure.md`. The gate is named for 憲 (ken = constitution,
fundamental law) + 門 (mon = gate).

**Naming**: ken = constitution, fundamental law. Kennōmon guards the architecture itself — no constitutional change without adversarial review.

## Execution Flow

Execution starts with the user question. hm evaluates the five gates in
parallel: Amamon for ambiguity, Kyōmon for comparative claims, Shōmon for
consequential testimony, Kan'nukimon for prompt drift, and Kennōmon for
architecture-changing writes.

When Shōmon passes, hm-coordination runs the execution phases listed above. hm
then presents the final result. Any push remains behind the KENGEN push gate.

## Key Clarifications

- **Shōmon ≠ execution pipeline.** Shōmon gate (~1s judgment) and Shōmon execution (pipeline) are two layers. The gate decides "enter the pipeline?" The execution layer is the pipeline itself.
- **All five gates are hm-operated gate checks in Phase -1**, each ~1-2s. They do not execute the full debate — they make entry decisions.
- **憲門 is enforced externally by HIGHBALL's BANNIN layer**, not by hm self-enforcement. This breaks the self-execution circularity (hm enforcing rules on itself).

*GATES.md — Five gates with 憲門 architecture gate (HIGHBALL/BANNIN-enforced), 2026-06-19, updated 2026-06-22*
