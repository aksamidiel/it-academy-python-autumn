# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания
phrase = input("Please enter some phrase with signs separated by space: ")

print("Entered phrase: ", phrase)

# out = "".join(k for k in phrase if k not in('!', '.', ','))
# print(out)

signs = ['.', ',', ':', ';', '!', '?', '(', ')',
         ' .', ' ,', ' :', ' ;', ' !', ' ?', ' (', ' )',
         '. ', ', ', ': ', '; ', '! ', '? ', '( ', ') ']
list_word = phrase.split()
i = 0

for word in list_word:
    if word[-1] in signs:
        list_word[i] = word[:-1]
        word = list_word[i]
    if word[0] in signs:
        list_word[i] = word[1:]
    i += 1

i = 0
while i < len(list_word):

    print(list_word[i], end=' \n')
    i += 1

long_word = 0
for i in range(1, len(list_word)):
    if len(list_word[long_word]) < len(list_word[i]):
        long_word = i

print('long word/words: ', list_word[long_word])
print("length of word: ", len(list_word[long_word]))

# task2: Вводится строка. Требуется удалить из нее
# повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def",
# то должно быть выведено "abcdef".

phrase = input("Please enter simple phrase: ")
print("Entered phrase: ", phrase)

# list_word = phrase.split()

newPhrase = ''
for i in phrase:
    if i not in newPhrase and (i != ' '):
        newPhrase += i
print(newPhrase)

# Посчитать количество строчных (маленьких) и прописных
# (больших) букв в введенной строке. Учитывать только английские буквы.

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
