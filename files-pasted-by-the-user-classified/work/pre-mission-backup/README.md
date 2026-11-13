# CLASSIFIED — INTELLIGENCE DOSSIER

Prototype for a Persian, RTL presentation and mobile reader about Social Engineering & OSINT. Scientific slide content is intentionally left for a later phase.

## Architecture

- `index.html`: shared shell, mode navigation, presentation HUD.
- `css/styles.css`: shared design tokens, presentation shell and reader styles.
- `css/slides.css`: responsive editorial layouts for slides 1–4.
- `js/app.js`: routing, slide rendering, keyboard navigation, fullscreen and presenter guide.
- `data/slides.js`: slide manifest separated from rendering.
- `assets/`: reserved for locally hosted fonts, images, icons, audio and video.

The prototype uses native HTML, CSS and JavaScript modules, with no build step or backend. This keeps GitHub Pages deployment straightforward. The presenter field on the cover can be edited directly in the browser; its initial value is configured in `data/slides.js`.

## Run locally

Use a local static server because browsers restrict JavaScript modules opened with `file://`. For example, run `python -m http.server 8000` in this folder and open `http://localhost:8000`.

## Controls

- `←` / `Space`: next slide
- `→`: previous slide
- `Esc`: exit browser fullscreen
- The top-right control toggles fullscreen.

The current slide manifest contains four entries. Add future slides as data entries and matching render functions in `js/app.js`; the slide counter and presenter guide are generated from the manifest. The next phase can add sourced research content and notes for the following slides.
