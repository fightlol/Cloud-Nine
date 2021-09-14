import discord
import aiohttp 

import random

from discord.ext import commands


class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def neko(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/neko") as r:
                neko = (await r.json())["url"]

                embed = discord.Embed(description=f"**Here is a random neko pic**", color = ctx.author.color)
                embed.set_image(url=neko)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def waifu(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/waifu") as r:
                waifu = (await r.json())["url"]

                embed = discord.Embed(description=f"**Here is a random waifu pic**", color = ctx.author.color)
                embed.set_image(url=waifu)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def megumin(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/megumin") as r:
                megumin = (await r.json())["url"]

                embed = discord.Embed(description=f"**Megumin?**", color = ctx.author.color)
                embed.set_image(url=megumin)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def shinobu(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/shinobu") as r:
                megumin = (await r.json())["url"]

                embed = discord.Embed(description=f"**Shinobu?**", color = ctx.author.color)
                embed.set_image(url=megumin)
                await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Anime(bot))