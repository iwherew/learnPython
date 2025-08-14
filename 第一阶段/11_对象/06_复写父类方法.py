class Parent:
    msg = 'parent msg'
    type = 'human'

    def hi(self):
        print("hi parent")

    def say(self):
        print(f"say something: {self.msg}")

class Child(Parent):
    msg = 'child msg'

    def hi(self):
        print("hi child")

    def say_child(self):
        # 使用父类的成员和方法
        # 方式一：使用父类的类名调用，方法要传self
        print(Parent.type)
        Parent.say(self)
        # 方式二：使用super调用，不用传self
        print(super().type)
        super().say()

person = Child()
person.hi()
print(person.msg)
person.say() # say something: child msg
person.say_child()