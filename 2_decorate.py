def bar():
    print("in the bar")

def test1(func):
    print(func)
    func()

def test2(func):
    print(func)
    return func

bar = test2(bar)
bar()
