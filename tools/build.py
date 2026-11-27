#!/usr/bin/env python3
"""
Build the site from projects.json.

    python tools/build.py              rebuild every page
    python tools/build.py new <slug> "<Title>"   add a project, then rebuild
    python tools/build.py list         show what's in projects.json

Everything the site shows lives in projects.json. This writes index.html and
projects/<slug>.html from it. Hand edits to those files are overwritten, so make
changes in projects.json.
"""

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "projects.json"

ICON = {
    "pin": '<path d="M12 21s-7-6.1-7-11a7 7 0 0 1 14 0c0 4.9-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
    "li": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4.2c0-1.6 1-2.8 2.5-2.8S17 11.2 17 12.8V17M12 10v7"/>',
    "gh": '<path d="M9 19c-4 1.3-4-2-6-2.5m12 4.5v-3.4a3 3 0 0 0-.8-2.3c2.7-.3 5.6-1.3 5.6-6a4.7 4.7 0 0 0-1.3-3.2 4.4 4.4 0 0 0-.1-3.2s-1-.3-3.4 1.3a11.6 11.6 0 0 0-6 0C6.6 2.6 5.6 2.9 5.6 2.9a4.4 4.4 0 0 0-.1 3.2A4.7 4.7 0 0 0 4.2 9.3c0 4.6 2.8 5.7 5.5 6a3 3 0 0 0-.8 2.3V21"/>',
    "doc": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "moon": '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>',
}

# Sets the theme before first paint, so there is no flash of the wrong one.
BOOT = (
    '<script>(function(){try{var t=localStorage.getItem("theme");'
    'if(t)document.documentElement.setAttribute("data-theme",t);}catch(e){}})();</script>'
)


def e(s):
    return html.escape(str(s), quote=True)


