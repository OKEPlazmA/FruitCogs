import discord
from discord.ext import commands
from random import choice as rndchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

defaults = [
    "https://i.imgur.com/Ltmb8aa.gif",
    "https://www.tenor.co/xNYw.gif",
    "https://www.tenor.co/FQNP.gif",
    "https://giphy.com/gifs/happy-hug-od5H3PmEG5EVq",
    "https://tenor.com/view/hug-fall-anime-cute-gif-353203",
    "https://tenor.com/view/hug-chicken-boy-gif-3536563",
    "https://tenor.com/view/hearts-cat-valentine-hugging-hearts-hug-gif-3550845",
    "https://tenor.com/view/love-cartoon-hug-gif-5139573",
    "https://tenor.com/view/hug-sibling-awkward-pat-gravity-gif-6151709",
    "https://tenor.com/view/disney-pocahontas-john-smith-irene-bedard-mel-gibson-gif-5619513",
    "https://gifimage.net/wp-content/uploads/2017/06/anime-hug-gif-4.gif"
    "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"
    "https://media.giphy.com/media/qscdhWs5o3yb6/giphy.gif"]


class Hug:
    """Hug people."""

    def __init__(self, bot):
        self.bot = bot
        self.items = fileIO("data/hug/items.json", "load")

    def save_items(self):
        fileIO("data/hug/items.json", 'save', self.items)

    @commands.group(pass_context=True, invoke_without_command=True)
    async def hug(self, ctx, *, user: discord.Member=None):
        """Hug a user"""
        botid = self.bot.user.id
        if user is None:
            user = ctx.message.author
            await self.bot.say("You have to hug a real person, i am not capable of hugs sorry, " + user.name)
        elif user.id == botid:
            user = ctx.message.author
            botname = self.bot.user.name
            await self.bot.say("-" + botname + " hugs " + user.mention +
                               " :D " +
                               (rndchoice(self.items) + ""))
        else:
            await self.bot.say("You have recieved a hug, " + user.mention + ", :3 " +
                               (rndchoice(self.items) + ""))

    @hug.command()
    async def add(self, item):
        """Adds a hug image or message."""
        if item in self.items:
            await self.bot.say("That is already an Item.")
        else:
            self.items.append(item)
            self.save_items()
            await self.bot.say("Item added.")

    @hug.command()
    @checks.is_owner()
    async def remove(self, item):
        """Removes item"""
        if item not in self.items:
            await self.bot.say("That is not an item")
        else:
            self.items.remove(item)
            self.save_items()
            await self.bot.say("item removed.")


def check_folders():
    if not os.path.exists("data/hug"):
        print("Creating data/hug folder...")
        os.makedirs("data/hug")


def check_files():
    f = "data/hug/items.json"
    if not fileIO(f, "check"):
        print("Creating empty items.json...")
        fileIO(f, "save", defaults)


def setup(bot):
    check_folders()
    check_files()
    n = Hug(bot)
    bot.add_cog(n)
