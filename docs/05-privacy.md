# 5. Keep chats private

Ollama is private by design: models run on your hardware, and your prompts never leave your server unless you deliberately send them elsewhere. This section is a checklist to keep it that way.

## What stays local

- Every model you download (`ollama pull`) is stored on your server
- Every chat you have is processed on your server
- No account, no login, and no API key are required
- Ollama, Inc. does not see your conversations when you run Ollama yourself

## Verify Ollama is not reaching out

Confirm Ollama is listening only where you expect:

```
curl http://127.0.0.1:11434/api/tags
```

If you followed Step 3, it also answers on your server's LAN IP. That is fine inside your home. Do **not** open port 11434 on your router, and do not use a cloud "tunnel" service to expose Ollama to the internet.

## Option A: Maximum privacy — localhost only

If only this server needs to use Ollama, leave it on localhost (the default). No other device can reach it, and no network traffic leaves the machine at all.

To undo Step 2's network change:

```
sudo rm /etc/systemd/system/ollama.service.d/override.conf
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

## Option B: Home network — trust your Wi-Fi

Binding to `0.0.0.0:11434` (Step 3) lets phones and laptops on your Wi-Fi use Ollama. This is safe if:

- You trust everyone on your home network
- Your router does not have port 11434 forwarded to the internet
- You do not connect unknown devices (guest Wi-Fi, strangers) to your main network

## Option C: Away from home — use a private VPN

If you want to reach your home server while traveling, do not punch a hole in your router. Instead:

- Install **Tailscale** or another mesh VPN on the server and your devices
- Access Ollama over the VPN's private IP address
- Your traffic stays encrypted and never touches the public internet

## Disable telemetry (optional)

Ollama sends minimal telemetry by default. To turn it off, add this to the same override file from Step 3:

```
Environment="OLLAMA_HOST=0.0.0.0:11434"
Environment="OLLAMA_DISABLE_TELEMETRY=1"
```

Then:

```
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

## Back up your models

Your models live here:

```
/usr/share/ollama/.ollama/models
```

Copy this folder to an external drive or another computer if you want to keep your models after reinstalling the server. Chats (conversation history) are not stored by Ollama between sessions — once you exit a chat, it is gone from the server unless your frontend saves it.

## What Ollama is not

Ollama is a tool for running models locally. It does not filter, diagnose, or advise on health matters. This guide is educational only — see the disclaimer in [Welcome](00-welcome.md).

## What happens next

You have a private, local-first AI server. Print the [setup checklist](06-checklist.md) and walk through each step one more time to confirm everything is in place.

<hr>
<small>Copyright (c) 2026 Asdale Dynamics, LLC. MIT Licensed. See LICENSE.</small>
