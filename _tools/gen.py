#!/usr/bin/env python3
"""Generates the static pages of the Klabunde Media portfolio. Run from repo root: python3 _tools/gen.py"""
import os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATS = [
 ("commercial", "Commercial &amp; Brand", "Product films, brand spots and social campaigns, with notes on the brief, the constraints and the decisions behind each cut.",
  [("commercial-01", "Placeholder: Product Launch Film", "30s and 15s spot, plus social cutdowns"),
   ("commercial-02", "Placeholder: Brand Story Series", "A multi-part social series")]),
 ("cinematic", "Cinematic &amp; Narrative", "Short films, travel pieces and story-driven edits, where pacing, sound and structure carry the work.",
  [("cinematic-01", "Placeholder: Main Cinematic Compilation", "The reel at the top of the home page"),
   ("cinematic-02", "Placeholder: Short Narrative Edit", "A short story told in a few minutes")]),
 ("color", "Color Grading", "Before-and-after grades in DaVinci Resolve, with the look, the reference and the node approach written out.",
  [("color-01", "Placeholder: Moody Exterior Grade", "Before/after look development"),
   ("color-02", "Placeholder: Skin-Tone Matching Across Cameras", "Before/after camera match")]),
 ("motion-vfx", "Motion Graphics &amp; VFX", "Titles, tracking, rotoscoping and compositing, each with a breakdown of how the shot was built.",
  [("motion-vfx-01", "Placeholder: Tracked Title Sequence", "Breakdown: track, roto, composite"),
   ("motion-vfx-02", "Placeholder: Compositing Breakdown", "Breakdown: plates, layers, final")]),
 ("ai-evaluation", "AI Video Evaluation", "Written critiques of AI-generated video, scored against a rubric: motion, physics, continuity, lighting and what an editor would fix.",
  [("ai-evaluation-01", "Placeholder: AI Clip Critique Set", "3–5 generated clips scored against a rubric"),
   ("ai-evaluation-02", "Placeholder: Critique-to-Rules Workflow", "Turning editing feedback into written rules")]),
]
NAV = [(c[0], c[1]) for c in CATS] + [("about", "About")]

def rel(depth): return "../" * depth

def head(title, depth, desc="Daniel Klabunde. Video editing, color and cinematic storytelling."):
    r = rel(depth)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{r}assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css">
</head>
<body>
"""

def header(depth, active=None):
    r = rel(depth)
    links = "".join(
        f'<li><a href="{r}{slug}/"{" class=\"active\"" if slug == active else ""}>{name}</a></li>' for slug, name in NAV)
    return f"""<header class="site-header">
  <div class="wrap nav-row">
    <a class="brand" href="{r}index.html"><img src="{r}assets/monogram.png" alt="" class="brand-mark"><span class="brand-text">Daniel Klabunde<small>Klabunde Media</small></span></a>
    <nav><ul class="nav">{links}</ul></nav>
  </div>
</header>
"""

def footer(depth):
    r = rel(depth)
    cols = "".join(f'<li><a href="{r}{s}/">{n}</a></li>' for s, n in NAV)
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <div class="footer-brand"><img src="{r}assets/monogram.png" alt="" class="brand-mark"> Klabunde Media</div>
      <p class="muted">Video editing, color grading and cinematic storytelling by Daniel Klabunde.</p>
    </div>
    <div><h4>Work</h4><ul>{cols}</ul></div>
    <div><h4>Contact</h4><ul><li><a href="{r}about/#contact">Get in touch</a></li><li class="ph-inline">Placeholder: email</li><li class="ph-inline">Placeholder: YouTube / Instagram links</li></ul></div>
  </div>
  <div class="wrap footer-base">© 2026 Daniel Klabunde · Klabunde Media</div>
</footer>
</body>
</html>
"""

def video_slot(label, note):
    return f"""<div class="video-frame" data-slot="video">
      <!-- VIDEO SLOT: replace this whole <div class="video-placeholder"> with one of:
           <iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID" title="..." allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>
           <iframe src="https://player.vimeo.com/video/VIDEO_ID" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
           <video src="assets/video/FILE.mp4" poster="assets/video/FILE.jpg" controls playsinline></video> -->
      <div class="video-placeholder">
        <div class="play"></div>
        <div class="ph-label">{label}</div>
        <div class="ph-note">{note}</div>
      </div>
    </div>"""

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(content)

