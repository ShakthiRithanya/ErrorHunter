# Sum of Digits: Write a program to calculate the sum of digits of a number using a while loop.
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num + 10  # Bug: Adding 10 instead of dividing by 10
    return total