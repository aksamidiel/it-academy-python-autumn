def long_word():
    phrase = input("Please enter some phrase with signs separated by space: ")

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

        return "This is longest word in phrase: {}".format(word)

    print(l_word(phrase))


def sym_deleter():
    phrase = input("Please enter simple phrase: ")

    def space_sym_deleter(ph):
        newPhrase = ''
        for i in ph:
            if i not in newPhrase and (i != ' '):
                newPhrase += i
        return "{}".format(newPhrase)

    print(space_sym_deleter(phrase))


def up_low():
    phrase = input("Please enter simple phrase: ")

    def up_lo_letter(ph):
        m = 0
        u = 0
        for i in ph:
            if 'a' <= i <= 'z':
                m += 1
            elif 'A' <= i <= 'Z':
                u += 1
            else:
                pass

        return "Number of lower letter: {} Number of upper letter: {} ".format(m, u)

    print(up_lo_letter(phrase))
