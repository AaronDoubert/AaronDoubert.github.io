# aarondoubert.github.io

Portfolio. Plain HTML and one stylesheet, generated from `projects.json`. No Jekyll, no build
on GitHub's side — the files in this repo are the site. Push and it's live in about a minute.

<https://aarondoubert.github.io>

---

## Adding a project

```powershell
python tools/build.py new grid-fin "Grid fin modeling"
```

That adds an entry to `projects.json` and writes `projects/grid-fin.html`. Then open
`projects.json`, fill in its `summary`, `context`, `when`, `tools`, `status`, and list its
pictures under `shots`. Put the image files in `img/` first.

```powershell
python tools/build.py
```

Rebuilds every page. Sidebar, nav order, previous/next and the home page all follow from
`projects.json` — there is nothing else to update, and no HTML to hand-edit. Anything you type
directly into `index.html` or `projects/*.html` gets overwritten on the next build.

### A project entry

```json
{
  "slug": "grid-fin",
  "title": "Grid fin modeling",
  "summary": "One line, shown under the title and on the home cards.",
  "context": "Personal project",
  "when": "2026",
  "tools": "Fusion 360, Simulink",
  "status": "In progress",
  "current": "In progress",
  "repo": "https://github.com/AaronDoubert/gridfinModeling",
  "body": [
    { "h": "A heading" },
    { "p": "A paragraph." },
    { "note": "A grey callout, for things still to do." },
    { "table": { "head": ["Thing", "Case", "Value"],
                 "rows": [["Row", "Condition", "1.0 unit"]] } }
  ],
  "shots": [
    { "img": "gf-assembly.jpg", "cap": "First one is the big image at the top." },
    { "img": "gf-cfd.jpg",      "cap": "The rest become the gallery." },
    { "img": "gf-sweep.jpg",    "cap": "Full width.", "size": "wide" }
  ]
}
```

Drop `current` if it shouldn't appear under "Currently working on". Drop `body` entirely if the
pictures say it. The last column of a table is right-aligned in mono, for numbers.

### Image options

| Option | Use it when |
|---|---|
| *(nothing)* | A CAD render on white. The tile is white too, so the part floats in it. |
| `"photo": true` | A camera photo. Fills the tile instead of fitting inside it. |
| `"tone": "dark"` | The render has its own black ground, like a KiCad 3D board. |
| `"tone": "grey"` | The render has a flat grey ground, like a raw SolidWorks viewport grab. |
| `"size": "wide"` | Gallery image spans both columns. |

`tone` stops an image with a baked-in background sitting in the tile as a hard rectangle.

### Other commands

```powershell
python tools/build.py list
```

Shows every project, its status and how many pictures it has, so it's obvious which pages are
still thin.

---

## Light and dark

Both. The site follows the visitor's system setting, and the button at the bottom of the sidebar
overrides it; that choice is remembered in their browser. The theme is set before the page paints,
so there's no flash.

Colours are CSS variables at the top of `style.css` — one block for light, one for dark. On dark,
CAD renders sit on a slightly dimmed off-white mat (`--mat` plus `--dim`) so they don't glare.

---

## Images

Site images are JPEGs, 1400 px on the long edge. To bring in a new screenshot:

```powershell
python "..\tools\prep_images.py" "C:\Users\doubi\Documents\Portfolio Content\02_PART_Control_Surfaces\renders\new" img --prefix cs-
```

Trims the white margin, scales, writes an optimised JPEG. `--crop left,top,right,bottom` shaves
CAD UI off first. `--help` for the rest.

Prefixes in use: `cs-` control surfaces, `pl-` payload, `afc-` flight controller, `dc-` Dacora,
`asme-` battlebot, `ece-` electronics labs.

---

## Where things are

| What | Where |
|---|---|
| All content | `projects.json` |
| Generator | `tools/build.py` |
| Colours, type, layout | `style.css` |
| Theme button behaviour | `theme.js` |
| Images | `img/` |
| Fonts | `fonts/` — Archivo and Chivo Mono, self-hosted, no third-party requests |
| Generated pages | `index.html`, `projects/*.html` — don't edit these |

`.nojekyll` tells GitHub Pages to serve the files as they are rather than running Jekyll over them.

---

## Still to do

- Resume link is off. Set `"resume": "resume.pdf"` in `projects.json` and put the file in the repo
  root. The repo is public, so scrub the phone number first.
- Ping pong launcher has no pictures and a live page.
- Aileron images are the weak half of the control-surfaces page. See
  `..\notes\CAD_SHOT_LIST.md`.

## History

Two earlier versions are still on disk under `Documents\My Website`, untouched: `minimal-site/`
(this layout's origin) and `site/` (al-folio, now the private repo `portfolio-al-folio`). Neither
feeds this site.
