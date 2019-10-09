res = []
some_text = input("Enter some text: ").split()
print(some_text)
for st in some_text:
    print(st)
    res += st.rstrip('/n')
print(res)

#print(some_text)

dict_res = dict((word, res.count(word)) for word in set(res))

print(dict_res)
