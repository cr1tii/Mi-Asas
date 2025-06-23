import os
import random
import discord


async def BOT_COMMAND(message):

    # make sure the bot wont answer any ohter bots from the same CHANNEL
    if message.author.bot:
        return
    # your message or command
    content = message.content.strip()
    
    if content == "i" or content == "I":
        
        # summon the pictrues from your Gallery file
        image_files = [f for f in os.listdir("Pins") if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

        # set a random picture
        if image_files:
            filename = random.choice(image_files)
            await message.channel.send(file=discord.File(f"Pins/{filename}"))


    elif content.startswith("i") or content.startswith("I") and content[1:].isdigit():
        count = int(content[1:])
        
        # here should be how many pics you got in the file , for example got 100
        if 1 <= count <= 1066:
            image_files = [f for f in os.listdir("Pins") if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

            # here i used random sample so if i wanted more than a 10 pics it doesnt get repeated while the bot is sneding it.
            k1 = count
            filename = random.sample(image_files,k=k1)
            # a For loop so he can send more than a 1 pic
            for fname in filename:
                    await message.channel.send(file=discord.File(f"Pins/{fname}"))

        # expect Errors:
        else:
            await message.channel.send("Error: number is out of range, try: !help")
