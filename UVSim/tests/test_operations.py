import pytest
from ..src.simulation.operations import Operator

#TODO: MAKE THIS EXECUTABLE

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

def test_initialize():
    opA = operations.Operator()
    assert opA