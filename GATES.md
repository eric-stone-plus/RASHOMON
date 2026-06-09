# 四道门 — The Four Gates (v3.0)

QUINTE v3.0 的四道强制门。**并行执行（~5s），hm 操作。證門是快速判断"是否需要 QUINTE"的闸门，通过后由 cc Workflow 执行完整 pipeline。**

v3.0 变更: 四门从串行改为并行。證門（原由 hm 手动调度 R1+R2+R3）现在拆分为两层：① 證門闸门 — hm 快速判断"结论性输出？→ 进入 cc pipeline"（~1s）；② 證門执行 — cc Workflow 完整 R1→R2→R3→loop-until-dry→KANSA pipeline，hm 每 Phase 同步否决。

---

## 门 1：雨門 Amamon · Ambiguity Gate

**罗生门隐喻**: 樵夫在雨中走进罗生门——进入之前，先确认你到底要审什么。

**失败模式**: 问错问题（wrong question asked）

**触发**: 用户问题模糊不清——不确定意图、范围、具体指哪个。

**动作**: 必须先 `clarify` 反问确认，再行动。

**设计理由**: 与其花半小时跑完 QUINTE 发现理解错了，不如多问一句。

**v3.0 操作者**: hm (xhigh reasoning)，在 Phase -1 并行执行

**命名**: 雨（あめ / ame）= rain。罗生门开场是大雨。雨門是入口——不清晰不进入。

---

## 门 2：鏡門 Kyōmon · Mirror Gate

**罗生门隐喻**: 樵夫检查自己的眼睛——"我看到的是真的吗，还是光影的错觉？" 镜不解释、不争辩、不偏袒——只反射真实。

**失败模式**: hm 理解错误（analyst comprehension error）——hm 在比较分析中做出方向性事实错误，基于记忆/印象而非逐行验证。

**触发**: hm 即将做出任何比较性声明时——"A 有 X，B 有 Y"、"local 比 repo 多了 Z"。

**动作**: 六条规则——
1. **双向验证**：对比较的每一侧独立验证。存在→`file:line`，缺失→search command+result。
2. **证据锚定**：存在声明附精确位置，缺失声明附搜索命令和结果。
3. **方向显式**：`LOCAL → REPO` / `REPO → LOCAL` / `SYMMETRIC`。
4. **声明假设**：每次比较前显式声明基线假设，然后验证修正。
5. **三档处置**：✅确认→放行 / 🛑证伪→硬阻断 / ⚠️不确定→标注后放行。
6. **记忆声明**：无可检索来源→`[memory/unsourced]`，⚠️档。

**机械后盾**: 每条比较声明须以 `[鏡門 ✓]` 开头并附验证证据。

**v3.0 操作者**: hm (xhigh reasoning)，在 Phase -1 并行执行

**命名**: 鏡（かがみ / kagami）= mirror。

---

## 门 3：證門 Shōmon · QUINTE Gate

**羅生門 metaphor**: Witnesses testify inside the gate. Truth emerges when one witness, reviewing *another's* account, spots what that witness could not see about themselves.

**v3.0 两层设计**:

```
證門 = 闸门层(hm, ~1s) + 执行层(cc Workflow, 30-180s)
```

### 闸门层（Phase -1，hm 并行执行）

**失败模式**: 不必要的 QUINTE（trivial query getting full debate）或遗漏 QUINTE（conclusion user may rely on but not debated）。

**触发**: 用户问题可能产生用户会依赖的结论时。
**动作**: 快速判断——结论性输出？→ 进入 cc pipeline。非结论性（如"这个文件在哪"）→ 跳过 QUINTE。
**不自行判断简化**: "这个简单不需要 QUINTE" = violation。简单任务藏着微妙错误是 QUINTE 的存在意义。

### 执行层（Phase 0-6，cc Workflow 执行，hm 同步否决）