# ---------------- HOME ----------------
def home():
    cards = ""
    for i, (slug, name, blurb, projs) in enumerate(CATS, 1):
        cards += f"""<a class="cat-row" href="{slug}/">
        <span class="cat-num">0{i}</span>
        <span class="cat-body"><h3>{name}</h3><p>{blurb}</p></span>
        <span class="cat-meta">{len(projs)} projects <span class="arrow">→</span></span>
      </a>"""
    feat = ""
    for slug, name, blurb, projs in CATS[:3]:
        pslug, ptitle, psub = projs[0]
        feat += f"""<article class="feature">
        <a href="projects/{pslug}.html" class="thumb ph-thumb"><span>Placeholder still</span></a>
        <div class="feature-body">
          <div class="eyebrow">{name}</div>
          <h3><a href="projects/{pslug}.html">{ptitle}</a></h3>
          <p class="ph-text">Placeholder: a two-sentence summary of the project and the story behind it goes here.</p>
          <a class="text-link" href="projects/{pslug}.html">Read the story →</a>
        </div>
      </article>"""
    body = f"""<section class="hero">
  <!-- HEADER IMAGE SLOT: assets/header.jpg (swap the file to replace it; keep the name). -->
  <div class="hero-img" style="background-image:url('assets/header.jpg')"></div>
  <div class="hero-overlay"></div>
  <div class="wrap hero-content">
    <div class="eyebrow light">Klabunde Media</div>
    <h1>Daniel Klabunde</h1>
    <p class="hero-sub">Video editing, color and cinematic storytelling.</p>
    <a href="#reel" class="btn">Watch the reel</a>
  </div>
</section>

<section id="reel" class="section reel">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Showreel</div><h2>Main Cinematic Compilation</h2></div>
    {video_slot("Placeholder: main cinematic compilation", "16:9 slot, ready for a YouTube or Vimeo embed or a local MP4")}
    <p class="caption ph-text">Placeholder: one line about the reel (length, what's in it, tools used).</p>
  </div>
</section>

<section class="section intro">
  <div class="wrap intro-grid">
    <div><div class="eyebrow">About the work</div><h2>Stories, not collages.</h2></div>
    <div class="prose">
      <p class="ph-text">Placeholder: short intro. Two or three sentences about how Daniel approaches editing, pacing and color, and what visitors will find on this site.</p>
      <p>Every project here has its own page with the brief, the role, the tools, and the full story of how it came together, including what I'd do differently next time.</p>
      <a class="text-link" href="about/">More about me →</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Selected work</div><h2>Featured projects</h2></div>
    <div class="features">{feat}</div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Browse</div><h2>Types of work</h2></div>
    <div class="cat-list">{cards}</div>
  </div>
</section>

<section class="section cta">
  <div class="wrap cta-inner">
    <h2>Have a project in mind?</h2>
    <a class="btn" href="about/#contact">Get in touch</a>
  </div>
</section>
"""
    write("index.html", head("Daniel Klabunde · Klabunde Media", 0) + header(0) + "<main>" + body + "</main>" + footer(0))

# ---------------- CATEGORY ----------------
def category(slug, name, blurb, projs):
    items = ""
    for pslug, ptitle, psub in projs:
        items += f"""<article class="entry">
      <a href="../projects/{pslug}.html" class="thumb ph-thumb"><span>Placeholder still</span></a>
      <div class="entry-body">
        <div class="entry-meta"><span>Placeholder: year</span><span>Placeholder: role</span><span>Placeholder: tools</span></div>
        <h2><a href="../projects/{pslug}.html">{ptitle}</a></h2>
        <p class="entry-sub">{psub}</p>
        <p class="ph-text">Placeholder: project story preview. A short paragraph on the goal, the challenge and how the edit solved it. The full write-up lives on the project page.</p>
        <a class="text-link" href="../projects/{pslug}.html">Read the full story →</a>
      </div>
    </article>"""
    extra = ""
    if slug == "ai-evaluation":
        extra = """<aside class="note-box"><div class="eyebrow">Side note</div><p>I've also written editing rules and critiques to train an AI editing assistant (Editron). That work is a small part of this section; the focus here is my own judgment of what makes a shot work or fail.</p></aside>"""
    body = f"""<section class="page-head">
  <div class="wrap">
    <div class="crumbs"><a href="../index.html">Home</a> / {name}</div>
    <h1>{name}</h1>
    <p class="lede">{blurb}</p>
  </div>
</section>
<section class="section tight">
  <div class="wrap narrow-wide">
    <div class="entries">{items}</div>
    {extra}
  </div>
</section>
"""
    write(f"{slug}/index.html", head(f"{html.unescape(name)} · Daniel Klabunde", 1) + header(1, slug) + "<main>" + body + "</main>" + footer(1))

