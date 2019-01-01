def decorator(func):
    def helper(x):
        print("Decorating", func.__name__)
        func(x)
    return helper


@decorator
def foo(x):
    print(x)


foo("sandeep")

print('***************************')

def decorator1(f):
    def helper():
        print("Decorating", f.__name__)
        f()
    return helper

@decorator1
def foo():
    print("inside foo()")

foo()


#The following decorator implemented as a class does the same "job":
class decorator2:
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        print("Decorating", self.f.__name__)
        self.f(x)

@decorator2
def foo(x):
    print("inside foo()", x)

foo("me")


print('****************************************')

def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
        print("Decorating", func.__name__)
        func(name)
    return func_wrapper

@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))
