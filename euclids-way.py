import math

def begin(a: int, b: int):
    rems = []
    new_b = b // a
    remainder = b % a

    while remainder != 0:
        new_a = new_b
        new_b = remainder

        # rems.append(remainder)
        print(remainder)

        begin(new_a, new_b)

        if remainder == 0:
            break


a = int(input("Input first number: "))
b = int(input("Input second number: "))
q = 1

# Calculate the quotient
if b > 0:
    q = math.floor(a/b)
else:
    q = math.ceil(a/b)

# Next, find the initial remainder
r = a - (b * q)

remainders = []

begin(b, a)
# print(r)
