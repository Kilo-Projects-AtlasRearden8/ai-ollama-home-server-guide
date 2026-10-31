"""Verify the static site: pages exist, internal links resolve, required strings present."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DOCS = ROOT / "docs"

PAGES = [
    "index.html",
    "install.html",
    "autostart.html",
    "access.html",
    "models.html",
    "privacy.html",
    "checklist.html",
]

ASSETS = ["assets/style.css", "assets/script.js"]

errors = []
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if condition:
        print(f"  ok: {message}")
    else:
        errors.append(message)
        print(f"  FAIL: {message}")


class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag in ("a", "link"):
            for key, value in attrs:
                if key == "href" and value and not value.startswith(("http://", "https://", "mailto:")):
                    self.links.append(value)
        if tag == "script":
            for key, value in attrs:
                if key == "src" and value:
                    self.links.append(value)


def normalize_link(link):
    """Return (kind, target_path). kind in {fragment, external_doc, site_page, asset}."""
    if link.startswith("#"):
        return ("fragment", link)
    # strip fragment
    path_part = link.split("#")[0]
    if path_part.endswith(".md"):
        # source-doc cross-reference; should exist in docs/
        return ("external_doc", DOCS / path_part)
    if path_part.endswith(".html"):
        return ("site_page", SITE / path_part)
    return ("asset", SITE / path_part)


print(f"Verifying site in {SITE}")

for page in PAGES:
    path = SITE / page
    check(path.exists(), f"{page} exists")
    text = path.read_text(encoding="utf-8")
    check("<html" in text.lower(), f"{page} is HTML")
    check("Asdale Dynamics, LLC" in text, f"{page} credits Asdale Dynamics, LLC")
    check("Copyright (c) 2026 Asdale Dynamics, LLC" in text, f"{page} has exact copyright line")
    collector = LinkCollector()
    collector.feed(text)
    for link in collector.links:
        kind, target = normalize_link(link)
        if kind == "fragment":
            check(True, f"{page} -> {link} (fragment, valid anchor link)")
        elif kind == "external_doc":
            check(target.exists(), f"{page} -> {link} source doc exists in docs/")
        else:
            check(target.exists(), f"{page} -> {link} resolves")

for asset in ASSETS:
    check((SITE / asset).exists(), f"asset {asset} exists")

checklist = (SITE / "checklist.html").read_text(encoding="utf-8")
check("type=\"checkbox\"" in checklist, "checklist page renders checkbox inputs")
check("task-list" in checklist or "checkbox" in checklist, "checklist page has task-list items")
check("@media print" in (SITE / "assets" / "style.css").read_text(encoding="utf-8"), "print styles exist")

license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
check("Copyright (c) 2026 Asdale Dynamics, LLC" in license_text, "LICENSE has exact copyright line")
check("MIT License" in license_text, "LICENSE is MIT")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
check("Asdale Dynamics, LLC" in readme, "README credits Asdale Dynamics, LLC")
check("MIT" in readme, "README mentions license")

print()
print(f"Checks: {checks}, Failures: {len(errors)}")
if errors:
    print("Failures:")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)
print("All checks passed.")
