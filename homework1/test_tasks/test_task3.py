import task3

# Test if number_test and tell if a number is negative or not
def test_number_test(capsys):
    assert number_test(-1000) == "Negative"
    assert number_test(0) == "Zero"
    assert number_test(1000) == "Positive"

# Test that the first ten prime numbers are correctly found
def test_prime_num(capsys):
    ten_prime_nums()
    captured_prime_num = capsys.readouterr()
    assert captured_prime_num.out == "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]\n"

# Test that the sum is the sum of integers 1 - 100
def test_sum_100():
    assert sum_100() == 5050