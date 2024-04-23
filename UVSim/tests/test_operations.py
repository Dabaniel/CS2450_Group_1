import pytest

import sys
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import src.simulation.operations as operations
import src.controllers.buffer as buffer


memory = [""] * 100
accumulator = -1
register = "00"

def get_memory():
    return memory

def set_position_in_memory(pos, value):
    memory[pos] = value

def get_accumulator():
    global accumulator
    return accumulator

def set_accumulator(value):
    global accumulator
    accumulator = value

def get_register():
    global register
    return register

def set_register(value):
    global register
    register = value

@pytest.mark.parametrize('acc,reg', [
    (0, "00"),
    (0, "11"),
    (2, "65"),
    (3, "54"),
    (1, "11"),
    (4, "99"),
    (1, "00"),
])

def test_write(acc,reg):
    global memory, accumulator, register
    buff = buffer.Buffer()
    memory = [""] * 100
    accumulator = acc
    register = reg
    ops = operations.Operator(get_memory, set_position_in_memory, get_accumulator, set_accumulator, get_register, set_register, buff)
    set_position_in_memory(accumulator, register)
    ops.Write(get_accumulator())
    assert buff.get_buffer_message() == register

@pytest.mark.parametrize('acc,value', [
    (0, "00"),
    (0, "11"),
    (2, "65"),
    (3, "54"),
    (1, "11"),
    (4, "99"),
    (1, "00"),
])

def test_read(acc,value,monkeypatch):
    global memory, accumulator, register
    buff = buffer.Buffer()
    memory = [""] * 100
    ops = operations.Operator(get_memory, set_position_in_memory, get_accumulator, set_accumulator, get_register, set_register, buff)
    monkeypatch.setattr('builtins.input', lambda _: "2")
    ops.Read(get_accumulator())
    assert ops._get_register() == value
