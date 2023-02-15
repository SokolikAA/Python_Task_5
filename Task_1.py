# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.

number = int(input('Введите число: '))
num_degree = int(input('Введите степень: '))


def erect(num, degree):
    if degree == 1:
        return num
    if degree != 1:
        return num * degree(num, degree - 1)


print(erect(number, num_degree))
