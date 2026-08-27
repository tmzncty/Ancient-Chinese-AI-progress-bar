# START HERE / 从这里进兔子洞

这个仓库现在已经不只是一根 progress bar 了。

如果你第一次来，可以按你想找的东西走：

## 我只想知道：古文 AI 到底能干嘛？

→ [`README.md`](./README.md)

看 2026 能力矩阵：OCR、断句、NER、翻译、检索、校勘、多模态古典学分别走到哪一步。

→ [`progress.yaml`](./progress.yaml)

同一套判断的机器可读版本。

---

## 我不信，我想知道这些数字是谁说的

→ [`verification.yaml`](./verification.yaml)

逐来源记录：论文、代码、数据、权重到底能不能拿到，以及现在是作者报告、独立复现还是本站复现。

→ [`docs/verification-ledger.md`](./docs/verification-ledger.md)

人类可读解释：为什么“论文存在”“代码公开”“数据可下载”“结果可复现”是四件事。

→ [`docs/evidence-2026.md`](./docs/evidence-2026.md)

本轮能力校准的证据笔记。

---

## 我想看 AI 在哪里最容易翻车

→ [`docs/torture-tests.md`](./docs/torture-tests.md)

古文 AI 拷打场：同名异人、年代错配、假出处、版本异文、OCR 冲突、引文套娃……

→ [`lab/cases.yaml`](./lab/cases.yaml)

上面拷打题的机器可读版本，可以以后统一跑不同模型。

→ [`docs/field-notes.md`](./docs/field-notes.md)

不太适合塞进 leaderboard 的田野问题。

---

## 我喜欢那些“很土但真正有用”的东西

→ [`docs/boring-things-that-matter.md`](./docs/boring-things-that-matter.md)

stable ID、原图回链、版本号、diff、review queue、abstention……

一个核心观点：

> 每个字能回到扫描页，有时比模型会不会说漂亮文言重要得多。

---

## 我想继续挖坑

→ [`SIDE_QUESTS.md`](./SIDE_QUESTS.md)

实体链接、年代检索、引文核验、古籍 diff、Unicode 缺字、音韵体系、官职地名、文本复用、RAG、benchmark contamination、错误传播……

这里允许问题还没有答案。

---

## 我真的跑了实验，怎么记？

→ [`experiments/README.md`](./experiments/README.md)

→ [`experiments/run-template.yaml`](./experiments/run-template.yaml)

只有真正留下代码 commit、数据 revision、模型版本、命令、指标和原始输出 hash 的记录，才有资格把 `verification.yaml` 升成 **L4 / reproduced_here**。

失败、跑不通、数据申请不到，也欢迎记录。

---

## 我想看控制台

→ [`docs/index.html`](./docs/index.html)

静态控制室直接读取 `progress.yaml + verification.yaml`，同时显示：

- 能力等级；
- evidence audit 等级；
- 数据是 public / gated / partial；
- 具体 claim 是作者报告还是本站复现；
- 当前本站实际复现数量。

如果通过 GitHub Pages 发布 `docs/`，它可以直接作为项目页；在此之前也可以作为普通静态页面使用。

---

## 我想贡献

→ [`CONTRIBUTING.md`](./CONTRIBUTING.md)

原则越来越简单：

```text
不要告诉我“模型更懂古文了”。
告诉我：
它做什么任务，
在什么材料上，
证据在哪里，
失败在哪里，
这个结果是作者说的、别人复现的，还是你亲手跑的。
```

---

## 最后一个非正式导航

```text
想看结论      → README.md
想看机器数据  → progress.yaml
想查“谁说的”  → verification.yaml
想看证据      → docs/evidence-2026.md
想找茬        → docs/torture-tests.md
想批量找茬    → lab/cases.yaml
想看怪问题    → docs/field-notes.md
想看土工程    → docs/boring-things-that-matter.md
想继续挖坑    → SIDE_QUESTS.md
想真的复现    → experiments/
想看仪表盘    → docs/index.html
```

欢迎迷路。这个仓库现在本来就是一张地图。
