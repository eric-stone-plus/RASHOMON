# Residual-First Architecture

> RASHOMON names the failure: a single perspective can produce a coherent
> testimony that hides its own blind spot. The response is not answer
> aggregation. It is controlled residual exposure.

## 1. Core Claim

The primary artifact of the ecosystem is not an answer. It is a **residual**:
an evidence-bearing difference between outputs produced under controlled
perspective perturbations.

A residual may be:

- a contradiction between two claim sets
- an omission discovered by another perspective
- a confidence mismatch on the same evidence
- a citation or evidence gap
- a prompt-restatement drift
- a mind-change caused by cited evidence
- a runtime mismatch between a claim and executable behavior
- suspicious low-tension convergence around an unverified claim

This is a black-box behavioral concept. It is related to "attention residual"
only as an operating metaphor. Unless activation, logit, or attention-head
traces are available, RASHOMON does not claim to observe transformer internals.
It observes how the same system behaves when its observer-position changes.

## 2. Why This Is Not MoA

Mixture-of-Agents systems usually optimize for a better final answer by
aggregating multiple candidate answers across layers. That is a performance
scaling pattern.

Residual-first architecture optimizes for a different outcome:

1. perturb the observer position
2. preserve the resulting differences
3. verify evidence for each difference
4. classify the unresolved tension
5. route action through an operational gate

The difference matters most when all perspectives share the same base model.
Same-model agreement is weak evidence of truth because errors may be correlated.
Same-model disagreement is still valuable because it exposes behavioral
instability: the same system cannot keep its testimony invariant under
controlled pressure.

Cross-model heterogeneity remains stronger when available, but it is not the
definition of the method. Heterogeneity decorrelates error; residual exposure
makes error inspectable.

## 3. Layer Responsibilities

- RASHOMON defines the epistemic problem, residual ontology, false-consensus risks, and escalation states.
- QUINTE produces adversarial residuals through independent testimony, anonymous cross-examination, evidence gates, and dual verdict.
- MAGI produces triadic convergence/divergence residuals without voting or forced closure.
- HIGHBALL selects and enforces the runtime path for producing, validating, measuring, preserving, closing, waiving, blocking, or escalating residuals.
- A measurement layer may track residual patterns over time: drift, lazy governance, repeated aporia, and resource burn.

No layer owns truth. Each layer owns a constraint on how truth-claims are
allowed to move.

## 4. Residual Lifecycle

Residuals move through a conservative lifecycle:

1. Start with a user question or proposed action.
2. Apply controlled perspective perturbation.
3. Preserve the resulting residual artifact.
4. Normalize and compare the claims.
5. Validate evidence against files, commands, runtime output, sources, or user
   input.
6. Assign a disposition.
7. Send action-relevant residuals to the HIGHBALL action gate.
8. Record later observable outcomes when direct evidence, runtime behavior,
   human review, or external feedback becomes available.
9. When a route may become a future default, compare calibration, route-pairing,
   baseline, and outcome evidence against a pre-run experiment manifest so route
   policy is not inferred from post hoc sample selection.
10. Synthesize calibration, pairing, baseline, experiment-review, and outcome
    evidence into reviewed route-policy recommendations without automatically
    changing the router.

Dispositions are intentionally conservative:

- `verified`: the residual is resolved by file, command, runtime, source, or user-provided evidence.
- `falsified`: the residual was an artifact of bad reasoning, bad citation, prompt drift, or stale context.
- `unresolved`: the residual is real but cannot be resolved with current evidence.
- `escalated`: the residual affects an action boundary and must pass through HIGHBALL governance.
- `discarded`: the residual failed the protocol contract, such as missing task restatement or unusable output.

Outcome records are separate from dispositions. A disposition says what the
trace can justify at decision time. An outcome says what later evidence showed.
Keeping them separate prevents hindsight from rewriting the original evidence
state.

## 5. Instrument Selection

Residual-first architecture treats QUINTE and MAGI as instruments, not as
standing authorities.

Use MAGI when a low-risk claim needs an independent stability check and three
perspectives can reveal convergence or divergence cheaply.

Use QUINTE when a consequential conclusion may affect code, protocol, or
irreversible action and adversarial review is needed before trust or action.

Use direct runtime evidence when a claim is executable; behavior outranks
testimony, with QUINTE or MAGI added only when interpretation still matters.

Use HIGHBALL when the residual is at a governance or action boundary because
routing, authorization, and protected writes are runtime concerns.

Use human review when a residual remains high-impact after tool review and
machine debate has reached its ceiling.

## 6. Metrics

Residual-first architecture reinterprets existing RASHOMON metrics:

- **Yabu no Naka Index**: how divergent the initial testimonies are.
- **Rashomon Ratio**: how much of the union of claims survives all perspectives.
- **RTS (Residual Tension Score)**: how dangerous the remaining unresolved
  residuals are, especially when surface convergence is high.
