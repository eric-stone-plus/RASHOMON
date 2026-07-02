# Refined Brute Force (精煉暴力)

> *«При достаточной тяге и кирпич полетит — но с хвостовым оперением и автопилотом.»*
> "With enough thrust, even a brick flies — but this one has fins and a flight computer."
>
> Historical label for QUINTE's architecture, recorded from a 2026-06-09
> meta-QUINTE run.

## Origin

Coined by **omp** (R1, 2026-06-09 meta-QUINTE) during a discussion of *«при достаточной тяге и кирпич полетит»*. The user proposed QUINTE was brute-force aesthetics — Soviet aviation style: compensate for lack of refinement with raw power. Five agents debated whether QUINTE is truly brute force or something more nuanced.

omp's three-tier verdict (core = brute, governance = refined, deployment = brute) produced the synthesis label: **Refined Brute Force**.

## Definition

Refined Brute Force means a brute-force computation core constrained by
structural governance and role-differentiated agents.

**What is brute force about QUINTE**:
- Five parties enter R1 and R2, with R3 dual verdict review.
- The protocol spends extra inference and review budget to expose residuals
  that a single answer would normally smooth away.
- The method is intentionally redundant: independent testimony,
  cross-examination, citation validation, and runtime verification all look at
  the same proposed claim from different positions.
- Extra compute is useful only when it leaves evidence-bearing residuals; it is
  not a substitute for verification.

**What is refined about QUINTE**:
- Five Gates: targeted failure-mode defense, not "run more checks"
  - 雨門 (Amamon): ambiguity detection followed by clarification
  - 鏡門 (Kyōmon): bidirectional grep + evidence anchoring + directional explicitness
  - 證門 (Shōmon): cross-examination topology with recusal rules
  - 閂門 (Kan'nukimon): three-layer anti-drift prompt engineering
  - 憲門 (Kennōmon): architecture gate — BANNIN-enforced protected-write check
    backed by HIGHBALL `specs/residual-closure.md`
- Independent governance audit when configured: prevents "imperial authority"
  accumulation without making the auditor part of RASHOMON's ontology
- KENGEN authorization perimeter: session-level push gate
- Role differentiation: different reasoning effort levels (xhigh/max), different toolchains, different cognitive strengths — not 5 identical model clones

## The Decisive Constraint: Same-Model Limitation

§3.5 self-assessment: *"same-model agents cannot produce genuine epistemic challenge."*

When multiple parties share the same base model, cross-detection is behavioral,
not mechanistic. It works through controlled position perturbation: changing
role, evidence budget, prompt frame, and review duty can change which claim is
noticed, challenged, or abandoned. That does not prove access to transformer
attention, residual streams, or activations.

- Cross-detection can catch salience and framing failures: cases where the same
  base model can produce the correction when forced into another stance.
- Cross-detection is weak against genuine knowledge gaps, shared training-data
  assumptions, architecture bias, and common alignment pressure.
- Same-model agreement is evidence of stability under the tested perturbation,
  not evidence of truth.

The protocol was designed for multi-model deployment. Current same-model implementation is a cost constraint, not a permanent design choice.

## The Soviet Aviation Analogy

> *«При достаточной тяге и кирпич полетит.»*
> "With enough thrust, even a brick will fly."

The phrase is attributed to the culture of the Mikoyan-Gurevich (MiG) design bureau during the Cold War. It captures an engineering philosophy of radical pragmatism: when you cannot match your adversary's material science or manufacturing precision, you compensate with raw power.

The MiG-25 (NATO: Foxbat) is the canonical example. While American engineers pursued titanium airframes and exquisite aerodynamics for their Mach-3 interceptors, Soviet engineers faced a different set of constraints. Titanium was expensive and difficult to work with given Soviet metallurgy. The solution was not better materials — it was bigger engines. The MiG-25's Tumansky R-15 turbojets produced 11 tonnes of thrust each. Two of them, side by side, propelled a largely stainless-steel airframe to Mach 3.2. The aircraft was heavy, aerodynamically crude, and drank fuel at an alarming rate — but it *worked*. It intercepted SR-71 Blackbirds, outran missiles, and forced the United States to redesign its next-generation fighter program in response to a threat that turned out to be largely imaginary. The Foxbat was a brick. It flew because the engines were enormous.

The American equivalent — "a triumph of thrust over aerodynamics" — was coined for the McDonnell Douglas F-4 Phantom II, another aircraft that proved more successful than its ungainly appearance suggested. The Japanese phrase *chikaramakase* ( "forcing through with brute strength") captures the same ethos from a different cultural angle.

**QUINTE sits in the same lineage.** It does not rely on a single model's
elegant reasoning. It spends extra review effort to surface blind spots through
structured redundancy. The difference: the Soviet brick was genuinely just a
brick with massive engines. QUINTE's brick has fins (the Five Gates, each
targeting a specific failure mode) and a flight computer (the
Orchestration-Oversight Separation). The thrust is still expensive, but the
structure only matters when it produces residuals that can be verified,
blocked, waived, or preserved.

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

The structure *matters* — it changes how errors are caught
(cross-detection asymmetry vs. random cancellation), which failure modes are
defended (targeted gate design vs. generic redundancy), and whether the system
can self-diagnose (§3.5 self-assessment). But the structure cannot change the
fundamental fact: confidence is not produced by compute volume. Confidence is
earned only when exposed residuals are tied to evidence and action closure.

*REFINED-BRUTE-FORCE.md — ratified 2026-06-09, archived 2026-06-10*
