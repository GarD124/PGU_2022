# 7. Сделать из функций калькулятора отдельный класс.

import math
import random


class Calculator:
    @staticmethod
    def plus(num1, num2):
        return num1 + num2

    @staticmethod
    def minus(num1, num2):
        return num1 - num2

    @staticmethod
    def div(num1, num2):
        return num1 / num2

    @staticmethod
    def mul(num1, num2):
        return num1 * num2

    @staticmethod
    def pow(num1, num2):
        return math.pow(num1, num2)

    @staticmethod
    def module(num1):
        return abs(num1)

    @staticmethod
    def random_num():
        return random.randint(0, 1337)

    @staticmethod
    def factorial(num1):
        return math.factorial(num1)

    @staticmethod
    def acos(num1):
        return math.acos(num1)


operator_str = input("Введите операцию: ")

inst_calc = Calculator()
if operator_str == "+":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(f"Результат: {inst_calc.plus(num1, num2)}")
elif operator_str == "-":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(f"Результат: {inst_calc.minus(num1, num2)}")
elif operator_str == "/":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    try:
        print(f"Результат: {inst_calc.div(num1, num2)}")
    except ZeroDivisionError:
        print("Деление на ноль")
elif operator_str == "*":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(f"Результат: {inst_calc.mul(num1, num2)}")
elif operator_str == "^":
    num1 = float(input("Ввведите число: "))
    num2 = float(input("Введите степень: "))
    print(f"Результат: {inst_calc.pow(num1, num2)}")
elif operator_str == "abs":
    num1 = float(input("Ввведите число: "))
    print(f"Результат: {inst_calc.module(num1)}")
elif operator_str == "rand":
    print(f"Результат: {inst_calc.random_num()}")
elif operator_str == "fact":
    num1 = int(input("Ввведите число: "))
    print(f"Результат: {inst_calc.factorial(num1)}")
elif operator_str == "acos":
    num1 = float(input("Ввведите число: "))
    try:
        print(f"Результат: {inst_calc.acos(num1)}")
    except ValueError:
        print("Введенное число не удовлетворяет интервалу -1..1")
