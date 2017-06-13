import time

def timer(func):
    def deco(*args,**argv):
        StartTime = time.time()
        func(*args, ** argv)
        StopTime = time.time()
        print("the func run time is %s"%(StopTime - StartTime))
    return deco

@timer
def test1():
    time.sleep(3)
    print("in the test1")

@timer
def test2(name):
    time.sleep(3)
    print("in the test2 %s"%name)

test1()
test2('asdasd')
