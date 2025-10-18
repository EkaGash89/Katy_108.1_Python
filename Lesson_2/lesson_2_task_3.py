import math

def square(stor):
    return math.ceil(stor * stor)

plogh_stor = float(input("Введите сторону кадрата: "))
print(f"Площадь квадрата: {square(plogh_stor)}")
    