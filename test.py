some_text = input("Enter some text: ").split()

dict_res = {}
for word in some_text:
    dict_res[word] = dict_res.get(word, 0) + 1
print(dict_res)

max_lst = []
m_word_in_text = max(dict_res.values())
for key in dict_res.keys():
    if dict_res[key] == m_word_in_text:
        max_lst.append(key)
max_lst = sorted(max_lst)
print("Result sorted: ", max_lst[0])
