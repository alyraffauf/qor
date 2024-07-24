clean:
	-find . -name "*.~[0-9]~" -exec rm -f {} \;
	-find . -name "*.py[co]" -exec rm -f {} \;
