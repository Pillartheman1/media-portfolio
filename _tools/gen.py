#!/usr/bin/env python3
"""Generates the static pages of the two-sided portfolio. Run from repo root: python3 _tools/gen.py
Root index.html = split landing. /daniel/ = personal side. /media-co/ = business side.
Old URLs (pre-split) get redirect stubs."""
import os, html, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SIDES = {
 "daniel": dict(
   name="Daniel Klabunde", sub="Personal work", logo="monogram.png", logo_cls="", hero="header.jpg",
   reel=("Placeholder: main cinematic compilation", "16:9 slot, ready for a YouTube or Vimeo embed or a local MP4"),
   reel_title="Main Cinematic Compilation",
   tagline="Personal projects in cinematic storytelling, color and visual craft.",
   other="media-co",
   cats=[
    ("cinematic", "Cinematic &amp; Narrative", "Short films, travel pieces and story-driven edits, where pacing, sound and structure carry the work.",
     [("cinematic-01", "Placeholder: Cinematic Compilation Breakdown", "The story behind the reel at the top of the home page"),
      ("cinematic-02", "Placeholder: Short Narrative Edit", "A short story told in a few minutes")]),
    ("color", "Color Grading", "Before-and-after grades in DaVinci Resolve, with the look, the reference and the node approach written out.",
     [("color-01", "Placeholder: Moody Exterior Grade", "Before/after look development"),
      ("color-02", "Placeholder: Skin-Tone Matching Across Cameras", "Before/after camera match")]),
    ("motion-vfx", "Motion &amp; VFX", "Titles, tracking, rotoscoping and compositing, each with a breakdown of how the shot was built.",
     [("motion-vfx-01", "Placeholder: Tracked Title Sequence", "Breakdown: track, roto, composite"),
      ("motion-vfx-02", "Placeholder: Compositing Breakdown", "Breakdown: plates, layers, final")]),
    ("ai-evaluation", "AI Video Evaluation", "Written critiques of AI-generated video, scored against a rubric: motion, physics, continuity, lighting and what an editor would fix.",
     [("ai-evaluation-01", "Placeholder: AI Clip Critique Set", "3–5 generated clips scored against a rubric"),
      ("ai-evaluation-02", "Placeholder: Critique-to-Rules Workflow", "Turning editing feedback into written rules")]),
   ],
   pages=[("about", "About Daniel")],
 ),
 "media-co": dict(
   name="Klabunde Media Co.", sub="Business work", logo="kmc-logo.png", logo_cls=" kmc", hero="kmc-hero.jpg",
   reel=("Placeholder: company showreel", "16:9 slot, ready for a YouTube or Vimeo embed or a local MP4"),
   reel_title="Company Showreel",
   tagline="Commercial, brand and social video production for businesses.",
   other="daniel",
   cats=[
    ("commercial", "Commercial &amp; Brand", "Product films, brand spots and campaigns, with notes on the brief, the constraints and the decisions behind each cut.",
     [("commercial-01", "Placeholder: Product Launch Film", "30s and 15s spot, plus social cutdowns"),
      ("commercial-02", "Placeholder: Brand Story Series", "A multi-part brand series")]),
    ("social", "Social Content", "Short-form vertical and feed content: hooks, pacing for the platform, and series built to be consistent week to week.",
     [("social-01", "Placeholder: Weekly Reel Series", "Recurring short-form deliverables"),
      ("social-02", "Placeholder: Launch Week Social Pack", "A set of cutdowns for one campaign")]),
   ],
   pages=[("services", "Services"), ("about", "About"), ("contact", "Contact")],
 ),
}
OLD = {  # old path -> new path (redirect stubs)
 "commercial/": "media-co/commercial/", "cinematic/": "daniel/cinematic/", "color/": "daniel/color/",
 "motion-vfx/": "daniel/motion-vfx/", "ai-evaluation/": "daniel/ai-evaluation/", "about/": "daniel/about/",
}
for side, cfg in SIDES.items():
    for c in cfg["cats"]:
        for p in c[3]:
            if not p[0].startswith("social"):
                OLD[f"projects/{p[0]}.html"] = f"{side}/projects/{p[0]}.html"

