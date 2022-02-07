import os

# Change it according to os
# Linux
shell_command = "chmod u+x ./scripts/compile.sh && ./scripts/compile.sh"
# Windows
# shell_command = "scripts\\compile.bat"

def texrender(msg):
    template = open("scripts/template.tex", 'r')
    tex = template.read()
    template.close()

    tex += msg + "\n\n\\end{document}"
    
    tmptex = open("tmp/tmp.tex", 'w')
    tmptex.write(tex)
    tmptex.close()

    os.system(shell_command)

    if not os.path.exists("tmp/tmp.pdf"): raise Exception("Compile error")
    else : os.remove("tmp/tmp.pdf")

def get_error():
    output = open("tmp/compile.log", 'r')
    error = output.read()
    output.close()
    return error