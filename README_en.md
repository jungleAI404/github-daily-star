# 🌟 StarScope
![License](https://img.shields.io/badge/License-MIT-blue.svg)
[![Deployed on GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-89216B.svg)](https://github-stars.xjmunity.com/en/index.html)

**English Name**: StarScope  
**Chinese Name**: 星探 (Xīng Tàn)

A hand-curated list of trending GitHub projects, updated daily and presented in minimal style.

🌐 **Live Site**: [StarScope](https://github-stars.xjmunity.com/en/index.html)

---

## 📖 Project Overview

Among the thousands of new repositories on GitHub every day, truly remarkable "rising stars" often vanish unnoticed. Algorithm-driven recommendations may overlook niche yet brilliant projects — only human curation can capture those that are genuinely interesting, promising, and full of stories.

**StarScope** is exactly that: a human-powered discovery platform for exceptional open-source projects.

Curated daily by a developer passionate about uncovering hidden gems, each entry is personally reviewed, selected, and refined from the fastest-growing, most-starred, and most-talked-about new GitHub projects — then presented in a clean, elegant, and archivable format.

🔍 **Human-Curated**: No algorithms. Only thoughtful human judgment.  
📅 **Daily Updates**: One “open-source evening paper” every day — never miss a highlight.  
🌐 **Bilingual Support**: Content available in both Chinese and English; interface auto-redirects.  
🗂️ **Complete Archive**: Browse recommendations by day or month.  
🎨 **Minimalist Design**: Focus on content — no tracking, no distractions.  

This is not a data aggregator — it's a developer’s open-source playbook.

---

## 🎯 Core Features

✅ **Hand-Picked Curation**  
Every project is manually read, evaluated, and polished for quality and readability.

🌐 **Bilingual Interface**  
All pages support Chinese and English, with automatic language redirection via `root_index.html`.

📅 **Timeline Archive**  
Full historical archive organized by month, showing daily highlights at a glance.

🌙 **Dark Mode Support**  
Toggle between dark and light themes — your preference is saved locally.

🧱 **Fully Static Deployment**  
Hosted on GitHub Pages — zero server cost, ultra-lightweight.

🔓 **Open Source & Reusable**  
All code, templates, and data are publicly available. Contributions and forks welcome!

---

## 🖼️ Preview Screenshots

**Homepage (Today's Picks)**  
![Home Page Preview](https://github.com/jungleAI404/github-stars/blob/main/static/images/en/homepage.png)  

**Archive Page**  
![Archive Page Preview](https://github.com/jungleAI404/github-stars/blob/main/static/images/en/Archive.png)  


**About Page**  
![About Page Preview](https://github.com/jungleAI404/github-stars/blob/main/static/images/en/about.png)  


---

## 🛠️ Tech Stack

StarScope uses a **"human input + static generation"** workflow, with a clean and transparent tech stack:

| Layer             | Technology                                      |
|-------------------|-------------------------------------------------|
| Frontend          | HTML5, CSS3, Vanilla JavaScript                 |
| Template Engine   | Jinja2 (Python)                                 |
| Build Script      | `build.py` (Python)                             |
| Styling           | Native CSS + `:root` variables + responsive layout |
| Multilingual      | JSON translation files + template injection     |
| Deployment        | GitHub Pages (`gh-pages` branch or `/docs`)     |
| SEO Optimization  | `sitemap.xml`, `og:` meta tags, `hreflang`      |

---

## 🗂️ Project Structure
```bash
star-scope/
├── build.py # Static site generator (Jinja2)
├── data/ # Manually curated daily data
│ ├── en/ # English JSON data
│ └── zh/ # Chinese JSON data
├── templates/ # HTML templates (Jinja2)
├── static/ # Assets (CSS, JS)
├── translations/ # Site-wide text translations
├── output/ # Build output (for deployment)
└── README.md # This file (Chinese)
└── README_en.md # English version (this file)
```

---
## 🌍 How to View in Chinese  
To view the **Chinese version of this README**, please visit the repository directly on GitHub — this `README.md` is the default and primary file.  
👉 The Chinese `README.md` will always be the main landing file.  
🌐 You can also visit the live site: [https://github-stars.xjmunity.com](https://github-stars.xjmunity.com) — it supports **auto language detection and switching**.  

---
## 🤝 Contributions  
Welcome! Whether it's fixing typos, improving templates, or suggesting better curation workflows — all contributions are appreciated.  
Just open an issue or submit a pull request.

---
## 📄 License  
MIT License. See [LICENSE](LICENSE) for details.
