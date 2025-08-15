t1 = (1, 'hello', True)
t2 = ()
t3 = tuple()

print(t1)
print(t2)
print(t3)

# 定义单个元素元组, 需要在后面加逗号
t4 = ("hello",)
print(f"type(t4) = {type(t4)}")

# 元组可嵌套
t5 = ((1,2,3),(4,5,6))
print(t5)

print(t5[1][2]) # 通过下标取元素

t6 = ("amadeus","iwhere")
index = t6.index("iwhere") # 查找指定元素的下标
print(index)

t7 = ("amadeus","iwhere", "amadeus", "amadeus")
count = t7.count("amadeus") # 统计指定元素数量
print(count)

t8 = ("amadeus","iwhere", "amadeus", "amadeus")
length = len(t8) # 统计元组长度
print(length)

index = 0
while index < len(t8):
    print(t8[index])
    index = index + 1

for item in t8:
    print(item)

# 元组里的元素不可修改，如果元组里有list，可以修改里面的list