all: Homework.html

%.html : %.md
	pandoc -s --mathjax $< -o $@

%.pdf : %.md
	pandoc -s -t beamer $< -o $@

install :
	cp *.html *.pdf ../blackboard
