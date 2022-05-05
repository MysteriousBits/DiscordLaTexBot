@echo off
cd tmp
pdflatex tmp.tex --interaction=nonstopmode -quiet >compile.log
magick convert -background rgb(201,198,193) -flatten -density 300 -quality 95 tmp.pdf tmp.png
magick convert -negate tmp.png tmp.png
cd ..