#6. Переделываем задачу номер 3(калькулятор) и номер 5 на функции.


import math
import random

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2

def mul(num1, num2):
    return num1 * num2

def pow(num1, num2):
    return math.pow(num1, num2)

def module(num1):
    return abs(num1)

def random_num():
    return random.randint(0,1337)

def factorial(num1):
    return math.factorial(num1)

def acos(num1):
    return math.acos(num1)


operator_str = input("Введите операцию: ")

if operator_str == "+":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(f"Результат: {plus(num1, num2)}")
elif operator_str == "-":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(f"Результат: {minus(num1, num2)}")
elif operator_str == "/":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    try:
        print(f"Результат: {div(num1, num2)}")
    except ZeroDivisionError:
        print("Деление на ноль")
elif operator_str == "*":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(f"Результат: {mul(num1, num2)}")
elif operator_str == "^":
    num1 = float(input("Ввведите число: "))
    num2 = float(input("Введите степень: "))
    print(f"Результат: {pow(num1,num2)}")
elif operator_str == "abs":
    num1 = float(input("Ввведите число: "))
    print(f"Результат: {module(num1)}")
elif operator_str == "rand":
    print(f"Результат: {random_num()}")
elif operator_str == "fact":
    num1 = int(input("Ввведите число: "))
    print(f"Результат: {factorial(num1)}")
elif operator_str == "acos":
    num1 = float(input("Ввведите число: "))
    try:
        print(f"Результат: {acos(num1)}")
    except ValueError:
        print("Введенное число не удовлетворяет интервалу -1..1")