def rel(depth): return "../" * depth
import hashlib as _h, pathlib as _p
CSS_VER = _h.md5(_p.Path(__file__).resolve().parent.parent.joinpath("assets/style.css").read_bytes()).hexdigest()[:8]
X_URL = "https://x.com/DanJKlabunde"
X_HANDLE = "@DanJKlabunde"
X_SVG = '<svg class="x-icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'
def x_link(cls="x-link", text=True):
    t = f'<span>{X_HANDLE}</span>' if text else ''
    return f'<a class="{cls}" href="{X_URL}" target="_blank" rel="noopener" title="Dan Klabunde on X: {X_HANDLE}" aria-label="{X_HANDLE} on X">{X_SVG}{t}</a>'
FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">"""

def head(title, depth, side=None, desc="Daniel Klabunde and Klabunde Media Co. Video editing, color and cinematic storytelling."):
    r = rel(depth)
    fav = "favicon.png"  # DK favicon site-wide (Daniel: don't use the [K] icon)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{r}assets/{fav}">
{FONTS}
<link rel="stylesheet" href="{r}assets/style.css?v={CSS_VER}">
</head>
<body class="side-{side or 'landing'}">
"""

def nav_items(side):
    cfg = SIDES[side]
    return [(c[0], c[1]) for c in cfg["cats"]] + list(cfg["pages"])

def header(side, depth, active=None):
    cfg = SIDES[side]; r = rel(depth); s = f"{r}{side}/"
    o = SIDES[cfg["other"]]
    links = "".join(f'<li><a href="{s}{slug}/"{" class=\"active\"" if slug == active else ""}>{n}</a></li>' for slug, n in nav_items(side))
    return f"""<div class="util-bar"><div class="wrap util-row">
  <a href="{r}index.html">← Back to the landing page</a>
  <a class="switch" href="{r}{cfg['other']}/"><img src="{r}assets/{o['logo']}" alt="">Switch to {o['name']} →</a>
</div></div>
<header class="site-header">
  <div class="wrap nav-row">
    <a class="brand" href="{s}"><img src="{r}assets/{cfg['logo']}" alt="{cfg['name']} logo" class="brand-mark{cfg['logo_cls']}"><span class="brand-text">{cfg['name']}<small>{cfg['sub']}</small></span></a>
    <nav class="nav-wrap"><ul class="nav">{links}</ul>{x_link("x-link nav-x")}</nav>
  </div>
</header>
"""

def footer(side, depth):
    cfg = SIDES[side]; r = rel(depth); s = f"{r}{side}/"; o = SIDES[cfg["other"]]
    cols = "".join(f'<li><a href="{s}{slug}/">{n}</a></li>' for slug, n in nav_items(side))
    contact = f"{s}contact/" if side == "media-co" else f"{s}about/#contact"
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <div class="footer-brand"><img src="{r}assets/{cfg['logo']}" alt="" class="brand-mark{cfg['logo_cls']}"> {cfg['name']}</div>
      <p class="muted">{cfg['tagline']}</p>
      <p><a href="{r}{cfg['other']}/">Visit {o['name']} →</a><br><a href="{r}index.html">← Back to the landing page</a></p>
    </div>
    <div><h4>Explore</h4><ul>{cols}</ul></div>
    <div><h4>Contact</h4><ul><li><a href="{contact}">Get in touch</a></li><li><a href="{X_URL}" target="_blank" rel="noopener">X: {X_HANDLE}</a> <span class="muted small">(AI, filmmaking &amp; engineering)</span></li><li class="ph-inline">Placeholder: email</li><li class="ph-inline">Placeholder: other social links</li></ul></div>
  </div>
  <div class="wrap footer-base">© 2026 Daniel Klabunde · Klabunde Media Co.</div>
</footer>
</body>
</html>
"""