# ---------------- PROJECT ----------------
def project(cat, pslug, ptitle, psub, nxt):
    cslug, cname = cat[0], cat[1]
    block = ""
    if cslug == "color":
        block = """<section class="block">
        <h2>Before / After</h2>
        <div class="ba" data-ba>
          <div class="ba-pane ba-before ph-thumb"><span>Placeholder: BEFORE (log / ungraded)</span></div>
          <div class="ba-pane ba-after ph-thumb warm"><span>Placeholder: AFTER (final grade)</span></div>
          <input type="range" min="0" max="100" value="50" class="ba-range" aria-label="Before/after slider">
          <div class="ba-handle"></div>
        </div>
        <p class="caption">Drag to compare. Replace the two panes with <code>&lt;img&gt;</code> stills of the same frame.</p>
      </section>"""
    elif cslug == "motion-vfx":
        block = """<section class="block">
        <h2>Breakdown</h2>
        <div class="steps">
          <figure><div class="ph-thumb small"><span>Placeholder: 1. Plate</span></div><figcaption>Placeholder: original plate</figcaption></figure>
          <figure><div class="ph-thumb small"><span>Placeholder: 2. Track / roto</span></div><figcaption>Placeholder: tracking and roto pass</figcaption></figure>
          <figure><div class="ph-thumb small"><span>Placeholder: 3. Composite</span></div><figcaption>Placeholder: final composite</figcaption></figure>
        </div>
      </section>"""
    elif cslug == "ai-evaluation":
        block = """<section class="block">
        <h2>Rubric &amp; scores</h2>
        <table class="rubric">
          <thead><tr><th>Criterion</th><th>Clip A</th><th>Clip B</th><th>Clip C</th></tr></thead>
          <tbody>
            <tr><td>Motion &amp; physics</td><td>–</td><td>–</td><td>–</td></tr>
            <tr><td>Temporal consistency</td><td>–</td><td>–</td><td>–</td></tr>
            <tr><td>Lighting &amp; color</td><td>–</td><td>–</td><td>–</td></tr>
            <tr><td>Camera language</td><td>–</td><td>–</td><td>–</td></tr>
            <tr><td>Prompt adherence</td><td>–</td><td>–</td><td>–</td></tr>
          </tbody>
        </table>
        <p class="caption ph-text">Placeholder: scores and written critique per clip.</p>
      </section>"""
    else:
        block = """<section class="block">
        <h2>Stills</h2>
        <div class="steps">
          <figure><div class="ph-thumb small"><span>Placeholder still</span></div></figure>
          <figure><div class="ph-thumb small"><span>Placeholder still</span></div></figure>
          <figure><div class="ph-thumb small"><span>Placeholder still</span></div></figure>
        </div>
      </section>"""
    body = f"""<article class="project">
  <section class="page-head">
    <div class="wrap">
      <div class="crumbs"><a href="../index.html">Home</a> / <a href="../{cslug}/">{cname}</a> / Project</div>
      <h1>{ptitle}</h1>
      <p class="lede">{psub}</p>
    </div>
  </section>
  <section class="section tight">
    <div class="wrap">
      {video_slot("Placeholder: project video", "Swap in the embed or MP4 for this project")}
    </div>
  </section>
  <section class="section tight">
    <div class="wrap project-grid">
      <div class="prose story">
        <section class="block">
          <h2>Overview</h2>
          <p class="ph-text">Placeholder: project overview. What the piece is, who it was for (described generally, no client names), and what it needed to accomplish.</p>
        </section>
        <section class="block">
          <h2>The challenge</h2>
          <p class="ph-text">Placeholder: project story goes here. Describe the constraints: footage, deadline, audio, look, or anything that made this one hard.</p>
          <p class="ph-text">Placeholder: second paragraph for more detail.</p>
        </section>
        <section class="block">
          <h2>My approach</h2>
          <p class="ph-text">Placeholder: how the edit was structured, pacing and music choices, color decisions, and key moments in the cut.</p>
          <blockquote class="ph-text">Placeholder: a pull quote or the one decision that made the piece work.</blockquote>
          <p class="ph-text">Placeholder: further process notes.</p>
        </section>
        {block}
        <section class="block">
          <h2>What I'd do differently</h2>
          <p class="ph-text">Placeholder: an honest look back. What I'd change with more time, budget, or what I know now.</p>
        </section>
      </div>
      <aside class="details">
        <div class="details-card">
          <h3>Project details</h3>
          <dl>
            <dt>Category</dt><dd>{cname}</dd>
            <dt>Role</dt><dd class="ph-text">Placeholder: role</dd>
            <dt>Tools</dt><dd class="ph-text">Placeholder: tools</dd>
            <dt>Timeline</dt><dd class="ph-text">Placeholder: timeline</dd>
            <dt>Deliverables</dt><dd class="ph-text">Placeholder: deliverables</dd>
            <dt>Year</dt><dd class="ph-text">Placeholder: year</dd>
          </dl>
        </div>
      </aside>
    </div>
  </section>
  <section class="section tight">
    <div class="wrap pager">
      <a href="../{cslug}/">← All {cname}</a>
      <a href="{nxt[0]}.html">Next project: {nxt[1]} →</a>
    </div>
  </section>
</article>
<script src="../assets/site.js"></script>
"""
    write(f"projects/{pslug}.html", head(f"{html.unescape(ptitle)} · Daniel Klabunde", 1) + header(1, cslug) + "<main>" + body + "</main>" + footer(1))

