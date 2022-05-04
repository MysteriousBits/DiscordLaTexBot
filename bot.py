"""
Make sure to add a file named "config.py" in the same directory
Add a string variable named "token"
Set the value to your bot token
"""

from config import token
import discord
import asyncio
from discord import user
from discord.message import Message
from discord.client import Client
from tex2png import *

client: Client = discord.Client(status = discord.Status.invisible, activity = discord.Game("TexRender"))

async def handle_tex_message(message: Message):
    spoiler = message.content.startswith("$texsp")
    text = message.content[5:] if not spoiler else message.content[7:] #Remove the '$tex ' or '$texsp ' at beginning
    try:
        texrender(text)
        file = discord.File("tmp/tmp.jpg")
        if spoiler:
            file.filename = f"SPOILER_{file.filename}"

        reply = await message.reply("✅Compiled successfully. You can edit your message in 1 minute to recompile.",
                                        file = file,
                                    ) 

    except:
        reply = await message.reply("❗Compilation error\n```\n" + get_error() + "\n```")
    
    def check(before, after):
        return before == message

    # Wait for user to edit
    try:
        before, after = await client.wait_for('message_edit', timeout = 60.0, check = check)
    except asyncio.TimeoutError:
        await message.add_reaction('⏹️')
    else:
        if reply is not None: await reply.delete()
        await handle_tex_message(after)


#Discord events
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    # Command prefix "$tex"
    if message.content.startswith("$tex"):
        await handle_tex_message(message)

    elif message.content.startswith("$help"):
        await message.channel.send("Command syntex: `$tex <latex code>`\nYou can edit you message in 1 minute to recompile.")
        

client.run(token)
