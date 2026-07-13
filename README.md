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

## Common edits

- **Update your intro / about** — edit the text in `index.html` (look for `EDIT ME` comments).
- **Add a project** — copy a `<div class="card">…</div>` block in `projects.html` and edit it. Put your best two on `index.html` too.
- **Publish a note** — copy `notes/sample-note.html` to `notes/your-title.html`, edit the title/date/content, then add a `<li>` link on `notes.html` (and optionally `index.html`).
- **Fix your links** — replace the placeholder LinkedIn/GitHub URLs in the footer of every page.
- **Change the accent color** — edit `--accent` at the top of `css/style.css`.

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
