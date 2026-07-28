<div align="center">

# 🎩 黑客松路演魔术师
## Hackathon Roadshow Magician

**黑客松专属路演全链助手 · The All-in-One Roadshow Assistant for Hackathons**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.5.0-blue.svg)](CHANGELOG.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

**把任意成果源代码一键转换为竞赛级路演材料**
*From source code to stage-ready pitch — in one conversation*

---

![4+1视觉风格 · 四套风格对比预览](style-showcase.png)

**🎨 4+1视觉风格 | 📊 17种专业图表 | 🌍 中英双语 | 📦 19种产物**

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
| 🎨 **4+1视觉风格** | 4+1 Visual Styles | 暗色科技/工业/卡通/赛博朋克/自定义 | Dark Tech / Industrial / Cartoon / Cyberpunk / Custom |
| 📊 **17种专业图表** | 17 Chart Types | 流程图/架构图/UML/ER/关系图/3D/手绘等 | Flowcharts / Architecture / UML / ER / Graphs / 3D / Hand-drawn |
| 🌍 **中英双语** | Bilingual Ready | 中文为主、英文点缀，风格差异化排版 | CN-primary, EN-accent, style-matched typography |
| 🎭 **六维版本矩阵** | 6D Variant Matrix | 时长×侧重×风格×格式×语言×团队 | Length × Focus × Tone × Format × Language × Team |
| 📦 **19种产物** | 19 Deliverables | 赛前提报4+现场展示5+评委互动4+赛后传播4+存档复用2 | Pre-event 4 + Onstage 5 + Q&A 4 + Amplify 4 + Archive 2 |
| 🛡️ **三级工具链** | 3-Tier Toolchain | 主工具→备用(开源高赞)→降级方案 | Primary → Backup (open-source) → Fallback |
| 🔒 **完全本地运行** | Fully Local | 绝不联网、绝不外传 | Runs entirely on your machine — nothing leaves your device |

---

## 🎨 视觉风格预览 | Style Showcase

| 暗色科技风 | 工业风 | 卡通风 | 赛博朋克风 |
|:---:|:---:|:---:|:---:|
| Dark Tech | Industrial | Cartoon | Cyberpunk |
| #1A1A2E + #00D4FF | #2C2C2C + #FF6B35 | #FFF8E7 + #FF6B6B | #0D0D0D + #FF00FF/#00FFFF |
| 霓虹发光 · 科技感 | 硬朗线条 · 金属质感 | 圆润可爱 · 活泼有趣 | 霓虹渐变 · 故障艺术 |

---

## 🚀 快速开始 | Quick Start

### 中文

1. **触发**：对AI助手说"黑客松路演"或"帮我做路演材料"
2. **丢入项目**：提供你的成果项目路径（源代码/文档/链接）
3. **7步交互**：按SOP流程确认信息、选择类型、审核大纲、选择风格
4. **获取产物**：多风格HTML路演页 + 演讲稿 + 问答 + 图表 + 推广样品截图

### English

1. **Kick it off**: Say "hackathon roadshow" or "help me build a pitch"
2. **Drop in your project**: Point it at your source code, docs, or links
3. **Walk through 7 steps**: Confirm details, pick format & style, review outline
4. **Get your deck**: Multi-style HTML pages + speaker script + Q&A prep + charts + promo screenshots

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
│  三级工具链 · 17种图表 · 7种布局 · 专家降级           │
├─────────────────────────────────────────────────────┤
│  Layer 4 · 视觉层 (Visuals)                          │
│  4+1风格 · 中英双语 · 7种渲染风格                    │
├─────────────────────────────────────────────────────┤
│  Layer 5 · 产物层 (Deliverables)                     │
│  5环节 · 19种产物 · 推广样品自动生成                 │
└─────────────────────────────────────────────────────┘
```

---

## 📂 项目结构 | Project Structure

```
hackathon-roadshow-magician__skillhub/
├── SKILL.md                 # 主文件 (Skill Definition, v1.5.0)
├── ref-roadshow-types.md    # 8类路演模板库 (Pitch Format Library)
├── ref-charts.md            # 17种图表模板与风格规范
├── 架构图.html              # 交互式架构图 (Interactive Architecture)
├── style-showcase.png       # 四风格对比预览图 (Style Showcase)
├── social-preview.png       # GitHub社交预览图 (Social Preview)
├── 路演材料/                 # 路演产物 (Generated Pitch Materials)
│   ├── 推广样品/             # 各风格截图，用于宣传 (Promo Screenshots)
│   ├── 图表素材/             # 独立图表文件 (Chart Assets)
│   ├── 风格对比/             # 单风格预览页 (Style Demos)
│   └── *_5min_完整版.html    # 四套双语风格路演页
├── CHANGELOG.md             # 版本记录 (Changelog)
├── LICENSE                  # MIT协议 (License)
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
| 流程图/架构 | Mermaid.js (89K⭐) | flowchart.js / draw.io | HTML/CSS+箭头 |
| 数据图表 | Chart.js (64K⭐) | ECharts (61K⭐) | 纯CSS柱状图/进度条 |
| 关系图/依赖 | D3.js (110K⭐) | cytoscape.js (10K⭐) | HTML/CSS连线+卡片 |
| 交互动图 | ECharts (61K⭐) | Plotly.js / Leaflet | 静态SVG |
| 手绘风格 | Rough.js (20K⭐) | rough-notation | 波浪线CSS+手写字体 |
| 文件写入 | Write | Edit追加 | 分片Write拼合 |
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
| v1.0.0 | 7步工作流 + 六维版本 + 19种产物 | ✅ 已发布 |
| v1.4.0 | Ask/Plan模式 + 追问环节 + 数据铁律 + 经验库 | ✅ 已发布 |
| v1.5.0 | 4+1视觉风格 + 17种图表 + 中英双语 + 推广样品 | ✅ 当前 |
| v1.6.0 | PPT生成支持（MCP/HTML转PPT） | 🔄 规划中 |
| v1.7.0 | 协作模式（多人评审大纲） | 📋 规划中 |
| v1.8.0 | AI驱动个性化风格学习 | 📋 规划中 |

---

## 🎩 自举案例：魔术师的路演

这份README同目录下的路演材料，就是**用黑客松路演魔术师给它自己生成的**（四套风格双语版）：

- [🌑 暗色科技风 · 5min完整版](路演材料/黑客松路演魔术师_暗色科技风_5min_完整版.html) — 默认推荐，科技感十足
- [🟧 工业风 · 5min完整版](路演材料/黑客松路演魔术师_工业风_5min_完整版.html) — 硬朗金属质感
- [🎈 卡通风 · 5min完整版](路演材料/黑客松路演魔术师_卡通风_5min_完整版.html) — 活泼可爱
- [💜 赛博朋克风 · 5min完整版](路演材料/黑客松路演魔术师_赛博朋克风_5min_完整版.html) — 霓虹故障艺术
- [📊 风格合集对比预览](路演材料/风格合集_对比预览.html) — 四套风格同屏对比
- [📝 5分钟演讲稿](路演材料/黑客松路演魔术师_演讲稿_5min.md) — 口语化腹稿
- [❓ 预测问答5min版](路演材料/黑客松路演魔术师_问答_5min.md) — 评委互动准备

> **同一个项目，同一套代码，不同的表达。** 这不是魔法，是工程化。

---

## 🤝 参与贡献 | Contributing

欢迎提 Issue 和 PR！无论是 Bug 报告、功能建议还是文档改进，都欢迎。

Issues and PRs are welcome — bug reports, feature requests, and doc improvements are all appreciated.

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