# ---------------- ABOUT ----------------
def about():
    body = """<section class="page-head">
  <div class="wrap">
    <div class="crumbs"><a href="../index.html">Home</a> / About</div>
    <h1>About</h1>
    <p class="lede">Daniel Klabunde, editor and colorist at Klabunde Media.</p>
  </div>
</section>
<section class="section tight">
  <div class="wrap about-grid">
    <div class="ph-thumb portrait"><span>Placeholder: portrait</span></div>
    <div class="prose">
      <h2>Background</h2>
      <p class="ph-text">Placeholder: bio. How Daniel got into video, what kind of work Klabunde Media does, and what he cares about in an edit.</p>
      <p class="ph-text">Placeholder: second paragraph on approach, taste and influences.</p>
      <h2>Tools</h2>
      <ul class="tag-list"><li>DaVinci Resolve</li><li class="ph-text">Placeholder: tool</li><li class="ph-text">Placeholder: tool</li><li class="ph-text">Placeholder: tool</li></ul>
      <h2>Services</h2>
      <ul class="plain-list">
        <li>Editing: commercial, social and long-form</li>
        <li>Color grading</li>
        <li class="ph-text">Placeholder: motion graphics / VFX</li>
        <li class="ph-text">Placeholder: AI video evaluation and critique</li>
      </ul>
    </div>
  </div>
</section>
<section id="contact" class="section alt">
  <div class="wrap contact-grid">
    <div><div class="eyebrow">Contact</div><h2>Let's work together</h2><p class="muted">The best way to reach me is by email.</p></div>
    <div class="details-card">
      <dl>
        <dt>Email</dt><dd class="ph-text">Placeholder: email address</dd>
        <dt>YouTube</dt><dd><a href="https://www.youtube.com/@danklabunde">@danklabunde</a></dd>
        <dt>Instagram</dt><dd class="ph-text">Placeholder: handle</dd>
        <dt>Résumé</dt><dd class="ph-text">Placeholder: PDF link</dd>
      </dl>
    </div>
  </div>
</section>
"""
    write("about/index.html", head("About · Daniel Klabunde", 1) + header(1, "about") + "<main>" + body + "</main>" + footer(1))

if __name__ == "__main__":
    home(); about()
    allp = [(c, p) for c in CATS for p in c[3]]
    for c in CATS: category(*c)
    for i, (c, p) in enumerate(allp):
        n = allp[(i + 1) % len(allp)][1]
        project(c, p[0], p[1], p[2], (n[0], n[1]))
    print("built", 2 + len(CATS) + len(allp), "pages")
