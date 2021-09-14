import os
import io
import ksoftapi
from googletrans import Translator, LANGUAGES
from textwrap import TextWrapper

import random

import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.trans = Translator()

    @commands.command()
    async def listusers(self, ctx):
        """Displays the list of connected users"""
        if not ctx.author.voice:
            return await ctx.send("You are not connected to a voice channel :mute:")
        members = ctx.author.voice.channel.members
        memnames = []
        for member in members:
            memnames.append(member.name)
        embed = discord.Embed(title = f"Members in *{ctx.author.voice.channel.name}*", color = ctx.author.color)
        embed.add_field(name= "List of users", value= f"**\n" + "\n".join(memnames) + "**")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @commands.command(no_pm=True)
    async def whosplaying(self, ctx, *, game):
        """Shows who's playing a specific game"""
        if len(game) <= 1:
            await ctx.send("```The game should be at least 2 characters long...```", delete_after=5.0)
            return

        guild = ctx.message.guild
        members = guild.members
        playing_game = ""
        count_playing = 0

        for member in members:
            if not member:
                continue
            if not member.activity or not member.activity.name:
                continue
            if member.bot:
                continue
            if game.lower() in member.activity.name.lower():
                count_playing += 1
                if count_playing <= 15:
                    emote = random.choice([":trident:", ":high_brightness:", ":low_brightness:", ":beginner:",
                                           ":diamond_shape_with_a_dot_inside:"])
                    playing_game += f"{emote} {member.name} ({member.activity.name})\n"

        if playing_game == "":
            await ctx.send("Search results:\nNo users are currently playing that game.")
        else:
            msg = playing_game
            if count_playing > 15:
                showing = "(Showing 15/{})".format(count_playing)
            else:
                showing = "({})".format(count_playing)

            em = discord.Embed(description=msg, colour=discord.Colour(value=0x36393e))
            em.set_author(name=f"""Who's playing "{game}"? {showing}""")
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Utility(bot))