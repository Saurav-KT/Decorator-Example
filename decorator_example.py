def make_preety(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_preety
def ordinary():
    print("I am ordinary")


# call function
# ordinary()

# In the example shown below, make_pretty() is a decorator. In the assignment step. The function ordinary() got decorated and the returned function was given the name pretty.
# preety = make_preety(ordinary)
# preety()


# Decorator with parameter example
def check_param_type(func):
    def validatedatatype(param1, param2):
        if type(param1) is not int or type(param2) is not int:
            print("Invalid params")
            return False
        elif param1 <= 0 or param2 <= 0:
            print("Invalid params")
        else:
            return func(param1, param2)

    return validatedatatype


@check_param_type
def main_method(param1,param2):
    print(param1,param2)

# print(divide(10, 0))
