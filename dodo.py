#!/usr/bin/env python

from devtools import debug
from ppci.lang.python import python_to_ir, python_to_wasm, ir_to_python
from ppci.utils.reporting import TextReportGenerator

SRC_IR = "mandelbrot-ir.py"
SRC_WASM = "mandelbrot-wasm.py"


def task_compile_to_ir():
    def run(targets):
        print("Compiling...")
        source_fd = open(SRC_IR)
        ir_module = python_to_ir(source_fd)

        with open("mandelbrot.ir.txt", "w") as output:
            reporter = TextReportGenerator(output)
            reporter.dump_ir(ir_module)

        with open("mandelbrot.ir.py", "w") as output:
            ir_to_python([ir_module], output)

    return {
        "file_dep": [SRC_IR],
        "targets": ["mandelbrot.ir.txt", "mandelbrot.ir.py"],
        "actions": [run],
        "clean": True,
    }


def task_compile_to_wasm():
    WASM_FILE = "mandelbrot.wasm"

    def run(targets):
        source = open(SRC_WASM).read()
        wasm_module = python_to_wasm(source)
        debug(wasm_module)
        debug(wasm_module.to_string())

        open(WASM_FILE, "w").write(wasm_module.to_string())

    return {
        "file_dep": [SRC_WASM],
        "targets": [WASM_FILE],
        "actions": [run],
        "clean": True,
    }
