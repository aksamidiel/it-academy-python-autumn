# Homework6
# task_1
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


def input_calculate():
    rub = int(input('Enter cost in rub(please use whole number): '))
    coins = int(input('Enter cost in coins(please use whole number <100 : '))
    number_of_items = int(input("Input number of item: "))

    @save_func
    def calc(n, r, c):
        if c * n >= 100:
            # число рублей с учетом монет
            r = r * n + (c * n) // 100
            # остаток монеток
            c = (c * n) % 100
        else:
            r = r * n
            c = c * n

        return 'Our cost: rub = {}  coins = {} item = {}'.format(r, c, n)

    print(calc(rub, coins, number_of_items))


# task v.2
def input_palindrome():
    some_number = int(input("Enter some number: "))

    @save_func
    def is_pal(s_n):
        temp = s_n
        reverse = 0
        while s_n > 0:
            digit = s_n % 10
            reverse = reverse * 10 + digit
            s_n = s_n // 10

        if temp == reverse:
            return 'This number is palindrome: {}'.format(temp)
        else:
            return 'This number is not palindrome: {}'.format(temp)

    print(is_pal(some_number))


# task_fibonacci
# fibonacci start to 1
# ряд фиббоначи начинается с 1
def input_fib():
    n = int(input("Enter number of Fibonacci: "))

    @save_func
    def is_fib(number):
        num1 = num2 = 1
        i = 0
        while i < number - 2:
            fib = num1 + num2
            num1 = num2
            num2 = fib
            i += 1
        return "Number of Fibonacci: {}".format(num2)

    print(is_fib(n))
