# Daniel Klabunde · Media Portfolio

Static site (plain HTML/CSS, tiny JS) for Klabunde Media, hosted on GitHub Pages.

## Structure
- `index.html`: split landing (lake background, two clickable logo panels)
- `daniel/`: personal side (cinematic compilation, Cinematic & Narrative, Color Grading, Motion & VFX, AI Video Evaluation, About Daniel)
- `media-co/`: Klabunde Media Co. side (company showreel, Commercial & Brand, Social Content, Services, About, Contact)
- `*/projects/*.html`: project write-ups (story template)
- Old pre-split URLs (`/commercial/`, `/projects/color-01.html`, ...) are redirect stubs.
- `_tools/gen.py` regenerates every page (`python3 _tools/gen.py`); hand edits to generated HTML are overwritten.

## Swapping placeholders
- **Lake header:** `assets/header.jpg` (landing background + Daniel hero).
- **KMC wordmark:** `assets/kmc-logo.png` (PLACEHOLDER; white on transparent). **KMC hero:** `assets/kmc-hero.jpg` (PLACEHOLDER).
  With the real files: `python3 _tools/import_kmc_assets.py HERO.png WORDMARK_BLACK.png [VERTICAL.png]`.
- **Videos:** search for `VIDEO SLOT` and replace the placeholder div with an `<iframe>` or `<video>`.
- **Before/after:** replace the two `.ba-pane` divs on Color Grading pages with `<img>` stills.
- Text styled *Placeholder: …* is a stand-in.
