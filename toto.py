# Automatically generated on Thu Sep 30 16:03:32 2021
# Generator /Users/fermigier/envs/ppci-sandbox-X6ycXMEE-py3.9/lib/python3.9/site-packages/ppci/lang/python/ir2py.py

import struct
import math

_irpy_heap = bytearray()
_irpy_stack = bytearray()
HEAP_START = 0x10000000
_irpy_func_pointers = list()
_irpy_externals = {}

def _irpy_correct(value, bits, signed):
    base = 1 << bits
    value %= base
    if signed and value.bit_length() == bits:
        return value - base
    else:
        return value

def _irpy_idiv(x, y):
    sign = False
    if x < 0: x = -x; sign = not sign
    if y < 0: y = -y; sign = not sign
    v = x // y
    return -v if sign else v

def _irpy_irem(x, y):
    if x < 0:
        x = -x
        sign = True
    else:
        sign = False
    if y < 0: y = -y
    v = x % y
    return -v if sign else v

def _irpy_ishl(x, amount, bits):
    amount = amount % bits
    return x << amount

def _irpy_ishr(x, amount, bits):
    amount = amount % bits
    return x >> amount

def _irpy_alloca(amount):
    ptr = len(_irpy_stack)
    _irpy_stack.extend(bytes(amount))
    return (ptr, amount)

def _irpy_free(amount):
    for _ in range(amount):
        _irpy_stack.pop()

def read_mem(address, size):
    mem, address = _irpy_get_memory(address)
    assert address+size <= len(mem), str(hex(address))
    return mem[address:address+size]

def write_mem(address, data):
    mem, address = _irpy_get_memory(address)
    size = len(data)
    assert address+size <= len(mem), str(hex(address))
    mem[address:address+size] = data

def _irpy_get_memory(v):
    if v >= HEAP_START:
        return _irpy_heap, v - HEAP_START
    else:
        return _irpy_stack, v

def _irpy_heap_top():
    return len(_irpy_heap) + HEAP_START

def load_f64(p):
    return struct.unpack("d", read_mem(p, 8))[0]

def store_f64(v, p):
    write_mem(p, struct.pack("d", v))

def load_f32(p):
    return struct.unpack("f", read_mem(p, 4))[0]

def store_f32(v, p):
    write_mem(p, struct.pack("f", v))

def load_i64(p):
    return struct.unpack("q", read_mem(p, 8))[0]

def store_i64(v, p):
    write_mem(p, struct.pack("q", v))

def load_u64(p):
    return struct.unpack("Q", read_mem(p, 8))[0]

def store_u64(v, p):
    write_mem(p, struct.pack("Q", v))

def load_i32(p):
    return struct.unpack("i", read_mem(p, 4))[0]

def store_i32(v, p):
    write_mem(p, struct.pack("i", v))

def load_u32(p):
    return struct.unpack("I", read_mem(p, 4))[0]

def store_u32(v, p):
    write_mem(p, struct.pack("I", v))

def load_ptr(p):
    return struct.unpack("i", read_mem(p, 4))[0]

def store_ptr(v, p):
    write_mem(p, struct.pack("i", v))

def load_i16(p):
    return struct.unpack("h", read_mem(p, 2))[0]

def store_i16(v, p):
    write_mem(p, struct.pack("h", v))

def load_u16(p):
    return struct.unpack("H", read_mem(p, 2))[0]

def store_u16(v, p):
    write_mem(p, struct.pack("H", v))

def load_i8(p):
    return struct.unpack("b", read_mem(p, 1))[0]

def store_i8(v, p):
    write_mem(p, struct.pack("b", v))

def load_u8(p):
    return struct.unpack("B", read_mem(p, 1))[0]

def store_u8(v, p):
    write_mem(p, struct.pack("B", v))


