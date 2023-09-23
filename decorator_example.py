"""Decorators without parameters example
Example-1
"""


def make_preety(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_preety
def ordinary():
    print("I am ordinary")


# ordinary()

"""Problem Statement: Check the parameters type and passed value using decorator"""


def check_param_type(func):
    def validatetype(param1, param2):
        if type(param1) is not int or type(param2) is not int:
            print("Invalid params")
            return False
        elif param1 <= 0 or param2 <= 0:
            print("Invalid params")
        else:
            return func(param1, param2)

    return validatetype


@check_param_type
def main_method(param1, param2):
    print(param1, param2)


''' parametrized decorator example '''


def print_in_loop(loop_repeate_count):
    def middle_decorator(func):
        def inner(msg: str):
            for i in range(loop_repeate_count):
                func(msg)

        return inner

    return middle_decorator


@print_in_loop(4)
def print_text(msg):
    print(f"welcome to the world of python {msg}")


print_text("Buddy")


# Decorators with parameters Example-2
def prefect_square(string_param):
    def middle_decorator(func):
        def inner(a: int):
            print(f"{string_param} of {a}")
            print(f"The square of {a} is")
            return func(a)

        return inner

    return middle_decorator


@prefect_square("find the square")
def display_square(a):
    return a * a


print(display_square(5))
