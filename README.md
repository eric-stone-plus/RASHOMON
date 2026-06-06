# RASHOMON

> 芥川龍之介《藪の中》（1922）→ 黒澤明《羅生門》（1950）→ AI agent truth-seeking

**RASHOMON** is the philosophical foundation of the QUINTE debate protocol. It asks the question QUINTE is built to answer: *when a single perspective cannot be trusted, how do we converge on actionable truth?*

## About

RASHOMON is the philosophical companion to [QUINTE](https://github.com/eric-stone-plus/QUINTE), a five-agent structured debate protocol. Where QUINTE specifies *how* to orchestrate multi-agent cross-examination, RASHOMON explores *why* this approach is necessary — grounding the protocol in Kurosawa's 1950 film *Rashomon* and the broader problem of single-perspective truth in AI systems.

## The Rashomon Problem

Kurosawa's *Rashomon* (1950) presents four witnesses to the same event offering mutually contradictory testimonies. Not because anyone is lying — but because each person sees only what their position allows them to see.

This is the exact problem facing single-agent AI systems. One model, one perspective, one blind spot. The answer isn't a better model — it's a *structure that forces perspectives to confront each other*.

## The QUINTE Answer

[QUINTE](https://github.com/eric-stone-plus/QUINTE) is the engineering layer — a five-agent structured debate protocol that operationalizes the Rashomon insight. Where RASHOMON asks *why*, QUINTE builds *how*.

QUINTE implements the second gate (證門 Shōmon) of the three-gate discipline:

```
                       User asks a question
                                 ▼
          ╔═══════════════════════════════════════════════╗
          ║  雨門 Amamon · Ambiguity Gate                  ║
          ║  (雨 = rain, the uncertainty before            ║
          ║   entering Rashomon's gate)                   ║
          ║                                               ║
          ║  "What am I actually being asked?"            ║
          ║                                               ║
          ║  Vague or ambiguous?                          ║
          ║    ├─ Yes → clarify() first                   ║
          ║    └─ No  → pass through                      ║
          ║                                               ║
          ║  Operated by: Hermes (pre-debate check)       ║
          ╚═══════════════════════════════════════════════╝
                                 ▼
                           Clarification
                                 ▼
          ╔═══════════════════════════════════════════════╗
          ║  證門 Shōmon · QUINTE Gate                     ║
          ║  (證 = testimony, evidence)                    ║
          ║                                               ║
          ║  Structured multi-agent debate                ║
          ║                                               ║
          ║  R1 · 4 agents analyze independently          ║
          ║  R2 · 5 agents cross-review                   ║
          ║  R3 · Hermes synthesizes verdict              ║
          ║                                               ║
          ║  R2 never skipped — consensus can             ║
          ║  hide shared blind spots                      ║
          ║                                               ║
          ║  R2 finds fatal flaw?                         ║
          ║    └─ restart R1 (once)                       ║
          ║                                               ║
          ║  Operated by: Hermes + 5 agents (R1–R3)       ║
          ╚═══════════════════════════════════════════════╝
                                  ▼
                             Verification
                                  ▼
          ╔═══════════════════════════════════════════════╗
          ║  閂門 Kan'nukimon · Anti-Drift Gate            ║
          ║  (閂 = bolt, latch — no collusion)             ║
          ║                                               ║
          ║  "No witness collusion"                       ║
          ║                                               ║
          ║  Every prompt to external agents              ║
          ║  must use three-layer defense:                ║
          ║    ① Task-first (task before context)         ║
          ║    ② ONLY Y, not NOT X                        ║
          ║       e.g. "Use Rust" not "Don't              ║
          ║       use Python" — positive framing          ║
          ║       prevents concept collision              ║
          ║    ③ TASK: restatement required               ║
          ║                                               ║
          ║  Drift detected? → kill & retry               ║
          ║                                               ║
          ║  Operated by: Hermes (prompt construction)    ║
          ╚═══════════════════════════════════════════════╝
                                 ▼
                               Output
```

## Structure

| File | Content |
|------|---------|
| [GATES.md](GATES.md) | The Three Gates — 雨門·證門·閂門 |
| [CONCEPTS.md](CONCEPTS.md) | Core concepts — Rashomon Depth, YNI, Kurosawa Check |
| [PHENOMENOLOGY.md](PHENOMENOLOGY.md) | Phenomenological expansion (forthcoming) |

## Cultural Anchors

- **芥川龍之介**《藪の中》（1922）— seven testimonies, one death, no resolution
- **黒澤明**《羅生門》（1950）— Venice Golden Lion, Academy Award for Best Foreign Language Film
- **Rashomon Effect** — entered English academic vocabulary: contradictory interpretations of the same event by different observers

## License

MIT
