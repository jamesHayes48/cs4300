import task2 as t2

# Test if the integer variable is integer
def test_int():
    assert isinstance(t2.integer_var, int)

# Test if the float variable is an integer
def test_float():
    assert isinstance(t2.float_var, float)

# Test if the string variable is a string
def test_string():
    assert isinstance(t2.string_var, str)

# Test if the boolean variable is a boolean
def test_bool():
    assert isinstance(t2.boolean_var, bool)