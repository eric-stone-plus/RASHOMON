# RASHOMON Concept Index

## Core Terms

- **Rashomon Depth**: number of independent perspectives used to perturb a
  claim.
- **Residual-First Architecture**: treats evidence-bearing differences between
  controlled perspectives as the primary artifact, not the final answer.
- **Residual Artifact**: contradiction, omission, evidence gap, confidence
  mismatch, drift, execution mismatch, or false-consensus signal preserved for
  verification.
- **Residual Trace**: portable record containing residual ids, source,
  evidence, disposition, closure state, closure evidence, scope, and action
  boundary.
- **Residual Trial Manifest**: optional trace section recording perspectives,
  perturbation axes, independence controls, contamination risks, and cost so a
  residual can be interpreted as trial-conditioned evidence rather than an
  unsupported independence claim.
- **Closure Coverage**: fraction of action-blocking residuals that are closed,
  blocked, waived, or not applicable with adequate evidence and scope.
- **Evidence Coverage**: fraction of material claims grounded in source,
  file-line, command, runtime, or explicit user evidence.
- **Residual Quality Metrics**: consumer-derived measurements of residual
  count, evidence coverage, closure coverage, open high-risk risk, unsupported
  closure, silent-collapse signals, and trial-manifest quality.
- **Residual Route Calibration**: cohort-level comparison of scored residual
  traces by instrument, model relation, action boundary, closure, manifest
  strength, risk, and cost. It helps choose future routes; it is not truth
  probability or authorization.
- **Residual Route Baseline Report**: HIGHBALL comparison between a target
  route group and a same-boundary baseline route group. It asks whether the
  target route earned its cost against a cheaper, stronger, or more direct
  evidence path.
- **Residual Route Pairing Report**: HIGHBALL same-question comparison between
  target and baseline traces for the same action boundary. It uses residual
  scoring deltas rather than LLM judge voting, so a route is challenged by what
  it exposed, not by which answer sounded better.
- **Residual Outcome Ledger**: follow-up record connecting residual traces,
  Action Packets, or calibration reports to later command, runtime, source,
  human-review, or external observations. It is empirical feedback, not a truth
  oracle.
- **Residual Route Policy Report**: non-authorizing synthesis of route
  calibration, baseline comparison, and outcome feedback into keep, watch,
  reroute, block, or insufficient-evidence recommendations for future route
  policy.
- **Residual Route Experiment Manifest**: non-authorizing pre-run plan that
  states which route group, baseline, route-pairing evidence, outcome window,
  success criteria, and stopping rules will govern a route cohort before
  calibration results are interpreted.
- **Residual Route Experiment Review**: non-authorizing comparison between a
  route experiment manifest and actual calibration, baseline, pairing, and
  outcome artifacts. It prevents post hoc route promotion from cherry-picked
  traces.
- **Residual Route Change Proposal**: non-authorizing HIGHBALL artifact that
  turns a route policy report into maintainer-review candidate changes, required
  gates, and affected documentation or host-overlay paths. It does not edit
  routing rules.
- **Residual Evidence Chain**: cross-artifact reference path from route policy
  report to calibration report, outcome ledger, Action Packet, route pairing
  report, residual trace, and residual ids. It prevents locally valid artifacts
  from forming a broken evidence story.
- **Orchestration-Oversight Separation**: execution and judgment remain
  separate.
- **Three-Mechanism Epistemology**: agent, workflow, and command evidence make
  different kinds of claims and must not be collapsed into one authority.
- **Cross-Model Adversarial Depth**: independent perspectives from cross-model
  adversarial verification.
- **Refined Brute Force**: governed brute-force ensembling under explicit
  evidence and closure constraints.

## Gate Terms

- **Amamon**: ambiguity gate. Clarify before acting when intent, scope, or
  referent is unclear.
- **Kyōmon**: mirror gate. Comparative and routing claims require bidirectional
  evidence.
- **Shōmon**: testimony gate. Consequential claims enter the testimony and
  cross-examination route.
- **Kan'nukimon**: anti-drift gate. Prompts use task-first framing, semantic
  isolation, and first-line restatement.

## Metrics

- **Yabu no Naka Index**: R1 divergence measure.
- **Kurosawa Check**: R2 mandatory cross-review and adversarial verification.
- **Kyōmon IR**: Kyōmon interception rate.
- **Model Multiplicity**: multiple equally valid analyses may exist for the
  same input.
- **Partial Order Consensus**: consensus represented as a partial order with
  incomparable pairs when claims cannot be safely ranked.
- **Rashomon Ratio**: stability coefficient comparing surviving consensus with
  the union of claims.
- **Uncertainty Decomposition**: routes aleatoric uncertainty through Amamon
  and epistemic uncertainty through Shōmon.
- **CDA (Cross-Detection Asymmetry)**: relative error detection rates between
  perspective pairs.
- **Diversity Score**: system health signal for correlated perspectives and
  same-model echo.
- **Fleiss' Kappa**: multi-rater agreement adjusted for chance.
- **NMI (Normalized Mutual Information)**: structural similarity between
  agreement patterns across debates.

## Retired Or Externalized Terms

RASHOMON no longer treats KOZO, KANSA, Semantic PBFT, or Oestrus as active
ontology components. Historical documents may mention them, but the active
contract is Residual Trace plus HIGHBALL residual closure.
