# Discord Honeypot Bot

A simple, configurable Discord bot that monitors a "honeypot" channel.  
Any user who posts in that channel will have their message deleted, their recent messages purged, and then be **kicked or banned** depending on configuration.

This is meant as a lightweight moderation helper — minimal setup, minimal dependencies.

---

## Features

- Automatic honeypot detection  
- Configurable moderation action (`kick` or `ban`)  
- Deletes the triggering message  
- Purges recent messages from the user  
- Sends a log entry to a moderation channel  
- Easy to configure via `.env` file  
- Modular codebase which is easy to expand upon

---

## Requirements

- Python 3.10+  
- A Discord bot token  
- Permissions for:
  - Message Content intent  
  - Members intent  
  - Managing messages  
  - Kicking/banning members (depending on `BOT_ACTION`)

Make sure you enable the privileged intents in the Discord Developer Portal.

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/lukasclarysse/honeypot.git
cd honeypot
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Inviting the Bot to Your Server

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) → Your Bot → OAuth2 → URL Generator.  
2. Select the **bot** scope.  
3. Under **Bot Permissions**, select:  
   - Manage Messages  
   - Kick Members / Ban Members (depending on `BOT_ACTION`)  
   - Read Message History  
   - Send Messages  
   - Embed Links  
4. Copy the generated URL and open it in your browser.  
5. Choose the server you want to add the bot to and authorize it.

---

## Configuration

Create a `.env` file in the project root.

Example:

```
TOKEN=your_discord_bot_token_goes_here

GUILD_ID=123456789012345678
HONEYPOT_CHANNEL=123456789012345678
LOG_CHANNEL=123456789012345678

BOT_ACTION=kick       # or "ban"
PURGE_TIMEFRAME=60    # seconds
```

### Variable meanings

| Variable | Description |
|---------|-------------|
| `TOKEN` | Your bot's API token |
| `GUILD_ID` | ID of the server the bot runs in |
| `HONEYPOT_CHANNEL` | Channel where posting triggers punishment |
| `LOG_CHANNEL` | Channel where moderator logs should be sent |
| `BOT_ACTION` | `"kick"` or `"ban"` |
| `PURGE_TIMEFRAME` | How many seconds of the user's history to delete |

---

## Running the Bot

### Initializing

Start the bot with:

```bash
python src/bot.py
```

Spawning this process can be automated through systemd, cron, or other process managers.

### Verifying

Check whether the bot is online using the `$ping` command.

---

## License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.
