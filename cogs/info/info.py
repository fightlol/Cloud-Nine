import random
import asyncio
import platform
import datetime, time
import aiohttp
import humanize
import json

from io import BytesIO

from PIL import Image

import discord
from discord.ext import commands

import utility.http as http

import utility.json

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def urban(self, ctx, *, search: commands.clean_content):
        """ Find the 'best' definition to your words """
        async with ctx.channel.typing():
            try:
                url = await http.get(f"https://api.urbandictionary.com/v0/define?term={search}", res_method="json")
            except Exception:
                return await ctx.send("Urban API returned invalid data... might be down atm.")

            if not url:
                return await ctx.send("I think the API broke...")

            if not len(url["list"]):
                return await ctx.send("Couldn't find your search in the dictionary...")

            result = sorted(url["list"], reverse=True, key=lambda g: int(g["thumbs_up"]))[0]

            definition = result["definition"]
            if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(" ", 1)[0]
                definition += "..."

            await ctx.send(f"📚 Definitions for **{result['word']}**\n**{definition}**")

    @commands.command()
    @commands.guild_only()
    async def mods(self, ctx):
        """ Check which mods are online on current guild """
        message = ""
        all_status = {
            "online": {"users": [], "emoji": "🟢"},
            "idle": {"users": [], "emoji": "🟡"},
            "dnd": {"users": [], "emoji": "🔴"},
            "offline": {"users": [], "emoji": "⚫"}
        }

        for user in ctx.guild.members:
            user_perm = ctx.channel.permissions_for(user)
            if user_perm.kick_members or user_perm.ban_members:
                if not user.bot:
                    all_status[str(user.status)]["users"].append(f"**{user}**")

        for g in all_status:
            if all_status[g]["users"]:
                message += f"{all_status[g]['emoji']} {', '.join(all_status[g]['users'])}\n"

        await ctx.send(f"Mods in **{ctx.guild.name}**\n{message}")

    @commands.command()
    async def stats(self, ctx):
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))

        embed = discord.Embed(title = f"{self.bot.user.name}'s stats", description = '\uFEFF', colour = ctx.author.colour, timestamp = ctx.message.created_at)
        embed.add_field(name = "Bot Version: ", value = "0.0.1", inline=False)
        embed.add_field(name = "Python Version ", value=pythonVersion)
        embed.add_field(name = "Discord.py Version: ", value=dpyVersion)
        embed.add_field(name = "Total guilds: ", value=serverCount)
        embed.add_field(name = "Total Members: ", value=memberCount)
        embed.add_field(name = "Uptime ", value=uptime)
        embed.add_field(name = "Bot Developers ", value="<@467631169358528513>")
        await ctx.send(embed = embed)

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        """The obligatory ping command"""
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(
            name="Pong!",
            value=f":ping_pong:{round(self.bot.latency * 1000)}ms",
            inline=True,
        )
        embed.set_footer(text=f"Pong request by {ctx.message.author}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def support(self, ctx):
        """Sends an invite to the bot support server."""
        try:
            await ctx.author.send("https://discord.gg/dwjeKAfX4E")
            await ctx.send('You Have Mail :envelope:')
        except discord.Forbidden:
            await ctx.send(f'I Cannot Direct Message You **{ctx.author.display_name}**')

    @commands.command(alises = ['p'])
    @commands.guild_only()
    async def poll(self, ctx, *args):
        """Make a simple poll."""
        poll_title = " ".join(args)
        embed = discord.Embed(
            title="Poll",
            description=f"**{poll_title}**",
            color=0xFFB6C1,
        )
        embed.set_footer(text=f"Poll created by: {ctx.message.author} • React to vote!")
        embed_message = await ctx.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")

    @commands.command(aliases = ['btc'])
    @commands.guild_only()
    async def bitcoin(self, ctx):
        """Get information about bitcoin."""
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=":information_source: Info",
                description=f"Bitcoin price is: ${response['bpi']['USD']['rate']}",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def av(self, ctx, *, member: discord.Member = None):

        if member == None:
            member = ctx.author

        av = Image.open("assets/av.jpg")

        asset = member.avatar_url_as(size = 256)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((380, 400))

        av.paste(pfp, (97, 73))

        av.save("saves/profile.jpg")

        embed = discord.Embed(description=f"[URL]({member.avatar_url})", colour= ctx.author.color)
        await ctx.send(embed = embed)
        await ctx.send(file = discord.File("saves/profile.jpg"))

    
    @commands.command(alises = ['sav'])
    async def server(self, ctx):
        embed = discord.Embed(
            description=f'[URL]({ctx.guild.icon_url})',
            color=ctx.author.color
        )

        av = Image.open("assets/av.jpg")
        asset = ctx.guild.icon_url_as(size=256)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((380, 400))

        av.paste(pfp, (97, 73))

        av.save("saves/server.jpg")

        embed = discord.Embed(description=f"[URL]({ctx.guild.icon_url})", colour=ctx.author.color)
        await ctx.send(file=discord.File("saves/server.jpg"), embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
    async def createrole(ctx, *, name):
	    guild = ctx.guild
	    await guild.create_role(name=name)
	    await ctx.send(f'Role `{name}` has been created')

    @commands.command(aliases=["uinfo", "memberinfo", "minfo"])
    @commands.guild_only()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def userinfo(self, ctx: commands.context, user: discord.Member = None):
        """Returns info about a user"""
        if user is None:
            user = ctx.author

        user_flags = "\n".join(i.replace("_", " ").title() for i, v in user.public_flags if v)
        roles = user.roles[-1:0:-1]
        embed = discord.Embed(color=user.color or self.bot.ok_color)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Name", value=user)
        embed.add_field(name="ID", value=user.id)
        embed.add_field(
            name="Account Creation",
            value=user.created_at.strftime("%c"),
        )
        embed.add_field(
            name=f"{ctx.guild} Join Date", value=user.joined_at.strftime("%c"), inline=False
        )
        if roles:
            embed.add_field(
                name=f"Roles **{(len(user.roles) - 1)}**",
                value=", ".join([x.mention for x in roles[:10]]),
                inline=False,
            )
        if user_flags:
            embed.add_field(name="Public User Flags", value=user_flags.upper(), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def addrole(self, ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)
        await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")

    @commands.command(aliases=["rinfo"])
    async def roleinfo(self, ctx: commands.Context, *, role: discord.Role):
        """Returns info about a role"""
        await ctx.send(
            embed=discord.Embed(title=f"Role info for {role.name}", color=role.color)
            .add_field(name="ID", value=role.id, inline=True)
            .add_field(name="Color", value=role.color, inline=True)
            .add_field(name="Creation Time", value=role.created_at.strftime("%c"), inline=True)
            .add_field(name="Members", value=len(role.members), inline=True)
            .add_field(name="Hoisted", value=role.hoist, inline=True)
            .add_field(name="Mentionable", value=role.mentionable, inline=True)
            .add_field(name="Position", value=role.position, inline=True)
            .add_field(
                name="Permissions",
                value=f"Click [Here](https://cogs.fixator10.ru/permissions-calculator/?v={role.permissions.value})",
                inline=True,
            )
        )

    @commands.command(aliases=["einfo", "emoteinfo"])
    async def emojiinfo(self, ctx: commands.Context, emoji: discord.Emoji):
        """Returns information about a emoji/emote(Within the current guild)"""
        await ctx.send(
            embed=discord.Embed(title="Emoji Information")
            .add_field(name="ID", value=emoji.id, inline=False)
            .add_field(name="Animated", value=emoji.animated, inline=False)
            .add_field(name="Link", value=emoji.url, inline=False)
            .set_image(url=emoji.url)
        )

    @commands.command()
    async def uptime(self, ctx: commands.Context):
        """Shows bot's uptime."""
        since = self.bot.uptime.strftime("%H:%M:%S UTC | %Y-%m-%d")
        delta = datetime.utcnow() - self.bot.uptime
        uptime_text = humanize.time.precisedelta(delta) or ("Less than one second.")
        embed = discord.Embed(colour=self.bot.ok_color)
        embed.add_field(name=f"{self.bot.user.name} has been up for:", value=uptime_text)
        embed.set_footer(text=f"Since: {since}")
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=["sinfo", "ginfo", "guildinfo"])
    async def serverinfo(self, ctx: commands.Context, guild: discord.Guild = None):
        """Get information about a certain guild"""
        if guild is None:
            guild = ctx.guild

        weird_stuff = {
            "ANIMATED_ICON": ("Animated Icon"),
            "BANNER": ("Banner Image"),
            "COMMERCE": ("Commerce"),
            "COMMUNITY": ("Community"),
            "DISCOVERABLE": ("Server Discovery"),
            "FEATURABLE": ("Featurable"),
            "INVITE_SPLASH": ("Splash Invite"),
            "MEMBER_LIST_DISABLED": ("Member list disabled"),
            "MEMBER_VERIFICATION_GATE_ENABLED": ("Membership Screening enabled"),
            "MORE_EMOJI": ("More Emojis"),
            "NEWS": ("News Channels"),
            "PARTNERED": ("Partnered"),
            "PREVIEW_ENABLED": ("Preview enabled"),
            "PUBLIC_DISABLED": ("Public disabled"),
            "VANITY_URL": ("Vanity URL"),
            "VERIFIED": ("Verified"),
            "VIP_REGIONS": ("VIP Voice Servers"),
            "WELCOME_SCREEN_ENABLED": ("Welcome Screen enabled"),
        }
        guild_features = [
            f"✅ {name}\n"
            for weird_stuff, name in weird_stuff.items()
            if weird_stuff in guild.features
        ]
        embed = discord.Embed(title=guild.name, color=ctx.author.color)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(
            name="Owner", value=f"Name: **{guild.owner}**\nID: **{guild.owner_id}**", inline=True,
        )
        embed.add_field(name="Server ID", value=f"**{guild.id}**", inline=True)
        embed.add_field(name="Creation Time", value=guild.created_at.strftime("%c"), inline=False)
        embed.add_field(name="Region", value=str(guild.region).upper(), inline=True)
        embed.add_field(name="Member Count", value=f"**{guild.member_count}**", inline=True)
        embed.add_field(name="Role Count", value="**{}**".format(len(guild.roles)), inline=False)
        embed.add_field(
            name="Channel Count",
            value=f"Categories: **{len(guild.categories)}**\nText: **{len(guild.text_channels)}**\nVoice: **{len(guild.voice_channels)}**\nTotal: **{len(guild.text_channels) + len(guild.voice_channels)}**",
            inline=True,
        )
        embed.add_field(name="Emoji Count", value="**{}**".format(len(guild.emojis)), inline=True)
        if guild_features:
            embed.add_field(name="Features", value="".join(guild_features), inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))