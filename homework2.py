# homework2
#
# Our cost of item's v.2
rub = int(input('Enter cost in rub(please use whole number: '))
coins = int(input('Enter cost in coins(please use whole number <100 : '))
number_of_items = int(input("Input number of item: "))

if coins * number_of_items >= 100:
    # число рублей с учетом монет
    rub = rub * number_of_items + (coins * number_of_items) // 100
    # остаток монеток
    coins = (coins * number_of_items) % 100
else:
    rub = rub * number_of_items
    coins = coins * number_of_items

print('Our cost: rub - {} coins - {} '.format(rub, coins))

# task_palindrome v.2
some_number = int(input("Enter some number: "))
temp = some_number
reverse = 0

while some_number > 0:
    digit = some_number % 10
    reverse = reverse * 10 + digit
    some_number = some_number // 10

if temp == reverse:
    print("This number is palindrome")
else:
    print("This number is not palindrome")

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
