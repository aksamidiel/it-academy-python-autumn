
phrase = input("Please enter simple phrase: ")
print("Entered phrase: ", phrase)

#list_word = phrase.split()


newPhrase = ''
for i in phrase:
    if i not in newPhrase and (i != ' '):
        newPhrase += i
print(newPhrase)







