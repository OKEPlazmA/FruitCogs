import discord
from discord.ext import commands
from random import choice as rndchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

kisslist = [
    "https://i.imgur.com/II1bakc.gif",
    "https://i.imgur.com/MzAjNdv.gif",
    "https://i.imgur.com/eKcWCgS.gif",
    "https://i.imgur.com/3aX4Qq2.gif",
    "https://i.imgur.com/uobBW9K.gif",
    "https://i.imgur.com/3jzT5g6.gif",
    "https://i.imgur.com/Esqtd1u.gif",
    "https://i.imgur.com/FozOXkB.gif",
    "https://i.imgur.com/7GhTplD.gif",
    "https://i.imgur.com/B6UKulT.gif",
    "https://i.imgur.com/Uow8no2.gif",
    "https://i.imgur.com/EwQPLZI.gif",
    "https://i.imgur.com/agdhkfE.gif",
    "https://i.imgur.com/1IuyOxK.gif",
    "https://i.imgur.com/nodEB4W.gif",
    "https://i.imgur.com/KSiA3Ws.gif",
    "https://i.imgur.com/nVM7Ll8.gif",
    "https://i.imgur.com/glTzPMZ.gif"]

class Social:
    """Kiss"""

    @commands.command()
    async def kiss(self):

        kissed = random.choice(kisslist)
        kissimg = discord.Embed(description="Here is your meme!", color=0x0f8a6e)
        kissimg.set_image(url=kissed)
        await self.bot.say(embed=kissimg)


def setup(bot):
    bot.add_cog(Kiss(bot))
