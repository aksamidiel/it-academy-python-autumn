# Реализовать функцию get_ranges,
# которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
# get_ranges([4,7,10]) // "4,7,10"
# get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def getRanges(lst):
    diap = ''
    for elm in range(len(lst) - 1):
        if lst[elm] + 1 == lst[elm + 1] and lst[elm] - 1 != lst[elm - 1]:
            diap += '{}-'.format(lst[elm])
        elif lst[elm] + 1 != lst[elm + 1]:
            diap += '{},'.format(lst[elm])
    diap += str(lst[-1])
    print(diap)


some_string_1 = [0, 1, 2, 3, 4, 7, 8, 10]
getRanges(some_string_1)
some_string_2 = [4, 7, 10]
getRanges(some_string_2)
some_string_3 = [2, 3, 8, 9]
getRanges(some_string_3)
