# Homework6
# task_1
rub = int(input('Enter cost in rub(please use whole number): '))
coins = int(input('Enter cost in coins(please use whole number <100): '))
number_of_items = int(input("Input number of item: "))


def calc(n, r, c):
    if c * n >= 100:
        # число рублей с учетом монет
        r = r * n + (c * n) // 100
        # остаток монеток
        c = (c * n) % 100
    else:
        r = r * n
        c = c * n

    return 'Our cost: rub = {}  coins = {}'.format(r, c)


rub = int(input('Enter cost in rub(please use whole number: '))
coins = int(input('Enter cost in coins(please use whole number <100 : '))
number_of_items = int(input("Input number of item: "))

result = calc(number_of_items, rub, coins)


# task v.2
def is_pal(s_n):
    reverse = 0
    while s_n > 0:
        digit = s_n % 10
        reverse = reverse * 10 + digit
        s_n = s_n // 10

    if temp == reverse:
        return "This number is palindrome: {s_n}".format(s_n)
    else:
        return "This number is not palindrome: {s_n}".format(s_n)


some_number = int(input("Enter some number: "))
temp = some_number

is_pal(some_number)

# task_fibonacci
# fibonacci start to 1
# ряд фиббоначи начинается с 1

n = int(input("Enter number of Fibonacci: "))


def is_fib(number):
    num1 = num2 = 1
    i = 0
    while i < number - 2:
        fib = num1 + num2
        num1 = num2
        num2 = fib
        i += 1
    return "Number of Fibonacci: {num2}".format(num2)


is_fib(n)
