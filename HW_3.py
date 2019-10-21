def sm_print():
    first_position = int(input("Please enter first position: "))
    last_position = int(input("Please enter last position: "))

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
        print("create list with list comprehension ")
        n = int(input("Enter number of range: "))

        lst_1 = [[a, b] for a in range(n) for b in range(n)]
        return "Result: {}".format(lst_1)

    print(smart_printer(first_position, last_position))


def test_list_comp():
    lst_1 = [a + b for a in ['a', 'b'] for b in ['b', 'c', 'd']]

    def const_comp_1():
        lst_1 = [a + b for a in ['a', 'b'] for b in ['b', 'c', 'd']]
        lst_2 = lst_1[::2]
        print("Result :{}".format(lst_2))
        return "Result: {}".format(lst_1)

    const_comp_1()

    def const_comp_2(lst_1):
        lst_2 = lst_1[::2]
        return "Result :{}".format(lst_2)
    const_comp_2(lst_1)

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
