# homework2

rub = int(input('Enter cost in rub(please use whole number: '))
coins = int(input('Enter cost in coins(please use whole number <100 : '))
number_of_items = int(input("Input number of item: "))

rub_our = rub * number_of_items
coin_our = coins * number_of_items
if coin_our >= 100:
    rub_our += coin_our // 100
    coin_our = coin_our % 100
print('Our cost: rub - {} coins - {} '.format(rub_our, coin_our))

# task_palindrome
number = input('Enter number: ')
n = number[::-1]  # переворот чтение введенного с последнего символа <----
if number == n:
    print("yes, this is palindrome")
else:
    print("no, this is not palindrome")

# task_fibonacci
# fibonacci start to 1
# ряд фиббоначи начинается с 1
num1 = num2 = 1

n = int(input("Enter number of Fibonacci: "))
i = 0
while i < n - 2:
    fib = num1 + num2
    num1 = num2
    num2 = fib
    i += 1
print(num2)
