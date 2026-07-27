<div align="center">

# 🎩 黑客松路演魔术师
## Hackathon Roadshow Magician

**黑客松专属路演全链助手 · The All-in-One Roadshow Assistant for Hackathons**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](CHANGELOG.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

**把任意成果源代码一键转换为竞赛级路演材料**
*From source code to stage-ready pitch — in one conversation*

</div>

---

## 📖 项目简介 | Introduction

### 中文

黑客松路演魔术师是一个**对话式路演材料生成助手**。你丢给它一个成果项目（源代码/文档/链接），它会深度分析、核对信息、匹配路演类型、构建大纲、生成图表，最终产出**六维版本×19种产物**。整个过程7步交互，不浪费时间在排版和措辞上。

**核心痛点**：很多人不会写路演或写不好路演。DEMO做出来以后，要花很久去准备路演材料，浪费很多本该用于完善和搭建DEMO产品的时间。

### English

Hackathon Roadshow Magician is a **conversational pitch deck generator built for hackathons**. Hand it your project — source code, docs, or links — and it dives deep, cross-checks the details, picks the right pitch format, drafts the outline, builds the visuals, and ships **6-dimension variants × 19 ready-to-use deliverables**. Seven guided steps. Zero time lost on formatting or phrasing.

**Why it matters**: Most hackers can build, but struggle to pitch. After the demo works, hours vanish into slide-making — hours that should go back into the product. This tool gives that time back.

---

## ✨ 核心特性 | Key Features

| 特性 | Feature | 说明 | Description |
|------|---------|------|-------------|
| 🎯 **7步工作流** | 7-Step Workflow | 源码分析→核对→定类→大纲→图表→生成→交付 | Analyze → Verify → Classify → Outline → Visualize → Generate → Deliver |
| 🎪 **8类路演类型** | 8 Pitch Formats | 竞赛/投资/答辩/推广/电梯/展位/讲课/对接 | Demo Day / Investor / Defense / Launch / Elevator / Booth / Workshop / Partnering |
| 📊 **4类图表生成** | 4 Visual Types | Mermaid流程图/HTML架构图/Chart.js数据图/概念图 | Mermaid flowcharts / HTML architecture / Chart.js data viz / Concept maps |
| 🎨 **六维版本矩阵** | 6D Variant Matrix | 时长×侧重×风格×格式×语言×团队 | Length × Focus × Tone × Format × Language × Team |
| 📦 **19种产物** | 19 Deliverables | 赛前提报4+现场展示5+评委互动4+赛后传播4+存档复用2 | Pre-event 4 + Onstage 5 + Q&A 4 + Amplify 4 + Archive 2 |
| 🛡️ **三级工具链** | 3-Tier Toolchain | 主工具→备用(开源高赞)→降级方案 | Primary → Backup (open-source) → Fallback |
| 🔒 **完全本地运行** | Fully Local | 绝不联网、绝不外传 | Runs entirely on your machine — nothing leaves your device |

---

## 🚀 快速开始 | Quick Start

### 中文

1. **触发**：对AI助手说"黑客松路演"或"帮我做路演材料"
2. **丢入项目**：提供你的成果项目路径（源代码/文档/链接）
3. **7步交互**：按SOP流程确认信息、选择类型、审核大纲
4. **获取产物**：HTML路演页 + 演讲稿 + 问答 + 图表等

### English

1. **Kick it off**: Say "hackathon roadshow" or "help me build a pitch"
2. **Drop in your project**: Point it at your source code, docs, or links
3. **Walk through 7 steps**: Confirm the details, pick a format, review the outline
4. **Get your deck**: Interactive HTML page + speaker script + Q&A prep + charts

---

## 📐 架构图 | Architecture

```
┌─────────────────────────────────────────────────────┐
│  Layer 1 · 场景层 (Scenarios)                        │
│  8类路演全覆盖 (8 Pitch Formats)                     │
├─────────────────────────────────────────────────────┤
│  Layer 2 · SOP层 (Workflow)                          │
│  7步工作流 · 5个确认点 (7 Steps · 5 Checkpoints)     │
├─────────────────────────────────────────────────────┤
│  Layer 3 · 工具层 (Tools)                            │
│  三级工具链 · 补全降级 (3-Tier · Fallback)           │
├─────────────────────────────────────────────────────┤
│  Layer 4 · 产物层 (Deliverables)                     │
│  5环节 · 19种产物 (5 Stages · 19 Deliverables)       │
└─────────────────────────────────────────────────────┘
```

> 📁 完整交互式架构图见 [架构图.html](架构图.html)

---

## 📂 项目结构 | Project Structure

```
hackathon-roadshow-magician__skillhub/
├── SKILL.md                 # 主文件 (Skill Definition)
├── ref-roadshow-types.md    # 8类路演模板库 (Pitch Format Library)
├── ref-charts.md            # 图表模板与风格规范 (Visual Templates)
├── 架构图.html              # 交互式架构图 (Interactive Architecture)
├── CHANGELOG.md             # 版本记录 (Changelog)
├── LICENSE                  # MIT协议 (License)
├── .gitignore               # Git忽略规则
└── README.md                # 本文件 (This File)
```

---

## 🎪 8类路演类型 | 8 Roadshow Types

| 类型 | Format | 叙事框架 | Narrative Arc | 默认时长 |
|------|--------|----------|--------------|----------|
| 竞赛Demo | Demo Day | 问题→缘起→方案→Demo→技术→成绩→未来 | Problem → Origin → Solution → Demo → Tech → Results → Future | 15min |
| 投资路演 | Investor Pitch | 痛点→市场→产品→商业→团队→融资 | Pain → Market → Product → Business → Team → Ask | 10min |
| 技术答辩 | Tech Defense | 背景→方法→实现→验证→结论 | Background → Method → Implementation → Validation → Conclusion | 20min |
| 产品推广 | Product Launch | 场景→痛点→体验→优势→行动 | Scene → Pain → Experience → Edge → Action | 5min |
| 电梯演讲 | Elevator Pitch | 钩子→价值→差异→行动 | Hook → Value → Edge → Ask | 30s |
| 展位展示 | Booth Showcase | 亮点→Demo→互动→资源→连接 | Highlight → Demo → Engage → Assets → Connect | 3-5min |
| 技术讲课 | Workshop | 背景→概念→原理→实操→答疑 | Context → Concept → Theory → Hands-on → Q&A | 30-60min |
| 资源对接 | Partnering | 项目→价值→需求→资源→合作 | Project → Value → Needs → Resources → Partnership | 5-10min |

---

## 📦 19种产物 | 19 Deliverables

| 环节 | Stage | 产物 | Deliverables | 数量 |
|------|-------|------|--------------|------|
| 赛前提报 | Pre-event | 报名表/简介/一句话/声明 | Registration / Summary / Tagline / Declaration | 4 |
| 现场展示 | Onstage | HTML/PPT/腹稿/图表/操作清单 | HTML Deck / PPT / Speaker Notes / Charts / Demo Checklist | 5 |
| 评委互动 | Q&A | 预测问答/备忘录/技术FAQ/红线卡 | Predicted Q&A / Cheat Sheet / Tech FAQ / Red-line Card | 4 |
| 赛后传播 | Amplify | 海报/社媒文案/README/短视频脚本 | Poster / Social Copy / README / Video Script | 4 |
| 存档复用 | Archive | 项目档案/素材包 | Project Archive / Asset Bundle | 2 |

---

## 🛡️ 三级工具链 | 3-Tier Toolchain

| 环节 | 主工具 | 备用(开源高赞) | 降级方案 |
|------|--------|---------------|----------|
| 代码搜索 | SearchCodebase | ast-grep (15.2K⭐) | Grep+Glob |
| 图表生成 | Mermaid.js (89K⭐) | Chart.js (64K⭐) | HTML/CSS |
| 文件写入 | Write | SearchReplace | echo |
| 渲染测试 | RunCommand | Grep验证 | 人工检查 |

---

## 🔄 生态关系 | Ecosystem

```
Golden Idea (Idea Evaluator)  →  Roadshow Magician (Pitch Builder)  →  Qinshubao (Skill Inspector)
       Should you build it?         Build the pitch                    Is the pitch good enough?
            ↑ Three tools covering the full journey from spark to stage ↑
```

---

## 📋 版本规划 | Roadmap

| 版本 | 功能 | 状态 |
|------|------|------|
| v1.0.0 | 7步工作流 + 六维版本 + 19种产物 + 双语 | ✅ 当前 |
| v1.1.0 | PPT生成支持 | 🔄 规划中 |
| v1.2.0 | 协作模式（多人评审大纲） | 📋 规划中 |
| v1.3.0 | AI驱动个性化风格学习 | 📋 规划中 |

---

## 📄 许可证 | License

[MIT License](LICENSE) — Open source, community-friendly, build on top of it freely.

## 👤 作者 | Author

**喜气杨杨** (Xiqi Yangyang)

---

<div align="center">

**⭐ 如果这个项目帮到了你，欢迎Star支持！**
**Found it useful? Give it a Star — it helps others discover it too. ⭐**

</div>
