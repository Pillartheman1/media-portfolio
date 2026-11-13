"""Home sections and dedicated pages for shot listing / pre-production.

Mockups are original, illustrative examples — not the I Deleted Instagram
Notion workflow, and not tied to any named client.
"""
import html


def esc(s):
    return html.escape(s, quote=True)


# --- Example data: DK personal narrative, dusk departure -------------------
# Columns follow a working shot list: number, scene/set, description,
# shot size, angle, lens, movement, lighting, duration, A/B-roll.

DK_ROWS = [
    dict(n="01", scene="Porch, last light",
         desc="I stand in the doorway, one hand on the frame, looking out at the street. Don't start walking yet.",
         size="MS", angle="Eye-level, slightly off-axis, the door as a second frame",
         lens="35mm", move="Static, locked off on sticks",
         light="Golden hour, sun just under the roofline; warm spill on the left cheek, porch in open shade",
         dur="4s", roll="A-roll"),
    dict(n="02", scene="Front steps",
         desc="Feet take the first two steps down and pause on the third.",
         size="CU", angle="High angle, looking down the steps",
         lens="50mm", move="Tilt down with the first step, then hold",
         light="Same last light, no fill; let the shadows go",
         dur="3s", roll="B-roll"),
    dict(n="03", scene="Sidewalk under the trees",
         desc="Walking and talking, eyeline just off-lens — not a straight vlog hold.",
         size="MS", angle="Eye-level, beside me, leading room ahead",
         lens="28mm", move="Gimbal, match pace; a gentle push-in over the last line",
         light="Dappled late light; watch the flicker through the leaves so it doesn't strobe the cut",
         dur="8s", roll="A-roll"),
    dict(n="04", scene="Corner, looking back",
         desc="I stop and look back at the house. Hold the look longer than is comfortable.",
         size="WS", angle="Across the street, house and figure in the same frame",
         lens="35mm", move="Static; start on the house, I walk into frame and stop",
         light="Sky still holding a little color; the house starting to go to silhouette",
         dur="6s", roll="B-roll"),
    dict(n="05", scene="Kitchen window, later",
         desc="Through the glass: a kettle, then my face entering the reflection.",
         size="CU", angle="Outside looking in, slightly below eye-level",
         lens="50mm", move="Slow rack from the kettle to the reflection",
         light="Interior practicals only; the window as a black frame, no street spill on the glass",
         dur="5s", roll="B-roll"),
    dict(n="06", scene="Kitchen table",
         desc="Sitting down with the cup. I start the next line only after the chair is still.",
         size="MS", angle="Profile, table edge along the bottom of the frame",
         lens="35mm", move="Static, sticks",
         light="Warm practical above the table, soft; keep the far wall a stop down",
         dur="7s", roll="A-roll"),
    dict(n="07", scene="Hands, the cup",
         desc="Both hands around the cup, steam catching the light. No face.",
         size="ECU", angle="Level with the rim, slight three-quarter",
         lens="100mm", move="Static; a short push-in only if the steam holds",
         light="The practical as a single source; a small edge to separate the steam from the wall",
         dur="3s", roll="B-roll"),
    dict(n="08", scene="Porch again, night",
         desc="The same doorway as shot 01, now dark. The streetlamp is the only key. Empty frame for a beat, then I step in and close the door.",
         size="MS", angle="Same axis as 01, for continuity",
         lens="35mm", move="Static, locked off on the same marks",
         light="Cool streetlamp from the right; no porch practical",
         dur="6s", roll="A-roll"),
]

DK_STORYBOARD = [
    dict(n="01", title="The doorway", note="MS · 35mm · static", tone="warm", subject="door"),
    dict(n="02", title="The steps", note="CU · 50mm · tilt down", tone="warm", subject="ground"),
    dict(n="03", title="Under the trees", note="MS · 28mm · gimbal push-in", tone="dusk", subject="walk"),
    dict(n="04", title="Looking back", note="WS · 35mm · walk-in, hold", tone="dusk", subject="wide"),
    dict(n="05", title="The window", note="CU · 50mm · rack focus", tone="night", subject="glass"),
]

