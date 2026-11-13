#!/usr/bin/env python3
"""Generates the static pages of the two-sided portfolio. Run from repo root: python3 _tools/gen.py
Root index.html = split landing. /daniel/ = personal side. /media-co/ = business side.
Old URLs (pre-split) get redirect stubs."""
import os, html, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def is_real(p):
    return isinstance(p, dict)
def pslug(p):
    return p["slug"] if is_real(p) else p[0]
def ptitle(p):
    return p["title"] if is_real(p) else p[1]
def psub(p):
    return p["subtitle"] if is_real(p) else p[2]
def paras(text, placeholder=False):
    cls = ' class="ph-text"' if placeholder else ""
    return "".join(f"<p{cls}>{html.escape(p.strip())}</p>" for p in text.split("\n\n") if p.strip())
def detail_dd(label, value, placeholder=False):
    ph = placeholder or (value or "").startswith("Placeholder")
    cls = ' class="ph-text"' if ph else ""
    return f"<dt>{label}</dt><dd{cls}>{html.escape(value)}</dd>"

# Real KMC projects. Write-ups are first-person, limited to the videos and facts Daniel provided.
ETHER = dict(
    slug="ether-exotics",
    title="Ether Exotics",
    subtitle="Two vertical films for a luxury dog-breeding ranch in northern Indiana.",
    summary="Two vertical videos for Ether Exotics, a luxury dog-breeding ranch in northern Indiana. Shot in a day, with about two days to prepare.",
    category_name="Commercial &amp; Brand",
    client="Ether Exotics",
    role="Cinematography and edit",
    tools="Sony a6100, DaVinci Resolve",
    timeline="Booked with about two days' notice; full-day shoot",
    deliverables="Two vertical videos, Lifestyle and Living Real Estate",
    year="2025",
    thumb="assets/video/ether-exotics/thumb.jpg",
    videos=[
        dict(label="Lifestyle", src="assets/video/ether-exotics/lifestyle.mp4", poster="assets/video/ether-exotics/lifestyle.jpg"),
        dict(label="Living Real Estate", src="assets/video/ether-exotics/living-real-estate.mp4", poster="assets/video/ether-exotics/living-real-estate.jpg"),
    ],
    stills=[
        dict(src="assets/video/ether-exotics/still-drone.jpg", cap="A drone look at the McLaren on the driveway"),
        dict(src="assets/video/ether-exotics/still-utv.jpg", cap="Dogs and friends in the ranch UTV"),
        dict(src="assets/video/ether-exotics/still-mclaren.jpg", cap="The McLaren 720S"),
    ],
    overview="I made two vertical videos for Ether Exotics, a luxury dog-breeding ranch in northern Indiana that sells dogs for more than $100,000. The brief was two films of the ranch, the owner and his friends, the dogs, and the cars on the property, including a McLaren 720S. The finished pieces are Lifestyle and Living Real Estate.",
    challenge="The shoot came together in about two days. There was no shot list and no schedule, and I was working with a borrowed backup camera, a Sony a6100, because my own body wasn't available. The ranch is in northern Indiana, a long drive, and the day ran on Central Time. We had a full day on the property, which is what made the short window workable.",
    approach="I spent the day walking the ranch and filming what was there: the dogs, a horse, cats, chickens, the people, and the cars. A drone shot looks down on the McLaren on the driveway. I didn't go in with a plan for individual setups. I just kept moving and covered the place. The two cuts came out of that footage.",
    differently="I'd build in more prep time, even on a short-notice job, and I'd keep a spare camera body ready so I'm not borrowing one the day before a shoot.",
)

LIV = dict(
    slug="liv-realty",
    title="LIV Realty · Jacob Deacon",
    subtitle="Short-form videos for Jacob Deacon and LIV Realty in Indianapolis.",
    summary="Vertical videos for Jacob Deacon, the number one realtor in Indiana, and LIV Realty, his brokerage.",
    category_name="Social Content",
    client="LIV Realty / Jacob Deacon",
    role="Placeholder: role",
    tools="Placeholder: tools",
    timeline="June 2026",
    deliverables="Three vertical videos: LIV Indy, Life Story, and Why Most Agents Fail",
    year="2026",
    thumb="assets/video/liv-realty/thumb.jpg",
    videos=[
        dict(label="LIV Indy", src="assets/video/liv-realty/liv-indy.mp4", poster="assets/video/liv-realty/liv-indy.jpg"),
        dict(label="Life Story", src="assets/video/liv-realty/life-story.mp4", poster="assets/video/liv-realty/life-story.jpg"),
        dict(label="Why Most Agents Fail", src="assets/video/liv-realty/why-most-agents-fail.mp4", poster="assets/video/liv-realty/why-most-agents-fail.jpg"),
    ],
    stills=[],
    overview="These are short vertical videos for Jacob Deacon, the number one realtor in Indiana, and LIV Realty, his brokerage, also the number one in the state. They were made in June 2026. Three pieces from that set are here: a brand video for the LIV Indy team, a personal story, and a talking-head on why most agents fail.",
    challenge=None,
    approach="LIV Indy cuts interview footage of Jacob with scenes of the team in the office. Life Story stays mostly on Jacob, with a little B-roll, as he talks about a roommate he barely knew, getting thrown out of an apartment, and an idea he thought could change other people's lives. Why Most Agents Fail is a talking-head piece about culture and working as a team.",
    differently=None,
)

