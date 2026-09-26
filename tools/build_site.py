"""Build the hosted Synecdoche GDD for keepoffthetrack.co.uk.

The GDD is edited in the Unity repo (Docs/GDD/index.html). This script copies
that full version into synecdoche/index.html and adds the Keep Off The Track
studio credit (masthead strip at the top, credit line at the bottom). The
credit exists only on the hosted copy, never in the submitted GDD.

Run from anywhere:  python "tools/build_site.py"
Then commit and push this repo to update the live site.
"""
from pathlib import Path

site = Path(__file__).resolve().parent.parent
source = Path(r"C:\Users\jackb\Documents\Game Dev\ModeratorPOC\Quiz UI\Docs\GDD\index.html")
target = site / "synecdoche" / "index.html"

html = source.read_text(encoding="utf-8")

studio_css = """
<style>
/* Keep Off The Track studio credit (hosted copy only) */
.studio-strip{max-width:1180px;margin:0 auto;display:flex;flex-wrap:wrap;align-items:center;gap:6px 14px;padding-block:10px 4px;text-decoration:none;color:var(--muted)}
.studio-strip img{display:block;height:34px;width:auto;image-rendering:pixelated;border-radius:2px}
.studio-strip span{font:600 11.5px/1.3 var(--mono);letter-spacing:.08em;text-transform:uppercase}
.studio-strip:hover span{color:var(--ink)}
.studio-credit{font-size:13.5px;color:var(--muted);padding:4px 4px 0}
.studio-credit a{color:var(--accent-ink)}
@media print{ .studio-strip,.studio-credit{display:none!important} }
</style>
"""

strip = ('<a class="studio-strip" href="../" aria-label="Keep Off The Track, back to the studio homepage">'
         '<img src="../assets/keep-off-the-track-masthead.png" '
         'srcset="../assets/keep-off-the-track-masthead.png 1x, ../assets/keep-off-the-track-masthead@2x.png 2x" '
         'width="183" height="34" alt="Keep Off The Track">'
         '<span>A Keep Off The Track game</span></a>\n')
credit = '    <p class="studio-credit">Synecdoche is a <a href="../">Keep Off The Track</a> game.</p>\n'

assert html.count('</head>') == 1 and html.count('<div class="appbar">') == 1 and html.count('  </main>') == 1
html = html.replace('</head>', studio_css + '</head>', 1)
html = html.replace('<div class="appbar">', strip + '<div class="appbar">', 1)
html = html.replace('  </main>', credit + '  </main>', 1)
html = html.replace('<title>Synecdoche GDD</title>', '<title>Synecdoche GDD · Keep Off The Track</title>', 1)

target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(html, encoding="utf-8")
print(f"Wrote {target.relative_to(site)} from {source}")