DK_BREAKDOWN = dict(
    line="I left the house later than I meant to, and the light was already going.",
    shots=[
        ("01", "MS, static, 35mm", "The line begins here, still in the doorway, before any walk."),
        ("02", "CU, tilt down, 50mm", "The first steps; no dialogue, just the move out of the house."),
        ("03", "MS, gimbal push-in, 28mm", "The rest of the line, walking, eyeline off-lens."),
        ("04", "WS, static, 35mm", "A hold after the line, looking back, so the thought can land."),
    ],
)

# --- Example data: KMC generic luxury product (jewelry + tailoring) --------
# No client names.

KMC_ROWS = [
    dict(n="01", scene="Atelier table, cloth roll",
         desc="A roll of dark wool unrolls toward camera. A hand enters from the right to stop it.",
         size="WS", angle="Slight high angle, table edge parallel to the bottom of the frame",
         lens="35mm", move="Slow dolly in as the cloth settles",
         light="Soft north window; no hard edge on the wool; a warm practical deep in the background",
         dur="6s", roll="B-roll"),
    dict(n="02", scene="The same table",
         desc="Macro of the weave, then a chalk line. Hold until the chalk lifts.",
         size="ECU", angle="Top-down, chalk line on a diagonal",
         lens="100mm macro", move="Static, then a short rack from the weave to the chalk tip",
         light="Same window; flag the practical so the texture holds",
         dur="4s", roll="B-roll"),
    dict(n="03", scene="Fitting area",
         desc="A jacket is settled onto the shoulders. Hands smooth the lapel and rest.",
         size="MS", angle="Three-quarter back, over the fitter's shoulder",
         lens="50mm", move="Gentle gimbal arc left to right, stop on the lapel",
         light="Window key, warm practicals; no shiny hotspot on the wool",
         dur="5s", roll="B-roll"),
    dict(n="04", scene="Jewelry table, black cloth",
         desc="A ring is placed into the frame. The fingers leave. Hold on the stone.",
         size="CU", angle="Low, across the cloth, ring slightly left of center",
         lens="90mm macro", move="Push-in, ending tight on the stone",
         light="Large soft key, a hard kicker for the facet, black flags around the table",
         dur="4s", roll="B-roll"),
    dict(n="05", scene="The stone",
         desc="ECU of a single facet catching the kicker. No hand, no setting.",
         size="ECU", angle="Dead-on the table plane, stone centered",
         lens="100mm macro", move="Static; a very slow rack across the facet if the sparkle holds",
         light="Kicker only, barely any fill; let the cloth fall to black",
         dur="3s", roll="B-roll"),
    dict(n="06", scene="Hands at the bench",
         desc="A needle pulls through the lapel. The other hand keeps the cloth taut.",
         size="CU", angle="Oblique, at bench height, looking along the stitch line",
         lens="50mm", move="Static, sticks; no hunting",
         light="Window as a soft side key; a small bounce for the fingers, nothing on the background",
         dur="5s", roll="B-roll"),
    dict(n="07", scene="Showroom, late afternoon",
         desc="The finished jacket on a stand, then a hand brings the ring into the lower foreground, out of focus, and I rack to it.",
         size="MS to CU", angle="Eye-level, stand slightly right, ring entering lower left",
         lens="50mm", move="Static body, rack from the jacket to the ring",
         light="Late window, warm; no extra kick on the metal until it is sharp",
         dur="6s", roll="B-roll"),
    dict(n="08", scene="Atelier, end of day",
         desc="Wide of the empty table, cloth folded, the window going blue. Hold, then a slow fade.",
         size="WS", angle="From the doorway, table in the lower third, window in the upper left",
         lens="35mm", move="Static, locked off",
         light="Whatever is left of the window, mixed with the first practicals; don't add day",
         dur="5s", roll="B-roll"),
]