def video_slot(label, note):
    return f"""<div class="video-frame" data-slot="video">
      <!-- VIDEO SLOT: replace this whole <div class="video-placeholder"> with one of:
           <iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID" title="..." allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>
           <iframe src="https://player.vimeo.com/video/VIDEO_ID" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
           <video src="FILE.mp4" poster="FILE.jpg" controls playsinline></video> -->
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

def page(side, path, title, depth, active, body, script=False):
    js = f'<script src="{rel(depth)}assets/site.js"></script>' if script else ""
    write(path, head(title, depth, side) + header(side, depth, active) + "<main>" + body + "</main>" + js + footer(side, depth))

def page_head(side, depth, crumbs, h1, lede):
    r = rel(depth)
    c = f'<a href="{r}{side}/">{SIDES[side]["name"]}</a>' + "".join(f" / {x}" for x in crumbs)
    return f"""<section class="page-head"><div class="wrap">
    <div class="crumbs">{c}</div><h1>{h1}</h1><p class="lede">{lede}</p></div></section>"""

# ---------------- LANDING ----------------
def landing():
    d, m = SIDES["daniel"], SIDES["media-co"]
    body = f"""<main class="landing">
  <div class="landing-inner">
    <div class="landing-kicker">Choose a side</div>
    <div class="split">
      <a class="split-panel dk-panel" href="daniel/">
        <div class="panel-bg" style="background-image:url('assets/header-clean.jpg')"></div><div class="panel-shade"></div>
        <img src="assets/monogram.png" alt="DK monogram" class="split-logo dk">
        <h2>Daniel Klabunde</h2>
        <p>Personal projects: cinematic work, color, motion and AI video evaluation.</p>
        <span class="split-enter">Enter →</span>
      </a>
      <a class="split-panel kmc-panel" href="media-co/">
        <div class="panel-bg" style="background-image:url('assets/kmc-hero.jpg')"></div><div class="panel-shade"></div>
        <!-- LOGO SLOT: assets/kmc-logo.png = white transparent KLABUNDE / MEDIA COMPANY wordmark. -->
        <img src="assets/kmc-logo.png" alt="Klabunde Media Company wordmark" class="split-logo kmc">
        <h2>Klabunde Media Co.</h2>
        <p>Business projects: commercial, brand and social video production.</p>
        <span class="split-enter">Enter →</span>
      </a>
    </div>
    <p class="landing-x">AI, filmmaking &amp; engineering on X {x_link("x-link")}</p>
  </div>
