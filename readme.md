Sandbox for experimenting with PPCI
===================================


Note: The ppci (pure python compiler infrastructure) project is a compiler written entirely in python.


More info:

- <https://github.com/windelbouwman/ppci>
- <https://ppci.readthedocs.io/en/latest/>


## 1) Install:

```
poetry shell
poetry install
```

## 2) Run JIT examples:

```
python mandelbrot-jit.py
```

Speed gain seems to be ~15.


(Won't work on a Mac, unless you apply this patch: <https://github.com/sfermigier/ppci/commit/805b>)

## 3) Compile examples to WASM and IR:

```
doit
```

Then you get (currently): 

- a `mandelbrot.wasm` file which should run under a WASM interpreter (ex: Wasmer), but actually doesn't :(
- a `mandelbrot.ir.txt` file (textual representation of the program compiled to IR) 
- a `mandelbrot.ir.py` file (python version of the program compiled to IR) 

### Running the compiled files:

`mandelbrot.wasm` can be run by mannually removing the line: 

```
(import "env" "f64_print" (func $print (type $0)))
```

then runing: 

```
wasmer run mandelbrot.wasm -i mandelbrot
```

(Assuming Wasmer is installed).

`mandelbrot.ir.py` can be run from Python:

```
context = {}
exec(open("mandelbrot.ir.py").read(), context)
context["mandelbrot"]()
```


```
