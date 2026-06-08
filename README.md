# RASHOMON

> 芥川龍之介《藪の中》（1922）→ 黒澤明《羅生門》（1950）→ AI agent truth-seeking

**RASHOMON** is the philosophical foundation of the QUINTE debate protocol. It asks the question QUINTE is built to answer: *when a single perspective cannot be trusted, how do we converge on actionable truth?*

## About

RASHOMON is the philosophical companion to [QUINTE](https://github.com/eric-stone-plus/QUINTE), a five-agent structured debate protocol, and to [KENGEN](https://github.com/eric-stone-plus/KENGEN), the agent authorization perimeter. Where QUINTE specifies *how* to orchestrate multi-agent cross-examination and KENGEN defines *whether* an operation may proceed, RASHOMON explores *why* this approach is necessary — grounding the protocol in Kurosawa's 1950 film *Rashomon* and the broader problem of single-perspective truth in AI systems.

## The Rashomon Problem

Kurosawa's *Rashomon* (1950) presents four witnesses to the same event offering mutually contradictory testimonies. Not because anyone is lying — but because each person sees only what their position allows them to see.

This is the exact problem facing single-agent AI systems. One model, one perspective, one blind spot. The answer isn't a better model — it's a *structure that forces perspectives to confront each other*.

## The Four Gates

QUINTE operates through four mandatory gates, each preventing a distinct failure mode.
The gates follow the woodcutter's journey: arrive in rain, check your eyes, hear the witnesses, bolt the door.

```
                           User asks a question
                                    ▼
   ╔══════════════════════════════════════════════════════════════════╗
   ║  雨門 Amamon · Ambiguity Gate                                     ║
   ║  (雨 = rain — the uncertainty before entering Rashōmon's gate)   ║
   ║                                                                  ║
   ║  "What am I actually being asked?"                               ║
   ║                                                                  ║
   ║  Vague or ambiguous?                                             ║
   ║    ├─ Yes → clarify() first                                      ║
   ║    └─ No  → pass through                                         ║
   ║                                                                  ║
   ║  Operated by: Hermes (pre-debate check)                          ║
   ╚══════════════════════════════════════════════════════════════════╝
                                    ▼
                              Clarification
                                    ▼
   ╔══════════════════════════════════════════════════════════════════╗
   ║  鏡門 Kyōmon · Mirror Gate                                        ║
   ║  (鏡 = mirror — reflects truth, never distorts. 八咫鏡)            ║
   ║                                                                  ║
   ║  "Did I see what I think I saw, or a trick of the light?"        ║
   ║                                                                  ║
   ║  Comparative claim made?                                         ║
   ║    ├─ Bidirectional grep verification                            ║
   ║    ├─ [鏡門 ✓] evidence tag required                              ║
   ║    ├─ 🛑 falsified → fix & re-verify                             ║
   ║    └─ ✅ verified → pass through                                 ║
   ║                                                                  ║
   ║  Operated by: Hermes (premise verification)                      ║
   ╚══════════════════════════════════════════════════════════════════╝
                                    ▼
                            Verified Premises
                                    ▼
   ╔═════════════════════════════════════════════════════════════════╗
   ║  證門 Shōmon · QUINTE Gate                                       ║
   ║  (證 = testimony, evidence — witnesses speak, truth emerges)    ║
   ║                                                                 ║
   ║  Structured multi-agent debate                                  ║
   ║                                                                 ║
   ║  R1 · 4 agents analyze independently (hm+cc+cw+omp)             ║
   ║  R2 · 5 agents cross-review (+rx) — never skipped               ║
   ║  R3 · Hermes synthesizes verdict · ⚠️ advisory 鏡門 (drift)     ║
   ║                                                                 ║
   ║  R2 finds fatal flaw? → restart R1 (once)                       ║
   ║  Consensus can hide shared blind spots · R2 is the only check   ║
   ║                                                                 ║
   ║  Operated by: Hermes + 5 agents (R1–R3)                         ║
   ╚═════════════════════════════════════════════════════════════════╝
                                    ▼
                              Verification
                                    ▼
   ╔═════════════════════════════════════════════════════════════════╗
   ║  閂門 Kan'nukimon · Anti-Drift Gate                              ║
   ║  (閂 = bolt, latch — no witness collusion)                       ║
   ║                                                                 ║
   ║  "No witness collusion" — each prompt must be independent       ║
   ║                                                                 ║
   ║  Every prompt to external agents must use three-layer defense:   ║
   ║    ① Task-first (task before context, not after)                ║
   ║    ② ONLY Y, not NOT X — positive framing prevents collision    ║
   ║    ③ TASK: restatement required — drift caught in first line    ║
   ║                                                                 ║
   ║  Drift detected? → kill & retry with shrunk prompt              ║
   ║  Operated by: Hermes (prompt construction)                      ║
   ╚═════════════════════════════════════════════════════════════════╝
                                    ▼
                                  Output
```

## Structure

| File | Content |
|------|---------|
| [GATES.md](GATES.md) | The Four Gates — 雨門·鏡門·證門·閂門 |
| [CONCEPTS.md](CONCEPTS.md) | Core concepts — Rashomon Depth, YNI, Kurosawa Check, Kyōmon IR |
| [PHENOMENOLOGY.md](PHENOMENOLOGY.md) | Phenomenological expansion (forthcoming) |

## Trilogy

RASHOMON is part of a three-repo framework for reliable AI agents:

| Repo | Role | Question |
|------|------|----------|
| [RASHOMON](https://github.com/eric-stone-plus/RASHOMON) | Design philosophy | *Why* multi-perspective truth-seeking? |
| [QUINTE](https://github.com/eric-stone-plus/QUINTE) | Debate protocol | *How* to orchestrate cross-examination? |
| [KENGEN](https://github.com/eric-stone-plus/KENGEN) | Authorization perimeter | *May I* execute this operation? |

RASHOMON and QUINTE form the epistemology→methodology axis. KENGEN is orthogonal — a safety rail that gates whether conclusions may become external actions, regardless of how they were reached. Each is necessary; none is sufficient alone.

## Cultural Anchors

- **芥川龍之介**《藪の中》（1922）— seven testimonies, one death, no resolution
- **黒澤明**《羅生門》（1950）— Venice Golden Lion, Academy Award for Best Foreign Language Film
- **Rashomon Effect** — entered English academic vocabulary: contradictory interpretations of the same event by different observers

## License

MIT
