def make_preety(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_preety
def ordinary():
    print("I am ordinary")


# ordinary()
# In the example shown below, make_pretty() is a decorator. In the assignment step. The function ordinary() got decorated and the returned function was given the name pretty.
# preety = make_preety(ordinary)
# preety()


# Decorator with parameter example

def smart_division(func):
    def inner(a, b):
        # Put here the code you want to be executed BEFORE the original function is called
        # print("I am going to divide", a, "and", b)
        if b == 0:
            print("Aahh can't divide")
            return
        # Call the function here (using parentheses)
        return func(a, b)
        # Put here the code you want to be executed AFTER the original function is called

    return inner


# General decorators that work with any number of parameters

def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)

    return inner


@smart_division
def divide(a, b):
    return a / b

# print(divide(10, 0, 1))
