#!/usr/bin/env python3
"""Assemble index.html from shell.html and the page parts, in tree order."""
import pathlib
here = pathlib.Path(__file__).parent
PARTS = ['l1-overview', 'l2-pillars', 'l2-uses', 'l3-tech']
body = ''.join((here/'parts'/f'{p}.html').read_text() for p in PARTS if (here/'parts'/f'{p}.html').exists())
(here/'index.html').write_text((here/'shell.html').read_text().replace('<!-- PAGES -->\n', body))

# Standalone page for static hosting (the artifact host supplies its own skeleton).
page = (here/'index.html').read_text()
split = page.index('</style>') + len('</style>')
dist = here/'dist'
dist.mkdir(exist_ok=True)
(dist/'index.html').write_text(
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<style>body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>\n'
    + page[:split] + '\n</head>\n<body>\n' + page[split:] + '\n</body>\n</html>\n')

# Social preview image (1200×630) from og-card.html, when a headless Chromium is available.
import shutil, subprocess
if shutil.which('chromium'):
    subprocess.run(['chromium', '--headless', '--disable-gpu', '--hide-scrollbars', '--virtual-time-budget=4000',
                    f'--screenshot={dist/"og.png"}', '--window-size=1200,630', f'file://{here/"og-card.html"}'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
