# from xml.dom.minidom import parse
#
# dom = parse('config.xml')  # 打开xml文件
# root = dom.documentElment  # 得到文档元素对象
# tag_name = root.getElementsByTagName('os')  # 获取一组标签
#
# print(tag_name[0].firstChild.data)
# print(tag_name[1].firstChild.data)
# print(tag_name[2].firstChild.data)


# from xml.dom.minidom import parse
#
# dom = parse('config.xml')
# root = dom.documentElment
# login_info = root.getElementsByTagName('login')
# # 获得login标签的username属性值
# username = login_info[0].getAttribute("username")
# print(username)
# password = login_info[0].getAttribute("password")
# print(password)
