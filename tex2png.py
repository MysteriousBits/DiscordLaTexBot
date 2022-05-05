import os
import platform

if platform.system() == "Windows":
    shell_command = "scripts\\compile.bat"
else:
    shell_command = "chmod u+x ./scripts/compile.sh && ./scripts/compile.sh"

# Another method of getting os name
# But it should be avoided
# Because it returns 'posix' for both Linux and MacOS
# However it is not a problem for now because we are either using Windows batchfile or shell script
#
# If you don't prefer platform module, you can use this method 
#if os.name == "nt":
#    shell_command = "scripts\\compile.bat"
#else:
    #shell_command = "chmod u+x ./scripts/compile.sh && ./scripts/compile.sh"

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