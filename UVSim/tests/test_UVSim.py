import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import pytest
import src.simulation.UVSim as UVSim

#TODO: MAKE THIS EXECUTABLE

#TODO: TESTS MUST BE KEPT UP-TO-DATE WITH PROGRESS IN MEMORY

def test_get_memory():
    sim = UVSim.I_UVSim(UVSim.UVSim())
    assert type(sim.get_memory()) == list
    assert sim.get_memory() == [''] * 250

def test_get_accumulator():
    sim = UVSim.I_UVSim(UVSim.UVSim())
    assert type(sim.get_accumulator()) == int
    assert sim.get_accumulator() == -1

@pytest.mark.parametrize('expected_list', [
    (['+1007', '+1008', '+2007', '+2008', '+2109', '+1109', '+4300', '+0000', '+0000', '+0000', '-99999']),
    (['+1009', '+1010', '+2009', '+3110', '+4107', '+1109', '+4300', '+1110', '+4300', '+0000', '+0000', '-99999']),
    (['+1009', '+1010', '+2009', '+3110', '+4107', '+1109', '+4300', '+1110', '+4300', '+0000', '+0000', '-99999']),
    (['+1007', '+1000', '+2007', '+2008', '+2109', '+1109', '+4300', '+0000', '+0000', '+0000', '-99999']),
    ([]),
    (['+1000', '+1010', '+2009', '+3110', '+4107', '+1109', '+4300', '+1110', '+4300', '+0000', '+0000', '-99999'])
])

def test_load_from_text(expected_list):
    sim = UVSim.I_UVSim(UVSim.UVSim())
    sim.load_list(expected_list)
    seen = True
    for i in range(len(expected_list)):
        current = sim.get_memory()[i] == expected_list[i]
        seen = current and seen
        assert current

@pytest.mark.parametrize('num', [
    (0),
    (1),
    (2),
    (3),
    (4),
    (5),
    (6)
])

def test_accumulator_progression(num):
    sim = UVSim.I_UVSim(UVSim.UVSim())
    sim.set_accumulator(0)
    for i in range(num):
        sim.step()
    assert sim.get_accumulator() == num

# @pytest.mark.parametrize('example,num', [
#     ('examplearg1', 1),
#     ('examplearg2', 2),
#     ('examplearg3', 3),
#     ('examplearg4', 4),
#     ('examplearg5', 5),
#     ('examplearg6', 6),
#     ('examplearg7', 7)
# ])

# def test_example(example,num):
#     assert int(example[-1]) == num
