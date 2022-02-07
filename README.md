# DiscordLaTexBot
A discord bot with python to render latex from user's message.

This is a simple bot to add latex rendering functionality to discord. It takes the latex code from user message, compile it locally, convert to image and send back to discord.

### Update
Before it used python matplotlib to render latex and then pillow to do some image processing. But both of them are a little slow and resources hungry.  
Now whole the system has been changed. It natively compiles the latex code to pdf using texlive. Then uses *Image Magick* to convert into image. Also its ready to deploy in heroku.

### Guide To Running
1. Clone the repo and edit `config.py`. (put your bot token in place)
2. If you are on windows, edit `tex2png.py`. (Uncomment the shell command to execute batch script and comment/remove the line for shell script in linux.)  
3. ```pip install -r requirements.txt```  
4. Install miketex or texlive distro if you are running locally.  
5. Install Image Magick.  
6. To deploy in heroku, just push it to your own repo and connect with heroku. All packages will be automatically installed.  
Invite the bot to a server and go!

### Guide to Use
Its pretty simple to use. Send `$help` from discord channel to see the commands. Send `$tex <latex code>` to compile. You can edit your message in 1 minute to recompile.
Also it will show the errors if type wrong.

#### Resources
Image Magick - https://imagemagick.org/script/download.php
Texlive - https://www.tug.org/texlive/
Heroku buildpack - https://elements.heroku.com/buildpacks/thermondo/heroku-buildpack-tex
