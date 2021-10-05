"""
3 points.

A strong number is a number whose sum of the factorial of digits is equal to the original number.

E.g. (1*1) + (4*3*2*1) + (5*4*3*2*1) = 145

Write a program that allows the user to enter an integer. The program outputs whether the number is strong or
not and ensures that an arithmetic overflow cannot crash the program.
"""


def is_number(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def input_number():
    while True:
        user_input = input("Enter a number: ")
        if is_number(user_input):
            num = int(user_input)

            if num < 0:
                print("Please enter a positive number.")
                continue

            return num
        else:
            print("Invalid integer. Please try again.")


def is_strong(num):
    sum = 0
    for digit in str(num):
        sum += factorial(int(digit))
    return sum == num


_memoised_factorials = {}


def factorial(num):
    if num in _memoised_factorials:
        return _memoised_factorials[num]

    fact = inner_factorial(num)
    _memoised_factorials[num] = fact

    return fact


def inner_factorial(num):

    if num == 0:
        return 1
    else:
        try:
            return num * factorial(num - 1)
        except OverflowError:
            print("Overflow error. Please try a smaller number.")
            exit()


num = input_number()

if is_strong(num):
    print("The number is strong.")
else:
    print("The number is not strong.")
