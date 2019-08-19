all : Week1.html Week1.pdf Week1.md

%.html : %.md
	pandoc -s --mathjax -t slidy $< -o $@   

%.pdf : %.md
	pandoc -s --mathjax -t beamer $< -o $@

install : 
	rsync -uv *.html *.pdf ../blackboard

