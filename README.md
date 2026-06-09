# RASHOMON (羅生門)

> 芥川龍之介《藪の中》（1922）→ 黒澤明《羅生門》（1950）→ Claude Code orchestrated truth-seeking

**RASHOMON** is the philosophical foundation of the QUINTE debate protocol. It asks the question QUINTE is built to answer: *when a single perspective cannot be trusted, how do we converge on actionable truth?*

## v3.0: The Orchestration-Oversight Separation

QUINTE v3.0 (2026-06-09) introduced a fundamental architectural insight: **the entity that executes the debate should not be the same entity that judges its quality.** This is not a technical preference — it is an epistemological necessity.

In v2.x, Hermes was both orchestrator (deciding who speaks, in what order, on what topic) and participant (producing analysis). This created an intrinsic conflict of interest: the orchestrator could unconsciously trim the debate to fit its own analytical conclusions — skipping agents it deemed "unnecessary," narrowing scope based on its own blind spots, treating its own R1 conclusions as ground truth for R2 synthesis.

The v3.0 architecture separates these concerns:

```
Claude Code (Execution Domain)          Hermes (Oversight Domain)
──────────────────────────────          ──────────────────────────
Workflow pipeline/parallel              Per-phase synchronous veto
Agent dispatch with JSON Schema         Drift detection across rounds
Adversarial verification                Quality audit of claims
loop-until-dry convergence              ABORT authority on cascade
Structured logging                      Context injection from memory
Bash external agent calls               User communication layer
```

**Why cc?** Claude Code possesses three native mechanisms that Hermes cannot replicate:
1. **Agent** — internal sub-agents with independent contexts for specialized review
2. **Workflow** — pipeline/parallel/adversarial-verification/judge-panel/loop-until-dry as first-class primitives
3. **Bash** — direct invocation of external agents (hm, cw, omp, rx) within orchestration logic

These are not "better tools." They are a different category of capability — structural guarantees (pipeline cannot skip an agent; schema validation cannot miss a malformed claim) that replace fallible human-model discipline with mechanical enforcement.

**Why hm retains veto power?** The separation is not about "cc is better than hm." It is about comparative advantage. hm's xhigh reasoning is best applied to auditing orchestration plans (spotting omissions, detecting drift, catching cascade failures) rather than executing them. The synchronous veto — hm must APPROVE every phase output before cc proceeds — ensures the oversight is real, not ceremonial.

## The Rashomon Problem

Kurosawa's *Rashomon* (1950) presents four witnesses to the same event offering mutually contradictory testimonies. Not because anyone is lying — but because each person sees only what their position allows them to see.

This is the exact problem facing single-agent AI systems. One model, one perspective, one blind spot. The answer isn't a better model — it's a *structure that forces perspectives to confront each other*.

But confrontation alone is not the mechanism. The deeper property — the one that makes RASHOMON a paradigm, not just a voting scheme — is **cross-detection**: an agent reviewing *another's* output in R2 can spot errors it could never have caught in its own R1. Self-review is epistemologically closed — you cannot see the blind spot you are standing in. Cross-review breaks that closure. Each agent carries its own distribution of errors into R1; R2 is where those errors become visible to agents who don't share them. The value is not "majority wins" — it is that the error an agent cannot self-detect is precisely the error another agent's position allows it to see.

### v3.0 Extension: Cross-Model Adversarial Depth

v2.x treated all four witnesses as epistemologically equivalent — four DeepSeek instances with different system prompts. v3.0 recognizes that **same-model consensus is weaker than cross-model consensus.** Three DeepSeek instances agreeing gives you 1 verification with 3 samples of the same noise distribution. Cross-model adversarial verification (≥1 refuter from different provider) decorrelates errors across architectures, training data, and RLHF alignment — producing genuinely independent verification rather than same-model echo.

## The Four Gates

QUINTE v3.0 operates through four mandatory gates, executed in parallel by Hermes (~5s). The gates follow the woodcutter's journey: arrive in rain, check your eyes, hear the witnesses, bolt the door.

