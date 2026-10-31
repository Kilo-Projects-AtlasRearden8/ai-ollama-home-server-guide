"""Build the static HTML site from the Markdown manual in docs/.

Reads docs/*.md, converts each page with Python-Markdown, wraps it in a
shared template, and writes site/*.html plus assets/.
"""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
ASSETS = SITE / "assets"

PAGES = [
    ("00-welcome.md", "index.html", "Welcome — Ollama Home Server Guide"),
    ("01-install.md", "install.html", "1. Install Ollama"),
    ("02-autostart.md", "autostart.html", "2. Auto-start on Boot"),
    ("03-access.md", "access.html", "3. Access from Other Devices"),
    ("04-models.md", "models.html", "4. Pull and Run Models"),
    ("05-privacy.md", "privacy.html", "5. Keep Chats Private"),
    ("06-checklist.md", "checklist.html", "6. Printable Setup Checklist"),
]

NAV = [
    ("index.html", "Welcome"),
    ("install.html", "Install"),
    ("autostart.html", "Auto-start"),
    ("access.html", "Access"),
    ("models.html", "Models"),
    ("privacy.html", "Privacy"),
    ("checklist.html", "Checklist"),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Ollama Home Server Guide</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="wrapper">
    <a class="brand" href="index.html">Ollama Home Server Guide</a>
    <p class="dek">A beginner-friendly, local-first manual for running Ollama as a headless home server.</p>
  </div>
</header>

<nav class="site-nav">
  <div class="wrapper">
    <ul>
      {nav_items}
    </ul>
    <p class="nav-credit">Published by <strong>Asdale Dynamics, LLC</strong> &middot; Indiana, formed October 2026</p>
  </div>
</nav>

<main class="wrapper">
  <article class="page">
    <a class="back" href="index.html">&larr; Back to guide</a>
    <h1>{h1}</h1>
    {body}
  </article>
</main>

<footer class="site-footer">
  <div class="wrapper">
    <p>Published by <strong>Asdale Dynamics, LLC</strong> &mdash; beginner-friendly AI education, books, and practical tools.</p>
    <p>Copyright (c) 2026 Asdale Dynamics, LLC. MIT Licensed. See LICENSE.</p>
    <p><a href="https://dylanasdale.github.io">dylanasdale.github.io</a> &middot; <a href="index.html">Read the full guide</a></p>
  </div>
</footer>
</body>
</html>
"""

CSS = """/* Ollama Home Server Guide — Asdale Dynamics, LLC */
:root {
  --ink: #1f2937;
  --muted: #6b7280;
  --accent: #0f6f4b;
  --accent-soft: #e7f7ee;
  --bg: #ffffff;
  --line: #e5e7eb;
  --radius: 8px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  color: var(--ink);
  line-height: 1.7;
  background: #f9fafb;
}
.wrapper { max-width: 720px; margin: 0 auto; padding: 0 20px; }

/* Header */
.site-header { background: var(--ink); color: #fff; padding: 32px 0 24px; }
.site-header .wrapper { display: grid; gap: 8px; }
.brand {
  color: #fff;
  text-decoration: none;
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -0.02em;
}
.brand:hover { color: #bfdbfe; }
.dek { color: #cbd5e1; margin: 0; font-size: 0.95rem; }

/* Nav */
.site-nav { background: #fff; border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 10; }
.site-nav ul {
  list-style: none;
  margin: 0; padding: 0;
  display: flex; gap: 10px; flex-wrap: wrap;
}
.site-nav a {
  display: block; padding: 8px 14px; border-radius: var(--radius);
  text-decoration: none; color: var(--ink); font-weight: 600; font-size: 0.9rem;
  border: 1px solid transparent;
}
.site-nav a:hover { background: #f3f4f6; border-color: var(--line); }
.site-nav a.active { background: var(--accent-soft); color: var(--accent); border-color: var(--accent); }
.nav-credit { margin: 10px 0 0; color: var(--muted); font-size: 0.8rem; }

/* Main */
main { padding: 40px 0; }
.page a.back {
  color: var(--accent); text-decoration: none; font-size: 0.85rem; margin-bottom: 12px; display: inline-block;
}
.page a.back:hover { text-decoration: underline; }
.page h1 { font-size: 1.75rem; margin: 0 0 6px; line-height: 1.25; }
.page h2 { font-size: 1.3rem; margin: 32px 0 10px; border-bottom: 1px solid var(--line); padding-bottom: 6px; }
.page h3 { font-size: 1.1rem; margin: 24px 0 8px; color: var(--accent); }
.page p { margin: 0 0 14px; }
.page ul, .page ol { margin: 4px 0 16px; padding-left: 24px; }
.page li { margin: 0 0 6px; }
.page code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.875em; background: #f3f4f6; padding: 2px 6px; border-radius: 4px; color: #9333ea;
}
.page pre {
  background: #0f172a; color: #e2e8f0; padding: 16px; border-radius: var(--radius);
  overflow-x: auto; margin: 16px 0;
}
.page pre code { background: transparent; color: inherit; padding: 0; font-size: 0.9rem; }
.page table {
  width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 0.9rem;
}
.page th, .page td { border: 1px solid var(--line); padding: 8px 10px; text-align: left; }
.page th { background: #f3f4f6; font-weight: 700; }
.page blockquote {
  border-left: 4px solid var(--accent); background: var(--accent-soft);
  padding: 12px 16px; margin: 16px 0; border-radius: 0 var(--radius) var(--radius) 0;
}
.page hr { border: none; border-top: 1px solid var(--line); margin: 28px 0; }

/* Checklist */
.page ul.tasks, .page ul.task-list { list-style: none; padding-left: 0; }
.page ul.tasks li, .page ul.task-list li { display: flex; gap: 10px; align-items: flex-start; margin: 0 0 12px; }
.page ul.tasks input[type=checkbox], .page ul.task-list input[type=checkbox] { width: 18px; height: 18px; margin-top: 2px; cursor: pointer; accent-color: var(--accent); }

/* Callouts */
.callout {
  border-radius: var(--radius); padding: 14px 18px; margin: 18px 0; font-size: 0.92rem;
}
.callout.warn { background: #fef3c7; border-left: 4px solid #d97706; color: #78350f; }
.callout.ok { background: #dcfce7; border-left: 4px solid #15803d; color: #14532d; }

/* Footer */
.site-footer { background: var(--ink); color: #e5e7eb; padding: 32px 0; margin-top: 60px; }
.site-footer a { color: #93c5fd; text-decoration: underline; }
.site-footer p { margin: 0 0 8px; font-size: 0.85rem; }

/* Print */
@media print {
  body { background: #fff; color: #000; }
  .site-header, .site-nav, .site-footer, .back, nav { display: none !important; }
  .page h2 { page-break-after: avoid; border-bottom: 1px solid #000; }
  .page a::after { content: " (" attr(href) ")"; font-size: 0.8rem; color: #000; }
  .page a.back::after { content: ""; }
  .callout { border: 1px solid #000; background: #fff !important; }
  pre { white-space: pre-wrap; word-wrap: break-word; }
}

/* Small screens */
@media (max-width: 600px) {
  .wrapper { padding: 0 14px; }
  .page h1 { font-size: 1.4rem; }
}
"""

JS = """// Ollama Home Server Guide — minor enhancements
document.addEventListener('DOMContentLoaded', function () {
  // Highlight the current page in the nav
  var path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.site-nav a').forEach(function (link) {
    if (link.getAttribute('href') === path) {
      link.classList.add('active');
    }
  });
  // Print shortcut hint
  if (window.matchMedia && window.matchMedia('print').matches) return;
  var hint = document.createElement('p');
  hint.className = 'print-hint';
  hint.style.cssText = 'font-size:0.8rem;color:#6b7280;text-align:center;margin-top:8px;';
  hint.textContent = 'Tip: use your browser Print command for a printable checklist.';
  var checklist = document.querySelector('.page ul.tasks');
  if (checklist) checklist.after(hint);
});
"""

MD_TO_HTML = {md_file: html_file for md_file, html_file, _ in PAGES}
MD_LINK = re.compile(r"\]\(([^)]+?)\.md\)")


def rewrite_md_links(md_text: str) -> str:
    """Rewrite [text](file.md) cross-references to [text](file.html) for the HTML site."""

    def repl(match):
        source = match.group(1) + ".md"
        target = MD_TO_HTML.get(source, match.group(1) + ".html")
        return "](" + target + ")"

    return MD_LINK.sub(repl, md_text)


TASK_ITEM = re.compile(r"^(\s*[-*+])\s+\[( |x)\] ", re.MULTILINE)


def render_task_items(md_text: str) -> str:
    """Convert markdown task-list items into HTML with checkbox inputs."""

    def repl(match):
        marker = match.group(1)
        checked = match.group(2).strip() == "x"
        checkbox = (
            '<input type="checkbox" class="task-list-item-checkbox" disabled'
            + (" checked" if checked else "")
            + ">"
        )
        return f'{marker} {checkbox} '

    return TASK_ITEM.sub(repl, md_text)


def md_to_html(md_text: str) -> str:
    md_text = render_task_items(md_text)
    return markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "toc", "attr_list"],
        extension_configs={
            "toc": {"permalink": True, "toc_depth": "2-3"},
            "attr_list": {},
        },
    )

def build() -> None:
    SITE.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)

    (ASSETS / "style.css").write_text(CSS, encoding="utf-8")
    (ASSETS / "script.js").write_text(JS, encoding="utf-8")

    nav_items = "\n".join(
        f'      <li><a href="{href}"{" class=\"active\"" if i == 0 else ""}>{text}</a></li>'
        for i, (href, text) in enumerate(NAV)
    )

    for md_file, html_file, title in PAGES:
        source = (DOCS / md_file).read_text(encoding="utf-8")
        # Strip the leading H1 from the markdown body so the template h1 stays clean
        body_md = source
        first_line = source.strip().splitlines()[0] if source.strip() else ""
        if first_line.startswith("# "):
            h1 = first_line[2:].strip()
            body_md = "\n".join(source.splitlines()[1:]).lstrip("\n")
        else:
            h1 = title
        body_md = rewrite_md_links(body_md)
        body_html = md_to_html(body_md)
        page = TEMPLATE.format(title=title, h1=h1, nav_items=nav_items, body=body_html)
        (SITE / html_file).write_text(page, encoding="utf-8")
        print(f"wrote site/{html_file}")

if __name__ == "__main__":
    build()
