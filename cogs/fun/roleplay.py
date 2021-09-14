import discord
import aiohttp  # requests are gey. dey blocking

import random



from discord.ext import commands
from discord.ext.commands.core import command

npa = ""  # default value for the args param if not passed in by a user


class Roleplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # copy and pasting time bois
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx, member:discord.Member, *, args = npa):
        """Pats a user!"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/pat") as r:

                pat = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"**{ctx.author.name}** pats **{member.name}**", color = ctx.author.color
                )
                embed.set_image(url=pat)
                await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    async def hug(self, ctx, member:discord.Member, *, args = npa):
        """Hug someone!"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/hug") as r:

                hug = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"**{ctx.author.name}** hugs **{member.name}**", color = ctx.author.color
                )
                embed.set_image(url=hug)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def cuddle(self, ctx, member:discord.Member, *, args = npa):
        """Cuddle with someone!"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/cuddle") as r:

                cuddle = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"**{ctx.author.name}** cuddles **{member.name}**", color = ctx.author.color
                )
                embed.set_image(url=cuddle)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def lick(self, ctx, member:discord.Member, *, args = npa):
        """Lick someone."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/lick") as r:

                lick = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"**{ctx.author.name}** licks **{member.name}**... gross", color = ctx.author.color
                )
                embed.set_image(url=lick)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def bully(self, ctx, member:discord.Member, *, args = npa):
        """Bully someone :imp:"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/bully") as r:

                bully = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"**{ctx.author.name}** bullies **{member.name}**...",color = ctx.author.color
                )
                embed.set_image(url=bully)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def poke(self, ctx, member:discord.Member, *, args = npa):
        """Boop Boop."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/poke") as r:

                poke = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"**{ctx.author.name}** pokes **{member.name}**", color = ctx.author.color
                )
                embed.set_image(url=poke)
                await ctx.send(embed=embed)

   

    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx, member:discord.Member, *, args = npa):
        """Slap someone."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/slap") as r:

                slap = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"**{ctx.author.name}** slaps **{member.name}**", color = ctx.author.color
                )
                embed.set_image(url=slap)
                await ctx.send(embed=embed)

   
    @commands.command()
    @commands.guild_only()
    async def smug(self, ctx):
        """Be smug ig.."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/smug") as r:

                smug = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"**{ctx.author.name}** has a smug look", color = ctx.author.color
                )
                embed.set_image(url=smug)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def kiss(self, ctx, member:discord.Member, *, args = npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/kiss") as r:

                kiss = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** kissed **{member.name}**", color = ctx.author.color)
                embed.set_image(url=kiss)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def cry(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/cry") as r:
                cry = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} is crying :(", color = ctx.author.color)
                embed.set_image(url=cry)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def bonk(self, ctx, member:discord.Member, *, args = npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/bonk") as r:
                bonk = (await r.json()) ["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** bonked **{member.name}**", color = ctx.author.color)
                embed.set_image(url=bonk)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def yeet(self, ctx, member:discord.Member, *, args = npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/yeet") as r:
                yeet = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** yeeted **{member.name}** into the void", color = ctx.author.color)
                embed.set_image(url=yeet)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def highfive(self, ctx, member:discord.Member, *, args = npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/highfive") as r:
                highfive = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** highfives **{member.name}**", color = ctx.author.color)
                embed.set_image(url=highfive)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def blush(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/blush") as r:
                blush = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** is blushing ///w///", color = ctx.author.color)
                embed.set_image(url=blush)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def smile(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/smile") as r:
                smile = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** is smiling aww :>", color = ctx.author.color)
                embed.set_image(url=smile)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def wave(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/wave") as r:
                wave = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** is waving... hii", color = ctx.author.color)
                embed.set_image(url=wave)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def happy(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/happy") as r:
                happy = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** is happy!", color = ctx.author.color)
                embed.set_image(url=happy)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def dance(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/dance") as r:
                dance = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** got some moves!", color = ctx.author.color)
                embed.set_image(url=dance)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def cringe(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/cringe") as r:
                cringe = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** cringed oww >:(", color = ctx.author.color)
                embed.set_image(url=cringe)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def nom(self, ctx):
        """Slap someone."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/nom") as r:
                nom = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"**{ctx.author.name}** is eating", color = ctx.author.color
                )
                embed.set_image(url=nom)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def bite(self, ctx, member:discord.Member, *, args = npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/bite") as r:
                bite = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** bit **{member.name}**", color = ctx.author.color)
                embed.set_image(url=bite)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def glomp(self, ctx, member:discord.Member, *, args = npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/glomp") as r:
                glomp = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** glomps **{member.name}**", color = ctx.author.color)
                embed.set_image(url=glomp)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def kill(self, ctx, member:discord.Member, *, args = npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/kill") as r:
                kill = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** killed **{member.name}**", color = ctx.author.color)
                embed.set_image(url=kill)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def wink(self, ctx, member:discord.Member, *, args = npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/wink") as r:
                wink = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** winked at **{member.name}**", color = ctx.author.color)
                embed.set_image(url=wink)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def facepalm(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/face_palm") as r:
                wink = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** face palmed... smh", color = ctx.author.color)
                embed.set_image(url=wink)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def handhold(self, ctx, member:discord.Member):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/handhold") as r:
                wink = (await r.json())["url"]

                embed = discord.Embed(description=f"**{ctx.author.name}** is holding **{member.name}'s** hands", color = ctx.author.color)
                embed.set_image(url=wink)
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Roleplay(bot))