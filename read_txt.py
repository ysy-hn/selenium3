file = './/user_info.txt'
# 读取文件
with open(file, 'r') as f:
    data = f.readlines()
# 格式化处理
users = []
for line in data:
    user = line[:-1].split(":")
    users.append(user)

# 打印users二维数组
print(users)

