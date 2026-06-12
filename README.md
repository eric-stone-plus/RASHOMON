# RASHOMON (羅生門)

> 芥川龍之介《藪の中》（1922）→ 黒澤明《羅生門》（1950）→ multi-agent orchestrated truth-seeking

**RASHOMON** is the philosophical foundation of the QUINTE debate protocol. It asks the question QUINTE is built to answer: *when a single perspective cannot be trusted, how do we converge on actionable truth?*

## RASHOMON v3.1: The Orchestration-Oversight Separation

QUINTE v3.1 (2026-06-10) introduced a fundamental architectural insight: **the entity that executes the debate should not be the same entity that judges its quality.** This is not a technical preference — it is an epistemological necessity born from observed failure.

In v2.x, Hermes was both orchestrator (deciding who speaks, in what order, on what topic) and participant (producing analysis). This created an intrinsic conflict of interest: the orchestrator could unconsciously trim the debate to fit its own analytical conclusions — skipping agents it deemed "unnecessary," narrowing scope based on its own blind spots, treating its own R1 conclusions as ground truth for R2 synthesis. This was observed in production: hm dispatched only omp, omitting cc and cw (2026-06-07, twice). hm selected files from memory rather than enumerating complete manifests. hm declared "no other issues" on incomplete coverage. These were not discipline failures — they were structural consequences of conflating execution with oversight.

