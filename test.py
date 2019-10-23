
def long_word():
    phrase = input("Please enter some phrase with signs separated by space: ")
    def l_word(ph):
        word = ''
        print("Entered phrase: ", ph)
        signs = '.,/:;&^%$#@!><+=_-*'
        for j in signs:  # поиск и замена символов
            ph = ph.replace(j, '')

        list_word = ph.split()
        length_some_word = len(list_word[-1])
        for i in range(1, len(list_word)):
            if length_some_word < len(list_word[i]):
                length_some_word = len(list_word[i])
                word = list_word[i]

        return "This is longest word in phrase: {}".format(word)

    print(l_word(phrase))

long_word()