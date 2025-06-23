
import os
import random
import discord

channel_id = ['your channel id']

async def your_command(message):
    
    # make sure the bot wont answer any ohter bots from the same channel
    if message.author.bot:
        return
    # make sure its the wanted channel.
    if message.channel.id not in channel_id:
        return
    # your message or command
    content = message.content.strip()
    
    if content == "!":
        
        # summon the pictrues from your Gallery file
        image_files = [f for f in os.listdir("yourFileName") if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

        # set a random picture
        if image_files:
            filename = random.choice(image_files)
            await message.channel.send(file=discord.File(f"yourFileaName/{filename}"))


    elif content.startswith("!") and content[1:].isdigit():
        count = int(content[1:])
        
        # here should be how many pics you got in the file , for example got 100
        if 1 <= count <= 101:
            image_files = [f for f in os.listdir("yourFileName") if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

            # here i used random sample so if i wanted more than a 10 pics it doesnt get repeated while the bot is sneding it.
            k1 = count
            filename = random.sample(image_files,k=k1)
            # a For loop so he can send more than a 1 pic
            for fname in filename:
                    await message.channel.send(file=discord.File(f"yourFileName/{fname}"))

        # expect Errors:
        else:
            await message.channel.send("Error: number is out of range, try: !help")
