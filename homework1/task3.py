# Test numbers if they are negative, positive, or zero
def number_test(num):
    num_identity = ""
    if num < 0:
        num_identity = "Negative"
    elif num > 0:
        num_identity = "Positive"
    else:
        num_identity = "Zero"
    return num_identity

# Find first ten prime numbers and return them
def ten_prime_nums():
    primes = []
    num = 2

    while len(primes) != 10:
        prime = True
        # Iterate until num - 1
        # Check if it has factors other than
        # 1 and itself
        for n in range(2, num):
            if num % n == 0:
                prime = False
        if prime:
            primes.append(num)

        num += 1
    print(primes)
                
# Sum all numbers up to 100
def sum_100():
    num = 1
    sum = 0
    while num < 101:
        sum += num
        num += 1
    return sum


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