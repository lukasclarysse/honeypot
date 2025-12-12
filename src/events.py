import discord
from config import HONEYPOT_CHANNEL, LOG_CHANNEL, BOT_ACTION, PURGE_TIMEFRAME
from logging_setup import log
from embeds import HONEYPOT_WARNING_EMBED, HONEYPOT_WARNING_MARKER
from utils import delete_recent_user_messages

async def ensure_honeypot_warning(bot):
    channel = bot.get_channel(HONEYPOT_CHANNEL)
    if not channel:
        log.warning("Honeypot channel not found")
        return

    async for msg in channel.history(limit=50):
        for emb in msg.embeds:
            if emb.footer and HONEYPOT_WARNING_MARKER in (emb.footer.text or ""):
                log.info("Honeypot warning already posted")
                return

    try:
        await channel.send(embed=HONEYPOT_WARNING_EMBED)
        log.info("Honeypot warning posted")
    except Exception as e:
        log.error(f"Failed to send honeypot warning: {e}")

def register_events(bot):
    @bot.event
    async def on_ready():
        log.info(f"Bot online as {bot.user}")
        await ensure_honeypot_warning(bot)

    @bot.event
    async def on_message(message):
        if message.author.bot:
            return

        await bot.process_commands(message)

        if message.channel.id != HONEYPOT_CHANNEL:
            return

        log.info(f"HONEYPOT TRIGGER: {message.author} in #{message.channel.name}")

        guild = message.guild
        mod_channel = bot.get_channel(LOG_CHANNEL)

        if mod_channel:
            try:
                embed = discord.Embed(
                    title="Honeypot Alert",
                    description=f"User: {message.author.mention}",
                    color=discord.Color.green(),
                    timestamp=message.created_at
                )
                embed.add_field(name="Message", value=message.content or "*No content*", inline=False)
                embed.set_footer(text=f"User ID: {message.author.id}")
                await mod_channel.send(embed=embed)
            except Exception as e:
                log.error(f"Failed to send log embed: {e}")

        try:
            await message.delete()
        except Exception as e:
            log.warning(f"Failed to delete honeypot message: {e}")

        try:
            deleted = await delete_recent_user_messages(guild, message.author, PURGE_TIMEFRAME)
            if mod_channel and deleted > 0:
                await mod_channel.send(
                    f"Deleted `{deleted}` recent messages from {message.author.mention} "
                    f"(last {PURGE_TIMEFRAME} seconds)."
                )
        except Exception as e:
            log.error(f"Failed to purge messages: {e}")

        try:
            member = await guild.fetch_member(message.author.id)
            if BOT_ACTION == "ban":
                await guild.ban(member, reason="Triggered honeypot")
            else:
                action_method = getattr(member, BOT_ACTION, None)
                if action_method:
                    await action_method(reason="Triggered honeypot")
                else:
                    log.info(f"BOT_ACTION={BOT_ACTION} → no action taken")

            log.info(f"{BOT_ACTION.capitalize()} {member}")
        except Exception as e:
            log.error(f"Failed to apply moderation action: {e}")