MOON = dict(
    slug="moon-speaks-style",
    title="Moon Speaks Style",
    subtitle="A short vertical piece for Moon's personal brand.",
    summary="A short style video for Moon Speaks Style, Moon's personal brand.",
    category_name="Social Content",
    client="Moon Speaks Style",
    role="Production",
    tools="DaVinci Resolve",
    timeline="Placeholder: timeline",
    deliverables="One vertical video",
    year="2025",
    thumb="assets/video/moon-speaks-style/thumb.jpg",
    videos=[dict(label="Moon Speaks Style", src="assets/video/moon-speaks-style/moon-speaks-style.mp4", poster="assets/video/moon-speaks-style/poster.jpg")],
    stills=[],
    overview="I made a short vertical video for Moon Speaks Style, Moon's personal brand. Moon also owns Carmel Tailoring; this piece is for the personal brand, not for the shop. It's shot in close: a cigar being cut and lit, a skeleton watch, the texture of a jacket. The piece ends on a Klabunde Media Company card.",
    challenge=None,
    approach=None,
    differently=None,
)

NOOTRIMIND = dict(
    slug="nootrimind",
    title="Nootrimind",
    subtitle="A vertical brand film for a mental wellness supplement company in Indianapolis.",
    summary="A vertical brand film for Nootrimind, a mental wellness supplement brand based in Indianapolis.",
    category_name="Commercial &amp; Brand",
    client="Nootrimind",
    role="Placeholder: role",
    tools="DaVinci Resolve",
    timeline="Placeholder: timeline",
    deliverables="One vertical brand film",
    year="2025",
    thumb="assets/video/nootrimind/thumb.jpg",
    videos=[dict(label="Nootrimind", src="assets/video/nootrimind/nootrimind.mp4", poster="assets/video/nootrimind/poster.jpg")],
    stills=[],
    overview="I made a vertical brand film for Nootrimind, a mental wellness supplement brand based in Indianapolis. The film follows the founder, Joe, as he tells his story: watching his father go through dementia, then facing his own struggles with brain fog, confusion, and addiction after time in the Army. He talks about turning to fitness, wellness, and natural nootropics, and says he built the brand to help others find calm, focus, and balance. Later in the piece he talks about giving back to causes that matter to him, including the Alzheimer's Association, in honor of his father, and the Headstrong Project. The film ends on the NootriMind mark.",
    challenge=None,
    approach=None,
    differently=None,
)

RX = dict(
    slug="rx-building-murph",
    title="The RX Building · CrossFit Murph",
    subtitle="An event recap of the CrossFit Murph at The RX Building.",
    summary="An event recap of the CrossFit Murph at The RX Building, a community health center and CrossFit gym.",
    category_name="Social Content",
    client="The RX Building",
    role="Placeholder: role",
    tools="DaVinci Resolve",
    timeline="Placeholder: timeline",
    deliverables="One event recap video",
    year="2026",
    thumb="assets/video/rx-building-murph/thumb.jpg",
    videos=[dict(label="CrossFit Murph", src="assets/video/rx-building-murph/rx-building-murph.mp4", poster="assets/video/rx-building-murph/poster.jpg", aspect="4/3")],
    stills=[],
    overview="I made an event recap for The RX Building, a community health center and CrossFit gym, covering their CrossFit Murph. The video is a minute long and stays with the people in the gym: athletes working, a group coming through the doors, close shots of the barbells and the effort on people's faces. It opens and closes on black.",
    challenge=None,
    approach=None,
    differently=None,
)


