import json

with open('user_info.json') as f:
    data = f.read()

user_list = json.loads(data)
print(user_list)
