# 2026 Evidence Notes

> Calibration snapshot: 2026-08-28

本页保存 README / `progress.yaml` 背后的主要证据。它不是完整文献综述，而是为了让仓库中的等级可以追溯。

## 1. EvaHan：任务本身已经形成连续时间轴

项目：<https://github.com/GoThereGit/EvaHan>

EvaHan 的历年任务提供了一条非常有用的能力演进线：

| 年份 | 任务 |
|---|---|
| 2022 | 古代汉语分词与词性标注 |
| 2023 | 古代汉语机器翻译 |
| 2024 | 古代汉语断句与标点 |
| 2025 | 古代汉语命名实体识别 |
| 2026 | 面向古籍的多模态 OCR |

2026 任务又把 OCR 拆成：

- Task A：刻本文字识别；
- Task B：版面元素分析（text / image / book_edge / seal）；
- Task C：手写文字识别。

主指标包括 CER、F1、NED、mAP 和 IoU。官方仓库给出的 baseline 路线已经使用 Qwen2.5-VL-7B-Instruct、Xunzi_Qwen2_VL_7B_Instruct、LoRA 与 vLLM。

**对本仓库的意义：** OCR 已经从“传统 OCR 小模块”升级为多模态模型参与的完整研究方向，但共享任务仍然专门评测刻本、版面和手写，说明不能把“古籍 OCR”标成成熟完结。

---

## 2. EvaHan 2024：断句比标点更成熟，而且 LLM 会改原文

论文：

- *Overview of EvaHan2024: The First International Evaluation on Ancient Chinese Sentence Segmentation and Punctuation*
- <https://aclanthology.org/2024.lt4hala-1.27/>

重要结果：

- 4 类未公开文本；
- 11 种标点；
- 6 支队伍、32 组结果；
- closed modality 最高 F1：
  - 断句 88.47%；
  - 标点 75.29%；
- unseen data 表现比常见公开数据低约 10%；
- 论文指出 LLM 会因 over-generation 改动约 1–2% 原字符，因此需要后处理保证原文一致性。

**对本仓库的意义：** 断句/标点非常适合做预处理和初稿，但还不应该自动替代整理者。特别是在文献工作流里，“不能改原字”往往比生成得像不像一句话更重要。

---

## 3. EvaHan 2025：NER 已可规模化预标注，但文体影响很明显

论文：

- *Overview of EvaHan2025: The First International Evaluation on Ancient Chinese Named Entity Recognition*
- <https://aclanthology.org/2025.alp-1.19/>

重要结果：

- 历史文本 + 医籍；
- 12 类命名实体；
- 13 支队伍、77 组结果；
- closed modality 最高 F1：
  - TestA（历史）：85.04%；
  - TestB（历史）：90.28%；
  - TestC（医籍）：84.49%。

论文明确指出 genre 与实体自身特征会显著影响结果。

**对本仓库的意义：** NER 已经适合承担大规模预标注，但“某个榜单 90%”不能直接外推到地方志、笔记、诗文集或其他实体体系。

---

## 4. ACLUE：古文理解已经可以被拆成可测任务

论文：

- *Can Large Language Model Comprehend Ancient Chinese? A Preliminary Test on ACLUE*
- <https://aclanthology.org/2023.alp-1.9/>

ACLUE 包含 15 个任务，覆盖：

- phonetic；
- lexical；
- syntactic；
- semantic；
- inference；
- knowledge。

论文 2023 年评测的 8 个模型中，最好平均准确率为 37.45%。这个数字已经很旧，**不应拿来代表 2026 模型水平**；它的价值在于建立了任务框架和公开 benchmark。

**对本仓库的意义：** “理解古文”不再只能靠聊天截图判断，可以继续拆分并量化；同时，不同子能力必须分别看。

---

## 5. CHisIEC：古代史信息抽取已经有像样的专门语料

论文：

- *CHisIEC: An Information Extraction Corpus for Ancient Chinese History*
- <https://aclanthology.org/2024.lrec-main.283/>

