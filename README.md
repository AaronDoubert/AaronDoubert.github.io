# aarondoubert.github.io

Portfolio site. Jekyll, built by GitHub Pages straight from `main` — push and it's live in
about a minute. No Actions workflow, no build step on your machine.

Live at <https://aarondoubert.github.io>

---

## Adding a project

One file. Create `_projects/your-slug.md`:

```yaml
---
slug: grid-fin                      # must be unique; the collage refers to it
order: 8                            # position in the sidebar and in prev/next
title: Grid fin modeling
summary: One line. Shows under the title and on the home cards.
context: Personal project
when: 2026
tools: Fusion 360, Simulink
status: In progress
current: In progress                # delete this line if it shouldn't show under
                                    # "Currently working on"
repo: https://github.com/AaronDoubert/gridfinModeling   # optional

hero:
  src: gf-assembly.jpg              # a file in assets/img/
  alt: Grid fin assembly.
  caption: Grid fin assembly.

shots:
  - src: gf-cfd.jpg
    alt: Pressure field on one fin.
    caption: Pressure field on one fin.
  - src: gf-sweep.jpg
    alt: Hinge moment against deflection.
    caption: Hinge moment against deflection.
    full: true                      # spans both gallery columns
---

Two or three sentences, if the images don't say it. That's all this needs.
```

Commit and push. The sidebar, the numbering, prev/next and the page itself all follow from
`order` — nothing else to update.

Then, to put its images on the home page, add rows to `_data/collage.yml`.

### Image options

| Option | Use it when |
|---|---|
| *(nothing)* | A CAD render on white. The frame is white, so the part floats in it. |
| `photo: true` | A camera photo. Fills the tile edge to edge instead of fitting inside it. |
| `tone: dark` | The render has its own black ground — a KiCad 3D board, say. |
| `tone: grey` | The render has a flat grey ground, like a raw SolidWorks viewport grab. |

`tone` exists so an image with a baked-in background bleeds to the tile edge rather than
sitting in it as a hard rectangle.

---

## Preparing images

Site images are JPEGs, 1400 px on the long edge. Convert a raw screenshot with:

```powershell
python "..\tools\prep_images.py" "C:\Users\doubi\Documents\Portfolio Content\02_PART_Control_Surfaces\renders\new" assets\img --prefix cs-
```

It trims the white margin, scales, and writes an optimised JPEG. `--crop left,top,right,bottom`
shaves CAD UI (view cube, toolbar) off first. `--help` for the rest.

Prefixes in use: `cs-` control surfaces, `pl-` payload, `afc-` flight controller, `dc-` Dacora,
`asme-` battlebot, `ece-` electronics labs.

---

## Where everything lives

| What | Where |
|---|---|
| A project's content and images | `_projects/<slug>.md` |
| Home page intro | `index.md` |
| Home page image grid | `_data/collage.yml` |
| "Currently working on" with no page yet | `_data/soon.yml` |
| Name, email, LinkedIn, GitHub, resume | `_config.yml` under `author:` |
| Colours, type, spacing | `_sass/_style.scss` |
| Page structure | `_layouts/`, `_includes/sidebar.html` |
| Images | `assets/img/` |
| Fonts | `assets/fonts/` (self-hosted, no third-party requests) |

Changing anything in `_config.yml` changes it on every page at once.

---

## The resume link

The sidebar Resume link is switched off. To turn it on, drop `resume.pdf` in the repo root and
uncomment the `resume:` line in `_config.yml`. Note the repo is public, so anything you commit
is downloadable — scrub the phone number first.

---

## Type

Self-hosted, no Google Fonts requests at runtime:

- **Newsreader** — headings, titles, the lead paragraph
- **Archivo** — body text
- **Chivo Mono** — specs, captions, labels, numbers

To swap one, drop a `.woff2` in `assets/fonts/` and change the `@font-face` block and the
`$display` / `$body` / `$mono` variables at the top of `_sass/_style.scss`.

---

## Running it locally (optional)

Needs Ruby, which isn't installed on this machine. If you want it:

```powershell
winget install RubyInstallerTeam.RubyWithDevKit
```

then

```powershell
bundle install
```

```powershell
bundle exec jekyll serve --livereload
```

Pushing to `main` and waiting a minute works just as well, and is what's been used so far.

---

## History

Supersedes two earlier attempts, both still on disk under `Documents\My Website`:

- `minimal-site/` — hand-written static HTML with a `projects.json` plus `tools/add_project.py`
  generator. Replaced by this. Its `add_project.py` and `sync` no longer apply.
- `site/` — the al-folio Jekyll site, now in the private repo `portfolio-al-folio`. Untouched.
