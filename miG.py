# important, this is a main file so if youre using more than a command  under @bot.command or @bot.event,  u set all your commands under one @bot.event so it makes the bot run faster.


import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

# here you summon your command from the file
from CD import your_command

#API's
intents = discord.Intents.default()
intents.message_content=True

#command perfix
bot = commands.Bot(command_prefix="!", intents=intents)

# here you set your command
@bot.event
async def on_message(message):
    await your_command(message)

# make sure youre putting your discord token in a env file in the same mkdir so you can summon it, just for a more privacy.
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
