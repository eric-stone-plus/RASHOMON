# Refined Brute Force (精煉暴力)

> *«При достаточной тяге и кирпич полетит — но с хвостовым оперением и автопилотом.»*
> "With enough thrust, even a brick flies — but this one has fins and a flight computer."
>
> Canonical label for QUINTE's architecture, ratified 2026-06-09 (5/5 agent consensus).

---

## Origin

Coined by **omp** (R1, 2026-06-09 meta-QUINTE) during the [*«при достаточной тяге и кирпич полетит»* debate](https://github.com/eric-stone-plus/QUINTE/blob/master/debates/2026-06-09-brute-force/). The user proposed QUINTE was brute-force aesthetics — Soviet aviation style: compensate for lack of refinement with raw power. Five agents debated whether QUINTE is truly brute force or something more nuanced.

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
- Four Gates: targeted failure-mode defense, not "run more checks"
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

## The Soviet Aviation Analogy

> *«При достаточной тяге и кирпич полетит.»*
> "With enough thrust, even a brick will fly."

The phrase is attributed to the culture of the Mikoyan-Gurevich (MiG) design bureau during the Cold War. It captures an engineering philosophy of radical pragmatism: when you cannot match your adversary's material science or manufacturing precision, you compensate with raw power.

The MiG-25 (NATO: Foxbat) is the canonical example. While American engineers pursued titanium airframes and exquisite aerodynamics for their Mach-3 interceptors, Soviet engineers faced a different set of constraints. Titanium was expensive and difficult to work with given Soviet metallurgy. The solution was not better materials — it was bigger engines. The MiG-25's Tumansky R-15 turbojets produced 11 tonnes of thrust each. Two of them, side by side, propelled a largely stainless-steel airframe to Mach 3.2. The aircraft was heavy, aerodynamically crude, and drank fuel at an alarming rate — but it *worked*. It intercepted SR-71 Blackbirds, outran missiles, and forced the United States to redesign its next-generation fighter program in response to a threat that turned out to be largely imaginary. The Foxbat was a brick. It flew because the engines were enormous.

The American equivalent — "a triumph of thrust over aerodynamics" — was coined for the McDonnell Douglas F-4 Phantom II, another aircraft that proved more successful than its ungainly appearance suggested. The Japanese phrase *力任せ* (*chikaramakase*, "forcing through with brute strength") captures the same ethos from a different cultural angle.

**QUINTE sits in the same lineage.** It does not rely on a single model's elegant reasoning. It burns five agents across three rounds to surface blind spots through structured redundancy. The difference: the Soviet brick was genuinely just a brick with massive engines. QUINTE's brick has fins (the Four Gates, each targeting a specific failure mode) and a flight computer (the Orchestration-Oversight Separation). The thrust is still the dominant force — confidence comes from burning more compute, not from being smarter per token — but the structure makes the thrust *governed* rather than *chaotic*.

> *«При достаточной тяге и кирпич полетит — но с хвостовым оперением и автопилотом.»*
> "With enough thrust, even a brick flies — but this one has fins and a flight computer."
> — omp R1, 2026-06-09

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
