# 私有成员变量和方法都以两个下划线开头 __xxx

class Phone:

    __name = None,

    def __init__(self,name):
        self.__name = name

    def __hi(self):
        print("hello")

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

phone = Phone("iphone")
# print(phone.__name) # AttributeError: 'Phone' object has no attribute '__name'
# phone.__hi() # AttributeError: 'Phone' object has no attribute '__hi'

print(phone.getName())
phone.setName("xiaomi")
print(phone.getName())