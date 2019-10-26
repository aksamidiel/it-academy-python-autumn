from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "ru")


def save_func(dec_fun):
    def wrapper(*args, **kwargs):
        return_inf = dec_fun(*args, **kwargs)
        with open("save_fun.txt", "a") as f_obj:
            f_obj.write(str(datetime.now()) + "\n" + return_inf + "\n")
        print(return_inf)

    return wrapper


# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания

def long_word():
    phrase = input("Please enter some phrase with signs separated by space: ")

    @save_func
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


# task2: Вводится строка. Требуется удалить из нее
# повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def",
# то должно быть выведено "abcdef".

def sym_deleter():
    phrase = input("Please enter simple phrase: ")

    @save_func
    def space_sym_deleter(ph):
        newPhrase = ''
        for i in ph:
            if i not in newPhrase and (i != ' '):
                newPhrase += i
        return "{}".format(newPhrase)

    print(space_sym_deleter(phrase))


# Посчитать количество строчных (маленьких) и прописных
# (больших) букв в введенной строке. Учитывать только английские буквы.

def up_low():
    phrase = input("Please enter simple phrase: ")

    @save_func
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
