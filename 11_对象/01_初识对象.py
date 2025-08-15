class Student:
    name = None,
    gender = None,
    age = None,

    # self 必写，形参从第二个参数开始传入
    def hi(self):
        print(f"name: {self.name}, gender: {self.gender}, age: {self.age}")

    def add(self, num):
        self.age += num
        print(f"age: {self.age}")

stu1 = Student()
stu1.name = 'amadeus'
stu1.gender = 'male'
stu1.age = 20

print(stu1.name)
stu1.hi()

stu1.add(2)