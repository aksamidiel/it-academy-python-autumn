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


# 1. Write a program that prints the numbers from 1 to 100
# but for multiples of three print “Fizz” instead of the
# number and for multiples of five print “Buzz”.
# For numbers which are multiples of both three and five,
# print “FizzBuzz”


def sm_print():
    first_position = int(input("Please enter first position: "))
    last_position = int(input("Please enter last position: "))

    @save_func
    def smart_printer(f_p, l_p):
        lst = []
        for i in range(f_p, l_p):

            if i % 15:
                lst.append('FizzBuzz')

            elif i % 3 == 0:
                lst.append('Fizz')
            elif i % 5 == 0:
                lst.append('Buzz')
            else:
                lst.append(i)

        index = 0
        for ls in lst:  # цикл вывода
            print(lst[index], end=", ")
            index += 1
        return "Result: {}".format(lst)

    print(smart_printer(first_position, last_position))


# 2. Use a list comprehension to construct the
# list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# 3. Use a slice on the above list to construct the
# list ['ab', 'ad', 'bc'].
# 4. Use a list comprehension to construct the list ['1a', '2a', '3a', '4a']
# 5. Simultaneously remove the element '2a'
# from the above list and print it.
# 6. Copy the above list and add '2a'
# back into the list such that the
# original is still missing it.


def test_list_comp():
    lst_1 = [a + b for a in ['a', 'b'] for b in ['b', 'c', 'd']]
    @save_func
    def const_comp_0():
        print("create list with list comprehension ")
        n = int(input("Enter number of range: "))

        lst_0 = [[a, b] for a in range(n) for b in range(n)]
        return "Result: {}".format(lst_0)

    const_comp_0()
    @save_func
    def const_comp_1():
        lst_1 = [a + b for a in ['a', 'b'] for b in ['b', 'c', 'd']]
        lst_2 = lst_1[::2]
        print("Result :{}".format(lst_2))
        return "Result: {}".format(lst_1)

    const_comp_1()
    @save_func
    def const_comp_2(lst_1):
        lst_2 = lst_1[::2]
        return "Result :{}".format(lst_2)

    const_comp_2(lst_1)
    @save_func
    def const_comp_3():
        lst_2 = [[str(i) + 'a'] for i in range(1, 5)]
        flat_list_2 = [item for sublist in lst_2 for item in sublist]
        print("Remove '2a': ", flat_list_2.pop(1))
        print("Welcome back")
        flat_list_3 = flat_list_2.copy()

        print(flat_list_3)
        flat_list_3.insert(1, '2a')
        print(flat_list_3)

        return "Result: {}".format(flat_list_2)

    const_comp_3()
