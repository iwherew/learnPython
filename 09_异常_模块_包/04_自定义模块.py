# import my_module1
# my_module1.test(1,2)

from my_module1 import test
test(2,3)

# 不同模块里同名方法导入，会使用最后导入的方法
