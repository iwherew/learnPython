class Student:
    name = None,
    gender = None,
    age = None,

    # 构造方法
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    # 字符串方法，不写的话打印返回对象地址
    def __str__(self):
        return f'name: {self.name}, gender: {self.gender}, age: {self.age}'

    # < 小于比较，返回小于为true的逻辑，不需要写大于逻辑
    def __lt__(self, other):
        return self.age < other.age

    # < 小于等于比较，返回小于等于为true的逻辑
    def __le__(self, other):
        return self.age <= other.age

    # 等于比较
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("amadeus","female",18)
print(stu1)

stu2 = Student("iwhere","male",11)
stu3 = Student("ct","male",20)

print(stu1 < stu2)
print(stu1 > stu2)
print(stu1 < stu3)
print(stu1 > stu3)
print(stu1 >= stu3)

stu4 = Student("he","male",18)
print(stu1 == stu4)