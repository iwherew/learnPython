# 控制*引入的方法
__all__ =["test"]

def test(a, b):
    print(a + b)

def test2(a, b):
    print(a + b)



# 只在本模块运行，不在引用的模块运行
if __name__ == '__main__':
    print("inner module")