# 核心概念 — Core Concepts

QUINTE 从罗生门隐喻中提取的操作性概念。v3.0 新增：编排-监督分离、三机制认识论、跨模型对抗深度。

---

## 罗生门深度（Rashomon Depth）

**定义**: 不是 agent 数量，而是实际产生的独立视角数。

```
Rashomon Depth = |{ genuinely different reasoning paths }|
```

**判断标准**:
- 同模型换 prompt 参数 → Depth = 1（换面具，不是新证人）
- 不同模型、不同工具链、不同关注偏好 → Depth 增加
- R2 交叉审本身也贡献 Depth——换个角度看别人的分析

**v3.0 扩展**: 对抗性验证的跨模型要求（≥1 反驳 Agent 使用不同 provider）是 Rashomon Depth 的工程化实现。同模型共识 = 1 验证 × 3 噪声采样。跨模型共识 = 真正独立的验证路径。

**经验法则**: 如果四方 R1 输出惊人一致且无人说"不确定"，**这可能是共享盲区，不是共识**。罗生门里如果四个人说的完全一样，反而可疑。

---

## 编排-监督分离（Orchestration-Oversight Separation）

**v3.0 核心概念**: 执行辩论的实体不应是评判辩论质量的实体。

```
Claude Code (执行域)              Hermes (监督域)
──────────────────────            ──────────────────────
Workflow pipeline/parallel        逐 Phase 同步否决
Agent dispatch + JSON Schema      跨轮漂移检测
对抗性验证                        质量审计
loop-until-dry 收敛               ABORT 级联终止权
Bash 外部 Agent 调用              上下文注入 (memory → prompt)
```

**认识论理由**: v2.x 中 hm 既是 orchestrator 又是 participant，存在内在利益冲突——hm 会不自觉地按自己的判断裁剪编排（跳过"觉得不重要"的 Agent、凭记忆挑文件而非全枚举）。这不是意志力问题，是角色冲突的必然结果。

**分离原则**:
1. **执行者不能自我监督** — 编排引擎不能审计自己的编排质量
2. **监督者不能参与执行** — hm 的 xhigh reasoning 用于审计编排计划，不用于调度 Agent
3. **否决权必须在执行之前** — 同步 APPROVE/REJECT，非异步事后审计

---

## 三机制认识论（Three-Mechanism Epistemology）

**定义**: cc 的三种原生机制各自贡献不同类型的认识论保障。

| 机制 | 认识论贡献 | 防止的失败模式 |
|------|-----------|--------------|
| **Agent** (内置子Agent) | 独立上下文专项审查 | 单一上下文的信息过载和确认偏差 |
| **Workflow** (编排引擎) | pipeline/parallel 结构性保证 + JSON Schema 验证 | 人肉调度遗漏、输出格式歧义、假收敛 |
| **Bash** (外部Agent) | 跨系统/跨工具的多样化视角 | 单一工具链的共享盲区 |

**Agent 的认识论价值**: 每个内置 Agent 有独立上下文窗口——不会共享编排者的注意力偏差。清单生成 Agent 独立决定参与方，不经过 cc 的编排逻辑——这是"执行者不能决定谁参与"的认识论保障。

**Workflow 的认识论价值**: `pipeline()` 和 `parallel()` 不是性能优化——它们是纪律保证。pipeline 不可能跳过已加入的 item；agent({schema}) 不可能输出格式错误但被忽略的 claim。这些是人肉编排无法提供的机械性保障。

**Bash 的认识论价值**: hm 的 browser/desktop、cw 的深度搜索、rx 的纯推理、omp 的快速风控——这些是不同的认知工具，它们的"偏见"不会完全相关，因为它们的工具链和关注偏好不同。

---

## 藪の中指数（Yabu no Naka Index）

**定义**: R1 各方陈述的不一致度。取自芥川龙之介原著名《藪の中》（竹林中）。

```
YNI = 1 - (各方论点交集 / 各方论点并集)
```

**解读**:
- YNI ≈ 0：高度一致 → ⚠️ 可能共享盲区，R2 做确认性审计
- YNI ≈ 0.3–0.5：健康分歧 → R2 标注争议
- YNI > 0.7：高度分散 → 可能原问题本身模糊，退回雨門

**v3.0 修正**: YNI 的计算现在由 Phase 2 的自动 diff（JSON Schema 对齐后的 claims 对比）完成，非 hm 人眼估计。机械性的 diff 消除了 hm 标注分歧时可能的主观偏差。

---

## 黑泽明检查（Kurosawa Check）

**定义**: R2 强制交叉审 + 对抗性验证。QUINTE 的核心机制。

**隐喻**: 黑泽明拍《罗生门》不只是让四个人各说各的。真正的力量在于：**观众在对比供述的过程中，自己推演出接近真相的理解。** R2 就是这个"对比"环节——但 v3.0 加了对抗性反驳。

**v3.0 升级**: 
- v2.x: 交叉审 = 读别人的输出 + 标注争议
- v3.0: 交叉审 = 交叉审 + 对抗性验证（每争议 3 反驳 Agent，跨模型）+ 跨轮一致性审查

**规则**: R2 永不跳过。四方一致也可能是共享盲区。

---

## 镜門拦截率（Kyōmon Interception Rate）

```
Kyōmon IR = errors_caught / comparative_claims_made
```

v3.0 不变。衡量 hm 方向错误的发生频率和镜門的有效性。

---

## 术语表

| 术语 | 日语/English | 读音 | 含义 |
|------|-------------|------|------|
| Rashomon Depth | — | — | 独立视角数 |
| Orchestration-Oversight Separation | — | — | v3.0 核心架构原则：执行与监督分离 |
| Three-Mechanism Epistemology | — | — | Agent/Workflow/Bash 的差异化认识论贡献 |
| Cross-Model Adversarial Depth | — | — | 跨模型对抗性验证提供的独立视角 |
| Yabu no Naka Index | 藪の中 | やぶのなか | R1 分歧度 |
| Kurosawa Check | — | — | R2 强制交叉审 + 对抗性验证 |
| Kyōmon IR | — | — | 镜門拦截率 |
| Amamon | 雨門 | あまもん | Ambiguity gate |
| Kyōmon | 鏡門 | きょうもん | Mirror gate |
| Shōmon | 證門 | しょうもん | QUINTE gate |
| Kan'nukimon | 閂門 | かんぬきもん | Anti-Drift gate |

---

*CONCEPTS-v3.md — ratified 2026-06-09*
