# Refined Brute Force (力任せ精錬)

> *«При достаточной тяге и кирпич полетит — но с хвостовым оперением и автопилотом.»*
> "With enough thrust, even a brick flies — but this one has fins and a flight computer."
>
> Canonical label for QUINTE's architecture, ratified 2026-06-09 (5/5 agent consensus).

---

## Origin

Coined by **omp** (R1, 2026-06-09 meta-QUINTE) during the [*«при достаточной тяге и кирпич полетит»* debate](https://github.com/eric-stone-plus/QUINTE/blob/main/debates/2026-06-09-brute-force/). The user proposed QUINTE was brute-force aesthetics — Soviet aviation style: compensate for lack of refinement with raw power. Five agents debated whether QUINTE is truly brute force or something more nuanced.

omp's three-tier verdict (core = brute, governance = refined, deployment = brute) produced the synthesis label: **Refined Brute Force**.

## Definition

```
Refined Brute Force = brute-force computation core + structural governance + role-differentiated agents
```

**What is brute force about QUINTE**:
- 5 agents × 3 rounds = 15 agent-invocations per debate
- Token budget: unlimited (DeepSeek v4-pro)
- §3.4 bakes resource intensity into protocol requirements ("Never shorten prompts or merge rounds to save tokens")
- Cross-detection uses *more compute* to surface blind spots — not smarter algorithms

**What is refined about QUINTE**:
- Four Gates (四道門, shidōmon): targeted failure-mode defense, not "run more checks"
  - 雨門 (Amamon): ambiguity detection → clarify back
  - 鏡門 (Kyōmon): bidirectional grep + evidence anchoring + directional explicitness
  - 證門 (Shōmon): cross-examination topology with recusal rules
  - 閂門 (Kan'nukimon): three-layer anti-drift prompt engineering
- KANSA rotating auditor: prevents "imperial authority" accumulation (Roman Republic model)
- KENGEN authorization perimeter: session-level push gate
- Role differentiation: different reasoning effort levels (xhigh/max), different toolchains, different cognitive strengths — not 5 identical model clones

## The Decisive Constraint: Same-Model Limitation

§3.5 self-assessment: *"same-model agents cannot produce genuine epistemic challenge."*

All five agents share identical model weights. Cross-detection works through **attention displacement** (changing the anchor shifts what the model notices), not through genuinely independent epistemic positions. This means:

- Cross-detection catches "model knows but didn't notice" errors (attention failures) — **effective**
- Cross-detection catches "model genuinely doesn't know" errors (knowledge gaps) — **weak**
- All agents share the same training data boundaries, the same architecture biases, the same knowledge cutoff

The protocol was designed for multi-model deployment. Current same-model implementation is a cost constraint, not a permanent design choice.

## Cultural References

| Language | Phrase | Context |
|----------|--------|---------|
| RU | При достаточной тяге и кирпич полетит | Soviet aviation proverb — MiG-25: massive engines, stainless steel airframe |
| EN | A triumph of thrust over aerodynamics | F-4 Phantom II epitaph |
| JA | 力任せ (ちからまかせ) | Relying on brute strength; forcing through with power |

## Relationship to Other RASHOMON Concepts

- **Rashomon Depth**: Refined Brute Force describes *how* depth is achieved — through structured redundancy, not random sampling
- **Orchestration-Oversight Separation**: The primary *non-brute* structural element — separates execution from judgment
- **Kurosawa Check**: The cross-examination mechanism that gives brute force its "refined" character — structured adversarial review, not majority voting
- **Yabu no Naka Index**: Measures the *output* of refined brute force — divergence across perspectives

## Key Insight

> "Three gates organize brute force. They don't replace it. The brick has fins and a flight computer, but it still flies on thrust, not aerodynamics."
> — omp R1, 2026-06-09

The structure *matters* — it changes how errors are caught (cross-detection asymmetry vs. random cancellation), which failure modes are defended (targeted gate design vs. generic redundancy), and whether the system can self-diagnose (§3.5 self-assessment). But the structure cannot change the fundamental fact: confidence is achieved by burning more compute, not by being smarter per-token.

---

*REFINED-BRUTE-FORCE-v1.md — ratified 2026-06-09, archived 2026-06-10*
