import discord
from discord.ext import commands
from discord import Activity, ActivityType

import os
import datetime
from aiohttp import ClientSession
from pathlib import Path 
import json

import sqlite3
import motor.motor_asyncio

from utility import json as js
import utility.json

from utility.mongo import Document

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n---")

def get_prefix(bot, message):
    data = utility.json.read_json('prefixes')
    if not str(message.guild.id) in data:
        return commands.when_mentioned_or('=')(bot, message)
    return commands.when_mentioned_or(data[str(message.guild.id)])(bot, message)

idk = json.load(open(cwd+'/config/donttouch.json'))
bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=discord.Intents.all())
bot.config_token = idk['shh']

bot.remove_command('help')
@bot.event
async def on_ready():
    print(f"-----\n Logged in as: {bot.user.name} : {bot.user.id}\n-----")
    await bot.change_presence(activity=Activity(name=f"Ping me to get help || In {len(bot.guilds)} servers", 
                                                type=ActivityType.playing))

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if f"<@!{bot.user.id}>" in message.content:
        data = utility.json.read_json('prefixes')
        if str(message.guild.id) in data:
            prefix = data[str(message.guild.id)]
        else:
            prefix = '='
        prefixmsg= await message.channel.send(f"My prefix here is `{prefix}`\n\n Use `{prefix}help` to get help")
        await prefixmsg.add_reaction('👀')


    await bot.process_commands(message)

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs/database"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.database.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs/fun"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.fun.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs/info"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.info.{file[:-3]}")

print("Cloud Nine running...")
bot.run(bot.config_token)