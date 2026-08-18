# Assumptions Review — which of RASHOMON's claims are load-bearing, and how an implementation checks them

Status: 2026-08-18, after the five gates were mapped onto an implementation
of the doctrine.

## Sound assumptions (structural, cheap to hold)

1. **Cross-detection beats self-review.** An observer reviewing another's
   account catches errors the author cannot self-detect. This is a
   structural claim, and it is the strongest card RASHOMON plays. It is
   also the weakest to transfer to LLMs: self-review by the *same model*
   is known to be weak, but cross-review strength between models is an
   empirical question — measured, not assumed, below.

2. **Residuals over votes.** The value is not majority wins; it is that
   disagreement becomes a preserved, verifiable artifact. Sound, and an
   implementation instantiating the doctrine enforces it strictly: dissent is
   recorded, high-risk residuals survive arbitration omissions, merge is
   deterministic.

3. **External constitution (Kennōmon).** The enforcer must not be the
   constrained. Sound — it breaks the self-execution circularity, and the
   governance-boundary instrument's Protected-Write Guard instantiates it
   outside the operator's session.

4. **Clarify, don't guess (Amamon), and anchor every claim to evidence
   (Kyōmon).** Sound economics and sound mechanics; both are now enforced
   by schema and gate rather than by habit.

## The load-bearing assumption: five prompt schools = five perspectives

RASHOMON's founding metaphor — woodcutter, bandit, wife, ghost — describes
*genuinely different observers*: different positions, different priors,
different interests. The single-vendor doctrine replaces those with five
prompt-framed schools on **one model family**: same weights, same training
distribution, same RLHF alignment. The schools are five hats on one head.

This is not a refutation; it is a hypothesis that must be **measured**:

- If the five schools agree ~100% of the time, the adversarial value is
  nil — either the schools are not differentiated enough or the questions
  never matter. The run is paying for theater.
- If they disagree chaotically, the merge produces noise rather than
  signal, and dissent inflation destroys the residual's meaning.
- Within one family, *sycophantic cascade* (lanes converging on the same
  wrong answer because they share alignment) is a plausible failure mode
  that no amount of school framing is guaranteed to break.

The cross-detection claim therefore holds *conditionally*: only insofar as
the manufactured perspectives actually diverge on material questions. The
same-model caveat in `trial_manifest` is the honest label for this
conditionality — it travels with every result and the host gate records it.

## How an implementation measures it

An implementation instantiating this doctrine measures the divergence per run
through its contestation predicate: verdict disagreement, disposition
conflicts, attestation asymmetry, and the contested-lane set are computed in
code. The durable skipped-round record (k=0) and the contested-only follow-up
packet turn those into per-run observables.

**Follow-up instrumentation (next step):** aggregate these into the
result's `trial_manifest` — observed verdict distribution, residual
attestation counts, contested rate k/n — so every run self-reports how
much perspective actually diverged, and the operator can track the
healthy band over time. A k/n stuck at 0 (or 1) is the signal that the
load-bearing assumption needs rework: stronger school differentiation,
question selection that earns contention, or — when budget exists — a
second family.

## Verdict

The *structure* of RASHOMON is sound: multi-perspective confrontation,
residual preservation, and external constitution are the right
architecture. The *operational assumption* — that one model family
wearing five school hats produces the perspective diversity the
architecture needs — is the load-bearing hypothesis, now instrumented
rather than asserted.
