# 打开文件
f = open("test.txt","r",encoding="utf-8")
# print(type(f))

# 读取文件 - read()， 多次调用会从上次读取结束的地方开始读取
# print(f"读取4个字节：{f.read(4)}")
# print(f"读取全部内容：{f.read()}")

# 读取文件 - readlines() 读取多行内容并转为列表
# lines = f.readlines()
# print(lines)

# 读取文件 - readLine() 一次读取一行内容
# line1 = f.readline()
# line2 = f.readline()
# print(f"line1: {line1}")
# print(f"line2: {line2}")

# for循环读取文件行
# for line in f:
#     print(f"each line: {line}")

# 关闭文件，不关闭会被程序占用
# f.close()

# with open 操作文件，自动close
with open("test.txt","r",encoding="utf-8") as f:
    for line in f:
        print(f"each line: {line}")
