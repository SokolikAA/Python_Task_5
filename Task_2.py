# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))


def summa(a, b):
    if b == 0:
        return a
    elif b > 0:
        return summa(a + 1, b - 1)
    else:
        return summa(a - 1, b + 1)


print(summa(first_number, second_number))
