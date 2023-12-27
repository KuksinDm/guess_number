from math import sqrt


def add_numbers(x_1: int, y_1: int) -> int:
    return x_1 + y_1


def calculate_square_root(number: int) -> float:
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        return
    else:
        bibi = calculate_square_root(your_number)
    return f"""Мы вычислили квадратный \
корень из введённого вами числа. Это будет: {bibi}"""


x_1 = 10
y_1 = 5

print('Сумма чисел: ', add_numbers(x_1, y_1))

print(calc(25.5))
