# Ancient-Chinese-AI-progress-bar
本进度条旨在记录古文AI发展进度和未来发展趋势，并对古文AI应用在纯智性思维层面进行深入剖析。

目前尚未完稿，将不断更新。如果您有好的想法，欢迎提出issue。
# 0.说明
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本进度条作为设想和记录，对纯智性思维层面的古文AI应用进行分析。至于悟性思维部分，因为目前尚未完全证明纯智性思维的AI可以通过悟性思维文本产生对应思维。通俗的来说就是AI作诗没有意境。并且对应的机制尚未完全探明。在本研究中，我们将不做古文与文言文的区分，视之为同一种语言体系。
</font>
# 1.需求分析
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    随着现代科技的迅猛发展及普及，文言文为核心的学术领域正在充满活力地发展。不仅云端数据库日臻完善，本地文献的检索系统也逐渐成熟，为研究者开辟了全新的研究视野及工作模式。因此，人工智能的引入将为研究者提供更多便利，满足他们的多元需求。以下将对此话题进行深入的分析和总结。
</font>

## 1.1识文断句
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;古文虽然已经不再被广泛使用，然而它依旧存在各类文献之中。因此，如何识别这些古老的文字，成为人工智能需要首先攻克的挑战。并且，古代汉语和现代汉语都是孤立语，语序和虚词的使用是表达意义的关键。因此，标明语序，以及进行断句的标点符号，显得尤为重要。
</font>
### 1.1.1古文OCR
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;光学字符识别(OCR)技术历史悠久，在古文研究领域存在相当大的需求。无论是刻本还是抄本，都需要识别为文字，然后加入检索系统。然而，对于石刻材料的识别需求相对较小，其原因主要有二：一是数量较少，二是研究者往往能自行完成录入工作。<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;许多研究者在无法获得成品数据库或者成品数据库缺乏所需内容的情况下，不得不选择自行运用OCR以满足研究需求。
</font>
### 1.1.2古文断句
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    断句可视为理解古文的基础，但实际需求并不多。因大多数文本的使用者都能自行断句，无需机器辅助。即便是辅助断句，也常因某些专有名词而产生错误，带来二次修改的麻烦。然而，对于机器学习的语料来说，未断句，无标点的文本，基本不能作为数据集使用。即使是单纯的生成模型可能可以接受，但生成的仍会是混乱的文字。对于对话模型，无标点可能会导致训练效果不佳。
</font>

