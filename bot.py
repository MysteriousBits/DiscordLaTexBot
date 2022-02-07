# Make sure to add a file named "config.py" in the same directory
# Add a string variable named "token"
# Set the value to your bot token
from config import token

import discord
from discord import user
from discord import message
from discord import client
from tex2png import *
import asyncio


client = discord.Client()

async def handle_tex_message(message):
    text = message.content[5:] #Remove the '$tex ' at beginning
    try:
        texrender(text)
        reply = await message.reply("✅Compiled successfully. You can edit your message in 1 minute to recompile.", file = discord.File("tmp/tmp.jpg"))
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
        if reply != None: await reply.delete()
        await handle_tex_message(after)


#Discord events
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("TexRender"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # Command prefix "$tex"
    if message.content.startswith("$tex"):
        await handle_tex_message(message)
    
    elif message.content.startswith("$help"):
        await message.channel.send("Command syntex: `$tex <latex code>`\nYou can edit you message in 1 minute to recompile.")
        

client.run(token)