#####装饰器传多个参数

from time import ctime, sleep

def ftfunc(func):
    def timef(*s, **gs):
        print("[%s] %s() called" % (ctime(), func.__name__))
        return func(*s, **gs)
    return timef


@ftfunc
def foo(*s, **gs):
    print(f"===here s is {s} ===")
    print(f"===here gs is {gs} ===")


if __name__ == "__main__":
    foo()
    foo(1)
    foo(1,2)
    foo(1,2,3)
    stu = {
        'name' : 'bob',
        'age' : 20
    }

    foo(1,2,3,**stu)