cc Workflow pipeline:
```
Phase 0: Agent manifest 生成
Phase 1: R1 — parallel 四方独立分析
Phase 2: Auto-diff claims 共识/分歧
Phase 3: R2 — 跨模型对抗性验证
Phase 4: rx 裁判 + 跨轮一致性审查
Phase 5: loop-until-dry 收敛
Phase 6: KANSA 監査
───────────────────────
每 Phase: hm 同步否决 (APPROVE/REJECT/ABORT/MODIFY)
```

**v3.0 操作者**: hm（闸门判断）→ cc Workflow（执行引擎）+ hm（同步否决监督层）

**命名**: 證（しょう / shō）= testimony, evidence。證門是闸门+对质的完整机制。

---

## 门 4：閂門 Kan'nukimon · Anti-Drift Gate

**罗生门隐喻**: 门闩——不许证人串供。每个人的供述必须独立，不受外部关联污染。

**失败模式**: prompt 污染/概念碰撞（prompt contamination / concept collision）

**触发**: 每次向外部 agent（hm/cw/omp/rx）发送 prompt 时。

**动作**: 三层法——
1. **Task-first**: 具体任务放 prompt 最前面
2. **语义隔离**: "ONLY Y" 替代 "NOT X"，建立正向身份
3. **强制首行复述**: 要求 `TASK: [restatement]`，漂移在第一句即可检测

**v3.0 操作者**: hm（在 Phase -1 并行执行时审核 prompt 包装）+ cc（在 Workflow agent dispatch 时自动应用三层法）

**命名**: 閂（かんぬき / kan'nuki）= bolt, latch。

---

## 执行流程 (v3.0)

```
用户问题
  │
  ▼
┌─────────────────────────────────────────────────────────┐
│  四道门 — hm 并行执行 (~5s)                              │
│                                                         │
│  ┌──────┐ ┌──────┐ ┌──────────┐ ┌──────┐              │
│  │ 雨門 │ │ 鏡門 │ │ 證門(闸门)│ │ 閂門 │              │
│  │      │ │      │ │          │ │      │              │
│  │ambiguous│compar-│ │conclusion│ │prompt│              │
│  │?→     │ │ative  │ │user may  │ │污染?→ │              │
│  │clarify│ │claim? │ │rely on?  │ │3-layer│              │
│  │       │ │→verify│ │→pipeline │ │wrapper│              │
│  └──┬───┘ └──┬───┘ └────┬─────┘ └──┬───┘              │
│     └────────┴──────────┴──────────┘                    │
│               hm 上下文注入                               │
└──────────────────┬──────────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────────┐
│  cc Workflow — 證門执行层                                │
│                                                         │
│  Phase 0: Agent manifest → 必须参与方清单                 │
│  Phase 1: R1 parallel 四方 (cc/hm/cw/omp)               │
│  Phase 2: Auto-diff claims (共识/分歧池)                  │
│  Phase 3: R2 跨模型对抗性验证 (per-dispute 3 refuters)    │
│  Phase 4: rx 纯推理裁判 + 跨轮一致性 Agent                │
│  Phase 5: loop-until-dry (双critic + 双条件终止)          │
│  Phase 6: KANSA 監査 (毒化检测 + 越权标注)                │
│  ─────────────────────────────────────                  │
│  每 Phase 后: hm 同步否决 (APPROVE/REJECT/ABORT/MODIFY)  │
└──────────────────┬──────────────────────────────────────┘
                   ▼
              hm 终裁展示 + push gate
```

## 关键澄清

- **證門 ≠ cc Workflow pipeline。** 證門闸门（~1s 判断）和證門执行（pipeline）是两层。闸门决定"要不要进 pipeline"，执行层是 pipeline 本身。
- **四门都是 hm 在 Phase -1 并行执行的闸门检查**，每个 ~1-2s。它们不执行完整辩论，只做进入判断。
- **cc Workflow 是證門授权后的执行引擎**，不是證門本身。

---

*GATES-v3.1.md — clarified Shōmon gate vs. pipeline distinction + parallel execution, 2026-06-09*
