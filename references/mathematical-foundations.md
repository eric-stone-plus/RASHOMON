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
| **NMI (Normalized Mutual Information)** | `NMI(X,Y) = 2·I(X;Y)/(H(X)+H(Y))` — structural similarity between debate agreement patterns | Information Theory — detects cross-debate drift in *how* agents agree, not just *how much* |

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

### 5.1 Cross-Debate Drift Detection (κ-drift)

Single-debate κ is a snapshot. Systematic change across debates requires temporal monitoring.

**Method**: Record κ_t per debate. Establish baseline μ_κ ± 2σ from first 5 debates. Flag any subsequent debate where |κ_t - μ_κ| > 2σ.

**Interpretation**:
- κ_t declining → agent agreement weakening over time. Possible causes: model updates, prompt entropy accumulation, concept drift.
- κ_t rising → agent agreement strengthening. In single-model deployment, rising κ may indicate deepening shared blind spot rather than improving truth-seeking.
- κ_t volatile → unstable debate dynamics. May reflect inconsistent prompt construction or changing question complexity.

**Precision**: Requires ≥5 debates for stable baseline. Before 5 debates, flag only extreme deviations (κ < 0 or κ > 0.95). Computationally trivial — κ is already computed per debate.

### 5.2 Pairwise κ Dependency Matrix

Global κ aggregates all 5 agents. The pairwise κ matrix decomposes agreement into agent-pair contributions:

```
        hm    cc    cw    omp   rx
    hm  1.0   κ_hc  κ_hw  κ_ho  κ_hr
    cc   —    1.0   κ_cw  κ_co  κ_cr
    cw   —     —    1.0   κ_wo  κ_wr
    omp  —     —     —    1.0   κ_or
    rx   —     —     —     —    1.0
```

**Interpretation**: High pairwise κ between two agents across multiple debates → redundant information → effective Rashomon Depth < 5. If hm↔cc pairwise κ consistently > 0.8 while hm↔rx κ < 0.4, the debate's effective independent perspectives are approximately 3, not 5.

**Cross-debate tracking**: Pairwise κ drift — if hm↔cc κ drops from 0.7 to 0.3 across 5+ debates, something structural changed in how those agents interact. Flag as potential model update effect or prompt template degradation.

### 5.3 Blind Spots and Mitigations

κ has four structural limitations that must be annotated, not hidden:

| Blind Spot | Description | Mitigation |
|------------|-------------|------------|
| **Echo Paradox** | Same-model deployment: independence null is wrong baseline. κ may be inflated — high κ could be model consistency, not evidential convergence. | Annotate κ>0.8 with: "All agents share model weights — high κ may reflect model consistency rather than independent confirmation." |
| **Binary Compression Loss** | κ operates on confirm/not-confirm. Confidence gradation (strong vs. weak confirm, hedged vs. emphatic) is discarded. | Report κ with 95% CI, not point estimate. Future: weighted κ extension if agents adopt standardized confidence annotations. |
| **κ≈1.0 = Most Dangerous** | Near-perfect agreement is a red flag for shared blind spot, not a success signal. | κ>0.8 triggers mandatory R2 confirmatory audit annotation. Never report κ≈1.0 as "excellent consensus." |
| **Small-N Instability** | 5 raters × 15 claims → SE(κ) ≈ ±0.15. Single-debate κ shifts of <0.2 are noise, not signal. | Always report κ with 95% CI. Use κ-drift across ≥5 debates for trend detection — aggregates reduce SE.

---

## 6. Normalized Mutual Information — Cross-Debate Structural Comparison (Cover & Thomas 1991)

**Source**: Cover, T.M. & Thomas, J.A. (1991). *Elements of Information Theory*. Wiley.

**Definition**: Normalized Mutual Information measures the dependence between two clusterings of the same set of objects:

```
NMI(X, Y) = 2 · I(X; Y) / (H(X) + H(Y))
```

where I(X;Y) is mutual information and H(·) is entropy. NMI ∈ [0,1]; 0 = independent clusterings, 1 = identical.

**QUINTE mapping**: NMI operates at the **debate-pair** level, not the claim level. Two debates D_a and D_b are each represented as their agreement structure — the claim×agent binary matrix or its derived clustering. NMI(D_a, D_b) measures how structurally similar the two debates are.

**Why debate-pair, not agent-pair.** Agent-pair NMI (comparing how agent A and agent B cluster claims within a single debate) requires sufficient claims per debate for stable estimation — a constraint rarely met in QUINTE's typical 10–40 claim range. Debate-pair NMI treats each debate as an object, comparing whole-debate agreement structures. This sidesteps the cold-start problem that agent-pair NMI faces.

**Interpretation**:
- NMI > 0.9 across consecutive debates → agreement structure is stable → system behavior is stationary
- NMI declining over time → agreement patterns are shifting → potential model update effects, prompt degradation, or concept drift
- NMI between debate pairs separated by a model update → direct measurement of how much the update changed agent behavior
- Cluster of debates with high pairwise NMI → a "debate regime" — similar questions produce similar agreement patterns

**Cold-start requirement**: NMI requires ≥5 debates for stable estimation. Before 5 debates, only κ time-series (κ-drift) is available. After 5+ debates, NMI complements κ-drift: κ-drift detects *magnitude* shifts in agreement, NMI detects *structural* shifts in how agreement is organized across agents.

**Relationship to κ**: κ measures *how much* agents agree. NMI measures *how similarly* they agree across debates. A system can have stable κ (0.6 ± 0.05 across 10 debates) but decaying NMI — agents agree at the same rate, but *which* claims they agree on is shifting. This pattern would be invisible to κ alone.

**Precision**: Computable once ≥5 debates are archived. No ground truth required. Debate-pair NMI avoids the "same items" trap that limits agent-pair NMI — debates are compared as structural objects, not as claim vectors.

**Relationship to Diversity Score**: Diversity Score = 1 - mean(pairwise κ) measures *within-debate* agent independence. NMI measures *cross-debate* structural stability. Together they span both dimensions: Diversity tells you whether perspectives are genuinely independent; NMI tells you whether that independence is stable over time.

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
5. Fleiss, J.L. (1971). "Measuring Nominal Scale Agreement Among Many Raters." *Psychological Bulletin*, 76(5):378–382.
6. Cover, T.M. & Thomas, J.A. (1991). *Elements of Information Theory*. Wiley.

---

*mathematical-foundations.md — ratified 2026-06-10 (hm+cw+omp+rx, cc unavailable)*
