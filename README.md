# Daniel Klabunde · Media Portfolio

Static site (plain HTML/CSS, tiny JS) for Klabunde Media, hosted on GitHub Pages.

## Swapping placeholders
- **Header image:** `assets/header.jpg` (1918×1080, cropped from Daniel's screenshot). Replace with the full-res original anytime, keeping the filename.
- **Main cinematic compilation:** in `index.html`, find `VIDEO SLOT` and replace the `video-placeholder` div with a YouTube/Vimeo `<iframe>` or a `<video>` tag (examples are in the comment). Each project page has the same slot.
- **Before/after (Color Grading pages):** replace the two `.ba-pane` divs with `<img>` stills.
- Any text styled as *Placeholder: …* is a stand-in to rewrite.

## Structure
- `index.html`: home (hero, reel, intro, featured, categories)
- `commercial/`, `cinematic/`, `color/`, `motion-vfx/`, `ai-evaluation/`, `about/`: section pages
- `projects/*.html`: project write-ups
- `_tools/gen.py`: regenerates all pages from one template (`python3 _tools/gen.py`). Edits made directly to the HTML are overwritten if you re-run it.
