for i in range(5):
    if i == 3:
        continue # 跳出本次循环，进行下一轮循环
    print(i)

print("-----------")

for i in range(5):
    if i == 3:
        break # 结束本次循环
    print(i)