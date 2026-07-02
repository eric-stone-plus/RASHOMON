# RASHOMON Ontology

## Core Concepts

### Epistemic States

**Residual**
Evidence-bearing difference between controlled perspectives. The primary
artifact of RASHOMON. May appear as contradiction, omission, evidence gap,
confidence mismatch, drift, mind-change, execution mismatch, or false-consensus
signal.

System output: preserve source, evidence, and disposition.

Routing: MAGI, QUINTE, direct evidence, HIGHBALL, or human review.

**Aporia (ἀπορία)**
Reasoning chain incomplete. Cannot determine truth with available evidence.

System output: "undecidable" plus suspended claim points.

Escalation: records an unresolved residual. HIGHBALL or human review handles
action boundaries when needed.

**Hard Collision**
All reasoning chains complete and internally consistent, but conclusions mutually exclusive.

System output: structured dialectical synthesis, followed by RTS evaluation and
possible HIGHBALL or human review when an action boundary is involved.

### Trace States

**Residual Trace**
Portable artifact that records residuals, evidence, disposition, closure state,
scope, and action boundary. It is the boundary object shared by RASHOMON,
QUINTE, MAGI, HIGHBALL, direct evidence, and human review.

System output: JSON-compatible trace with stable residual ids.

Routing: HIGHBALL may consume the trace when a protected action is proposed.

**Residual Trial Manifest**
Trace section that records the trial conditions under which residuals were
produced: perspective count, artifacts, prompt hashes, perturbation axes,
independence controls, contamination risks, model relationship, and cost.

System output: optional JSON-compatible `trial_manifest` in the residual trace.

Rule: a manifest bounds the evidential claim. Same-model traces with a manifest
show stability or instability under recorded perturbation, not independent proof
of truth.

**Residual Route Pair**
Same-question target and baseline residual traces for the same action boundary.

System output: HIGHBALL route pairing report with trace refs, route groups,
metric deltas, pair verdict, and conservative recommendation.

Rule: route pairs are not answer votes and not LLM judge preferences. They ask
whether the target route exposed better residual evidence than a cheaper,
stronger, or more direct route under the same question and boundary.

**Closure State**
Operational state assigned to a residual when action is proposed.

Allowed values: `open`, `closed`, `blocked`, `waived`, and `not_applicable`.

Rule: language-model agreement alone cannot close a high-risk residual.
Closure requires external evidence, runtime evidence, a block record, or an
explicit scoped waiver.

### Governance States

**Rubicon Moment**
Transition point where MAGI/QUINTE output crosses into executable action.

HIGHBALL evaluates the residual trace, the action boundary, risk,
reversibility, and authorization.

Outcome: pass, review, block, escalate, or record that no action boundary
applies.

### Failure Modes

**Silent Collapse (Implicit Drift)**
All agents drift toward same error direction. High convergence + low tension.

Detected by: diversity monitoring, external anchoring, and temporal drift
detection.

Defence: evidence validation, preserved dissent, independent routes when
available, and HIGHBALL blocking when high-risk residuals remain open.

**Sybil / Byzantine Attack**
Malicious agent(s) inject coordinated false perspectives.

Detected by: route provenance, asymmetric evidence checks, anomalous agreement
patterns, and inconsistent closure evidence.

Defence: do not treat consensus as closure; require source provenance and
external evidence for action-bound claims.

### Structural Roles

**QUINTE**
Adversarial residual-exposure instrument.

Role: force independent testimony, cross-examination, evidence validation, and
dual verdict. Produces action-ready residual traces when the R3 ledger is
complete.

**MAGI**
Triadic independent inquiry instrument.

Role: expose convergence and divergence across three independently formed
perspectives. Produces stability traces, not forced closure.

**HIGHBALL**
Runtime operation layer.

Role: select evidence routes, bind concrete routes, enforce authorization,
measure trace quality, compare same-question route pairs, inspect residual
closure, and block protected actions when high-risk residuals remain open.

**Direct Evidence**
Files, commands, tests, runtime output, source retrieval, or user-provided facts.

Role: outrank testimony when executable or source-verifiable claims are at
issue.

### Metrics

**RTS (Residual Tension Score)**
Detects false consensus. High convergence + high tension = danger.
Complemented by Diversity Score (independent dimension).

**Closure Coverage**
Fraction of action-blocking residuals that are `closed`, `blocked`, `waived`,
or `not_applicable` with adequate evidence and scope.

**Evidence Coverage**
Fraction of material claims whose evidence resolves to a source, file line,
command output, runtime output, or explicit user statement.

**Trial Manifest Quality**
Consumer-derived signals for perspective count, independent first-pass count,
perturbation axes, contamination risks, same-model flag, and cost fields.

## Domain Architecture

Epistemic-deliberative domain: equal debate.

- RASHOMON: parallel perspective aggregation and tension preservation.
- QUINTE: adversarial cross-examination and residual ledger production.
- MAGI: independent triadic protocol framework; no active runtime route or
  QUINTE escalation role.

Rubicon Moment: the boundary where epistemic output becomes executable action.

Governance-operational domain: constrained adjudication.

- HIGHBALL: route binding, authorization, residual closure, process guard, and
  protected-action blocking.
- Human review: explicit scoped waiver, escalation decision, or final
  responsibility when machine evidence reaches its ceiling.

## Related

- [Parallel Topology](../specs/parallel-topology.md) — architecture implementation
- [Adversarial Defense](../specs/adversarial-defense.md) — Sybil/Byzantine protection
- [Drift Detection](../specs/drift-detection.md) — silent collapse prevention
