my_dict = {
    "name" : "amadeus",
    "age": 22,
    "money": 1000
}

# 定义空字典
empty_dict1 = {}
empty_dict2 = dict()

print(my_dict)
print(my_dict["name"]) # 根据key获取value值

my_dict["sex"] = 'male' # 新增/修改
print(my_dict)

money = my_dict.pop("money") # 删除元素并返回
print(money)
print(my_dict)

keys = my_dict.keys() # 获取所有的keys
print(keys)

# 遍历字典
for key in my_dict.keys():
    print(f"{key}: {my_dict[key]}")

for key in my_dict:
    print(f"{key}: {my_dict[key]}")

print(len(my_dict)) # 统计元素数量

my_dict.clear() # 清空元素
print(my_dict)