The v3.1 architecture (simplified from v3.0) separates these concerns:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        RASHOMON v3.1 — Architecture                          │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                    EXECUTION DOMAIN (Claude Code)                      │ │
│  │                                                                       │ │
│  │  ┌──────────────────────────────────────────────────────────────┐    │ │
│  │  │  PIPELINE: Phase 0→1→2→3→4→5→5a→6                            │    │ │
│  │  │  · Phase 0: Agent Manifest → mandatory participant list       │    │ │
│  │  │  · Phase 1: R1 4-Agent parallel (cc+cw+omp+hm)                │    │ │
│  │  │  · Phase 2: Auto-Diff claims → consensus/dispute pools        │    │ │
│  │  │  · Phase 3: R2 Adversarial — 3 refuters per dispute           │    │ │
│  │  │  · Phase 4: rx Cross-Judge — pure reasoning review            │    │ │
│  │  │  · Phase 5: Loop-Until-Dry — single critic + 3-round cap      │    │ │
│  │  │  · Phase 5a: omp Verification — LSP/DAP/exec claims           │    │ │
│  │  │  · Phase 6: KANSA Dual Verdict — Consul A + Auditor B  │    │ │
│  │  │  Epistemology: structural guarantees — cannot skip, cannot miss│    │ │
│  │  └──────────────────────────────────────────────────────────────┘    │ │
│  │                                                                       │ │
│  │  ┌──────────────────────────────────────────────────────────────┐    │ │
│  │  │  BASH (External Agents) — toolchain diversity                  │    │ │
│  │  │  · hermes chat -q    → hm (oversight + participant)            │    │ │
│  │  │  · codewhale exec    → cw (deep analysis + impl verification)  │    │ │
│  │  │  · reasonix run      → rx (pure reasoning cross-judge, R2 only)│    │ │
│  │  │  · omp               → omp (rapid reasoning + LSP/DAP)         │    │ │
│  │  │  Epistemology: toolchain diversity → decorrelated blind spots  │    │ │
│  │  └──────────────────────────────────────────────────────────────┘    │ │
│  │                                                                       │ │
│  │  ┌──────────────────────────────────────────────────────────────┐    │ │
│  │  │  GOVERNANCE LAYER (v3.1)                                      │    │ │
│  │  │  · Cost Circuit Breaker:  claims≤100, refutations≤50, loop≤5  │    │ │
│  │  │  · Poison Detection:      agent>50 claims→anomaly→KANSA check │    │ │
│  │  │  · State Persistence:     structured logs→~/.hermes/quinte/   │    │ │
│  │  │  · Human Intervention:    per-phase injection + dry→escalate  │    │ │
│  │  │  · Truth Verification:    code claims→Bash runtime execution  │    │ │
│  │  │  · Metrics: Fleiss' κ (consistency) + κ-drift (drift detect)  │    │ │
│  │  └──────────────────────────────────────────────────────────────┘    │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│                              JSON Protocol                                  │
│                           {phase_id, output,                                │
│                            claims_diff, status}                             │
│                                    │                                        │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                    OVERSIGHT DOMAIN (Hermes)                           │ │
│  │                                                                       │ │
│  │  ┌──────────────────────────────────────────────────────────────┐    │ │
│  │  │  FOUR GATES — Parallel Execution (~5s)                        │    │ │
│  │  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │    │ │
│  │  │  │ 雨門      │ │ 鏡門      │ │ 證門      │ │ 閂門      │       │    │ │
│  │  │  │ Amamon   │ │ Kyōmon   │ │ Shōmon   │ │Kan'nukimon│      │    │ │
│  │  │  │          │ │          │ │          │ │          │       │    │ │
│  │  │  │ambiguous?│ │comparat- │ │conclus-  │ │every      │      │    │ │
│  │  │  │→clarify  │ │ive claim?│ │ion user  │ │prompt:    │      │    │ │
│  │  │  │          │ │→bidirect-│ │may rely  │ │3-layer    │      │    │ │
│  │  │  │          │ │ional grep│ │on?→full  │ │wrapper +  │      │    │ │
│  │  │  │          │ │+[鏡門✓]  │ │R1+R2+R3  │ │TASK:1line │      │    │ │
│  │  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │    │ │
│  │  └──────────────────────────────────────────────────────────────┘    │ │
│  │                                                                       │ │
│  │  ┌──────────────────────────────────────────────────────────────┐    │ │
│  │  │  SYNCHRONOUS VETO — Per-Phase Blocking Authority              │    │ │
│  │  │                                                               │    │ │
│  │  │  After EVERY Phase:                                           │    │ │
│  │  │    cc → hm:  {phase_id, output, claims_diff, agent_status}    │    │ │
│  │  │    hm → cc:  APPROVE | REJECT(reason) | ABORT(reason)         │    │ │
│  │  │              | MODIFY(specification)                          │    │ │
│  │  │    15s timeout → cc PAUSE (never auto-continue)               │    │ │
│  │  │                                                               │    │ │
│  │  │  Veto Powers:                                                 │    │ │
│  │  │    · Drift Veto:    "topic slid from X→Y, return to X"        │    │ │
│  │  │    · Omission Veto: "missing cw security analysis, add"       │    │ │
│  │  │    · Quality Veto:  "omp claims lack evidence, reject"        │    │ │
│  │  │    · Cascade Veto:  "error cascade formed, ABORT→Phase 1"     │    │ │
│  │  └──────────────────────────────────────────────────────────────┘    │ │
│  │                                                                       │ │
│  │  ┌──────────────────────────────────────────────────────────────┐    │ │
│  │  │  CONTEXT INJECTION + USER COMMUNICATION                       │    │ │
│  │  │  · session_search + memory → structured preamble for cc       │    │ │
│  │  │  · TUI resident: real-time user interaction                   │    │ │
│  │  │  · Browser/CDP: external information cc cannot access         │    │ │
│  │  │  · Desktop automation: system-level operations                │    │ │
│  │  │  · Fallback orchestrator: cc failure → hm takes over          │    │ │
│  │  └──────────────────────────────────────────────────────────────┘    │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                         EXECUTION FLOW                                 │ │
│  │                                                                       │ │
│  │  User Question                                                        │ │
│  │      │                                                                │ │
│  │      ▼                                                                │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase -1: hm Four Gates│ ← hm parallel (~5s)                       │ │
│  │  │ 雨門+鏡門+證門+閂門  │                                             │ │
│  │  → hm context inject      │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 0: Manifest    │ ← Agent(registry) → participant list       │ │
│  │  │ cc add-only → hm sign│                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 1: R1 4-Agent  │ ← cc parallel{cc,cw,omp,hm}                │ │
│  │  │ independent analysis │   TASK: first-line anchor                   │ │
│  │  │ → hm sync sign-off   │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 2: Auto-Diff   │ ← claims diff → consensus/dispute pools    │ │
│  │  │ → hm sign-off        │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 3: R2 Adversarial│ ← per-dispute 3 refuters                   │ │
│  │  │ ≥2/3 refute→drop     │   1/3→contested keep                        │ │
│  │  │ → hm sign-off        │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 4: rx Cross-Judge│ ← structured claims (read-only)             │ │
│  │  │ pure reasoning verdict│   → hm sign-off                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 5: loop-until  │ ← single critic + 3-round cap              │ │
│  │  │ -dry Convergence     │   dry→escalate human                        │ │
│  │  │ → hm sign-off        │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 5a: omp Verify │ ← LSP/DAP/exec ≤5 high-impact claims       │ │
│  │  │ verified/falsified   │   → feeds Phase 5 convergence               │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 6: KANSA Dual  │ ← Consul A (hm) + Auditor B                │ │
│  │  │ Verdict         │   consensus/dissent → hm final sign-off     │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ hm Final + push gate │ ← structured log → ~/.hermes/quinte/        │ │
│  │  │ Phase 6a cross-match │   replay-auditable                           │ │
│  │  └──────────────────────┘                                             │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Mathematical Foundations

