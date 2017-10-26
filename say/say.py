import discord
from discord.ext import commands

class Say:
    """Tell Fruit to say words *use your words son*"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def say(self, ctx, *, text):
        """Tell Fruit to say something! *use your words son.*"""
        channel = ctx.message.channel
        await self.bot.send_message(channel, text)
        await self.bot.delete_message(ctx.message)

def setup(bot):
    bot.add_cog(Say(bot))
