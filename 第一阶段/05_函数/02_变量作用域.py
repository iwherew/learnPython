num = 10

def test_a():
    num = 50
    print("num =", num) # 50

test_a()
print(f"global num = {num}") # 10

def test_b():
    global num # global 声明是全局变量
    num = 50
    print("num =", num) # 50

test_b()
print(f"global num = {num}") # 50