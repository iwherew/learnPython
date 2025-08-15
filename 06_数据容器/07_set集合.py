# set 集合 不允许重复，内容无序，不支持下标索引访问

my_set = {"amadeus","iwhere","python","amadeus","iwhere","python","amadeus","iwhere","python"}
my_set_empty = set() # 定义空集合
print(my_set) # {'python', 'iwhere', 'amadeus'}
print(my_set_empty) # set()

my_set.add("java") # 添加元素
print(my_set)

my_set.remove("iwhere") # 移除元素
print(my_set)

element = my_set.pop() # 随机取一个元素，并在集合内删除
print(element)
print(my_set)

my_set.clear() # 清空集合
print(my_set)

# 取两个集合的差集
# set1.difference(set2)
# 取出set1有而set2没有的，不修改原集合
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2) # {2, 3}
print("set1 is", set1) # {1, 2, 3}
print("set2 is", set2) # {1, 5, 6}
print("set3 is", set3) # {2, 3}

# 消除两个集合的差集
# set1.difference_update(set2)
# 在set1中删除和set2相同的元素
# 没有返回值，直接修改set1
set1.difference_update(set2)
print("set1 is", set1) # {2, 3}
print("set2 is", set2) # {1, 5, 6}

# 合并两个集合，返回一个新集合
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print("set3 is", set3) # {1, 2, 3, 5, 6}

# 统计集合元素数量
print(len(set1))

# 集合的遍历
for item in set1:
    print(item)