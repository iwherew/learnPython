class Parent:
    type = "human"

    def hi_parent(self):
        print("hello parent")

class Parent2:
    action = "sleep"

    def do(self):
        print("do")

# 可以多继承，多继承如果有重名变量/重名方法，先继承的保留，后继承的被覆盖，左边最优先
class Child(Parent, Parent2):
    gender = "female"

    def hi_child(self):
        print("hello child")

person = Child()
person.hi_parent()
person.hi_child()
person.do()
print(person.type)
print(person.gender)
print(person.action)