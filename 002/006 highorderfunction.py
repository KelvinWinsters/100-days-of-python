import math


def simple_tax_calc(amount):
    return math.ceil(amount * 0.3)


def calculate_tax(salary, func):
    return func(salary)


print(calculate_tax(45000, simple_tax_calc))