ZAIDI = dict(
    slug="zaidi-jewelers",
    title="Zaidi Jewelers",
    subtitle="Recurring content for a premium jewelry brand in Indianapolis.",
    summary="A selection of ongoing work for Zaidi Jewelers, a regular client and a premium jewelry brand in Indianapolis.",
    category_name="Commercial &amp; Brand",
    client="Zaidi Jewelers",
    role="Placeholder: role",
    tools="DaVinci Resolve",
    timeline="Ongoing",
    deliverables="A selection of vertical videos for the brand",
    year="Ongoing",
    thumb="assets/video/zaidi-jewelers/thumb.jpg",
    videos=[
        dict(label="Pendants", src="assets/video/zaidi-jewelers/zaidi-1.mp4", poster="assets/video/zaidi-jewelers/zaidi-1.jpg"),
        dict(label="Worn", src="assets/video/zaidi-jewelers/zaidi-2.mp4", poster="assets/video/zaidi-jewelers/zaidi-2.jpg"),
        dict(label="The sketch", src="assets/video/zaidi-jewelers/zaidi-4.mp4", poster="assets/video/zaidi-jewelers/zaidi-4.jpg"),
        dict(label="The box", src="assets/video/zaidi-jewelers/zaidi-6.mp4", poster="assets/video/zaidi-jewelers/zaidi-6.jpg"),
    ],
    editron_videos=[
        dict(label="Cafe", src="assets/video/zaidi-jewelers/editron/cafe.mp4", poster="assets/video/zaidi-jewelers/editron/cafe.jpg"),
        dict(label="Date", src="assets/video/zaidi-jewelers/editron/date.mp4", poster="assets/video/zaidi-jewelers/editron/date.jpg"),
        dict(label="Event 1", src="assets/video/zaidi-jewelers/editron/event-1.mp4", poster="assets/video/zaidi-jewelers/editron/event-1.jpg"),
        dict(label="Event 2", src="assets/video/zaidi-jewelers/editron/event-2.mp4", poster="assets/video/zaidi-jewelers/editron/event-2.jpg"),
        dict(label="Event 3", src="assets/video/zaidi-jewelers/editron/event-3.mp4", poster="assets/video/zaidi-jewelers/editron/event-3.jpg"),
        dict(label="Newspaper, City Center", src="assets/video/zaidi-jewelers/editron/newspaper-city-center.mp4", poster="assets/video/zaidi-jewelers/editron/newspaper-city-center.jpg"),
        dict(label="Phone Captions", src="assets/video/zaidi-jewelers/editron/phone-captions.mp4", poster="assets/video/zaidi-jewelers/editron/phone-captions.jpg"),
        dict(label="Steering Wheel", src="assets/video/zaidi-jewelers/editron/steering-wheel.mp4", poster="assets/video/zaidi-jewelers/editron/steering-wheel.jpg"),
    ],
    stills=[],
    overview="Zaidi Jewelers, a premium jewelry brand in Indianapolis, is one of my most regular clients. I make recurring content for the brand, and the videos here are a selection of that work. One is a close look at pendants on a bust. Another puts the pieces on a person: earrings, a necklace, rings. A third follows a ring from a pencil sketch to the finished piece in its box. Another opens on a Zaidi Jewelers box and then shows the jewelry being worn.",
    challenge=None,
    approach=None,
    differently=None,
)


def yt_proj(slug, title, yt_id, category_name, kind):
    """A personal YouTube video. Titles are the real YouTube titles; write-ups stay limited to that fact."""
    poster = f"assets/video/youtube/{yt_id}.jpg"
    subtitle = f"A {kind} from my personal YouTube channel."
    overview = f'A {kind} from my personal YouTube channel, titled "{title}."'
    return dict(
        slug=slug,
        title=title,
        subtitle=subtitle,
        summary=subtitle,
        overview=overview,
        category_name=category_name,
        youtube=yt_id,
        thumb=poster,
        poster=poster,
        videos=[],
        stills=[],
        role="Placeholder: role",
        tools="Placeholder: tools",
        timeline="Placeholder: timeline",
        deliverables="One YouTube video",
        year="Placeholder: year",
        challenge=None,
        approach=None,
        differently=None,
    )

