# Welcome to the Ollama Home Server Guide

**A beginner-friendly, step-by-step manual for running Ollama as a headless home server — no API key, no cloud account, everything local.**

Written for Dylan Asdale and published by **Asdale Dynamics, LLC** (Indiana, formed October 2026). Asdale Dynamics makes beginner-friendly AI education, books, and practical tools. This guide accompanies *The Massive AI Manual* and the hub site dylanasdale.github.io.

## What is Ollama?

Ollama is a free, open-source program that lets you run large language models (AI models) on your own hardware. When you chat with Ollama, the model runs on **your** computer — not on someone else's server. Nothing you type is sent to Ollama, Inc., and you never need an API key.

## What is a "headless home server"?

A headless server is just a computer that runs without a monitor, keyboard, or mouse attached. You set it up once, tuck it away (an old laptop or desktop works great), and access it from your other devices over your home Wi-Fi.

## What this guide covers

| Step | Topic | What you'll do |
|------|-------|----------------|
| 1 | [Install Ollama](01-install.md) | Install Ollama on a Linux home server |
| 2 | [Auto-start on boot](02-autostart.md) | Make Ollama start automatically whenever the server turns on |
| 3 | [Access from other devices](03-access.md) | Reach Ollama from your phone, laptop, or tablet on the same Wi-Fi |
| 4 | [Pull and run models](04-models.md) | Download your first AI model and start chatting |
| 5 | [Keep chats private](05-privacy.md) | Lock down your server so your data never leaves your home |
| 6 | [Printable setup checklist](06-checklist.md) | A one-page checklist to print and check off as you go |

## What you'll need

- A 64-bit computer running Linux (Ubuntu, Debian, Mint, or similar) — an old laptop or desktop is perfect
- At least 4 GB of RAM (8 GB or more recommended)
- About 5–10 GB of free disk space for your first model
- An Ethernet cable or Wi-Fi connection to your home router
- Another device (phone, laptop, tablet) on the same network to test with

No graphics card is required. Ollama runs fine on ordinary processors; a GPU just makes it faster.

## Who this is for

You do not need to be a programmer. If you can copy and paste commands into a terminal, you can follow this guide. Every step is written in plain English, with no jargon without an explanation.

## A note on privacy and safety

This guide is **local-first**: every model, every chat, and every setting stays on your hardware unless you explicitly choose to share it. Ollama has no built-in password, so we will keep the server on your home network and **not** expose it to the public internet.

*Educational use only.* Dylan Asdale is a registered nurse, but this guide and anything from Asdale Dynamics is not medical advice. If you are using AI for health-related questions, please consult a qualified clinician.

---

**Next step:** [1. Install Ollama](01-install.md)

<hr>
<small>Copyright (c) 2026 Asdale Dynamics, LLC. MIT Licensed. See LICENSE.</small>