- **Diversity Score**: how correlated the perspectives appear to be.
- **CDA (Cross-Detection Asymmetry)**: which perspectives detect which other
  perspectives' errors.

The key anti-pattern is high agreement with low verified evidence. That is not
confidence. It is a silent-collapse candidate.

Metrics become empirically meaningful only after outcome feedback accumulates.
Outcome ledgers compare later observations against earlier residual traces and
route decisions. They do not make the original trace "true"; they show whether
the route's evidence held up under later observation.

Route pairing reports ask whether a target trace earned its cost against a
same-question baseline trace for the same action boundary. Route baseline
reports aggregate that comparative pressure at route-group level by asking
whether a route earned its cost against a cheaper, stronger, or more direct
same-boundary route. Route policy reports add one more boundary: they can
recommend keeping, watching, rerouting, or blocking a route policy, but they do
not mutate the runtime router. This preserves human and protocol oversight over
route changes.

Route change proposals are one step more concrete but still non-authorizing:
they identify candidate documentation or host-overlay changes and required
review gates without applying the change.

Route experiment manifests and reviews close a different gap. They are the
pre-registration layer for route evaluation: what cohort is being tested, which
baseline and same-question pair evidence must be present, what outcome evidence
is required, and which stopping rules prevent promotion. This matters because
same-model QUINTE can surface valuable behavioral residuals while still losing
to direct evidence, self-correction, human review, or a cheaper heterogeneous
route on a planned baseline.

## 7. Failure Modes

- Residual inflation: random sampling noise is treated as insight. Control: require evidence and disposition.
- Residual laundering: disagreement is merged into smooth synthesis. Control: preserve source claim and dissent.
- Judge circularity: the same model evaluates its own output and amplifies self-bias. Control: external evidence, anonymous review, Auditor B, and human escalation.
- Prompt contamination: perturbation changes the task instead of the perspective. Control: task-first prompts and first-line restatement.
- False consensus: correlated agents agree around an unsupported claim. Control: evidence gate, diversity monitoring, and RTS.
- Cost burn: debate continues after no useful residuals appear. Control: HIGHBALL resource, route, and governance gates.
- Hindsight laundering: later success or failure is used to rewrite what the trace originally showed. Control: separate outcome ledgers from residual traces and Action Packets.
- Post hoc route promotion: a route is promoted after selecting convenient traces, baselines, pairs, or outcomes. Control: route experiment manifest and review before policy synthesis.
- Self-modifying route drift: weak calibration or outcome evidence silently changes future routing. Control: treat route policy reports as reviewed evidence, not router mutation.

## 8. Residual Trace Contract

Every instrument that claims to follow RASHOMON must leave a residual trace.
The trace is not a final answer. It is the minimum portable artifact that lets a
host runtime decide whether a claim can cross an action boundary.

Required top-level fields:

- `question`: the user question, proposed action, or claim under review.
- `instrument`: the producing route, such as `MAGI`, `QUINTE`, `direct-evidence`, or `human`.
- `residuals`: evidence-bearing differences, doubts, or false-consensus warnings.
- `trial_manifest`: optional trial conditions including perspectives, perturbation axes, independence controls, contamination risks, and cost.
- `action_boundary`: the strongest boundary the result may affect.
- `highball_decision`: HIGHBALL's decision when a runtime gate has evaluated the trace.

Required residual fields:

- `id`: stable residual identifier within the trace.
- `severity`: one of `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`, or `P0`.
- `type`: residual type such as contradiction, omission, evidence gap, confidence mismatch, drift, execution mismatch, or silent collapse.
- `source`: round, perspective, file, command, or human source that produced the residual.
- `finding`: the specific claim, defect, or unresolved tension.
- `affected_paths`: paths or globs affected by the residual; use an empty array when not applicable.
- `error_signature`: narrow string, regex, command, or test that detects whether the issue remains; use null when not applicable.
- `evidence`: file line, command output, runtime output, source, or null.
- `disposition`: one of `verified`, `falsified`, `unresolved`, `escalated`, or `discarded`.
- `required_closure`: one of `none`, `edit`, `test`, `command`, `block`, `waiver`, or `human_review`.
- `closure_state`: one of `open`, `closed`, `blocked`, `waived`, or `not_applicable`.
- `closure_evidence`: evidence that justifies the closure state.
- `scope`: the action scope covered by the closure state.

The contract is intentionally shared with HIGHBALL's residual closure ledger.
RASHOMON defines what the fields mean; QUINTE and MAGI produce them under
different pressure regimes; HIGHBALL decides whether a high-risk residual is
closed enough for action.

