# CLASSIFIED — INTELLIGENCE DOSSIER

Static, Persian RTL presentation for a 15-minute university talk about social engineering, OSINT, negotiation, historical cases, and ethical defenses. No backend, database, package install, or build tool is required.

## Architecture

- `index.html`: shared shell, mode navigation, presentation HUD.
- `css/styles.css`: shared design tokens, presentation shell and reader styles.
- `css/slides.css`: editorial foundation carried forward from the prototype.
- `css/deck.css`: responsive layouts, slide-specific motion, reader and print/PDF styles.
- `js/deck.js`: renderers, navigation, fullscreen, touch input, notes, print and built-in QR encoder.
- `js/app.js`: retained original prototype entry for reference; `index.html` uses `deck.js`.
- `data/slides.js`: slide manifest, source register and the central `siteConfig`.
- `assets/`: favicon and room for any locally licensed media.
- `.github/workflows/pages.yml`: static GitHub Pages deployment workflow.

The site uses native HTML, CSS, SVG and JavaScript modules. Diagrams and motion are authored in CSS/SVG; there are no remote images or runtime libraries. Persian type currently loads from Google Fonts, with system fallbacks if unavailable. External links in the references slide open the cited primary sources and research records.

## Run locally

Run `python serve.py` from this folder (on Windows, `py serve.py` may also work), then visit `http://127.0.0.1:8000`. The server uses Python's standard library; no packages need to be installed. Browsers restrict JavaScript modules opened with `file://`, so serve the folder instead of double-clicking `index.html`. If you have Node.js but not Python, `node serve.mjs` is an alternative.

## Controls

- `←` / `Space`: next slide; `→`: previous slide.
- `Home` / `End`: first / last slide.
- `P`: open presenter notes; `Esc`: close notes or exit fullscreen.
- Touch swipe and the on-screen buttons also move through slides.
- Use the PDF button and choose “Save as PDF” in the browser print dialog.

## GitHub Pages

The workflow packages only `index.html`, `css/`, `js/`, `data/`, and `assets/` into `_site/`; backups and working files are excluded. It deploys on pushes to `main` and can also be started manually. If the repository uses another default branch, change the workflow branch filter.

Before publishing, put the exact Pages URL into `siteConfig.publicUrl` in `data/slides.js`. The cover QR is generated in-browser from that value and the PNG download appears there. An empty value shows a clearly labeled, non-scannable demo pattern with a subtle pulse, never a QR for localhost or a made-up destination. The built-in encoder accepts UTF-8 URLs up to 106 bytes; ordinary GitHub Pages URLs fit.

After adding this folder to the intended GitHub repository, choose **Settings → Pages → Source: GitHub Actions**, push the workflow to the default branch, and wait for the deployment. No push or account setting was performed from this workspace.

The presenter notes are brief. Print/PDF uses a landscape reader layout. The reader mode contains all slides in a vertical flow. The navigation count and notes are generated from the slide data.
