# 通过占位的形式，完成拼接
name = "amadeus"
tel = 1234
message = "name: %s, tel:%s" % (name, tel)
print(message)

name = "长和"
year = 1950
price = 50.5
# %.2f 控制精度为小数点后两位
message = "name: %s, year: %d, price: %.2f" % (name, year, price)
print(message)

# 快速格式化，字符串前用f开头，不限制数据类型，不控制精度
msg = f"name: {name}, year: {year}, price: {price}"
print(msg)