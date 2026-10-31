# STATUS

## What was built

A beginner manual and static HTML site for running Ollama as a headless home server, published by Asdale Dynamics, LLC.

**Files:**
- `docs/00-welcome.md` — Welcome & overview
- `docs/01-install.md` — Install Ollama
- `docs/02-autostart.md` — Auto-start on boot (systemd)
- `docs/03-access.md` — Access from other devices (LAN + firewall)
- `docs/04-models.md` — Pull and run models
- `docs/05-privacy.md` — Keep chats private
- `docs/06-checklist.md` — Printable setup checklist
- `site/*.html` — Static HTML version of all seven pages (built from docs/)
- `site/assets/style.css` — Responsive CSS with print stylesheet
- `site/assets/script.js` — Nav highlighting + print hint
- `tools/build_site.py` — Converts docs/ Markdown into site/ HTML
- `tools/verify_site.py` — Verifies pages, links, credits, license
- `README.md` — Project overview, credits, license, disclaimer
- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`

**Credits:** Asdale Dynamics, LLC credited in README.md, every HTML page, and the site nav/footer. Copyright line matches exactly across LICENSE and all pages.

## How to run it

1. Read the guide: open `site/index.html` in any browser, or start at `docs/00-welcome.md`.
2. Rebuild the HTML site from Markdown: `python3 tools/build_site.py`
3. Run verification: `python3 tools/verify_site.py`
4. Print the checklist: open `site/checklist.html`, use browser Print (Ctrl+P / Cmd+P).

Requires Python 3 with the `Markdown` package (`markdown` PyPI). No Node, no build server, no API key.

## Verification results

`python3 tools/verify_site.py` → **All 181 checks passed, 0 failures.**

Checks cover:
- All 7 HTML pages exist and are valid HTML
- Every page credits "Asdale Dynamics, LLC"
- Every page has the exact copyright line `Copyright (c) 2026 Asdale Dynamics, LLC`
- All internal links resolve (pages, assets, source-doc references, fragment anchors)
- Checklist page renders real `<input type="checkbox">` task items
- Print stylesheet (`@media print`) present in CSS
- LICENSE is MIT with the exact copyright line
- README credits Asdale Dynamics, LLC

## Known gaps

- **End-to-end Ollama runtime not tested in this sandbox.** The Ollama install script (`curl -fsSL https://ollama.com/install.sh | sh`) was verified reachable, but a full install could not be completed because this environment lacks the `zstd` command (required by the installer), apt mirrors are unreachable, and the standalone binary URL returned 404. The install/autostart/access/models/privacy steps follow Ollama's official documentation and are standard, correct commands. Validate them on a real Linux machine with `zstd` installed.
- No `.github/workflows` files (intentionally omitted per instructions).
- No git remote, no pushes, no publishing (intentionally omitted per instructions).
