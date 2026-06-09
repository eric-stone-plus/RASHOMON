# RASHOMON (羅生門)

> 芥川龍之介《藪の中》（1922）→ 黒澤明《羅生門》（1950）→ Claude Code orchestrated truth-seeking

**RASHOMON** is the philosophical foundation of the QUINTE debate protocol. It asks the question QUINTE is built to answer: *when a single perspective cannot be trusted, how do we converge on actionable truth?*

## v3.0: The Orchestration-Oversight Separation

QUINTE v3.0 (2026-06-09) introduced a fundamental architectural insight: **the entity that executes the debate should not be the same entity that judges its quality.** This is not a technical preference — it is an epistemological necessity born from observed failure.

In v2.x, Hermes was both orchestrator (deciding who speaks, in what order, on what topic) and participant (producing analysis). This created an intrinsic conflict of interest: the orchestrator could unconsciously trim the debate to fit its own analytical conclusions — skipping agents it deemed "unnecessary," narrowing scope based on its own blind spots, treating its own R1 conclusions as ground truth for R2 synthesis. This was observed in production: hm dispatched only omp, omitting cc and cw (2026-06-07, twice). hm selected files from memory rather than enumerating complete manifests. hm declared "no other issues" on incomplete coverage. These were not discipline failures — they were structural consequences of conflating execution with oversight.

The v3.0 architecture separates these concerns:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        RASHOMON v3.0 — Architecture                          │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                    EXECUTION DOMAIN (Claude Code)                      │ │
│  │                                                                       │ │
│  │  ┌──────────────────────────────────────────────────────────────┐    │ │
│  │  │  MECHANISM 1: Agent (Internal Sub-Agents)                     │    │ │
│  │  │  · Explore:     full file enumeration (replaces hm memory)    │    │ │
│  │  │  · Plan:        architecture validation                       │    │ │
│  │  │  · general-purpose: completeness critic / poison detection    │    │ │
│  │  │  · Manifest Agent: reads registry → mandatory participant list│    │ │
│  │  │  · Cross-Round Agent: R1→R2→R3 stance drift detection        │    │ │
│  │  │  Epistemology: independent contexts → decorrelated attention   │    │ │
│  │  └──────────────────────────────────────────────────────────────┘    │ │
│  │                                                                       │ │
│  │  ┌──────────────────────────────────────────────────────────────┐    │ │
│  │  │  MECHANISM 2: Workflow (Orchestration Engine)                 │    │ │
│  │  │  · pipeline():  R1→diff→R2 adversarial→rx→loop-until-dry→KANSA│   │ │
│  │  │  · parallel():  4-agent R1 dispatch / per-dispute 3 refuters  │    │ │
│  │  │  · agent({schema}): JSON Schema enforced structured output    │    │ │
│  │  │  · Adversarial Verification: per-disagreement 3 refuter agents│    │ │
│  │  │  · loop-until-dry: dual-condition convergence + escalate      │    │ │
│  │  │  Epistemology: structural guarantees — cannot skip, cannot miss│    │ │
│  │  └──────────────────────────────────────────────────────────────┘    │ │
│  │                                                                       │ │
│  │  ┌──────────────────────────────────────────────────────────────┐    │ │
│  │  │  MECHANISM 3: Bash (External Agents)                          │    │ │
│  │  │  · hermes chat -q "..."    → hm (oversight + participant)     │    │ │
│  │  │  · codewhale exec --auto   → cw (deep analysis + impl verify) │    │ │
│  │  │  · reasonix run --effort max → rx (pure reasoning cross-judge)│    │ │
│  │  │  · omp "..."               → omp (rapid reasoning + security) │    │ │
│  │  │  Epistemology: toolchain diversity → decorrelated blind spots │    │ │
│  │  └──────────────────────────────────────────────────────────────┘    │ │
│  │                                                                       │ │
│  │  ┌──────────────────────────────────────────────────────────────┐    │ │
│  │  │  GOVERNANCE LAYER (v3.0)                                      │    │ │
│  │  │  · Cost Circuit Breaker:  claims≤100, refutations≤50, loop≤5  │    │ │
│  │  │  · Poison Detection:      agent>50 claims→anomaly→KANSA check │    │ │
│  │  │  · State Persistence:     structured logs→~/.hermes/quinte/   │    │ │
│  │  │  · Human Intervention:    per-phase injection + dry→escalate  │    │ │
│  │  │  · Truth Verification:    code claims→Bash runtime execution  │    │ │
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
│  │  │  │"Am I     │ │"Did I    │ │"Does this│ │"No witness│      │    │ │
│  │  │  │ asking   │ │ see what │ │ need full│ │ collusion"│      │    │ │
│  │  │  │ the right│ │ I think  │ │ QUINTE?" │ │           │      │    │ │
│  │  │  │ question?"│ │ I saw?"  │ │          │ │           │      │    │ │
│  │  │  │          │ │          │ │          │ │           │      │    │ │
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
│  │  │ Phase -1: hm 四道門  │ ← hm parallel (~5s)                        │ │
│  │  │ 雨門+鏡門+證門+閂門  │                                             │ │
│  │  │ → hm context inject  │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 0: Manifest    │ ← Agent(registry) → participant list       │ │
│  │  │ cc只能加不能减 → hm签核│                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 1: R1 四方并行 │ ← cc parallel{cc,cw,omp,hm}                │ │
│  │  │ JSON(宽松schema)     │   TASK:首行锚定                             │ │
│  │  │ → hm 同步签核        │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 2: Auto-Diff   │ ← JSON Schema claim diff                   │ │
│  │  │ 相同→共识池 不同→分歧池│   新增类别→Schema扩展提案                    │ │
│  │  │ → hm 签核            │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 3: R2 对抗验证 │ ← per-dispute 3 refuters(跨模型≥1)          │ │
│  │  │ ≥2/3 refute→废弃     │   1/3→contested保留                         │ │
│  │  │ → hm 签核(防误杀)    │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 4: rx裁判      │ ← 结构化claims JSON输入(不读文件)            │ │
│  │  │ + 跨轮一致性Agent     │   R1→R2→R3 drift detection                 │ │
│  │  │ → hm 签核            │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 5: loop-until  │ ← 双critic(不同配置) 双条件终止              │ │
│  │  │ -dry 收敛检测        │   ①2轮无新 ②分歧↓+重复度>90%                 │ │
│  │  │ dry→escalate人工     │   代码claims→Bash runtime验证               │ │
│  │  │ → hm 签核            │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ Phase 6: KANSA 監査  │ ← KANSA persona + poison detect             │ │
│  │  │ 议题轮换审计+越权标注 │   低质量claims→降权                          │ │
│  │  │ → hm 终裁签核        │                                             │ │
│  │  └──────────┬───────────┘                                             │ │
│  │             ▼                                                         │ │
│  │  ┌──────────────────────┐                                             │ │
│  │  │ hm 閂門: 终裁展示    │ ← structured log → ~/.hermes/quinte/        │ │
│  │  │ + push gate          │   可回放审计                                 │ │
│  │  └──────────────────────┘                                             │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Why cc? Three Mechanisms, Three Epistemologies

