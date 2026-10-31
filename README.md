# Ollama Home Server Guide

A beginner-friendly, step-by-step manual for running **Ollama** as a headless home server: install, auto-start on boot, access from other devices, pull and run models, and keep your chats private. **No API key, no cloud account, everything local.**

Written for **Dylan Asdale**, registered nurse turned AI author and founder of **Asdale Dynamics, LLC** (Indiana, formed October 2026). Published by Asdale Dynamics — beginner-friendly AI education, books, and practical tools. This guide accompanies *The Massive AI Manual* and dylanasdale.github.io.

## Who this is for

You do not need to be a programmer. If you can copy and paste a command into a terminal, you can follow this guide. Every step is written in plain English, with jargon explained the first time it appears.

It is written for anyone who wants a private AI chat server at home — an old laptop or desktop tucked away on your Wi-Fi, reachable from your phone and laptop, with nothing sent to the cloud.

## What's inside

| Folder | Contents |
|--------|----------|
| `docs/` | The manual in Markdown: welcome, install, auto-start, access, models, privacy, and a printable setup checklist |
| `site/` | A polished static HTML version of the same manual — open `site/index.html` in any browser |
| `tools/build_site.py` | Build script that converts `docs/` into `site/` |
| `tools/verify_site.py` | Verification script: checks pages, links, credits, and license |
| `LICENSE` | MIT License |

## The guide in six steps

1. **[Install Ollama](docs/01-install.md)** — run the official install script on a Linux home server
2. **[Auto-start on boot](docs/02-autostart.md)** — enable the systemd service so Ollama survives reboots
3. **[Access from other devices](docs/03-access.md)** — reach Ollama from your phone and laptop on the same Wi-Fi
4. **[Pull and run models](docs/04-models.md)** — download your first model and start chatting
5. **[Keep chats private](docs/05-privacy.md)** — keep Ollama on your home network, never expose it to the internet
6. **[Printable setup checklist](docs/06-checklist.md)** — a one-page checklist to print and check off

## Quick start

Read the guide:

- Markdown: start at [`docs/00-welcome.md`](docs/00-welcome.md)
- HTML: open [`site/index.html`](site/index.html) in your browser

Rebuild the HTML site from the Markdown source:

```bash
python3 tools/build_site.py
```

Run the verification script:

```bash
python3 tools/verify_site.py
```

## What you need

- A 64-bit computer running Linux (Ubuntu, Debian, Linux Mint, Raspberry Pi OS, etc.) — an old laptop or desktop works great
- At least 4 GB of RAM (8 GB or more recommended)
- About 5–10 GB of free disk space for your first model
- An Ethernet cable or Wi-Fi connection to your home router
- Another device (phone, laptop, tablet) on the same network to test with
- A user account with `sudo` access

No graphics card is required. Ollama runs on ordinary processors; a GPU just makes it faster.

## Privacy by design

Ollama runs models on **your** hardware. Your prompts and the model's answers never leave your server unless you deliberately send them elsewhere. No account, no login, and no API key are ever required. This guide keeps Ollama on your home network and does not expose it to the public internet.

## Print the checklist

Open [`site/checklist.html`](site/checklist.html) in your browser and use your browser's Print command (Ctrl+P / Cmd+P). The page hides headers, nav, and footer when printed, and shows the full URL of each link so the checklist works on paper.

## Credits

Written for **Dylan Asdale**, registered nurse turned AI author and founder of **Asdale Dynamics, LLC** (Indiana, formed October 2026). Asdale Dynamics makes beginner-friendly AI education, books, and practical tools. This guide accompanies *The Massive AI Manual* and the hub site dylanasdale.github.io.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See [`LICENSE`](LICENSE).

## Disclaimer

Educational use only. Ollama is a tool for running AI models locally; it is not medical advice. Dylan Asdale is a registered nurse, but nothing in this guide is medical advice. Consult a qualified clinician for health-related questions.
