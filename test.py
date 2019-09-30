



# является ли фигура треугольником

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a+b) < c or (b+c) < a or (c+a) < b:
    print("This is not triangle")

else:
    p = (a + b + c) / 2
    square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Square: ", square)


stroka = input("Vvedite stroky: ")

#вывести 3 символ строки
print(stroka[3])
#предпоследний символ строки
print(stroka[-2])
#вывести первые 5 символов строки введенной
print(stroka[:5])
#вывести всю строку кроме паследних 2 символов
print(stroka[:len(stroka)-2])
#вывести все символы с четными индексами
print(stroka[0::2])
#вывести все символы с нечетными индексами
print(stroka[::2])
#вывести символы в обратном порядке
print(stroka[::-1])
#символы через один в обратном порядке
print(stroka[::-2])
#вывести длину введенной строки
print(len(stroka))



# дана строка , удалить все пробелы и выяснить является ли строка палиндромом

stroka = input("Vvedite stroky: ")

a = input("vvedite ydaliaemiy simvol: ")
b = input("simvol vmesto ydaliaemogo: ")



#удаление simvola
print("res: ", stroka.replace(a, b))

#определение является ли строка палиндромом


if stroka[::] == stroka[::-1]:
    print("This is palindrome")
else:
    print("is not palindrome")



#удаление пробелов
# rstrip()   -справа
# lstrip()   -слева
# strip()    -с обоих сторон