# 🌟 StarScope / 星探
🌍 **English users**: View the English version → [README_en.md](README_en.md)  
👉 This is the main (Chinese) README. The site itself is bilingual: [StarScope](https://github-stars.xjmunity.com//en/index.html)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Deployed on GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-89216B.svg)](https://github-stars.xjmunity.com/)

> **中文名**：星探  
> **English Name**：StarScope  
> 一份由开发者**人工精心挑选**的 GitHub 高增长项目推荐列表，每日更新，极简呈现。

🌐 **在线访问**：[星探](https://github-stars.xjmunity.com/)

---

## 📖 项目简介

在 GitHub 每日成千上万的项目中，真正值得关注的“新星”往往转瞬即逝。算法推荐可能错过小众但惊艳的项目，而人工筛选才能捕捉到那些**真正有趣、有潜力、有故事**的开源之作。

**StarScope**（星探）正是这样一个**人工精选项目发现平台**。  
由我（一名热爱发掘开源项目的开发者）每日亲自浏览、筛选、整理 GitHub 上**新增 star 数最多、增长最快、最具话题性**的项目，并以**极简、优雅、可归档**的方式呈现。

- 🔍 **人工精选**：拒绝算法，坚持人工阅读与判断。
- 📅 **每日更新**：每天一份“开源晚报”，不错过任何亮点。
- 🌐 **中英文双语**：内容双语呈现，界面自动跳转。
- 🗂️ **完整归档**：支持按日、按月回溯历史推荐。
- 🎨 **极简设计**：专注内容，无追踪、无干扰。

> 这不是一个数据聚合工具，而是一份**写给开发者的开源秘籍**。

---

## 🎯 核心特性

- ✅ **人工精选**：每一条数据都经过人工阅读、筛选与润色，确保质量与可读性。
- 🌐 **双语支持**：所有页面支持中文与英文，通过 `root_index.html` 自动跳转。
- 📅 **时间线归档**：提供完整的“历史归档”页面，支持按月浏览每日推荐。
- 🌙 **暗色模式**：支持暗色/亮色主题切换，偏好保存至本地。
- 🧱 **纯静态部署**：使用 GitHub Pages 部署，零服务器成本，极致轻量。
- 🔓 **完全开源**：所有代码、模板、数据均公开，欢迎贡献与复用。

---

## 🖼️ 截图预览

### 首页（今日推荐）
![首页截图](https://github.com/jungleAI404/github-stars/blob/main/static/images/zh/homepage.png)  

### 历史归档
![归档截图](https://github.com/jungleAI404/github-stars/blob/main/static/images/zh/Archive.png)  

### 关于页面
![关于截图](https://github.com/jungleAI404/github-stars/blob/main/static/images/zh/about.png)  


---

## 🛠️ 技术架构

本项目采用 **“人工输入 + 静态生成”** 的模式，技术栈简洁透明：

| 层级 | 技术 |
|------|------|
| **前端** | HTML5, CSS3, JavaScript (Vanilla) |
| **模板引擎** | [Jinja2](https://jinja.palletsprojects.com/)（Python） |
| **构建脚本** | `build.py`（Python） |
| **样式设计** | 原生 CSS + `:root` 变量 + 响应式布局 |
| **多语言支持** | JSON 翻译文件 + 模板变量注入 |
| **部署方式** | GitHub Pages（`gh-pages` 分支或 `docs/` 目录） |
| **SEO 优化** | `sitemap.xml`、`og:` 标签、`hreflang` 多语言支持 |

### 项目结构说明

```bash
star-scope/
├── build.py                 # 静态站点生成脚本（使用 Jinja2）
├── data/                    # 人工整理的每日项目数据
│   ├── en/                  # 英文版数据（JSON）
│   └── zh/                  # 中文版数据（JSON）
├── templates/               # HTML 模板（Jinja2）
├── static/                  # 静态资源（CSS, JS）
├── translations/            # 多语言文案翻译（site_name, nav, etc.）
├── output/                  # 构建输出目录（部署内容）
└── README.md
└── README_en.md
