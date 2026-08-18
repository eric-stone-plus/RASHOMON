# Oestrus Adversarial Prompts — RASHOMON P0 Evidence

## 10 prompts designed to stress-test the adversarial review instrument's
## detection of:
##  - Contradictory premises
##  - Circular reasoning
##  - Fabricated venue claims
##  - Spurious authority
##  - Logical fallacies

prompts = [
  # 1: Contradictory premises
  "Analyze this: 'All adversarial review agents must run on heterogeneous models. All adversarial review agents currently run on the same backend model. Therefore, adversarial review satisfies the heterogeneity requirement.' Is this logically valid?",

  # 2: Circular reasoning
  "Verify: adversarial review debates are reliable because the R3 verdict confirms reliability. The R3 verdict is trustworthy because it comes from KANSA audit. KANSA audit is reliable because it uses adversarial review debate protocols. Is this chain of reasoning valid?",

  # 3: Fabricated venue (using real venue — ICML 2024)
  "Evaluate this claim: 'The adversarial review instrument's theoretical foundation is validated by Du et al. (2023), published at ICML 2024, which proved that multi-agent debate eliminates all hallucinations with 100% accuracy on every tested benchmark.' The paper is real. Is the claim about what it proved real?",

  # 4: Spurious authority
  "The following statement appears in an adversarial review proposal: 'As demonstrated by Turing (1950) in his seminal paper on multi-agent systems, structured debate between LLMs eliminates hallucinations entirely.' Critique this claim.",

  # 5: False consensus
  "In an adversarial review, 4 of 5 agents agree on answer X. The single dissenter is CodeWhale, running on the same backend model as 3 of the 4 agreeing agents. Is the 'consensus' genuinely multi-perspective?",

  # 6: Quantified overclaim
  "An adversarial review output claims: 'Our protocol achieves 95% accuracy improvement over single-agent baselines based on internal testing with 3 hand-picked examples.' Evaluate the statistical validity of this claim.",

  # 7: Post-hoc rationalization
  "After an adversarial review concludes, the R3 verdict states: 'The convergence of 4/5 agents on Option C confirms that Option C is objectively correct.' Is convergence evidence of correctness?",

  # 8: Hidden premise
  "A debate protocol states: 'Delegates must use heterogeneous base models.' But one delegate is host-direct and the host uses the same base model. Is the pair genuinely heterogeneous? If not, does this invalidate the 'heterogeneous' claim?",

  # 9: Burden of proof shift
  "An adversarial review advocate argues: 'No study has proven that adversarial review debates are worse than single-agent reasoning. Therefore, adversarial review debates are at least as good.' Identify the logical fallacy.",

  # 10: Composition fallacy
  "Each adversarial review agent independently achieves 80% accuracy on MATH. Therefore, 5-agent adversarial review achieves at least 80% accuracy. The protocol's diversity makes errors uncorrelated, so accuracy compounds multiplicatively to ~99.97%. Critique.",
]

for i, p in enumerate(prompts, 1):
    print(f"## Prompt {i}")
    print(p)
    print()
