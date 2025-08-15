# [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

import time # 引入模块的所有功能
print("start")
time.sleep(1)
print("end")

from time import sleep # 引入模块的指定功能
print("start")
sleep(1)
print("end")

from time import * # 引入模块的所有功能，使用时候不需要写模块名
print("start")
sleep(1)
print("end")

import time as t # 模块别名
print("start")
t.sleep(1)
print("end")

from time import sleep as sl # 方法别名
print("start")
sl(1)
print("end")