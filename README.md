# RASHOMON (羅生門)

> 芥川龍之介《藪の中》（1922）, 黒澤明《羅生門》（1950）, multi-perspective truth-seeking

**RASHOMON** is the philosophical foundation of the multi-perspective residual
architecture. It does not describe *how* agents debate — that is QUINTE's
domain. It does not prescribe *which* tools or models instantiate a perspective
— that is an operational concern. It asks the prior question: *why must
perspectives confront each other, and what kind of truth emerges when they do?*

## The Rashomon Problem

Kurosawa's *Rashomon* (1950) presents four witnesses to the same event offering mutually contradictory testimonies. The woodcutter, the bandit, the wife, the samurai's ghost — each saw the event. Each account is internally coherent. The accounts cannot be reconciled.

Not because anyone is lying. Because each person sees only what their position allows them to see.

This is the exact problem facing any single-perspective system. One model, one training distribution, one set of RLHF alignments — one blind spot. The answer is not a better model. It is a *structure that forces perspectives to confront each other*.

## Cross-Detection: The Epistemological Core

The deeper property — the one that makes RASHOMON a paradigm rather than a voting scheme — is **cross-detection**: an observer reviewing *another's* account can spot errors it could never have caught in its own.

Self-review is epistemologically closed. You cannot see the blind spot you are standing in. Cross-review breaks that closure. The value is not "majority wins" — it is that the error one perspective cannot self-detect is precisely the error another perspective's position allows it to see.

This is not an engineering claim about model accuracy. It is a structural claim about the nature of observation: *what you cannot see about your own seeing, another can.*

## Residual-First Architecture

The operational artifact of RASHOMON is not a final answer. It is the
**residual**: an evidence-bearing difference exposed when the same question is
viewed from controlled alternate positions.

A residual may be a contradiction, omission, evidence gap, confidence mismatch,
prompt drift, mind-change, execution mismatch, or suspiciously low-tension
convergence around an unverified claim. These residuals are the material that
QUINTE, MAGI, and HIGHBALL operate on.

This makes RASHOMON different from mixture-of-agents aggregation. The goal is
not to blend several answers into a smoother answer. The goal is to make the
blind spot observable, preserve it long enough to verify it, and route action
only after the unresolved tension is classified.

See [Residual-First Architecture](specs/residual-first-architecture.md). The
canonical machine-readable schema is
[residual-trace.schema.json](schemas/residual-trace.schema.json).
Residual usefulness is evaluated by derived quality metrics, not by producer
self-certification; see
[Residual Quality Metrics](specs/residual-quality-metrics.md).
Trace conditions are recorded by an optional
[Residual Trial Manifest](specs/residual-trial-manifest.md): perspectives,
perturbation axes, independence controls, contamination risks, and cost.
HIGHBALL may package a route decision, residual trace, validation result, and
quality metrics into an Action Packet for a proposed action.
When trace cohorts are used to justify future route policy, HIGHBALL can also
bind them to same-question route pairing reports, same-boundary baseline
reports, a pre-run route experiment manifest, and a post-run experiment review
so baseline, pairing, and stopping-rule evidence remains inspectable.

## Position Perturbation And Error Correlation

Not all cross-review is equal. Two observers sharing the same training data, the
same architecture, and the same alignment may produce different answers, but
their errors are correlated. Three identical-model instances agreeing gives
evidence of stability under the tested perturbation, not proof of truth.

The first control is **position perturbation**: force the same question through
different roles, evidence budgets, prompt frames, and review duties, then
preserve the behavioral residuals that appear. This is especially useful when a
deployment is constrained to one base model, because same-model disagreement
exposes instability the model could not report from a single stance.

Cross-model heterogeneity is still stronger when available because it can
decorrelate error sources. It is an engineering amplifier, not the definition of
the paradigm. RASHOMON's core claim is narrower: controlled perspective changes
make blind spots inspectable before action.

Those controlled changes must be recorded. Without a trial manifest, a
same-model run may be repeated sampling, simulated plurality, or prompt
contamination rather than useful perspective perturbation.

## Instruments

RASHOMON names the problem and the residual ontology. It does not merge the
instruments that expose residuals:

- **QUINTE**: structured adversarial residual exposure. It forces independent
  testimony, cross-examination, evidence validation, and dual verdict.

