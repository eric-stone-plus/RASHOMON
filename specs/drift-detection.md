# Drift Detection - Silent Collapse Prevention

## Source
QUINTE debate synthesis, updated for the residual trace contract.

## Problem
All perspectives can drift toward the same wrong answer. High convergence with
low tension is not automatically safe; it may mean the protocol failed to
create or preserve the right residual.

## Detection Dimensions

### Multi-Dimensional Diversity Monitoring

- Reasoning path diversity: do perspectives use materially different
  intermediate claims?
- Evidence source diversity: are claims grounded in distinct sources, files,
  commands, or tests?
- Assumption diversity: do perspectives expose different hidden premises?
- Residual diversity: do the remaining residuals come from multiple routes, or
  only from one dissenting source?

When diversity drops while convergence rises, the trace should include a
silent-collapse residual unless direct evidence already closes the claim.

### Temporal Drift Detection

Track the consensus position and residual set over time. Significant drift
without new evidence is suspicious. The active artifact is not only the answer
delta; it is also the change in residual ids, evidence coverage, and closure
coverage.

### External Anchoring

Inject known-correct and known-wrong cases where possible. High confidence on
wrong anchors is a systemic collapse signal. Executable claims should be tested
directly instead of debated indefinitely.

### Meta-Epistemic Monitoring

- Confidence should be compared with actual verification rate.
- High confidence plus low evidence coverage is a residual, not a pass signal.
- Closure coverage should fall when high-risk residuals lack evidence, scope,
  or waiver.

## Residual Trace Metrics

Silent collapse prevention depends on metrics that can be inspected by the
runtime:

- unresolved high-risk residual count
- evidence coverage for material claims
- closure coverage for action-blocking residuals
- repeated residual signatures across sessions
- same-route agreement without external evidence
- residuals reopened after supposed closure

These metrics can be implemented by HIGHBALL or another host measurement
layer. RASHOMON defines their epistemic meaning; it does not require a specific
runtime ledger implementation.

See `specs/residual-quality-metrics.md` for the derived measurement contract.

## Related
- RASHOMON/specs/adversarial-defense.md - active probing complements passive detection
- RASHOMON/specs/residual-first-architecture.md - residual trace contract
- HIGHBALL/specs/residual-closure.md - action-boundary closure checks
