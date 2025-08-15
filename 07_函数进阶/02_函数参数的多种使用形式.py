def user_info(name, age, gender = 'male'):
    print(f"name: {name}, age: {age}, gender: {gender}")

# 位置参数 - 默认使用形式，根据位置对应
user_info("amadeus", 20, 'male')

# 关键字参数, 可以不按照参数定义的顺序传参
user_info(name = 'amadeus', age = 20, gender = 'male')
user_info(age = 20, gender = 'male', name = 'amadeus')
user_info('amadeus', gender = 'male', age = 20) # 位置参数先使用，再用关键字参数

# 缺省参数（默认值）
user_info("amadeus", 20)

# 不定长 - 位置不定长， *号
# 不定长定义的形式参数会作为元组存在
def user_info(*args):
    print(f"args: {args}") # 元组

user_info("amadeus", 20, 'male')

# 不定长 - 关键字不定长， **号
# 不定长定义的形式参数会作为字典存在
def user_info(**kwargs):
    print(f"kwargs: {kwargs}") # 字典

user_info(name = 'amadeus', age = 20, gender = 'male')