# important, this is a main file so if youre using more than a command  under @bot.command or @bot.event,  u set all your commands under one @bot.event so it makes the bot run faster.


import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

# here you summon your command from the file
from CDG import BOT_COMMAND

#API's
intents = discord.Intents.default()
intents.message_content=True

#command perfix
bot = commands.Bot(command_prefix="!", intents=intents)

channel_id = None
# here you set your command
@bot.event
async def on_message(message): 
    global channel_id

    content = message.content.strip()
    if content == "set-channel":
        await message.channel.send("type your id channel")
        msg = await bot.wait_for("Message",timeout=None)
        try:
            channel_id = int(msg.content)
            await message.channel.send(f"successfully saved channel id , channel is: <#{channel_id}>")
        except ValueError:
            await message.channel.send("Error: invalid number")
            return
            
        
    if channel_id is not None and message.channel.id == channel_id:
        await BOT_COMMAND(message)

# make sure youre putting your discord token in a env file in the same mkdir so you can summon it, just for a more privacy.
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
