# 可以使用闭包实现，在已有函数执行前后添加功能
def outerFunc(func):
    def inner():
        print("before")
        func()
        print("after")
    return inner

def doing():
    print("doing")

fn = outerFunc(doing)
fn()

# 使用装饰器（注解）
@outerFunc
def doing2():
    print("doing2")

doing2()