</main>
</body>
</html>
"""
    write("index.html", head("Daniel Klabunde · Klabunde Media Co.", 0) + body)

# ---------------- SIDE HOME ----------------
def home(side):
    cfg = SIDES[side]; r = "../"
    cards = ""
    for i, (slug, name, blurb, projs) in enumerate(cfg["cats"], 1):
        cards += f"""<a class="cat-row" href="{slug}/"><span class="cat-num">0{i}</span>
        <span class="cat-body"><h3>{name}</h3><p>{blurb}</p></span>
        <span class="cat-meta">{len(projs)} projects <span class="arrow">→</span></span></a>"""
    feats = [(c[1], c[3][0]) for c in cfg["cats"]]
    if len(feats) < 3: feats.append((cfg["cats"][0][1], cfg["cats"][0][3][1]))
    feat = "".join(f"""<article class="feature">
        <a href="projects/{p[0]}.html" class="thumb ph-thumb"><span>Placeholder still</span></a>
        <div class="feature-body"><div class="eyebrow">{cn}</div>
          <h3><a href="projects/{p[0]}.html">{p[1]}</a></h3>
          <p class="ph-text">Placeholder: a two-sentence summary of the project and the story behind it goes here.</p>
          <a class="text-link" href="projects/{p[0]}.html">Read the story →</a></div></article>""" for cn, p in feats[:3])
    if side == "daniel":
        intro_h, intro = "Stories, not collages.", """<p class="ph-text">Placeholder: short intro. Two or three sentences about how Daniel approaches editing, pacing and color in his personal work.</p>
      <p>Every project here has its own page with the role, the tools, and the full story of how it came together, including what I'd do differently next time.</p>
      <a class="text-link" href="about/">More about me →</a>"""
        extra = ""
    else:
        intro_h, intro = "Video that does a job.", """<p class="ph-text">Placeholder: short company intro. What Klabunde Media Co. makes, who it's for (described generally, no client names), and how a project runs.</p>
      <p>Each case study covers the brief, the deliverables and how the edit solved the problem.</p>
      <a class="text-link" href="about/">About the company →</a>"""
        extra = """<section class="section"><div class="wrap">
    <div class="section-head"><div class="eyebrow">What we do</div><h2>Services</h2></div>
    <div class="svc-grid">""" + "".join(f"""<div class="svc"><h3>{t}</h3><p class="ph-text">Placeholder: one or two lines describing this service.</p></div>""" for t in ["Commercial &amp; brand films", "Social content", "Editing &amp; post-production", "Color grading"]) + """</div>
    <p style="margin-top:28px"><a class="text-link" href="services/">All services →</a></p></div></section>"""
    cta = "contact/" if side == "media-co" else "about/#contact"
    x_cta = f"""<section class="x-cta"><div class="wrap x-cta-inner">
    <div class="x-cta-mark">{X_SVG}</div>
    <div class="x-cta-text"><div class="eyebrow">On X</div>
      <h2>AI, filmmaking, and engineering.</h2>
      <p>Video production, Linux and STEM, and everything I&#39;m teaching myself about engineering along the way. Follow along on X.</p></div>
    <a class="btn btn-accent" href="{X_URL}" target="_blank" rel="noopener">Follow {X_HANDLE}</a>
</div></section>"""
    body = f"""<section class="side-hero">
  <!-- HERO IMAGE: assets/{cfg['hero']} (its logo is part of the image). -->
  <div class="side-hero-bg" style="background-image:url('{r}assets/{cfg['hero']}')"></div><div class="side-hero-overlay"></div>
  <div class="wrap side-hero-content">
    <h1 class="sr-only">{cfg['name']}</h1>
    {f'<img src="{r}assets/kmc-logo.png" alt="Klabunde Media Company" class="hero-logo">' if side != 'daniel' else ''}
    <div class="eyebrow light">{cfg['sub']}</div>
    <p class="hero-sub">{cfg['tagline']}</p>
    <a href="#reel" class="btn">Watch the {'reel' if side == 'daniel' else 'showreel'}</a>
  </div>
