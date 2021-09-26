token = "YourTokenHere"

import discord
import os
from discord import user
from discord import message
from discord import client
import matplotlib.pyplot as plt
import io
from PIL import Image, ImageChops
import gc

client = discord.Client()

def latex_to_img(tex):
    buf = io.BytesIO()
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.axis('off')
    plt.text(0.1, 0.5, tex, size=10)
    plt.savefig(buf, format='jpg', dpi=200, bbox_inches = "tight")
    plt.close()

    im = Image.open(buf)
    bg = Image.new("RGB", im.size, color = (255, 255, 255))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    im.crop(bbox).save('img.jpg')

    buf.close()
    im.close()
    bg.close()
    diff.close()
    del buf
    del im
    del bg
    del diff
    gc.collect()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("TexTex"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$"):
        text = message.content[1:]
        try:
            latex_to_img(text)
            await message.reply(file = discord.File("img.jpg"))
        except:
            await message.reply("Cant compile latex.")
        if os.path.exists("img.jpg"):
            os.remove("img.jpg")
        gc.collect()
    


client.run(token)