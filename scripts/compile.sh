cd tmp
: | pdflatex -halt-on-error tmp.tex | grep '^!.*' -A3 > compile.log
convert -background 'rgb(201,198,193)' -flatten -density 300 -quality 95 tmp.pdf tmp.png
convert -negate tmp.png tmp.png
cd ..