## 1.2说文解字
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    此处我们并不打算区分文字与词汇，因古文主要为单音节字词。有时我们需要查找某个文字的意思，便会下意识查阅词典。但有时仅靠词头可能无法充分利用整本词典，因此需要进行全文搜索。但是，如果有一种机器能理解文意，知道某个字在某个句子的具体意思，那么许多基础问题将被直接解决。如果还能提供对应例证，将事半功倍。特别是在训诂时，我们需要寻找类似的用法，AI的全文理解能力就可以发挥其作用，比起简单全文搜索更为精确。
</font>
## 1.3音形义结合分析
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们知道，语言是音义结合的符号系统，文字是承载语言的工具。因此音形义这三者基本上连接在一起。但如果仅靠人脑记忆，从古至今的音变，形变，义变进行分析，恐怕需要花费大量时间。我们也可以借助多模态模型，将其串联，变成可以问答的资料库。
。</font>
# 2.可能的实现方法
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  结合上文，本文将从AI技术的三个主要方面探讨需求的实现可能性。
</font>
## 2.1CV方面
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CV，是计算机视觉的简称。在古文AI领域主要是OCR。</font>
### 2.1.1基础数据
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;图文对应的数据，并且有</font>
### 2.1.2硬件需求
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>
### 2.1.3目前困境
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    多模态模型能够处理和理解多种类型的输入数据，例如文本、音频、图像等。在古文AI领域，这种模型可以结合文字的音义形等特点，进行更深层次的分析。
</font>
## 2.2NLP/NLU方面
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NLP（Natural Language Processing）指的是使用计算机技术处理和分析人类语言的领域。它涵盖了一系列技术和方法，旨在使计算机能够理解、处理和生成人类语言。NLP的目标是建立能够与人类自然语言进行交互的智能系统，使计算机能够理解文本、语音和对话，并从中提取有意义的信息。<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NLU（Natural Language Understanding）是NLP的一个子领域，专注于理解和解释人类语言的含义。NLU的目标是使计算机能够更深入地理解文本或对话的含义和上下文，并从中获取更高层次的语义信息。</font>
### 2.2.1基础数据
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;不同模型对数据集的格式等要求不同，但大都要求utf-8编码且通常字体包含的字符。这里以ChatGLM和RWKV的格式为例进行说明。</font>
#### 2.2.1.1 ChatGLM
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ChatGLM是对话模型，其微调的数据集为对话体，也就是类似论语的格式。以下是笔者微调中使用的格式之一https://huggingface.co/datasets/TMZN/lunyu 
```json
[
  {
    "instruction": "问题：曰:贫而无谄富而无骄何如?",
    "input": "",
    "output": "可也、未若贫而乐富而好礼者也、"
  },

  {
    "instruction": "问题：曰:夫子至于是邦也必闻其政求之与?抑与之与?",
    "input": "",
    "output": "夫子温、良、恭、俭、让以得之、夫子之求之也其诸异乎人之求之与?"
  },

  {
    "instruction": "问题：何谓四恶?",
    "input": "",
    "output": "不教而杀谓之虐;不戒视成谓之暴;慢令致期谓之贼;犹之与人也出纳之吝谓之有司、"
  },

  {
    "instruction": "问题：吾以女为死矣",
	"input": "",
    "output": "子在回何敢死?"
  }
 ]
```
```json
//这个格式有点迷惑，在《论语》是可以进行下去的，但是换成其他数据源不行。
{"prompt": "问题：曰:贫而无谄富而无骄何如?\n" ,"completion": "可也、未若贫而乐富而好礼者也、"}
{"prompt": "问题：曰:夫子至于是邦也必闻其政求之与?抑与之与?\n" ,"completion": "夫子温、良、恭、俭、让以得之、夫子之求之也其诸异乎人之求之与?"}
{"prompt": "问题：何谓四恶?\n" ,"completion": "不教而杀谓之虐;不戒视成谓之暴;慢令致期谓之贼;犹之与人也出纳之吝谓之有司、"}
{"prompt": "问题：吾以女为死矣\n" ,"completion": "子在回何敢死?"}
{"prompt": "问题：仁?\n" ,"completion": "仁者先难而后获可谓仁矣、"}
{"prompt": "问题：乡人皆好之何如?\n" ,"completion": "未可也、"}
{"prompt": "问题：问政\n" ,"completion": "先有司赦小过举贤才、"}
{"prompt": "问题：夫子为卫君乎?\n" ,"completion": "诺、吾将问之、"}
{"prompt": "问题：奚自?\n" ,"completion": "自孔氏、是知其不可而为之者与?"}
{"prompt": "问题：令尹子文三仕为令尹无喜色;三已之无愠色、旧令尹之政必以告新令尹、何如?\n" ,"completion": "忠矣、"}
{"prompt": "问题：如有博施于民而能济众何如?可谓仁乎?\n" ,"completion": "何事于仁必也圣乎!尧舜其犹病诸!夫仁者己欲立而立人己欲达而达人、能近取譬可谓仁之方也已、"}
{"prompt": "问题：子行三军则谁与?\n" ,"completion": "暴虎冯河死而无悔者吾不与也、必也临事而惧好谋而成者也、"}
{"prompt": "问题：乡人皆恶之何如?\n" ,"completion": "未可也、不如乡人之善者好之其不善者恶之、"}
{"prompt": "问题：为圃?\n" ,"completion": "吾不如老圃、"}
```
</font>

