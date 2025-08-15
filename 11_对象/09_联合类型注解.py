# 数据类型可能有多种类型，使用Union
from typing import Union

my_list: list[Union[str, int]] = [1,2,"hello"]

my_dict: dict[str, Union[str, int]] = {"name":"amadeus", "age": 20}

def func(data: Union[int, str]) -> Union[int, str]:
    pass
