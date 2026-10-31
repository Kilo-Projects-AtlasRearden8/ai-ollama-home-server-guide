# 3. Access from other devices

By default, Ollama only listens on the server itself (`127.0.0.1`, also called localhost). That is the safest setting, but it means your phone and laptop cannot reach it yet. In this step we will let other devices on your home Wi-Fi talk to Ollama.

## Step 1: Find your server's IP address

On the server, run:

```
hostname -I
```

You will see something like:

```
192.168.1.42
```

That is your server's address on your home network. Write it down — you will use it in place of `<SERVER-IP>` below.

If you see multiple addresses, pick the one that looks like `192.168.x.x` or `10.x.x.x`.

## Step 2: Tell Ollama to listen on all network addresses

Create a configuration override so Ollama binds to `0.0.0.0` (every network address) instead of localhost only:

```
sudo mkdir -p /etc/systemd/system/ollama.service.d
sudo tee /etc/systemd/system/ollama.service.d/override.conf > /dev/null <<'EOF'
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
EOF
```

Reload systemd and restart Ollama:

```
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

Confirm it is still running:

```
systemctl status ollama
```

## Step 3: Open the firewall (if you have one)

Many Linux distributions ship with a firewall called `ufw`. Check whether it is active:

```
sudo ufw status
```

If it says `Status: active`, allow port 11434 on your home network:

```
sudo ufw allow 11434/tcp
```

If `ufw` is not installed or inactive, your router's built-in firewall already protects you — as long as you do not set up port forwarding (see the warning below).

## Step 4: Test from another device

On your phone, laptop, or tablet connected to the same Wi-Fi, open a browser and visit:

```
http://<SERVER-IP>:11434
```

Replace `<SERVER-IP>` with the address from Step 1, for example:

```
http://192.168.1.42:11434
```

You should see a plain text message saying Ollama is running. That page confirms the server is reachable — the actual chatting happens in the next step ([Pull and run models](04-models.md)).

You can also test with `curl` from another device:

```
curl http://<SERVER-IP>:11434/api/tags
```

## Important privacy warning

**Do not forward port 11434 on your router, and do not expose Ollama directly to the internet.** Ollama has no built-in password or login. Anyone who can reach port 11434 can run models and read your chats.

- **At home on your Wi-Fi:** safe, as long as you trust the people on your network.
- **Away from home:** use a private VPN (such as Tailscale) to reach your server, or wait until you are back on your home network.

## What happens next

Now that your devices can reach Ollama, let's download a model and start chatting: [4. Pull and run models](04-models.md).

<hr>
<small>Copyright (c) 2026 Asdale Dynamics, LLC. MIT Licensed. See LICENSE.</small>
