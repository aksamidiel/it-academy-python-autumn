some_str = input("Enter some text: ")


def rep_word(s_st):
    s_st.lower().split(" ")
    list_buf = []
    dict_buf = {}
    for i in s_st:
        if i not in list_buf:
            list_buf.append(i)
            dict_buf[i] = 1
        else:
            dict_buf[i] += 1
    for i in range(len(list_buf)):
        print(list_buf[i] + " " + str(dict_buf[list_buf[i]]))

rep_word(some_str)