> ⚠️ The relationship between QUINTE and ML Rashomon Set theory is **heuristic, not isomorphic**. QUINTE lacks the formal prerequisites — loss function, optimal model, ground truth. Partial Order consensus (JMLR 2023) is the strongest structural analogy. See [references/mathematical-foundations.md](references/mathematical-foundations.md).

### Model Multiplicity (Breiman 2001)

The mathematical existence proof for QUINTE's core premise. In ML, many models with different structures achieve near-identical performance — single-model feature importance is unreliable. QUINTE extends this insight: a single agent's analysis is unreliable not because the agent is flawed, but because **model multiplicity is a mathematical property of underdetermined problem spaces**.

### Partial Order Consensus (JMLR 2023, Peer-Reviewed)

When only statements on which **all** models agree are retained, the result is a partial order — pairs where consensus exists are ranked; pairs with conflicting evidence are left **incomparable**. This is the exact mechanism of QUINTE's R2 consensus detection: unanimous claims enter the consensus pool, contested claims are deferred. The theorem that partial orders are "conservative over total rankings" mirrors QUINTE's design — R3 verdicts are a subset of what any individual agent would claim.

### Rashomon Ratio

`|consensus claims| / |union of all claims|` — a stability coefficient for R3 verdicts. High ratio → robust across perspectives. Low ratio despite convergence → **Rashomon-fragile**, surface as warning.

## The Four Gates

Four gates, four failure modes. Each gate is a mandatory checkpoint operated by hm in Phase -1, running in parallel (~5s). They are not ceremonial — each prevents a class of error that has been observed in production and caused by the previous architecture. The gates follow the woodcutter's journey in Kurosawa's *Rashomon*: arrive in rain at the gate, check your own eyes before you look at others, let the witnesses testify, then bolt the door so no one colludes.

### 雨門 Amamon · Ambiguity Gate

> *「雨が降っている。門の下で、樵夫は立ち止まる。」— "It is raining. Under the gate, the woodcutter stops."*

The first gate, named for the rain (雨 *ame*) that opens the film — the uncertainty that shrouds every question before it is examined. Before any agent can analyze, before any debate can begin, someone must ask: **do I actually understand what is being asked?**

This seems trivial. It is not. The most expensive mistake in multi-agent debate is running five agents through R1+R2+R3 only to discover everyone misunderstood the question. Amamon catches this at the source. When hm detects ambiguity in the user's question — vague intent, unclear scope, undefined reference — it must `clarify()` rather than guess. The cost of asking one clarification is approximately zero. The cost of a full QUINTE on a misunderstood question is five API calls, three rounds, and a wrong conclusion the user will rely on.

**Failure mode**: Wrong question asked. **Trigger**: Ambiguous user input. **Action**: Clarify first, debate later. **Operator**: hm (xhigh reasoning).

### 鏡門 Kyōmon · Mirror Gate

> *「鏡は語らない。ただ映すだけだ。」— "The mirror does not speak. It only reflects."*