# Personal YouTube — titles from YouTube oEmbed, grouped as Daniel listed them.
# Vlogs & Storytelling
YT_POV_PRODUCTION = yt_proj("pov-running-a-production-company", "POV: Running a production company at 21 years old", "MSwFTPgla-8", "Vlogs &amp; Storytelling", "vlog")
YT_ONE_WEEK_CEO = yt_proj("one-week-with-a-production-company-ceo", "One week with a production company CEO", "Sqz7dxV9S0Q", "Vlogs &amp; Storytelling", "vlog")
YT_BATMAN = yt_proj("i-turned-myself-into-batman", "I turned myself into Batman", "J3RDdiJIqKI", "Vlogs &amp; Storytelling", "vlog")
YT_FOUND_MY_PASSION = yt_proj("i-finally-found-my-passion", "I finally found my passion", "K8_2jLyZvbU", "Vlogs &amp; Storytelling", "vlog")
YT_RESOLUTIONS = yt_proj("how-to-get-your-resolutions-to-stick", "How to get your resolutions to stick (don't make them)", "8wUFfLX5KlE", "Vlogs &amp; Storytelling", "vlog")
# Motion & VFX (motion graphics)
YT_DELETED_INSTAGRAM = yt_proj("i-deleted-instagram", "I deleted Instagram and it changed my life forever", "xurQZXO8B2I", "Motion &amp; VFX", "motion graphics video")
YT_DOPAMINE_DETOX = yt_proj("dopamine-detox-doesnt-work", "Dopamine Detox doesn't work", "0Hd6guhOTTE", "Motion &amp; VFX", "motion graphics video")
# Cinematic & Narrative (short films)
YT_THANKS_MOM = yt_proj("thanks-mom", "Thanks, Mom", "npCfEAypAoU", "Cinematic &amp; Narrative", "short film")
YT_EVERY_AMERICAN = yt_proj("every-american-needs-to-hear-this", "Every American NEEDS to Hear This", "whXj6oMwWEc", "Cinematic &amp; Narrative", "short film")
YT_IF_YOU_ARE_IN_PAIN = yt_proj("if-you-are-in-pain", "If you are in pain...", "3NuR39PLYsk", "Cinematic &amp; Narrative", "short film")
YT_LEFT_THE_MARINES = yt_proj("i-left-the-marines-dont", "I left the Marines. Don't.", "j_9FB71lt7Q", "Cinematic &amp; Narrative", "short film")
YT_ONCE_A_MARINE = yt_proj("once-a-marine", "Once a Marine...", "d9Rqc6ww0t4", "Cinematic &amp; Narrative", "short film")

VLOGS = [YT_POV_PRODUCTION, YT_ONE_WEEK_CEO, YT_BATMAN, YT_FOUND_MY_PASSION, YT_RESOLUTIONS]
SHORT_FILMS = [YT_THANKS_MOM, YT_EVERY_AMERICAN, YT_IF_YOU_ARE_IN_PAIN, YT_LEFT_THE_MARINES, YT_ONCE_A_MARINE]
MOTION_GRAPHICS = [YT_DELETED_INSTAGRAM, YT_DOPAMINE_DETOX]
FEATURED_DK = [YT_THANKS_MOM, YT_POV_PRODUCTION, YT_DELETED_INSTAGRAM]


CARMEL = dict(
    slug="carmel-tailoring",
    title="Carmel Tailoring",
    subtitle="Recurring content for the most prestigious men's clothier and tailor in the Indianapolis area.",
    summary="A selection of ongoing work for Carmel Tailoring, a consistent client and a men's clothier and tailor in Indianapolis, owned by Moon.",
    category_name="Commercial &amp; Brand",
    client="Carmel Tailoring",
    role="Placeholder: role",
    tools="DaVinci Resolve",
    timeline="Ongoing",
    deliverables="A selection of cinematic, social, and interview videos for the brand",
    year="Ongoing",
    thumb="assets/video/carmel-tailoring/thumb.jpg",
    videos=[],
    video_sections=[
        dict(title="Cinematic films", videos=[
            dict(label="The burgundy suit", src="assets/video/carmel-tailoring/vid-4.mp4", poster="assets/video/carmel-tailoring/vid-4.jpg", aspect="16/9"),
            dict(label="Portraits", src="assets/video/carmel-tailoring/vid-1.mp4", poster="assets/video/carmel-tailoring/vid-1.jpg", aspect="16/9"),
            dict(label="The shop", src="assets/video/carmel-tailoring/establishment.mp4", poster="assets/video/carmel-tailoring/establishment.jpg", aspect="16/9"),
            dict(label="The fitting", src="assets/video/carmel-tailoring/process.mp4", poster="assets/video/carmel-tailoring/process.jpg", aspect="16/9"),
        ]),
        dict(title="Social", videos=[
            dict(label="Fabrics", src="assets/video/carmel-tailoring/fabrics.mp4", poster="assets/video/carmel-tailoring/fabrics.jpg", aspect="9/16"),
            dict(label="The jacket", src="assets/video/carmel-tailoring/suit.mp4", poster="assets/video/carmel-tailoring/suit.jpg", aspect="9/16"),
            dict(label="Details", src="assets/video/carmel-tailoring/ct-1-1.mp4", poster="assets/video/carmel-tailoring/ct-1-1.jpg", aspect="9/16"),
        ]),
        dict(title="Interviews", videos=[
            dict(label="The designer", src="assets/video/carmel-tailoring/landry-intro.mp4", poster="assets/video/carmel-tailoring/landry-intro.jpg", aspect="9/16"),
            dict(label="Kay", src="assets/video/carmel-tailoring/testimonial.mp4", poster="assets/video/carmel-tailoring/testimonial.jpg", aspect="16/9"),
            dict(label="Interview", src="assets/video/carmel-tailoring/interview.mp4", poster="assets/video/carmel-tailoring/interview.jpg", aspect="16/9"),
        ]),
    ],
    stills=[],
    overview="Carmel Tailoring, the most prestigious men's clothier and tailor in the Indianapolis area, owned by Moon, is one of my most consistent clients. I make recurring content for the brand, and the videos here are a selection of that work.\n\nAmong them are landscape cinematic films. One follows a man in a burgundy suit, from a close look at his watch through an interior with bookshelves and a painting. Another moves with a man in tailored suits: walking through glass doors, sitting in a paneled room, sitting outside. A third stays in the shop — jackets on the rack, a suited mannequin, hanging cloth. Another is about the craft: a fitting with a tape measure, and a card showing stitching samples, including standard stitching and picked stitching.\n\nShort verticals look at the materials and the clothes on a person: fabric labels and swatch books, a man putting on a plaid jacket, and close details of a jacket cuff, with a shot of a man in a suit by a pond.\n\nThe interviews include a vertical piece with a menswear designer at Carmel Tailoring; a landscape film in which Kay introduces herself as the owner and founder and talks about the people she gets to dress; and a longer sit-down in the shop with several people.",
    challenge=None,
    approach=None,
    differently=None,
)

