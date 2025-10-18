#Задачка с собеседования
#Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
#Функция должна печатать числа от 1 до n. При этом: если число делится на 3, печатать Fizz;
#если число делится на 5, печатать Buzz; если число делится на 3 и на 5, печатать FizzBuzz.

n = int (input("Ведите число"))
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(f"{i} - Fizz")
        elif i % 5 == 0:
            print(f"{i} - Buzz")
        elif i % 5 == 0 and i % 3 == 0:
            print(f"{i} - FizzBuzz")
        else:
            print(i)

fizz_buzz(n)