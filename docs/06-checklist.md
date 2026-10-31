# 6. Printable setup checklist

Print this page and check off each box as you complete it. Keep it with your server notes.

## Ollama headless home server — setup checklist

**Server:** ____________________   **IP address:** ____________________   **Date:** ____________________

### Before you begin
- [ ] 64-bit Linux computer ready (old laptop or desktop is fine)
- [ ] At least 4 GB RAM (8 GB recommended)
- [ ] 5–10 GB free disk space
- [ ] Ethernet or Wi-Fi connected to home router
- [ ] Another device (phone/laptop/tablet) on the same network
- [ ] User account with `sudo` access

### 1. Install Ollama
- [ ] `curl` installed
- [ ] `curl -fsSL https://ollama.com/install.sh | sh` ran successfully
- [ ] `ollama --version` shows a version number
- [ ] `ollama list` runs without error

### 2. Auto-start on boot
- [ ] `sudo systemctl enable --now ollama` ran successfully
- [ ] `systemctl status ollama` shows `active (running)`
- [ ] `curl http://127.0.0.1:11434/api/tags` returns JSON
- [ ] (Optional) Reboot test passed — Ollama is running after restart

### 3. Access from other devices
- [ ] Server IP address recorded (`hostname -I`)
- [ ] `OLLAMA_HOST=0.0.0.0:11434` override created
- [ ] `sudo systemctl daemon-reload` and `restart ollama` completed
- [ ] Firewall rule added (`sudo ufw allow 11434/tcp`) — if you use `ufw`
- [ ] Browser on another device reaches `http://<SERVER-IP>:11434`

### 4. Pull and run models
- [ ] First model pulled (for example `ollama pull llama3.2:3b`)
- [ ] `ollama list` shows the model
- [ ] Chatted with the model using `ollama run`
- [ ] (Optional) Tested `curl http://<SERVER-IP>:11434/api/generate` from another device

### 5. Keep chats private
- [ ] Port 11434 is NOT forwarded on the router
- [ ] Ollama is not exposed to the public internet
- [ ] Remote access (if needed) goes through a private VPN such as Tailscale
- [ ] Model folder backed up: `/usr/share/ollama/.ollama/models`
- [ ] No API keys or accounts created — chats stay local

### Done?
- [ ] All checkboxes complete — your Ollama home server is ready

## Notes

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

Models downloaded: ________________________________________________________

<hr>
<small>Copyright (c) 2026 Asdale Dynamics, LLC. MIT Licensed. See LICENSE.</small>
