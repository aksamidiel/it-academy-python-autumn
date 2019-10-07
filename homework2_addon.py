
# stepic.org tasks
#
# нужно написать программу, которая считывает строку и заменяет
# в ней группы пробельных символов на символ подчёркивания.

some_simple_string = input("Enter some string: ").replace(' ', '_')
while "__" in some_simple_string:
    some_simple_string = some_simple_string.replace('__', '_')
print(some_simple_string)

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
roma_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
dec_list = [roma_dict[index] for index in s]
print(dec_list)
for j in range(len(dec_list) - 1):
    if dec_list[j] < dec_list[j + 1]:
        dec_list[j] = dec_list[j] * (-1)
s = 0
for i in dec_list:
    s += i
print("Number in dec system: ", s)

# Напишите простой интерпретатор математического выражения.
#
# На вход подаётся строка с выражением,
# состоящим из двух чисел, объединённых бинарным оператором:
# a operator b, где вместо operator могут использоваться следующие слова:
# plus, minus, multiply, divide для,
# соответственно, сложения, вычитания,
# умножения и целочисленного деления.

some_expression = str(input("Enter some simple expression: [a operator b]"))
exp_list = some_expression.split(' ')
i = 0
for ch in exp_list:
    if i == 0:
        num_1 = int(ch)
    if i == 1:
        operator = str(ch)
    if i == 2:
        num_2 = int(ch)
    i = i + 1
if operator == 'plus':
    res = num_1 + num_2
elif operator == 'minus':
    res = num_1 - num_2
elif operator == 'multiply':
    res = num_1 * num_2
elif operator == 'divide':
    res = num_1 / num_2
else:
    res = "Bad operation"
print("Result: ", res)

# напишите программу, которая переводит имена
# переменных из стиля написания underscore в стиль UpperCamelCase.
# Стиль underscore характеризуется тем,
# что слова в имени пишутся маленькими буквами
# и разделяются между собой символом подчёркивания "_".
# Стиль UpperCamelCase означает,
# что каждое слово пишется с большой буквы и
# разделителей между словами нет.
#

text = input("Enter some text: ").split("_")
buf_text = ""
for i in text:
    v = i[0].upper() + i[1:]
    buf_text += v
print(buf_text)

# Программа должна выводить
# для каждого уникального слова
# число его повторений (без учёта регистра).

some_str = input("Enter some text: ").lower().split(" ")
list_buf = []
dict_buf = {}
for i in some_str:
    if i not in list_buf:
        list_buf.append(i)
        dict_buf[i] = 1
    else:
        dict_buf[i] += 1
for i in range(len(list_buf)):
    print(list_buf[i] + " " + str(dict_buf[list_buf[i]]))
