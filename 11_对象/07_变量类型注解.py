# 变量:类型
# 做ide推断或备注，不是强制性的
import json
import random

var_1:int = 10
var_2:str = 'hello'
var_3:bool = True

class Student:
    pass
stu: Student = Student()

my_list:list = [1,2,3]
my_tuple:tuple = (1,2,3)
my_dict:dict = {'a':1,'b':2}
my_set:set = {'a','b'}

my_list1:list[int] = [1,2,3]
my_tuple2:tuple[str, int] = ("a", 1)
my_dict2:dict[str, int] = {'a':1,'b':2}
my_set2:set[str] = {'a','b'}

# 也能在注释中注解，type: 类型
var_4 = random.randint(1,10) # type: int
var_5 = json.loads('{"name": "amadeus"}') # type: dict[str, str]

def func():
    return 10
var_6 = func() # type: int

