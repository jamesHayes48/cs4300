def divide_by_2(num):
    return num / 2

def reverse_string(string):
    return string[::-1]

def my_xor_func(A, B):
    return (A and (not B)) or ((not A) and B)

def test_func():
    assert divide_by_2(1001) == 500.5
    assert divide_by_2(1000) == 500
    assert reverse_string("desserts") == "stressed"
    assert my_xor_func(True, True) == False
    assert my_xor_func(False, False) == False
    assert my_xor_func(True, False) == True