KMC_STORYBOARD = [
    dict(n="01", title="The cloth", note="WS · 35mm · dolly in", tone="atelier", subject="table"),
    dict(n="02", title="Weave and chalk", note="ECU · 100mm · rack", tone="atelier", subject="macro"),
    dict(n="03", title="The fitting", note="MS · 50mm · gimbal arc", tone="atelier", subject="figure"),
    dict(n="04", title="The ring", note="CU · 90mm · push-in", tone="jewel", subject="macro"),
    dict(n="05", title="The facet", note="ECU · 100mm · static", tone="jewel", subject="spark"),
]

KMC_BREAKDOWN = dict(
    line="The work is in the cloth, and in the last thing you put on.",
    shots=[
        ("01", "WS, dolly in, 35mm", "The cloth arrives; the line can start here, under the rumble of the roll."),
        ("02", "ECU, rack, 100mm", "A cut in for the weave and the chalk, no dialogue needed."),
        ("03", "MS, gimbal arc, 50mm", "The jacket finds the shoulders; the first half of the line sits here."),
        ("04–05", "CU / ECU, macro", "The ring, then the facet. The second half of the line, quieter."),
    ],
)

COLS = [
    ("n", "Shot #"),
    ("scene", "Scene / set"),
    ("desc", "Description"),
    ("size", "Shot size"),
    ("angle", "Angle"),
    ("lens", "Lens"),
    ("move", "Camera movement"),
    ("light", "Lighting / time of day"),
    ("dur", "Duration"),
    ("roll", "A / B-roll"),
]

HOME_COLS = ["n", "scene", "desc", "size", "move", "lens"]


def _table(rows, cols=None, caption="Example shot list"):
    cols = cols or [c[0] for c in COLS]
    labels = {k: lab for k, lab in COLS}
    head = "".join(f"<th>{esc(labels[k])}</th>" for k in cols)
    body = []
    for r in rows:
        tds = "".join(f"<td>{esc(r.get(k) or '')}</td>" for k in cols)
        body.append(f"<tr>{tds}</tr>")
    cap = f"<caption>{esc(caption)}</caption>"
    return (
        f'<div class="sl-table-wrap"><table class="sl-table">{cap}'
        f"<thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"
    )


def _cards(rows, caption="Example shot list"):
    items = []
    for r in rows:
        meta = (
            f'<div class="sl-card-meta"><span>{esc(r["size"])}</span>'
            f'<span>{esc(r["lens"])}</span><span>{esc(r["move"])}</span>'
            f'<span>{esc(r["roll"])}</span><span>{esc(r["dur"])}</span></div>'
        )
        items.append(
            f'<article class="sl-card"><div class="sl-card-top">'
            f'<span class="sl-num">{esc(r["n"])}</span>'
            f'<span class="sl-scene">{esc(r["scene"])}</span></div>'
            f'<p class="sl-desc">{esc(r["desc"])}</p>'
            f'<p class="sl-angle">{esc(r["angle"])}. {esc(r["light"])}</p>'
            f"{meta}</article>"
        )
    return (
        f'<div class="sl-cards"><p class="sl-example-label">{esc(caption)}</p>'
        f'{"".join(items)}</div>'
    )


def _storyboard(frames, caption="Example shot list — storyboard"):
    figs = []
    for f in frames:
        figs.append(
            f'<figure class="sl-frame tone-{esc(f["tone"])} subject-{esc(f["subject"])}">'
            f'<div class="sl-frame-art" aria-hidden="true">'
            f'<span class="sl-thirds"></span><span class="sl-subject"></span>'
            f'<span class="sl-frame-num">{esc(f["n"])}</span></div>'
            f'<figcaption><strong>{esc(f["title"])}</strong><span>{esc(f["note"])}</span></figcaption>'
            f"</figure>"
        )
    return (
        f'<div class="sl-board"><p class="sl-example-label">{esc(caption)}</p>'
        f'<div class="sl-board-row">{"".join(figs)}</div></div>'
    )


