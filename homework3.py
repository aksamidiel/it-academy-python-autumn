# Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания

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