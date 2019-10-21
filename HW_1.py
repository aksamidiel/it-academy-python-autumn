# Homework6

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


# task v.2
def is_pal(s_n):
    temp = s_n
    reverse = 0
    while s_n > 0:
        digit = s_n % 10
        reverse = reverse * 10 + digit
        s_n = s_n // 10

    if temp == reverse:
        return "This number is palindrome: {s_n}".format(s_n)
    else:
        return "This number is not palindrome: {s_n}".format(s_n)




# task_fibonacci
# fibonacci start to 1
# ряд фиббоначи начинается с 1
def is_fib(number):
    num1 = num2 = 1
    i = 0
    while i < number - 2:
        fib = num1 + num2
        num1 = num2
        num2 = fib
        i += 1
    return "Number of Fibonacci: {num2}".format(num2)