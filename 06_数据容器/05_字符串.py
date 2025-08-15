my_str = "my name is amadeus"

print(my_str[1])
print(my_str[-2])

# 字符串是无法修改的，调用str的方法会得到一个新字符串

# index
print(my_str.index("is"))

# replace，不修改原字符串，返回一个替换后的字符串
new_str = my_str.replace("amadeus", "iwhere")
print(new_str)

# split 返回一个切分后的list
split_list = new_str.split(" ")
print(split_list)

# strip 去除前后指定字符，不传参数默认空格，传入参数去除匹配上的所有字符串及子串
my_str1 = "  my name is amadeus  "
print(my_str1.strip())
my_str2 = "abbcbba"
print(my_str2.strip("ab")) # c

print(my_str2.count("bb")) # 统计指定字符串出现次数
print(len(my_str2)) # 统计字符串长度