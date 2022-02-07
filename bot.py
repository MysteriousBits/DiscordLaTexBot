# Make sure to add a file named "config.py" in the same directory
# Add a string variable named "token"
# Set the value to your bot token
from config import token

import discord
from discord import user
from discord import message
from discord import client
from tex2png import texrender
import asyncio


client = discord.Client()

async def handle_tex_message(message):
    text = message.content[5:] #Remove the '$tex ' at beginning
    try:
        texrender(text)
        reply = await message.reply(file = discord.File("tmp/tmp.png"))
    except:
        #Inform user if any problem in compiling
        await message.reply("❗Compilation error")
    
    def check(before, after):
        return before == message

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
        

client.run(token)