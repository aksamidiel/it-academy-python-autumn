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


# task_1
# Define a dict comprehension which returns a dictionary where
# the keys are numbers between 1 and n (both included)
# and the values are square of keys.
# n – function argument. Default is 20.

@save_func
def range_calc():
    while True:
        try:
            n = int(input("Enter some range in (int): "))
        except ValueError:
            print("Not an integer, set default n = 20")
            n = 20
            break
        else:
            print("Try input")
            break

    def dict_cons(n):
        dic_ = {x: x * x for x in range(1, n + 1)}
        return dic_

    res = dict_cons(n)
    return "Result: {}".format(res)


# task_1.2
# Define a code which count and return
# the numbers of each character in a count_me_string argument.


def simple_dict_const():
    some_string = input("Enter some string: ")

    @save_func
    def dict_const(some_str):
        dict_res = dict((ch, some_str.count(ch)) for ch in set(some_str))
        return "Result: {}".format(dict_res)

    print(dict_const(some_string))


# Задача. Дан текст (строк может быть много, разделенных \n).
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в
# лексикографическом порядке.


def spl_search():
    some_text = input("Enter some text: ").split()

    @save_func
    def search_num_word(s_t):
        s_t = [line.rstrip() for line in s_t]
        dict_res = dict((word, some_text.count(word)) for word in set(s_t))
        print(dict_res)

        sort_res = sorted(dict_res.items(), key=lambda i: (-i[1], i[0]))[0]  # tuple
        return "Result sorted: {}".format(sort_res[0])

    search_num_word(some_text)


# Даны два списка чисел.
# Посчитайте, сколько чисел содержится одновременно
# как в первом списке, так и во втором.


def tw_l():
    list_l1 = input("Enter list of numbers 1: ")
    list_l2 = input("Enter list of numbers 2: ")

    @save_func
    def two_list(l1, l2):
        et_list_l1 = set(l1)
        set_list_l2 = set(l2)
        l = len(et_list_l1 & set_list_l2)
        return "the number of numbers found in both: {}".format(l)

    print(two_list(list_l1, list_l2))


# Даны два списка чисел. Посчитайте,
# сколько чисел входит только в один из этих списков.


def tw_dif():
    list_l1 = input("Enter list of numbers 1: ")
    list_l2 = input("Enter list of numbers 2: ")

    @save_func
    def two_list_dif(l1, l2):
        et_list_l1 = set(l1)
        set_list_l2 = set(l2)
        l = len(et_list_l1 ^ set_list_l2)
        return "the number of numbers found in both: {}".format(l)

    print(two_list_dif(list_l1, list_l2))
