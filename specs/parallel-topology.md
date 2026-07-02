# Parallel Topology - Residual-Preserving Parallel Review

## Source
QUINTE debate synthesis, updated for the residual trace contract.

## Architecture Claim

RASHOMON favors parallel independent interpretation over a sequential pipeline
when the goal is to expose blind spots. Each perspective receives the same
task boundary under controlled isolation. The aggregator does not produce
"higher truth." It preserves residuals, evidence gaps, undecidable regions,
and source provenance.

## Four Parallel Analysis Dimensions

1. Surface claim consistency.
2. Reasoning chain completeness.
3. Practical consequence assessment.
4. Meta-epistemic status: evidence, uncertainty, drift, and action boundary.

## Aggregator Output

The aggregator should leave a residual trace, not only a narrative synthesis.
At minimum it preserves:

- perspective source and task restatement
- material claims and supporting evidence
- convergence and dissent with source provenance
- aporia regions that cannot be resolved with current evidence
- residual ids and closure state when an action boundary is involved

If a host needs a machine-readable artifact, it should use the shared Residual
Trace Contract in `specs/residual-first-architecture.md`.

## Why Not Sequential Pipeline

Sequential pipelines can reintroduce an implicit hierarchy where later layers
are treated as closer to truth. That is acceptable for implementation work, but
it is risky for epistemic review. RASHOMON keeps perspective outputs
inspectable so later synthesis cannot erase dissent without evidence.

## Relation To QUINTE And MAGI

QUINTE is the adversarial instrument for high-risk review. MAGI is the lighter
triadic instrument for convergence and divergence review. Both can implement
this topology, but neither is the ontology itself.

## Related
- RASHOMON/ontology/rashomon-ontology.md - epistemic domain definition
- RASHOMON/specs/residual-first-architecture.md - residual trace contract
- QUINTE/specs/PROTOCOL.md - adversarial residual exposure
- MAGI/specs/PROTOCOL.md - triadic convergence and divergence trace
