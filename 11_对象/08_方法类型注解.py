# 形参的类型注解 和 返回值的类型注解
def sum(my_list: list) -> int:
    count = 0
    for i in my_list:
        count += i
    return count

print(sum([1,2,3,4]))