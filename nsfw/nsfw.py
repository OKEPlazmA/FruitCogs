import discord
import os
import collections
from .utils.dataIO import fileIO, dataIO
from .utils import checks
from discord.ext import commands

class Help:
    def __init__(self, bot):
        self.bot = bot
        self.profile = "data/help/toggle.json"
        self.riceCog = dataIO.load_json(self.profile)

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def sethelp(self, ctx):
        self.profile = "data/help/toggle.json"
        self.riceCog = dataIO.load_json(self.profile)
        dm_msg = "The help message will now be send in DM."
        no_dm_msg = "The help message will now be send into the channel."
ggle' not in self.riceCog:
            self.riceCog['toggle'] = "no_dm"
            dataIO.save_json(self.profile,
                             self.riceCog)
            msg = no_dm_msg
        elif self.riceCog['toggle'] == "dm":
            self.riceCog['toggle'] = "no_dm"
            dataIO.save_json(self.profile,
                             self.riceCog)
            msg = no_dm_msg
        elif self.riceCog['toggle'] == "no_dm":
            self.riceCog['toggle'] = "dm"
            dataIO.save_json(self.profile,
                             self.riceCog)
            msg = dm_msg
        if msg:
            await self.bot.say(msg)



    @commands.command(name='help', pass_context=True)
    async def _help(self, ctx, command = None):
        """Embedded help command"""
        author = ctx.message.author
        if 'toggle' not in self.riceCog:
            self.riceCog['toggle'] = "dm"
            dataIO.save_json(self.profile,
                             self.riceCog)
            await self.bot.say("Help message is set to DM by default. use "u
                               "**{}sethelp** to change it!".format(ctx.prefix))
            toggle = self.riceCog['toggle']
        else:
            toggle = self.riceCog['toggle']
        if not command:
            msg = "**Command list:**"
            color = 0xD2B48C


            final_coms = {}
            com_groups = []
            for com in self.bot.commands:
                try:
                    if not self.bot.commands[com].can_run(ctx):
                        continue
                    if self.bot.commands[com].module.__name__ not in com_groups:
                        com_groups.append(self.bot.commands[com].module.__name__)
                    else:
                        continue
                except Exception as e:
                        print(e)
                        continue
            com_groups.sort()
            alias = []
            #print(com_groups)
            for com_group in com_groups:
                commands = []
                for com in self.bot.commands:
                    if not self.bot.commands[com].can_run(ctx):
                        continue
                    if com in self.bot.commands[com].aliases:
                        continue
                    if com_group == self.bot.commands[com].module.__name__:
                        commands.append(com)
                final_coms[com_group] = commands

            to_send = []

            final_coms = collections.OrderedDict(sorted(final_coms.items()))
            field_count = 0
            page = 0
            counter = 0

            for group in final_coms:
                counter += 1
                if field_count == 0:
                    page += 1
                    title = "**Command list,** page {}".format(page)
                    em=discord.Embed(description=title,
                                     color=color)

                field_count += 1
                is_last = counter == len(final_coms)
                msg = ""
                final_coms[group].sort()
                count = 0
                for com in final_coms[group]:
                    if count == 0:
                        msg += '`{}`'.format(com)
                    else:
                        msg += '~`{}`'.format(com)
                    count += 1

                cog_name = group.replace("cogs.", "").title()
                cog =  "```\n"
                cog += cog_name
                cog += "\n```"
                em.add_field(name=cog,
                             value=msg,
                             inline=False)

                if field_count == 15 or is_last:
                    to_send.append(em)
                    field_count = 0


            if toggle == "dm":
                await self.bot.say("Hey there, {}! I sent you a list of "
                                   "commands through DM.".format(author.mention))
                for em in to_send:
                    await self.bot.send_message(ctx.message.author,
                                                embed=em)
                await self.bot.send_message(ctx.message.author,
                                        "Spoopy, the discord bot that does stuff because reasons. "
                                        "Made by OKE PlazmA, helped by it's community.")
            elif toggle == 'no_dm':
                for em in to_send:
                    await self.bot.say(embed=em)
                await self.bot.say("Spoopy, the discord bot that does stuff because reasons. "
                                   "Made by OKE PlazmA, helped by it's community.")

        else:
            msg = "**Command Help:**"
            color = 0xD2B48C

            em=discord.Embed(description=msg,
                             color=color)
            try:
                if not self.bot.commands[command].can_run(ctx):
                    await self.bot.say("Might be lacking perms for this "
                                       "command.")
                    return
                commie =  "```\n"
                commie += command + " " + " ".join(["[" + com + "]" for com in \
                                                    self.bot.commands[command].\
                                                    clean_params])
                commie += "\n```"
                info = self.bot.commands[command].help
                em.add_field(name=commie,
                             value=info,
                             inline=False)
                await self.bot.say(embed=em)
            except Exception as e:
                print(e)
                await self.bot.say("Couldn't find command! Try again.")

def check_folder():
    if not os.path.exists("data/help"):
        print("Creating data/help folder")
        os.makedirs("data/help")

