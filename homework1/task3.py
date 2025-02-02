# Test numbers if they are negative, positive, or zero
def number_test(num):
    if num < 0:
        print("Negative")
    elif num > 0:
        print("Positive")
    else:
        print("Zero")

# Find first ten prime numbers
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
    return primes
                
# Sum all numbers up to 100
def sum_100():
    num = 1
    sum = 0
    while 1 < 101:
        sum += num
        num += 1
    return sum

def test_func(capsys):
    #
    assert number_test(-1000) == "Negative"
    assert number_test(0) == "Zero"
    assert number_test(1000) == "Positive"

    assert ten_prime_nums() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    assert sum_100() == 5050