数据概况：

- 选取《二十四史》中 13 部史书；
- 时间跨度覆盖 13 个朝代、1830 余年；
- 14,194 个实体；
- 8,609 个关系；
- 4 类实体；
- 12 类关系；
- 用于 NER 与 relation extraction。

**对本仓库的意义：** “古文 AI 缺数据”仍然是问题，但已经不能笼统写成“几乎没有数据集”；至少在历史信息抽取等子领域，已经出现了可重复评测的专业资源。

---

## 6. MCS-Bench：多模态古典学仍有巨大缺口

论文：

- *MCS-Bench: A Comprehensive Benchmark for Evaluating Multimodal Large Language Models in Chinese Classical Studies*
- ACL 2025
- <https://aclanthology.org/2025.acl-long.515/>

范围：

- 7 个子领域：Ancient Chinese Text、Calligraphy、Painting、Oracle Bone Script、Seal、Cultural Relic、Illustration；
- 45 个细粒度任务；
- 评测 37 个多模态大模型；
- 论文报告最佳模型 InternVL2.5-78B 平均分仍低于 50。

**对本仓库的意义：** “看得见古籍图片”与“能做古典学判断”完全不是一回事。视觉文字识别、文化语境理解、书画/印章/甲骨等任务之间差距很大。

---

## 7. 古文专用模型已经从 BERT 走到 LLM

### GuwenBERT

<https://github.com/Ethan-yt/guwenbert>

- 基于大量古文语料继续训练 RoBERTa；
- 早期重点面向断句、标点、专名标注等序列标注任务；
- 项目报告其训练语料来自 15,694 本古文书籍、约 1.7B 字符；
- 在 2020 年古籍 NER 评测中形成过有影响力的专用基线。

### XunziALLM

<https://github.com/Xunzi-LLM-of-Chinese-classics/XunziALLM>

古籍领域模型已经扩展到 Qwen、ChatGLM、Baichuan 等多个基座，并继续出现 Qwen2 系列版本。

### WenyanGPT / WenyanBENCH

- IJCAI 2025：*WenyanGPT: A Large Language Model for Classical Chinese Tasks*
- <https://www.ijcai.org/proceedings/2025/927>

该工作基于 LLaMA3-8B-Chinese 做继续预训练与指令微调，同时发布 WenyanBENCH。

**对本仓库的意义：** 2023 版“要不要自己微调 ChatGLM / RWKV”的问题已经变成历史切片。2026 年更合理的问题是：

> 这个任务需要通用 LLM、领域 LLM、BERT 类编码器、RAG、OCR 模型，还是根本不需要生成模型？

---

## 8. 为什么没有给“AI 是否有意境”一个等级

OCR 可以看 CER，NER 可以看 F1，版面识别可以看 mAP / IoU。

“意境”“悟性”“诗味”属于不同层次的文学批评与审美判断。如果要研究模型生成诗歌，应该先把问题变成可描述的观察，例如：

- 格律满足率；
- 用韵；
- 典故使用与出处；
- 套语与重复；
- 时代词汇错置；
- 风格模仿稳定性；
- 人类读者盲评；
- 不同批评标准下的分歧。

仓库可以记录这些研究，但不会把“悟性 27%”与“OCR 3/5”画在同一个测量尺度上。

---

## 9. 下次校准时优先检查什么

1. EvaHan 2026 正式结果与各赛道最佳系统；
2. 新的古籍 OCR / historical document OCR benchmark；
3. WenyanBENCH、ACLUE 等在 2026 主流模型上的复测；
4. 古籍 RAG / 引文对齐是否出现公开、可重复 benchmark；
5. 古籍版本校勘、异文对齐是否出现专门共享任务；
6. MCS-Bench 后续版本及多模态模型提升幅度。

如果这些证据出现，再调整 `progress.yaml`，不要仅因为某个新模型发布就自动加一格。
