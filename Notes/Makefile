all : Week1.html Week1.pdf Week1.md Week2.html Week2.pdf Week2.html Week3.html Week3.md Week3.pdf Week4.md Week4.html Week4.pdf Week6.md Week6.html Week6.pdf

%.html : %.md
	pandoc -s --mathjax -t slidy $< -o $@   

%.pdf : %.md
	pandoc -s --mathjax -t latex $< -o $@

install : all
	cp *.html *.pdf ../blackboard

