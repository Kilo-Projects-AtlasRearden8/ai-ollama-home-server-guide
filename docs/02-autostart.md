# 2. Auto-start on boot

A headless server is only useful if it comes back up by itself after a power outage or reboot. Ollama's installer already creates a system service — we just need to turn it on.

## Check whether Ollama is already enabled

```
systemctl is-enabled ollama
```

- `enabled` → Ollama will start on boot. You are done with this step.
- `disabled` → continue below.

## Enable Ollama to start automatically

```
sudo systemctl enable --now ollama
```

- `enable` starts Ollama on every boot.
- `--now` starts it right away, too.

## Confirm it is running

```
systemctl status ollama
```

Look for a line like:

```
Active: active (running) since ...
```

Press `q` to exit the status screen.

## Check that it responds

```
curl http://127.0.0.1:11434/api/tags
```

You should see JSON output listing your models (or an empty list if you have not pulled any yet):

```
{"models":[]}
```

If you get `connection refused`, Ollama is not running. Start it manually:

```
sudo systemctl start ollama
```

## Reboot test (optional but recommended)

Restart the server and check again:

```
sudo reboot
```

After it comes back up, log in again and run:

```
systemctl status ollama
curl http://127.0.0.1:11434/api/tags
```

If both succeed, Ollama will survive reboots on its own.

## Where Ollama stores its data

Because we are using the system service, Ollama keeps models and data under:

```
/usr/share/ollama/.ollama
```

Back this folder up if you ever reinstall the server — it contains every model you have downloaded.

## What happens next

Ollama now starts on boot, but it still only listens on the server itself. Next we will open it up to your other home devices: [3. Access from other devices](03-access.md).

<hr>
<small>Copyright (c) 2026 Asdale Dynamics, LLC. MIT Licensed. See LICENSE.</small>
