def foo():
    print('in the foo')
    bar()
def bar():
    print('in the bar')
    foo()

foo()
