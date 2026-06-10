# Core Concepts — 核心概念

Operational concepts extracted from the Rashōmon metaphor for the QUINTE protocol. v3.0 additions: Orchestration-Oversight Separation, Three-Mechanism Epistemology, Cross-Model Adversarial Depth, Refined Brute Force.

---

## Rashomon Depth

**Definition**: Not the number of agents, but the number of genuinely independent perspectives produced.

```
Rashomon Depth = |{ genuinely different reasoning paths }|
```

**Criteria**:
- Same model, different prompt parameters → Depth = 1 (changing the mask, not the witness)
- Different models, different toolchains, different attention biases → Depth increases
- R2 cross-review itself contributes Depth — reviewing another's analysis from a different position

**v3.0 extension**: The cross-model requirement for adversarial verification (≥1 refuting agent from a different provider) is the engineering realization of Rashomon Depth. Same-model consensus = 1 verification × 3 noise samples. Cross-model consensus = genuinely independent verification paths.

**Heuristic**: If all four R1 outputs are strikingly consistent and no one says "I'm not sure," this may be a shared blind spot, not consensus. In Rashōmon, if four witnesses tell exactly the same story, that is precisely when you should be suspicious.

---

## Orchestration-Oversight Separation

**v3.0 core concept**: The entity that executes the debate must not be the same entity that judges its quality.

```
Claude Code (Execution Domain)       Hermes (Oversight Domain)
────────────────────────────         ──────────────────────────
Workflow pipeline/parallel           Per-Phase synchronous veto
Agent dispatch + JSON Schema         Cross-round drift detection
Adversarial verification             Quality audit
loop-until-dry convergence           ABORT cascade authority
Bash external agent invocation       Context injection (memory → prompt)
```

**Epistemological rationale**: In v2.x, hm was both orchestrator (deciding who speaks, in what order, on what topic) and participant (producing analysis). This created an intrinsic conflict of interest — hm would unconsciously trim the debate to fit its own conclusions: skipping agents it deemed "unnecessary," narrowing scope based on its own blind spots, treating its own R1 as ground truth for R2 synthesis. This was observed in production (2026-06-07, twice). These were not discipline failures — they were structural consequences of conflating execution with oversight.

**Separation principles**:
1. **Executor cannot self-audit** — the orchestration engine cannot audit its own orchestration quality
2. **Overseer cannot participate in execution** — hm's xhigh reasoning is used to audit the orchestration plan, not to dispatch agents
3. **Veto must precede execution** — synchronous APPROVE/REJECT, not asynchronous post-hoc audit

---

## Three-Mechanism Epistemology

**Definition**: cc's three native mechanisms each contribute a different type of epistemological guarantee.

| Mechanism | Epistemological Contribution | Failure Mode Prevented |
|-----------|------------------------------|------------------------|
| **Agent** (internal sub-agents) | Independent context → decorrelated attention biases | Single-context information overload + confirmation bias |
| **Workflow** (orchestration engine) | Structural guarantees: pipeline cannot skip, schema cannot overlook | Manual dispatch omission, output format ambiguity, false convergence |
| **Bash** (external agents) | Toolchain diversity → decorrelated blind spots | Single-toolchain shared blindness |

**Agent's epistemological value**: Each internal Agent has an independent context window — it does not share the orchestrator's attention biases. The Manifest Agent independently reads the registry and generates the mandatory participant list without passing through cc's orchestration logic — an epistemological guarantee that "the executor cannot decide who participates."

**Workflow's epistemological value**: `pipeline()` and `parallel()` are not performance optimizations — they are discipline guarantees. pipeline cannot skip an item once added; `agent({schema})` cannot produce a format error that goes undetected. These are mechanical guarantees that manual orchestration cannot provide.

**Bash's epistemological value**: hm's browser/desktop, cw's deep search, rx's pure reasoning, omp's rapid security review — these are different cognitive tools. Their "biases" do not fully correlate because their toolchains and attention biases differ.

---

## Yabu no Naka Index (藪の中指数)

**Definition**: The degree of divergence across R1 witness accounts. Named after Akutagawa's original story title *Yabu no Naka* (藪の中, "In a Grove").

```
YNI = 1 - (intersection of claims / union of claims)
```

**Interpretation**:
- YNI ≈ 0: High consistency → ⚠️ possible shared blind spot. R2 performs confirmatory audit.
- YNI ≈ 0.3–0.5: Healthy divergence → R2 flags disputes.
- YNI > 0.7: High dispersion → the original question may be ambiguous. Return to Amamon.

**v3.0 revision**: YNI is now computed by Phase 2 auto-diff (claims comparison after JSON Schema alignment), not by hm manual estimation. Mechanical diff eliminates subjective bias in hm's dispute annotation.

---

## Kurosawa Check (黒澤明檢查)

**Definition**: R2 mandatory cross-review + adversarial verification. QUINTE's core mechanism.

**Metaphor**: Kurosawa did not simply let four witnesses tell their stories. The power of *Rashōmon* lies in the audience comparing the testimonies and constructing an understanding closer to the truth through that act of comparison. R2 is this "comparison" step — with v3.0 adding adversarial refutation.

**v3.0 upgrade**:
- v2.x: Cross-review = read others' output + flag disputes
- v3.0: Cross-review = cross-review + adversarial verification (3 refuters per dispute, cross-model) + cross-round consistency review

**Rule**: R2 is never skipped. Four-way consensus can still be a shared blind spot.

---

## Kyōmon Interception Rate (鏡門拦截率)

```
Kyōmon IR = errors_caught / comparative_claims_made
```

Unchanged in v3.0. Measures the frequency of hm directional errors and Kyōmon's effectiveness at intercepting them.

---

## Refined Brute Force (精煉暴力 · 力任せ精錬)

> *«При достаточной тяге и кирпич полетит — но с хвостовым оперением и автопилотом.»*

**Definition**: QUINTE's architecture classification — brute-force computation core + structural governance + role-differentiated agents. Ratified 2026-06-09 (5/5 agent consensus). See [REFINED-BRUTE-FORCE.md](REFINED-BRUTE-FORCE.md) for the full concept.

---

## Glossary

| Term | 日本語 / English | Reading | Meaning |
|------|-----------------|---------|---------|
| Rashomon Depth | — | — | Number of independent perspectives |
| Orchestration-Oversight Separation | — | — | v3.0 core architectural principle: execution ≠ judgment |
| Three-Mechanism Epistemology | — | — | Agent/Workflow/Bash differentiated epistemological contributions |
| Cross-Model Adversarial Depth | — | — | Independent perspectives from cross-model adversarial verification |
| Refined Brute Force | 精煉暴力 | — | Canonical architecture label: governed brute-force ensembling |
| Yabu no Naka Index | 藪の中 | やぶのなか | R1 divergence measure |
| Kurosawa Check | 黒澤明檢查 | — | R2 mandatory cross-review + adversarial verification |
| Kyōmon IR | 鏡門拦截率 | — | Kyōmon interception rate |
| Amamon | 雨門 | あまもん | Ambiguity Gate |
| Kyōmon | 鏡門 | きょうもん | Mirror Gate |
| Shōmon | 證門 | しょうもん | Testimony Gate |
| Kan'nukimon | 閂門 | かんぬきもん | Anti-Drift Gate |

---

*CONCEPTS-v3.md — ratified 2026-06-09, updated 2026-06-10*
