# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


# def return_hexadecimal(num):
#     hexadecimal = hex(num)
#     return hexadecimal
#
#
# num = int(input('Введите число: '))
#
# print(f'Вот его шестнадцатеричное строковое представление: {return_hexadecimal(num)}')

# ----------------------------------------------------------------------------------------------------------------

"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions."""

# from fractions import Fraction

# def sum_and_product(frac1, frac2):
#     frac1 = Fraction(frac1)
#     frac2 = Fraction(frac2)
#     print(frac1, frac2)
#
#     sum_fracs = frac1 + frac2
#     product_fracs = frac1 * frac2
#
#     return sum_fracs, product_fracs
#
#
# frac1 = input("Введите первую дробь в виде a/b: ")
# frac2 = input("Введите вторую дробь в виде a/b: ")
#
# print(sum_and_product(frac1, frac2))
