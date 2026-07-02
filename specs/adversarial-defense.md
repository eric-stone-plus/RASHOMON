# Adversarial Defense - Sybil And Byzantine Protection

## Source
QUINTE debate synthesis, updated for the residual trace contract.

## Threat Model
Malicious or correlated parties can inject coordinated false perspectives.
Even without malice, homogeneous routes can converge around a shared error.
The dangerous pattern is high agreement, low verified evidence, and no residual
left for later closure.

## Defense Controls

### 1. Source Provenance And Route Diversity

Each residual trace records the route, round, reviewer, cited evidence, and
affected action boundary. Heterogeneous routes are preferred when available,
but the protocol does not treat route diversity as truth. It treats diversity
as one way to reduce correlated error.

### 2. Asymmetric Context Perturbation

The same task can be presented through logically equivalent but physically
different prompts. If separate routes produce near-identical unsupported
claims despite prompt perturbation, the result is a Sybil or conformity signal,
not closure evidence.

### 3. Evidence And Residual Validation

Claims about files, commands, runtime behavior, or external sources require
direct evidence. A majority claim with no evidence remains a residual. A
minority claim with strong evidence can close or overturn a majority claim.

### 4. Closure-Aware Reputation

Historical quality is measured by evidence quality, false citation rate,
prompt-restatement drift, correction rate, and unresolved high-risk residuals.
Reputation can inform review priority, but it cannot close an action-blocking
residual by itself.

### 5. Runtime Boundary Control

When a residual affects a protected write, push, deletion, deployment, or other
action boundary, HIGHBALL consumes the residual trace. BANNIN may block if
high-risk residuals remain open or if their closure evidence is missing.

## Non-Goals

RASHOMON does not claim Byzantine fault tolerance in the distributed-systems
sense. It does not prove correctness by quorum. Its narrower claim is that
adversarial residuals should remain inspectable until direct evidence, a block
record, or a scoped waiver closes them.

## Related
- RASHOMON/specs/parallel-topology.md - residual-preserving parallel topology
- RASHOMON/specs/residual-first-architecture.md - residual trace contract
- HIGHBALL/specs/residual-closure.md - protected-action closure gate