```
                           User asks a question
                                    ▼
   ┌──────────────────────────────────────────────────────────────────┐
   │               Four Gates — Parallel Execution (~5s)               │
   │                                                                  │
   │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐  │
   │  │ 雨門 Amamon │ │ 鏡門 Kyōmon│ │ 證門 Shōmon│ │ 閂門 Kan'nu │  │
   │  │  "Am I      │ │  "Did I    │ │  "Does this│ │  "No witness│  │
   │  │   asking    │ │   see what │ │   need full│ │   collusion"│  │
   │  │   the right │ │   I think  │ │   QUINTE?" │ │             │  │
   │  │   question?"│ │   I saw?"  │ │            │ │             │  │
   │  │            │ │            │ │            │ │             │  │
   │  │  Ambiguous?│ │  Compara-  │ │  Conclus-  │ │  Every      │  │
   │  │  → clarify │ │  tive claim│ │  ion user  │ │  prompt:    │  │
   │  │            │ │  → verify  │ │  may rely  │ │  3-layer    │  │
   │  │            │ │  bidirec-  │ │  on? →     │ │  wrapper    │  │
   │  │            │ │  tionally  │ │  R1+R2+R3  │ │             │  │
   │  └────────────┘ └────────────┘ └────────────┘ └────────────┘  │
   │                                                                  │
   │  Operated by: Hermes (xhigh reasoning)                           │
   └──────────────────────────────────────────────────────────────────┘
                                    ▼
                            hm context injection
                            (session_search + memory)
                                    ▼
   ┌──────────────────────────────────────────────────────────────────┐
   │               Claude Code Workflow — Execution Engine             │
   │                                                                  │
   │  Phase 0: Agent manifest → Phase 1: 4-agent R1 →                 │
   │  Phase 2: Auto-diff → Phase 3: Adversarial verification →        │
   │  Phase 4: rx + cross-round audit → Phase 5: loop-until-dry →     │
   │  Phase 6: KANSA audit                                            │
   │                                                                  │
   │  Per phase: hm synchronous veto (APPROVE/REJECT/ABORT/MODIFY)    │
   └──────────────────────────────────────────────────────────────────┘
                                    ▼
                                  Verdict
```

## Structure

| File | Content |
|------|---------|
| [GATES.md](GATES.md) | The Four Gates — 雨門·鏡門·證門·閂門 (v3.0: parallel, cc-backed) |
| [CONCEPTS.md](CONCEPTS.md) | Core concepts — Rashomon Depth, YNI, Kurosawa Check, Orchestration-Oversight Separation, Cross-Model Adversarial Depth |
| [PHENOMENOLOGY.md](PHENOMENOLOGY.md) | Phenomenological expansion (forthcoming) |

## Ecosystem

| Repo | Role | Question |
|------|------|----------|
| [RASHOMON](https://github.com/eric-stone-plus/RASHOMON) | Design philosophy | *Why* multi-perspective truth-seeking? |
| [QUINTE](https://github.com/eric-stone-plus/QUINTE) | Debate protocol | *How* to orchestrate cross-examination? |
| [KANSA](https://github.com/eric-stone-plus/KANSA) | Verdict audit | *Sound?* Does the conclusion hold up? |
| [KENGEN](https://github.com/eric-stone-plus/KENGEN) | Authorization perimeter | *May I* execute this operation? |

v3.0 repositions the ecosystem: RASHOMON supplies epistemology, QUINTE provides the cc Workflow execution protocol, KANSA audits verdict integrity, KENGEN gates external action. The orchestration-oversight separation is the architectural instantiation of RASHOMON's core insight: no single perspective — not even the orchestrator's — can be trusted to judge itself.

## Cultural Anchors

- **芥川龍之介**《藪の中》（1922）— seven testimonies, one death, no resolution
- **黒澤明**《羅生門》（1950）— Venice Golden Lion, Academy Award for Best Foreign Language Film
- **Rashomon Effect** — entered English academic vocabulary: contradictory interpretations of the same event by different observers

## License

MIT