#### 2.2.1.2 RWKV
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RWKV有多种格式可供选择，貌似不同格式差距不是特别大。参考https://zhuanlan.zhihu.com/p/629809101 中的描述，格式如下。
```json
// 基于Pile基础模型，jsonl格式建议如下

{"text": "Instruction：基于专业背景的知识问题\n\nInput：专业领域的资料背景知识内容\n\nResponse：基于上述的专业回答"}
{"text": "\nInstruction：基于专业背景的知识问题\n\nInput：专业领域的资料背景知识内容\n\nResponse：基于上述的专业回答\n"}
{"text": "\n\nInstruction：基于专业背景的知识问题\n\nInput：专业领域的资料背景知识内容\n\nResponse：基于上述的专业回答\n\n"}
{"text": "\n\nInstruction：基于专业背景的知识问题\n\nInput：专业领域的资料背景知识内容\n\nResponse：基于上述的专业回答\n基于上述的专业回答\n\n"}

// Instruction 是指示，Input 是需要操作的数据，Response是答案

{"text": "Instruction：基于专业背景的知识问题\n\nContext：专业领域的资料背景知识内容\n\nResponse：基于上述的专业回答"}
{"text": "\nInstruction：基于专业背景的知识问题\n\nContext：专业领域的资料背景知识内容\n\nResponse：基于上述的专业回答\n"}
{"text": "\n\nInstruction：基于专业背景的知识问题\n\nContext：专业领域的资料背景知识内容\n\nResponse：基于上述的专业回答\n\n"}
{"text": "\n\nInstruction：基于专业背景的知识问题\n\nContext：专业领域的资料背景知识内容\n\nResponse：基于上述的专业回答\n基于上述的专业回答\n\n"}

// 基于Raven对话模型，jsonl格式建议如下（Instruction - Response的格式也可以）

// Bob是指用户提问方，Alice是指机器人回答方

{"text": "Bob: 提问\n\nAlice: 回答"}
{"text": "\nBob: 提问\n\nAlice: 回答\n"}
{"text": "\n\nBob: 提问\n\nAlice: 回答\n\n"}
{"text": "\n\nBob: 提问\n\nAlice: 回答\n回答\n\n"}

// 如果是FAQ问答式可以试试以下的jsonl格式

{"text": "Q: 问题\n\nA: 答案"}
{"text": "\nQ: 问题\n\nA: 答案\n"}
{"text": "\n\nQ: 问题\n\nA: 答案\n\n"}
{"text": "\nQ: 问题\n\nA: 答案\n答案\n"}
```

<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这里也给出对应《论语》的格式。</font>
```json
{"text":  "Bob: 曰: 贫而无谄富而无骄何如?\n\nAlice:  可也、未若贫而乐富而好礼者也、"}
{"text":  "Bob: 曰: 夫子至于是邦也必闻其政求之与?抑与之与?\n\nAlice:  夫子温、良、恭、俭、让以得之、夫子之求之也其诸异乎人之求之与?"}
{"text":  "Bob: 何谓四恶?\n\nAlice:  不教而杀谓之虐;不戒视成谓之暴;慢令致期谓之贼;犹之与人也出纳之吝谓之有司、"}
{"text":  "Bob: 吾以女为死矣\n\nAlice:  子在回何敢死?"}
{"text":  "Bob: 仁?\n\nAlice:  仁者先难而后获可谓仁矣、"}
{"text":  "Bob: 乡人皆好之何如?\n\nAlice:  未可也、"}
{"text":  "Bob: 问政\n\nAlice:  先有司赦小过举贤才、"}
{"text":  "Bob: 夫子为卫君乎?\n\nAlice:  诺、吾将问之、"}
{"text":  "Bob: 奚自?\n\nAlice:  自孔氏、是知其不可而为之者与?"}
{"text":  "Bob: 令尹子文三仕为令尹无喜色;三已之无愠色、旧令尹之政必以告新令尹、何如?\n\nAlice:  忠矣、"}
{"text":  "Bob: 如有博施于民而能济众何如?可谓仁乎?\n\nAlice:  何事于仁必也圣乎!尧舜其犹病诸!夫仁者己欲立而立人己欲达而达人、能近取譬可谓仁之方也已、"}
{"text":  "Bob: 子行三军则谁与?\n\nAlice:  暴虎冯河死而无悔者吾不与也、必也临事而惧好谋而成者也、"}
{"text":  "Bob: 乡人皆恶之何如?\n\nAlice:  未可也、不如乡人之善者好之其不善者恶之、"}
{"text":  "Bob: 为圃?\n\nAlice:  吾不如老圃、"}
{"text":  "Bob: 庶矣哉!\n\nAlice:  既庶矣、又何加焉?"}
{"text":  "Bob: 何谓孝?\n\nAlice:  无违、"}
```
</font>

