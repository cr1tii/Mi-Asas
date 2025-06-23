# this command is made to help who use your bot of how to use the commands , what is the commands and where to type it

import discord
from discord.ext import commands

# API PERMISIONS
intents = discord.Intents.default()

bot = commands.Bot(command_prefix="+",intents=intents)


channel_id = ['your channel id']

async def pics_commands(message):

    if message.author.bot:
        return
    if message.channel.id not in channel_id:
        return

    content = message.content.strip()

    if content == "!help":
        embed = discord.Embed(
                title="YOUR TITLE",
                description=" YOUR COMMANDS DESCRIPTION",
                color=0x00FFFF # you can set another colors as well, its just to make the command more fancy.
                )
        # send the message
        await message.channel.send(embed=embed)
    # if you tried to set an id for the command itself either a user used this command in the same channel you can help him and force him to write the command in the targeted channel:
    elif content == "!":
        Error1 = """
        write this command here :  <#YOUR CHANNEL ID>
        """
        await message.channel.send(Error1)

# BUT I RECOMMEND USING THREADS FOR THESE COMMANDS AS WELL.