- **MAGI**: triadic independent inquiry. It produces convergence/divergence
  residuals without joining QUINTE as a participant or voting bloc.

- **HIGHBALL**: host-side operation layer. It selects the runtime route, checks
  authorization, measures trace quality, and prevents unresolved high-risk
  residuals from crossing protected action boundaries.

The instruments may be composed by a host runtime, but their authority remains
separate. QUINTE exposes adversarial residuals; MAGI is one possible route for
lighter triadic inquiry; HIGHBALL decides which route is required and what may
be done with the result.

## Partial Order Consensus

When only statements on which *all* perspectives agree are retained, the result is a partial order — pairs where consensus exists are ranked; pairs with conflicting evidence are left *incomparable*. This is conservative epistemology: the system refuses to assert a total ordering where the evidence does not support one.

The Rashomon Ratio measures the size of the consensus-claim set divided by the
size of the union-of-claims set. It measures the stability of a verdict across
perspectives. A high ratio indicates robustness. A low ratio despite
convergence indicates fragility: the agreement may be accidental, an artifact
of shared assumptions rather than genuine alignment.

## Phenomenology of the Orchestrated Gaze

The act of orchestration is not neutral. The entity that decides *who speaks, in what order, on what topic* shapes the truth that emerges. This is the phenomenological insight at the heart of the architecture: oversight must be separated from execution.

When the same agent both orchestrates the debate and participates in it, an intrinsic conflict of interest arises. The orchestrator may unconsciously trim the debate to fit its own analytical conclusions — narrowing scope based on its own blind spots, treating its own first-round analysis as ground truth. This is not a failure of discipline. It is a structural consequence of conflating two incommensurable roles.

The separation of execution and oversight is therefore not an engineering optimization. It is an epistemological necessity.

## Counter-Evidence

The Rashomon paradigm has limits:

- **Same-model consensus is weaker than cross-model consensus.** Three instances of the same model agreeing proves internal consistency, not truth.
- **Shared cultural assumptions survive heterogeneity.** Models trained on overlapping internet-scale corpora may share blind spots that no amount of architectural diversity eliminates.
- **Adversarial structure does not guarantee adversarial outcome.** Conformity pressure, anchoring effects, and the psychological weight of apparent consensus can suppress legitimate dissent even in well-designed adversarial systems (Cemri et al. 2025; Cui et al. 2025).
- **The orchestrator's gaze is inescapable.** Even with oversight separation, the act of framing a question for debate shapes the answers that emerge. No structure fully escapes the phenomenology of the orchestrated gaze.

These limits are not reasons to abandon structured debate. They are reasons to remain skeptical of its outputs — to treat every verdict as contingent, every consensus as provisional, every blind spot as waiting to be discovered by the next round of cross-examination.

## Cultural Anchors

- **芥川龍之介**《藪の中》（1922）— seven testimonies, one death, no resolution
- **黒澤明**《羅生門》（1950）— Venice Golden Lion, Academy Award for Best Foreign Language Film
- **Rashomon Effect** — contradictory interpretations of the same event by different observers
- **Polybius**, *Histories* VI.10 — the Roman Republic's mixed constitution as institutionalized tension
- **Matthew 2:1-12** — three wise men, three gifts, one truth sought from different directions

## References

1. Breiman, L. (2001). Statistical Modeling: The Two Cultures. *Statistical Science*.
2. Du, Y. et al. (2023). Improving Factuality and Reasoning in Language Models through Multiagent Debate. *ICML 2024*. arXiv:2305.14325.
3. Zhang, H. et al. (2025). Stop Overvaluing Multi-Agent Debate. arXiv:2502.08788.
4. Cemri, M. et al. (2025). Why Do Multi-Agent LLM Systems Fail? arXiv:2503.13657.
5. Cui et al. (2025). MAD-Spear: A Conformity-Driven Prompt Injection Attack. arXiv:2507.13038.
6. Wang, X. et al. (2022). Self-Consistency Improves Chain of Thought Reasoning. *ICLR 2023*.
7. Zheng, L. et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. arXiv:2306.05685.
8. Huang, J. et al. (2024). Large Language Models Cannot Self-Correct Reasoning Yet. arXiv:2310.01798.
9. Polybius (c. 140 BCE). *Histories* VI.10.

Full theoretical foundation: [specs/theoretical-foundation.md](specs/theoretical-foundation.md)
