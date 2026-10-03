"""Bundle the app into a single shareable file: dist/hide-the-word.html

Inlines theme.css, vendor/material.js (Material Web components) and web.js (WEB text) into index.html.
Fonts still load from Google Fonts when online and fall back to system fonts offline.
"""
import re
from pathlib import Path

root = Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")
read = lambda name: (root / name).read_text(encoding="utf-8").replace("</script", "<\\/script")

replacements = {
    '<link rel="stylesheet" href="theme.css">': "<style>\n" + read("theme.css") + "</style>",
    '<script src="web.js"></script>': "<script>\n" + read("web.js") + "</script>",
}
# The vendor script carries a ?v= cache-busting hash, so match it with a pattern.
html, n = re.subn(r'<script type="module" src="vendor/material\.js(\?v=\w+)?"></script>',
                  lambda _: '<script type="module">\n' + read("vendor/material.js") + "</script>", html)
assert n == 1, "vendor/material.js script tag not found in index.html"
for tag, inline in replacements.items():
    assert tag in html, f"{tag} not found in index.html"
    html = html.replace(tag, inline)

out = root / "dist" / "hide-the-word.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print(f"Wrote {out} ({out.stat().st_size / 1e6:.1f} MB)")
