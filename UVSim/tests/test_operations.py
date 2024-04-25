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

@pytest.mark.parametrize('mem_loc,value', [
    ("00", "2"),
    ("11", "a"),
    ("65", "43"),
    ("54", "6"),
    ("11", "9"),
    ("99", "0"),
])

def test_read(mem_loc,value):
    global memory, accumulator, register
    buff = buffer.Buffer()
    memory = [""] * 100
    operations.input = lambda: value
    ops = operations.Operator(get_memory, set_position_in_memory, get_accumulator, set_accumulator, get_register, set_register, buff)
    ops.Read(mem_loc)
    assert get_memory()[int(mem_loc)] == value
    
    ops.Read("string not int")
    assert ops._get_register() == value


def test_case_switch():
    global memory, accumulator, register
    buff = buffer.Buffer()
    ops = operations.Operator(get_memory, set_position_in_memory, get_accumulator, set_accumulator, get_register, set_register, buff)
    
    assert ops.case_switch("+10", 0) == None
    assert ops.case_switch("+30", -1) == ValueError