def get_range(lst):
    result = list()
    result.append(lst[0])
    for i in lst[1:]:
        if i - result[-1] == 1:

            if len(result) == 1:
                result.append(i)

            elif len(result) == 2:
                result[-1] = i

        else:
            print('-'.join(map(str, result)), end=', ')
            result.clear()
            result.append(i)

    print('-'.join(map(str, result)))


get_range([0, 1, 2, 3, 4, 7, 8, 10])


def get_range_1(lst_1):
    res = []
    res.append(lst_1[0])
    for j in lst_1[1:]:
        if j - res[-1] == 1:
            res.append(j)
        elif len(res) == 2:
            res[-1] = j
        else:
            print('-'.join(map(str, res)), end=', ')
            res.clear()
            res.append(j)
    print('-'.join(map(str, res)))

get_range_1([0, 1, 2, 3, 4, 7, 8, 10])





