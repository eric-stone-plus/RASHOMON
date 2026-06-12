# Mathematical Foundations

> **Honesty statement**: The relationship between QUINTE and ML Rashomon Set theory is **heuristic, not isomorphic**. QUINTE lacks the three formal prerequisites — a loss function L̂, an optimal model f*, and ground truth labels. Partial Order consensus (JMLR 2023) is the strongest structural analogy. Concepts below are introduced as structural inspiration, not as mathematical instantiations within QUINTE.

---

## 1. Model Multiplicity (Breiman 2001)

**Source**: Leo Breiman, "Statistical Modeling: The Two Cultures" (2001).

**Definition**: In ML, many models with different internal structures can achieve near-identical predictive performance on the same dataset. Single-model feature importance is unreliable — switch the model, and feature rankings can change dramatically.

**QUINTE mapping**: This is the mathematical existence proof for QUINTE's core premise. A single agent's analysis is unreliable not because the agent is flawed, but because **model multiplicity is a mathematical property of underdetermined problem spaces**. Multiple equally-valid analyses exist — QUINTE surfaces them through structured debate rather than hiding them behind a single output.

**Precision**: Heuristic analogy. The mechanism differs: ML multiplicity arises from non-convex optimization landscapes; QUINTE's multi-agent divergence arises from different reasoning paths, toolchains, and attention biases.

---

## 2. Partial Order Consensus (JMLR 2023)

**Source**: Laberge, Pequignot, Mathieu, Khomh & Marchand. "Partial Order in Chaos: Consensus on Feature Attributions in the Rashomon Set." *Journal of Machine Learning Research*, Vol. 24 (2023). Peer-reviewed.

**Definition** (JMLR 2023, Def. 4, Eq. 14): Feature i is locally less important than feature j across the entire Rashomon Set iff **every** model in the set agrees:

$$i \preceq_{\epsilon,x} j \iff \forall h \in \mathcal{R}(\mathcal{H}, \epsilon) \quad |\phi_i(h, x)| \leq |\phi_j(h, x)|$$

When no consensus exists, features are **incomparable** — the method abstains rather than forcing a ranking.

**QUINTE mapping**: R2 consensus detection operates on the same principle. Claims supported by **all** agents enter the consensus pool (≈ partial order relations). Claims with conflicting support are flagged as **contested** (≈ incomparable pairs) and deferred to the user rather than resolved by majority vote. The theorem that partial orders are "conservative over total rankings" mirrors QUINTE's design: R3 verdicts are a subset of what any individual agent would claim.

**Precision**: Structural analogy. The JMLR paper operates within a loss-function framework over model spaces; QUINTE's agent-agreement domain has neither. The structural correspondence — consensus-as-partial-order with incomparable pairs — is the strongest mathematical anchor available.

---

## 3. Rashomon Ratio (Stability Coefficient)

**Source**: "Exploring the Whole Rashomon Set of Sparse Decision Trees" (arXiv:2209.08040). Adapted for QUINTE.

**Definition**: The fraction of claims that survive cross-examination:

$$\text{Rashomon Ratio} = \frac{|\text{consensus claims}|}{|\text{union of all claims across rounds}|}$$

**QUINTE mapping**: A quantitative stability measure for R3 verdicts. High ratio → conclusions are robust across perspectives. Low ratio despite convergence → **Rashomon-fragile** — surface as a formal warning. Gives mathematical teeth to the "dry ≠ done" invariant.

**Precision**: Computable within QUINTE from native primitives (claim sets, diff pools, refutation tallies). No loss function or ground truth required.

---

## 4. Uncertainty Decomposition (Aleatoric vs. Epistemic)

**Source**: ML Rashomon Set theory.

**Definition**:
- **Aleatoric uncertainty**: Irreducible noise inherent in the question itself (ambiguous phrasing, underspecified scope).
- **Epistemic uncertainty**: Reducible uncertainty from model/agent limitations (blind spots, knowledge gaps, attention failures).

**QUINTE mapping**: Provides mathematical vocabulary for the Four Gates' decision logic:
- Aleatoric uncertainty → **Amamon (雨門)**: "Is the question itself ambiguous?" → `clarify()` back to user.
- Epistemic uncertainty → **Shōmon (證門)**: "Can more perspectives resolve this?" → enter debate pipeline.

Currently the Yabu no Naka Index (YNI) conflates both. This decomposition enables a principled routing decision.

**Precision**: Heuristic analogy. The decomposition is a conceptual framework, not a computable quantity within QUINTE.

---

## Existing Mathematical Concepts in RASHOMON

RASHOMON already contains two mathematical constructs that require no external mapping:

