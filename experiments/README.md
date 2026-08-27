# Reproduction Lab

这个目录只收一种东西：**真的跑过的东西。**

论文摘要、作者 README、模型宣传页、聊天截图，都不能放进 `runs/` 冒充复现。

## 目录约定

```text
experiments/
├── README.md
├── run-template.yaml
└── runs/
    └── <date>-<project>-<short-name>.yaml
```

原始大输出不一定适合直接进 Git；可以记录 SHA256、外部 artifact、GitHub Actions artifact 或可重新生成的路径。但是**指标必须能追溯到原始输出**。

## 一个合格 run 最少需要什么

- `id`
- `date`
- `target_claim`
- `source_project`
- `runner`
- 代码仓库和 commit
- 数据集名称和 revision / hash
- 模型名称和 revision / hash
- 环境（Python、关键依赖、GPU/CPU）
- 完整命令或可执行脚本
- 随机种子
- 指标定义
- 论文报告值（如果是在复现论文）
- 本次实测值
- 原始输出位置或 hash
- 是否完整复现、部分复现、失败
- 已知偏差

## “跑通 demo”不算“复现论文”

例如：

```text
python demo.py
```

能够输出一句断句结果，只能证明软件在某个环境里能启动。

要复现“F1 = 88.47%”，至少需要同一测试集、同一标签定义、同一评分脚本，最好还有对应模型/提交版本。

所以 run 有三种类型：

- `smoke_test`：能不能启动；
- `partial_reproduction`：只复现论文的一部分；
- `claim_reproduction`：针对一个明确 claim 重新计算；
- `independent_test`：我们自己的 torture test / field test，不声称复现论文。

## 失败也是结果

欢迎这种记录：

```yaml
outcome: blocked
reason: dataset_requires_institutional_application
```

或者：

```yaml
outcome: mismatch
reported: 90.28
observed: 86.71
notes: "paper checkpoint unavailable; used repository default checkpoint"
```

这比“我没跑出来所以不写”更有价值。

## 升级到 verification L4

只有满足以下条件才允许把 `verification.yaml` 中某项标为 `reproduced_here`：

1. `experiments/runs/` 中有对应 run；
2. run 不是 `smoke_test`；
3. 指标有原始输出或 hash；
4. 代码、数据、模型版本可以定位；
5. `scripts/validate_experiments.py` 通过；
6. README/文档措辞写清楚复现范围，不把单一数据集外推成普遍能力。
