# 1. Install Ollama

Install Ollama on your Linux home server. This step takes about 10 minutes, most of it waiting for the download to finish.

## What you need before you start

- A 64-bit Linux computer (Ubuntu, Debian, Linux Mint, Raspberry Pi OS, etc.)
- A user account with `sudo` privileges (the account you log in with)
- An internet connection for the initial download
- About 2 GB of free disk space for the Ollama program itself (models are separate)

## Step 1: Open a terminal

If your server has a monitor and keyboard, open the terminal application. If it is headless (no screen), log in over SSH from another device:

```
ssh your-username@your-server-ip
```

## Step 2: Install Ollama

Run the official Ollama install script:

```
curl -fsSL https://ollama.com/install.sh | sh
```

What this does: downloads the Ollama program, creates an `ollama` system user, and sets Ollama up to start automatically when the computer boots.

When it finishes, you should see a message like:

```
ollama installed successfully
```

## Step 3: Verify the installation

Check the version:

```
ollama --version
```

You should see something like:

```
ollama version is 0.5.x
```

List installed models (there won't be any yet):

```
ollama list
```

Expected output:

```
NAME    SIZE    MODIFIED
```

An empty list is normal — we will download a model in Step 4 of this guide ([Pull and run models](04-models.md)).

## Step 4: Quick smoke test

Start a tiny model right away to confirm Ollama works:

```
ollama run phi4-mini
```

Wait for the download, then type a message like `Hi, are you working?` and press Enter. You should get a reply. Type `/bye` and press Enter to exit.

If you do not want to download a model yet, skip this — it is just a sanity check.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `curl: command not found` | Install curl first: `sudo apt update && sudo apt install curl -y` |
| `permission denied` | Make sure your user can use `sudo`. Ask the person who set up the computer. |
| `command not found: ollama` after install | Close and reopen your terminal, or run `source /etc/profile.d/ollama.sh` if it exists. |

## What happens next

Ollama is now installed, but by default it only listens on the server itself (localhost). In the next step we will make sure it starts automatically on boot: [2. Auto-start on boot](02-autostart.md).

<hr>
<small>Copyright (c) 2026 Asdale Dynamics, LLC. MIT Licensed. See LICENSE.</small>
