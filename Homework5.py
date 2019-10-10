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
dict_res = dict((ch, some_string.count(ch)) for ch in set(some_string))
print("Result", dict_res)

# Задача. Дан текст (строк может быть много, разделенных \n).
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в
# лексикографическом порядке.

some_text = input("Enter some text: ").split()
print(some_text)

some_text = [line.rstrip() for line in some_text]
dict_res = dict((word, some_text.count(word)) for word in set(some_text))
print(dict_res)

sort_res = sorted(dict_res.items(), key=lambda i: (-i[1], i[0]))[0]   # tuple
print("Result sorted: ", sort_res[0])


