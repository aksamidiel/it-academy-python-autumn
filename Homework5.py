# task_1
# Define a dict comprehension which returns a dictionary where
# the keys are numbers between 1 and n (both included)
# and the values are square of keys.
# n – function argument. Default is 20.
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
print("Result: ", res)

# task_1.2
# Define a code which count and return
# the numbers of each character in a count_me_string argument.

some_string = input("Enter some string: ")
print(some_string)
dict_res = {dict_res: some_string.count(dict_res)
            for dict_res in set(some_string)}
print("Result", dict_res)

# Задача. Дан текст (строк может быть много, разделенных \n).
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в
# лексикографическом порядке.

some_text = input("Enter some text: ").split()

dict_res = {}
for word in some_text:
    dict_res[word] = dict_res.get(word, 0) + 1
print(dict_res)

max_lst = []
m_word_in_text = max(dict_res.values())
for key in dict_res.keys():
    if dict_res[key] == m_word_in_text:
        max_lst.append(key)
max_lst = sorted(max_lst)
print("Result sorted: ", max_lst[0])

# Задача Дан список стран и городов каждой страны.
# Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

num = input('Enter the number of countries: ')
county_with_cities = {}
for i in range(num):
    country, *cities = input('Enter country and some cities: ').split()
    for city in cities:
        county_with_cities[city] = country

number = int(input('Enter count cities? which you want to see: '))
city_list = []
for i in range(number):
    print('Enter city: ')
    city_list.append(input())
for city in city_list:
    print(county_with_cities.get(city, 'the city is not listed'))

# Даны два списка чисел.
# Посчитайте, сколько чисел содержится одновременно
# как в первом списке, так и во втором.

list_l1 = input("Enter list of numbers 1: ")
list_l2 = input("Enter list of numbers 2: ")

set_list_l1 = set(list_l1)
set_list_l2 = set(list_l2)

print("the number of numbers found in both: ", len(set_list_l1 & set_list_l2))

# Даны два списка чисел. Посчитайте,
# сколько чисел входит только в один из этих списков.

print("the number of numbers in the list: ", len(set_list_l1 ^ set_list_l2))
