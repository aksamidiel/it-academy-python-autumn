


def decorator_with_arguments(func_to_decorate):
    def wrapper_accepting(*args, **kwargs):
        print("parameters: args{}  kwargs{}", args, kwargs)
        func_to_decorate(*args, **kwargs)
    return wrapper_accepting

@decorator_with_arguments
def function_without_arg():
    print("without argument's")

function_without_arg()

@decorator_with_arguments
def function_with_arg(a, b, c):
    print(a, b, c)

function_with_arg(5, 4, 3)





