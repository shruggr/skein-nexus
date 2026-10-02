# skein-nexus

The source of https://skein.nexus, the public explainer for
[skein](https://github.com/shruggr/skein). The site explains what a skein is
in three levels, from an overview down to the technical pages, and has the
one page that says what is built. The reference is the skein repository's
docs; where the two differ, the repository docs and the issues win.

## What it is

| path | what |
|---|---|
| `site-v2/parts/*.html` | the content: `l1-overview`, `l2-pillars`, `l2-uses`, `l3-tech` (one file per level) |
| `site-v2/shell.html` | the page skeleton, styles and script; the parts go in at `<!-- PAGES -->` |
| `site-v2/build.py` | assembles `shell.html` and the parts into `index.html`, then the standalone `dist/index.html`, and `dist/og.png` from `og-card.html` |
| `site-v2/og-card.html` | the 1200×630 social preview |
| `site-v2/wrangler.jsonc` | the Cloudflare Workers static-assets deployment: `dist/` served at the custom domain `skein.nexus` |
| `site-v2/dist/` | the built site (committed) |
| `site/index.html` | the single page deployed on 2026-09-29, kept for history; not deployed |
| `CHANGE-PLAN.md` | a working note: the 2026-10-01 comparison of the site against skein main |

## Use it

Edit a part, build, look, deploy:

```
cd site-v2
python3 build.py              # index.html, dist/index.html; dist/og.png when `chromium` is on PATH
python3 -m http.server -d dist 8000   # look at http://localhost:8000
npx wrangler deploy           # publishes dist/ to skein.nexus (needs Cloudflare credentials for the account)
```

Commit the parts and the rebuilt `index.html` and `dist/` together.

Writing for the site: plain and factual, present tense, the decided
vocabulary of skein's tracker (shruggr/skein#31): the kernel (the machine,
its four tables, the signer), apps under their own names, hosts
(transports, providers, store, signer). The design pages describe what is
decided; only the "What is built" page says what is built, and it names the
skein commit it was checked against.

## Build and test

There is no test suite. `build.py` needs Python 3 only; the social preview
needs a headless Chromium. Check a change by building and reading the
result in a browser, at phone width as well.

## Docs

| what | where |
|---|---|
| the reference for everything the site says | skein `README.md` and `docs/` |
| decisions, open questions, what is next | shruggr/skein issue [#31](https://github.com/shruggr/skein/issues/31) |

## Versions

Unversioned. Deploy from a clean `main`, so `site-v2/dist/` on `main` is what skein.nexus serves.

## Contributing

Work is tracked in shruggr/skein (#39 is the site); start at issue
[#31](https://github.com/shruggr/skein/issues/31).
