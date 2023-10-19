# Lab_03_3.py
# Товтин ОЛександра
# Лабораторна робота №3.3   
# Розгалуження, задане графіком функції
# Варіант  21

import math
x = int(input("Type x: ")) #вхідний аргумент
R = int(input("Type R: ")) #вхідний параметр
def main(x, R):
    if x <= -2 * R:
        y = R
    elif x > -2 * R and x <= 0:
        y = x * -0.5
    elif x > 0 and x <= R:
        y = R - math.sqrt(R**2 - x**2)
    elif x > R and x <= R * 2:
        y = math.sqrt(R**2 - (x**2 - 2 * x * R + R**2))
    elif x > 2 * R:
        y = -((x - 2 * R) / (6 - 2 * R))
    return y
result = main(x, R)
print("y = ", result)