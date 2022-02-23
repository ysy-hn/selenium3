import csv
import codecs
from itertools import islice

# 读取本地csv文件
data = csv.reader(codecs.open('..\\user_info.csv', 'r'))  # ..\\,相对路径返回代码中的文件；其中一个\是转义。
users = []
# 循环输出每行信息
for line in islice(data, 1, None):
    users.append(line)
print(users)