# 1. Write a program that prints the numbers from 1 to 100,
# but for multiples of three print “Fizz” instead of the
# number and for multiples of five print “Buzz”.
# For numbers which are multiples of both three and five,
# print “FizzBuzz”.


print("Prints row numbers: ")
first_position = int(input("Please enter first position: "))
last_position = int(input("Please enter last position: "))
lst = []
for i in range(first_position, last_position):

    if i % 3 == 0 and i % 5 == 0:
        lst.append('FizzBuzz')

    elif i % 3 == 0:
        lst.append('Fizz')
    elif i % 5 == 0:
        lst.append('Buzz')
    else:
        lst.append(i)

index = 0
for ls in lst:   # цикл вывода
    print(lst[index], end=", ")
    index += 1

# for j in range(first_position, last_position):
#    print("Result: ", lst[j])
