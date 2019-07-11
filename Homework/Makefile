all: Homework.html

%.html : %.md
	pandoc -s $< -o $@

%.pdf : %.md
	pandoc -s -t beamer $< -o $@

install :
	cp *.html *.pdf ../blackboard
