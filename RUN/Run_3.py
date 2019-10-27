from HW import HW_1
from HW import HW_1_addon
from HW import HW_2
from HW import HW_3
from HW import HW_4


def runner_3(elem):
    call_list = []
    for i in elem:
        call_list.append(i)

    for j in call_list:

        if j == '1':
            HW_1.input_calculate()
        elif j == '2':
            HW_1.input_palindrome()
        elif j == '3':
            HW_1.input_fib()
        elif j == '4':
            HW_1_addon.simple_input()
        elif j == '5':
            HW_1_addon.roma_num_input()
        elif j == '6':
            HW_1_addon.simple_math_sight()
        elif j == '7':
            HW_1_addon.simple_converter()
        elif j == '8':
            HW_1_addon.simple_rep()
        elif j == '9':
            HW_2.long_word()
        elif j == '10':
            HW_2.sym_deleter()
        elif j == '11':
            HW_2.up_low()
        elif j == '12':
            HW_3.sm_print()
        elif j == '13':
            HW_3.test_list_comp()
        elif j == '14':
            print(HW_4.range_calc())
        elif j == '15':
            HW_4.simple_dict_const()
        elif j == '16':
            HW_4.spl_search()
        elif j == '17':
            HW_4.tw_l()
        elif j == '18':
            HW_4.tw_dif()
        else:
            print("Not operation")