def check_file():
    data = {}
    f = "data/help/toggle.json"
    if not dataIO.is_valid_json(f):
        print("Creating data/help/toggle.json")
        dataIO.save_json(f,
                         data)

def setup(bot):
    check_folder()

    bot.add_cog(Help(bot))
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

DIR_DATA = "data/oboobs"
SETTINGS = DIR_DATA+"/settings.json"
DEFAULT = {"nsfw_channels": ["133251234164375552"], "invert" : False, "nsfw_msg": True, "last_update": 0,  "ama_boobs": 10548, "ama_ass": 4542}# Red's testing chan. nsfw content off by default.

#API info:
#example: "/boobs/10/20/rank/" - get 20 boobs elements, start from 10th ordered by rank; noise: "/noise/{count=1; sql limit}/",
#example: "/noise/50/" - get 50 random noise elements; model search: "/boobs/model/{model; sql ilike}/",
#example: "/boobs/model/something/" - get all boobs elements, where model name contains "something", ordered by id; author search: "/boobs/author/{author; sql ilike}/",
#example: "/boobs/author/something/" - get all boobs elements, where author name contains "something", ordered by id; get boobs by id: "/boobs/get/{id=0}/",
#example: "/boobs/get/6202/" - get boobs element with id 6202; get boobs count: "/boobs/count/"; get noise count: "/noise/count/"; vote for boobs: "/boobs/vote/{id=0}/{operation=plus;[plus,minus]}/",
#example: "/boobs/vote/6202/minus/" - negative vote for boobs with id 6202; vote for noise: "/noise/vote/{id=0}/{operation=plus;[plus,minus]}/",
#example: "/noise/vote/57/minus/" - negative vote for noise with id 57;

#example: "/butts/10/20/rank/" - get 20 butts elements, start from 10th ordered by rank; noise: "/noise/{count=1; sql limit}/",
#example: "/noise/50/" - get 50 random noise elements; model search: "/butts/model/{model; sql ilike}/",
#example: "/butts/model/something/" - get all butts elements, where model name contains "something", ordered by id; author search: "/butts/author/{author; sql ilike}/",
#example: "/butts/author/something/" - get all butts elements, where author name contains "something", ordered by id; get butts by id: "/butts/get/{id=0}/",
#example: "/butts/get/6202/" - get butts element with id 6202; get butts count: "/butts/count/"; get noise count: "/noise/count/"; vote for butts: "/butts/vote/{id=0}/{operation=plus;[plus,minus]}/",
#example: "/butts/vote/6202/minus/" - negative vote for butts with id 6202; vote for noise: "/noise/vote/{id=0}/{operation=plus;[plus,minus]}/",
#example: "/noise/vote/57/minus/" - negative vote for noise with id 57;

