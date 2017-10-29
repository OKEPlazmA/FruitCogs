import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help
# Sys
import asyncio
import aiohttp
import time
import random
import os
import sys

class Hug:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hug(self, context, int, member: discord.Member):
        """Hug People!"""
        author = context.message.author.mention
        mention = member.mention
        
        hug = "**{0} gave {1} a hug!**"
        
        choices = ['http://i.imgur.com/sW3RvRN.gif', 'http://i.imgur.com/gdE2w1x.gif', 'http://i.imgur.com/zpbtWVE.gif', 'http://i.imgur.com/ZQivdm1.gif', 'http://i.imgur.com/MWZUMNX.gif', 'https://m.popkey.co/fca5d5/bXDgV.gif', 'http://gifimage.net/wp-content/uploads/2017/01/Anime-hug-GIF-Image-Download-24.gif', 'https://i.imgur.com/2WywS3T.gif']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=hug.format(author, mention), colour=0xffa500())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Hug(bot)
    bot.add_cog(n)
