import test.runner as Runner

# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner.
# runner() – все фукнции вызываются по очереди
# runner(‘gen_numbers’) – вызывается только функцию gen_numbers.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции
p = input("Enter: ")
if p == '1':
    Runner()
elif p == '2':
    name_f = input("Name of function: ")
    Runner(name_f)
else:
    lst_name_f = input("Enter some function: ")
    Runner(lst_name_f)