class oboobs:
    """The oboobs/obutts.ru NSFW pictures of nature cog.
    https://github.com/Canule/Mash-Cogs
    """

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json(SETTINGS)

    @commands.group(name="oboobs", pass_context=True)
    async def _oboobs(self, ctx):
        """The oboobs/obutts.ru pictures of nature cog."""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            return

    # Boobs
    @commands.command(pass_context=True, no_pm=False)
    async def boobs(self, ctx):
        """Shows some boobs."""
        author = ctx.message.author
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True

        try:
            rdm = random.randint(0, self.settings["ama_boobs"])
            search = ("http://api.oboobs.ru/boobs/{}".format(rdm))
            async with aiohttp.get(search) as r:
                result = await r.json()
                boob = random.choice(result)
                boob = "http://media.oboobs.ru/{}".format(boob["preview"])
        except Exception as e:
            await self.bot.reply("Error getting results.")
            return
        if not dis_nsfw:
            await self.bot.say("{}".format(boob))
        else:
            await self.bot.send_message(ctx.message.author, "{}".format(boob))
            if self.settings["nsfw_msg"]:
                await self.bot.reply("nsfw content is not allowed in this channel, instead I have send you a DM.")

    # Ass
    @commands.command(pass_context=True, no_pm=False)
    async def ass(self, ctx):
        """Shows some ass."""
        author = ctx.message.author
        dis_nsfw = None
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                if self.settings["invert"]:
                    dis_nsfw = False
                else:
                    dis_nsfw = True
                break
        if dis_nsfw is None and not self.settings["invert"]:
            dis_nsfw = False
        else:
            dis_nsfw = True

        try:
            rdm = random.randint(0, self.settings["ama_ass"])
            search = ("http://api.obutts.ru/butts/{}".format(rdm))
            async with aiohttp.get(search) as r:
                result = await r.json()
                ass = random.choice(result)
                ass = "http://media.obutts.ru/{}".format(ass["preview"])
        except Exception as e:
            await self.bot.reply("Error getting results.")
            return
        if not dis_nsfw:
            await self.bot.say("{}".format(ass))
        else:
            await self.bot.send_message(ctx.message.author, "{}".format(ass))
            if self.settings["nsfw_msg"]:
                await self.bot.reply("nsfw content is not allowed in this channel, instead I have send you a DM.")

    @checks.admin_or_permissions(manage_server=True)
    @_oboobs.command(pass_context=True, no_pm=True)
    async def nsfw(self, ctx):
        """Toggle oboobs nswf for this channel on/off.
        Admin/owner restricted."""
        nsfwChan = None
        # Reset nsfw.
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                nsfwChan = True
                self.settings["nsfw_channels"].remove(a)
                await self.bot.reply("nsfw ON")
                break
        # Set nsfw.
        if not nsfwChan:
            if ctx.message.channel not in self.settings["nsfw_channels"]:
                self.settings["nsfw_channels"].append(ctx.message.channel.id)
                await self.bot.reply("nsfw OFF")
        dataIO.save_json(SETTINGS, self.settings)
        
    @checks.admin_or_permissions(manage_server=True)
    @_oboobs.command(pass_context=True, no_pm=True)
    async def invert(self, ctx):
        """Invert nsfw blacklist to whitlist
        Admin/owner restricted."""
        if not self.settings["invert"]:
            self.settings["invert"] = True
            await self.bot.reply("The nsfw list for all servers is now: inverted.")
        elif self.settings["invert"]:
            self.settings["invert"] = False
            await self.bot.reply("The nsfw list for all servers is now: default(blacklist)")
        dataIO.save_json(SETTINGS, self.settings)    

    @checks.admin_or_permissions(manage_server=True)
    @_oboobs.command(pass_context=True, no_pm=True)
    async def togglemsg(self, ctx):
        """Enable/Disable the oboobs nswf not allowed message
        Admin/owner restricted."""
        # Toggle
        if self.settings["nsfw_msg"]:
            self.settings["nsfw_msg"] = False
            await self.bot.reply("DM nsfw channel msg is now: Disabled.`")
        elif not self.settings["nsfw_msg"]:
            self.settings["nsfw_msg"] = True
            await self.bot.reply("DM nsfw channel msg is now: Enabled.")
        dataIO.save_json(SETTINGS, self.settings)

    async def boob_knowlegde():
        # KISS
        settings = dataIO.load_json(SETTINGS)
        now = round(time.time())
        interval = 86400*2
        if now >= settings["last_update"]+interval:
            settings["last_update"] = now
            dataIO.save_json(SETTINGS, settings)
        else:
            return
            
        async def search(url, curr):
            search = ("{}{}".format(url, curr))
            async with aiohttp.get(search) as r:
                result = await r.json()
                return result

        # Upadate boobs len
        print("Updating amount of boobs...")
        curr_boobs = settings["ama_boobs"]
        url = "http://api.oboobs.ru/boobs/"
        done = False
        reachable = curr_boobs
        step = 50
        while not done:
            q = reachable+step
            #print("Searching for boobs:", q)
            res = await search(url, q)
            if res != []:
                reachable = q
                res_dc = await search(url, q+1)
                if res_dc == []:
                    settings["ama_boobs"] = reachable
                    dataIO.save_json(SETTINGS, settings)
                    break
                else:
                    await asyncio.sleep(2.5) # Trying to be a bit gentle for the api.
                    continue
            elif res == []:
                step = round(step/2)
                if step <= 1:
                    settings["ama_boobs"] = curr_boobs
                    done = True
            await asyncio.sleep(2.5)
        print("Total amount of boobs:", settings["ama_boobs"])

        # Upadate ass len
        print("Updating amount of ass...")
        curr_ass = settings["ama_ass"]
        url = "http://api.obutts.ru/butts/"
        done = False
        reachable = curr_ass
        step = 50
        while not done:
            q = reachable+step
            #print("Searching for ass:", q)
            res = await search(url, q)
            if res != []:
                reachable = q
                res_dc = await search(url, q+1)
                if res_dc == []:
                    settings["ama_ass"] = reachable
                    dataIO.save_json(SETTINGS, settings)
                    break
                else:
                    await asyncio.sleep(2.5)
                    continue
            elif res == []:
                step = round(step/2)
                if step <= 1:
                    settings["ama_ass"] = curr_ass
                    done = True
            await asyncio.sleep(2.5)
        print("Total amount of ass:", settings["ama_ass"])

def check_folders():
    if not os.path.exists(DIR_DATA):
        print("Creating data/oboobs folder...")
        os.makedirs(DIR_DATA)

def check_files():
    if not os.path.isfile(SETTINGS):
        print("Creating default boobs ass settings.json...")
        dataIO.save_json(SETTINGS, DEFAULT)
    else:  # Key consistency check
        try:
            current = dataIO.load_json(SETTINGS)
        except JSONDecodeError:
            dataIO.save_json(SETTINGS, DEFAULT)
            current = dataIO.load_json(SETTINGS)

        if current.keys() != DEFAULT.keys():
            for key in DEFAULT.keys():
                if key not in current.keys():
                    current[key] = DEFAULT[key]
                    print( "Adding " + str(key) + " field to boobs settings.json")
            dataIO.save_json(SETTINGS, DEFAULT)

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(oboobs(bot))
    bot.loop.create_task(oboobs.boob_knowlegde())
