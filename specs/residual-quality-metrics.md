# Residual Quality Metrics

> A residual trace is useful only when its residuals are inspectable, evidenced,
> and closed or escalated at the right boundary. Quality is derived by the
> consumer, not self-declared by the producing instrument.

## 1. Measurement Claim

RASHOMON does not treat debate agreement as the main success metric. It treats
residual quality as the measurable object.

The measurement layer answers four questions:

1. Did the run preserve material residuals instead of laundering them into a
   smooth answer?
2. Are residuals tied to source, evidence, and affected scope?
3. Are action-blocking residuals closed, blocked, waived, or marked not
   applicable with evidence and scope?
4. Does the trace show false-consensus risk, such as low evidence with high
   convergence or explicit `silent_collapse` residuals?
5. Does the trace declare the trial conditions that produced the residuals:
   perturbation axes, independence controls, contamination risks, and cost?

These metrics are derived from the trace after production. QUINTE, MAGI, or any
other producer may not close the loop by merely asserting that its own output is
high quality.

## 2. Core Metrics

- Residual Count: number of residuals preserved in the trace. Zero residuals near protected action may require review.
- Evidence Coverage: fraction of residuals with non-empty `evidence`. Low coverage means findings are present but not inspectable.
- Closure Evidence Coverage: fraction of residuals with non-empty `closure_evidence`. Low coverage means closure is asserted without support.
- Action-Blocking Closure Coverage: fraction of action-blocking residuals closed, blocked, waived, or not applicable with evidence and scope. Low coverage means discovered risk is being converted into permission.
- Open High-Risk Count: count of `HIGH`, `CRITICAL`, or `P0` residuals whose `closure_state` is `open`. Protected or irreversible action should block.
- Unsupported High-Risk Closure Count: count of high-risk residuals marked closed, blocked, waived, or not applicable without evidence or scope. This is closure laundering.
- Silent-Collapse Count: count of `silent_collapse` residuals. Agreement may be correlated rather than evidential.
- Decision Conflict Count: count of runtime decisions that contradict high-risk residual state. A `pass` decision conflicts with open or unsupported high-risk findings.
- Trial Manifest Present: whether `trial_manifest` is present. A strict-boundary trace without one cannot show how residuals were produced.
- Independent First-Pass Count: count of manifest perspectives with `independent_first_pass: true`. Low count indicates simulated plurality or contaminated review.
- Perturbation Axis Count: number of declared perturbation axes. Low count means the trace may not distinguish observer-position changes from repeated sampling.
- Same-Model Flag: whether the manifest says `same_model` or `same_family`. Consensus should be treated as stability, not independent confirmation.
- Cost Fields Present: whether cost fields are present. Without them, residual yield cannot be compared to self-correction or direct-evidence baselines.

## 3. Action-Blocking Residuals

A residual is action-blocking when any of the following holds:

1. `severity` is `HIGH`, `CRITICAL`, or `P0`.
2. `required_closure` is not `none`.
3. `disposition` is `escalated`.

Low-severity residuals may still be action-blocking when they affect a protected
boundary. The trace should express that with `required_closure`.

## 4. Advisory Gate

The measurement layer may produce an advisory gate:

- `pass`: no open or unsupported action-blocking risk is visible in the trace.
- `review`: the trace is structurally valid, but evidence or residual coverage is weak.
- `block`: a protected or irreversible boundary has open or unsupported high-risk residuals, or the trace decision contradicts the residual state.

This advisory gate does not replace HIGHBALL authorization. It helps operators
decide whether the residual trace is informative enough to rely on.

## 5. Anti-Gaming Rule

Metrics can be gamed by omitting residuals. Therefore a low residual count is
never proof of safety. It is only proof that few residuals were preserved.

For consequential action, an empty trace should be paired with direct runtime
evidence, source evidence, or explicit human review. Otherwise it should be
treated as a review signal, not as confidence.

The same applies to missing trial conditions. A trace can be structurally valid
without `trial_manifest`, but a protected or irreversible action should review
that trace unless direct evidence or a scoped human waiver explains why
perspective perturbation is not relevant.

## 6. Ownership

RASHOMON defines metric meaning. HIGHBALL or another host measurement layer may
implement the calculation. QUINTE and MAGI should produce enough trace material
for the metrics to be derived, but they should not be trusted as the authority
on their own trace quality.

## 7. Archive Adoption

Historical debate archives may predate the residual trace contract. They should
not be rewritten merely to improve metrics. Instead, scan them as historical
evidence and report adoption separately:

- Scanned Files: files inspected by the archive scanner.
- Files With Trace: files containing at least one residual trace.
- Trace Adoption Rate: files with traces divided by scanned files.
- Valid Trace Rate: valid traces divided by files with traces.
- Blocked Trace Files: files whose traces are valid enough to parse but contain open or unsupported high-risk residuals.
- Invalid Trace Files: files containing trace-like JSON that fails structural validation.

Archive adoption is a migration metric, not a truth metric. A low adoption rate
does not invalidate historical debates; it identifies which archives cannot yet
serve as machine-checkable protected-action evidence.

## 8. Action Packet Use

Quality metrics become action-relevant when bound to the original route request
and residual trace. HIGHBALL's Action Packet records that binding. RASHOMON
defines the meaning of the metrics; HIGHBALL owns the packet format and the
runtime boundary decision.

## 9. Empirical Calibration

Trial manifest metrics let the ecosystem compare residual yield against cost
and baseline routes:

- same-model QUINTE versus isolated self-correction
- MAGI convergence versus direct evidence
- heterogeneous review versus same-family review
- high perturbation-axis count versus residual inflation
- token and wall-time cost versus action-blocking residuals surfaced

