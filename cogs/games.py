import random
import asyncio

import discord
from discord.ext import commands

from games import minesweeper, wumpus, twenty

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball")
    async def _8ball(self, ctx, ques=""):
        if ques=="":
            await ctx.send("Ask me a question first")
        else:
            choices = [
            'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.', 'You may rely on it.',
            'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
            'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
            "Don't count on it.", 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.'
            ]
            embed = discord.Embed(title = f"{ctx.author.name} is playing 8Ball", colour = ctx.author.colour)
            embed.add_field(name = "**Question:**", value= str(ques),inline= False)
            embed.add_field(name = ":8ball: **says:**", value= f"||{random.choice(choices)}||", inline= False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed = embed)

    @commands.command(name='minesweeper', aliases=['ms'])
    async def minesweeper(self, ctx, columns = None, rows = None, bombs = None):
        """Play Minesweeper"""
        await minesweeper.play(ctx, columns, rows, bombs)

    @commands.command(name='rps', aliases=['rockpaperscissors'])
    async def rps(self, ctx):
        def check_win(p, b):
            if p=='🌑':
                return False if b=='📄' else True
            if p=='📄':
                return False if b=='✂' else True
            # p=='✂'
            return False if b=='🌑' else True

        async with ctx.typing():
            reactions = ['🌑', '📄', '✂']
            game_message = await ctx.send("**Rock Paper Scissors**\nChoose:", delete_after=15.0)
            for reaction in reactions:
                await game_message.add_reaction(reaction)
            bot_emoji = random.choice(reactions)

        def check(reaction, user):
            return user != self.bot.user and user == ctx.author and (str(reaction.emoji) == '🌑' or '📄' or '✂')
        try:
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Time's Up! :stopwatch:")
        else:
            await ctx.send(f"**{ctx.author.name} chose =\t{reaction.emoji}\nI chose =\t{bot_emoji}**")
            # if conds
            if str(reaction.emoji) == bot_emoji:
                await ctx.send("**It's a Tie :ribbon:**")
            elif check_win(str(reaction.emoji), bot_emoji):
                await ctx.send("**You win :sparkles:**")
            else:
                await ctx.send("**I win :cloud:**")

    @commands.command(name='wumpus')
    async def _wumpus(self, ctx):
        await wumpus.play(self.bot, ctx)

    @commands.command()
    async def twenty(self, ctx):
        """Play 2048 game"""
        await twenty.play(ctx, self.bot)

    @commands.command(aliases=['team'])
    async def teams(self, ctx, num=2):
        """Makes random teams with specified number(def. 2)"""
        if not ctx.author.voice:
            return await ctx.send("You are not connected to a voice channel :mute:")
        members = ctx.author.voice.channel.members
        memnames = []
        for member in members:
            memnames.append(member.name)

        remaining = memnames
        if len(memnames)>=num:
            for i in range(num):
                team = random.sample(remaining,len(memnames)//num)
                remaining = [x for x in remaining if x not in team]
                await ctx.send(f"Team {chr(65+i)}\n" + "**" + '\n'.join(team) + "\n**")
        if len(remaining)> 0:
            await ctx.send("Remaining\n```diff\n- " + '\n- '.join(remaining) + "\n```")

    @commands.command(aliases=['flip'])
    async def toss(self, ctx):
        """Flips a Coin"""
        coin = ['+ heads', '- tails']
        await ctx.send(f"**{random.choice(coin)}\n**")
def setup(bot):
    bot.add_cog(Game(bot))