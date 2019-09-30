phrase = input("Please enter simple phrase: ")
print("Entered phrase: ", phrase)

#list_word = phrase.split()


#newPhrase = ''
#for i in phrase:
    #if i not in newPhrase and (i != ' '):
       # newPhrase += i
#print(newPhrase)
# //////////
#list_word = phrase.split()
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







