from operator import eq


def getRanges(lst):
    mass = [[lst[0]] * 2]
    for x in lst[1:]:
        if x == mass[-1][-1] + 1:
            mass[-1][-1] = x
        else:
            mass += [[x] * 2]
            print(mass)
    print(','.join((str(i[0])
                    if eq(*i) else '-'.join(map(str, i))
                    for i in mass)))


some_string_1 = [0, 1, 2, 3, 4, 7, 8, 10]
getRanges(some_string_1)
some_string_2 = [4, 7, 10]
getRanges(some_string_2)
some_string_3 = [2, 3, 8, 9]
getRanges(some_string_3)
