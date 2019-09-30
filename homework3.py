# Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания

fraz = input("Please enter some frases: ")

print("Entered frazes: ", fraz)

list_word = fraz.split()
list_word.
print(len(list_word))
for k in range(len(list_word)):
    for m in list_word[k]:
        if m == "," or m == "!" or m == "/" or m == ".":

            list_word[k] = list_word[k].replace(m, " ")
            list_word.append(list_word[k])
    #list_word
    print(str(list_word[k]))

    #list_word += list_word[k].split()
list_word = str(list_word).split()
print(list_word)
print(len(list_word))



     #print(list_word[k].replace(',', ''))

#for j in range(1, len(list_word)):
   #for k in list_word[j]:
      #  if k == ',':
        #    list_word[j].replace(',', '')






long_word = 0
for i in range(1, len(list_word)):
    if len(list_word[long_word]) < len(list_word[i]):
        long_word = i

print(list_word[long_word])