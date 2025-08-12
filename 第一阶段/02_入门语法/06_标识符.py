# 规则1：内容限定，限定只能使用：中文（不推荐）、英文、数字、下划线。不能以数字开头

# 规则2：大小写敏感
Andy = "Andy1"
andy = "andy2"
print(Andy) # Andy1
print(andy) # andy2


# 规则3：不可使用关键字（大小写敏感）
# SyntaxError: invalid syntax
# class = 1
false = False
true = True
print(false)
print(true)

"""
    变量名规范：
        1、见名知意
        2、下划线命名
        3、英文字母全小写
        
    例子： first_name = "Amadeus"
"""