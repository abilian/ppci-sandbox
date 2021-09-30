.PHONY:
all:
	doit

.PHONY:
clean:
	doit clean
	rm -rf __pycache__

.PHONY:
run:
	python mandelbrot-jit.py