The canonical machine-readable schema lives at
`schemas/residual-trace.schema.json`. Runtime consumers may add stricter
closure policy, but they should not redefine field names or allowed values.
Minimal valid and blocking fixtures should live in downstream validation
corpora, not in this repository.
Trial manifest semantics are specified in `specs/residual-trial-manifest.md`.

## 9. Instrument Responsibilities

- MAGI must produce convergence and divergence residuals. Material dissent and missing evidence remain visible even when two or three perspectives agree.
- QUINTE must produce adversarial residuals with source provenance from R1/R2 and an R3 closure ledger for action-blocking findings.
- Direct evidence must produce execution residuals from files, commands, tests, runtime output, or external sources.
- Human review must produce explicit waiver, block, or review evidence with scope.
- HIGHBALL must select the next evidence route, consume the trace, and pass, review, block, escalate, or record that no action boundary applies.

An instrument may return a useful answer without satisfying this contract, but
it has not produced a residual-first artifact. Such an answer may inform a
human, but it must not be used as protected-write evidence.

HIGHBALL may bind route decision, trace validation, quality metrics, execution
evidence, and action scope into an Action Packet. The packet is a consumer-side
evidence bundle; it does not replace the residual trace schema. For QUINTE near
protected or irreversible boundaries, execution evidence includes complete
phase dispatch ledgers so an incomplete debate cannot be laundered into a
valid-looking residual trace.

## 10. Research Fit

The literature supports the narrow claim, not the broad myth.

- Self-consistency shows that multiple reasoning paths can improve some
  reasoning tasks, but it still aggregates answers rather than preserving
  residuals.
- Multi-agent debate work such as Du et al. (2023) and Liang et al. (2023)
  supports the possibility that interaction can expose reasoning failures and
  encourage divergent thinking.
- Negative and mixed evaluations such as Zhang et al. (2025) show that
  multi-agent debate often fails to beat strong single-agent or
  self-consistency baselines unless model heterogeneity and evaluation design
  are handled carefully.
- Recent work on homogeneous debate cost, consensus-free debate, trace-level
  synthesis, and reasoning-tree audit strengthens the same point: agreement is
  less important than preserved reasoning evidence, declared baselines, and
  stopping rules.
- Multi-agent failure taxonomies such as Cemri et al. (2025) show that system
  design, inter-agent misalignment, and task-verification failures are
  systematic rather than anecdotal.
- Prompt-injection and conformity work such as MAD-Spear shows that debate
  systems can amplify manipulated minority views through conformity pressure.
- LLM-as-judge studies such as Zheng et al. (2023) and self-preference studies
  such as Wataoka et al. (2024) and Panickssery et al. (2024) show that model
  judges can be useful but biased. Judge output should therefore be treated as
  residual evidence, not final authority.

Therefore the ecosystem should be evaluated by residual quality, not only answer
accuracy: how many high-impact errors were surfaced before action, how many
citations were verified, how much dissent was preserved, and how often false
consensus was blocked.

The derived measurement contract is specified in
`specs/residual-quality-metrics.md`. Metrics are computed from traces by the
consumer or host runtime. Producing instruments should supply enough evidence
for measurement, but they should not be treated as authorities on their own
trace quality.

## 11. Minimal Viable Output

Any residual-first run should leave a JSON-compatible artifact matching
`schemas/residual-trace.schema.json`:

```json
{
  "trace_version": "1.0",
  "question": "string",
  "instrument": "QUINTE",
  "residuals": [
    {
      "id": "RC-001",
      "severity": "HIGH",
      "type": "evidence_gap",
      "source": "round/participant/file/command",
      "finding": "string",
      "affected_paths": ["path or glob"],
      "error_signature": "literal string, regex, command, or null",
      "evidence": "file:line, command output, source, or null",
      "disposition": "unresolved",
      "required_closure": "human_review",
      "closure_state": "open",
      "closure_evidence": ["file:line, command output, source, waiver, or null"],
      "scope": "what action this closure covers"
    }
  ],
  "trial_manifest": {
    "manifest_version": "1.0",
    "base_model_relation": "same_model",
    "perspective_count": 3,
    "perspectives": [
      {
        "id": "Perspective A",
        "role": "string",
        "route": "string or null",
        "artifact": "string or null",
        "prompt_hash": "string or null",
        "independent_first_pass": true
      }
    ],
    "perturbation_axes": ["role"],
    "independence_controls": ["independent_first_pass"],
    "contamination_risks": ["same_model_error_correlation"],
    "cost": {
      "total_tokens": 0,
      "wall_time_seconds": 0,
      "tool_calls": 0,
      "human_minutes": 0
    }
  },
  "action_boundary": "protected_write",
  "highball_decision": "review"
}
```

This is the shared conceptual contract: RASHOMON asks what residuals mean;
QUINTE and MAGI produce them under different pressure regimes; HIGHBALL decides
what may be done with them.
