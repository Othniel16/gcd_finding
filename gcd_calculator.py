# implement base cases
# base case 1: if a and b are same, gcd is 1


# base case 2: if one of a and b is prime, gcd is 1

# General Algorithm
'''
1. Take the two numbers
2. Check if any of them are PRIME
3. If any of them are prime, gcd is 1
4. If none of them are prime, LIST THE FACTORS of both numbers in two arrays
5. Compare the arrays and find the longest array (check the length of both arrays)
6. Compare each value in the shortest array with the values in the longer array and store the similar values in a third array
7. Find the largest number of the third array and that is your gcd
'''

# Find factors of a number
def find_factors(n: int) -> list:
    a = range(2, n)

    factors = [i for i in a if n % i == 0]
    factors.extend([1, n])

    return factors

# Find prime number
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Find GCD
def findGCD():
    a = find_factors(number1)
    b = find_factors(number2)

    if len(a) < len(b):
        for i in a:
            if b.__contains__(i):
                common_factors.append(i)
    else:
        for i in b:
            if a.__contains__(i):
                common_factors.append(i)

    print('GCD : ' + str(max(common_factors)))


number1 = int(input("Input first number: "))
number2 = int(input("Input second number: "))
common_factors = []

isPrime = is_prime(number1) or is_prime(number2)

if number1 == 2 or number2 == 2:
    findGCD()
elif isPrime:
    print('GCD : ' + str(1))
else:
    findGCD()
