from discord.ext import commands

def register_commands(bot):
    @bot.command()
    async def ping(ctx):
        latency = round(bot.latency * 1000)
        await ctx.send(f"pong `{latency}ms`")
