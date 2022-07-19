clean:
	jupyter-book clean itc2

build: clean
	jupyter-book build itc2

run: build
	python3 -m http.server --directory itc2/_build/html 8000