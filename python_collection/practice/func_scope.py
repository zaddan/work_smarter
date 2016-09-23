def foo1(x):
    def foo2():
        print x
    foo2()

foo1(3)
