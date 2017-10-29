from discord.ext import commands
import random
import discord

class Kiss:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kiss(self, context, member: discord.Member):
        """Kiss People!"""
        author = context.message.author.mention
        mention = member.mention
        
        kiss = "**{0} gave {1} a kiss!**"
        
        choices = ['http://i.imgur.com/0D0Mijk.gif', 'http://i.imgur.com/TNhivqs.gif', 'http://i.imgur.com/3wv088f.gif', 'http://i.imgur.com/7mkRzr1.gif', 'http://i.imgur.com/8fEyFHe.gif', "https://i.imgur.com/II1bakc.gif", "https://i.imgur.com/MzAjNdv.gif", "https://i.imgur.com/eKcWCgS.gif", "https://i.imgur.com/3aX4Qq2.gif", "https://i.imgur.com/uobBW9K.gif", "https://i.imgur.com/3jzT5g6.gif", "https://i.imgur.com/Esqtd1u.gif", "https://i.imgur.com/FozOXkB.gif", "https://i.imgur.com/7GhTplD.gif", "https://i.imgur.com/B6UKulT.gif", "https://i.imgur.com/Uow8no2.gif", "https://i.imgur.com/EwQPLZI.gif", "https://i.imgur.com/agdhkfE.gif", "https://i.imgur.com/1IuyOxK.gif", "https://i.imgur.com/nodEB4W.gif", "https://i.imgur.com/KSiA3Ws.gif", "https://i.imgur.com/nVM7Ll8.gif", "https://i.imgur.com/glTzPMZ.gif"]
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=kiss.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Kiss(bot)
    bot.add_cog(n)
