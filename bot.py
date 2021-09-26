token = "YourTokenHere"

#import all needed modules
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

#This is a little expensive way but works fine
def latex_to_img(tex):
    buf = io.BytesIO() #memory buffer for image file

    #plot text with latex enabled by matplotlib
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.axis('off')
    plt.text(0.1, 0.5, tex, size=10)
    plt.savefig(buf, format='jpg', dpi=200, bbox_inches = "tight")
    plt.close()

    #Load the image from memory buffer saved by matplotlib
    im = Image.open(buf)
    bg = Image.new("RGB", im.size, color = (255, 255, 255))
    #Make all white areas black and black text white
    diff = ImageChops.difference(im, bg)
    #Tight bounding box around text
    bbox = diff.getbbox()  #Delete areas outside bounding box 
    im.crop(bbox).save('img.jpg') #Save in disk!

    #This are optional, added just to check if there is any memory usage change
    buf.close()
    im.close()
    bg.close()
    diff.close()
    del buf
    del im
    del bg
    del diff
    gc.collect()
    #Test Purpose

#Discord events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("TexTex"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$"):
        text = message.content[1:] #Remove the '$' at beginning
        try:
            latex_to_img(text)
            await message.reply(file = discord.File("img.jpg"))
        except:
            #Inform user if any problem in compiling
            await message.reply("Cant compile latex.")

        #Delete the image from disk after use
        if os.path.exists("img.jpg"):
            os.remove("img.jpg")
        #Test purpose
        gc.collect()
    
client.run(token)