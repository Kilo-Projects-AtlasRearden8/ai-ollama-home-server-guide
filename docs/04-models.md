# 4. Pull and run models

A model is the AI itself — a file you download once, then run as often as you like. Models live on your server. Nothing goes to Ollama, Inc., and no API key is ever needed.

## Pick your first model

For a first model, choose something small so it runs well on modest hardware:

| Model | Size | Good for |
|-------|------|----------|
| `llama3.2:1b` | ~1.3 GB | Quick questions, short answers, very low RAM |
| `llama3.2:3b` | ~2.0 GB | General chatting, best first choice if you have 8 GB+ RAM |
| `phi4-mini` | ~2.3 GB | Strong reasoning in a small package |
| `qwen2.5:1.5b` | ~0.9 GB | Fast, lightweight, multilingual |
| `gemma3:1b` | ~0.8 GB | Tiny, efficient, simple tasks |

Rule of thumb: a model needs about 1 GB of RAM for every 1 billion parameters ("1b" = 1 billion). `llama3.2:3b` needs roughly 3–4 GB of free RAM.

## Pull (download) a model

On the server, run:

```
ollama pull llama3.2:3b
```

Watch the progress bars. When it finishes, the model is stored locally under `/usr/share/ollama/.ollama/models`.

List your models:

```
ollama list
```

You will see something like:

```
NAME             SIZE    MODIFIED
llama3.2:3b      2.0 GB  ...
```

## Run a model and chat

Start the model in your terminal:

```
ollama run llama3.2:3b
```

Type a message and press Enter:

```
Hi, what can you help me with?
```

The model will reply. Keep typing to continue the conversation. When you are done, type:

```
/bye
```

Other handy commands while running a model:

- `/?` — show help
- `/set` — change model settings
- `/bye` — exit

## Chat from another device (over the network)

Once you have finished Step 3 ([Access from other devices](03-access.md)), you can chat from your phone or laptop using `curl`:

```
curl http://<SERVER-IP>:11434/api/generate -d '{
  "model": "llama3.2:3b",
  "prompt": "Write a one-sentence bedtime story.",
  "stream": false
}'
```

Replace `<SERVER-IP>` with your server's address. You will get a JSON reply containing the model's answer.

## Remove a model you no longer need

Models take up space. To delete one:

```
ollama rm llama3.2:3b
```

## Tips for beginners

- Start small. You can always pull a bigger model later.
- The first `ollama run` of a new model automatically downloads it — you do not need a separate `pull` step.
- If a model is slow or won't start, your server may be low on RAM. Try a smaller model (look for `:1b` variants).
- Model files are yours to keep, copy, or back up. They live in `/usr/share/ollama/.ollama/models`.

## What happens next

Your server is installed, starts on boot, is reachable from your devices, and can run models. The last step is making sure your chats stay private: [5. Keep chats private](05-privacy.md).

<hr>
<small>Copyright (c) 2026 Asdale Dynamics, LLC. MIT Licensed. See LICENSE.</small>
