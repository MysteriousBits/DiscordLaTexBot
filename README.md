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
6. To deploy in heroku, just push it to your own repo and connect with heroku. All packages will be automatically installed. If you want to add more latex package, just add the name into `texlive.packages` file and add `\usepackage{package_name}` in the `scripts/template.tex` file.  
    
Invite the bot to a server and go!

### Guide to Use
Its pretty simple to use. Send `$help` from discord channel to see the commands. Send `$tex <latex code>` to compile. You can edit your message in 1 minute to recompile.
Also it will show the errors if type wrong.

#### Example
This command (code from overleaf example) produce the following
```
$tex $tex \begin{abstract}
\LaTeX{} is the best way to write mathematics. It completely pisses all over Word. However, it does take some time to get used to so might not be worth your while if you won't write too much. The way I use it is to first download and install a latex editor and then get writing, but I would recommend that you use this website instead since you can get going a lot quicker. The upshot of the whole business is that you type in here and then a pdf is generated with all the equations looking ace. I'll give you some examples. 
\end{abstract}

\section{Writing some mathematics}

\LaTeX{} is great at typesetting mathematics. Let's say you want to write some equations involving integrals. You have to first setup and ``equation environment'' and then plug in the correct commands for the integral signs etc. An example is the following.
\begin{equation}
        y(s) = \int_0^1 \left(t^2+\ln(t)+\frac{1}{t}\right)\text{d}t.
\end{equation}
Here I've used a the command text to get the straight d in the integral which is usually used to denote the infinitesimal in integration, but this doesn't really matter. 

How about if you want to write a differential equation. 
\begin{equation}
        \frac{\text{d}^2y}{\text{d}x^2}+ x^3\frac{\text{d}y}{\text{d}x}+y = e^{3x}.
\end{equation}
You can see that the frac command is pretty handy here.

If you want to learn more. Try googling ``Latex for beginners'' or something and then taking it from there. It requires an investment of time to get used to Latex but is really worth it in the longrun if you are going to write lots of mathematics. Every scientist and engineer in the world uses this software so it's not just small peanuts!

Anyway, hope this is helpful and that the tone isn't too patronising!

Sam
```
![image](https://user-images.githubusercontent.com/80115356/152975794-0dc5d281-2cc4-491a-a80c-dff2f8569a08.png)

  
#### Resources
Image Magick - https://imagemagick.org/script/download.php
Texlive - https://www.tug.org/texlive/
Heroku buildpack - https://elements.heroku.com/buildpacks/thermondo/heroku-buildpack-tex
