from HW import HW_1
import types
from HW import HW_1_addon
from HW import HW_2
from HW import HW_3
from HW import HW_4

res = ([getattr(HW_1, x)() for x in dir(HW_1)
        if isinstance(getattr(HW_1, x), types.FunctionType)])
res_1 = ([getattr(HW_1_addon, x)() for x in dir(HW_1_addon)
          if isinstance(getattr(HW_1_addon, x), types.FunctionType)])
res_2 = ([getattr(HW_2, x)() for x in dir(HW_2)
          if isinstance(getattr(HW_2, x), types.FunctionType)])
res_3 = ([getattr(HW_3, x)() for x in dir(HW_3)
          if isinstance(getattr(HW_3, x), types.FunctionType)])
res_4 = ([getattr(HW_4, x)() for x in dir(HW_4)
          if isinstance(getattr(HW_4, x), types.FunctionType)])
#result = [res, res_1, res_2, res_3, res_4]
res_all = res + res_1 + res_2 + res_3 + res_4


def runner(*args):
    if args == '':
        print(res_all)
        return res_all

    elif args == getattr(runner(args), args):
        print(getattr(runner(args), args)())

    else:
        call_list = []
        for i in args:
            call_list.append(i)
        for j in call_list:
            print(getattr(runner(j)()))