This is the path from philosophy to falsifiable engineering. If a route burns
more resources while surfacing no higher-quality residuals than a simpler
baseline, HIGHBALL should route future work differently.

HIGHBALL may implement this as residual trial scoring: a bounded profile over
residual yield, closure strength, manifest strength, risk penalty, and
cost-normalized yield. The score is not truth probability. It is a calibration
signal for whether MAGI, QUINTE, direct evidence, or human review was the right
route for similar future work.

## 10. Route Calibration

Residual trial scoring applies to one trace or trace bundle. Route calibration
applies to cohorts.

A route-calibration ledger should group traces by instrument, base-model
relation, and action boundary, then compare residual yield, closure strength,
manifest strength, risk penalty, invalid trace rate, and cost-normalized yield.
This keeps same-model behavioral perturbation separate from heterogeneous
review and direct evidence.

Route calibration does not decide whether a claim is true. It decides whether a
route has historically produced enough inspectable residual value to justify
using it again, rerouting to a cheaper baseline, escalating to QUINTE or human
review, or blocking when high-risk residuals remain open.

Malformed trace candidates must be reported, not silently dropped. Otherwise a
route can look clean merely because failed artifacts disappeared before
measurement.

A route-calibration report is a boundary object like an Action Packet: RASHOMON
defines the meaning of residual quality signals, while HIGHBALL owns the
machine-readable report format and validator.

## 11. Route Baseline Feedback

Route calibration can overvalue a route when it is judged only against itself.
Baseline comparison asks whether a target route outperformed a cheaper,
stronger, or more direct same-boundary route.

This is especially important for same-model QUINTE. A single-base-model debate
may expose useful behavioral residuals, but it must still earn its cost against
isolated self-correction, direct verification, human review, or heterogeneous
review when those routes exist.

RASHOMON defines the semantic claim: residual value is comparative, not
self-certifying. HIGHBALL owns the concrete route-baseline report format and
validator.

Same-question route pairing is the more local version of this rule. A target
trace and baseline trace answer the same question under the same action
boundary, then HIGHBALL compares residual scores and risk deltas. This avoids
LLM-as-judge preference voting and asks whether the route exposed better
residual evidence.

## 12. Route Experiment Review

Calibration, pairing, and baseline evidence can still be misleading when the
cohort is chosen after the result is known. A route experiment manifest
registers the planned route group, trace inputs, pair manifest, baseline routes,
outcome requirements, success criteria, and stopping rules before the route is
promoted. A route experiment review compares that plan with the actual
calibration, pairing, baseline, and outcome artifacts.

This is the pre-registration hook for residual-first engineering. It does not
make a route true or authorized; it prevents a route from claiming empirical
support when the evaluation was assembled after the fact.

RASHOMON defines the semantic claim: route evidence should be planned before it
is used for policy. HIGHBALL owns the concrete route experiment manifest and
review formats and validators.

## 13. Outcome Feedback

Route calibration remains a proxy until follow-up outcomes are recorded. A
residual outcome ledger connects traces, Action Packets, and calibration
reports to later evidence:

- command or test results
- runtime behavior
- source verification
- scoped human review
- external observations or incident reports

Outcome feedback does not prove universal truth. It records whether later
evidence supported, contradicted, failed to resolve, or regressed against what
the trace and route decision implied.

This is the falsifiability hook for residual-first architecture. A route that
scores well but later accumulates negative outcomes should be rerouted or
downgraded. A route that scores modestly but repeatedly surfaces action-blocking
residuals later confirmed by direct evidence may deserve stronger default use.

RASHOMON defines the semantics of outcome feedback. HIGHBALL owns the concrete
outcome-ledger format and validator.

## 14. Route Policy Feedback

Once calibration reports and outcome ledgers exist, a consumer may synthesize
them into a route-policy recommendation. This is not an authorization decision
and not a live router mutation. It is an evidence packet for maintainers:

- keep the route policy
- watch and collect more outcomes
- reroute future similar work
- block reuse for similar protected boundaries
- declare evidence insufficient

This layer matters because route learning is dangerous when automated. A system
that silently rewrites its own router from weak outcomes can amplify correlated
errors. RASHOMON therefore treats route policy synthesis as reviewed evidence,
not self-modification.

HIGHBALL owns the concrete route-policy report format and validator.

## 15. Route Execution Feedback

Residual quality can look strong while the route that produced it is
operationally unreliable. For QUINTE, a protected-boundary trace is not enough
if R1, R2, or R3 dispatch evidence is missing, degraded, blocked, or invalid.

Route execution feedback aggregates that operational signal across Action
Packets. It asks whether the route reliably produced the evidence its boundary
contract required. This is separate from residual quality: one measures the
trace; the other measures whether the route actually ran.

RASHOMON defines the semantic claim: provenance and execution completeness are
part of residual evidence. HIGHBALL owns the concrete route execution report
format and validator.

## 16. Evidence Chain Integrity

Every artifact in the residual workflow can be locally valid while still being
wrongly connected to the others. An outcome entry may cite a residual id that
does not exist. A route policy report may combine a calibration report for one
route group with outcomes from another. A trace source listed in a calibration
report may never have participated in the observed outcome. A route experiment
review may cite a manifest for one cohort while a policy report uses another.

Residual-first engineering therefore needs evidence-chain validation in
addition to schema validation. The chain should connect:

- route policy report
- route calibration report
- route execution report when policy evidence depends on dispatch reliability
- outcome ledger
- route experiment manifest and review when policy evidence depends on a
  pre-run plan
- Action Packet when one exists
- residual trace
- residual ids

RASHOMON defines why the chain matters: residual claims only remain meaningful
when their provenance survives synthesis. HIGHBALL owns the concrete chain
validator.
