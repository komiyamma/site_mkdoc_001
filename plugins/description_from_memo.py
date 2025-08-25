import os
import html
from mkdocs.plugins import BasePlugin

class Plugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        md_path = page.file.abs_src_path
        memo_path = os.path.splitext(md_path)[0] + '.memo'
        if os.path.exists(memo_path):
            with open(memo_path, encoding='utf-8') as f:
                desc = f.read().replace('\n', ' ')
                desc = html.escape(desc)
                if not page.meta:
                    page.meta = {}
                page.meta['description'] = desc
        return markdown
