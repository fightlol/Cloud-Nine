import json
import dotenv
import discord
import io
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
from io import BytesIO

class Mod(commands.Cog):
    def __init__(self, commands):
        self.commands = commands

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason='No reason Provided'):
        """Warns a member with the provided reason"""
        with open('databases/warnings.json', 'r') as f:
            warns = json.load(f)
        if str(ctx.guild.id) not in warns:
            warns[str(ctx.guild.id)] = {}
        if str(member.id) not in warns[str(ctx.guild.id)]:
            warns[str(ctx.guild.id)][str(member.id)] = {}
            warns[str(ctx.guild.id)][str(member.id)]["warns"] = 1
            warns[str(ctx.guild.id)][str(member.id)]["warnings"] = [reason]
        else:
            warns[str(ctx.guild.id)][str(member.id)]["warnings"].append(reason)
        with open('warnings.json', 'w') as f:
            json.dump(warns, f)
            await ctx.send(f"{member.mention} was warned for: {reason}")
        print(reason)
        embed = discord.Embed(
        description=str(member + " is warned | Reason = " + reason),
        colour=discord.Colour.blue()
        )
        await ctx.send(embed = embed)

    @commands.command()
    async def warns(self, ctx, member: discord.Member):
        with open('warnings.json', 'r') as f:
            warns = json.load(f)
        num = 1
        warnings = discord.Embed(title=f'{member}\'s warns ', color = ctx.author.color)
        for warn in warns[str(ctx.guild.id)][str(member.id)]["warnings"]:
            warnings.add_field(name=f"Warn {num}", value=warn)
            num += 1
        await ctx.send(embed=warnings)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def removewarn(self, ctx, member: discord.Member, num: int, *, reason='No reason provided.'):
        """Removes specified warn from warnings.json"""
        with open('warnings.json', 'r') as f:
            warns = json.load(f)
        num -= 1
        warns[str(ctx.guild.id)][str(member.id)]["warns"] -= 1
        warns[str(ctx.guild.id)][str(member.id)]["warnings"].pop(num)
        with open('warnings.json', 'w') as f:
            json.dump(warns, f)
            await ctx.send('Warn has been removed!')
            embed = discord.Embed(title='Your warn has been removed',
                                  description=f'Your warning was removed by {ctx.author}')
            await member.send(embed=embed)

    @commands.command(alises = ['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):
        """Kicks the mentioned member"""
        print(reason)
        embed = discord.Embed(
            description=str(
                str(member) + " is Kicked | reason = " + reason),
            colour=discord.Colour.green()
        )
        await member.kick(reason=reason)
        await member.send(embed=embed)
        await ctx.channel.send(embed = embed)

    @commands.command(alises = ['b'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        """Bans the mentioned member"""
        print(reason)
        embed = discord.Embed(
            description=str(
                str(member) + " is banned | reason = " + reason),
            colour=discord.Colour.green()
        )
        await member.ban(reason=reason)
        await member.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason):
        """Gives muted role to the mentioned user"""
        print(reason)
        Muted = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(Muted)
        embed = discord.Embed(
            description=str(
                str(member) + " is Muted | reason = " + reason),
            colour=discord.Colour.red()
        )
        await member.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member, *, reason="No reason specified"):
        """Unmutes the mentioned member"""
        print(reason)
        Muted = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(Muted)
        embed = discord.Embed(
            description=str(
                str(member) + " is Unmuted | reason = " + reason),
            colour=discord.Colour.green()
        )
        await member.send(embed=embed)

    @commands.command(aliases=["purge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, args):
        await ctx.channel.purge(limit=int(args) + 1)

    @commands.command(aliases =["ub"])
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, id: int):
        user = await commands.fetch_user(id)
        await ctx.guild.unban(user)

def setup(bot):
    bot.add_cog(Mod(bot))
