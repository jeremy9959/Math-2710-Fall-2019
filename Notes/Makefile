all : Week1.html Week1.pdf

%.html : %.md
	pandoc -s --mathjax -t revealjs $< -o $@ -V revealjs-url=https://revealjs.com -V theme=simple

%.pdf : %.md
	pandoc -s --mathjax -t beamer $< -o $@

install : 
	rsync -uv *.html *.pdf ../blackboard

