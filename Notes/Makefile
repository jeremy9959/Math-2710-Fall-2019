all : Week1.html Week1.pdf

%.html : %.md
#	pandoc -s --mathjax -t revealjs $< -o $@ -V revealjs-url=https://revealjs.com -V theme=simple
	pandoc -s --mathjax -t slidy $< -o $@ 

%.pdf : %.md
	pandoc -s --mathjax -t beamer $< -o $@

install : all
	cp *.html *.pdf ../blackboard

