# DiscordLaTexBot

This bot takes user's messages as a latex string(starting with $) and send an image of compiled version.
For this:
  It needs latex installed locally to compile latex string.
  It needs python matplotlib for generating rendered rendered latex.
  It needs python pillow library for some basic image processing in the rendered image(cropping blank white areas).
  
### How to use:
  1. To use this bot, clone this repository.
  2. Install latex distribution in your machine. For linux `sudo apt get install texlive-full` and for other os, grab MikTex from https://miktex.org/download. Make sure latex is added into PATH.
  3. Run `pip install matplotlib pillow discord.py` in terminal
  4. Go to the top of "bot.py" and paste your bot token from discord developper portal inside ""
  5. Run your code and add bot to your discord server.
  6. Include '$' at the beginning of your message including latex code. i.e., `$Here is a fraction $frac{x^2}{y}`

*Hope Some one got it helpful*
