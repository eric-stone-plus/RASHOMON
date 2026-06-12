# The Four Gates (四つの門)

QUINTE v3.1's four mandatory gates. **Parallel execution (~5s), hm-operated.** Shōmon gate layer makes a rapid "does this need QUINTE?" determination; if passed, cc Workflow executes the full pipeline.

v3.1 change: gates changed from serial to parallel. Shōmon (formerly hm manually dispatching R1+R2+R3) now has two layers: ① Shōmon gate — hm rapid judgment "consequential output? → enter cc pipeline" (~1s); ② Shōmon execution — cc Workflow full R1→R2→R3→loop-until-dry→KANSA pipeline, hm per-Phase synchronous veto.

---

## Gate 1: 雨門 Amamon · Ambiguity Gate

**Rashōmon metaphor**: The woodcutter walks through the Rashōmon gate in the rain — before entering, confirm what you are here to examine.

**Failure mode**: Wrong question asked.

**Trigger**: User question is ambiguous — vague intent, unclear scope, undefined reference.

**Action**: Must `clarify()` before acting. Do not guess.

**Design rationale**: Spending 30 minutes running a full QUINTE only to discover everyone misunderstood the question is far more expensive than asking one clarifying question.

**v3.1 operator**: hm (xhigh reasoning), executed in parallel in Phase -1.

**Naming**: 雨 (あめ / ame) = rain. The film opens in heavy rain at the Rashōmon gate. Amamon is the entry point — if the question is unclear, do not enter.

---

## Gate 2: 鏡門 Kyōmon · Mirror Gate

**Rashōmon metaphor**: The woodcutter checks his own eyes — "Did I see what I think I saw, or was it a trick of the light?" The mirror does not speak. It does not argue. It does not favor. It only reflects what is there.

**Failure mode**: hm comprehension error — hm makes directional factual errors in comparative analysis, based on memory/impression rather than line-by-line verification.

**Trigger**: Whenever hm is about to make a comparative claim — "A has X, B has Y," "local added Z compared to repo."

**Action**: Six rules —
1. **Bidirectional verification**: Independently verify each side of the comparison. Exists → `file:line`. Missing → search command + result.
2. **Evidence anchoring**: Existence claims include exact location. Absence claims include search command and result.
3. **Directional explicitness**: `LOCAL → REPO` / `REPO → LOCAL` / `SYMMETRIC`.
4. **Declared assumptions**: State baseline assumptions before each comparison, then verify and correct.
5. **Three-tier disposition**: ✅ confirmed → pass / 🛑 falsified → hard block / ⚠️ uncertain → tag and pass.
6. **Memory declaration**: No retrievable source → `[memory/unsourced]`, ⚠️ tier.

**Mechanical enforcement**: Every comparative statement must begin with `[鏡門 ✓]` followed by verification evidence.

**v3.1 operator**: hm (xhigh reasoning), executed in parallel in Phase -1.

**Naming**: 鏡 (かがみ / kagami) = mirror. Yata no Kagami (八咫鏡), the sacred mirror that reflects truth without interpretation.

---

## Gate 3: 證門 Shōmon · Testimony Gate

**Rashōmon metaphor**: Witnesses testify inside the gate. Truth emerges when one witness, reviewing *another's* account, spots what that witness could not see about themselves.

**v3.1 two-layer design**:

```
Shōmon = gate layer (hm, ~1s) + execution layer (cc Workflow, 30-180s)
```

### Gate Layer (Phase -1, hm parallel execution)

**Failure mode**: Unnecessary QUINTE (trivial query getting full debate) or missed QUINTE (conclusion user may rely on but not debated).

**Trigger**: User question may produce a conclusion the user will rely on.
**Action**: Rapid judgment — consequential output? → enter cc pipeline. Non-consequential (e.g., "where is this file") → skip QUINTE.
**Do not self-judge simplicity**: "This is too simple for QUINTE" = violation. Simple tasks hiding subtle errors are exactly why QUINTE exists.

### Execution Layer (Phase 0-6, cc Workflow + hm synchronous veto)

