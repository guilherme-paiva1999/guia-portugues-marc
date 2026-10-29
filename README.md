# Português do Brasil · Guia de aulas

Guia de aulas de português brasileiro (10 páginas). O resultado final é um único arquivo, `index.html`, gerado a partir dos fontes em `src/`.

## Como editar

| O que mudar | Onde |
|---|---|
| Texto/conteúdo de uma página | `src/pages/<página>.html` (só o corpo da página) |
| Título, id, nome no menu, ordem das páginas | `src/pages.json` |
| Layout, CSS e scripts comuns a todas as páginas | `src/shell.html` |
| Wrapper que carrega as páginas (iframes) | `src/template.html` |

Depois de editar, gere o arquivo final:

```bash
python build.py
```

Abra `index.html` no navegador para conferir. Se o site estiver no GitHub Pages, basta fazer commit e push de `index.html` junto com os fontes.

## Estrutura

```
build.py          # gera index.html
index.html        # arquivo final (gerado, versionado para o Pages)
src/
  template.html
  shell.html
  pages.json
  pages/*.html
```