</section>
{x_cta if side == "daniel" else ""}
<section id="reel" class="section reel"><div class="wrap">
    <div class="section-head"><div class="eyebrow">Showreel</div><h2>{cfg['reel_title']}</h2></div>
    {video_slot(*cfg['reel'])}
    <p class="caption ph-text">Placeholder: one line about the reel (length, what's in it, tools used).</p>
</div></section>
<section class="section intro"><div class="wrap intro-grid">
    <div><div class="eyebrow">About the work</div><h2>{intro_h}</h2></div>
    <div class="prose">{intro}</div>
</div></section>
<section class="section"><div class="wrap">
    <div class="section-head"><div class="eyebrow">Selected work</div><h2>Featured projects</h2></div>
    <div class="features">{feat}</div>
</div></section>
<section class="section alt"><div class="wrap">
    <div class="section-head"><div class="eyebrow">Browse</div><h2>Types of work</h2></div>
    <div class="cat-list">{cards}</div>
</div></section>
{extra}
<section class="section cta"><div class="wrap cta-inner">
    <h2>Have a project in mind?</h2><a class="btn" href="{cta}">Get in touch</a>
</div></section>
"""
    page(side, f"{side}/index.html", f"{html.unescape(cfg['name'])}", 1, None, body)

# ---------------- CATEGORY ----------------
def category(side, slug, name, blurb, projs):
    items = "".join(f"""<article class="entry">
      <a href="../projects/{p}.html" class="thumb ph-thumb"><span>Placeholder still</span></a>
      <div class="entry-body">
        <div class="entry-meta"><span>Placeholder: year</span><span>Placeholder: role</span><span>Placeholder: tools</span></div>
        <h2><a href="../projects/{p}.html">{t}</a></h2><p class="entry-sub">{sub}</p>
        <p class="ph-text">Placeholder: project story preview. A short paragraph on the goal, the challenge and how the edit solved it. The full write-up lives on the project page.</p>
        <a class="text-link" href="../projects/{p}.html">Read the full story →</a>
      </div></article>""" for p, t, sub in projs)
    extra = ""
    if slug == "ai-evaluation":
        extra = """<aside class="note-box"><div class="eyebrow">Side note</div><p>I've also written editing rules and critiques to train an AI editing assistant (Editron). That work is a small part of this section; the focus here is my own judgment of what makes a shot work or fail.</p></aside>"""
    body = page_head(side, 2, [name], name, blurb) + f"""<section class="section tight"><div class="wrap"><div class="entries">{items}</div>{extra}</div></section>"""
    page(side, f"{side}/{slug}/index.html", f"{html.unescape(name)} · {html.unescape(SIDES[side]['name'])}", 2, slug, body)

# ---------------- PROJECT ----------------
def project(side, cat, pslug, ptitle, psub, nxt):
    cslug, cname = cat[0], cat[1]
    if cslug == "color":
        block = """<section class="block"><h2>Before / After</h2>
        <div class="ba" data-ba>
          <div class="ba-pane ba-before ph-thumb"><span>Placeholder: BEFORE (log / ungraded)</span></div>
          <div class="ba-pane ba-after ph-thumb warm"><span>Placeholder: AFTER (final grade)</span></div>
          <input type="range" min="0" max="100" value="50" class="ba-range" aria-label="Before/after slider"><div class="ba-handle"></div>
        </div><p class="caption">Drag to compare. Replace the two panes with <code>&lt;img&gt;</code> stills of the same frame.</p></section>"""
    elif cslug == "motion-vfx":
        block = """<section class="block"><h2>Breakdown</h2><div class="steps">
          <figure><div class="ph-thumb small"><span>Placeholder: 1. Plate</span></div><figcaption>Placeholder: original plate</figcaption></figure>
          <figure><div class="ph-thumb small"><span>Placeholder: 2. Track / roto</span></div><figcaption>Placeholder: tracking and roto pass</figcaption></figure>
          <figure><div class="ph-thumb small"><span>Placeholder: 3. Composite</span></div><figcaption>Placeholder: final composite</figcaption></figure>
        </div></section>"""
    elif cslug == "ai-evaluation":
        rows = "".join(f"<tr><td>{c}</td><td>–</td><td>–</td><td>–</td></tr>" for c in ["Motion &amp; physics", "Temporal consistency", "Lighting &amp; color", "Camera language", "Prompt adherence"])
        block = f"""<section class="block"><h2>Rubric &amp; scores</h2><table class="rubric">
          <thead><tr><th>Criterion</th><th>Clip A</th><th>Clip B</th><th>Clip C</th></tr></thead><tbody>{rows}</tbody></table>
        <p class="caption ph-text">Placeholder: scores and written critique per clip.</p></section>"""
    else:
        block = """<section class="block"><h2>Stills</h2><div class="steps">""" + "<figure><div class=\"ph-thumb small\"><span>Placeholder still</span></div></figure>" * 3 + "</div></section>"
    who = "who it was for (described generally, no client names), " if side == "media-co" else ""
    body = f"""<article class="project">
  {page_head(side, 2, [f'<a href="../{cslug}/">{cname}</a>', 'Project'], ptitle, psub)}
  <section class="section tight"><div class="wrap">{video_slot("Placeholder: project video", "Swap in the embed or MP4 for this project")}</div></section>
  <section class="section tight"><div class="wrap project-grid">
      <div class="prose story">
        <section class="block"><h2>Overview</h2><p class="ph-text">Placeholder: project overview. What the piece is, {who}and what it needed to accomplish.</p></section>
        <section class="block"><h2>The challenge</h2><p class="ph-text">Placeholder: project story goes here. Describe the constraints: footage, deadline, audio, look, or anything that made this one hard.</p><p class="ph-text">Placeholder: second paragraph for more detail.</p></section>
        <section class="block"><h2>My approach</h2><p class="ph-text">Placeholder: how the edit was structured, pacing and music choices, color decisions, and key moments in the cut.</p>
          <blockquote class="ph-text">Placeholder: a pull quote or the one decision that made the piece work.</blockquote><p class="ph-text">Placeholder: further process notes.</p></section>
        {block}
        <section class="block"><h2>What I'd do differently</h2><p class="ph-text">Placeholder: an honest look back. What I'd change with more time, budget, or what I know now.</p></section>
      </div>
      <aside class="details"><div class="details-card"><h3>Project details</h3><dl>
            <dt>Category</dt><dd>{cname}</dd>
            <dt>Role</dt><dd class="ph-text">Placeholder: role</dd>
            <dt>Tools</dt><dd class="ph-text">Placeholder: tools</dd>
            <dt>Timeline</dt><dd class="ph-text">Placeholder: timeline</dd>
            <dt>Deliverables</dt><dd class="ph-text">Placeholder: deliverables</dd>
            <dt>Year</dt><dd class="ph-text">Placeholder: year</dd>
      </dl></div></aside>
  </div></section>
  <section class="section tight"><div class="wrap pager"><a href="../{cslug}/">← All {cname}</a><a href="{nxt[0]}.html">Next project: {nxt[1]} →</a></div></section>
</article>"""
    page(side, f"{side}/projects/{pslug}.html", f"{html.unescape(ptitle)} · {html.unescape(SIDES[side]['name'])}", 2, cslug, body, script=True)

# ---------------- STATIC PAGES ----------------
def contact_card(side):
    yt = f'<dt>X</dt><dd><a href="{X_URL}">{X_HANDLE}</a></dd><dt>YouTube</dt><dd><a href="https://www.youtube.com/@danklabunde">@danklabunde</a></dd>' if side == "daniel" else '<dt>Social</dt><dd class="ph-text">Placeholder: company social links</dd>'
    return f"""<div class="details-card"><dl>
        <dt>Email</dt><dd class="ph-text">Placeholder: email address</dd>{yt}
        <dt>Instagram</dt><dd class="ph-text">Placeholder: handle</dd>
        {'<dt>Résumé</dt><dd class="ph-text">Placeholder: PDF link</dd>' if side == 'daniel' else '<dt>Booking</dt><dd class="ph-text">Placeholder: inquiry form or calendar link</dd>'}
      </dl></div>"""

def daniel_about():
    body = page_head("daniel", 2, ["About"], "About Daniel", "Editor and colorist. This is the personal side of my work.") + f"""
<section class="section tight"><div class="wrap about-grid">
    <div class="ph-thumb portrait"><span>Placeholder: portrait</span></div>
    <div class="prose">
      <h2>Background</h2>
      <p class="ph-text">Placeholder: bio. How Daniel got into video, what he makes for himself, and what he cares about in an edit.</p>
      <p class="ph-text">Placeholder: second paragraph on approach, taste and influences.</p>
      <h2>Tools</h2>
      <ul class="tag-list"><li>DaVinci Resolve</li><li class="ph-text">Placeholder: tool</li><li class="ph-text">Placeholder: tool</li><li class="ph-text">Placeholder: tool</li></ul>
      <p>Looking for business work? <a class="text-link" href="../../media-co/">Visit Klabunde Media Co. →</a></p>
    </div>
</div></section>
<section id="contact" class="section alt"><div class="wrap contact-grid">
    <div><div class="eyebrow">Contact</div><h2>Say hello</h2><p class="muted">The best way to reach me is by email.</p></div>
    {contact_card("daniel")}
</div></section>"""
    page("daniel", "daniel/about/index.html", "About Daniel · Daniel Klabunde", 2, "about", body)

def media_pages():
    svcs = ["Commercial &amp; brand films", "Social content", "Editing &amp; post-production", "Color grading", "Motion graphics &amp; titles"]
    rows = "".join(f"""<article class="svc-row"><h3>{s}</h3><div><p class="ph-text">Placeholder: what this service includes, typical deliverables and turnaround.</p>
      <ul class="plain-list ph-text"><li>Placeholder: deliverable</li><li>Placeholder: deliverable</li></ul></div></article>""" for s in svcs)
    body = page_head("media-co", 2, ["Services"], "Services", "What Klabunde Media Co. offers businesses.") + f"""
<section class="section tight"><div class="wrap"><div class="svc-list">{rows}</div>
<div class="note-box"><div class="eyebrow">How a project runs</div><p class="ph-text">Placeholder: brief → plan → shoot/edit → review rounds → delivery.</p></div></div></section>"""
    page("media-co", "media-co/services/index.html", "Services · Klabunde Media Co.", 2, "services", body)
    body = page_head("media-co", 2, ["About"], "About the company", "Klabunde Media Co. is Daniel Klabunde's video production company.") + """
<section class="section tight"><div class="wrap about-grid">
    <div class="ph-thumb portrait"><span>Placeholder: company image</span></div>
    <div class="prose">
      <h2>The company</h2>
      <p class="ph-text">Placeholder: company story. When it started, what it makes, and the kinds of businesses it works with (described generally, no client names).</p>
      <h2>How we work</h2>
      <p class="ph-text">Placeholder: approach, communication, review rounds and turnaround.</p>
      <h2>Who's behind it</h2>
      <p>Klabunde Media Co. is run by Daniel Klabunde. <a class="text-link" href="../../daniel/">See Daniel's personal work →</a></p>
    </div>
</div></section>"""
    page("media-co", "media-co/about/index.html", "About · Klabunde Media Co.", 2, "about", body)
    body = page_head("media-co", 2, ["Contact"], "Contact", "Tell us about your project.") + f"""
<section class="section tight"><div class="wrap contact-grid">
    <div class="prose"><h2>Start a project</h2><p class="ph-text">Placeholder: what to include in an inquiry (goals, deliverables, timeline, budget range) and how fast you'll hear back.</p></div>
    {contact_card("media-co")}
</div></section>"""
    page("media-co", "media-co/contact/index.html", "Contact · Klabunde Media Co.", 2, "contact", body)

def redirects():
    for old, new in OLD.items():
        path = old + "index.html" if old.endswith("/") else old
        depth = path.count("/")
        target = rel(depth) + new
        write(path, f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Moved</title>
<meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{target}">
<script>location.replace({target!r} + location.hash);</script></head>
<body style="background:#202123;color:#eff0eb;font-family:sans-serif">This page moved to <a style="color:#e07b3e" href="{target}">{target}</a>.</body></html>
""")

if __name__ == "__main__":
    for d in ["daniel", "media-co", "projects", "commercial", "cinematic", "color", "motion-vfx", "ai-evaluation", "about"]:
        shutil.rmtree(os.path.join(ROOT, d), ignore_errors=True)
    landing(); redirects()
    n = 1
    for side, cfg in SIDES.items():
        home(side); n += 1
        allp = [(c, p) for c in cfg["cats"] for p in c[3]]
        for c in cfg["cats"]: category(side, *c); n += 1
        for i, (c, p) in enumerate(allp):
            nx = allp[(i + 1) % len(allp)][1]
            project(side, c, p[0], p[1], p[2], (nx[0], nx[1])); n += 1
    daniel_about(); media_pages(); n += 4
    print("built", n, "pages +", len(OLD), "redirects")
