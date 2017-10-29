import discord
from discord.ext import commands
from random import choice as rndchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

memelist = ['http://i.imgur.com/sW3RvRN.gif', 'http://i.imgur.com/gdE2w1x.gif', 'http://i.imgur.com/zpbtWVE.gif', 'http://i.imgur.com/ZQivdm1.gif', 'http://i.imgur.com/MWZUMNX.gif', 'https://m.popkey.co/fca5d5/bXDgV.gif', 'http://gifimage.net/wp-content/uploads/2017/01/Anime-hug-GIF-Image-Download-24.gif', 'https://i.imgur.com/2WywS3T.gif']

class Hug:
    """Hug People."""
    def __init__(self, bot) :
        self.bot = bot

    @commands.command()
    async def hug(self, ctx, **, user: discord.Member=None):
        user = ctx.message.author
        botname = self.bot.user.name
        memed = rndchoice(memelist)
        memeimg = discord.Embed(description="**" + user + "has recieved a hug!" "**", color=0xffa500)
        memeimg.set_image(url=memed)
        await self.bot.say(embed=memeimg)


def setup(bot):
    bot.add_cog(Hug(bot))

