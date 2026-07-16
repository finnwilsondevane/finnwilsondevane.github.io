# Finn's personal site

Plain HTML/CSS — no build tools needed. Edit a file, save, refresh.

## Files

| File | What it is |
|---|---|
| `index.html` | Homepage: intro, featured projects, recent notes, about |
| `projects.html` | Full project list |
| `notes.html` | List of all notes |
| `notes/sample-note.html` | Template for a note — copy it to make a new one |
| `css/style.css` | All styling. Colors live in the `:root` variables at the top |
| `sitemap.xml` / `robots.txt` | Tells Google what pages exist. Add new notes here when you publish them |

## Common edits

- **Update your intro / about** — edit the text in `index.html` (look for `EDIT ME` comments).
- **Add a project** — copy a `<div class="card">…</div>` block in `projects.html` and edit it. Put your best two on `index.html` too.
- **Publish a note** — copy `notes/sample-note.html` to `notes/your-title.html`, remove the `<meta name="robots" content="noindex, nofollow">` line (that's what keeps the template out of search results), edit the title/date/content, then add a `<li>` link on `notes.html` (and optionally `index.html`) and a `<url>` entry in `sitemap.xml`.
- **Fix your links** — replace the placeholder LinkedIn/GitHub URLs in the footer of every page.
- **Change the accent color** — edit `--accent` at the top of `css/style.css`.
- **Swap the photo** — overwrite `assets/photo.jpg` with a new square (or square-ish) image, centered on your face. No HTML changes needed.
- **Replace the resume** — `assets/resume.pdf` is a placeholder (export your real CV as PDF and overwrite that exact file/filename — the "Resume" nav link on every page already points to it, so nothing else needs to change).
- **Update the share preview image** — `assets/og-image.png` is what shows up when someone pastes your site link into LinkedIn/Slack/iMessage. If you change your name/role, edit the `NAME`/`LINE1`/`LINE2` constants in `tools/generate_og_image.py` and re-run it: `pip3 install --user Pillow` (one-time), then `python3 tools/generate_og_image.py`.

## Preview locally

```
cd personal-site
python3 -m http.server 8721
```

Then open http://localhost:8721

## Deploy (GitHub Pages)

The site lives in a GitHub repo named `<your-username>.github.io`. Any change
pushed (or uploaded via the GitHub website) to the `main` branch goes live at
`https://<your-username>.github.io` within a minute or two.
