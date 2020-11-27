import pytest

def test_method1(supply_AA_BB_CC):
    print('Sagar pytest prints by --capture command')
    pass


@pytest.mark.parametrize("input1, input2, output",[(5,5,10),(3,5,8)])
def test_add(input1, input2, output):
	assert input1+input2 == output,"failed"


@pytest.mark.parametrize("input1, input2",[(5,5),(3,5)])
def test_multiply(input1, input2):
	assert input1*input2 == 25,"failed"