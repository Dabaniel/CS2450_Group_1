import pytest
import UVSim

#TODO: TESTS MUST BE KEPT UP-TO-DATE WITH PROGRESS IN MEMORY

def test_get_memory():
    sim = UVSim.UVSim()
    assert type(sim.get_memory()) == type([])
    assert sim.get_memory() == [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

def test_get_acc():
    sim = UVSim.UVSim()
    assert type(sim.get_acc()) == type([])
    assert sim.get_acc() == [0, '0']

@pytest.mark.parametrize('input,expected,expected_list', [
    ('test1', True, ['+1007', '+1008', '+2007', '+2008', '+2109', '+1109', '+4300', '+0000', '+0000', '+0000', '-99999', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]),
    ('test2', True, ['+1009', '+1010', '+2009', '+3110', '+4107', '+1109', '+4300', '+1110', '+4300', '+0000', '+0000', '-99999', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]),
    ('test3', True, ['+1009', '+1010', '+2009', '+3110', '+4107', '+1109', '+4300', '+1110', '+4300', '+0000', '+0000', '-99999', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]),
    ('test1', False, ['+1007', '+1000', '+2007', '+2008', '+2109', '+1109', '+4300', '+0000', '+0000', '+0000', '-99999', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]),
    ('test2', False, []),
    ('test3', False, ['+1000', '+1010', '+2009', '+3110', '+4107', '+1109', '+4300', '+1110', '+4300', '+0000', '+0000', '-99999', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
])

def test_load_from_text(input, expected, expected_list):
    sim = UVSim.UVSim()
    sim.load_from_text(f'{input}.txt')
    assert (sim.get_memory() == expected_list) == expected

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
    sim = UVSim.UVSim()
    for i in range(num):
        sim.step()
    assert sim.get_acc() == [num, '0']

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
