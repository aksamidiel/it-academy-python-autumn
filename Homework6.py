import HW_1, HW_1_addon, HW_2, HW_3, HW_4

# task_1
rub = int(input('Enter cost in rub(please use whole number: '))
coins = int(input('Enter cost in coins(please use whole number <100 : '))
number_of_items = int(input("Input number of item: "))
print(HW_1.calc(number_of_items, rub, coins))

# task v.2
some_number = int(input("Enter some number: "))
temp = some_number
print(HW_1.is_pal(some_number))

# task_fibonacci
# fibonacci start to 1
# ряд фиббоначи начинается с 1
n = int(input("Enter number of Fibonacci: "))
print(HW_1.is_fib(n))

# нужно написать программу, которая считывает строку и заменяет
# в ней группы пробельных символов на символ подчёркивания.
some_simple_string = input("Enter some string: ").replace(' ', '_')
print(HW_1_addon.s_str(some_simple_string))

# В римской системе счисления для обозначения
# чисел используются следующие символы
# (справа записаны числа, которым они соответствуют
# в десятичной системе счисления):
#
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# Будем использовать вариант,
# в котором числа 4, 9, 40, 90, 400 и 900 записываются
# как вычитание из большего числа меньшего:
# IV, IX, XL, XC, CD и CM, соответственно.
#
# Напишите программу, которая переводит
# число из римской в десятичную систему счисления.

s = input("Please enter some Roma number: ")
print(HW_1_addon.roma_func(s))

# Напишите простой интерпретатор математического выражения.
#
# На вход подаётся строка с выражением,
# состоящим из двух чисел, объединённых бинарным оператором:
# a operator b, где вместо operator могут использоваться следующие слова:
# plus, minus, multiply, divide для,
# соответственно, сложения, вычитания,
# умножения и целочисленного деления.

some_expression = str(input("Enter some simple expression: [a operator b]"))
print(HW_1_addon.func_some_exp(some_expression))

# напишите программу, которая переводит имена
# переменных из стиля написания underscore в стиль UpperCamelCase.
# Стиль underscore характеризуется тем,
# что слова в имени пишутся маленькими буквами
# и разделяются между собой символом подчёркивания "_".
# Стиль UpperCamelCase означает,
# что каждое слово пишется с большой буквы и
# разделителей между словами нет.

text = input("Enter some text: ")
print(HW_1_addon.text_converter(text))

# Программа должна выводить
# для каждого уникального слова
# число его повторений (без учёта регистра).

some_str = input("Enter some text: ")
print(HW_1_addon.rep_word(some_str))

"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания"""
phrase = input("Please enter some phrase with signs separated by space: ")
print(HW_2.l_word(phrase))

""" task2: Вводится строка. Требуется удалить из нее
 повторяющиеся символы и все пробелы.
 Например, если было введено "abc cde def",
 то должно быть выведено "abcdef"."""

phrase = input("Please enter simple phrase: ")
print(HW_2.space_symb_deleter(phrase))

""" Посчитать количество строчных (маленьких) и прописных
(больших) букв в введенной строке. Учитывать только английские буквы. """

phrase = input("Please enter simple phrase: ")
print(HW_2.up_lo_letter(phrase))

# 1. Write a program that prints the numbers from 1 to 100
# but for multiples of three print “Fizz” instead of the
# number and for multiples of five print “Buzz”.
# For numbers which are multiples of both three and five,
# print “FizzBuzz”

print("Prints row numbers: ")
first_position = int(input("Please enter first position: "))
last_position = int(input("Please enter last position: "))
print(HW_3.smart_printer(first_position, last_position))

# 2. Use a list comprehension to construct the
# list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# 3. Use a slice on the above list to construct the
# list ['ab', 'ad', 'bc'].

print("create list with list comprehension ")
print(HW_3.constr_compt_1())

# 4. Use a list comprehension to construct the list ['1a', '2a', '3a', '4a']
# 5. Simultaneously remove the element '2a'
# from the above list and print it.
# 6. Copy the above list and add '2a'
# back into the list such that the
# original is still missing it.

print(HW_3.constr_comp_3())

# task_1
# Define a dict comprehension which returns a dictionary where
# the keys are numbers between 1 and n (both included)
# and the values are square of keys.
# n – function argument. Default is 20.
print(HW_4.calc_f1())

# task_1.2
# Define a code which count and return
# the numbers of each character in a count_me_string argument.

some_string = input("Enter some string: ")
print(some_string)

# Задача. Дан текст (строк может быть много, разделенных \n).
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в
# лексикографическом порядке.

some_text = input("Enter some text: ").split()
print(HW_4.search_num_word(some_text))

# Даны два списка чисел.
# Посчитайте, сколько чисел содержится одновременно
# как в первом списке, так и во втором.

list_l1 = input("Enter list of numbers 1: ")
list_l2 = input("Enter list of numbers 2: ")
print(HW_4.two_list(list_l1, list_l2))

# Даны два списка чисел. Посчитайте,
# сколько чисел входит только в один из этих списков.
print(HW_4.two_list_dif(list_l1, list_l2))








