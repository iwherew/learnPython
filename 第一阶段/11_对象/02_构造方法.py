class Student:
    name = None,
    gender = None,
    age = None,

    # 构造方法
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    # self 必写，形参从第二个参数开始传入
    def hi(self):
        print(f"name: {self.name}, gender: {self.gender}, age: {self.age}")

stu1 = Student("iwhere","female",18)
stu1.hi()