| Concept | Formulation | Mathematical Basis |
|---------|------------|-------------------|
| **Yabu no Naka Index (YNI)** | `1 - (intersection / union of claims)` | Jaccard Distance — the canonical set-based divergence metric |
| **Loop-Until-Dry** | Dual-condition termination → single-critic + 3-round hard cap (v3.1) | Fixed-Point Convergence — parallels gradient-descent plateau detection heuristics |
| **Fleiss' Kappa (κ)** | `κ = (P_o - P_e) / (1 - P_e)` — multi-rater agreement adjusted for chance | Inter-Rater Reliability — distinguishes genuine consensus from same-model echo |

---

## 5. Fleiss' Kappa — Multi-Rater Agreement (Fleiss 1971)

**Source**: Fleiss, J.L. "Measuring Nominal Scale Agreement Among Many Raters." *Psychological Bulletin*, Vol. 76, No. 5 (1971). 37,000+ citations.

**Definition**: For N subjects rated by k raters into m categories, Fleiss' Kappa quantifies agreement beyond chance:

```
κ = (P_o - P_e) / (1 - P_e)
```

where P_o = observed proportion of agreement, P_e = expected proportion under random-chance independence.

**QUINTE mapping**: Each debate produces an N-claims × 5-agents binary matrix (confirm / not confirm). Fleiss' Kappa is computed directly from this matrix — zero additional data required.

**Interpretation**:
- κ > 0.8: near-perfect agreement. In single-model deployment, this may indicate shared blind spot rather than truth — R2 adversarial verification must confirm.
- 0.4 < κ < 0.8: moderate agreement. Normal healthy debate range.
- κ < 0.4: weak agreement. Agent perspectives are genuinely divergent — YNI will be high.
- κ < 0: systematic disagreement below chance. Likely prompt ambiguity → return to Amamon.

**Why it matters**: QUINTE's ≥3/5 voting does not adjust for chance agreement. When all 5 agents share DeepSeek v4-pro weights, their base-rate agreement is elevated — a 4/5 vote may reflect model consistency rather than evidential strength. Kappa surfaces this: if same-model agents agree 70% of the time by chance, a 4/5 vote is less impressive than it looks. Kappa quantifies what REFINED-BRUTE-FORCE.md states qualitatively: "same-model consensus = 1 verification × 3 noise samples."

**Precision**: Computable within QUINTE from native primitives (claim-agent binary matrix). Does not require ground truth, calibrated probabilities, or loss functions. Pairwise Kappa can also be computed for agent-pair dependency analysis — high pairwise κ between hm and cc suggests their votes carry redundant rather than independent information.

**Relationship to Rashomon Ratio**: Rashomon Ratio = |consensus|/|union| measures claim-level survival rate. κ measures agent-level agreement strength. A debate can have high Ratio (many claims in consensus pool) but low κ (agent agreement barely above chance — large denominator P_e due to claim volume). Together they distinguish "broad but shallow" consensus from "narrow but deep."

---

## Excluded Concepts (and Why)

| Concept | Reason for Exclusion |
|---------|---------------------|
| **Quine-McCluskey algorithm** | Requires Boolean formula inputs; agent outputs are natural language. Category error. |
| **Rashomon Set formal definition** | Requires L̂ and f*, neither of which QUINTE possesses. Would be pseudo-precision. |
| **Prime Implicants / Petrick's Method** | Boolean algebra concepts with no mapping to QUINTE's semantic consensus domain. |
| **ε-tolerance quantification** | ML's ε is a continuous real; QUINTE's ≥3/5 threshold is qualitative voting. Non-isomorphic. |
| **Bayesian belief updating** | RASHOMON deliberately avoids probabilistic calculus as a prescriptive framework — claims are surfaced/disputed/refuted through structural mechanisms. Conditional probability notation MAY be used descriptively where existing primitives already capture the conditional relationship (e.g., Rashomon Ratio ≈ P(claim in consensus | claim survived cross-examination)). Full prior/likelihood/posterior calculation deferred — no ground truth for calibration. Explicit conditional dependence statement adopted: shared model weights → agent votes not independent → consensus count ≠ independent confirmations. Fleiss' Kappa is the preferred operational metric for agreement strength. |

---

## References

1. Breiman, L. (2001). "Statistical Modeling: The Two Cultures." *Statistical Science*, 16(3):199–231.
2. Laberge, G., Pequignot, Y., Mathieu, A., Khomh, F., & Marchand, M. (2023). "Partial Order in Chaos: Consensus on Feature Attributions in the Rashomon Set." *Journal of Machine Learning Research*, 24.
3. Xin, R., Zhong, C., Chen, Z., Takagi, T., Seltzer, M., & Rudin, C. (2022). "Exploring the Whole Rashomon Set of Sparse Decision Trees." *arXiv:2209.08040*.
4. Li, S., Wang, R., Deng, Q., & Barnard, A. (2023). "Exploring the Cloud of Feature Interaction Scores in a Rashomon Set." *arXiv:2305.10181*.

---

*mathematical-foundations.md — ratified 2026-06-10 (hm+cw+omp+rx, cc unavailable)*
