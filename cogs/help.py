import discord
from discord.ext import commands 

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title = "Help Commands", description = "Here are the list of commands", color = ctx.author.color)
        embed.add_field(name = ":slot_machine: Fun", value="`slot` `lovecalc` `combile` `beer` `hotcalc` `pokedex` `howgay` `drunkify` `expand` `reverse` `roast`", inline= False)
        embed.add_field(name = ":game_die: Games", value= "`8ball` `minesweeper` `rps` `toss` `twenty` `wumpus`", inline= False)
        embed.add_field(name = ":camera: Images", value =  "Usage: `image <category>` \n **Categories**\n `dog` `cat` `panda` `bird` `fox` `koala`", inline= False)
        embed.add_field(name = ":woman_in_tuxedo: Anime", value= "`waifu` `neko` `shinobu` `megumin`", inline= False)
        embed.add_field(name = ":loop: Misc", value= "`av` `server`", inline= False)
        embed.add_field(name = ":newspaper: Information", value="`stats` `serverinfo` `userinfo` `roleinfo` `mods` `ping` `urban`", inline= False)
        embed.add_field(name = ":person_in_tuxedo: Moderation", value ="`warn` `warns` `removewarn` `kick` `ban` `unban` `clear`", inline= False)
        embed.add_field(name = ":cloud: Quotes", value="`quote` `compliment` `dogfact` `catfact` `foxfact` `koalafact` `birdfact` `pandafact`", inline= False)
        embed.add_field(name = ":play_pause: Roleplay", value="`hug` `slap` `kiss` `kill` `bite` `blush` `cringe` `cry` `bonk` `bully` `cuddle` `dance` `facepalm` `glomp` `happy` `highfive` `lick` `nom` `pat` `poke` `slap` `smile` `smug` `wake` `wink` `yeet` `handhold`", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        embed.add_field(name = ":gear: Config", value="`prefix`", inline= False)
        await ctx.send(embed = embed)
def setup(bot):
    bot.add_cog(help(bot))