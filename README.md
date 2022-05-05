# DiscordLaTexBot
A discord bot with python to render latex from user's message.

This is a simple bot to add latex rendering functionality to discord. It takes the latex code from user message, compile it locally, convert to image and send back to discord.

### Update
Before it used python matplotlib to render latex and then pillow to do some image processing. But both of them are a little slow and resources hungry.  
Now whole the system has been changed. It natively compiles the latex code to pdf using texlive. Then uses *Image Magick* to convert into image. Also its ready to deploy in heroku.

### Guide To Running
1. Clone the repo and edit `config.py`. (put your bot token in place)
2. ```pip install -r requirements.txt```  
3. Install miketex or texlive distro if you are running locally.  
4. Install Image Magick.  
5. To deploy in heroku, just push it to your own repo and connect with heroku. All packages will be automatically installed. If you want to add more latex package, just add the name into `texlive.packages` file and add `\usepackage{package_name}` in the `scripts/template.tex` file.  
    
Invite the bot to a server and go!

### Guide to Use
Its pretty simple to use. Send `$help` from discord channel to see the commands. Send `$tex <latex code>` to compile. You can edit your message in 1 minute to recompile.
Also it will show the errors if type wrong.

#### Example
This command produce the following
```
$tex Lets call each m people a \emph{Group}, their common friend the \emph{Target} and a group including $P$ a \emph{Good Group}. Suppose $P$ has $k$ friends.
\\\\
\textbf{Claim:} $P$ has $m$ friends or $k=m$.
\\\\
\textbf{Lemma 1:} \emph{Each \emph{Good Group} has a distinct \emph{Target}}
\\
Suppose two \emph{Good Groups} $G_1$ and $G_2$ have same target $T$. Now make a \emph{Group} $G_3$ from the members of $G_1$ and $G_2$ excluding $P$. Now all the members of $G_3$ have 2 \emph{Targets} $T$ and $P$,  which is a contradiction.
\\\\ 
\textbf{Proof:} Suppose, $k > m$. There are $\binom{k}{m-1}$ different \emph{Targets} of all the \emph{Good Groups}  according to Lemma 1. Now all the \emph{Targets} are among those $k$ people as they are friends of $P$. Then $\binom{k}{m-1} \leq k$. But its a contradiction. 
\\
Hence $k=m$. \qed
```
![image](https://user-images.githubusercontent.com/80115356/166906834-237cbfc0-75e1-46a3-bbd3-66d2b603d0f1.png)


  
#### Resources
Image Magick - https://imagemagick.org/script/download.php
Texlive - https://www.tug.org/texlive/
Heroku buildpack - https://elements.heroku.com/buildpacks/thermondo/heroku-buildpack-tex
