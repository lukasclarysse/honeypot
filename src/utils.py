import asyncio
from datetime import datetime, timedelta, UTC
from logging_setup import log

async def delete_recent_user_messages(guild, user, seconds=300):
    now = datetime.now(UTC)
    cutoff = now - timedelta(seconds=seconds)
    deleted_count = 0

    for channel in guild.text_channels:
        if not channel.permissions_for(guild.me).manage_messages:
            continue

        try:
            async for msg in channel.history(limit=100, after=cutoff):
                if msg.author.id == user.id:
                    try:
                        await msg.delete()
                        deleted_count += 1
                        await asyncio.sleep(0.4)
                    except Exception as e:
                        log.warning(f"Failed to delete a message in #{channel.name}: {e}")
        except Exception as e:
            log.warning(f"Cannot access history in #{channel.name}: {e}")

    return deleted_count
