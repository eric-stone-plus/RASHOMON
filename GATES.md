# 四道门 — The Four Gates

QUINTE 的四道强制门，按逻辑优先级排列。每道门对应罗生门叙事中的一个意象。

---

## 门 1：雨門 Amamon · Ambiguity Gate

**罗生门隐喻**: 樵夫在雨中走进罗生门——进入之前，先确认你到底要审什么。

**失败模式**: 问错问题（wrong question asked）

**触发**: 用户问题模糊不清——不确定意图、范围、具体指哪个。

**动作**: 必须先 `clarify` 反问确认，再行动。

**设计理由**: 与其花半小时跑完 QUINTE 发现理解错了，不如多问一句。

**SOUL.md 位置**: § Ambiguity gate（强制 — 最优先）

**命名**: 雨（あめ / ame）= rain。罗生门开场是大雨。雨門是入口——不清晰不进入。

---

## 门 2：鏡門 Kyōmon · Mirror Gate

**罗生门隐喻**: 樵夫检查自己的眼睛——"我看到的是真的吗，还是光影的错觉？" 镜不解释、不争辩、不偏袒——只反射真实。八咫鏡（Yata no Kagami）象征智慧与未装饰的真实。

**失败模式**: hm 理解错误（analyst comprehension error）——hm 在比较分析中做出方向性事实错误（声称 A 有 X，实际 B 有 X），基于记忆/印象而非逐行验证。

**触发**: hm 即将做出任何比较性声明时——"A 有 X，B 有 Y"、"local 比 repo 多了 Z"、"X 在 A 不在 B"。也包括非平凡事实断言（含模型内部知识）。

**动作**: 六条规则——

1. **双向验证**：对比较的每一侧独立验证。存在→`file:line`，缺失→search command+result。默认 grep，必要时用 read_file/diff。
2. **证据锚定**：存在声明附精确位置，缺失声明附搜索命令和结果。原则：可复现验证。
3. **方向显式**：`LOCAL → REPO` / `REPO → LOCAL` / `SYMMETRIC`。未标注方向 = violation。N-way 比较须分解为 pairwise。
4. **声明假设**：每次比较前显式声明基线假设（如"假设 local 更更新"），然后验证修正。
5. **三档处置**：✅ 确认→放行 / 🛑 证伪→硬阻断（修正后重过鏡門）/ ⚠️ 不确定→标注原因后放行。
6. **记忆声明**：非平凡事实断言若无可检索来源，须标注 `[memory/unsourced]`，视为 ⚠️ 档，除非声明是平凡的/公理的。

**机械后盾**: 每条比较声明须以 `[鏡門 ✓]` 开头并附验证证据。R3 终裁检查——无标签的比较声明视为未验证，可拒绝。

**R3 advisory pass**: 非阻断 ⚠️ 信号——仅当鏡門检测到终裁输出与原前提间漂移时触发，静默遥测。不影响 R3 自主性。

**度量**: 鏡門拦截率 = `errors_caught / comparative_claims_made`

**SOUL.md 位置**: § 鏡門 Kyōmon（强制）

**命名**: 鏡（かがみ / kagami）= mirror。镜不偏袒观者——直接对抗 hm 的"自利偏差"。

---

## 门 3：證門 Shōmon · QUINTE Gate

**罗生门隐喻**: 证人在城门内各自供述，交叉对质。真相不在任何一个供述里，在对比中浮现。

**失败模式**: 单一视角偏差（single-perspective bias）

**触发**: 任何可能被用户依赖的结论——push、配置修改、报告、skill 更新、协议变更、台账、报表、经济分析、合同解释等。

**动作**: 完整 R1+R2+R3（hm+cc+cw+omp → +rx 交叉审 → hm 终裁）。

**关键约束**:
- 不自判简化：Hermes 不自行判断"这个简单不需要 QUINTE"
- 可验证性：终裁必须列出各 agent 文件名和论点引用
- R2 不跳过：四方一致也可能是共享盲区
- rx 仅 R2：run 模式无工具调用，纯推理交叉裁判
- R3 裁决：≥3/5 确认，2/5 分歧，≤1/5 驳回

**SOUL.md 位置**: § QUINTE discipline（强制）

**命名**: 證（しょう / shō）= testimony, evidence。證門是证人对质的场所。

---

## 门 4：閂門 Kan'nukimon · Anti-Drift Gate

**罗生门隐喻**: 门闩——不许证人串供。每个人的供述必须独立，不受外部关联污染。

**失败模式**: prompt 污染/概念碰撞（prompt contamination / concept collision）

**触发**: 每次向 cc/cw/omp/reasonix 发送 prompt。

**动作**: 三层法——
1. **Task-first**: 具体任务放 prompt 最前面
2. **语义隔离**: "ONLY Y" 替代 "NOT X"，建立正向身份
3. **强制首行复述**: 要求 `TASK: [restatement]`，漂移在第一句即可检测

**设计理由**: LLM agent 看到 prompt 中的关键词可能激活训练数据中的错误概念关联（概念命名空间碰撞）。否定指令无效——模型需先激活被否定概念才能理解否定。

**SOUL.md 位置**: § Agent dispatch anti-drift（强制）

**命名**: 閂（かんぬき / kan'nuki）= bolt, latch。閂門是门闩——防止外部污染进入证词。

---

## 边界说明

本文件是**设计哲学**，非协议规范。四道门的可执行定义在 [spec/PROTOCOL.md](../spec/PROTOCOL.md)：
- Ambiguity gate 的触发条件见 SOUL.md § Ambiguity gate
- Mirror gate 的六条规则见 SOUL.md § 鏡門 Kyōmon
- QUINTE gate 的 R1+R2+R3 机制见 PROTOCOL.md §1-5
- Anti-Drift gate 的三层法见 PROTOCOL.md §7 Agent Dispatch Requirements

此处仅提供隐喻解释和命名来源。所有规范性约束（MUST/SHALL/SHOULD）以 PROTOCOL.md 为准。

---

## 执行流程

```
用户问题
  │
  ▼
雨門 ── 模糊？→ clarify 反问
  │ 清晰
  ▼
鏡門 ── 比较声明？→ 双向 grep + [鏡門 ✓]验证
  │ 🛑 证伪 → 修正 → 重回鏡門
  ▼ 通过
證門 ── 结论性输出？→ R1+R2+R3
  │            └── R3 advisory 鏡門 ⚠️（合成漂移检测）
  ▼
閂門 ── 分发 prompt？→ 三层法包装
  │
  ▼
输出
```

## 设计边界

- **紧急旁路**：高时效场景可显式 opt-in 合并雨門+鏡門为快速通道（须审计记录）
- **不可解歧义**：鏡門循环须有硬超时，超时后 escalate 人工
- **多模态**：非文本输入鏡門须模态感知或降级为 ⚠️ caution flag
- **元问题**：鏡門自身可靠性是残余风险——通过审计日志和离线评估缓解

---

*GATES-v2.md — ratified by QUINTE R1 consensus 2026-06-08 (hm+omp+cc+cw+rx, 5/5 Plan B)*
