# RASHOMON Theoretical Foundation

> RASHOMON is a residual ontology, not a debate engine. Its claim is narrow:
> controlled perspective perturbation can expose blind spots, but only evidence
> and closure determine whether action is allowed.

## Core Thesis

A single coherent answer can hide its own failure mode. RASHOMON therefore
treats the residual as the primary artifact: an evidence-bearing difference,
gap, or false-consensus warning produced when a claim is viewed from controlled
alternate positions.

This is a behavioral black-box thesis. Unless internal traces are explicitly
available, RASHOMON does not claim access to activations, attention heads, or
logits. It observes output instability, missing evidence, disagreement,
confidence mismatch, prompt drift, and execution mismatch.

## Research Ground

The literature supports a constrained design, not a blanket belief that
multi-agent debate is automatically better.

Self-consistency work by Wang et al. (2022) shows that sampling multiple
reasoning paths can improve some reasoning tasks. RASHOMON borrows the value of
multiple paths but rejects answer aggregation as the final artifact, because
aggregation can hide the residuals that matter operationally.

Inference-time exploration work gives the same point a black-box engineering
form. Tree of Thoughts by Yao et al. (2023) shows that exploring multiple
reasoning paths can outperform a single left-to-right chain on planning tasks.
Self-Refine by Madaan et al. (2023) and Reflexion by Shinn et al. (2023) show
that a single base model can improve outputs through feedback and trial traces
without weight updates. But Huang et al. (2024) show the limiting case:
intrinsic self-correction without external feedback can fail or degrade
reasoning. RASHOMON therefore treats same-model QUINTE as controlled
inference-time perturbation, not as independent confirmation or self-certifying
truth.

Multiagent debate work by Du et al. (2023) and Liang et al. (2023) supports the
use of interaction and divergent roles to expose reasoning failures. RASHOMON
uses that support narrowly: cross-examination is useful when source,
evidence, and dissent are preserved.

The negative and mixed literature is more important for engineering. Zhang et
al. (2025) find that MAD often fails to beat strong single-agent or
self-consistency baselines unless evaluation design and model heterogeneity are
handled carefully. Choi et al. (2025) argue that majority voting accounts for
much of MAD's apparent gain and that unguided debate does not by itself improve
expected correctness. Bertalanič and Fortuna (2026) report that homogeneous
debate can be more expensive and less accurate than isolated self-correction,
with failure modes including sycophantic conformity, contextual fragility, and
consensus collapse.

Newer trace-centered and routing-centered MAD work sharpens the same point.
Fadnavis et al. (2026) argue that the useful unit is the reasoning trace rather
than the answer vote, because majority voting discards minority-chain
complementarity. Shin (2026) frames same-model closed debate as a reasoning
trap where copies of one model may preserve answer accuracy while degrading
evidence faithfulness. Hao et al. (2026) decompose stance convergence into
spontaneous instability, conformity, and persuasion, showing why convergence
cannot be read as correctness without controls. Niu and Zhang (2026) support
adaptive routing over fixed debate pipelines, especially when similar agents
would amplify correlated errors or waste computation.

MAS failure taxonomies such as Cemri et al. (2025) show that design flaws,
inter-agent misalignment, and task-verification failures are systematic rather
than anecdotal. MAD-Spear by Cui et al. (2025) shows that conformity and prompt
injection can degrade multi-agent debate. These results support residual
preservation, evidence gates, and closure checks rather than faith in debate.

LLM-as-judge studies such as Zheng et al. (2023) and self-preference studies
such as Wataoka et al. (2024) and Panickssery et al. (2024) show that judges can
be useful but biased. Judge output should therefore be treated as residual
evidence, not final authority.

## Design Consequences

1. Preserve residuals before synthesis.
2. Attach source and evidence to every material residual.
3. Treat same-model agreement as stability under the tested perturbation, not
   proof of truth.
4. Prefer direct runtime or source evidence over testimony when a claim is
   executable or externally verifiable.
5. Use QUINTE when adversarial pressure is needed.
6. Use MAGI when lighter independent inquiry is enough.
7. Use HIGHBALL when a residual approaches a protected action boundary.
8. Use human review when machine debate reaches its ceiling.
9. Record later observable outcomes separately from the original trace so route
   calibration can be falsified without rewriting history.
10. Register route experiments before using a cohort to support future route
    policy, so baselines, outcome windows, and stopping rules are not chosen
    after the result.
11. Treat route-policy synthesis as reviewed evidence, not automatic
    self-modification.

## Residual Trace As Boundary Object

The central theoretical move is the Residual Trace Contract. It gives all
instruments a shared artifact without collapsing them into one runtime:

- RASHOMON defines residual meaning.
- QUINTE produces adversarial residual traces.
- MAGI produces convergence/divergence residual traces.
- Direct evidence produces execution or source-verification traces.
- HIGHBALL consumes traces and blocks unsafe action.
- Outcome ledgers record later observable evidence against the trace and route
  decision.
- Route pairing reports compare same-question target and baseline traces at the
  same action boundary before a route is promoted.
