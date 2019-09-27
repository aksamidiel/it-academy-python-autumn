# task_fibonnachi
# fibbonachi start to 1
num1 = 1
num2 = 1

n = int(input("Enter number of Fibbonachi: "))
i = 0
while i < n - 2:
    fib = num1 + num2
    num1 = num2
    num2 = fib
    i += 1

print(num2)