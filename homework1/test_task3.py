import task3 as t3

# Test if number_test and tell if a number is negative or not
def test_number_test(capsys):
    assert t3.number_test(-1000) == "Negative"
    assert t3.number_test(0) == "Zero"
    assert t3.number_test(1000) == "Positive"

# Test that the first ten prime numbers are correctly found
def test_prime_num(capsys):
    t3.ten_prime_nums()
    captured_prime_num = capsys.readouterr()
    assert captured_prime_num.out == "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]\n"

# Test that the sum is the sum of integers 1 - 100
def test_sum_100():
    assert t3.sum_100() == 5050