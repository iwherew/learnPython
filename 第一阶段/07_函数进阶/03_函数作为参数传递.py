def test_func(compute):
    result = compute(1, 2)
    print(result)

def func(x, y):
    return x + y

test_func(func)

# 匿名函数
# lambda 传入参数:函数体（一行代码）
test_func(lambda x, y: x * y)