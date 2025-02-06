# Divide by 2
def divide_by_int(num):
    return num / 2

# Divide by 2.54, but round the float to
# 2 decimal places
def divide_by_float(num):
    return round(num / 2.54, 2)


# Return a reversed string
def reverse_string(string):
    return string[::-1]

# Return true or false statement 
# based on xor function
def my_xor_func(A, B):
    return (A and (not B)) or ((not A) and B)

# Test the integer function
def test_int():
    # Check if the values are floating point
    # or integer numbers respectively.
    assert divide_by_int(1001) == 500.5
    assert divide_by_int(1000) == 500

# Test the float function
def test_float():
    assert divide_by_float(1001) == 394.09
    assert divide_by_float(1000) == 393.70

def test_string():
    # Test if the string was reversed
    assert reverse_string("desserts") == "stressed"

def test_bool():
    # Check if the xor function is correct 
    # for expected output
    assert my_xor_func(True, True) == False
    assert my_xor_func(False, False) == False
    assert my_xor_func(True, False) == True