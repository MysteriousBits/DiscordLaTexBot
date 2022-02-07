from pdf2image import convert_from_path
import os

def texrender(msg):
    template = open("scripts/template.tex", 'r')
    tex = template.read()
    template.close()

    tex += msg + "\n\n\\end{document}"
    
    tmptex = open("tmp/tmp.tex", 'w')
    tmptex.write(tex)
    tmptex.close()

    os.system("scripts\\compile.bat")
    image = convert_from_path("tmp/tmp.pdf")
    image[0].save("tmp/tmp.png")