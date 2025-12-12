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
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create the `.env` file in the project root.

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

All you have to do to get started is run this command: 

```bash
python src/bot.py
```

Spawning this process can be automated through the likes of systemd and cron.

---

## License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.
