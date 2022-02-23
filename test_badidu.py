# # 4.2 控制浏览器大小
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.set_window_size(480,800)  # 设置浏览器尺寸显示
# driver.maximize_window()  # 设置浏览器最大尺寸显示
# print("设置浏览器宽480、高800显示")
# driver.quit()
#
#
# # 访问百度首页
# first_url = 'https://www.baidu.com'
# print("now access:%s" %(first_url))
# driver.get(first_url)
#
# # 访问新闻页
# second_url = 'https://news.baidu.com'
# print("now access:%s" %(second_url))
# driver.get(second_url)
#
# print('back to:%s' %(first_url))
# driver.back()  # 返回（后退）到百度首页
#
# print('forward to:%s' %(second_url))
# driver.forward()  # 前进到新闻页
# driver.refresh()  # 刷新当前页面
#
#
# # 4.3 常用方法
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.find_element_by_id('kw').clear()  # 清除文本
# driver.find_element_by_id('kw').send_keys('selenium')  # 模拟按键输入
# driver.find_element_by_id('su').click()  # 单击元素
#
# search_text = driver.find_element_by_id('kw')
# search_text.send_keys('selenium')
# search_text.submit()  # 模拟回车提交表单
#
# size = driver.find_element_by_id('kw').size  # 获得输入框的尺寸
# print(size)
# # text = driver.find_element_by_id("cp").text  # 获取元素文本；  返回百度页面底部备案信息,  异常
# # print(text)
# attribute = driver.find_element_by_id('kw').get_attribute('type')  # 返回元素的属性值，可以是id、name、type等
# print(attribute)
# result = driver.find_element_by_id('kw').is_displayed()  # 返回的元素结果是否可见，为true或false
# print(result)
# driver.quit()
#
#
# # 4.4 鼠标操作
# from selenium import webdriver
# from selenium.webdriver import ActionChains  # 引入鼠标操作的类
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.cn")
# above = driver.find_element_by_link_text("更多")  # 定位到要悬停的元素
# ActionChains(driver).move_to_element(above).perform()
# # move_to_element:鼠标悬停；
# # context_click():右击；
# # double_click():双击；
# # drag_and_drop():拖动；
# # perform：执行操作。
#
#
# # 4.5键盘操作
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys  # 导入键盘操作类
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.cn")
# driver.find_element_by_id('kw').send_keys('selenium')  # 在输入框中输入内容
# # sleep(2)
# # driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE) # 删除多输入的一个m
# # driver.find_element_by_id('kw').send_keys(Keys.SPACE)
# # driver.find_element_by_id('kw').send_keys('教程')  # 输入空格键+“教程”
# # driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')   # 输入组合键ctrl+a，全选输入框内容
# # # driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')   # 输入组合键ctrl+x，剪切输入框内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')   # 输入组合键ctrl+v，粘贴内容到输入框
# # driver.find_element_by_id('su').send_keys(Keys.ENTER)   # 用回车键代替单击操作
# sleep(4)
# driver.quit()
#
# # 4.6获得验证信息
# from time import sleep
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# print("Brfore search========")
# title = driver.title  # 打印当前页面title
# print(title)
# now_url = driver.current_url  # 打印当前页面URl
# print(now_url)
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()
# sleep(2)
# print('After search=========')
# title = driver.title  # 打印当前页面title
# print(title)
# now_url = driver.current_url  # 打印当前页面URl
# print(now_url)
# # num1 = driver.find_element_by_class_name('nums').text  # 获取当前页面文本信息
# # print(num1)
# driver.quit()
#
#
# # 4.7 设置元素等待,显示等待1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait  # 等待方法
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# element = WebDriverWait(driver,5,0.5).until(EC.visibility_of_element_located((By.ID, 'kw')))  # 显新等待
# element.send_keys('selenium')
# driver.quit()
#
# # 显示等待2
# from time import sleep, ctime
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# print(ctime())
# for i in range(10):
#     try:
#         el = driver.find_element_by_id('kw22')
#         if el.is_displayed():
#             break
#     except:
#         pass
#     sleep(1)
# else:
#     print("time out")
# print(ctime())
# driver.quit()
#
# # 隐式等待
# from time import ctime
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchAttributeException
#
# # driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)  # 设置隐式等待10s
# driver.get("http://www.baidu.com")
# try:
#     print(ctime())
#     driver.find_element_by_id('kw22').send_keys('selenium')
#     driver.find_element_by_id('kw').send_keys('selenium')
# except NoSuchAttributeException as e:
#     print(e)
# finally:
#     print(ctime())
#     driver.quit()
#
#
# 4.8定位一组元素与定位一个元素一样，在element后+s即可
# from time import sleep
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()
# sleep(2)
# texts = driver.find_elements_by_xpath("//div[@tpl='se_com_default']/h3/a")  # 定位一组元素
# print(len(texts))  # 计算匹配结果个数
# for t in texts:  # 循环遍历出每一条搜索结果的标题
#     print(t.text)
# driver.quit()
#
#
# # 4.9多表单切换
# from time import sleep
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http:www.126.com")
# sleep(2)
# login_frame = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
# driver.switch_to.frame(login_frame)
# driver.find_element_by_name("email").send_keys("username")
# driver.find_element_by_name("password").send_keys("password")
# driver.find_element_by_id("dologin").click()
# driver.switch_to.default_content()
# sleep(5)
# driver.quit()
#
#
# # 4.10多窗口切换
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("https://www.baidu.com")
# search_windows = driver.current_window_handle  # 获得百度搜索窗口句柄
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_link_text('立即注册').click()
# all_handles = driver.window_handles  # 获得当前所有打开的窗口句柄
# for handle in all_handles:  # 进入注册窗口
#     if handle != search_windows:
#         driver.switch_to.window(handle)
#         print(driver.title)
#         driver.find_element_by_name("username").send_keys('username')
#         driver.find_element_by_name('phone').send_keys('138xxxxxxx')
#         time.sleep(2)
#         driver.close()
# driver.switch_to.window(search_windows)  # 回到搜索窗口
# print(driver.title)
# driver.quit()
#
#
# # 4.11警告框处理
# from time import sleep
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# link = driver.find_element_by_link_text('设置').click()
# driver.find_element_by_link_text('搜索设置').click()
# sleep(2)
# driver.find_element_by_class_name("prefpanelgo").click()  # 保存设置
# alert = driver.switch_to.alert  # 获取警告框
# alert_text = alert.text  # 获取警告框提示信息
# print(alert_text)
# alert.accept()  # 接取警告框
# alert.dismiss()  # 解散现有警告框
# alert.send_keys('您好')  # 在警告框中输入文件，如果可以输入的话
# driver.quit()
#
#
# # 4.12下拉框处理
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.support.select import Select  # Select类处理下拉框
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# link = driver.find_element_by_link_text('更多').click()
# driver.find_element_by_link_text('搜索设置').click()
# sleep(2)
# sel = driver.find_elements_by_xpath("//select[@id='nr']")  # 搜索结果显示条数
# Select(sel).select_by_value('20')  # 通过value值定位下拉选项
# sleep(2)
# Select(sel).select_by_visible_text('每页显示50条')  # 通过text值定位下拉选项
# sleep(2)
# Select(sel).select_by_index(0)  # 通过索引定位下拉选项，第一个选项0，第二个1
# sleep(2)
# driver.quit()
#
#
# # 4.13上传文件
# import os
# from selenium import webdriver
#
# file_path = os.path.abspath('.//')
# print(file_path)
# driver = webdriver.Chrome()
# upload_page = 'file:///' + file_path + 'upfile.html'
# driver.get(upload_page)
# driver.find_elements_by_id('file').send_keys(file_path + 'test.txt')  # 定位上传按钮，添加本地文件
#
#
# # 4.14 下载文件，Firefox浏览器下载
# import os
# from selenium import webdriver
#
# fp = webdriver.FirefoxProfile()  # 实例化FirefoxProfile类
# fp.set_preference("browser.download.folderList", 2)  # browser.download.folderList：0，下载到默认路径；1下载到指定路径
# fp.set_preference("browser.download.dir", os.getcwd())  # browser.download.dir：指定下载文件目录；os.getcwd：获取当前文件的所在位置
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "binary/octet-stream")  # browser.helperApps.neverAsk.saveToDisk：下载文件类型；binary/octet-stream：二进制
# driver = webdriver.Firefox(firefox_profile = fp)
# driver.get("https://pypi.org/project/selenium/#files")
# driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()
#
# # Chrome浏览器下载
# import os
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# prefs = {'profile.default_content_settings.popups': 0,
#          'download.default_directory': os.getcwd()}  # profile.default_content_settings.popups：控制下载窗口弹窗，0，禁止；download.default_directory：下载路径
# options.add_experimental_option('prefs', prefs)
# driver = webdriver.Chrome(chrome_options = options)
# driver.get("https://pypi.org/project/selenium/#files")
# driver.find_element_by_partial_link_text('selenium-4.1.0.tar.gz').click()
#
#
# # 4.15操作cookie
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# cookie = driver.get_cookies()  # 获得所有cookie
# print(cookie)
# # driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbbbb'})  # 添加字典键值
# for cookie in driver.get_cookies():  # 遍历指定的cookies
#     print("%s  -> %s" %(cookie['name'], cookie['value']))
# print(driver.get_cookie('BD_HOME'))
# driver.quit()
# get_cookies():获得所有的cookie
# get_cookie(name):获得name的cookie
# add_cookie('x')：添加cookie
# delete_cookie(name, option)：删除名为option的cookie
# delete_all_cookies():删除所有cookie
#
#
# # 4.16调用JavaScript
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.set_window_size(800, 600)
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()

