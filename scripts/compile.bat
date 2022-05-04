@echo off
cd tmp
pdflatex tmp.tex --interaction=nonstopmode -quiet >compile.log
magick convert -density 300 tmp.pdf -quality 95 tmp.jpg
cd ..