FEATURED_KMC = [ETHER, ZAIDI, LIV, CARMEL, NOOTRIMIND, RX]

SIDES = {
 "daniel": dict(
   name="Daniel Klabunde", sub="Personal work", logo="monogram.png", logo_cls="", hero="header.jpg",
   reel=("Placeholder: main cinematic compilation", "16:9 slot, ready for a YouTube or Vimeo embed or a local MP4"),
   reel_title="Main Cinematic Compilation",
   tagline="Personal projects in cinematic storytelling, color and visual craft.",
   other="media-co",
   cats=[
    ("cinematic", "Cinematic &amp; Narrative", "Short films, travel pieces and story-driven edits, where pacing, sound and structure carry the work.",
     SHORT_FILMS),
    ("vlogs", "Vlogs &amp; Storytelling", "Personal vlogs and story-driven videos from my YouTube channel.",
     VLOGS),
    ("motion-vfx", "Motion &amp; VFX", "Motion graphics, titles, tracking, rotoscoping and compositing.",
     MOTION_GRAPHICS),
    ("color", "Color Grading", "Before-and-after grades in DaVinci Resolve, with the look, the reference and the node approach written out.",
     [("color-01", "Placeholder: Moody Exterior Grade", "Before/after look development"),
      ("color-02", "Placeholder: Skin-Tone Matching Across Cameras", "Before/after camera match")]),
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
     [ETHER, ZAIDI, CARMEL, NOOTRIMIND]),
    ("social", "Social Content", "Short-form vertical and feed content: hooks, pacing for the platform, and series built to be consistent week to week.",
     [LIV, MOON, RX]),
   ],
   pages=[("about", "About")],
 ),
}
OLD = {  # old path -> new path (redirect stubs)
 "commercial/": "media-co/commercial/", "cinematic/": "daniel/cinematic/", "color/": "daniel/color/",
 "motion-vfx/": "daniel/motion-vfx/", "ai-evaluation/": "daniel/ai-evaluation/", "about/": "daniel/about/",
}
for side, cfg in SIDES.items():
    for c in cfg["cats"]:
        for p in c[3]:
            slug = pslug(p)
            if not slug.startswith("social"):
                OLD[f"projects/{slug}.html"] = f"{side}/projects/{slug}.html"