Claude Code possesses three native mechanisms that Hermes cannot replicate. They are not "better tools" — they are a different category of capability:

| Mechanism | Epistemological Contribution | Failure Mode Prevented |
|-----------|------------------------------|------------------------|
| **Agent** (internal sub-agent) | Independent context → freedom from orchestrator's attentional biases | Single-context information overload + confirmation bias |
| **Workflow** (orchestration engine) | Structural guarantees: pipeline cannot skip, schema cannot overlook | Manual dispatch omission, output format ambiguity, false convergence |
| **Bash** (external agents) | Toolchain diversity → decorrelated blind spots across hm/cw/rx/omp | Single-toolchain shared blindness |

**Structural vs Disciplinary Guarantees.** v2.x relied on hm's discipline — "never skip an agent," "always enumerate all files," "never self-judge simplicity." These were repeatedly violated not because hm was careless but because the role of orchestrator-as-participant made them structurally unenforceable. v3.0 replaces disciplinary rules with structural guarantees: `pipeline()` cannot skip an item; `agent({schema})` cannot produce an unparseable claim; `parallel()` cannot accidentally serialize.

## Why hm Retains Veto Power

The separation is not about "cc is better than hm." It is about comparative advantage:

- **cc's strength**: executing complex multi-step orchestration with structural guarantees. max reasoning (32000 tokens) models full dependency topology. Workflow primitives eliminate entire classes of execution error.
- **hm's strength**: persistent session memory (session_search), cross-debate context, user relationship, browser/desktop access, and — critically — the ability to see what cc's execution pattern hides. xhigh reasoning applied to audit, not to dispatch.

