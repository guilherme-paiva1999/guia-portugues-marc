"""Gera index.html (arquivo único) a partir de src/.

Uso: python build.py
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')


def read(*parts):
    with open(os.path.join(SRC, *parts), encoding='utf-8') as f:
        return f.read()


def js(value):
    # "<" escapado para que o JSON possa ficar dentro de <script> sem fechar a tag
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')


meta = json.loads(read('pages.json'))
pages = {m['file']: {'id': m['id'], 'title': m['title'], 'body': read('pages', m['file'])} for m in meta}
order = [m['file'] for m in meta]
nav = [[m['file'], m['nav'], m['nav_en']] for m in meta]

html = read('template.html')
for key, value in (
    ('{{SHELL_JSON}}', read('shell.html')),
    ('{{PAGES_JSON}}', pages),
    ('{{ORDER_JSON}}', order),
    ('{{NAV_JSON}}', nav),
):
    html = html.replace(key, js(value))

with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print('index.html gerado (%d páginas)' % len(pages))