# Old placeholder slugs redirect to the real projects that replaced them.
OLD.update({
    "projects/commercial-01.html": "media-co/projects/ether-exotics.html",
    "projects/commercial-02.html": "media-co/projects/nootrimind.html",
    "media-co/projects/commercial-01.html": "media-co/projects/ether-exotics.html",
    "media-co/projects/commercial-02.html": "media-co/projects/nootrimind.html",
    "media-co/projects/social-01.html": "media-co/projects/liv-realty.html",
    "media-co/projects/social-02.html": "media-co/projects/moon-speaks-style.html",
    "projects/cinematic-01.html": "daniel/projects/thanks-mom.html",
    "projects/cinematic-02.html": "daniel/projects/every-american-needs-to-hear-this.html",
    "daniel/projects/cinematic-01.html": "daniel/projects/thanks-mom.html",
    "daniel/projects/cinematic-02.html": "daniel/projects/every-american-needs-to-hear-this.html",
    "projects/motion-vfx-01.html": "daniel/projects/i-deleted-instagram.html",
    "projects/motion-vfx-02.html": "daniel/projects/dopamine-detox-doesnt-work.html",
    "daniel/projects/motion-vfx-01.html": "daniel/projects/i-deleted-instagram.html",
    "daniel/projects/motion-vfx-02.html": "daniel/projects/dopamine-detox-doesnt-work.html",
})

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
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <div class="footer-brand"><img src="{r}assets/{cfg['logo']}" alt="" class="brand-mark{cfg['logo_cls']}"> {cfg['name']}</div>
      <p class="muted">{cfg['tagline']}</p>
      <p><a href="{r}{cfg['other']}/">Visit {o['name']} →</a><br><a href="{r}index.html">← Back to the landing page</a></p>
    </div>
    <div><h4>Explore</h4><ul>{cols}</ul></div>
    <div><h4>Contact</h4><ul><li><a href="{X_URL}" target="_blank" rel="noopener">X: {X_HANDLE}</a> <span class="muted small">(AI, filmmaking &amp; engineering)</span></li><li class="ph-inline">Placeholder: email</li><li class="ph-inline">Placeholder: other social links</li></ul></div>
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
    if side == "media-co":
        feats = [(proj["category_name"], proj) for proj in FEATURED_KMC]
        feat_class = "features kmc-featured"
        feat_eyebrow, feat_heading = "Selected work", "Featured projects"
    else:
        feats = [(proj["category_name"], proj) for proj in FEATURED_DK]
        feat_class = "features"
        feat_eyebrow, feat_heading = "YouTube", "Latest from YouTube"
    feat_cards = []
    for cn, proj in feats:
        slug, title = pslug(proj), html.escape(ptitle(proj))
        href = f"projects/{slug}.html"
        if is_real(proj) and proj.get("thumb"):
            thumb = f'<a href="{href}" class="thumb real"><img src="{r}{proj["thumb"]}" alt=""></a>'
            summary = f'<p>{html.escape(proj["summary"])}</p>'
        else:
            thumb = f'<a href="{href}" class="thumb ph-thumb"><span>Placeholder still</span></a>'
            summary = '<p class="ph-text">Placeholder: a two-sentence summary of the project and the story behind it goes here.</p>'
        feat_cards.append(f"""<article class="feature">
        {thumb}
        <div class="feature-body"><div class="eyebrow">{cn}</div>
          <h3><a href="{href}">{title}</a></h3>
          {summary}
          <a class="text-link" href="{href}">Read the story →</a></div></article>""")
    feat = "".join(feat_cards)
    if side == "daniel":
        intro_h, intro = "Stories, not collages.", """<p class="ph-text">Placeholder: short intro. Two or three sentences about how Daniel approaches editing, pacing and color in his personal work.</p>
      <p>Every project here has its own page with the role, the tools, and the full story of how it came together, including what I'd do differently next time.</p>
      <a class="text-link" href="about/">More about me →</a>"""
        extra = ""
    else:
        intro_h, intro = "Video that does a job.", """<p class="ph-text">Placeholder: short company intro. What Klabunde Media Co. makes, who it's for (described generally, no client names), and how the work runs, including ongoing client relationships.</p>
      <p>Each page covers the work for that client, including ongoing relationships, with notes on the constraints and the decisions behind the cuts.</p>
      <a class="text-link" href="about/">About the company →</a>"""
        extra = ""
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
    <div class="section-head"><div class="eyebrow">{feat_eyebrow}</div><h2>{feat_heading}</h2></div>
    <div class="{feat_class}">{feat}</div>
</div></section>
<section class="section alt"><div class="wrap">
    <div class="section-head"><div class="eyebrow">Browse</div><h2>Types of work</h2></div>
    <div class="cat-list">{cards}</div>
</div></section>
{extra}
"""
    page(side, f"{side}/index.html", f"{html.unescape(cfg['name'])}", 1, None, body)

# ---------------- CATEGORY ----------------
def category_entry(proj):
    slug, title, sub = pslug(proj), html.escape(ptitle(proj)), html.escape(psub(proj))
    href = f"../projects/{slug}.html"
    if is_real(proj):
        def meta_span(val):
            cls = ' class="ph-text"' if (val or "").startswith("Placeholder") else ""
            return f"<span{cls}>{html.escape(val)}</span>"
        if proj.get("youtube"):
            thumb = yt_lite(proj["youtube"], proj["poster"], proj["title"], 2)
        elif proj.get("thumb"):
            thumb = f'<a href="{href}" class="thumb real"><img src="../../{proj["thumb"]}" alt=""></a>'
        else:
            thumb = f'<a href="{href}" class="thumb ph-thumb"><span>Placeholder still</span></a>'
        meta = f'<div class="entry-meta">{meta_span(proj["year"])}{meta_span(proj["role"])}{meta_span(proj["tools"])}</div>'
        # YouTube cards already state the fact in the subtitle; don't repeat it.
        preview = "" if proj.get("youtube") else f'<p>{html.escape(proj["summary"])}</p>'
    else:
        thumb = f'<a href="{href}" class="thumb ph-thumb"><span>Placeholder still</span></a>'
        meta = '<div class="entry-meta"><span>Placeholder: year</span><span>Placeholder: role</span><span>Placeholder: tools</span></div>'
        preview = '<p class="ph-text">Placeholder: project story preview. A short paragraph on the goal, the challenge and how the edit solved it. The full write-up lives on the project page.</p>'
    return f"""<article class="entry">
      {thumb}
      <div class="entry-body">
        {meta}
        <h2><a href="{href}">{title}</a></h2><p class="entry-sub">{sub}</p>
        {preview}
        <a class="text-link" href="{href}">Read the full story →</a>
      </div></article>"""

def category(side, slug, name, blurb, projs):
    items = "".join(category_entry(proj) for proj in projs)
    extra = ""
    if slug == "ai-evaluation":
        extra = """<aside class="note-box"><div class="eyebrow">Side note</div><p>I've also written editing rules and critiques to train an AI editing assistant (Editron). That work is a small part of this section; the focus here is my own judgment of what makes a shot work or fail.</p></aside>"""
    body = page_head(side, 2, [name], name, blurb) + f"""<section class="section tight"><div class="wrap"><div class="entries">{items}</div>{extra}</div></section>"""
    page(side, f"{side}/{slug}/index.html", f"{html.unescape(name)} · {html.unescape(SIDES[side]['name'])}", 2, slug, body, script=True)

