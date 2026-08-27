# Ancient Chinese AI Field Lab

`docs/torture-tests.md` 负责解释“为什么要拷打”；这里负责把拷打题变成机器可读 case。

## 目标

不是造一个新的综合分数，而是积累**可重复失败模式**：

- 忠实转录 vs. 擅自改字；
- 断句存在多解时是否承认多解；
- 查不到出处时会不会编出处；
- 同名人物是否先检查年代；
- 不同版本是否被偷偷抹平；
- OCR、电子文本和图像冲突时以什么为依据；
- 模型能否在证据不足时停下来。

## `cases.yaml`

每个 case 都包含：

- `id`：稳定 ID；
- `category`：错误类型；
- `prompt`：给模型的任务；
- `evidence`：必要时提供材料；
- `oracle`：不是“标准作文”，而是**最低行为约束**；
- `failure_if`：出现哪些行为直接判失败；
- `scoring`：自动、半自动或人工。

很多文献学题没有唯一正确答案，所以我们更关心：

> 你可以答 A，也可以答 B；但你不能把“不确定”伪装成“唯一事实”。

## 不追求一个总分

一个模型可能：

- OCR 很强；
- 断句很好；
- 引文核验很差；
- 特别喜欢编版本；
- 但又很会主动 abstain。

把这些平均成 81.7 分会再次制造假精确。

因此 Field Lab 输出应该优先是**错误向量**：

```text
faithfulness       PASS
citation            FAIL
chronology          PASS
version-awareness   WARN
abstention          PASS
```

而不是：

```text
古文智商：87
```

## 运行器

本仓库暂时只提供 provider-neutral 数据和校验器，不把任何商业 API key 写进项目。

后续 runner 应把模型原始输出保存下来，并转换成 `experiments/runs/` 记录；否则结果仍然只是一张截图。