The second gate is named for the sacred mirror (鏡 *kagami*), Yata no Kagami (八咫鏡) — the mirror that reflects truth without interpretation, without argument, without favor. Kyōmon addresses the most insidious error in the system: **hm's own comprehension mistakes.**

hm has a documented tendency to make directional factual errors when comparing sources — claiming "local added X" when X existed in the remote, asserting "repo has the better Y" when local was the updated version. These errors propagate: a wrong premise in hm's R1 becomes a wrong basis for every other agent's analysis. Kyōmon intercepts this before the debate pipeline starts.

Six rules govern the mirror: bidirectional grep verification on both sides of every comparison, evidence anchored to file:line positions, explicit directional arrows (LOCAL→REPO / REPO→LOCAL / SYMMETRIC), stated baseline assumptions, three-tier disposition (✅ pass / 🛑 falsified→block / ⚠️ uncertain→tag), and memory-claim labeling. The mechanical enforcement: every comparative statement must begin with `[鏡門 ✓]` followed by verification evidence.

This gate was promoted from a sub-gate of Shōmon to an independent gate in 2026-06-08 after a QUINTE audit discovered that hm had made three directional errors in a single analysis. The reasoning: contamination must be intercepted *before* it enters the debate pipeline, not caught mid-stream.

**Failure mode**: hm comprehension error — directional factual mistakes based on memory rather than source verification. **Trigger**: Any comparative claim by hm. **Action**: Bidirectional grep, evidence anchoring, three-tier disposition. **Operator**: hm (xhigh reasoning, self-auditing).

### 證門 Shōmon · Testimony Gate

> *「証人たちは門の中で語る。一人の証言を別の者が読み、その者が自分では見えなかったものを見つける。」— "The witnesses testify inside the gate. One reads another's account and finds what that witness could not see about themselves."*

The third gate, 證 (*shō* = testimony, evidence), is the gate of witness confrontation. This is where the Rashomon problem meets its solution: no single perspective can be trusted, so we create a structure where perspectives must confront each other.

v3.1 gives Shōmon a two-layer design. The **gate layer** (~1s, hm) makes a fast determination: is this question likely to produce a conclusion the user will rely on? If yes → authorize the full cc Workflow pipeline. If no (trivial file lookup, deterministic measurement, single-tool query with zero reasoning) → skip. The gate layer prevents wasting five agents on "where is this file" while ensuring nothing consequential slips through.

The **execution layer** (30-180s, cc Workflow) is the full QUINTE pipeline: Phase 0 manifest generation, Phase 1 R1 four-agent parallel analysis, Phase 2 auto-diff claim extraction, Phase 3 R2 cross-model adversarial verification, Phase 4 rx pure reasoning cross-judgment, Phase 5 loop-until-dry convergence, Phase 6 KANSA Dual Verdict. hm holds synchronous veto at every phase boundary — APPROVE, REJECT, ABORT, or MODIFY. The veto is blocking: cc cannot proceed without hm's approval. 15 seconds of silence triggers a PAUSE, never an auto-continue.

The gate layer and execution layer were conflated in v2.x — Shōmon was described as both "the check" and "the pipeline itself." v3.1 separates them explicitly. The gate opens the door. The pipeline walks through it.

**Failure mode**: Single-perspective bias. **Trigger**: Conclusion the user may rely on. **Action**: Gate layer → authorize. Execution layer → full R1+R2+R3 pipeline with hm per-phase veto. **Operator**: hm (gate) + cc Workflow (execution) + hm (supervision).

### 閂門 Kan'nukimon · Bolt Gate

> *「閂をかける。証人たちは互いに話してはならない。」— "Bolt the door. The witnesses must not speak to each other."*

