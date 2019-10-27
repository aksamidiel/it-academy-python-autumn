from RUN import Run_1
from RUN import Run_2
from RUN import Run_3

# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner.
# runner() – все фукнции вызываются по очереди
# runner(‘gen_numbers’) – вызывается только функцию gen_numbers.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции
Run_1.runner_1()
n = input("Number of function(1-18): ")
Run_2.runner_2(n)
n = input("Enter some function(1-18): ")
Run_3.runner_3(n)
