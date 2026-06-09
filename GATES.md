# 四道门 — The Four Gates (v3.0)

QUINTE v3.0 的四道强制门。**并行执行（~5s），hm 操作，cc Workflow 为證門的执行引擎。**

v3.0 变更: 四门从串行改为并行——四道门同时审同一输入从不同角度，而不是 user 等 20s 才进入辩论。證門（原由 hm 手动调度 R1+R2+R3）现由 cc Workflow pipeline/parallel 执行，hm 保留同步否决权。

---

## 门 1：雨門 Amamon · Ambiguity Gate

**罗生门隐喻**: 樵夫在雨中走进罗生门——进入之前，先确认你到底要审什么。

**失败模式**: 问错问题（wrong question asked）

**触发**: 用户问题模糊不清——不确定意图、范围、具体指哪个。

**动作**: 必须先 `clarify` 反问确认，再行动。

**v3.0 操作者**: hm (xhigh reasoning)

---

## 门 2：鏡門 Kyōmon · Mirror Gate

**罗生门隐喻**: 樵夫检查自己的眼睛——"我看到的是真的吗，还是光影的错觉？"

**失败模式**: hm 理解错误——hm 在比较分析中做出方向性事实错误，基于记忆/印象而非逐行验证。

**触发**: hm 即将做出任何比较性声明时。

**动作**: 六条规则——
1. **双向验证**：对比较的每一侧独立验证。存在→`file:line`，缺失→search command+result。
2. **证据锚定**：存在声明附精确位置，缺失声明附搜索命令和结果。可复现验证。
3. **方向显式**：`LOCAL → REPO` / `REPO → LOCAL` / `SYMMETRIC`。
4. **声明假设**：每次比较前显式声明基线假设，然后验证修正。
5. **三档处置**：✅确认→放行 / 🛑证伪→硬阻断 / ⚠️不确定→标注后放行。
6. **记忆声明**：无可检索来源→`[memory/unsourced]`，⚠️档。

**v3.0 操作者**: hm (xhigh reasoning)

---

## 门 3：證門 Shōmon · QUINTE Gate

**羅生門 metaphor**: Witnesses testify inside the gate. Truth emerges when one witness, reviewing *another's* account, spots what that witness could not see about themselves.

**v3.0 重大变更**: 證門不再由 hm 手动调度。cc Workflow 接管全部编排执行：

```
證門 = R1(cc parallel 四方) → diff → R2(对抗性验证 + rx) → loop-until-dry → KANSA
       ↑ hm 每 Phase 同步否决 (APPROVE/REJECT/ABORT/MODIFY)
```

hm 从 **證門的操作者** 变为 **證門的审计者**——审 cc 的编排计划是否遗漏、是否漂移、输出质量是否达标。

**v3.0 操作者**: cc Workflow（执行引擎） + hm（同步否决监督层）

---

## 门 4：閂門 Kan'nukimon · Anti-Drift Gate

**罗生门隐喻**: 门闩——不许证人串供。每个人的供述必须独立。

**失败模式**: prompt 污染/概念碰撞

**触发**: 每次向外部 agent（hm/cw/omp/rx）发送 prompt。

**动作**: 三层法——
1. **Task-first**: 具体任务放 prompt 最前面
2. **语义隔离**: "ONLY Y" 替代 "NOT X"
3. **强制首行复述**: 要求 `TASK: [restatement]`

**v3.0 操作者**: cc（在 Workflow agent dispatch 时自动应用三层法）+ hm（审核 prompt 包装质量）

---

## 执行流程 (v3.0)

```
用户问题
  │
  ▼
┌─────────────────────────────────────────┐
│  四道门 — hm 并行执行 (~5s)              │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │ 雨門 │ │ 鏡門 │ │ 證門 │ │ 閂門 │  │
│  └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘  │
│     └────────┴────────┴────────┘        │
│          hm 上下文注入                    │
└──────────────────┬──────────────────────┘
                   ▼
┌─────────────────────────────────────────┐
│  cc Workflow — 證門执行引擎              │
│  Phase 0: 清单生成 → Agent(registry)     │
│  Phase 1: R1 → parallel 四方            │
│  Phase 2: diff → claims 共识/分歧        │
│  Phase 3: R2 → 对抗性验证(跨模型)        │
│  Phase 4: rx 裁判 + 跨轮一致性           │
│  Phase 5: loop-until-dry (双条件)        │
│  Phase 6: KANSA 監査                    │
│  ───────────────────────────────        │
│  每 Phase: hm 同步否决                   │
└──────────────────┬──────────────────────┘
                   ▼
              hm 终裁展示 + push gate
```

## 设计边界

- **并行执行**: 四门同时审而非串行，~5s vs ~20s
- **紧急旁路**: 高时效场景可显式 opt-in 合并雨門+鏡門为快速通道
- **不可解歧义**: 鏡門循环硬超时，超时后 escalate 人工

---

*GATES-v3.md — updated for v3.0: cc orchestration + hm oversight + parallel gates, 2026-06-09*
