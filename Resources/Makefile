all : links.html

%.html : %.md
	pandoc -s $< -o $@

install : links.html
	cp $< ../blackboard/Resources
