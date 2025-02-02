def divide_by_2(num):
    return num / 2

def reverse_string(string):
    return string[::-1]

def my_xor_func(A, B):
    return (A and (not B)) or ((not A) and B)

def test_func():
    # Check if the values are floating point 
    # or integer respectively.
    assert divide_by_2(1001) == 500.5
    assert divide_by_2(1000) == 500

    # Test if the string was reversed
    assert reverse_string("desserts") == "stressed"

    # Check if the xor function is correct 
    # for expected output
    assert my_xor_func(True, True) == False
    assert my_xor_func(False, False) == False
    assert my_xor_func(True, False) == True