cc Workflow pipeline:
```
Phase 0: Agent manifest generation
Phase 1: R1 — parallel four-agent independent analysis
Phase 2: Auto-diff claims consensus/dispute
Phase 3: R2 — cross-model adversarial verification
Phase 4: rx cross-judgment + cross-round consistency review
Phase 5: loop-until-dry convergence
Phase 6: KANSA audit (監査)
───────────────────────
Each Phase: hm synchronous veto (APPROVE/REJECT/ABORT/MODIFY)
```

**v3.1 operator**: hm (gate judgment) → cc Workflow (execution engine) + hm (synchronous veto oversight).

**Naming**: 證 (しょう / shō) = testimony, evidence. Shōmon is the complete gate + confrontation mechanism.

---

## Gate 4: 閂門 Kan'nukimon · Anti-Drift Gate

**Rashōmon metaphor**: The bolt — witnesses must not collude. Each testimony must be independent, uncontaminated by external associations.

**Failure mode**: Prompt contamination / concept collision.

**Trigger**: Every prompt dispatch to external agents (cc, cw, omp, rx).

**Action**: Three-layer defense —
1. **Task-first**: The specific task goes at the very beginning of the prompt
2. **Semantic isolation**: "ONLY Y" replaces "NOT X" — build a positive identity rather than suppressing a negative one
3. **Forced first-line restatement**: Require `TASK: [restatement]` — drift is caught in the first sentence, not after 120 seconds of wasted computation

**v3.1 operator**: hm (audits prompt wrapping during Phase -1 parallel execution) + cc (auto-applies three-layer wrapping during Workflow agent dispatch).

**Naming**: 閂 (かんぬき / kan'nuki) = bolt, latch.

---

## Execution Flow (v3.1)

```
User Question
  │
  ▼
┌─────────────────────────────────────────────────────────┐
│  Four Gates — hm parallel (~5s)                          │
│                                                         │
│  ┌──────┐ ┌──────┐ ┌──────────┐ ┌──────┐              │
│  │ 雨門 │ │ 鏡門 │ │ 證門(gate)│ │ 閂門 │              │
│  │      │ │      │ │          │ │      │              │
│  │ambiguous│compar-│ │conclusion│ │prompt│              │
│  │?→     │ │ative  │ │user may  │ │contam?│             │
│  │clarify│ │claim? │ │rely on?  │ │→3-layer│            │
│  │       │ │→verify│ │→pipeline │ │wrapper│             │
│  └──┬───┘ └──┬───┘ └────┬─────┘ └──┬───┘              │
│     └────────┴──────────┴──────────┘                    │
│               hm context injection                       │
└──────────────────┬──────────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────────┐
│  cc Workflow — Shōmon execution layer                    │
│                                                         │
│  Phase 0: Agent manifest → mandatory participant list   │
│  Phase 1: R1 parallel 4-agent (cc/hm/cw/omp)           │
│  Phase 2: Auto-diff claims (consensus/dispute pools)    │
│  Phase 3: R2 cross-model adversarial (per-dispute 3 ref)│
│  Phase 4: rx cross-judgment          │
│  Phase 5: loop-until-dry (single critic + 3-round cap) │
│  Phase 6: KANSA audit (Consul A + Auditor B)   │
│  ─────────────────────────────────────                  │
│  Each Phase: hm sync veto (APPROVE/REJECT/ABORT/MODIFY) │
└──────────────────┬──────────────────────────────────────┘
                   ▼
              hm final presentation + push gate
```

## Key Clarifications

- **Shōmon ≠ cc Workflow pipeline.** Shōmon gate (~1s judgment) and Shōmon execution (pipeline) are two layers. The gate decides "enter the pipeline?" The execution layer is the pipeline itself.
- **All four gates are hm-operated gate checks in Phase -1**, each ~1-2s. They do not execute the full debate — they make entry decisions.
- **cc Workflow is the execution engine authorized by Shōmon**, not Shōmon itself.

---

*GATES-v3.1.md — Shōmon two-layer gate-vs-pipeline design + parallel execution, 2026-06-09, updated 2026-06-10*