def svg(key, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 24 24" aria-hidden="true">{ICON[key]}</svg>'


def load():
    with DATA.open(encoding="utf-8") as f:
        return json.load(f)


def save(d):
    DATA.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8", newline="\n")


# ---------------------------------------------------------------- components


def head(d, title, desc, up):
    css = f"{up}style.css"
    return (
        '<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{e(title)}</title>"
        f'<meta name="description" content="{e(desc)}">'
        '<meta name="color-scheme" content="light dark">\n'
        f'<link rel="preload" href="{up}fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>'
        f'<link rel="stylesheet" href="{css}">\n'
        f"{BOOT}\n</head>\n<body>\n"
    )


def sidebar(d, current_slug, up):
    s = d["site"]
    out = ['<div class="shell">', '<aside class="side">']
    out.append(f'<a class="name" href="{up}index.html">{e(s["name"])}</a>')
    out.append(f'<p class="role">{s["role"]}</p>')

    out.append('<ul class="facts">')
    out.append(f'<li><span class="loc">{svg("pin")}{e(s["location"])}</span></li>')
    out.append(f'<li><a href="mailto:{e(s["email"])}">{svg("mail")}{e(s["email"])}</a></li>')
    out.append(f'<li><a href="{e(s["linkedin"])}" rel="me noopener">{svg("li")}LinkedIn</a></li>')
    out.append(f'<li><a href="{e(s["github"])}" rel="me noopener">{svg("gh")}GitHub</a></li>')
    if s.get("resume"):
        out.append(f'<li><a href="{up}{e(s["resume"])}">{svg("doc")}Resume</a></li>')
    out.append("</ul>")

    out.append('<ul class="nav"><li class="lbl">Projects</li>')
    for p in d["projects"]:
        mark = ' aria-current="page"' if p["slug"] == current_slug else ""
        out.append(f'<li><a href="{up}projects/{p["slug"]}.html"{mark}>{e(p["title"])}</a></li>')
    out.append("</ul>")

    out.append(
        f'<div class="foot"><span>{s["footer"]}</span>'
        f'<button class="theme" type="button" aria-label="Switch theme">'
        f'{svg("sun","sun")}{svg("moon","moon")}</button></div>'
    )
    out.append("</aside>")
    return "\n".join(out)


def tile(img, up, photo=False, tone=None, alt=""):
    cls = "tile"
    if photo:
        cls += " photo"
    if tone:
        cls += f" {tone}"
    return (f'<span class="{cls}"><img src="{up}img/{e(img)}" alt="{e(alt)}" loading="lazy"></span>')


def figure(sh, up, alt, wide=False):
    cls = ' class="wide"' if wide else ""
    cap = f'<figcaption>{e(sh["cap"])}</figcaption>' if sh.get("cap") else ""
    return (f"<figure{cls}>"
            f'{tile(sh["img"], up, sh.get("photo"), sh.get("tone"), alt)}'
            f"{cap}</figure>")


def body_blocks(blocks):
    out = []
    for b in blocks or []:
        if "h" in b:
            out.append(f'<h3>{e(b["h"])}</h3>')
        elif "p" in b:
            out.append(f'<p>{e(b["p"])}</p>')
        elif "note" in b:
            out.append(f'<p class="note">{e(b["note"])}</p>')
        elif "table" in b:
            t = b["table"]
            hd = "".join(
                f'<th{" class=\"n\"" if i == len(t["head"]) - 1 else ""}>{e(c)}</th>'
                for i, c in enumerate(t["head"]))
            rows = ""
            for r in t["rows"]:
                rows += "<tr>" + "".join(
                    f'<td{" class=\"n\"" if i == len(r) - 1 else ""}>{e(c)}</td>'
                    for i, c in enumerate(r)) + "</tr>"
            out.append(f"<table><tr>{hd}</tr>{rows}</table>")
    return "\n".join(out)


# ------------------------------------------------------------------- pages


def build_index(d):
    s = d["site"]
    o = [head(d, s["name"], s["lead_sub"], ""), sidebar(d, None, ""), '<main class="content">']

    o.append(f'<p class="intro"><b>{e(s["lead"])}</b> {e(s["lead_sub"])}</p>')

    now = [p for p in d["projects"] if p.get("current")]
    if now or d.get("soon"):
        o.append("<h2>Currently working on</h2>")
        o.append('<ul class="now">')
        for p in now:
            o.append(
                f'<li><a href="projects/{p["slug"]}.html"><b>{e(p["title"])}</b>'
                f'<span>{e(p["summary"].rstrip("."))}</span>'
                f'<em>{e(p["current"])}</em></a></li>')
        for x in d.get("soon", []):
            o.append(
                f'<li class="soon"><b>{e(x["title"])}</b>'
                f'<span>{e(x["summary"])}</span><em>{e(x["note"])}</em></li>')
        o.append("</ul>")

    by = {p["slug"]: p for p in d["projects"]}
    rows = [c for c in d.get("collage", []) if c["slug"] in by]
    if rows:
        o.append("<h2>Work</h2>")
        o.append('<div class="collage">')
        for c in rows:
            p = by[c["slug"]]
            o.append(
                f'<a href="projects/{p["slug"]}.html">'
                f'{tile(c["img"], "", c.get("photo"), c.get("tone"), p["title"])}'
                f'<span class="cap">{e(p["title"])}<small>{e(p["tools"])}</small></span></a>')
        o.append("</div>")

    o.append(f'</main></div>\n<script src="theme.js" defer></script>\n</body></html>\n')
    return "\n".join(o)


def build_project(d, i):
    p = d["projects"][i]
    n = len(d["projects"])
    up = "../"
    o = [head(d, f'{p["title"]} · {d["site"]["name"]}', p["summary"], up),
         sidebar(d, p["slug"], up), '<main class="content">']

    o.append(f'<h1>{e(p["title"])}</h1>')
    o.append(f'<p class="intro">{e(p["summary"])}</p>')
    o.append(
        f'<div class="facts-row">'
        f'<div><span>Context</span>{e(p["context"])}</div>'
        f'<div><span>When</span>{e(p["when"])}</div>'
        f'<div><span>Tools</span>{e(p["tools"])}</div>'
        f'<div><span>Status</span>{e(p["status"])}</div></div>')

    shots = p.get("shots") or []
    if shots:
        o.append(f'<div class="hero">{figure(shots[0], up, p["title"])}</div>')

    o.append(body_blocks(p.get("body")))

    if len(shots) > 1:
        o.append('<div class="gallery">')
        for sh in shots[1:]:
            o.append(figure(sh, up, p["title"], wide=(sh.get("size") == "wide")))
        o.append("</div>")

    if p.get("repo"):
        o.append(f'<p class="links"><a href="{e(p["repo"])}" rel="noopener">Code on GitHub →</a></p>')

    prev = d["projects"][(i - 1) % n]
    nxt = d["projects"][(i + 1) % n]
    o.append(
        f'<nav class="next">'
        f'<a href="{prev["slug"]}.html"><small>Previous</small><b>{e(prev["title"])}</b></a>'
        f'<a style="text-align:right" href="{nxt["slug"]}.html"><small>Next</small><b>{e(nxt["title"])}</b></a>'
        f"</nav>")

    o.append(f'</main></div>\n<script src="{up}theme.js" defer></script>\n</body></html>\n')
    return "\n".join(o)


# ------------------------------------------------------------------ commands


def build():
    d = load()
    slugs = [p["slug"] for p in d["projects"]]
    if len(set(slugs)) != len(slugs):
        sys.exit("error: duplicate slug in projects.json")

    (ROOT / "projects").mkdir(exist_ok=True)
    (ROOT / "index.html").write_text(build_index(d), encoding="utf-8", newline="\n")
    for i, p in enumerate(d["projects"]):
        (ROOT / "projects" / f'{p["slug"]}.html').write_text(
            build_project(d, i), encoding="utf-8", newline="\n")

    # drop pages for projects that no longer exist
    for f in (ROOT / "projects").glob("*.html"):
        if f.stem not in slugs:
            f.unlink()
            print(f"  removed stale page {f.name}")

    missing = []
    for p in d["projects"]:
        for sh in p.get("shots") or []:
            if not (ROOT / "img" / sh["img"]).exists():
                missing.append(sh["img"])
    for c in d.get("collage", []):
        if not (ROOT / "img" / c["img"]).exists():
            missing.append(c["img"])
    for m in sorted(set(missing)):
        print(f"  ! image not in img/: {m}")

    print(f"built index.html and {len(slugs)} project pages")


def new(slug, title):
    d = load()
    if any(p["slug"] == slug for p in d["projects"]):
        sys.exit(f"error: slug '{slug}' already exists")
    d["projects"].append({
        "slug": slug, "title": title,
        "summary": "One line that says what it is.",
        "context": "Personal project", "when": "2026",
        "tools": "TODO", "status": "In progress", "current": "In progress",
        "body": [{"p": "A sentence or two, if the pictures don't say it."}],
        "shots": [],
    })
    save(d)
    print(f"added '{title}'")
    build()
    print(f"\nnext: fill in its entry in projects.json - summary, context, tools,\n"
          f"      and add images to \"shots\" (put the files in img/ first).\n"
          f"      then: python tools/build.py")


def show():
    d = load()
    for i, p in enumerate(d["projects"], 1):
        n = len(p.get("shots") or [])
        print(f'{i:>2}. {p["slug"]:<26} {p["status"]:<12} {n} image(s)'
              + ("" if n else "   <- no pictures yet"))
    for x in d.get("soon", []):
        print(f'    {"(no page)":<26} soon         {x["title"]}')


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "build":
        build()
    elif a[0] == "list":
        show()
    elif len(a) == 3 and a[0] == "new":
        new(a[1], a[2])
    else:
        print(__doc__)
        sys.exit(1)