# ---------------- PROJECT ----------------
def yt_lite(yt_id, poster, title, depth):
    r = rel(depth)
    safe_title = html.escape(title)
    return (
        f'<div class="video-frame yt-lite" data-yt="{html.escape(yt_id)}" data-yt-title="{safe_title}">'
        f'<button type="button" class="yt-lite-btn" aria-label="Play {safe_title}">'
        f'<img src="{r}{poster}" alt="">'
        f'<span class="play" aria-hidden="true"></span>'
        f'</button></div>'
    )

def video_set_html(vids, depth):
    r = rel(depth)
    n = len(vids)
    items = []
    for v in vids:
        label = html.escape(v["label"])
        src_v = r + v["src"]
        poster = r + v["poster"]
        aspect = v.get("aspect") or "9/16"
        frame_cls = "vertical" if aspect == "9/16" else ("ar-4-3" if aspect == "4/3" else "landscape")
        cap = f"<figcaption>{label}</figcaption>" if n > 1 else ""
        items.append(
            f'<figure class="video-item">'
            f'<div class="video-frame {frame_cls}" data-slot="video">'
            f'<video src="{src_v}" poster="{poster}" controls preload="none" playsinline></video>'
            f'</div>{cap}</figure>'
        )
    aspects = [v.get("aspect") or "9/16" for v in vids]
    classes = [f"count-{n}"]
    if all(a == "16/9" for a in aspects) or (n == 1 and aspects[0] not in ("9/16", "4/3")):
        classes.append("landscape")
        if n == 1:
            classes.append("wide")
    return f'<div class="video-set {" ".join(classes)}">' + "".join(items) + "</div>"

def video_players(proj, depth):
    if proj.get("youtube"):
        return f'<div class="video-set count-1 wide">{yt_lite(proj["youtube"], proj["poster"], proj["title"], depth)}</div>'
    sections = proj.get("video_sections") or []
    if sections:
        blocks = []
        for sec in sections:
            heading = html.escape(sec["title"])
            vids = sec["videos"]
            verts = [v for v in vids if (v.get("aspect") or "9/16") == "9/16"]
            other = [v for v in vids if (v.get("aspect") or "9/16") != "9/16"]
            body = ""
            if verts and other:
                body = video_set_html(verts, depth) + video_set_html(other, depth)
            else:
                body = video_set_html(vids, depth)
            blocks.append(f'<div class="video-section"><h2>{heading}</h2>{body}</div>')
        return "".join(blocks)
    vids = proj.get("videos") or []
    if not vids:
        return video_slot("Placeholder: project video", "Swap in the embed or MP4 for this project")
    return video_set_html(vids, depth)


EDITRON_URL = "https://pillartheman1.github.io/engineering-portfolio/projects/editron/"

def editron_panel(proj, depth):
    vids = proj.get("editron_videos") or []
    if not vids:
        return ""
    r = rel(depth)
    items = []
    for v in vids:
        label = html.escape(v["label"])
        src_v = r + v["src"]
        poster = r + v["poster"]
        items.append(
            f'<figure class="video-item">'
            f'<div class="video-frame vertical" data-slot="video">'
            f'<video src="{src_v}" poster="{poster}" controls preload="none" playsinline></video>'
            f'</div><figcaption>{label}</figcaption></figure>'
        )
    n = len(vids)
    grid = f'<div class="video-set count-{n}">' + "".join(items) + "</div>"
    return (
        f'<section class="section tight"><div class="wrap">'
        f'<div class="editron-panel">'
        f'<h2>Edited by <a href="{EDITRON_URL}" target="_blank" rel="noopener">Editron</a></h2>'
        f'<p class="editron-lede">These cuts were edited by Editron, the AI editing system I built, from footage of the same Zaidi Jewelers work.</p>'
        f'{grid}'
        f'</div></div></section>'
    )