def _breakdown(data, caption="Example — script to shots"):
    items = "".join(
        f"<li><span class=\"sl-bd-shot\">{esc(n)}</span> "
        f"<span class=\"sl-bd-tech\">{esc(tech)}</span>"
        f"<p>{esc(note)}</p></li>"
        for n, tech, note in data["shots"]
    )
    return (
        f'<div class="sl-break"><p class="sl-example-label">{esc(caption)}</p>'
        f'<blockquote class="sl-script-line"><p>{esc(data["line"])}</p></blockquote>'
        f'<ol class="sl-break-list">{items}</ol></div>'
    )


def _example_block(rows, frames, breakdown, n_home=None):
    show = rows[:n_home] if n_home else rows
    cap = "Example shot list" + (f" — first {n_home} of {len(rows)} setups" if n_home else "")
    table_cols = HOME_COLS if n_home else None
    return (
        _table(show, table_cols, cap)
        + _cards(show, cap)
        + _storyboard(frames)
        + _breakdown(breakdown)
    )


def home_section(side, depth=1):
    """Semi-prominent mid-page section with a short write-up and a compact mockup."""
    if side == "daniel":
        copy = (
            "<p>I write a hyper-detailed shot list and a script in Notion for every project, "
            "personal and client. Each line is a precise visual description: shot composition "
            "and framing, lens choice, camera movement, lighting, and how the shot should sit "
            "in the cut.</p>"
            "<p>That written direction is what I shoot from, and what I use afterward to evaluate "
            "the footage against a written spec — whether the continuity holds, and whether the "
            "pacing still has the temporal coherence I planned on the page.</p>"
        )
        rows, frames, br = DK_ROWS, DK_STORYBOARD, DK_BREAKDOWN
        href = "shot-listing/"
    else:
        copy = (
            "<p>I write a hyper-detailed shot list and a script in Notion for every project, "
            "including the commercial work on this side of the site. For a product film that "
            "means describing the shot composition, the lens, the move, and the light before "
            "I shoot, in language precise enough to work from and to judge the footage by.</p>"
            "<p>The mockup here is an example shot list for a generic luxury-brand product "
            "film — cloth, a fitting, a piece of jewelry — not a client from this site.</p>"
            "<p>I also publish long-form videos that break down cinematography, sometimes "
            "shot by shot: a visual evaluation of composition, lighting, and movement, "
            "describing the footage precisely. "
            '<a class="text-link" href="projects/kmc-in-house.html#cinematography-breakdowns">'
            "See the cinematography breakdowns →</a></p>"
        )
        rows, frames, br = KMC_ROWS, KMC_STORYBOARD, KMC_BREAKDOWN
        href = "shot-listing/"
    # Home: table + storyboard only (keep the script breakdown for the dedicated page)
    teaser = _table(rows[:4], HOME_COLS, "Example shot list") + _cards(rows[:4], "Example shot list")
    teaser += _storyboard(frames[:4], "Example shot list — storyboard")
    return f"""<section id="shot-listing" class="section sl-home">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Pre-production</div><h2>Shot listing</h2></div>
    <div class="sl-home-copy prose">{copy}
      <p><a class="text-link" href="{esc(href)}">Read the process and see a fuller example →</a></p>
    </div>
    <div class="sl-home-example">{teaser}</div>
  </div>
</section>"""


