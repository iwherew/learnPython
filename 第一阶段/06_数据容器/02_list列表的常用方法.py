list = ["amadeus","iwhere", True, 666]

print(list.index("amadeus")) # 查询元素索引

list[1] = "test" # 修改元素内容
print(list)

list.insert(1, "inserted") # 指定下标插入元素
print(list)

list.append("appended") # 尾部追加元素（单个）
print(list) # ...'appended']

new_list = [33,44]
list.extend(new_list) # 尾部追加新的数据容器（多个，解构后的数据）
print(list) # 'appended', 33, 44]

list.append(new_list)  # 尾部追加元素（单个）
print(list) # 'appended', 33, 44, [33, 44]]

del list[1] # 删除元素
print(list)

element = list.pop(2) # 删除元素并返回
print(list)
print(element)

list.remove(666) # 移除第一个匹配到的元素
print(list)

count = list.count(33) # 统计指定元素的数量
print(count)

length = len(list) # 统计列表长度
print(length)

list.clear() # 清空列表
print(list)
