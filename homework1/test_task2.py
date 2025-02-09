import task2 as t2

# Test the integer function
def test_int():
    # Check if the values are floating point
    # or integer numbers respectively.
    assert t2.divide_by_int(1001) == 500.5
    assert t2.divide_by_int(1000) == 500

# Test the float function
def test_float():
    assert t2.divide_by_float(1001) == 394.09
    assert t2.divide_by_float(1000) == 393.70

def test_string():
    # Test if the string was reversed
    assert t2.reverse_string("desserts") == "stressed"

def test_bool():
    # Check if the xor function is correct 
    # for expected output
    assert t2.my_xor_func(True, True) == False
    assert t2.my_xor_func(False, False) == False
    assert t2.my_xor_func(True, False) == True