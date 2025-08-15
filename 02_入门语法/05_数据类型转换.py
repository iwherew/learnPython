int_str = str(666)
print(type(int_str), int_str)

str_int = int("111")
print(type(str_int), str_int)

str_float = float("12.34")
print(type(str_float), str_float)

# ValueError: invalid literal for int()
# int("he")

int_float = float(13)
print(type(int_float), int_float) # 13.0

float_int = int(12.66)
print(type(float_int), float_int) # 12