# RASHOMON

> 芥川龍之介《藪の中》（1922）→ 黒澤明《羅生門》（1950）→ AI agent truth-seeking

**RASHOMON** is the philosophical foundation of the QUINTE debate protocol. It asks the question QUINTE is built to answer: *when a single perspective cannot be trusted, how do we converge on actionable truth?*

## About

RASHOMON is the philosophical companion to [QUINTE](https://github.com/eric-stone-plus/QUINTE), a five-agent structured debate protocol. Where QUINTE specifies *how* to orchestrate multi-agent cross-examination, RASHOMON explores *why* this approach is necessary — grounding the protocol in Kurosawa's 1950 film *Rashomon* and the broader problem of single-perspective truth in AI systems.

## The Rashomon Problem

Kurosawa's *Rashomon* (1950) presents four witnesses to the same event offering mutually contradictory testimonies. Not because anyone is lying — but because each person sees only what their position allows them to see.

This is the exact problem facing single-agent AI systems. One model, one perspective, one blind spot. The answer isn't a better model — it's a *structure that forces perspectives to confront each other*.

## The Four Gates

QUINTE operates through four mandatory gates, each preventing a distinct failure mode:

```
                       User asks a question
                                 ▼
          ╔═══════════════════════════════════════════════╗
          ║  雨門 Amamon · Ambiguity Gate                  ║
          ║  (雨 = rain, the uncertainty before entering)  ║
          ║                                               ║
          ║  "What am I actually being asked?"            ║
          ║  Vague? → clarify() first.  Clear? → proceed. ║
          ║  Operated by: Hermes (pre-debate check)       ║
          ╚════════════════════════╤══════════════════════╝
                                   │
          ╔════════════════════════╧══════════════════════╗
          ║  鏡門 Kyōmon · Mirror Gate                     ║
          ║  (鏡 = mirror — reflects truth, never distorts)║
          ║                                               ║
          ║  "Did I see what I think I saw?"              ║
          ║  [鏡門✓] bidirectional grep · ✅ 🛑 ⚠️       ║
          ║  Operated by: Hermes (premise verification)   ║
          ╚════════════════════════╤══════════════════════╝
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             │
          ╔══════════════════╗          ╔═════════╧════════╗
          ║  證門 Shōmon      ║          ║  閂門 Kan'nukimon ║
          ║  (證 = testimony) ║          ║  (閂 = bolt)     ║
          ║                   ║          ║                  ║
          ║  R1 · 4 agents    ║          ║  "No witness     ║
          ║  R2 · 5 cross     ║          ║   collusion"     ║
          ║  R3 · verdict     ║          ║                  ║
          ║       ⚠️鏡門      ║─────────▶║  ① task-first   ║
          ║                   ║          ║  ② ONLY Y       ║
          ║  R2 never skipped ║          ║  ③ TASK: restate║
          ║  Fatal?→restart R1║          ║                  ║
          ║                   ║          ║  Drift?→kill+retry║
          ║  Operated by:     ║          ║  Operated by:    ║
          ║  Hermes+5 agents  ║          ║  Hermes (prompt) ║
          ╚═══════╤══════════╝          ╚═══════╤══════════╝
                  └─────────────┬─────────────────┘
                                ▼
                             Output
```

## Structure

| File | Content |
|------|---------|
| [GATES.md](GATES.md) | The Four Gates — 雨門·鏡門·證門·閂門 |
| [CONCEPTS.md](CONCEPTS.md) | Core concepts — Rashomon Depth, YNI, Kurosawa Check, Kyōmon IR |
| [PHENOMENOLOGY.md](PHENOMENOLOGY.md) | Phenomenological expansion (forthcoming) |

## Cultural Anchors

- **芥川龍之介**《藪の中》（1922）— seven testimonies, one death, no resolution
- **黒澤明**《羅生門》（1950）— Venice Golden Lion, Academy Award for Best Foreign Language Film
- **Rashomon Effect** — entered English academic vocabulary: contradictory interpretations of the same event by different observers

## License

MIT
