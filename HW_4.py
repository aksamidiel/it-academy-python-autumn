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


def simple_dict_const():
    some_string = input("Enter some string: ")

    def dict_const(some_str):
        dict_res = dict((ch, some_str.count(ch)) for ch in set(some_str))
        return "Result: {}".format(dict_res)

    print(dict_const(some_string))


def spl_search():
    some_text = input("Enter some text: ").split()

    def search_num_word(s_t):
        s_t = [line.rstrip() for line in s_t]
        dict_res = dict((word, some_text.count(word)) for word in set(s_t))
        print(dict_res)

        sort_res = sorted(dict_res.items(), key=lambda i: (-i[1], i[0]))[0]  # tuple
        return "Result sorted: {}".format(sort_res[0])

    search_num_word(some_text)


def tw_l():
    list_l1 = input("Enter list of numbers 1: ")
    list_l2 = input("Enter list of numbers 2: ")

    def two_list(l1, l2):
        et_list_l1 = set(l1)
        set_list_l2 = set(l2)
        l = len(et_list_l1 & set_list_l2)
        return "the number of numbers found in both: {}".format(l)

    print(two_list(list_l1, list_l2))


def tw_dif():
    list_l1 = input("Enter list of numbers 1: ")
    list_l2 = input("Enter list of numbers 2: ")

    def two_list_dif(l1, l2):
        et_list_l1 = set(l1)
        set_list_l2 = set(l2)
        l = len(et_list_l1 ^ set_list_l2)
        return "the number of numbers found in both: {}".format(l)

    print(two_list_dif(list_l1, list_l2))
