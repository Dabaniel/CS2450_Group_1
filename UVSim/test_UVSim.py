import pytest
import UVSim

def test_get_memory():
    sim = UVSim.UVSim()
    assert type(sim.get_memory()) == type([])
    assert sim.get_memory() == [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

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