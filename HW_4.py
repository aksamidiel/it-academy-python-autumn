

def calc_f1():
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
    return "Result: {res}".format(res)



def dict_constr(some_str):
    dict_res = dict((ch, some_str.count(ch)) for ch in set(some_str))
    return "Result: {dict_res}".format(dict_res)

def search_num_word(some_text):
    some_text = [line.rstrip() for line in some_text]
    dict_res = dict((word, some_text.count(word)) for word in set(some_text))
    print(dict_res)

    sort_res = sorted(dict_res.items(), key=lambda i: (-i[1], i[0]))[0]  # tuple
    return "Result sorted: {sort_res}".format(sort_res[0])

def two_list(l1, l2):
    et_list_l1 = set(l1)
    set_list_l2 = set(l2)
    l = len(et_list_l1 & set_list_l2)
    return "the number of numbers found in both: {l}".format(l)

def two_list_dif(l1, l2):
    et_list_l1 = set(l1)
    set_list_l2 = set(l2)
    l = len(et_list_l1 ^ set_list_l2)
    return "the number of numbers found in both: {l}".format(l)
