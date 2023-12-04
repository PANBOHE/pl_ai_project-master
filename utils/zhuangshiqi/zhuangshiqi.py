### 装饰器
### https://www.cnblogs.com/louis-w/p/9578766.html
###
def outer(func):
    def inner():
        print(" ====before function running==== ")
        resdata = func()
        print(" ====after function running==== ")
        return resdata
    return inner  ##这里写 inner  inner() 和 "inner" 三种情况都不一样

@outer
def use4test():
    print("Here is main function work")
    datadic = {
        "info" : "detect info"
    }
    return datadic  




if __name__ == '__main__':
    res = use4test()
    print(res)  

