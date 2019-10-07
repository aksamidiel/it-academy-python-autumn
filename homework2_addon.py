# stepik tasks
# В римской системе счисления для обозначения чисел используются следующие символы
# (справа записаны числа, которым они соответствуют в десятичной системе счисления):
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
# как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.
#
# Напишите программу, которая переводит число из римской в десятичную систему счисления.

s = input("Please enter some Roma number: ")
roma_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
dec_list = [roma_dict[index] for index in s]
print(dec_list)
for j in range(len(dec_list) - 1):
    if dec_list[j] < dec_list[j + 1]:
        dec_list[j] = dec_list[j] * (-1)

sum = 0
for i in dec_list:
    sum += i
print("Number in dec system: ", sum)

# Напишите простой интерпретатор математического выражения.
#
# На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором:
# a operator b, где вместо operator могут использоваться следующие слова:
# plus, minus, multiply, divide для, соответственно, сложения, вычитания, умножения и целочисленного деления.

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


