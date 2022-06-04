#3.
#Написать мини калькулятор.
#В консоле ожидается ввод того символа, операцию которую мы будем выполнять.
#Операции: +, -, /, *, возведение в степень, модуль, рандомное число, факториал и арккосинус.
#В консоль вводим столько значений, сколько требуется для операции. Для рандомного, например, 0.
#Выводим значение.

import math
import random

operator_str = input("Введите операцию: ")

if operator_str == "+":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(f"Результат: {num1 + num2}")
elif operator_str == "-":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(f"Результат: {num1 - num2}")
elif operator_str == "/":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    try:
        print(f"Результат: {num1 / num2}")
    except ZeroDivisionError:
        print("Деление на ноль")
elif operator_str == "*":
    num1 = float(input("Ввведите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(f"Результат: {num1 * num2}")
elif operator_str == "^":
    num1 = float(input("Ввведите число: "))
    num2 = float(input("Введите степень: "))
    print(f"Результат: {pow(num1,num2)}")
elif operator_str == "abs":
    num1 = float(input("Ввведите число: "))
    print(f"Результат: {abs(num1)}")
elif operator_str == "rand":
    print(f"Результат: {random.randint(0,1337)}")
elif operator_str == "fact":
    num1 = int(input("Ввведите число: "))
    print(f"Результат: {math.factorial(num1)}")
elif operator_str == "acos":
    num1 = float(input("Ввведите число: "))
    try:
        print(f"Результат: {math.acos(num1)}")
    except ValueError:
        print("Введенное число не удовлетворяет интервалу -1..1")