"""Render the pre-production panel for the I deleted Instagram project page.
Shot list and script text are quoted from Daniel's public Notion workflow, unedited."""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT, "_tools", "data", "i-deleted-instagram-prepro.json")
NOTION_URL = "https://luck-column-b39.notion.site/I-Deleted-Instagram-You-Probably-Should-Too-f4ef8db3e5ec4d1489fa90eb7f2728a5"


def _data():
    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def shotlist_table(shots, caption=None):
    head = "<th>Time</th><th>Set/shot</th><th>Angle</th><th>Camera</th><th>Type</th><th>Code</th>"
    rows = []
    for s in shots:
        rows.append(
            "<tr>"
            f"<td>{html.escape(s.get('time') or '')}</td>"
            f"<td>{html.escape(s.get('set_shot') or '')}</td>"
            f"<td>{html.escape(s.get('angle') or '')}</td>"
            f"<td>{html.escape(s.get('camera') or '')}</td>"
            f"<td>{html.escape(s.get('type') or '')}</td>"
            f"<td>{html.escape(str(s.get('code') or ''))}</td>"
            "</tr>"
        )
    cap = f"<caption>{html.escape(caption)}</caption>" if caption else ""
    return (
        '<div class="shotlist-wrap"><table class="shotlist">'
        f"{cap}<thead><tr>{head}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>"
    )


def preproduction_panel(proj):
    if (proj.get("slug") if isinstance(proj, dict) else None) != "i-deleted-instagram":
        return ""
    data = _data()
    shots = data["shots"]
    excerpt_n = set(data["excerpt_n"])
    excerpt = [s for s in shots if s["n"] in excerpt_n]
    script_html = "".join(f"<p>{html.escape(line)}</p>" for line in data["script_excerpt"])
    n = len(shots)
    k = len(excerpt)
    notion = data.get("source") or NOTION_URL
    href = html.escape(notion, quote=True)
    return f"""<section id="pre-production" class="section tight prepro-section"><div class="wrap">
    <div class="prepro-panel">
      <div class="eyebrow">Pre-production</div>
      <h2>Shot list and script</h2>
      <p class="prepro-lede">I write a detailed shot list and script for every project, personal and client. This is the pre-production I put together for this video: {k} shots from the list of {n}, and the intro from the script. The wording below is from the original notes, unedited.</p>
      <p class="prepro-link"><a class="text-link" href="{href}" target="_blank" rel="noopener">View the full Notion workflow</a></p>
      <h3>Shot list</h3>
      {shotlist_table(excerpt, caption=f"{k} of {n} shots")}
      <details class="shotlist-more">
        <summary>See all {n} shots</summary>
        {shotlist_table(shots, caption=f"Complete shot list, {n} shots")}
      </details>
      <h3>Script, intro</h3>
      <blockquote class="script-excerpt">{script_html}</blockquote>
      <p class="prepro-link"><a class="text-link" href="{href}" target="_blank" rel="noopener">View the full Notion workflow</a></p>
    </div>
  </div></section>"""
