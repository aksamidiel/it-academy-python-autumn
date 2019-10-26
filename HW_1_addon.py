from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "ru")


def save_func(dec_fun):
    def wrapper(*args, **kwargs):
        return_inf = dec_fun(*args, **kwargs)
        with open("save_fun.txt", "a") as f_obj:
            f_obj.write(str(datetime.now()) + "\n" + return_inf + "\n")
        print(return_inf)

    return wrapper


# stepic.org tasks
#
# нужно написать программу, которая считывает строку и заменяет
# в ней группы пробельных символов на символ подчёркивания.

def simple_input():
    some_simple_string = input("Enter some string: ").replace(' ', '_')

    @save_func
    def s_str(some_str):
        while "__" in some_str:
            some_str = some_str.replace('__', '_')
        return "This string is: {}".format(some_str)

    print(s_str(some_simple_string))


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


def roma_num_input():
    s = input("Please enter some Roma number: ")

    @save_func
    def roma_func(some_string):
        roma_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
        dec_list = [roma_dict[index] for index in some_string]
        print(dec_list)
        for j in range(len(dec_list) - 1):
            if dec_list[j] < dec_list[j + 1]:
                dec_list[j] = dec_list[j] * (-1)

        some_string = 0
        for j in dec_list:
            some_string += j
        return "Number in dec system: {}".format(some_string)

    print(roma_func(s))


# Напишите простой интерпретатор математического выражения.
#
# На вход подаётся строка с выражением,
# состоящим из двух чисел, объединённых бинарным оператором:
# a operator b, где вместо operator могут использоваться следующие слова:
# plus, minus, multiply, divide для,
# соответственно, сложения, вычитания,
# умножения и целочисленного деления.

def simple_math_sight():
    some_expression = str(input("Enter some simple expression: [a operator b]: "))

    @save_func
    def func_some_exp(some_ex):
        exp_list = some_ex.split(' ')
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
        return "Result: {}".format(res)

    print(func_some_exp(some_expression))


# напишите программу, которая переводит имена
# переменных из стиля написания underscore в стиль UpperCamelCase.
# Стиль underscore характеризуется тем,
# что слова в имени пишутся маленькими буквами
# и разделяются между собой символом подчёркивания "_".
# Стиль UpperCamelCase означает,
# что каждое слово пишется с большой буквы и
# разделителей между словами нет.
#

def simple_converter():
    text = input("Enter some text: ")

    @save_func
    def text_converter(txt):
        txt.split("_")
        buf_text = ""
        for i in text:
            v = i[0].upper() + i[1:]
            buf_text += v
        return buf_text

    print(text_converter(text))


# Программа должна выводить
# для каждого символа
# число его повторений (без учёта регистра).
def simple_rep():
    some_str = input("Enter some text: ")

    @save_func
    def rep_word(s_st):
        text_list = []
        s_st.lower().split(" ")
        list_buf = []
        dict_buf = {}
        for i in s_st:
            if i not in list_buf:
                list_buf.append(i)
                dict_buf[i] = 1
            else:
                dict_buf[i] += 1
        for i in range(len(list_buf)):
            text_list.append(list_buf[i] + ":" + str(dict_buf[list_buf[i]]))
        print(text_list)

    print(rep_word(some_str))