# js = "window.scrollTo(100, 450);"   # window.scrollTo（）：设置浏览器窗口滚动条的水平和垂直位置
# driver.execute_script(js)  # execute_script：执行操作
# text = "input text"
# js = "document.getElementById('id').value='" + text + "';"  # document.getElementById('id')：借助JavaScript代码输入文本信息
# driver.execute_script(js)
# driver.quit()
#
#
# # 4.17处理HTML5视频播放
# from time import sleep
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://videojs.com/")
# video = driver.find_element_by_id("preview-player_html5_api")
# url = driver.execute_script("return arguments[0].currentSrc;", video)  # 返回播放文件地址
# print(url)
# driver.execute_script("arguments[0].load()", video)  # 加载视频
# print("开始")
# driver.execute_script("arguments[0].play()", video)  # 播放视频
# sleep(15)
# print("停止")
# driver.execute_script("arguments[0].pause()", video)  # 停止视频
# driver.quit()
# JavaScript有个内置对象arguments，currentSrc返回当前音频/视频的url，未设置返空字符
# load：加载；play：播放；pause：暂停
#
#
# # 4.18滑动解锁，左右移动滑块
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.common.exceptions import UnexpectedAlertPresentException
#
# driver = webdriver.Chrome()
# driver.get("https://www.helloweba.com/demo/2017/unlock/")
# # 定位滑块
# slider = driver.find_element_by_class_name("slide-to-unlock-handle")[0]  # slide-to-unlock-handle：滑块
# action = ActionChains(driver)
# action.click_and_hold(slider).perform()  # click_and_hold：单击并按下鼠标左键
# for index in range(200):
#     try:
#         action.move_by_offset(2, 0).perform()  # move_by_offset：移动鼠标，x，y距离
#     except UnexpectedAlertPresentException:
#         break
#     action.reset_action()  # 重置action
#     sleep(0.1)  # 等待停顿时间
# # 打印警告框提示
# success_text = driver.switch_to.alert.text
# print(success_text)
# # slide-to-unlock-handle：滑块
# # slide-to-unlock-progress：滑过后的背景色
#
# # 上下滑动
# from time import sleep
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://www.jq22.com/yanshi4976")
# sleep(2)
# driver.switch_to.frame("iframe")
# driver.find_element_by_id("appDate").click()
# # 定位要滑动的年月日
# dwwos = driver.find_element_by_class_name('dwwo')
# year = dwwos[0]
# month = dwwos[1]
# day = dwwos[2]
# action = webdriver.TouchActions(driver)
# action.scroll_from_element(year, 0, 5).perform()
# action.scroll_from_element(month, 0, 30).perform()
# action.scroll_from_element(day, 0, 30).perform()
# driver.quit()
# TouchActions类中的scroll_from_element滑动元素，元素，x距离，y距离
#
#
# # 4.19窗口截图
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# driver.save_screenshot("./baidu_img.png")  # 截取当前窗口，指定截图图片的保存位置
# driver.quit()
# # save_screenshot:保存截图

# 4.20关闭窗口
# quit()：关闭所有窗口
# close():关闭某个窗口
