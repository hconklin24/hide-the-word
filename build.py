"""Bundle index.html + web.js into a single shareable file: dist/hide-the-word.html"""
from pathlib import Path

root = Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")
data = (root / "web.js").read_text(encoding="utf-8")

tag = '<script src="web.js"></script>'
assert tag in html, "web.js script tag not found in index.html"
html = html.replace(tag, "<script>\n" + data.replace("</script", "<\\/script") + "</script>")

out = root / "dist" / "hide-the-word.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print(f"Wrote {out} ({out.stat().st_size / 1e6:.1f} MB)")
