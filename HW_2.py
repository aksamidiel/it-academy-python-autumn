def l_word(ph):
    print("Entered phrase: ", ph)
    signs = '.,/:;&^%$#@!><+=_-*'
    for j in signs:  # поиск и замена символов
        ph = ph.replace(j, '')

    list_word = ph.split()
    length_some_word = len(list_word[-1])
    word = ''
    for i in range(1, len(list_word)):
        if length_some_word < len(list_word[i]):
            length_some_word = len(list_word[i])
            word = list_word[i]

    return "This is longest word in phrase: {word}".format(word)


def space_symb_deleter(phrase):
    newPhrase = ''
    for i in phrase:
        if i not in newPhrase and (i != ' '):
            newPhrase += i
    return "{newPhrase}".format(newPhrase)


def up_lo_letter(phrase):
    m = 0
    u = 0
    for i in phrase:
        if 'a' <= i <= 'z':
            m += 1
        elif 'A' <= i <= 'Z':
            u += 1
        else:
            pass

    return "Number of lower letter: {m} Number of upper letter: {u} ".format(m, u)
