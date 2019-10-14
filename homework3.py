"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания"""
phrase = input("Please enter some phrase with signs separated by space: ")

print("Entered phrase: ", phrase)

signs = '.,/:;&^%$#@!><+=_-*'
for j in signs:   # поиск и замена символов
    phrase = phrase.replace(j, '')

list_word = phrase.split()
length_some_word = len(list_word[-1])
word = ''
for i in range(1, len(list_word)):
    if length_some_word < len(list_word[i]):
        length_some_word = len(list_word[i])
        word = list_word[i]
print("This is longest word in phrase: ", word)

""" task2: Вводится строка. Требуется удалить из нее
 повторяющиеся символы и все пробелы.
 Например, если было введено "abc cde def",
 то должно быть выведено "abcdef"."""

phrase = input("Please enter simple phrase: ")
print("Entered phrase: ", phrase)

newPhrase = ''
for i in phrase:
    if i not in newPhrase and (i != ' '):
        newPhrase += i
print(newPhrase)

""" Посчитать количество строчных (маленьких) и прописных
(больших) букв в введенной строке. Учитывать только английские буквы. """

phrase = input("Please enter simple phrase: ")
print("Entered phrase: ", phrase)

m = 0
u = 0
for i in phrase:
    if 'a' <= i <= 'z':
        m += 1
    elif 'A' <= i <= 'Z':
        u += 1
    else:
        pass

print("Number of lower letter: ", m, end="\n")
print("Number of upper letter: ", u, end="\n")
