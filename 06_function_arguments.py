def say_hello(name):
    print("hello", name)


say_hello("Popo")


def plus(a, b):
    print("a =", a)
    print("b =", b)
    print("a + b =", a + b)


def minus(a, b=1):
    print("a =", a)
    print("b = ", b)
    print("a - b = ", a - b)


plus(2, 5)
minus(2)