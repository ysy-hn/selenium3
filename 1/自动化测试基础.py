# # ！/usr/bin/python3
# -*- coding: utf-8 -*-
# 当前项目名称：python_基础教程
# 文件名称： 自动化测试基础
# 登录用户名： yanshaoyou
# 作者： 闫少友
# 邮件： 2395969839@qq.com
# 电话：17855503800
# 创建时间： 2021/10/12  9:50


# back()： 在浏览器历史记录中后退一步
# forward()： 在浏览器历史上前进一步
# close()： 关闭当前窗口
# quit()：退出驱动程序并关闭每个关联的窗口
# refresh()：刷新当前页面
# name：返回此实例的基础浏览器的名称
# title：返回当前页面的标题
# current_url：获取当前页面的URL
# add_cookie(cookie_dict)：为当前会话添加一个cookie，为字典类型
# delete_all_cookies()：删除会话范围内的所有cookie delete_cookie(name)： 删除具有给定名称的单个cookie
# get_cookie(name)：按名称获取单个cookie get_cookies()：返回一组字典的cookies
# execute(driver_command,params=None)： 发送command执行的命令
# execute_async_script(script,*args)：异步执行当前窗口或框架中的JavaScript，它不会阻塞主线程执行
# execute_script(script,*args)：同步执行当前窗口或框架中的JavaScript，用它执行js代码会阻塞主线程执行，直到js代码执行完毕
# get(url)：在当前浏览器会话中加载网页，一定要输入全部链接，包括“http://”，否则可能找不到
# get_log(log_type)：获取给定日志类型的日志
# get_screenshot_as_base64()：获取当前窗口的屏幕截图，作为base64编码的字符串
# get_screenshot_as_file(filename)：将当前窗口中的截屏保存为png图形
# save_screenshot(filename)：将当前窗口的屏幕截图保存为PNG图形文件
# get_screenshot_as_png()：获取当前窗口的屏幕截图作为二进制数据
# get_window_position(windowhandle=‘current’)：获取当前窗口的x,y位置
# get_window_rect()：获取窗口的x,y坐标以及当前窗口的高度和宽度
# get_window_size()：获取当前窗口的高度和宽度
# maximize_window()：最大化webdriver正在使用的当前窗口
# minimize_window()：最小化当前webdricer使用窗口
# fullscreen_window()：调用窗口管理器特定的全屏操作
# set_window_rect(x=None,y=None,width=None,height=None)：设置窗口的x,y坐标以及当前窗口的高度和宽度
# set_window_size(width,height,windowHandle=‘current’)：设置当前窗口的高度和宽度
# set_window_position(x,y,windowHandle=‘current’)：设置当前窗口的x,y位置
# current_window_handle：返回当前窗口的句柄
# window_handles：返回当前会话中所有窗口的句柄
# create_web_element(element_id)： 使用指定的id创建Web元素
# set_page_load_timeout(time_to_wait)：设置等待页面加载完成的时间
# set_script_timeout(time_to_wait)：设置脚本在执行期间等待的时间
# desired_capabilities：返回驱动程序当前使用的所需功能
# log_types：获取可用日志类型的列表
# page_source：获取当前页面的源码
# switch_to 将焦点切换到所有选项的对象上
# switch_to.alert 返回浏览器的Alert对象，可对浏览器alert、confirm、prompt框操作
# switch_to.default_content() 切到主文档
# switch_to.frame(frame_reference) 切到某个frame
# switch_to.parent_frame() 切到父frame，有多层frame的时候很有用
# switch_to.window(window_name) 切到某个浏览器窗口
# switch_to.active_element 返回当前焦点的WebElement对象，网页上当前操作的对象（也就是你网页上光标的位置），比如你鼠标点击到了一个input框，你可以在这个input框里输入信息，这时这个input框即焦点。