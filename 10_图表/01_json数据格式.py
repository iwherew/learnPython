import json
data = [{"name": "amadeus", "age": 11},{"name": "iwhere", "age": 22}]
# 将数据转为json字符串
json_str = json.dumps(data)
print(f"type: {type(json_str)}, json_str: {json_str}")
# 将json字符串转为数据
p_data= json.loads(json_str)
print(f"type: {type(p_data)}, p_data: {p_data}")
