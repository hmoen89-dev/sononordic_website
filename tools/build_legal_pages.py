"""Build eight static, JavaScript-free review pages from checked-in translations."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
LANGUAGES = {'sv': 'Svenska', 'nb': 'Norsk', 'da': 'Dansk', 'en': 'English'}


def filename(kind, lang):
    return f'akutpocus-{kind}{"" if lang == "sv" else "-" + lang}.html'


def esc(value):
    return html.escape(value, quote=True)


def paragraph(value):
    return esc(value).replace('info@sononordic.se',
                             '<a href="mailto:info@sononordic.se">info@sononordic.se</a>')


for lang in LANGUAGES:
    data = json.loads((SITE / 'legal-content' / f'{lang}.json').read_text())
    for kind in ('privacy', 'terms'):
        title = data[f'{kind}Title']
        links = []
        for code, label in LANGUAGES.items():
            current = ' aria-current="page"' if code == lang else ''
            links.append(f'<a href="{filename(kind, code)}" lang="{code}"{current}>{label}</a>')
        nav = ''.join(links)
        # Keep all content available even with JavaScript disabled.
        sections = ''.join(f'<section aria-labelledby="section-{i}"><h2 id="section-{i}">'
                           f'{esc(heading)}</h2><p>{paragraph(body)}</p></section>'
                           for i, (heading, body) in enumerate(data[kind], 1))
        contents = ''.join(f'<a href="#section-{i}">{esc(heading)}</a>'
                           for i, (heading, _) in enumerate(data[kind], 1))
        sibling = 'terms' if kind == 'privacy' else 'privacy'
        home_lang = 'sv' if lang in ('sv', 'nb', 'da') else 'en'
        providers = ''
        if kind == 'privacy':
            providers = '''<div class="providers">
<a href="https://www.revenuecat.com/dpa">RevenueCat</a>
<a href="https://www.loopia.se/om-loopia/dataskydd/">Loopia</a>
<a href="https://policies.google.com/privacy">Google</a>
<a href="https://www.apple.com/legal/privacy/">Apple</a>
<a href="https://www.imy.se/">IMY</a></div>'''
        page = f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{esc(title)} — AkutPOCUS App — SonoNordic</title>
<link rel="icon" href="logo.png"><link rel="stylesheet" href="akutpocus-legal.css"></head>
<body><a class="skip" href="#main">{esc(data['skip'])}</a>
<header><div class="top"><a class="brand" href="./?lang={home_lang}"><img src="logo.png" alt="">SonoNordic <small>AB</small></a>
<a class="home" href="./?lang={home_lang}">{esc(data['home'])} ↗</a></div></header>
<main id="main"><div class="intro"><p class="eyebrow">AkutPOCUS App</p><h1>{esc(title)}</h1>
<p class="date">{esc(data['date'])}</p><nav class="languages" aria-label="{esc(data['language'])}">{nav}</nav>
<p class="notice">{esc(data['notice'])}</p></div>
<div class="layout"><nav class="contents" aria-label="{esc(title)}">{contents}</nav>
<article>{sections}{providers}<a class="sibling" href="{filename(sibling, lang)}">{esc(data[sibling+'Title'])} →</a></article></div></main>
<footer><span>SonoNordic AB · 559586-5816</span><a href="mailto:info@sononordic.se">info@sononordic.se</a><span>© 2026 SonoNordic AB</span></footer>
</body></html>
'''
        (SITE / filename(kind, lang)).write_text(page)