def stills_block(proj, depth):
    stills = proj.get("stills") or []
    if not stills:
        return ""
    r = rel(depth)
    figs = "".join(
        f'<figure><img src="{r}{s["src"]}" alt="{html.escape(s.get("cap") or "")}"><figcaption>{html.escape(s.get("cap") or "")}</figcaption></figure>'
        for s in stills
    )
    return f'<section class="block"><h2>Stills</h2><div class="steps stills">{figs}</div></section>'

def story_section(title, text, placeholder=False):
    if not text and not placeholder:
        return ""
    if not text:
        text = "Placeholder: this section will be filled in when I have more to say about it."
        placeholder = True
    return f'<section class="block"><h2>{title}</h2>{paras(text, placeholder)}</section>'

def project(side, cat, p, nxt):
    cslug, cname = cat[0], cat[1]
    slug, title, sub = pslug(p), ptitle(p), psub(p)
    nxt_slug, nxt_title = pslug(nxt), ptitle(nxt)
    if is_real(p):
        details = [
            ("Client", p.get("client") or ""),
            ("Category", cname),
            ("Role", p.get("role") or "Placeholder: role"),
            ("Tools", p.get("tools") or "Placeholder: tools"),
            ("Timeline", p.get("timeline") or "Placeholder: timeline"),
            ("Deliverables", p.get("deliverables") or "Placeholder: deliverables"),
            ("Year", p.get("year") or "Placeholder: year"),
        ]
        dl = []
        for label, value in details:
            if not value:
                continue
            if label == "Category":
                dl.append(f"<dt>{label}</dt><dd>{value}</dd>")
            else:
                dl.append(detail_dd(label, value))
        challenge = p.get("challenge")
        approach = p.get("approach")
        differently = p.get("differently")
        body = f"""<article class="project">
  {page_head(side, 2, [f'<a href="../{cslug}/">{cname}</a>', 'Project'], html.escape(title), html.escape(sub))}
  <section class="section tight"><div class="wrap">{video_players(p, 2)}</div></section>
  {editron_panel(p, 2)}
  <section class="section tight"><div class="wrap project-grid">
      <div class="prose story">
        {story_section("Overview", p.get("overview") or "")}
        {story_section("The challenge", challenge, placeholder=challenge is None)}
        {story_section("My approach", approach, placeholder=approach is None)}
        {stills_block(p, 2)}
        {story_section("What I'd do differently", differently, placeholder=differently is None)}
      </div>
      <aside class="details"><div class="details-card"><h3>Project details</h3><dl>
            {"".join(dl)}
      </dl></div></aside>
  </div></section>
  <section class="section tight"><div class="wrap pager"><a href="../{cslug}/">← All {cname}</a><a href="{nxt_slug}.html">Next project: {html.escape(nxt_title)} →</a></div></section>
</article>"""
        page(side, f"{side}/projects/{slug}.html", f"{title} · {html.unescape(SIDES[side]['name'])}", 2, cslug, body, script=True)
        return
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
  {page_head(side, 2, [f'<a href="../{cslug}/">{cname}</a>', 'Project'], title, sub)}
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
  <section class="section tight"><div class="wrap pager"><a href="../{cslug}/">← All {cname}</a><a href="{nxt_slug}.html">Next project: {html.escape(nxt_title)} →</a></div></section>
</article>"""
    page(side, f"{side}/projects/{slug}.html", f"{html.unescape(title)} · {html.unescape(SIDES[side]['name'])}", 2, cslug, body, script=True)


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
    body = page_head("media-co", 2, ["About"], "About the company", "Klabunde Media Co. is Daniel Klabunde's video production company.") + """
<section class="section tight"><div class="wrap about-grid">
    <div class="ph-thumb portrait"><span>Placeholder: company image</span></div>
    <div class="prose">
      <h2>The company</h2>
      <p class="ph-text">Placeholder: company story. When it started, what it makes, and the kinds of businesses it works with (described generally, no client names).</p>
      <h2>How we work</h2>
      <p class="ph-text">Placeholder: approach, communication, review, and how ongoing work is handled.</p>
      <h2>Who's behind it</h2>
      <p>Klabunde Media Co. is run by Daniel Klabunde. <a class="text-link" href="../../daniel/">See Daniel's personal work →</a></p>
    </div>
</div></section>"""
    page("media-co", "media-co/about/index.html", "About · Klabunde Media Co.", 2, "about", body)

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
            project(side, c, p, nx); n += 1
    daniel_about(); media_pages(); n += 2
    print("built", n, "pages +", len(OLD), "redirects")