def page_body(side, page_head):
    """Full dedicated page."""
    if side == "daniel":
        lede = (
            "How I write a shot list and a script before I shoot, and how I use that page "
            "once the footage is in."
        )
        h1 = "Shot listing"
        crumbs = ["Shot listing"]
        copy = """
        <p>Before I pick up a camera I translate the creative intent of a piece into a written shot list and a script. I do this in Notion, for every project: the personal work on this side of the site, and the client work at <a class="text-link" href="../../media-co/">Klabunde Media Co.</a> The lists are prompt-ready shot descriptions: a precise visual description of each setup — framing, lens, movement, light, duration — written with enough attention to detail that I can execute it without guessing, and so the footage can be checked against what was planned.</p>
        <p>Visual storytelling, for me, starts on that page. A list is where shot composition gets decided, where camera movement is chosen for a reason, and where I can see whether a sequence will hold together. After the shoot I come back to the same document to evaluate the footage against a written spec: does the continuity hold, does the pacing match what I wrote, and do the shots still have temporal coherence when they sit next to each other.</p>
        <p>The mockups below are an example shot list for a short personal narrative — a dusk departure, then a quiet return — not a project from this site. They show the level of detail I write to. For a look at a real pre-production file, including the full shot list and script, see <a class="text-link" href="../projects/i-deleted-instagram.html#pre-production">I deleted Instagram</a>. On the company side I also publish long-form cinematography breakdowns, including shot-by-shot visual evaluation of footage; those live on <a class="text-link" href="../../media-co/projects/kmc-in-house.html#cinematography-breakdowns">Klabunde Media Co. — Cinematography breakdowns</a>.</p>
        """
        rows, frames, br = DK_ROWS, DK_STORYBOARD, DK_BREAKDOWN
    else:
        lede = (
            "How I write a shot list and a script for commercial work, before anyone is in front of the camera."
        )
        # "anyone is in front of the camera" is generic, not inventing a crew. OK.
        h1 = "Shot listing"
        crumbs = ["Shot listing"]
        copy = """
        <p>I write a hyper-detailed shot list and a script in Notion for every project, including the commercial and brand work on this side of the site. The point of the page is to turn creative intent into precise written direction: a precise visual description of shot composition and framing, what the lens is doing, how the camera moves, and what the light is doing at that time of day, written with the same attention to detail I want in the final frame.</p>
        <p>On a product film that written spec is what I shoot from, and what I use afterward to evaluate the footage — checking continuity from setup to setup, whether the pacing of a process sequence still holds, and whether the shots have temporal coherence when they are cut together. Visual storytelling here is often about material and light; the descriptions are written so they can be followed without a conversation filling in the gaps.</p>
        <p>The mockups below are an example shot list for a generic luxury-brand product film, mixing a tailoring process with jewelry macro work. They are not a record of a client from this site, and they do not use a client's name.</p>
        <p>For examples of how I look at footage shot by shot after the fact — composition, lens, movement, lighting, and why a shot works — see <a class="text-link" href="../projects/kmc-in-house.html#cinematography-breakdowns">Cinematography breakdowns</a>, a set of long-form videos from the Klabunde Media Co. YouTube channel.</p>
        """
        rows, frames, br = KMC_ROWS, KMC_STORYBOARD, KMC_BREAKDOWN

    body = page_head(side, 2, crumbs, h1, lede) + f"""
<section class="section tight"><div class="wrap sl-page">
    <div class="prose sl-page-copy">{copy}</div>
    <h2>Example shot list</h2>
    <p class="sl-col-note">Shot size is written ECU / CU / MS / WS. Movement, lens, and light are written in the same row as the action, so the description stays prompt-ready.</p>
    {_table(rows)}
    {_cards(rows)}
    <h2>Storyboard</h2>
    <p class="sl-col-note">A frame strip for the same example, annotated with size, lens, and movement. The frames are illustrative, not production stills.</p>
    {_storyboard(frames)}
    <h2>Script to shots</h2>
    <p class="sl-col-note">One line from a script, mapped to the setups that cover it.</p>
    {_breakdown(br)}
</div></section>"""
    return body


def footer_items(side, nav):
    """Append a Shot listing link to the footer Explore list, not the primary nav."""
    return list(nav) + [("shot-listing", "Shot listing")]