<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;关于微调其他模型或者重新训练基础模型，数据格式的差异不大，具体的选择应根据具体情况进行。然而，值得强调的是，如果没有先进的OCR和标点技术，我们现在所拥有的数据集将无法存在。</font>
### 2.2.2硬件需求
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;语言模型在硬件平台上的运行可以被分为两个部分：训练和推理。接下来，我们将以ChatGLM和RWKV为例，简要介绍相关的硬件需求。</font>
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;首先，预训练阶段（从零开始）通常会消耗最大量的硬件资源。基本的硬件需求通常从100张A100 80G SXM5开始，而上限则没有明确的限制（目前的平台价格大致在五百万到一千万人民币左右，这还不包括配套设施的费用）。至少也需要64张相同的显卡（据传RWKV在初期阶段就有这样的需求），如果低于这个标准，那么运行预训练可能就没有太大的意义。<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;接下来是微调阶段的硬件需求，这个阶段的需求相比预训练阶段会显著降低，但也与基础模型直接相关。例如，ChatGLM-6B可以使用2080TI-22G显卡和lora方法轻松完成微调。而对于RWKV-7B来说，可能需要A6000-48G或者1-2张A100-80G显卡来完成微调。当然，这也与微调的方式有关，但在此我们不做详细的阐述。<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 最后，推理阶段的硬件需求可以进一步降低。在模型正常运行的情况下，可以进行量化操作，例如使用int8或int4等，这样可以极大地降低硬件需求。但是，为了保持模型的正常运行能力，我们请大家不要过度量化。</font>
### 2.2.3目前困境
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;虽然，LLM（大型语言模型）如雨后春笋，但是目前依旧存在如下困境。</font>
#### 2.2.3.1 语料不足
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    相比于现代汉语的广泛存在的数据集，古代汉语的数据集数量极少，质量也良莠不齐。没有好的数据，就算有优秀的模型也无法实现其潜力。
</font>

#### 2.2.3.2 知识割裂
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    根据目前的观察，大部分AI从业者可能只具备最基础的文言文能力，也就是到达民国水平。由于缺乏相关的知识储备，他们无法进行某些专业的判断。当前，我们迫切需要能够跨界，跨学科甚至超学科的人才，来解决文言文与AI结合的问题。
</font>

#### 2.2.3.3 算力稀缺
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;文科的科研经费一向较少，但AI却是最耗资的领域之一。虽然模型的运行可能成本不高，但一旦需要根据自身需求调整模型，产生的计算需求可能无法得到满足。</font>
## 2.3VITS方面
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>
### 2.3.1基础数据
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>
### 2.3.2硬件需求
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>
### 2.3.3目前困境
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>
# 3.结语
<font face="思源宋体" size=4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    古文AI的发展需要综合运用计算机视觉、自然语言处理和多模态模型等技术。通过构建高质量的数据集，提升模型的处理能力，以及优化硬件资源的使用，可以推动古文AI领域的进步。然而，目前仍存在数据稀缺、模型复杂、资源需求高等问题，需要更多的研究和尝试来解决。同时，跨学科的合作也是必要的，通过结合专业的古文知识和先进的AI技术，可以开拓更多的研究领域和应用场景。</font>
