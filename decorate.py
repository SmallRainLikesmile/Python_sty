import time

def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("The func run time is %s"%(stop_time - start_time))
    return warpper

@timmer
def test1():
    time.sleep(3)
    print("In th test1")


test1()
