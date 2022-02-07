cd tmp
: | pdflatex -halt-on-error tmp.tex | grep '^!.*' -A3 > compile.log
convert -density 300 tmp.pdf -quality 95 tmp.jpg
cd ..