The fourth gate, 閂 (*kan'nuki* = bolt, latch), is the anti-collusion gate. Its function is to ensure that every external agent receives an independent, uncontaminated prompt — no witness sees another's testimony before producing their own.

This gate exists because of a specific, repeatedly observed failure: agents share a concept namespace. When cc or cw see certain keywords in their prompt, their training-data associations activate — and the agent drifts from the assigned task to a tangentially related topic it "knows more about." This is not malicious. It is a fundamental property of LLM attention: strong concept associations in training data override explicit instructions.

Kan'nukimon enforces a three-layer defense on every prompt to external agents:
1. **Task-first**: the specific task (not context, not constraints) goes at the very beginning of the prompt — the agent's attention lands on the task before anything else
2. **ONLY Y, not NOT X**: positive framing ("Your ONLY function: cross-review this file for claim consistency") replaces negative framing ("Do NOT inspect hermes-desktop") — negation creates the very association it tries to suppress
3. **TASK: restatement**: every agent's first line of output must restate what it understands its task to be. Drift is caught in the first sentence, not discovered after 120 seconds of wasted computation.

The gate takes its name from the bolt on the Rashōmon gate — once the witnesses are inside, they must not coordinate their stories. Each prompt is a sealed chamber. Each agent sees only what it needs to see.

**Failure mode**: Prompt contamination — agents drift to training-data associations, producing irrelevant output. **Trigger**: Every prompt to external agents (cc, cw, omp, rx). **Action**: Three-layer wrapper on all prompts. **Operator**: hm (prompt construction).

---

## Why cc? Three Mechanisms, Three Epistemologies

Claude Code possesses three native mechanisms that Hermes cannot replicate. They are not "better tools" — they are a different category of capability:

| Mechanism | Epistemological Contribution | Failure Mode Prevented |
|-----------|------------------------------|------------------------|
| **Agent** (internal sub-agent) | Independent context → freedom from orchestrator's attentional biases | Single-context information overload + confirmation bias |
| **Workflow** (orchestration engine) | Structural guarantees: pipeline cannot skip, schema cannot overlook | Manual dispatch omission, output format ambiguity, false convergence |
| **Bash** (external agents) | Toolchain diversity → decorrelated blind spots across hm/cw/rx/omp | Single-toolchain shared blindness |

**Structural vs Disciplinary Guarantees.** v2.x relied on hm's discipline — "never skip an agent," "always enumerate all files," "never self-judge simplicity." These were repeatedly violated not because hm was careless but because the role of orchestrator-as-participant made them structurally unenforceable. v3.1 replaces disciplinary rules with structural guarantees: `pipeline()` cannot skip an item; `agent({schema})` cannot produce an unparseable claim; `parallel()` cannot accidentally serialize.

## Why hm Retains Veto Power

The separation is not about "cc is better than hm." It is about comparative advantage:

- **cc's strength**: executing complex multi-step orchestration with structural guarantees. max reasoning (32000 tokens) models full dependency topology. Workflow primitives eliminate entire classes of execution error.
- **hm's strength**: persistent session memory (session_search), cross-debate context, user relationship, browser/desktop access, and — critically — the ability to see what cc's execution pattern hides. xhigh reasoning applied to audit, not to dispatch.

The synchronous veto — hm must APPROVE every phase output before cc proceeds — ensures oversight is real, not ceremonial. hm can ABORT on error cascade, REJECT on quality, MODIFY on omission. This is not a downgrade from v2.4's orchestrator role. It is applying hm's best capability (xhigh reasoning) to the hardest problem (auditing orchestration quality) rather than wasting it on mechanical dispatch.

## The Rashomon Problem

Kurosawa's *Rashomon* (1950) presents four witnesses to the same event offering mutually contradictory testimonies. Not because anyone is lying — but because each person sees only what their position allows them to see.

This is the exact problem facing single-agent AI systems. One model, one perspective, one blind spot. The answer isn't a better model — it's a *structure that forces perspectives to confront each other*.

The deeper property — the one that makes RASHOMON a paradigm, not just a voting scheme — is **cross-detection**: an agent reviewing *another's* output in R2 can spot errors it could never have caught in its own R1. Self-review is epistemologically closed — you cannot see the blind spot you are standing in. Cross-review breaks that closure. The value is not "majority wins" — it is that the error an agent cannot self-detect is precisely the error another agent's position allows it to see.

### v3.1 Extension: Cross-Model Adversarial Depth

v2.x treated all four witnesses as epistemologically equivalent — four DeepSeek instances with different system prompts. v3.1 recognizes that **same-model consensus is weaker than cross-model consensus.** Three DeepSeek instances agreeing gives you 1 verification with 3 samples of the same noise distribution. Cross-model adversarial verification (≥1 refuter from different provider in Phase 3) decorrelates errors across architectures, training data, and RLHF alignment — producing genuinely independent verification rather than same-model echo.

## The Cost Question: "Is This Just Brute Force?"

loop-until-dry + adversarial verification per dispute + 5 agents per round can scale to hundreds of API calls per debate. Is this *«при достаточной тяге и кирпич полетит»* ("with enough thrust, even a brick will fly") — brute force?

> Soviet aviation engineering proverb, apocryphal. Attributed to the MiG design bureau culture (MiG-25 / MiG-31 era), where massive engines and robust airframes compensated for material and aerodynamic limitations. The American equivalent — "a triumph of thrust over aerodynamics" — was coined for the F-4 Phantom II.

The answer has two layers:

**Layer 1 — Yes, it is brute force, and that is the point.** DeepSeek API pricing (~$0.14/M input, ~$0.28/M output tokens) makes a full 5-agent debate cost approximately $0.01–0.05. At that price, the marginal cost of another round of cross-verification is negligible relative to the cost of an undetected error. v3.1's cost circuit breaker (claims≤100, refutations≤50, loops≤5) bounds the worst case to approximately $1–3 per debate — cheaper than 5 minutes of human review.

**Layer 2 — But brute force without structure is just expensive noise.** loop-until-dry with dual-condition termination (not just "keep going") and escalate-to-human (not auto-accept) ensures the brute force has a stopping criterion. Cross-model adversarial verification ensures the brute force isn't just same-model echo. The governance layer ensures the brute force doesn't run away.

The philosophical position: **epistemic certainty is expensive. v3.1 makes it cheap enough to be default-on, with structural guards against runaway cost.** If DeepSeek were $15/M tokens instead of $0.15, the architecture would be different. The economics enable the epistemology.

## Structure

| File | Content |
|------|---------|
| [GATES.md](GATES.md) | The Four Gates — 雨門·鏡門·證門·閂門 (v3.1: parallel, cc-backed) |
| [CONCEPTS.md](CONCEPTS.md) | Core concepts — Orchestration-Oversight Separation, Rashomon Depth, YNI, Refined Brute Force |
| [PHENOMENOLOGY.md](PHENOMENOLOGY.md) | Phenomenology of the orchestrated gaze — the philosophical dimensions |
| [references/mathematical-foundations.md](references/mathematical-foundations.md) | Mathematical foundations — Model Multiplicity, Partial Order Consensus, Rashomon Ratio |

## Ecosystem

| Repo | Role | Question |
|------|------|----------|
| [RASHOMON](https://github.com/eric-stone-plus/RASHOMON) | Design philosophy | *Why* multi-perspective truth-seeking? |
| [QUINTE](https://github.com/eric-stone-plus/QUINTE) | Debate protocol | *How* to orchestrate cross-examination? |
| [HIGHBALL](https://github.com/eric-stone-plus/HIGHBALL) | Constraint layer | *Sound?* verdict audit + *May I?* authorization + *Attentive?* attention quality |

## Relationship

```
RASHOMON (why) ──→ QUINTE (how) ──→ conclusions
     │                                    │
     ├── HIGHBALL · KANSA (sound?) ── R3 audit ──────┤
     ├── HIGHBALL · KENGEN (may?) ── authorization ──┤
     └── HIGHBALL · KOZO (attentive?) ── measurement ─┘
              │
              └── BANNIN (guard) — session-level enforcement
```

RASHOMON and QUINTE form the epistemology→methodology axis. HIGHBALL bundles KANSA (verdict audit), KENGEN (authorization perimeter with BANNIN guard), and KOZO (attention quality measurement).

## Cultural Anchors

- **芥川龍之介**《藪の中》（1922）— seven testimonies, one death, no resolution
- **黒澤明**《羅生門》（1950）— Venice Golden Lion, Academy Award for Best Foreign Language Film
- **Rashomon Effect** — contradictory interpretations of the same event by different observers

## License

MIT