- Route baseline reports compare target routes against same-boundary baselines.
- Route experiment manifests and reviews compare planned route evaluation
  conditions with actual calibration, pairing, baseline, and outcome artifacts.
- Route policy reports synthesize calibration, pairing, baseline,
  experiment-review, and outcome evidence for future reviewed route changes.
- Human review can waive, block, or close within explicit scope.

A verdict without a residual trace may still be useful prose. It is not
protected-action evidence.

## Failure Modes

- Residual laundering: disagreement is smoothed into a confident answer.
  Required control: preserve dissent and source provenance.
- False consensus: correlated perspectives agree around unsupported claims.
  Required control: evidence gates, diversity notes, and HIGHBALL closure
  checks.
- Judge circularity: a model validates outputs too similar to its own.
  Required control: independent audit, direct evidence, and scoped human review.
- Prompt contamination: the perturbation changes the task instead of
  perspective.
  Required control: task restatement and prompt-drift detection.
- Trace collapse: a final answer lacks residual ids, evidence, or closure
  state.
  Required control: treat as non-actionable near protected boundaries.
- Closure laundering: a verdict detects a problem and is then used as
  permission to act.
  Required control: HIGHBALL residual closure enforcement.
- Hindsight laundering: later outcome evidence is used to make the original
  trace look stronger or weaker than it was.
  Required control: preserve traces and record outcomes in separate ledgers.
- Post hoc route promotion: a route cohort is promoted after selecting
  convenient traces, baselines, pairs, or outcomes.
  Required control: require route experiment manifest and review before policy
  synthesis.
- Route self-modification: a system treats weak calibration signals as
  permission to alter its own future routing.
  Required control: keep policy reports non-authorizing and review-bound.

## Evidence Requirements

RASHOMON should be judged by residual quality, not by answer polish:

- high-impact errors surfaced before action
- unsupported claims downgraded or blocked
- citations and runtime claims verified
- dissent preserved with source provenance
- high-risk residuals closed, blocked, waived, or marked not applicable before
  protected action

## Current Limits

1. The repository defines ontology and contracts; it does not execute routes.
2. Residual metrics need empirical calibration on archived debates.
3. Same-model residual exposure is useful for instability detection but weaker
   than true cross-model heterogeneity.
4. LLM judges remain biased instruments; they cannot close high-risk findings
   without external evidence or human waiver.
5. Same-model residual exposure is best treated as instability evidence and
   should be compared with self-correction or direct evidence baselines.
6. Route calibration needs cohorts with comparable action boundaries,
   manifests, same-question pairing reports, and direct-evidence baselines
   before it can justify changing a default route.
7. Outcome ledgers are only as strong as their follow-up evidence and
   observation window; one outcome is not universal route performance.
8. Route experiment reviews are only as strong as their manifest, pairing,
   baseline, and outcome references.
9. Route policy reports require maintainer review before changing live routing.
10. HIGHBALL enforcement currently depends on available verdict trails and JSON
   ledgers; earlier traces may only warn.

## References

1. Wang et al. (2022). Self-Consistency Improves Chain of Thought Reasoning in Language Models. arXiv:2203.11171.
2. Du et al. (2023). Improving Factuality and Reasoning in Language Models through Multiagent Debate. arXiv:2305.14325.
3. Liang et al. (2023). Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate. arXiv:2305.19118.
4. Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. arXiv:2306.05685.
5. Zhang et al. (2025). Stop Overvaluing Multi-Agent Debate -- We Must Rethink Evaluation and Embrace Model Heterogeneity. arXiv:2502.08788.
6. Cemri et al. (2025). Why Do Multi-Agent LLM Systems Fail? arXiv:2503.13657.
7. Cui et al. (2025). MAD-Spear: A Conformity-Driven Prompt Injection Attack on Multi-Agent Debate Systems. arXiv:2507.13038.
8. Wataoka, Takahashi, and Ri (2024). Self-Preference Bias in LLM-as-a-Judge. arXiv:2410.21819.
9. Panickssery, Bowman, and Feng (2024). LLM Evaluators Recognize and Favor Their Own Generations. arXiv:2404.13076.
10. Choi et al. (2025). Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models? arXiv:2508.17536.
11. Bertalanič and Fortuna (2026). The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate. arXiv:2605.00914.
12. Fadnavis, Kanakaraj, and Wyss (2026). Beyond Consensus: Trace-Level Synthesis in Mixture of Agents. arXiv:2605.29116.
13. Shin (2026). The Reasoning Trap: An Information-Theoretic Bound on Closed-System Multi-Step LLM Reasoning. arXiv:2605.01704.
14. Hao et al. (2026). Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate. arXiv:2606.00820.
15. Niu and Zhang (2026). ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Debate in Large Language Model Reasoning. arXiv:2606.13197.
16. Yao et al. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. arXiv:2305.10601.
17. Madaan et al. (2023). Self-Refine: Iterative Refinement with Self-Feedback. arXiv:2303.17651.
18. Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. arXiv:2303.11366.
19. Huang et al. (2024). Large Language Models Cannot Self-Correct Reasoning Yet. arXiv:2310.01798.
