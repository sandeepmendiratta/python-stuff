def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

f(g)


print (" This is another example")
print ("***********************")


def f(x):
    print(f'the x value {x}')
    def g(y):
        print(f'the y value {y}')
        return y + x + 3
    return g

nf1 = f(1)
nf2 = f(3)

print(f(2)(9))
# print(nf1(5))
# print(nf2(6))
print ("******************")



print("second example of function calling function")
def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x + b * x + c
    return polynomial

p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)
p3 = polynomial_creator(1, 2, 3)(3)
print(p3)

for x in range(1,3):
    print(x, p1(x), p2(x))


print("***************")

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        print(f'x value {x}')
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
my = our_decorator(foo)

print("We call foo after decoration:")
my(42)

print('*********************************************************')



def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        print(f' the value of x  {x}')
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def succ(n):
    return n + 1

succ(10)

print('\n')
@our_decorator
def foo1(x):
    return x + " how are you"
foo1("me")

print('**************************************')