The synchronous veto — hm must APPROVE every phase output before cc proceeds — ensures oversight is real, not ceremonial. hm can ABORT on error cascade, REJECT on quality, MODIFY on omission. This is not a downgrade from v2.4's orchestrator role. It is applying hm's best capability (xhigh reasoning) to the hardest problem (auditing orchestration quality) rather than wasting it on mechanical dispatch.

## The Rashomon Problem

Kurosawa's *Rashomon* (1950) presents four witnesses to the same event offering mutually contradictory testimonies. Not because anyone is lying — but because each person sees only what their position allows them to see.

This is the exact problem facing single-agent AI systems. One model, one perspective, one blind spot. The answer isn't a better model — it's a *structure that forces perspectives to confront each other*.

The deeper property — the one that makes RASHOMON a paradigm, not just a voting scheme — is **cross-detection**: an agent reviewing *another's* output in R2 can spot errors it could never have caught in its own R1. Self-review is epistemologically closed — you cannot see the blind spot you are standing in. Cross-review breaks that closure. The value is not "majority wins" — it is that the error an agent cannot self-detect is precisely the error another agent's position allows it to see.

### v3.0 Extension: Cross-Model Adversarial Depth

v2.x treated all four witnesses as epistemologically equivalent — four DeepSeek instances with different system prompts. v3.0 recognizes that **same-model consensus is weaker than cross-model consensus.** Three DeepSeek instances agreeing gives you 1 verification with 3 samples of the same noise distribution. Cross-model adversarial verification (≥1 refuter from different provider in Phase 3) decorrelates errors across architectures, training data, and RLHF alignment — producing genuinely independent verification rather than same-model echo.

## The Cost Question: "Is This Just Brute Force?"

loop-until-dry + adversarial verification per dispute + 5 agents per round can scale to hundreds of API calls per debate. Is this "力大砖飞" (brute force)?

The answer has two layers:

**Layer 1 — Yes, it is brute force, and that is the point.** DeepSeek API pricing (~$0.14/M input, ~$0.28/M output tokens) makes a full 5-agent debate cost approximately $0.01–0.05. At that price, the marginal cost of another round of cross-verification is negligible relative to the cost of an undetected error. v3.0's cost circuit breaker (claims≤100, refutations≤50, loops≤5) bounds the worst case to approximately $1–3 per debate — cheaper than 5 minutes of human review.

**Layer 2 — But brute force without structure is just expensive noise.** loop-until-dry with dual-condition termination (not just "keep going") and escalate-to-human (not auto-accept) ensures the brute force has a stopping criterion. Cross-model adversarial verification ensures the brute force isn't just same-model echo. The governance layer ensures the brute force doesn't run away.

The philosophical position: **epistemic certainty is expensive. v3.0 makes it cheap enough to be default-on, with structural guards against runaway cost.** If DeepSeek were $15/M tokens instead of $0.15, the architecture would be different. The economics enable the epistemology.

## Structure

| File | Content |
|------|---------|
| [GATES.md](GATES.md) | The Four Gates — 雨門·鏡門·證門·閂門 (v3.0: parallel, cc-backed) |
| [CONCEPTS.md](CONCEPTS.md) | Core concepts — Orchestration-Oversight Separation, Three-Mechanism Epistemology, Cross-Model Adversarial Depth |
| [PHENOMENOLOGY.md](PHENOMENOLOGY.md) | Phenomenology of the orchestrated gaze — the philosophical dimensions |

## Ecosystem

| Repo | Role | Question |
|------|------|----------|
| [RASHOMON](https://github.com/eric-stone-plus/RASHOMON) | Design philosophy | *Why* multi-perspective truth-seeking? |
| [QUINTE](https://github.com/eric-stone-plus/QUINTE) | Debate protocol | *How* to orchestrate cross-examination? |
| [KANSA](https://github.com/eric-stone-plus/KANSA) | Verdict audit | *Sound?* Does the conclusion hold up? |
| [KENGEN](https://github.com/eric-stone-plus/KENGEN) | Authorization perimeter | *May I* execute this operation? |

RASHOMON and QUINTE form the epistemology→methodology axis. KANSA audits verdict integrity. KENGEN gates external actions with BANNIN (番人) as the active session-level guard.

## Cultural Anchors

- **芥川龍之介**《藪の中》（1922）— seven testimonies, one death, no resolution
- **黒澤明**《羅生門》（1950）— Venice Golden Lion, Academy Award for Best Foreign Language Film
- **Rashomon Effect** — contradictory interpretations of the same event by different observers

## License

MIT