# Module foo
def mandelbrot():
    _irpy_prev_block = None
    _irpy_current_block = 'mandelbrot_block0'
    while True:
        if _irpy_current_block == "mandelbrot_block0":
            num = 0
            alloc_count = _irpy_alloca(8)
            addr_count = alloc_count[0]
            store_i64(num, addr_count)
            num_0 = 150.0
            alloc_h = _irpy_alloca(8)
            addr_h = alloc_h[0]
            store_f64(num_0, addr_h)
            num_1 = 0.0
            alloc_Z = _irpy_alloca(8)
            addr_Z = alloc_Z[0]
            store_f64(num_1, addr_Z)
            num_2 = 0.0
            alloc_z = _irpy_alloca(8)
            addr_z = alloc_z[0]
            store_f64(num_2, addr_z)
            num_3 = 0.0
            alloc_T = _irpy_alloca(8)
            addr_T = alloc_T[0]
            store_f64(num_3, addr_T)
            num_4 = 0.0
            alloc_t = _irpy_alloca(8)
            addr_t = alloc_t[0]
            store_f64(num_4, addr_t)
            num_5 = 0.0
            alloc_C = _irpy_alloca(8)
            addr_C = alloc_C[0]
            store_f64(num_5, addr_C)
            num_6 = 0.0
            alloc_c = _irpy_alloca(8)
            addr_c = alloc_c[0]
            store_f64(num_6, addr_c)
            num_7 = 0.0
            alloc_U = _irpy_alloca(8)
            addr_U = alloc_U[0]
            store_f64(num_7, addr_U)
            num_8 = 0.0
            alloc_V = _irpy_alloca(8)
            addr_V = alloc_V[0]
            store_f64(num_8, addr_V)
            num_9 = 1.5
            alloc_K = _irpy_alloca(8)
            addr_K = alloc_K[0]
            store_f64(num_9, addr_K)
            num_10 = 1.0
            alloc_k = _irpy_alloca(8)
            addr_k = alloc_k[0]
            store_f64(num_10, addr_k)
            num_11 = 0.0
            alloc_y = _irpy_alloca(8)
            addr_y = alloc_y[0]
            store_f64(num_11, addr_y)
            _irpy_prev_block = _irpy_current_block
            _irpy_current_block = "mandelbrot_block1"
        if _irpy_current_block == "mandelbrot_block1":
            tmp_load = load_f64(addr_y)
            num_12 = 150.0
            if tmp_load < num_12:
                _irpy_prev_block = _irpy_current_block
                _irpy_current_block = "mandelbrot_block2"
            else:
                _irpy_prev_block = _irpy_current_block
                _irpy_current_block = "mandelbrot_block3"
        if _irpy_current_block == "mandelbrot_block2":
            tmp_load_13 = load_f64(addr_y)
            num_14 = 1.0
            augassign = tmp_load_13 + num_14
            store_f64(augassign, addr_y)
            num_15 = 0.0
            alloc_x = _irpy_alloca(8)
            addr_x = alloc_x[0]
            store_f64(num_15, addr_x)
            _irpy_prev_block = _irpy_current_block
            _irpy_current_block = "mandelbrot_block4"
        if _irpy_current_block == "mandelbrot_block3":
            tmp_load_80 = load_i64(addr_count)
            _irpy_free(112)
            return tmp_load_80
        if _irpy_current_block == "mandelbrot_block4":
            tmp_load_16 = load_f64(addr_x)
            num_17 = 150.0
            if tmp_load_16 < num_17:
                _irpy_prev_block = _irpy_current_block
                _irpy_current_block = "mandelbrot_block5"
            else:
                _irpy_prev_block = _irpy_current_block
                _irpy_current_block = "mandelbrot_block6"
        if _irpy_current_block == "mandelbrot_block5":
            tmp_load_18 = load_f64(addr_x)
            num_19 = 1.0
            augassign_20 = tmp_load_18 + num_19
            store_f64(augassign_20, addr_x)
            num_21 = 0.0
            num_22 = 0.0
            num_23 = 0.0
            num_24 = 0.0
            store_f64(num_21, addr_Z)
            store_f64(num_22, addr_z)
            store_f64(num_23, addr_T)
            store_f64(num_24, addr_t)
            tmp_load_25 = load_f64(addr_x)
            num_26 = 2.0
            tmp = tmp_load_25 * num_26
            store_f64(tmp, addr_U)
            tmp_load_27 = load_f64(addr_U)
            tmp_load_28 = load_f64(addr_h)
            augassign_29 = tmp_load_27 / tmp_load_28
            store_f64(augassign_29, addr_U)
            tmp_load_30 = load_f64(addr_y)
            num_31 = 2.0
            tmp_32 = tmp_load_30 * num_31
            store_f64(tmp_32, addr_V)
            tmp_load_33 = load_f64(addr_V)
            tmp_load_34 = load_f64(addr_h)
            augassign_35 = tmp_load_33 / tmp_load_34
            store_f64(augassign_35, addr_V)
            tmp_load_36 = load_f64(addr_U)
            tmp_load_37 = load_f64(addr_K)
            tmp_38 = tmp_load_36 - tmp_load_37
            store_f64(tmp_38, addr_C)
            tmp_load_39 = load_f64(addr_V)
            tmp_load_40 = load_f64(addr_k)
            tmp_41 = tmp_load_39 - tmp_load_40
            store_f64(tmp_41, addr_c)
            num_42 = 0.0
            alloc_i = _irpy_alloca(8)
            addr_i = alloc_i[0]
            store_f64(num_42, addr_i)
            _irpy_prev_block = _irpy_current_block
            _irpy_current_block = "mandelbrot_block7"
        if _irpy_current_block == "mandelbrot_block6":
            _irpy_prev_block = _irpy_current_block
            _irpy_current_block = "mandelbrot_block1"
        if _irpy_current_block == "mandelbrot_block7":
            tmp_load_43 = load_f64(addr_i)
            num_44 = 50.0
            if tmp_load_43 < num_44:
                _irpy_prev_block = _irpy_current_block
                _irpy_current_block = "mandelbrot_block8"
            else:
                _irpy_prev_block = _irpy_current_block
                _irpy_current_block = "mandelbrot_block9"
        if _irpy_current_block == "mandelbrot_block8":
            tmp_load_45 = load_f64(addr_i)
            num_46 = 1.0
            augassign_47 = tmp_load_45 + num_46
            store_f64(augassign_47, addr_i)
            tmp_load_48 = load_f64(addr_T)
            tmp_load_49 = load_f64(addr_t)
            tmp_50 = tmp_load_48 + tmp_load_49
            num_51 = 4.0
            if tmp_50 <= num_51:
                _irpy_prev_block = _irpy_current_block
                _irpy_current_block = "mandelbrot_block10"
            else:
                _irpy_prev_block = _irpy_current_block
                _irpy_current_block = "mandelbrot_block11"
        if _irpy_current_block == "mandelbrot_block9":
            tmp_load_73 = load_f64(addr_T)
            tmp_load_74 = load_f64(addr_t)
            tmp_75 = tmp_load_73 + tmp_load_74
            num_76 = 4.0
            if tmp_75 <= num_76:
                _irpy_prev_block = _irpy_current_block
                _irpy_current_block = "mandelbrot_block13"
            else:
                _irpy_prev_block = _irpy_current_block
                _irpy_current_block = "mandelbrot_block14"
        if _irpy_current_block == "mandelbrot_block10":
            tmp_load_52 = load_f64(addr_Z)
            tmp_load_53 = load_f64(addr_z)
            tmp_54 = tmp_load_52 * tmp_load_53
            store_f64(tmp_54, addr_z)
            tmp_load_55 = load_f64(addr_z)
            num_56 = 2.0
            augassign_57 = tmp_load_55 * num_56
            store_f64(augassign_57, addr_z)
            tmp_load_58 = load_f64(addr_z)
            tmp_load_59 = load_f64(addr_c)
            augassign_60 = tmp_load_58 + tmp_load_59
            store_f64(augassign_60, addr_z)
            tmp_load_61 = load_f64(addr_T)
            tmp_load_62 = load_f64(addr_t)
            tmp_63 = tmp_load_61 - tmp_load_62
            store_f64(tmp_63, addr_Z)
            tmp_load_64 = load_f64(addr_Z)
            tmp_load_65 = load_f64(addr_C)
            augassign_66 = tmp_load_64 + tmp_load_65
            store_f64(augassign_66, addr_Z)
            tmp_load_67 = load_f64(addr_Z)
            tmp_load_68 = load_f64(addr_Z)
            tmp_69 = tmp_load_67 * tmp_load_68
            store_f64(tmp_69, addr_T)
            tmp_load_70 = load_f64(addr_z)
            tmp_load_71 = load_f64(addr_z)
            tmp_72 = tmp_load_70 * tmp_load_71
            store_f64(tmp_72, addr_t)
            _irpy_prev_block = _irpy_current_block
            _irpy_current_block = "mandelbrot_block12"
        if _irpy_current_block == "mandelbrot_block11":
            _irpy_prev_block = _irpy_current_block
            _irpy_current_block = "mandelbrot_block12"
        if _irpy_current_block == "mandelbrot_block12":
            _irpy_prev_block = _irpy_current_block
            _irpy_current_block = "mandelbrot_block7"
        if _irpy_current_block == "mandelbrot_block13":
            tmp_load_77 = load_i64(addr_count)
            num_78 = 1
            augassign_79 = tmp_load_77 + num_78
            augassign_79 = _irpy_correct(augassign_79, 64, True)
            store_i64(augassign_79, addr_count)
            _irpy_prev_block = _irpy_current_block
            _irpy_current_block = "mandelbrot_block15"
        if _irpy_current_block == "mandelbrot_block14":
            _irpy_prev_block = _irpy_current_block
            _irpy_current_block = "mandelbrot_block15"
        if _irpy_current_block == "mandelbrot_block15":
            _irpy_prev_block = _irpy_current_block
            _irpy_current_block = "mandelbrot_block4"
    
_irpy_func_pointers.append(mandelbrot)


