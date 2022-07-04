clean:
	rm -rf book/_build

build: clean
	jupyter-book build book

run: build
	python3 -m http.server --directory book/_build/html 8001