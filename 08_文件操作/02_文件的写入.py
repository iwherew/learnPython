# 打开文件
# w模式会创建新文件或覆盖旧文件
# a模式会创建新文件或续写旧文件
f = open("test.txt","a",encoding="utf-8")

# write写入
f.write("hello world\npython\n")

# flush，将内存的中内容写入到硬盘里
f.flush()

# 关闭文件，close内置flush功能
f.close()