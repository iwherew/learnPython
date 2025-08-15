# 基本捕获语法（捕获所有异常）
try:
    f = open("hello.txt", 'r', encoding='utf-8')
except:
    print("出现异常")
    f = open("hello.txt", 'w', encoding='utf-8')

# 捕获指定异常
try:
    print(val)
except NameError as e:
    print("出现变量未定义的异常")
    print(e) # name 'val' is not defined

# 捕获多个异常
try:
    1 / 0
    print(val)
except (NameError, ZeroDivisionError) as e:
    print("出现变量未定义 或者 除0异常")

# 捕获所有异常
try:
    1 / 0
    print(val)
except Exception as e:
    print("出现异常")

# 异常else，没有出现异常的时候执行else代码
# 异常finally，最后执行的代码，无论有无异常都要执行，比如资源关闭
try:
    print('hello')
except Exception as e:
    print(e)
else:
    print('no exception')
finally:
    print("end")