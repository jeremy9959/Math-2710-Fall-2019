all: Homework.html

%.html : %.md
	pandoc -s -t latex $< -o $@

%.pdf : %.md
	pandoc -s -t beamer $< -o $@

install :
	cp *.html *.pdf ../blackboard
