def my_len(data):
    print(f"length: {len(data)}")

my_len(range(5))
my_len(range(1,100,2))
my_len("amadeus")

def add_one(x):
    return x + 1

x = add_one(1)
print(x)

# 函数的注释
def add(x, y):
    """
    add函数可以接收两个参数，进行两数相加的功能
    :param x: 相加的其中一个数字
    :param y: 相加的另外一个数字
    :return: 相加的结果
    """
    return x + y

x = add(1, 2)
print(x)