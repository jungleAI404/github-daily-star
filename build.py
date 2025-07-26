# /build.py (修正版 v4)

import os
import json
import shutil
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

# --- 配置 ---
LANGUAGES = ['en', 'zh']
DEFAULT_LANGUAGE = 'en'
BASE_URL = "https://jungleAI404.github.io/github-daily-star"  # 部署后请修改为你的域名

# --- 路径定义 ---
PATH_DATA = 'data'
PATH_TEMPLATES = 'templates'
PATH_TRANSLATIONS = 'translations'
PATH_STATIC = 'static'
PATH_OUTPUT = 'output'


class SiteBuilder:
    def __init__(self):
        self.data = self._load_data()
        self.translations = self._load_translations()
        self.env = Environment(
            loader=FileSystemLoader(PATH_TEMPLATES, encoding='utf-8-sig'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.env.filters['format_k'] = lambda num: f"{num / 1000:.1f}" if isinstance(num, int) and num > 1000 else num

    def _load_data(self):
        all_data = {}
        for lang in LANGUAGES:
            lang_path = os.path.join(PATH_DATA, lang)
            all_data[lang] = {}
            if os.path.exists(lang_path):
                for filename in sorted(os.listdir(lang_path)):
                    if filename.endswith('.json'):
                        date_str = filename.split('.')[0]
                        date_obj = datetime.strptime(date_str, '%Y%m%d').date()
                        with open(os.path.join(lang_path, filename), 'r', encoding='utf-8-sig') as f:
                            all_data[lang][date_obj] = json.load(f)
        return all_data

    def _load_translations(self):
        translations = {}
        for lang in LANGUAGES:
            trans_path = os.path.join(PATH_TRANSLATIONS, f'{lang}.json')
            if os.path.exists(trans_path):
                with open(trans_path, 'r', encoding='utf-8-sig') as f:
                    translations[lang] = json.load(f)
        return translations

    def _render_page(self, template_name, path, context):
        template = self.env.get_template(template_name)
        dir_name = os.path.dirname(path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(template.render(context))

    def build(self):
        if os.path.exists(PATH_OUTPUT):
            shutil.rmtree(PATH_OUTPUT)
        os.makedirs(PATH_OUTPUT)

        shutil.copytree(PATH_STATIC, PATH_OUTPUT, dirs_exist_ok=True)

        all_urls = {}

        for lang in LANGUAGES:
            print(f"Building pages for language: {lang}...")

            lang_data = self.data.get(lang, {})
            if not lang_data:
                continue

            sorted_dates = sorted(lang_data.keys(), reverse=True)

            def translator(key):
                return self.translations.get(lang, {}).get(key, key)

            self.env.globals['T'] = translator

            date_format = "%B %d, %Y" if lang == 'en' else "%Y年 %m月 %d日"
            og_locale = "en_US" if lang == 'en' else "zh_CN"

            common_context = {
                "lang": lang,
                "og_locale": og_locale,
                "current_year": datetime.now().year,
                "base_url": BASE_URL,
                "date_format": date_format
            }

            latest_date = sorted_dates[0]
            prev_date_home = sorted_dates[1] if len(sorted_dates) > 1 else None
            home_path = f'/{lang}/index.html'
            self._render_page('index.html', os.path.join(PATH_OUTPUT, lang, 'index.html'), {
                **common_context,
                "title": f"{translator('site_name')} - {latest_date.strftime(date_format)}",
                "description": translator('hero_subtitle'),
                "nav_active": "home",
                "date": latest_date,
                "projects": lang_data[latest_date],
                "prev_date": prev_date_home,
                "canonical_path": home_path,
                "alternate_paths": {l: f'/{l}/index.html' for l in LANGUAGES}
            })
            all_urls[home_path] = {'lastmod': latest_date, 'alternates': {l: f'/{l}/index.html' for l in LANGUAGES}}

            for i, date in enumerate(sorted_dates):
                prev_date = sorted_dates[i + 1] if i + 1 < len(sorted_dates) else None
                next_date = sorted_dates[i - 1] if i > 0 else None
                daily_path = f"/{lang}/archive/{date.strftime('%Y-%m-%d')}.html"
                self._render_page('daily_archive.html',
                                  os.path.join(PATH_OUTPUT, lang, 'archive', f"{date.strftime('%Y-%m-%d')}.html"), {
                                      **common_context,
                                      "title": f"{translator('site_name')} - {date.strftime(date_format)}",
                                      "description": f"Trending projects for {date.strftime(date_format)}",
                                      "nav_active": "archive",
                                      "date": date,
                                      "projects": lang_data[date],
                                      "prev_date": prev_date,
                                      "next_date": next_date,
                                      "canonical_path": daily_path,
                                      "alternate_paths": {l: f"/{l}/archive/{date.strftime('%Y-%m-%d')}.html" for l in
                                                          LANGUAGES}
                                  })
                all_urls[daily_path] = {'lastmod': date,
                                        'alternates': {l: f"/{l}/archive/{date.strftime('%Y-%m-%d')}.html" for l in
                                                       LANGUAGES}}

            monthly_archives = {}
            for date in sorted_dates:
                month_key = date.strftime("%Y-%m")
                if month_key not in monthly_archives:
                    monthly_archives[month_key] = {
                        "display": date.strftime("%B %Y" if lang == 'en' else "%Y年 %m月"),
                        "days": []
                    }
                monthly_archives[month_key]['days'].append({
                    'date': date,
                    'count': len(lang_data[date])
                })

            sorted_monthly_archives = dict(sorted(monthly_archives.items(), reverse=True))

            archive_path = f'/{lang}/archive.html'
            self._render_page('archive.html', os.path.join(PATH_OUTPUT, lang, 'archive.html'), {
                **common_context,
                "title": f"{translator('archive_title')} - {translator('site_name')}",
                "description": "Archive of all past trending projects.",
                "nav_active": "archive",
                "monthly_archives": sorted_monthly_archives,
                "canonical_path": archive_path,
                "alternate_paths": {l: f'/{l}/archive.html' for l in LANGUAGES}
            })
            all_urls[archive_path] = {'lastmod': latest_date,
                                      'alternates': {l: f'/{l}/archive.html' for l in LANGUAGES}}

            about_path = f'/{lang}/about.html'
            self._render_page('about.html', os.path.join(PATH_OUTPUT, lang, 'about.html'), {
                **common_context,
                "title": f"{translator('about_title')} - {translator('site_name')}",
                "description": "About the Daily Stars project.",
                "nav_active": "about",
                "canonical_path": about_path,
                "alternate_paths": {l: f'/{l}/about.html' for l in LANGUAGES}
            })
            all_urls[about_path] = {'lastmod': latest_date, 'alternates': {l: f'/{l}/about.html' for l in LANGUAGES}}

        # --- 生成收尾文件 (逻辑已修正) ---
        # 1. 直接复制根跳转页，而不是渲染它
        print("Generating root index and sitemap...")
        shutil.copyfile(
            os.path.join(PATH_TEMPLATES, 'root_index.html'),
            os.path.join(PATH_OUTPUT, 'index.html')
        )

        # 2. 渲染 sitemap
        self._render_page('sitemap.xml', os.path.join(PATH_OUTPUT, 'sitemap.xml'), {
            "all_urls": all_urls,
            "base_url": BASE_URL
        })

        print("\nBuild finished successfully!")


if __name__ == '__main__':
    builder = SiteBuilder()
    builder.build()
