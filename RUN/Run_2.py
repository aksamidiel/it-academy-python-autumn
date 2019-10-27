from HW import HW_1
from HW import HW_1_addon
from HW import HW_2
from HW import HW_3
from HW import HW_4


def runner_2(num):
    if num == '1':
        HW_1.input_calculate()
    elif num == '2':
        HW_1.input_palindrome()
    elif num == '3':
        HW_1.input_fib()
    elif num == '4':
        HW_1_addon.simple_input()
    elif num == '5':
        HW_1_addon.roma_num_input()
    elif num == '6':
        HW_1_addon.simple_math_sight()
    elif num == '7':
        HW_1_addon.simple_converter()
    elif num == '8':
        HW_1_addon.simple_rep()
    elif num == '9':
        HW_2.long_word()
    elif num == '10':
        HW_2.sym_deleter()
    elif num == '11':
        HW_2.up_low()
    elif num == '12':
        HW_3.sm_print()
    elif num == '13':
        HW_3.test_list_comp()
    elif num == '14':
        print(HW_4.range_calc())
    elif num == '15':
        HW_4.simple_dict_const()
    elif num == '16':
        HW_4.spl_search()
    elif num == '17':
        HW_4.tw_l()
    elif num == '18':
        HW_4.tw_dif()
    else:
        print("Not operation")
