# Residual Trial Manifest

> A residual trace says what was found. A trial manifest says under what
> perturbation conditions it was found.

## 1. Purpose

Residual-first evaluation is only meaningful if the observer positions are
inspectable. Otherwise a verdict can claim independent perspectives while all
outputs came from one hidden narrator, one contaminated prompt, or one
correlated same-model swarm.

The trial manifest records the experimental conditions behind a residual trace:
which perspectives existed, what artifacts they produced, what perturbations
were applied, what independence controls were used, what contamination risks
remain, and how much the run cost.
It may also name external execution-evidence artifacts, such as QUINTE dispatch
ledgers, through perspective artifact references or a consumer-side Action
Packet. Those ledgers are not residuals themselves; they prove whether the
claimed perspectives actually ran.

This makes same-model residual exposure scientifically weaker but still useful.
The manifest does not pretend same-model disagreement is transformer-internal
access or independent confirmation. It records it as behavioral instability
under specified perturbations.

## 2. Relationship To The Trace

`trial_manifest` is an optional top-level field in
`schemas/residual-trace.schema.json`.

Earlier traces may lack it. New traces near protected or irreversible
action boundaries should include it so a host can distinguish:

- residuals produced under independent first-pass review
- residuals produced by simulated plurality
- same-model stability under prompt perturbation
- cross-model or human heterogeneity
- direct evidence with little or no perspective perturbation

If a strict-boundary trace lacks a manifest, consumers should treat that as a
review signal, not a structural schema failure.

## 3. Required Fields

- `manifest_version`: version of the trial manifest format.
- `base_model_relation`: relationship among producing perspectives, such as `unknown`, `same_model`, `same_family`, `heterogeneous_models`, `mixed`, `human`, or `direct_evidence`.
- `perspective_count`: number of perspectives or evidence routes represented.
- `perspectives`: perspective records with role, route, artifact, prompt hash, and independent first-pass flag.
- `perturbation_axes`: controlled observer-position differences, such as role, evidence budget, order, adversarial duty, or reviewer position.
- `independence_controls`: controls used to reduce contamination, such as separate artifacts, first-pass isolation, anonymous cross-review, fixed manifest, or source verification.
- `contamination_risks`: known residual risks, especially same-model correlation, shared training distribution, anchoring, or prompt leakage.
- `cost`: approximate token, wall-time, tool-call, and human-review cost.

## 4. Interpretation

The manifest does not prove truth. It bounds the evidential claim.

- Same model with independent first-pass artifacts: evidence of behavioral instability or stability under controlled perturbation.
- Same family with shared prompts: weak diversity; treat consensus cautiously.
- Heterogeneous models with separate artifacts: stronger error decorrelation, still not proof.
- Human or direct evidence route: different evidence class; useful for closure but not a debate substitute.
- Missing artifacts, missing prompt hashes, or no independent first pass: simulated plurality risk; review before relying on the trace.

## 5. Quality Signals

Consumers may derive manifest quality signals:

- Manifest Present: the trace declares its trial conditions.
- Perspective Count: number of recorded perspectives.
- Independent First-Pass Count: number of perspectives formed before reading peer outputs.
- Perturbation Axis Count: number of controlled observer-position differences.
- Contamination Risk Count: number of known residual contamination risks.
- Same-Model Flag: whether the trace is same-model or same-family and should not be treated as independent confirmation.
- Cost Fields Present: whether resource cost was recorded for cost-quality comparison.

These signals support empirical calibration against direct evidence,
self-correction, and historical archive outcomes.

HIGHBALL may turn these signals into residual trial scoring: a route-quality
profile over residual yield, closure strength, manifest strength, risk penalty,
and cost-normalized residual yield. The score is not a truth probability; it is
evidence for route selection and future calibration.

When enough traces accumulate, consumers may perform route calibration by
grouping scored traces by instrument, base-model relation, and action boundary.
The manifest is what prevents those cohorts from mixing same-model perturbation
evidence with heterogeneous review, direct execution, or human judgment.

## 6. Anti-Gaming Rule

A manifest can be forged as easily as any JSON. Therefore it is not authority by
itself. Its purpose is to make claims auditable:

- artifacts can be checked against files
- prompt hashes can be compared across runs
- route names can be checked by HIGHBALL/SHIMEI
- QUINTE dispatch ledger references can be checked by HIGHBALL Action Packets
- cost can be compared against residual yield
- contamination risks remain visible instead of being hidden behind consensus

The manifest raises the cost of pretending that one narrator is many witnesses.
