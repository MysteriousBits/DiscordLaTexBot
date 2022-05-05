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

client: Client = discord.Client(status = discord.Status.idle, activity = discord.Game("TexRender"))

async def handle_tex_message(message: Message):
    spoiler = message.content.startswith("$texsp")
    text = message.content[5:] if not spoiler else message.content[7:] #Remove the '$tex ' or '$texsp ' at beginning
    info_msg = None
    image_msg = None

    try:
        texrender(text)
        file = discord.File("tmp/tmp.png")
        if spoiler:
            file.filename = f"SPOILER_{file.filename}"

        info_msg = await message.reply("✅Compiled successfully. You can edit your message in 1 minute to recompile or react ❌ to delete.")
        image_msg = await message.channel.send(f"**{message.author.display_name}**", file = file)
        await image_msg.add_reaction("❌")

    except:
        info_msg = await message.reply("❗Compilation error\n```\n" + get_error() + "\n```")


# --------------------------------------------------------------------------------------------------

    # Check if the message is edited or ❌ readtion is added
    def check_react(reaction, user):
        return reaction.message == image_msg and user == message.author and str(reaction.emoji) == '❌'
    def check_edit(before, after):
        return before == message

    # Wait 1 minutes for the user
    done, pending = await asyncio.wait([
                        client.loop.create_task(client.wait_for('message_edit', timeout = 60.0, check = check_edit)),
                        client.loop.create_task(client.wait_for('reaction_add', timeout = 60.0, check = check_react))
                    ], return_when = asyncio.FIRST_COMPLETED)

    for future in done:
        future.exception()
    for future in pending:
        future.cancel()

    try:
        stuff = done.pop().result()

        # If reacted "❌"
        if type(stuff[0]) == discord.Reaction:
            try:
                await image_msg.delete()
                await info_msg.delete()
                await message.add_reaction('⏹️')
            except:
                pass
        # If edited, delete and resend
        else:
            try:
                await info_msg.delete()
                await image_msg.delete()
            except:
                pass
            await handle_tex_message(stuff[1])
        
    except asyncio.TimeoutError:
        try:
            await info_msg.delete()
            await message.add_reaction('⏹️')
        except:
            pass
        try:
            await image_msg.clear_reaction('❌')
        except discord.errors.Forbidden:
            await image_msg.remove_reaction('❌', client.user)
        except:
            pass

# ---------------------------------------------------------------------------------------


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
        await message.channel.send("Command syntex: `$tex <latex code>`\nYou can edit you message in 1 minute to recompile.\n`$texsp <latex code> for spoilered image.`")
        

client.run(token)